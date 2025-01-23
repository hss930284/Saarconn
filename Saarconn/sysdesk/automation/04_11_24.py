#importing required modules

import importlib
import os
import Utilities
from pathlib import Path
import pandas as pd  # Import pandas
importlib.reload(Utilities) # reloading Utilities
SdApplication = Utilities.ConnectToSystemDesk() # Connect to SystemDesk (get COM object)
import SystemDeskEnums  # type: ignore # pylint: disable=wrong-import-position
importlib.reload(SystemDeskEnums)
import re

def ReadUserDefinedExcel():
    # Load the user defined Excel file
    global Input_Excel_File
    Input_Excel_File = input("Please select the input Excel file (e.g., E:\\sysdesk\\automation): ")
    # referring xls variable as entire excel
    global xls
    xls = pd.ExcelFile(Input_Excel_File)
    # Read the first sheet
    global first_sheet
    first_sheet = pd.read_excel(Input_Excel_File, sheet_name=0,header=None)
    global sd_project
    sd_project = first_sheet.iloc[4,3] # Get the project name from cell D5

def GetColumnValidIndex(CellNo, NextTableCellValue):
    ActualValidCellNo = None

    def string_to_number(s):
        num = 0
        length = len(s)
        s = s.lower()

        for i, char in enumerate(s):
            value = ord(char) - ord('a')
            num += value * (26 ** (length - i - 1))

        return num

    def number_to_string(num):
        """Convert a 0-based index to an Excel-style column letter (A, B, C, ..., Z, AA, AB, ...)."""
        letters = []
        while num >= 0:
            letters.append(chr((num % 26) + ord('A')))
            num = num // 26 - 1
        return ''.join(reversed(letters))

    match = re.match(r"([a-zA-Z]+)(\d+)", CellNo)
    if match:
        global CellNo_Colomn,CellNo_Row,Actual_CellNo_Colomn
        CellNo_Colomn = match.group(1)  # Alphabetical part
        CellNo_Row = match.group(2)  # Numerical part
    else:
        print("The input does not match the expected format.") #error handling
        return None  # Return None or handle as needed

    Actual_CellNo_Colomn = string_to_number(CellNo_Colomn)
    Actual_CellNo_Row = int(CellNo_Row) - 1

    # Store values in a list to keep track
    values = []
    
    first_valid_cell_reference = None
    last_valid_cell_reference = None
    
    # Start searching from the specified row and column index
    for index in range(Actual_CellNo_Row, len(current_df)):
        cell_value = current_df.iloc[index, Actual_CellNo_Colomn]
        
        if pd.isna(cell_value):  # Check if the cell is empty (NaN)
            # Check if the next row exists
            if index + 1 < len(current_df):
                next_cell_value = current_df.iloc[index + 1, Actual_CellNo_Colomn]
                if next_cell_value == NextTableCellValue:
                    break  # Stop processing when the next cell matches "NextTableCellValue"
            continue  # Continue to the next iteration if the current cell is NaN
        else:
            values.append(cell_value)  # Collect valid cell values
            
            # Create the Excel-style cell reference
            current_cell_reference = number_to_string(Actual_CellNo_Colomn) + str(index + 1)
            # print(f"Current Cell - Reference: {current_cell_reference} - Value: {cell_value}")
            
            # Track the first valid cell reference
            if first_valid_cell_reference is None:
                first_valid_cell_reference = current_cell_reference
            
            # Update the last valid cell reference
            last_valid_cell_reference = current_cell_reference
    
    # Print or return the collected values if needed
    # print("Collected values:", values)
    global storedvariable
    storedvariable = values
    # print(f"storedvariable: {storedvariable}")
    
    # Print first and last valid cell references
    if first_valid_cell_reference is not None and last_valid_cell_reference is not None:
      
    
        global firstvalueCell ,lastvaluecell
        firstvalueCell= first_valid_cell_reference
        lastvaluecell = last_valid_cell_reference
        # print(f"First Valid Cell: {firstvalueCell} ")
        # print(f"Last Valid Cell: {lastvaluecell} ")
        
    ActualValidCellNo = len(values)  # or return values, or index as needed

    return ActualValidCellNo
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

