# Standard library imports
import importlib
import os
import warnings
from pathlib import Path

# Suppress warnings from openpyxl
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

# Third-party library imports
import pandas as pd
import openpyxl

# Local module imports
import Utilities
import SystemDeskEnums  # type: ignore

# Reloading modules
importlib.reload(Utilities)
importlib.reload(SystemDeskEnums)

# Connecting to SystemDesk (get COM object)
SdApplication = Utilities.ConnectToSystemDesk()

#####################################
# Excel-related functions
#####################################

def ReadUserDefinedExcel():
    """
    Reads the user-provided Excel file and loads the required data into global variables.
    """
    global Input_Excel_File, xls, first_sheet, sd_project, current_sheet, sheet_name

    Input_Excel_File = input("Please provide the path of input Excel file (e.g., E:\\sysdesk\\automation): ")
    workbook = openpyxl.load_workbook(Input_Excel_File, data_only=True)
    xls = pd.ExcelFile(Input_Excel_File)

    # Load the first sheet to extract project information
    first_sheet = pd.read_excel(Input_Excel_File, sheet_name=0, header=None)
    sd_project = first_sheet.iloc[3, 2]  # Get project name from cell D5

    # Load subsequent sheets
    for sheet_name in xls.sheet_names[1:]:
        current_sheet = pd.read_excel(Input_Excel_File, sheet_name=sheet_name, header=None)

#####################################
# Project Configuration Functions
#####################################

def ProjectConfig():
    """
    Configures the project with predefined settings.
    """
    global Options
    Options = Utilities.Options

    Options.ProjectName = sd_project
    Options.OpenExistingProject = False
    Options.SystemName = "System"
    Options.UseFrontIndicatorEcus = True
    Options.CreateImplementations = True
    Options.ImportNetworkCommunicationElements = True
    Options.GenerateCode = True
    Options.License_SYD_MOD = True
    Options.BuildForVeos = True
    Options.SaveProject = True

def CreateProjectAndPackages():
    """
    Creates a new project and imports predefined packages.
    """
    Utilities.CreateProject()
    applRootDir = r"<InstallationDir>"
    templateFiles = [os.path.join(applRootDir, r"Templates\FolderStructure.arxml")]
    Utilities.ImportAutosarFilesAtProject(templateFiles)

def CleanupProjectAndPackages():
    """
    Removes unnecessary elements imported from template files.
    """
    rootPackage = SdApplication.ActiveProject.RootAutosar
    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    # Delete unnecessary packages
    for pkg_name in ["MySwc", "MyComposition"]:
        pkg = swComponentTypesPackage.ArPackages.Item(pkg_name)
        if pkg is not None:
            pkg.Delete()

#####################################
# SWC Creation Functions
#####################################

def GetDataFromSheetByHeader(header_name, sheet_name="SWC_Info"):
    """
    Retrieves column values based on header name from a specific Excel sheet.

    Args:
        header_name (str): The name of the column to retrieve.
        sheet_name (str): The name of the Excel sheet.

    Returns:
        list: Column data as a list, or None if an error occurs.
    """
    try:
        df = pd.read_excel(Input_Excel_File, sheet_name=sheet_name, header=1)
        df.columns = df.columns.str.strip()  # Normalize headers
        if header_name not in df.columns:
            raise ValueError(f"Header '{header_name}' not found in sheet '{sheet_name}'.")
        return df[header_name].tolist()
    except Exception as e:
        print(f"Error in GetDataFromSheetByHeader: {e}")
        return None

