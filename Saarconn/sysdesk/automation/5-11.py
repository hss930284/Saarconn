# Standard library imports
import importlib
import os
import re
import openpyxl
from pathlib import Path

# Third-party library imports
import pandas as pd  # Import pandas

# Local module imports
import Utilities
import SystemDeskEnums  # type: ignore # pylint: disable=wrong-import-position

# Reloading modules
importlib.reload(Utilities)  # Reloading Utilities
importlib.reload(SystemDeskEnums)  # Reloading SystemDeskEnums

# Connecting to SystemDesk (get COM object)
SdApplication = Utilities.ConnectToSystemDesk()

def ReadUserDefinedExcel():
    # Load the user defined Excel file
    global Input_Excel_File, current_sheet, sheet_name
    Input_Excel_File = input("Please provide the path of input Excel file (e.g., E:\\sysdesk\\automation): ")

    # Referring xls variable as entire excel
    global xls
    xls = pd.ExcelFile(Input_Excel_File)

    global first_sheet
    first_sheet = pd.read_excel(Input_Excel_File, sheet_name=0,header=None)
    global sd_project
    sd_project = first_sheet.iloc[4,3] # Get the project name from cell D5

    for sheet_name in xls.sheet_names[1:]:  # This will skip the first sheet
        current_sheet = pd.read_excel(Input_Excel_File, sheet_name=sheet_name, header=None)


def GetColumnValidIndex(CellNo, NextTableCellValue):
    global column_index
    # Extract column and row from the cell reference
    column_letter = ''.join(filter(str.isalpha, CellNo))
    row_number = int(''.join(filter(str.isdigit, CellNo)))

    # Convert column letter to a zero-based index
    column_index = ord(column_letter) - ord('A')

    # Initialize c and d
    first_valid_cell_reference = CellNo  # c is the current cell
    last_valid_cell_reference = None  # d will be determined later

    # Check if row_number is within bounds
    if row_number >= current_sheet.shape[0]:
        print(f"Warning: Row number {row_number} exceeds the DataFrame size {current_sheet.shape[0]}.")
        return first_valid_cell_reference, last_valid_cell_reference

    # Start checking from the row of cell a
    for row in range(row_number - 1, current_sheet.shape[0]):  # Adjust for 0-based indexing
        if row >= current_sheet.shape[0]:
            print(f"Warning: Row index {row} exceeds the DataFrame size {current_sheet.shape[0]}.")
            break
        
        if column_index >= current_sheet.shape[1]:
            print(f"Warning: Column index {column_index} exceeds the DataFrame width {current_sheet.shape[1]}.")
            break

        current_cell_value = current_sheet.iat[row, column_index]

        # Check for empty cell
        if pd.isna(current_cell_value):
            # Check the next cell
            next_cell_value = current_sheet.iat[row + 1, column_index] if row + 1 < current_sheet.shape[0] else None
            
            if next_cell_value == NextTableCellValue:
                # Assign d to the cell above the empty cell
                last_valid_cell_reference = f"{column_letter}{row}"  # Adjust for 1-indexing
                # last_valid_cell_reference = f"{column_letter}{row + 1}"  # Adjust for 1-indexing
                break
        
    return first_valid_cell_reference, last_valid_cell_reference


def ProjectConfig():
    """
    #####################################
    Configuring project
    #####################################
    """
    # Global configuration options (shared with Utilities).
    global Options
    Options = Utilities.Options

    # Name of this project.
    Options.ProjectName = sd_project   # < %%%--- Change this to your project name.%%%

    # Set True to open an existing SystemDesk project (SDP). Otherwise, the SystemDesk project is created from scratch.
    Options.OpenExistingProject = False

    # Name of the AUTOSAR system.
    Options.SystemName = "System"

    # Set True to create a separate ECUs for the front-left- and front-right-indicators.
    Options.UseFrontIndicatorEcus = True

    # Set True to create SWC implementations with this script. Otherwise they can be imported from TargetLink.
    Options.CreateImplementations = True

    # Set True to import the network communication (Fibex) elements from a AUTOSAR System Description file.
    Options.ImportNetworkCommunicationElements = True

    # Set True to generate code for all ECU BSW modules including RTE.
    Options.GenerateCode = True

    # Set True if the SYD_MOD license for SystemDesk is available.
    Options.License_SYD_MOD = True

    # Set True to build an Offline Simulation Application for VEOS.
    Options.BuildForVeos = True

    # Set True to save the SystemDesk project when this script at the end of lesson 14.
    Options.SaveProject = True