def CreateProjectAndPackages():#need to revisit  this function and compare with utility function

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

    # Package "Communication" is not needed if the whole IndicatorSystem is
    # implemented on only one ECU.
    # if not Options.UseFrontIndicatorEcus:
    #     communicationPackage = SdProject.RootAutosar.ArPackages.Item("Communication")
    #     if communicationPackage != None:
    #         communicationPackage.Delete()
    # return "Function CreateProjectAndPackages executed"

    print("Function CreateProjectAndPackages executed") #error handling

def CleanupProjectAndPackages(): #not necessary at this moment, will include this  in the next version

    """
    Removes unnecessary elements which have been imported from the template files.
    """

    # Get existing project elements.
    rootPackage = SdApplication.ActiveProject.RootAutosar
    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    # Delete packages MySwc and MyComposition, which were imported from
    # template "PackageStructure.arxml".
    mySwc = swComponentTypesPackage.ArPackages.Item("MySwc")
    if mySwc != None:
        mySwc.Delete()
    myComposition = swComponentTypesPackage.ArPackages.Item("MyComposition")
    if myComposition != None:
        myComposition.Delete()

    # return "Function CleanupProjectAndPackages executed"

def CreateSwcs():
    global rootPackage,current_df,value_d3,sheet_name
    rootPackage = SdApplication.ActiveProject.RootAutosar
    for sheet_name in xls.sheet_names[1:]:  # This will skip the first sheet #move this excel part to perticular section of this code
        current_df = pd.read_excel(xls, sheet_name=sheet_name,header=None)
        # Get the value from cell D3 (row index 2, column index 3)
        value_d3 = current_df.iloc[2,3]  # D3 corresponds to row 2, column 3

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
            print(f"In sheet '{sheet_name}', Please provide correct software component type")  #error handling


#########################################################################################################################################
             ###########-------------------------------ApplicationSwComponentType-------------------------------############
#########################################################################################################################################
def ApplicationSwComponentType():
    global CurrentswComponentTypesPackage, CurrentApplSWCPkg, CurrentSWC, CurrentInternalBehaviors, CurrentRunnable, CurrentEvent

    CurrentswComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    CurrentApplSWCPkg= CurrentswComponentTypesPackage.ArPackages.Item("ApplSWC") # use this method >>ilSwcType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IndicatorLogic")
   
    CurrentSWC = CurrentApplSWCPkg.Elements.AddNewApplicationSwComponentType(current_df.iloc[2,2])

    CurrentInternalBehaviors = CurrentSWC.InternalBehaviors.AddNew(current_df.iloc[2,4])

    GetColumnValidIndex("f3", "Interface Type")
    
    # for runnable_name in storedvariable:  # Assuming 'values' contains the names for the runnables
    #     CurrentRunnable = CurrentInternalBehaviors.Runnables.AddNew(runnable_name)
    #     CurrentRunnable.MinimumStartInterval = 0.0
    #     CurrentRunnable.CanBeInvokedConcurrently = False
    #     CurrentRunnable.Symbol = CurrentRunnable.ShortName
    #     # Utilities.SetDescription(tssPreRun, "Performs preprocessing of TurnSwitchSensor signals.")

    # Assuming firstvalueCell and lastvaluecell are in the format like 'F3' and 'F10'
    first_row_index = int(firstvalueCell[1:]) - 1  # Convert from Excel row (1-based) to Python index (0-based)
    last_row_index = int(lastvaluecell[1:]) - 1  # Convert from Excel row (1-based) to Python index (0-based)

    # Iterate over the range from first_row_index to last_row_index
    for row_index in range(first_row_index, last_row_index + 1):  # +1 to include the last row
        runnable_name = current_df.iloc[row_index, Actual_CellNo_Colomn]  # Get the runnable name from the current row
        print(runnable_name,row_index,Actual_CellNo_Colomn)
        CurrentRunnable = CurrentInternalBehaviors.Runnables.AddNew(runnable_name)
        CurrentRunnable.MinimumStartInterval = 0.0
        CurrentRunnable.CanBeInvokedConcurrently = False
        CurrentRunnable.Symbol = CurrentRunnable.ShortName
        createrteevent(row_index,Actual_CellNo_Colomn)


    # createrteevent()
    

