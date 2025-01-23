"""
--------------------------------------------------------------------------------
File:        Tutorial.py

Description: This script is used together with the SystemDesk tutorial.
             It provides methods to bring a SystemDesk project into the state
             at the beginning or end of each tutorial lesson.

Tip/Remarks: In line 53++ you can configure some options to create different
             variants of this demo.

Limitations: -

Version:     2023-B

Since:       2007-04-13

             dSPACE GmbH shall not be liable for errors contained herein or
             direct, indirect, special, incidental, or consequential damages
             in connection with the furnishing, performance, or use of this
             file.
             Brand names or product names are trademarks or registered
             trademarks of their respective companies or organizations.

Copyright (c) 2023 by dSPACE GmbH, Paderborn, Germany
  All Rights Reserved.
--------------------------------------------------------------------------------
"""

import importlib
import os
import Utilities
importlib.reload(Utilities)

# Connect to SystemDesk (get COM object).
SdApplication = Utilities.ConnectToSystemDesk()

# Import enumeration definitions.
# This import needs a Python path pointing to <SystemDeskInstallDir>\Tools\Scripting, which is set in Utilities.ConnectToSystemDesk.
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
Options.ProjectName = "TESTING_PROJECT"
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


"""
##############################################
Definition of functions for lessons and steps.
##############################################
"""

def Lesson1_Complete():
    """ Setting up Your First Project """
    CreateProjectAndPackages()

def Lesson2_Complete():
    """ Modeling and Connecting Software Components """
    Lesson1_Complete()
    CreateSwcs()

def Lesson3_Step_1_4():
    """ How to Create Sender Receiver Interfaces """
    Lesson2_Complete()
    CreateSenderReceiverInterfaces()
def Lesson3_Step_5():
    """ How to Assign Interfaces to Ports """
    Lesson3_Step_1_4()
    AssignInterfacesToPorts()
def Lesson3_Step_6():
    """ How to Specify Queued or Nonqueued Communication and Initial Values """
    Lesson3_Step_5()
    SpecifyComSpecsAndInitialValues()
def Lesson3_Complete():
    """ Modeling sender-receiver interfaces for software components """
    Lesson3_Step_6()

def Lesson4_Step_1_2():
    """ How to Define Data Types, Data Constr Elements, Compu Methods, Units, Physical Dimensions """
    Lesson3_Complete()
    CreateTssIoDataType()
def Lesson4_Step_3_6():
    """ How to Create Client Server Interfaces """
    Lesson4_Step_1_2()
    CreateClientServerInterfaces()
def Lesson4_Complete():
    """ Modeling Client Server Interfaces of Software Components """
    Lesson4_Step_3_6()

def Lesson5_Step_1_3():
    """ How to Add an SWC Internal Behavior """
    Lesson4_Complete()
    CreateInternalBehavior()
def Lesson5_Step_4_5():
    """ How to Create Interrunnable Variables """
    Lesson5_Step_1_3()
    CreateInterRunnableVariables()
    CreateDataAccesses()
def Lesson5_Complete():
    """ Modeling the SWC Internal Behavior of Atomic Software Components """
    Lesson5_Step_4_5()
    CreateOtherInternalBehaviors()

def Lesson6_Complete():
    """ Modeling Measurements and Calibration Access """
    Lesson5_Complete()
    CreateMeasurements()
    CreateCalibrationParameters()

def Lesson7_Complete():
    """ Specifying Data Type Mapping Sets and Constant Specification Mapping Sets """
    Lesson6_Complete()
    CreateDataTypeMappingSets()
    CreateConstantSpecificationMappingSets()

def Lesson8_Complete():
    """ SWC Roundtrip with TargetLink """
    Lesson7_Complete()
    if Options.CreateImplementations:
        CreateImplementations()

def Lesson9_Complete():
    """ Creating and Configuring an ECU Instance """
    Lesson8_Complete()
    CreateCentralBodyEcu()
    if Options.UseFrontIndicatorEcus:
        CreateFrontLeftIndicatorEcu()
        CreateFrontRightIndicatorEcu()

def Lesson10_Complete():
    """ Importing Network Communication Elements """
    Lesson9_Complete()
    if Options.UseFrontIndicatorEcus:
        if Options.ImportNetworkCommunicationElements:
            ImportNetworkCommunicationElements()
        else:
            CreateNetworkCommunicationElements()

def Lesson11_Step_1():
    """ How to Create a System """
    Lesson10_Complete()
    CreateSystem()
def Lesson11_Step_2_4():
    """ How to Map Software Components to ECU Instances """
    Lesson11_Step_1()
    CreateSystemMappings()
def Lesson11_Complete():
    """ Defining the System and System Mappings """
    Lesson11_Step_2_4()

def Lesson12_Step_1():
    """ How to Use AUTOSAR Master Files """
    Lesson11_Complete()
    CreateMasterFiles()
    SaveMasterFiles()
