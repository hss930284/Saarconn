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

    print("Function CreateProjectAndPackages executed")

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
    global rootPackage,current_df,value_d3,value_c3
    rootPackage = SdApplication.ActiveProject.RootAutosar
    for sheet_name in xls.sheet_names[1:]:  # This will skip the first sheet
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
            print(f"In sheet '{sheet_name}', Please provide correct software component type")

#########################################################################################################################################
             ###########-------------------------------ApplicationSwComponentType-------------------------------############
#########################################################################################################################################
def ApplicationSwComponentType():
    global CurrentswComponentTypesPackage, CurrentApplSWCPkg, CurrentSWC, CurrentInternalBehaviors, CurrentRunnable, LastRunnable

    CurrentswComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    CurrentApplSWCPkg= CurrentswComponentTypesPackage.ArPackages.Item("ApplSWC") # use this method >>ilSwcType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IndicatorLogic")
   
    CurrentSWC = CurrentApplSWCPkg.Elements.AddNewApplicationSwComponentType(current_df.iloc[2,2])

    CurrentInternalBehaviors = CurrentSWC.InternalBehaviors.AddNew(current_df.iloc[2,4])

    # CurrentInternalBehaviors.SupportsMultipleInstantiation = False
    # CurrentInternalBehaviors.HandleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.CanBeTerminated
    
    CurrentRunnable = current_df.iloc[:, 5]
    LastRunnable = CurrentRunnable.last_valid_index()
    print(LastRunnable)



    # CurrentInternalBehaviors=CurrentSWC.InternalBehaviors.Item(current_df.iloc[2,4])
    # print(CurrentInternalBehaviors)


    # CurrentInternalBehaviors.Name = current_df.iloc[2,4]
    # CurrentInternalBehaviors.Description = current_df.iloc[2,2]
    
    

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
            print("Invalid path....!!!!")
            user_defined_path = input("Please give the appropraite path where you want to save the project (e.g., E:\\sysdesk\\automation): ")
            return  
        
        # full project file path
        project_file_path = os.path.join(user_defined_path, project_file_name)
        
        # Save the project to the specified path
        Utilities.SaveProject(project_file_path)  
        print(f"*** Saving project as '{project_file_name}' to '{project_file_path}'. ***") 
    else: 
        print("*** Project not saved. ***") 

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
    print("Ready")