def CreateProjectAndPackages():
    """
    Creates a new package for software components and compositions.
    """
    Utilities.CreateProject()
    SdProject = SdApplication.ActiveProject
    applRootDir = r"<InstallationDir>"

    # List of template files to be imported.
    templateFiles = [os.path.join(applRootDir, r"Templates\FolderStructure.arxml")]

    # Now import the files.
    Utilities.ImportAutosarFilesAtProject(templateFiles)

    print("Function CreateProjectAndPackages executed")

def CleanupProjectAndPackages():
    """
    Removes unnecessary elements which have been imported from the template files.
    """
    # Get existing project elements.
    rootPackage = SdApplication.ActiveProject.RootAutosar
    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    # Delete packages MySwc and MyComposition, which were imported from
    # template "PackageStructure.arxml".
    mySwc = swComponentTypesPackage.ArPackages.Item("MySwc")
    if mySwc is not None:
        mySwc.Delete()
    myComposition = swComponentTypesPackage.ArPackages.Item("MyComposition")
    if myComposition is not None:
        myComposition.Delete()

def CreateSwcs():
    global rootPackage, value_d3
    rootPackage = SdApplication.ActiveProject.RootAutosar
    value_d3 = current_sheet.iloc[2, 3]  # D3 corresponds to row 2, column 3

    if value_d3 == 'ApplicationSwComponentType':
        ApplicationSwComponentType()
    elif value_d3 == 'ComplexDeviceDriverSwComponentType':
        ComplexDeviceDriverSwComponentType()
    elif value_d3 == 'EcuAbstractionSwComponentType':
        EcuAbstractionSwComponentType()
    elif value_d3 == 'NvBlockSwComponentType':
        NvBlockSwComponentType()
    elif value_d3 == 'ParameterSwComponentType':
        ParameterSwComponentType()
    elif value_d3 == 'SensorActuatorSwComponentType':
        SensorActuatorSwComponentType()
    elif value_d3 == 'ServiceProxySwComponentType':
        ServiceProxySwComponentType()
    elif value_d3 == 'ServiceSwComponentType':
        ServiceSwComponentType()
    else:
        print(f"In sheet '{sheet_name}', Please provide correct software component type")

def ApplicationSwComponentType():
    global CurrentswComponentTypesPackage, CurrentApplSWCPkg, CurrentSWC, CurrentInternalBehaviors, CurrentRunnable

    CurrentswComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")
    CurrentApplSWCPkg = CurrentswComponentTypesPackage.ArPackages.Item("ApplSWC")
    CurrentSWC = CurrentApplSWCPkg.Elements.AddNewApplicationSwComponentType(current_sheet.iloc[2, 2])
    CurrentInternalBehaviors = CurrentSWC.InternalBehaviors.AddNew(current_sheet.iloc[2, 4])

    first_runnable, last_runnable = GetColumnValidIndex('F3', 'Interface Type')
    print(f"First runnable: {first_runnable}, Last runnable: {last_runnable}")

    if first_runnable and last_runnable:
        first_row_index = int(first_runnable[1:]) - 1
        last_row_index = int(last_runnable[1:]) - 1

        for row_index in range(first_row_index, last_row_index + 1):
            if row_index >= current_sheet.shape[0]:
                print(f"Warning: Row index {row_index} is out of bounds. Skipping.")
                continue

            runnable_name = current_sheet.iloc[row_index, column_index]
            if pd.isna(runnable_name):
                print(f"Warning: Empty runnable name at row {row_index + 1}. Skipping.")
                continue

            CurrentRunnable = CurrentInternalBehaviors.Runnables.AddNew(str(runnable_name))
            CurrentRunnable.MinimumStartInterval = 0.0
            CurrentRunnable.CanBeInvokedConcurrently = False
            CurrentRunnable.Symbol = CurrentRunnable.ShortName
            createrteevent(row_index, column_index)

#########################################################################################################################################
             ###########-------------------------------ComplexDeviceDriverSwComponentType-------------------------------############
#########################################################################################################################################   
def ComplexDeviceDriverSwComponentType():
    global swComponentTypesPackage, CddSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    CddSWC= swComponentTypesPackage.ArPackages.Item("CddSWC")
   
    CurrentSWC = CddSWC.Elements.AddNewComplexDeviceDriverSwComponentType(current_sheet.iloc[2,2])

#########################################################################################################################################
             ###########-------------------------------EcuAbstractionSwComponentType-------------------------------############
#########################################################################################################################################
def EcuAbstractionSwComponentType():
    global swComponentTypesPackage, EcuAbSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    EcuAbSWC= swComponentTypesPackage.ArPackages.Item("EcuAbSWC")
   
    CurrentSWC = EcuAbSWC.Elements.AddNewEcuAbstractionSwComponentType(current_sheet.iloc[2,2])

