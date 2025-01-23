#importing required modules

import importlib
import os
import Utilities
from pathlib import Path
import pandas as pd  # Import pandas




# Read the Excel file
excel_file_path = "package_data.xlsx" 
df = pd.read_excel(excel_file_path)



#--------------------------- ittereate through all the the sheets present in the excel----------------------------------------------------

# import pandas as pd

# # Load the Excel file
# excel_file_path = "package_data.xlsx"
# xls = pd.ExcelFile(excel_file_path)

# # Initialize a variable to hold the DataFrame if found
# df = None

# # Iterate through each sheet
# for sheet_name in xls.sheet_names:
#     # Read the current sheet
#     current_df = pd.read_excel(xls, sheet_name=sheet_name, header=0)  # Adjust header as needed
    
#     # Check if 'ProjectName' column exists
#     if 'ProjectName' in current_df.columns:
#         df = current_df
#         print(f"'ProjectName' found in sheet: {sheet_name}")
#         break  # Exit loop if found

# # if df is not None:
# #     # Now you can use df as it contains the DataFrame with 'ProjectName'
# #     Options.ProjectName = df['ProjectName'].dropna().iloc[0]
# # else:
# #     print("Column 'ProjectName' not found in any sheet. Setting default project name.")
# #     Options.ProjectName = "DefaultProjectName"  # Set a default value here


#--------------------------- ittereate through all the the sheets present in the excel----------------------------------------------------

 

# reloading Utilities

importlib.reload(Utilities)

# Connect to SystemDesk (get COM object).
SdApplication = Utilities.ConnectToSystemDesk()


import SystemDeskEnums  # pylint: disable=wrong-import-position
importlib.reload(SystemDeskEnums)






"""
#####################################
Configure some options for this demo.
#####################################
"""
# Global configuration options (shared with Utilities).
Options = Utilities.Options

# Name of this project.
Options.ProjectName = df['ProjectName'].dropna().iloc[0]    # < %%%--- Change this to your project name.%%%



# Set True to open an existing SystemDesk project (SDP). Otherwise, the SystemDesk project is created from scratch.
Options.OpenExistingProject = False

# Name of the AUTOSAR system.
Options.SystemName = "IndicatorSystem"


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
    templateFiles = [
        os.path.join(applRootDir, r"Templates\FolderStructure.arxml")
        # os.path.join(applRootDir, r"Templates\AUTOSAR_Platform.arxml"),
        # os.path.join(applRootDir, r"Templates\AUTOSAR_Std.arxml"),
        # os.path.join(applRootDir, r"Templates\AUTOSAR_PhysicalDimensions.arxml"),
        # os.path.join(applRootDir, r"Templates\AUTOSAR_Units.arxml"),
        # os.path.join(applRootDir, r"Templates\PackageStructure.arxml")
    ]

    # Now import the files.
    Utilities.ImportAutosarFilesAtProject(templateFiles)

    # Package "Communication" is not needed if the whole IndicatorSystem is
    # implemented on only one ECU.
    if not Options.UseFrontIndicatorEcus:
        communicationPackage = SdProject.RootAutosar.ArPackages.Item("Communication")
        if communicationPackage != None:
            communicationPackage.Delete()
    # return "Function CreateProjectAndPackages executed"

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
    if mySwc != None:
        mySwc.Delete()
    myComposition = swComponentTypesPackage.ArPackages.Item("MyComposition")
    if myComposition != None:
        myComposition.Delete()

    # return "Function CleanupProjectAndPackages executed"