def CreateSwcs():
    """
    Creates Software Components (SWCs) based on data from the SWC_Info sheet.
    """
    global rootPackage
    rootPackage = SdApplication.ActiveProject.RootAutosar

    swc_info_df = pd.read_excel(Input_Excel_File, sheet_name="SWC_Info", header=0)
    swc_info_df.columns = swc_info_df.columns.str.strip()  # Normalize headers

    if "SWC Type" not in swc_info_df.columns:
        print("Error: Column 'SWC Type' not found in SWC_Info sheet.")
        return

    swc_info_df["SWC Type"] = swc_info_df["SWC Type"].astype(str).str.strip()
    valid_swcs = swc_info_df[swc_info_df["SWC Type"].notna() & (swc_info_df["SWC Type"] != "") ]

    for index, row in valid_swcs.iterrows():
        swc_type = row["SWC Type"]
        
        # Retrieve all runnable names for the current SWC
        runnable_names = swc_info_df["Runnable Name"].tolist()
        
        if swc_type == 'ApplicationSwComponentType':
            ApplicationSwComponentType(row, runnable_names) 
        elif swc_type == 'ComplexDeviceDriverSwComponentType':
            ComplexDeviceDriverSwComponentType(row, runnable_names)
        elif swc_type == 'EcuAbstractionSwComponentType':
            EcuAbstractionSwComponentType(row, runnable_names)
        elif swc_type == 'NvBlockSwComponentType':
            NvBlockSwComponentType(row, runnable_names)
        elif swc_type == 'ParameterSwComponentType':
            ParameterSwComponentType(row, runnable_names)
        elif swc_type == 'SensorActuatorSwComponentType':
            SensorActuatorSwComponentType(row, runnable_names)
        elif swc_type == 'ServiceProxySwComponentType':
            ServiceProxySwComponentType(row, runnable_names)
        elif swc_type == 'ServiceSwComponentType':
            ServiceSwComponentType(row, runnable_names)
        else:
            print(f"In sheet '{sheet_name}', Please provide correct software component type")    

def ApplicationSwComponentType(row, runnable_names):
    """
    Creates an Application Software Component Type.
    """
    global CurrentswComponentTypesPackage, CurrentApplSWCPkg, CurrentSWC, CurrentInternalBehaviors

    CurrentswComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")
    CurrentApplSWCPkg = CurrentswComponentTypesPackage.ArPackages.Item("ApplSWC")

    software_component_name = row["Software Component Name"]
    internal_behavior_name = row["Internal Behavior Name"]
    symbol_behavior_name = row["SWC Symbol"]
    Handle_Termination_And_Restart = row["handleTerminationAndRestart"]
    Supports_Multiple_Instantiation = row["supportsMultipleInstantiation"]

    CurrentSWC = CurrentApplSWCPkg.Elements.AddNewApplicationSwComponentType(software_component_name)
    CurrentInternalBehaviors = CurrentSWC.InternalBehaviors.AddNew(internal_behavior_name)
    CurrentSWC.Symbol = symbol_behavior_name

    if Handle_Termination_And_Restart == 'noSupport':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.NoSupport
    elif Handle_Termination_And_Restart == 'canBeTerminated':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminated
    elif Handle_Termination_And_Restart == 'canBeTerminatedAndRestarted':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminatedAndRestarted
    else:
        raise ValueError(f"Unexpected value for handleTerminationAndRestart: {Handle_Termination_And_Restart}")

    CurrentInternalBehaviors.SupportsMultipleInstantiation = Supports_Multiple_Instantiation

    # Iterate over all runnable names and create them
    for runnable_name in runnable_names:
        Runnable_Symbol = row["Runnable Symbol"]
        can_Be_Invoked_Concurrently = row["canBeInvokedConcurrently"]

        CurrentRunnable = CurrentInternalBehaviors.Runnables.AddNew(str(runnable_name))
        CurrentRunnable.MinimumStartInterval = 0.0
        CurrentRunnable.CanBeInvokedConcurrently = can_Be_Invoked_Concurrently
        CurrentRunnable.Symbol = Runnable_Symbol