#########################################################################################################################################
             ###########-------------------------------NvBlockSwComponentType-------------------------------############
#########################################################################################################################################
def NvBlockSwComponentType():
    global swComponentTypesPackage, NvDataSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    NvDataSWC= swComponentTypesPackage.ArPackages.Item("NvDataSWC")
   
    CurrentSWC = NvDataSWC.Elements.AddNewNvBlockSwComponentType(current_sheet.iloc[2,2])

#########################################################################################################################################
             ###########-------------------------------ParameterSwComponentType-------------------------------############
#########################################################################################################################################
def ParameterSwComponentType():
    global swComponentTypesPackage, PrmSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    PrmSWC= swComponentTypesPackage.ArPackages.Item("PrmSWC")
   
    CurrentSWC = PrmSWC.Elements.AddNewParameterSwComponentType(current_sheet.iloc[2,2])

#########################################################################################################################################
             ###########-------------------------------SensorActuatorSwComponentType-------------------------------############
#########################################################################################################################################
def SensorActuatorSwComponentType():
    global swComponentTypesPackage, SnsrActSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    SnsrActSWC= swComponentTypesPackage.ArPackages.Item("SnsrActSWC")
   
    CurrentSWC = SnsrActSWC.Elements.AddNewSensorActuatorSwComponentType(current_sheet.iloc[2,2])

#########################################################################################################################################
             ###########-------------------------------ServiceProxySwComponentType-------------------------------############
#########################################################################################################################################
def ServiceProxySwComponentType():
    global swComponentTypesPackage, SrvcPrxySWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    SrvcPrxySWC= swComponentTypesPackage.ArPackages.Item("SrvcPrxySWC")
   
    CurrentSWC = SrvcPrxySWC.Elements.AddNewServiceProxySwComponentType(current_sheet.iloc[2,2])

#########################################################################################################################################
             ###########--------------------------------------ServiceSwComponentType---------------------------------------############
#########################################################################################################################################
def ServiceSwComponentType():
    global swComponentTypesPackage, SrvcSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    SrvcSWC= swComponentTypesPackage.ArPackages.Item("SrvcSWC")
   
    CurrentSWC = SrvcSWC.Elements.AddNewServiceSwComponentType(current_sheet.iloc[2,2])



def createrteevent(row_index, Actual_CellNo_Colomn):
    a = row_index
    b = Actual_CellNo_Colomn + 2
    c = Actual_CellNo_Colomn + 1

    if a < current_sheet.shape[0] and b < current_sheet.shape[1]:
        cell_value = current_sheet.iloc[a, b]

        if cell_value == 'AsynchronousServerCallReturnsEvent':
            AsynchronousServerCallReturnsEvent(a, c)
        elif cell_value == 'InitEvent':
            InitEvent(a, c)
        elif cell_value == 'TimingEvent':
            TimingEvent(a, c)
        else:
            print(f"In sheet '{sheet_name}', Unrecognized event type: {cell_value}")
    else:
        print(f"Warning: Indices ({a}, {b}) are out of bounds for the DataFrame.")

# Define other functions (InitEvent, TimingEvent, etc.) here...

def InitEvent(CurrentRteEvent,currenteventcell):
    CurrentEvent = CurrentInternalBehaviors.Events.AddNewInitEvent(current_sheet.iloc[CurrentRteEvent,currenteventcell])
    # Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    CurrentEvent.StartOnEventRef = CurrentRunnable

def TimingEvent(CurrentRteEvent,currenteventcell):
    CurrentEvent = CurrentInternalBehaviors.Events.AddNewTimingEvent(current_sheet.iloc[CurrentRteEvent,currenteventcell])
    # Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    CurrentEvent.Period = 0.01
    CurrentEvent.StartOnEventRef = CurrentRunnable

def AsynchronousServerCallReturnsEvent(CurrentRteEvent,currenteventcell):
    CurrentEvent = CurrentInternalBehaviors.Events.AddNewInitEvent(current_sheet.iloc[CurrentRteEvent,currenteventcell])
    # Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    CurrentEvent.StartOnEventRef = CurrentRunnable

def BackgroundEvent(CurrentRteEvent,currenteventcell):
    CurrentEvent = CurrentInternalBehaviors.Events.AddNewInitEvent(current_sheet.iloc[CurrentRteEvent,currenteventcell])
    # Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    CurrentEvent.StartOnEventRef = CurrentRunnable



def Main():
    ReadUserDefinedExcel()
    ProjectConfig()
    CreateProjectAndPackages()
    CleanupProjectAndPackages()
    CreateSwcs()
    

if __name__ == "__main__":
    Main()
    print("Ready")