# createrteevent() same as createswc() get enum list from the picture

def InitEvent(CurrentRteEvent,currenteventcell):
    CurrentEvent = CurrentInternalBehaviors.Events.AddNewInitEvent(current_df.iloc[CurrentRteEvent,currenteventcell])
    # Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    CurrentEvent.StartOnEventRef = CurrentRunnable

def TimingEvent(CurrentRteEvent,currenteventcell):
    CurrentEvent = CurrentInternalBehaviors.Events.AddNewTimingEvent(current_df.iloc[CurrentRteEvent,currenteventcell])
    # Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    CurrentEvent.Period = 0.01
    CurrentEvent.StartOnEventRef = CurrentRunnable

def AsynchronousServerCallReturnsEvent(CurrentRteEvent,currenteventcell):
    CurrentEvent = CurrentInternalBehaviors.Events.AddNewInitEvent(current_df.iloc[CurrentRteEvent,currenteventcell])
    # Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    CurrentEvent.StartOnEventRef = CurrentRunnable

def BackgroundEvent(CurrentRteEvent,currenteventcell):
    CurrentEvent = CurrentInternalBehaviors.Events.AddNewInitEvent(current_df.iloc[CurrentRteEvent,currenteventcell])
    # Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    CurrentEvent.StartOnEventRef = CurrentRunnable


def createrteevent(row_index,Actual_CellNo_Colomn):
    a=row_index
    b=Actual_CellNo_Colomn+2
    c=Actual_CellNo_Colomn+1

    cell_value = current_df.iloc[a, b]

    print(cell_value)

    if cell_value == 'AsynchronousServerCallReturnsEvent':
        AsynchronousServerCallReturnsEvent(a,c)
    elif cell_value == 'InitEvent':
        InitEvent(a,c)
    elif cell_value == 'TimingEvent':
        TimingEvent(a,c)
    else:
        print(f"In sheet '{sheet_name}', Please provide correct software component type")

#########################################################################################################################################
             ###########-------------------------------ComplexDeviceDriverSwComponentType-------------------------------############
#########################################################################################################################################   
def ComplexDeviceDriverSwComponentType():
    global swComponentTypesPackage, CddSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    CddSWC= swComponentTypesPackage.ArPackages.Item("CddSWC")
   
    CurrentSWC = CddSWC.Elements.AddNewComplexDeviceDriverSwComponentType(current_df.iloc[2,2])

#########################################################################################################################################
             ###########-------------------------------EcuAbstractionSwComponentType-------------------------------############
#########################################################################################################################################
def EcuAbstractionSwComponentType():
    global swComponentTypesPackage, EcuAbSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    EcuAbSWC= swComponentTypesPackage.ArPackages.Item("EcuAbSWC")
   
    CurrentSWC = EcuAbSWC.Elements.AddNewEcuAbstractionSwComponentType(current_df.iloc[2,2])

#########################################################################################################################################
             ###########-------------------------------NvBlockSwComponentType-------------------------------############
#########################################################################################################################################
def NvBlockSwComponentType():
    global swComponentTypesPackage, NvDataSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    NvDataSWC= swComponentTypesPackage.ArPackages.Item("NvDataSWC")
   
    CurrentSWC = NvDataSWC.Elements.AddNewNvBlockSwComponentType(current_df.iloc[2,2])