def CreateSwcs():
    """
    Creates software components and compositions.
    """
    print("Creating root software composition and SWCs")

    # Get existing project elements.
    rootPackage = SdApplication.ActiveProject.RootAutosar

    
    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    applswc= swComponentTypesPackage.ArPackages.Item("ApplSWC")

    # Remove unnecessary elements which have been imported from the template files.
    CleanupProjectAndPackages()

    # Create Indicator Composition.
    icPackage = swComponentTypesPackage.ArPackages.AddNew("IndicatorComposition")
    icType = icPackage.Elements.AddNewCompositionSwComponentType("IndicatorComposition")
    tssInPort = icType.Ports.AddNewRPortPrototype("tss")
    wlsInPort = icType.Ports.AddNewRPortPrototype("wls")
    leftOutPort = icType.Ports.AddNewPPortPrototype("left")
    rightOutPort = icType.Ports.AddNewPPortPrototype("right")

    # Create RootSwComposition.
    rswcPackage = swComponentTypesPackage.ArPackages.AddNew("RootSwComposition")
    rswcType = rswcPackage.Elements.AddNewCompositionSwComponentType("RootSwComposition")

    # Create SWC "TurnSwitchSensors".
    tssPackage = applswc.ArPackages.AddNew("TurnSwitchSensor")
    tssSwcType = tssPackage.Elements.AddNewSensorActuatorSwComponentType("TurnSwitchSensor")
    tssOutPort = tssSwcType.Ports.AddNewPPortPrototype("out_tss")
    tssIoPort = tssSwcType.Ports.AddNewRPortPrototype("io_tss") # pylint: disable=unused-variable

    # Create SWC "WarnLightSensors".
    wlsPackage = swComponentTypesPackage.ArPackages.AddNew("WarnLightsSensor")
    wlsSwcType = wlsPackage.Elements.AddNewSensorActuatorSwComponentType("WarnLightsSensor")
    wlsOutPort = wlsSwcType.Ports.AddNewPPortPrototype("out_wls")
    wlsIoPort = wlsSwcType.Ports.AddNewRPortPrototype("io_wls") # pylint: disable=unused-variable

    # Create SWC "BulbActuator".
    bulbPackage = swComponentTypesPackage.ArPackages.AddNew("BulbActuator")
    bulbSwcType = bulbPackage.Elements.AddNewSensorActuatorSwComponentType("BulbActuator")
    bulbInPort = bulbSwcType.Ports.AddNewRPortPrototype("bulb")
    bulbIoPort = bulbSwcType.Ports.AddNewRPortPrototype("io_bulb") # pylint: disable=unused-variable

    # Create SWC "IndicatorLogic".
    ilPackage = swComponentTypesPackage.ArPackages.AddNew("IndicatorLogic")
    ilSwcType = ilPackage.Elements.AddNewApplicationSwComponentType("IndicatorLogic")
    ilTssPort = ilSwcType.Ports.AddNewRPortPrototype("tss")
    ilWlsPort = ilSwcType.Ports.AddNewRPortPrototype("wls")
    ilLeftPort = ilSwcType.Ports.AddNewPPortPrototype("left")
    ilRightPort = ilSwcType.Ports.AddNewPPortPrototype("right")

    # Add software components to the RootSwComposition.
    tssSwcPrototype = rswcType.AddSensorActuatorSwComponentType(tssSwcType)
    wlsSwcPrototype = rswcType.AddSensorActuatorSwComponentType(wlsSwcType)
    rightBulbSwcPrototype = rswcType.AddSensorActuatorSwComponentType(bulbSwcType)
    rightBulbSwcPrototype.ShortName = "FrontRightActuator"
    leftBulbSwcPrototype = rswcType.AddSensorActuatorSwComponentType(bulbSwcType)
    leftBulbSwcPrototype.ShortName = "FrontLeftActuator"
    icPrototype = rswcType.AddCompositionSwComponentType(icType)

    # Add assembly connections.
    rswcType.AddNewAssemblyConnection(tssOutPort, tssInPort, tssSwcPrototype, icPrototype)
    rswcType.AddNewAssemblyConnection(wlsOutPort, wlsInPort, wlsSwcPrototype, icPrototype)
    rswcType.AddNewAssemblyConnection(leftOutPort, bulbInPort, icPrototype, leftBulbSwcPrototype)
    rswcType.AddNewAssemblyConnection(rightOutPort, bulbInPort, icPrototype, rightBulbSwcPrototype)

    # Add delegation connections.
    ilSwcPrototype = icType.AddApplicationSwComponentType(ilSwcType)
    icType.AddNewDelegationConnection(tssInPort, ilTssPort, ilSwcPrototype)
    icType.AddNewDelegationConnection(wlsInPort, ilWlsPort, ilSwcPrototype)
    icType.AddNewDelegationConnection(leftOutPort, ilLeftPort, ilSwcPrototype)
    icType.AddNewDelegationConnection(rightOutPort, ilRightPort, ilSwcPrototype)

    # Create the RootSwComposition diagram.
    rswcDiagram = rswcType.CreateNewCompositionDiagram()
    rswcDiagram.Name = "RootSwComposition"

    grIcPrototype = rswcDiagram.AddElement(icPrototype)
    Utilities.SetPositionAndSize(grIcPrototype, 330, 160, 220, 150)
    grIndicatorTssInPort = grIcPrototype.Ports.Item("tss")
    Utilities.SetPosition(grIndicatorTssInPort, grIcPrototype.LeftEdge, grIcPrototype.TopEdge + 30)
    grIndicatorWlsInPort = grIcPrototype.Ports.Item("wls")
    Utilities.SetPosition(grIndicatorWlsInPort, grIcPrototype.LeftEdge, grIcPrototype.BottomEdge - 40)
    grIndicatorLeftInPort = grIcPrototype.Ports.Item("left")
    Utilities.SetPosition(grIndicatorLeftInPort, grIcPrototype.RightEdge, grIcPrototype.TopEdge + 30)
    grIndicatorRightInPort = grIcPrototype.Ports.Item("right")
    Utilities.SetPosition(grIndicatorRightInPort, grIcPrototype.RightEdge, grIcPrototype.BottomEdge - 40)

    grTssSwcPrototype = rswcDiagram.AddElement(tssSwcPrototype)
    Utilities.SetPositionAndSize(grTssSwcPrototype, grIcPrototype.LeftEdge - 260, grIcPrototype.TopEdge - 120, 220, 120)
    grTurnSwitchSensorIoInPort = grTssSwcPrototype.Ports.Item("io_tss")
    Utilities.SetPosition(grTurnSwitchSensorIoInPort, grTssSwcPrototype.LeftEdge, grTssSwcPrototype.TopEdge + 30)
    grTurnSwitchSensorOutPort = grTssSwcPrototype.Ports.Item("out_tss")
    Utilities.SetPosition(grTurnSwitchSensorOutPort, grTssSwcPrototype.RightEdge, grTssSwcPrototype.TopEdge + 30)

    grWlsSwcType = rswcDiagram.AddElement(wlsSwcPrototype)
    Utilities.SetPositionAndSize(grWlsSwcType, grIcPrototype.LeftEdge - 260, grIcPrototype.BottomEdge, 220, 120)
    grWarnLightsSensorIoInPort = grWlsSwcType.Ports.Item("io_wls")
    Utilities.SetPosition(grWarnLightsSensorIoInPort, grWlsSwcType.LeftEdge, grWlsSwcType.TopEdge + 30)
    grWarnLightsSensorOutPort = grWlsSwcType.Ports.Item("out_wls")
    Utilities.SetPosition(grWarnLightsSensorOutPort, grWlsSwcType.RightEdge, grWlsSwcType.TopEdge + 30)

    grLeftbulbSwcPrototype = rswcDiagram.AddElement(leftBulbSwcPrototype)
    Utilities.SetPositionAndSize(grLeftbulbSwcPrototype, grIcPrototype.RightEdge + 40, grIcPrototype.TopEdge - 120, 220, 120)
    grFrontLeftActuatorSignalInPort = grLeftbulbSwcPrototype.Ports.Item("bulb")
    Utilities.SetPosition(grFrontLeftActuatorSignalInPort, grLeftbulbSwcPrototype.LeftEdge, grLeftbulbSwcPrototype.TopEdge + 30)
    grFrontLeftActuatorIoOutPort = grLeftbulbSwcPrototype.Ports.Item("io_bulb")
    Utilities.SetPosition(grFrontLeftActuatorIoOutPort, grLeftbulbSwcPrototype.RightEdge, grLeftbulbSwcPrototype.TopEdge + 30)

    grRightbulbSwcPrototype = rswcDiagram.AddElement(rightBulbSwcPrototype)
    Utilities.SetPositionAndSize(grRightbulbSwcPrototype, grIcPrototype.RightEdge + 40, grIcPrototype.BottomEdge, 220, 120)
    grFrontRightActuatorSignalInPort = grRightbulbSwcPrototype.Ports.Item("bulb")
    Utilities.SetPosition(grFrontRightActuatorSignalInPort, grRightbulbSwcPrototype.LeftEdge, grRightbulbSwcPrototype.TopEdge + 30)
    grFrontRightActuatorIoOutPort = grRightbulbSwcPrototype.Ports.Item("io_bulb")
    Utilities.SetPosition(grFrontRightActuatorIoOutPort, grRightbulbSwcPrototype.RightEdge, grRightbulbSwcPrototype.TopEdge + 30)

    # Create notes to explain the diagram.
    textNote = rswcDiagram.TextNotices.Add("This is the overall view of the direction indicator system.")
    Utilities.SetPositionAndSize(textNote, grIcPrototype.LeftEdge, grWlsSwcType.BottomEdge + 20, 220, 40)

    diagramNote = rswcDiagram.AddDiagramNotice()
    Utilities.SetPositionAndSize(diagramNote, grRightbulbSwcPrototype.LeftEdge, grRightbulbSwcPrototype.BottomEdge + 30, 100, 80)

    # Create the IndicatorComposition Diagram.
    icDiagram = icType.CreateNewCompositionDiagram()
    icDiagram.Name = "IndicatorComposition"
    grIlSwcPrototype = icDiagram.AddElement(ilSwcPrototype)
    grIlSwcPrototype.LabelAlignment = SystemDeskEnums.LabelAlignment.Top
    Utilities.SetPositionAndSize(grIlSwcPrototype, 180, 60, 280, 120)
    grIndicatorAtomicTssInPort = grIlSwcPrototype.Ports.Item("tss")
    Utilities.SetPosition(grIndicatorAtomicTssInPort, grIlSwcPrototype.LeftEdge, grIlSwcPrototype.TopEdge + 30)
    grIndicatorAtomicWlsInPort = grIlSwcPrototype.Ports.Item("wls")
    Utilities.SetPosition(grIndicatorAtomicWlsInPort, grIlSwcPrototype.LeftEdge, grIlSwcPrototype.BottomEdge - 40)
    grIndicatorAtomicLeftOutPort = grIlSwcPrototype.Ports.Item("left")
    Utilities.SetPosition(grIndicatorAtomicLeftOutPort, grIlSwcPrototype.RightEdge, grIlSwcPrototype.TopEdge + 30)
    grIndicatorAtomicRightOutPort = grIlSwcPrototype.Ports.Item("right")
    Utilities.SetPosition(grIndicatorAtomicRightOutPort, grIlSwcPrototype.RightEdge, grIlSwcPrototype.BottomEdge - 40)
    # Create delegation ports.
    grIndicatorViewTssInPort = icDiagram.Ports.AddElement(icType.Ports.Item("tss"))
    Utilities.SetPosition(grIndicatorViewTssInPort, grIlSwcPrototype.LeftEdge - 80, grIlSwcPrototype.TopEdge + 30)
    grIndicatorViewWlsInPort = icDiagram.Ports.AddElement(icType.Ports.Item("wls"))
    Utilities.SetPosition(grIndicatorViewWlsInPort, grIlSwcPrototype.LeftEdge - 80, grIlSwcPrototype.BottomEdge - 40)
    grIndicatorViewLeftOutPort = icDiagram.Ports.AddElement(icType.Ports.Item("left"))
    Utilities.SetPosition(grIndicatorViewLeftOutPort, grIlSwcPrototype.RightEdge + 80, grIlSwcPrototype.TopEdge + 30)
    grIndicatorViewRightOutPort = icDiagram.Ports.AddElement(icType.Ports.Item("right"))
    Utilities.SetPosition(grIndicatorViewRightOutPort, grIlSwcPrototype.RightEdge + 80, grIlSwcPrototype.BottomEdge - 40)




     