def ComplexDeviceDriverSwComponentType(row, runnable_names):
    """
    Creates a Complex Device Driver Software Component.
    """
    global swComponentTypesPackage, CddSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")
    CddSWC = swComponentTypesPackage.ArPackages.Item("CddSWC")

    software_component_name = row["Software Component Name"]
    internal_behavior_name = row["Internal Behavior Name"]
    symbol_behavior_name = row["SWC Symbol"]
    Handle_Termination_And_Restart = row["handleTerminationAndRestart"]
    Supports_Multiple_Instantiation = row["supportsMultipleInstantiation"]

    CurrentSWC = CddSWC.Elements.AddNewComplexDeviceDriverSwComponentType(software_component_name)
    CurrentInternalBehaviors = CurrentSWC.InternalBehaviors.AddNew(internal_behavior_name)
    CurrentSWC.Symbol = symbol_behavior_name

    if Handle_Termination_And_Restart == 'noSupport':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.NoSupport
    elif Handle_Termination_And_Restart == 'canBeTerminated':
        
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminated
    elif Handle_Termination_And_Restart == 'canBeTerminatedAndRestarted':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminatedAndRestarted
    else:
        raise ValueError(f"Unexpected value for handleTerminationAndRestart: {Handle_Termination_And_Restart}")

    CurrentInternalBehaviors.SupportsMultipleInstantiation = Supports_Multiple_Instantiation

    # Iterate over all runnable names and create them
    for runnable_name in runnable_names:
        Runnable_Symbol = row["Runnable Symbol"]
        can_Be_Invoked_Concurrently = row["canBeInvokedConcurrently"]

        CurrentRunnable = CurrentInternalBehaviors.Runnables.AddNew(str(runnable_name))
        CurrentRunnable.MinimumStartInterval = 0.0
        CurrentRunnable.CanBeInvokedConcurrently = can_Be_Invoked_Concurrently
        CurrentRunnable.Symbol = Runnable_Symbol

def EcuAbstractionSwComponentType(row, runnable_names):
    global swComponentTypesPackage, EcuAbSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")
    EcuAbSWC = swComponentTypesPackage.ArPackages.Item("EcuAbSWC")

    software_component_name = row["Software Component Name"]
    internal_behavior_name = row["Internal Behavior Name"]
    symbol_behavior_name = row["SWC Symbol"]
    Handle_Termination_And_Restart = row["handleTerminationAndRestart"]
    Supports_Multiple_Instantiation = row["supportsMultipleInstantiation"]

    CurrentSWC = EcuAbSWC.Elements.AddNewEcuAbstractionSwComponentType(software_component_name)
    CurrentInternalBehaviors = CurrentSWC.InternalBehaviors.AddNew(internal_behavior_name)
    CurrentSWC.Symbol = symbol_behavior_name

    if Handle_Termination_And_Restart == 'noSupport':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.NoSupport
    elif Handle_Termination_And_Restart == 'canBeTerminated':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminated
    elif Handle_Termination_And_Restart == 'canBeTerminatedAndRestarted':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminatedAndRestarted
    else:
        raise ValueError(f"Unexpected value for handleTerminationAndRestart: {Handle_Termination_And_Restart}")

    CurrentInternalBehaviors.SupportsMultipleInstantiation = Supports_Multiple_Instantiation

    # Iterate over all runnable names and create them
    for runnable_name in runnable_names:
        Runnable_Symbol = row["Runnable Symbol"]
        can_Be_Invoked_Concurrently = row["canBeInvokedConcurrently"]

        CurrentRunnable = CurrentInternalBehaviors.Runnables.AddNew(str(runnable_name))
        CurrentRunnable.MinimumStartInterval = 0.0
        CurrentRunnable.CanBeInvokedConcurrently = can_Be_Invoked_Concurrently
        CurrentRunnable.Symbol = Runnable_Symbol

def NvBlockSwComponentType(row, runnable_names):
    global swComponentTypesPackage, NvDataSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")
    NvDataSWC = swComponentTypesPackage.ArPackages.Item("NvDataSWC")

    software_component_name = row["Software Component Name"]
    internal_behavior_name = row["Internal Behavior Name"]
    symbol_behavior_name = row["SWC Symbol"]
    Handle_Termination_And_Restart = row["handleTerminationAndRestart"]
    Supports_Multiple_Instantiation = row["supportsMultipleInstantiation"]

    CurrentSWC = NvDataSWC.Elements.AddNewNvBlockSwComponentType(software_component_name)
    CurrentInternalBehaviors = CurrentSWC.InternalBehaviors.AddNew(internal_behavior_name)
    CurrentSWC.Symbol = symbol_behavior_name

    if Handle_Termination_And_Restart == 'noSupport':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.NoSupport
    elif Handle_Termination_And_Restart == 'canBeTerminated':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminated
    elif Handle_Termination_And_Restart == 'canBeTerminatedAndRestarted':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminatedAndRestarted
    else:
        raise ValueError(f"Unexpected value for handleTerminationAndRestart: {Handle_Termination_And_Restart}")

    CurrentInternalBehaviors.SupportsMultipleInstantiation = Supports_Multiple_Instantiation

    # Iterate over all runnable names and create them
    for runnable_name in runnable_names:
        Runnable_Symbol = row["Runnable Symbol"]
        can_Be_Invoked_Concurrently = row["canBeInvokedConcurrently"]

        CurrentRunnable = CurrentInternalBehaviors.Runnables.AddNew(str(runnable_name))
        CurrentRunnable.MinimumStartInterval = 0.0
        CurrentRunnable.CanBeInvokedConcurrently = can_Be_Invoked_Concurrently
        CurrentRunnable.Symbol = Runnable_Symbol