#########################################################################################################################################
             ###########-------------------------------ParameterSwComponentType-------------------------------############
#########################################################################################################################################
def ParameterSwComponentType():
    global swComponentTypesPackage, PrmSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    PrmSWC= swComponentTypesPackage.ArPackages.Item("PrmSWC")
   
    CurrentSWC = PrmSWC.Elements.AddNewParameterSwComponentType(current_df.iloc[2,2])

#########################################################################################################################################
             ###########-------------------------------SensorActuatorSwComponentType-------------------------------############
#########################################################################################################################################
def SensorActuatorSwComponentType():
    global swComponentTypesPackage, SnsrActSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    SnsrActSWC= swComponentTypesPackage.ArPackages.Item("SnsrActSWC")
   
    CurrentSWC = SnsrActSWC.Elements.AddNewSensorActuatorSwComponentType(current_df.iloc[2,2])

#########################################################################################################################################
             ###########-------------------------------ServiceProxySwComponentType-------------------------------############
#########################################################################################################################################
def ServiceProxySwComponentType():
    global swComponentTypesPackage, SrvcPrxySWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    SrvcPrxySWC= swComponentTypesPackage.ArPackages.Item("SrvcPrxySWC")
   
    CurrentSWC = SrvcPrxySWC.Elements.AddNewServiceProxySwComponentType(current_df.iloc[2,2])

#########################################################################################################################################
             ###########--------------------------------------ServiceSwComponentType---------------------------------------############
#########################################################################################################################################
def ServiceSwComponentType():
    global swComponentTypesPackage, SrvcSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    SrvcSWC= swComponentTypesPackage.ArPackages.Item("SrvcSWC")
   
    CurrentSWC = SrvcSWC.Elements.AddNewServiceSwComponentType(current_df.iloc[2,2])








    # swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")
    # mySwc = swComponentTypesPackage.ArPackages.Item("MySwc")
    # myApplicationSw = mySwc.ArComponents.Item("MyApplicationSw")
    # myApplicationSw.Delete()
    # myApplicationSw = mySwc.ArComponents.Item("MyApplicationSw")
    # myApplicationSw.Create()
    # myApplicationSw.Name = "MyApplicationSw"
    # myApplicationSw.Description = "MyApplicationSw Description"
    # myApplicationSw.Category = "Application"
    # myApplicationSw.Type = "ApplicationSwComponentType"
    # myApplicationSw.SwComponentType = "ApplicationSwComponentType"
    



def ProjectSave():
    # SdApplication.ActiveProject.Save() #try this function later
    # SdApplication.ActiveProject.SaveAs(r"<SavePath>")
    # print("Function ProjectSave executed")
    
    # # Save the SystemDesk project.
    if Options.SaveProject: 
        # Constructing the project file name
        project_file_name = f"{Options.ProjectName}.sdp"  
        
        
        user_defined_path = input("Please give the path where you want to save the project (e.g., E:\\sysdesk\\automation): ")
        
        # Check if the provided path exists
        if not os.path.exists(user_defined_path):
            print("Invalid path....!!!!") #error handling
            user_defined_path = input("Please give the appropraite path where you want to save the project (e.g., E:\\sysdesk\\automation): ")
            return  
        
        # full project file path
        project_file_path = os.path.join(user_defined_path, project_file_name)
        
        # Save the project to the specified path
        Utilities.SaveProject(project_file_path)  
        print(f"*** Saving project as '{project_file_name}' to '{project_file_path}'. ***")  #error handling
    else: 
        print("*** Project not saved. ***")  #error handling

def Main():
    ReadUserDefinedExcel()
    ProjectConfig()
    CreateProjectAndPackages()
    CleanupProjectAndPackages()
    CreateSwcs()
    ProjectSave()

#-------------
# Run the demo
#-------------
if (__name__ == "__main__"):
    Main()
    print("Ready")  #error handling