# -------------------------------------------------------loop hrough multiple components------------------------------------------------




# # Specify the path to your Excel file
# excel_file_path = "path/to/your/components.xlsx"  # Replace with the actual path

# # Read the Excel file into a DataFrame
# df = pd.read_excel(excel_file_path)

# # Assuming you have read the Excel file and have a DataFrame `df`
# structures_to_create = df['Structure'].dropna().unique()  # Get unique structures

# def CreateSwcs():
#     """
#     Creates software components and compositions based on the structures specified in the Excel sheet.
#     """
#     print("Creating root software composition and SWCs")

#     # Get existing project elements.
#     rootPackage = SdApplication.ActiveProject.RootAutosar
#     swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

#     # Remove unnecessary elements which have been imported from the template files.
#     CleanupProjectAndPackages()

#     # Loop through each structure to create the corresponding component
#     for structure in structures_to_create:
#         if structure == "Component A":
#             # Create Component A
#             print("Creating Component A")
#             pass  # Replace with actual creation code
        
#         elif structure == "Component B":
#             # Create Component B
#             print("Creating Component B")
#             pass  # Replace with actual creation code
        
#         elif structure == "Component C":
#             # Create Component C
#             print("Creating Component C")
#             pass  # Replace with actual creation code
        
#         elif structure == "Component D":
#             # Create Component D
#             print("Creating Component D")
#             pass  # Replace with actual creation code

#     # Add similar checks for other components as needed



# # -------------------------------------------------------loop hrough multiple components------------------------------------------------





def Main():
    
    CreateProjectAndPackages()
    CleanupProjectAndPackages()
    CreateSwcs()

#----------------- saving the project this will be uncommented later--------------------


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


# ----------------saving the project (uncomment it later later) --------------------------   



#-------------
# Run the demo
#-------------
if (__name__ == "__main__"):
    Main()
    print("Ready")