def ParameterSwComponentType(row, runnable_names):
    global swComponentTypesPackage, PrmSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")
    PrmSWC = swComponentTypesPackage.ArPackages.Item("PrmSWC")

    software_component_name = row["Software Component Name"]
    internal_behavior_name = row["Internal Behavior Name"]
    symbol_behavior_name = row["SWC Symbol"]
    Handle_Termination_And_Restart = row["handleTerminationAndRestart"]
    Supports_Multiple_Instantiation = row["supportsMultipleInstantiation"]

    CurrentSWC = PrmSWC.Elements.AddNewParameterSwComponentType(software_component_name)
    CurrentInternalBehaviors = CurrentSWC.InternalBehaviors.AddNew(internal_behavior_name)
    CurrentSWC.Symbol = symbol_behavior_name

    if Handle_Termination_And_Restart == 'noSupport':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.NoSupport
    elif Handle_Termination_And_Restart == 'canBeTerminated':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminated
    elif Handle_Termination_And_Restart == 'canBeTerminatedAndRestarted':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminatedAndRestarted
    else:
        raise ValueError(f"Unexpected value for handleTerminationAndRestart: {Handle_Termination_And_Restart}")

    CurrentInternalBehaviors.SupportsMultipleInstantiation = Supports_Multiple_Instantiation

    # Iterate over all runnable names and create them
    for runnable_name in runnable_names:
        Runnable_Symbol = row["Runnable Symbol"]
        can_Be_Invoked_Concurrently = row["canBeInvokedConcurrently"]

        CurrentRunnable = CurrentInternalBehaviors.Runnables.AddNew(str(runnable_name))
        CurrentRunnable.MinimumStartInterval = 0.0
        CurrentRunnable.CanBeInvokedConcurrently = can_Be_Invoked_Concurrently
        CurrentRunnable.Symbol = Runnable_Symbol

def SensorActuatorSwComponentType(row, runnable_names):
    global swComponentTypesPackage, SnsrActSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")
    SnsrActSWC = swComponentTypesPackage.ArPackages.Item("SnsrActSWC")

    software_component_name = row["Software Component Name"]
    internal_behavior_name = row["Internal Behavior Name"]
    symbol_behavior_name = row["SWC Symbol"]
    Handle_Termination_And_Restart = row["handleTerminationAndRestart"]
    Supports_Multiple_Instantiation = row["supportsMultipleInstantiation"]

    CurrentSWC = SnsrActSWC.Elements.AddNewSensorActuatorSwComponentType(software_component_name)
    CurrentInternalBehaviors = CurrentSWC.InternalBehaviors.AddNew(internal_behavior_name)
    CurrentSWC.Symbol = symbol_behavior_name

    if Handle_Termination_And_Restart == 'noSupport':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.NoSupport
    elif Handle_Termination_And_Restart == 'canBeTerminated':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminated
    elif Handle_Termination_And_Restart == 'canBeTerminatedAndRestarted':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminatedAndRestarted
    else:
        raise ValueError(f"Unexpected value for handleTerminationAndRestart: {Handle_Termination_And_Restart}")

    CurrentInternalBehaviors.SupportsMultipleInstantiation = Supports_Multiple_Instantiation

    # Iterate over all runnable names and create them
    for runnable_name in runnable_names:
        Runnable_Symbol = row["Runnable Symbol"]
        can_Be_Invoked_Concurrently = row["canBeInvokedConcurrently"]

        CurrentRunnable = CurrentInternalBehaviors.Runnables.AddNew(str(runnable_name))
        CurrentRunnable.MinimumStartInterval = 0.0
        CurrentRunnable.CanBeInvokedConcurrently = can_Be_Invoked_Concurrently
        CurrentRunnable.Symbol = Runnable_Symbol