def Lesson12_Step_2():
    """ How to Export System Extracts """
    Lesson12_Step_1()
    if Options.UseFrontIndicatorEcus:
        ExportSystemExtract()
def Lesson12_Step_3():
    """ How to Import AUTOSAR Master Files """
    # Only for users without SYD_MOD license.
    LoadMasterFiles()
def Lesson12_Complete():
    """ Importing and Exporting Data. """
    if Options.License_SYD_MOD:
        # Create AUTOSAR model from scratch. For users with SYS_MOD license.
        Lesson12_Step_2()
    else:
        # Load AUTOSAR model from master files. For users without SYS_MOD license.
        Lesson12_Step_3()

def Lesson13_Step_1():
    """ How to Create an ECU Configuration """
    Lesson12_Complete()
    CreateCentralBodyEcuConfiguration()
def Lesson13_Step_2_3():
    """ How to Create the I/O Hardware Abstraction, ECU State Manager and Com Stack """
    Lesson13_Step_1()
    CreateCentralBodyIoHwAb()
    if Options.UseFrontIndicatorEcus:
        CreateCentralBodyComConfiguration()
    CreateCentralBodyEcuMConfiguration()
def Lesson13_Step_4_5():
    """ How to Map Runnables to OS Tasks """
    Lesson13_Step_2_3()
    CreateCentralBodyOsConfiguration()
    CreateCentralBodyRunnableMapping()
def Lesson13_Step_6():
    """ How to Generate the RTE """
    if Options.OpenExistingProject:
        Utilities.OpenProject()
    else:
        Lesson13_Step_4_5()
    GenerateCodeForCentralBodyEcu()


def Lesson13_Complete():
    """ Modeling ECU Configurations and Basic Software Components """
    Lesson13_Step_6()
    if Options.UseFrontIndicatorEcus:
        # FrontLeftIndicatorEcu
        if not Options.OpenExistingProject:
            CreateFrontLeftIndicatorEcuConfiguration()
            CreateFrontLeftIndicatorIoHwAb()
            CreateFrontLeftIndicatorComConfiguration()
            CreateFrontLeftIndicatorEcuMConfiguration()
            CreateFrontLeftIndicatorOsConfiguration()
            CreateFrontLeftIndicatorRunnableMapping()
        GenerateCodeForFrontLeftIndicatorEcu()
        # FrontRightIndicatorEcu
        if not Options.OpenExistingProject:
            CreateFrontRightIndicatorEcuConfiguration()
            CreateFrontRightIndicatorIoHwAb()
            CreateFrontRightIndicatorComConfiguration()
            CreateFrontRightIndicatorEcuMConfiguration()
            CreateFrontRightIndicatorOsConfiguration()
            CreateFrontRightIndicatorRunnableMapping()
        GenerateCodeForFrontRightIndicatorEcu()

def Lesson14_Step_1():
    """ Create V-ECUs """
    Lesson13_Complete()
    CreateVEcus()

def Lesson14_Step_2():
    """ Test build V-ECUs using auto generated build script """
    Lesson14_Step_1()
    if Options.BuildForVeos:
        for vEcu in SdApplication.ActiveProject.ClassicVEcus.Elements:
            if vEcu.Build() == False:
                print("Coud not build the " + vEcu.Name + " V-ECU")

def Lesson14_Step_3():
    """ Export V-ECU implementation """
    Lesson14_Step_1()
    ExportVEcuImplementations()

def Lesson14_Step_4():
    """ Build V-ECUs using VEOS Player """
    Lesson14_Step_3()
    if Options.BuildForVeos:
        BuildForVeos()

def Lesson14_Complete():
    """ Create VEOS OSA and add V-ECU implementations """
    Lesson14_Step_4()

"""
##################
Lesson1_Complete()
##################
"""
def CreateProjectAndPackages():
    """
    Creates a new package for software components and compositions.
    """
    Utilities.CreateProject()
    SdProject = SdApplication.ActiveProject
    applRootDir = r"<InstallationDir>"

    # List of template files to be imported.
    templateFiles = [
        os.path.join(applRootDir, r"Templates\AUTOSAR_GenDef.arxml"),
        os.path.join(applRootDir, r"Templates\AUTOSAR_Platform.arxml"),
        os.path.join(applRootDir, r"Templates\AUTOSAR_Std.arxml"),
        os.path.join(applRootDir, r"Templates\AUTOSAR_PhysicalDimensions.arxml"),
        os.path.join(applRootDir, r"Templates\AUTOSAR_Units.arxml"),
        os.path.join(applRootDir, r"Templates\PackageStructure.arxml")
    ]

    # Now import the files.
    Utilities.ImportAutosarFilesAtProject(templateFiles)

    # Package "Communication" is not needed if the whole IndicatorSystem is
    # implemented on only one ECU.
    if not Options.UseFrontIndicatorEcus:
        communicationPackage = SdProject.RootAutosar.ArPackages.Item("Communication")
        if communicationPackage != None:
            communicationPackage.Delete()

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