def ServiceProxySwComponentType(row, runnable_names):
    global swComponentTypesPackage, SrvcPrxySWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")
    SrvcPrxySWC = swComponentTypesPackage.ArPackages.Item("SrvcPrxySWC")

    software_component_name = row["Software Component Name"]
    internal_behavior_name = row["Internal Behavior Name"]
    symbol_behavior_name = row["SWC Symbol"]
    Handle_Termination_And_Restart = row["handleTerminationAndRestart"]
    Supports_Multiple_Instantiation = row["supportsMultipleInstantiation"]

    CurrentSWC = SrvcPrxySWC.Elements.AddNewServiceProxySwComponentType(software_component_name)
    CurrentInternalBehaviors = CurrentSWC.InternalBehaviors.AddNew(internal_behavior_name)
    CurrentSWC.Symbol = symbol_behavior_name

    if Handle_Termination_And_Restart == 'noSupport':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.NoSupport
    elif Handle_Termination_And_Restart == 'canBeTerminated':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminated
    elif Handle_Termination_And_Restart == 'canBeTerminatedAndRestarted':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminatedAndRestarted
    else:
        raise ValueError(f"Unexpected value for handleTerminationAndRestart: {Handle_Termination_And_Restart}")

    CurrentInternalBehaviors.SupportsMultipleInstantiation = Supports_Multiple_Instantiation

    # Iterate over all runnable names and create them
    for runnable_name in runnable_names:
        Runnable_Symbol = row["Runnable Symbol"]
        can_Be_Invoked_Concurrently = row["canBeInvokedConcurrently"]

        CurrentRunnable = CurrentInternalBehaviors.Runnables.AddNew(str(runnable_name))
        CurrentRunnable.MinimumStartInterval = 0.0
        CurrentRunnable.CanBeInvokedConcurrently = can_Be_Invoked_Concurrently
        CurrentRunnable.Symbol = Runnable_Symbol

def ServiceSwComponentType(row, runnable_names):
    global swComponentTypesPackage, SrvcSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")
    SrvcSWC = swComponentTypesPackage.ArPackages.Item("SrvcSWC")

    software_component_name = row["Software Component Name"]
    internal_behavior_name = row["Internal Behavior Name"]
    symbol_behavior_name = row["SWC Symbol"]
    Handle_Termination_And_Restart = row["handleTerminationAndRestart"]
    Supports_Multiple_Instantiation = row["supportsMultipleInstantiation"]

    CurrentSWC = SrvcSWC.Elements.AddNewServiceSwComponentType(software_component_name)
    CurrentInternalBehaviors = CurrentSWC.InternalBehaviors.AddNew(internal_behavior_name)
    CurrentSWC.Symbol = symbol_behavior_name

    if Handle_Termination_And_Restart == 'noSupport':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.NoSupport
    elif Handle_Termination_And_Restart == 'canBeTerminated':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminated
    elif Handle_Termination_And_Restart == 'canBeTerminatedAndRestarted':
        CurrentInternalBehaviors.handleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminatedAndRestarted
    else:
        raise ValueError(f"Unexpected value for handleTerminationAndRestart: {Handle_Termination_And_Restart}")

    CurrentInternalBehaviors.SupportsMultipleInstantiation = Supports_Multiple_Instantiation

    # Iterate over all runnable names and create them
    for runnable_name in runnable_names:
        Runnable_Symbol = row["Runnable Symbol"]
        can_Be_Invoked_Concurrently = row["canBeInvokedConcurrently"]

        CurrentRunnable = CurrentInternalBehaviors.Runnables.AddNew(str(runnable_name))
        CurrentRunnable.MinimumStartInterval = 0.0
        CurrentRunnable.CanBeInvokedConcurrently = can_Be_Invoked_Concurrently
        CurrentRunnable.Symbol = Runnable_Symbol

#####################################
# Main Function
#####################################

def Main():
    """
    Main execution flow for project configuration and SWC creation 
    """
    ReadUserDefinedExcel()
    ProjectConfig()
    CreateProjectAndPackages()
    CleanupProjectAndPackages()
    CreateSwcs()

if __name__ == "__main__":
    Main()
    print("Process completed successfully.")