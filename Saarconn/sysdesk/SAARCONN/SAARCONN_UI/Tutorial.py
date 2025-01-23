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
Options.ProjectName = "saurabh"
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


"""
##################
Lesson2_Complete()
##################
"""
def CreateSwcs():
    """
    Creates software components and compositions.
    """
    print("Creating root software composition and SWCs")

    # Get existing project elements.
    rootPackage = SdApplication.ActiveProject.RootAutosar
    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

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
    tssPackage = swComponentTypesPackage.ArPackages.AddNew("TurnSwitchSensor")
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


"""
##################
Lesson3_Complete()
##################
"""
def CreateSenderReceiverInterfaces():
    """
    Creates sender/receiver interfaces.
    """
    print("Creating sender-receiver interfaces")

    # Get existing project elements.
    rootPackage = SdApplication.ActiveProject.RootAutosar
    sharedElementsPackage = rootPackage.ArPackages.Item("SharedElements")
    ifPackage = sharedElementsPackage.ArPackages.Item("PortInterfaces")
    dataTypesPackage = sharedElementsPackage.ArPackages.Item("ApplicationDataTypes")
    compuMethodsPackage = sharedElementsPackage.ArPackages.Item("CompuMethods")

    # Create interfaces.
    # ifTss
    ifTss = ifPackage.Elements.AddNewSenderReceiverInterface("if_tss")
    Utilities.SetDescription(ifTss, "TurnSwitchSensor signals")
    ifTss.SetNewIsService().SetValue(False)
    valueTss = ifTss.DataElements.AddNew("value")
    Utilities.SetDescription(valueTss, "Turn switch sensor position [left, off, right]")
    Utilities.SetInvalidationPolicy(ifTss, valueTss, SystemDeskEnums.HandleInvalidEnum.DontInvalidate)
    # ifWls
    ifWls = ifPackage.Elements.AddNewSenderReceiverInterface("if_wls")
    Utilities.SetDescription(ifWls, "WarnLightsSensor signals")
    ifWls.SetNewIsService().SetValue(False)
    valueWls = ifWls.DataElements.AddNew("value")
    Utilities.SetDescription(valueWls, "Warn lights sensor position [off, on]")
    Utilities.SetInvalidationPolicy(ifWls, valueWls, SystemDeskEnums.HandleInvalidEnum.DontInvalidate)
    # ifBulb
    ifBulb = ifPackage.Elements.AddNewSenderReceiverInterface("if_bulb")
    Utilities.SetDescription(ifBulb, "Bulb command")
    ifBulb.SetNewIsService().SetValue(False)
    valueBulb = ifBulb.DataElements.AddNew("signal")
    Utilities.SetDescription(valueBulb, "Bulb command [off, on]")
    Utilities.SetInvalidationPolicy(ifBulb, valueBulb, SystemDeskEnums.HandleInvalidEnum.DontInvalidate)
    # ifWlsIo
    ifWlsIo = ifPackage.Elements.AddNewSenderReceiverInterface("if_wls_io")
    Utilities.SetDescription(ifWlsIo, "Measured WarnLightsSensor signals from IO hardware abstraction")
    ifWlsIo.SetNewIsService().SetValue(True)
    valueWlsIo = ifWlsIo.DataElements.AddNew("value")
    Utilities.SetDescription(valueWlsIo, "Measured position of warn lights sensor from IO hardware abstraction [off, on]")
    Utilities.SetInvalidationPolicy(ifWlsIo, valueWlsIo, SystemDeskEnums.HandleInvalidEnum.DontInvalidate)

    # Create ApplicationPrimitiveDataTypes for VariableDataPrototypes.
    # dtTss
    dtTss = dataTypesPackage.Elements.AddNewApplicationPrimitiveDataType("adt_tss")
    Utilities.SetDescription(dtTss, "Application data type for turn switch sensor position [-1 = left; 0 = none; 1 = right]")
    dtTss.Category = "VALUE"
    Utilities.SetSwCalibrationAccess(dtTss, SystemDeskEnums.SwCalibrationAccessEnum.NotAccessible)
    # dtWls
    dtWls = dataTypesPackage.Elements.AddNewApplicationPrimitiveDataType("adt_wls")
    Utilities.SetDescription(dtWls, "Application data type for warn light sensor position [0 = off; 1 = on]")
    dtWls.Category = "BOOLEAN"
    Utilities.SetSwCalibrationAccess(dtWls, SystemDeskEnums.SwCalibrationAccessEnum.NotAccessible)
    # dtBulb
    dtBulb = dataTypesPackage.Elements.AddNewApplicationPrimitiveDataType("adt_bulb")
    Utilities.SetDescription(dtBulb, "Application data type for bulb command [0 = off; 1 = on]")
    dtBulb.Category = "BOOLEAN"
    Utilities.SetSwCalibrationAccess(dtBulb, SystemDeskEnums.SwCalibrationAccessEnum.NotAccessible)

    # Create CompuMethod for ApplicationPrimitiveDataTypes adt_tss.
    cmTss = compuMethodsPackage.Elements.AddNewCompuMethod("cm_tss")
    Utilities.SetDescription(cmTss, "TEXTTABLE CompuMethod for turn switch sensor position [-1=tss_left, 0=tss_off, 1=tss_right])")
    Utilities.SetTextTableCompuMethod(cmTss, [(-1, -1, "tss_left"),(0, 0, "tss_off"),(1, 1, "tss_right")])
    # Apply CompuMethod to data type.
    Utilities.ApplyCompuMethod(dtTss, cmTss)

    # Assign data types to VariableDataPrototypes.
    valueTss.TypeTref = dtTss
    valueWls.TypeTref = dtWls
    valueBulb.TypeTref = dtBulb
    valueWlsIo.TypeTref = dtWls


def AssignInterfacesToPorts():
    """
    Applies the previously defined interfaces to the SWC ports.
    """
    # Get existing project elements.
    ifTss = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_tss")
    ifWls = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_wls")
    ifBulb = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_bulb")
    ifWlsIo = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_wls_io")

    # TurnSwitchSensor
    tssSwcType = Utilities.GetElementByPath("/SwComponentTypes/TurnSwitchSensor/TurnSwitchSensor")
    tssSwcType.Ports.Item("out_tss").ProvidedInterfaceTref = ifTss

    # WarnLightsSensor
    wlsSwcType = Utilities.GetElementByPath("/SwComponentTypes/WarnLightsSensor/WarnLightsSensor")
    wlsSwcType.Ports.Item("out_wls").ProvidedInterfaceTref = ifWls
    wlsSwcType.Ports.Item("io_wls").RequiredInterfaceTref = ifWlsIo

    # IndicatorComposition
    icType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorComposition/IndicatorComposition")
    icType.Ports.Item("tss").RequiredInterfaceTref = ifTss
    icType.Ports.Item("wls").RequiredInterfaceTref = ifWls
    icType.Ports.Item("left").ProvidedInterfaceTref = ifBulb
    icType.Ports.Item("right").ProvidedInterfaceTref = ifBulb

    # IndicatorLogic
    ilSwcType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IndicatorLogic")
    ilSwcType.Ports.Item("tss").RequiredInterfaceTref = ifTss
    ilSwcType.Ports.Item("wls").RequiredInterfaceTref = ifWls
    ilSwcType.Ports.Item("left").ProvidedInterfaceTref = ifBulb
    ilSwcType.Ports.Item("right").ProvidedInterfaceTref = ifBulb

    # BulbActuator
    bulbSwcType = Utilities.GetElementByPath("/SwComponentTypes/BulbActuator/BulbActuator")
    bulbSwcType.Ports.Item("bulb").RequiredInterfaceTref = ifBulb


def SpecifyComSpecsAndInitialValues():
    """
    Set the initial values for the data elements at SWC ports.
    """
    # Get existing project elements.
    ifTss = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_tss")
    ifWls = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_wls")
    ifBulb = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_bulb")
    ifWlsIo = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_wls_io")
    deTssValue = ifTss.DataElements.Item("value")
    deWlsValue = ifWls.DataElements.Item("value")
    deWlsIoValue = ifWlsIo.DataElements.Item("value")
    deBulbSignal = ifBulb.DataElements.Item("signal")

    # Interface elements with unqueued SR semantics.
    Utilities.SetSwImplPolicy(deTssValue, SystemDeskEnums.SwImplPolicyEnum.Standard)
    Utilities.SetSwImplPolicy(deBulbSignal, SystemDeskEnums.SwImplPolicyEnum.Standard)

    # Interface elements with queued SR semantics.
    Utilities.SetSwImplPolicy(deWlsValue, SystemDeskEnums.SwImplPolicyEnum.Queued)
    Utilities.SetSwImplPolicy(deWlsIoValue, SystemDeskEnums.SwImplPolicyEnum.Queued)

    # TurnSwitchSensor
    tssSwcType = Utilities.GetElementByPath("/SwComponentTypes/TurnSwitchSensor/TurnSwitchSensor")
    Utilities.SetNonqueuedSenderComSpec(tssSwcType.Ports.Item("out_tss"), deTssValue, 0.0)

    # WarnLightsSensor
    wlsSwcType = Utilities.GetElementByPath("/SwComponentTypes/WarnLightsSensor/WarnLightsSensor")
    Utilities.SetQueuedReceiverComSpec(wlsSwcType.Ports.Item("io_wls"), deWlsIoValue, 3)

    # IndicatorLogic
    ilSwcType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IndicatorLogic")
    Utilities.SetNonqueuedReceiverComSpec(ilSwcType.Ports.Item("tss"), deTssValue, 0.0)
    Utilities.SetQueuedReceiverComSpec(ilSwcType.Ports.Item("wls"), deWlsValue, 3)
    Utilities.SetNonqueuedSenderComSpec(ilSwcType.Ports.Item("left"), deBulbSignal, \
        0, initValueCategory="BOOLEAN")
    Utilities.SetNonqueuedSenderComSpec(ilSwcType.Ports.Item("right"), deBulbSignal, \
        0, initValueCategory="BOOLEAN")

    # BulbActuator
    bulbSwcType = Utilities.GetElementByPath("/SwComponentTypes/BulbActuator/BulbActuator")
    Utilities.SetNonqueuedReceiverComSpec(bulbSwcType.Ports.Item("bulb"), deBulbSignal, \
        0, initValueCategory="BOOLEAN")


"""
##################
Lesson4_Complete()
##################
"""
def CreateTssIoDataType():
    """
    Configures the data type for the TurnSwitchSensor IO signal.
    """
    # Get existing project elements.
    sharedElementsPackage = Utilities.GetElementByPath("/SharedElements")
    applDataTypesPackage = Utilities.GetElementByPath("/SharedElements/ApplicationDataTypes")

    # Data Type for the tss_io signal.
    adtTssIo = applDataTypesPackage.Elements.AddNewApplicationPrimitiveDataType("adt_tss_io")
    Utilities.SetDescription(adtTssIo, "Data type for tss signal from IO Hardware Abstraction [-5 cm = left; 0 cm = none; 5 cm = right]")
    adtTssIo.Category = "VALUE"
    Utilities.SetSwCalibrationAccess(adtTssIo, SystemDeskEnums.SwCalibrationAccessEnum.NotAccessible)

    # DataConstr for adt_tss_io.
    dcTssIo = Utilities.GetOrCreateDataConstr(adtTssIo, "DC_adt_tss_io")
    Utilities.SetPhysicalConstraints(dcTssIo, -5, 5)

    # CompuMethod for adt_tss_io
    cmTssIo = Utilities.GetOrCreateCompuMethod(adtTssIo, "cm_tss_io")
    Utilities.SetDescription(cmTssIo, "Linear compu method for TurnSwitchSensor raw IO signal (unit: cm; resolution: 0.1 cm)")
    cmTssIo.DisplayFormat = "%3.1f"
    Utilities.SetLinearCompuMethod(cmTssIo, 0.1, 0)

    # Unit und Physical Dimension
    unitsPackage = sharedElementsPackage.ArPackages.AddNew("Units")
    pdMeter = Utilities.GetElementByPath("/AUTOSAR_PhysicalUnits/PhysicalDimensions/Len1")
    utCm = unitsPackage.Elements.AddNewUnit("ut_cm")
    Utilities.SetDescription(utCm, "Centimeter (1 m = 100 cm)")
    utCm.PhysicalDimensionRef = pdMeter
    utCm.FactorSiToUnit = 100.0
    utCm.OffsetSiToUnit = 0.0
    cmTssIo.UnitRef = utCm


def CreateClientServerInterfaces():
    """
    Set the initial values for the data elements at SWC ports.
    """
    print("Creating client-server interfaces")

    # Get existing project elements.
    ifPackage = Utilities.GetElementByPath("/SharedElements/PortInterfaces")
    adtTssIo = Utilities.GetElementByPath("/SharedElements/ApplicationDataTypes/adt_tss_io")
    adtBulb = Utilities.GetElementByPath("/SharedElements/ApplicationDataTypes/adt_bulb")

    # TurnSwitchSensor interface for IO signals.
    ifTssIo = ifPackage.Elements.AddNewClientServerInterface("if_tss_io")
    Utilities.SetDescription(ifTssIo, "Gets the raw TurnSwitchSensor value from the IO hardware abstraction.")
    ifTssIo.SetNewIsService().SetValue(True)
    opTss = ifTssIo.Operations.AddNew("OP_GET")
    Utilities.SetDescription(opTss, "Getter operation for the raw tss value.")
    valueTssIo = opTss.Arguments.AddNew("value")
    Utilities.SetDescription(valueTssIo, "Raw tss value [-5 cm .. 5 cm].")
    Utilities.SetSwImplPolicy(valueTssIo, SystemDeskEnums.SwImplPolicyEnum.Standard)
    valueTssIo.Direction = SystemDeskEnums.ArgumentDirectionEnum.Out
    valueTssIo.ServerArgumentImplPolicy = SystemDeskEnums.ServerArgumentImplPolicyEnum.UseArgumentType
    valueTssIo.TypeTref = adtTssIo

    # Assign ClientServerInterface to port.
    tssSwcType = Utilities.GetElementByPath("/SwComponentTypes/TurnSwitchSensor/TurnSwitchSensor")
    tssSwcType.Ports.Item("io_tss").RequiredInterfaceTref = ifTssIo

    # BulbActuator interface for IO signals.
    ifBulbIo = ifPackage.Elements.AddNewClientServerInterface("if_bulb_io")
    Utilities.SetDescription(ifBulbIo, "Sets the bulb value using the IO hardware abstraction.")
    ifBulbIo.SetNewIsService().SetValue(True)
    opBulb = ifBulbIo.Operations.AddNew("OP_SET")
    Utilities.SetDescription(opBulb, "Setter operation for the bulb value.")
    valueBulbIo = opBulb.Arguments.AddNew("value")
    Utilities.SetDescription(valueBulbIo, "Value of the bulb signal [off/on].")
    Utilities.SetSwImplPolicy(valueBulbIo, SystemDeskEnums.SwImplPolicyEnum.Standard)
    valueBulbIo.direction = SystemDeskEnums.ArgumentDirectionEnum.In
    valueBulbIo.ServerArgumentImplPolicy = SystemDeskEnums.ServerArgumentImplPolicyEnum.UseArgumentType
    valueBulbIo.TypeTref = adtBulb

    # Assign ClientServerInterface to port.
    bulbSwcType = Utilities.GetElementByPath("/SwComponentTypes/BulbActuator/BulbActuator")
    bulbSwcType.Ports.Item("io_bulb").RequiredInterfaceTref = ifBulbIo


"""
##################
Lesson5_Complete()
##################
"""
def CreateInternalBehavior():
    """
    Creates the SwcInternalBehavior for the IndicatorLogic component.
    """
    print("Creating internal behavior for SWC IndicatorLogic")

    # Get existing project elements.
    ilSwcType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IndicatorLogic")
    ifWls = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_wls")

    # Create Internal Behavior.
    ilInternalBehavior = ilSwcType.InternalBehaviors.AddNew("IB_IndicatorLogic")
    ilInternalBehavior.SupportsMultipleInstantiation = False
    ilInternalBehavior.HandleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.NoSupport

    # Create Runnables.
    # tssPreRun
    tssPreRun = ilInternalBehavior.Runnables.AddNew("TssPreprocessing")
    tssPreRun.MinimumStartInterval = 0.0
    tssPreRun.CanBeInvokedConcurrently = False
    tssPreRun.Symbol = tssPreRun.ShortName
    Utilities.SetDescription(tssPreRun, "Performs preprocessing of TurnSwitchSensor signals.")
    # wlsPreRun
    wlsPreRun = ilInternalBehavior.Runnables.AddNew("WlsPreprocessing")
    wlsPreRun.MinimumStartInterval = 0.0
    wlsPreRun.CanBeInvokedConcurrently = False
    wlsPreRun.Symbol = wlsPreRun.ShortName
    Utilities.SetDescription(wlsPreRun, "Performs preprocessing of WarnLightsSensor signals.")
    # logicRun
    logicRun = ilInternalBehavior.Runnables.AddNew("Logic")
    logicRun.MinimumStartInterval = 0.0
    logicRun.CanBeInvokedConcurrently = False
    logicRun.Symbol = logicRun.ShortName
    Utilities.SetDescription(logicRun, "Determines the indicator state considering the turn switch and warn lights sensor signals.")
    # toggleRun
    toggleRun = ilInternalBehavior.Runnables.AddNew("Toggle")
    toggleRun.MinimumStartInterval = 0.0
    toggleRun.CanBeInvokedConcurrently = False
    toggleRun.Symbol = toggleRun.ShortName
    Utilities.SetDescription(toggleRun, "Toggles the bulb signals depending on the indicator state.")

    # Create RteEvents and assign them to Runnables.
    # tssEvent
    tssEvent = ilInternalBehavior.Events.AddNewTimingEvent("TssCyclic10ms")
    Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    tssEvent.Period = 0.01
    tssEvent.StartOnEventRef = tssPreRun
    # wlsEvent
    wlsEvent = ilInternalBehavior.Events.AddNewDataReceivedEvent("WlsReceivedEvent")
    Utilities.SetDescription(wlsEvent, "DataReceivedEvent for WlsPreprocessing Runnable [wls signal]")
    wlsDataIref = wlsEvent.SetNewDataIref()
    wlsDataIref.ContextRPortRef = ilSwcType.Ports.Item("wls")
    wlsDataIref.TargetDataElementRef = ifWls.DataElements.Item("value")
    wlsEvent.StartOnEventRef = wlsPreRun
    # logicEvent
    logicEvent = ilInternalBehavior.Events.AddNewTimingEvent("LogicCyclic10ms")
    Utilities.SetDescription(logicEvent, "TimingEvent for Logic Runnable [10 ms period].")
    logicEvent.Period = 0.01
    logicEvent.StartOnEventRef = logicRun
    # toggleEvent
    toggleEvent = ilInternalBehavior.Events.AddNewTimingEvent("ToggleCyclic10ms")
    Utilities.SetDescription(toggleEvent, "TimingEvent for Toggle Runnable [10 ms period].")
    toggleEvent.Period = 0.01
    toggleEvent.StartOnEventRef = toggleRun


def CreateInterRunnableVariables():
    """
    Creates InterRunnableVariables for SWC IndicatorLogic.
    """

    # Get existing project elements.
    ilSwcType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IndicatorLogic")
    ilInternalBehavior = ilSwcType.InternalBehaviors.Item("IB_IndicatorLogic")
    adtTss = Utilities.GetElementByPath("/SharedElements/ApplicationDataTypes/adt_tss")
    adtWls = Utilities.GetElementByPath("/SharedElements/ApplicationDataTypes/adt_wls")

    # irvTssStatus
    irvTssStatus = ilInternalBehavior.ImplicitInterRunnableVariables.AddNew("tss_status")
    Utilities.SetDescription(irvTssStatus, "Turn switch sensor status")
    irvTssStatus.Category = "VALUE"
    irvTssStatus.TypeTref = adtTss
    Utilities.SetSwImplPolicy(irvTssStatus, SystemDeskEnums.SwImplPolicyEnum.Standard)
    # Initial value.
    irvWlsStatusConstantSpec = Utilities.GetOrCreateInitValueConstant(irvTssStatus)
    Utilities.SetApplicationPrimitiveValueSpecification(irvWlsStatusConstantSpec, 0.0)

    # irvWlsStatus
    irvWlsStatus = ilInternalBehavior.ImplicitInterRunnableVariables.AddNew("wls_status")
    Utilities.SetDescription(irvWlsStatus, "Warn lights sensor status")
    irvWlsStatus.Category = "BOOLEAN"
    irvWlsStatus.TypeTref = adtWls ## boolean
    Utilities.SetSwImplPolicy(irvWlsStatus, SystemDeskEnums.SwImplPolicyEnum.Standard)
    # Initial value.
    irvWlsStatusConstantSpec = Utilities.GetOrCreateInitValueConstant(irvWlsStatus)
    Utilities.SetApplicationPrimitiveValueSpecification(irvWlsStatusConstantSpec, 0.0, category="BOOLEAN")

    # irvIndicatorStatus
    irvIs = ilInternalBehavior.ImplicitInterRunnableVariables.AddNew("indicator_status")
    Utilities.SetDescription(irvIs, "Blink status")
    irvIs.Category = "VALUE"
    Utilities.SetSwImplPolicy(irvIs, SystemDeskEnums.SwImplPolicyEnum.Standard)
    # adtIs
    adtIs = Utilities.GetOrCreateApplicationPrimitiveDataType(irvIs, "adt_is")
    Utilities.SetDescription(adtIs, "Application data type for blink status [0 = off; 1 = left; 2 = right; 3 = both].")
    adtIs.Category = 'VALUE'
    Utilities.SetSwCalibrationAccess(adtIs, SystemDeskEnums.SwCalibrationAccessEnum.NotAccessible)
    # cmIs
    cmIs = Utilities.GetOrCreateCompuMethod(adtIs, "cm_is")
    Utilities.SetDescription(cmIs, "TEXTTABLE CompuMethod for indicator status [0=off; 1=left; 2=right; 3=both].")
    cmIs.DisplayFormat = "%g"
    Utilities.SetTextTableCompuMethod(cmIs, [
        (0, 0, "off"),
        (1, 1, "left"),
        (2, 2, "right"),
        (3, 3, "both")])
    # Initial value.
    irvIsConstantSpec = Utilities.GetOrCreateInitValueConstant(irvIs)
    Utilities.SetApplicationPrimitiveValueSpecification(irvIsConstantSpec, 0.0)


def CreateDataAccesses():
    """
    Creates data accesses for Runnables of SWC IndicatorLogic.
    """

    # Get existing project elements.
    ilSwcType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IndicatorLogic")
    ilInternalBehavior = ilSwcType.InternalBehaviors.Item("IB_IndicatorLogic")
    tssPreRun = ilInternalBehavior.Runnables.Item("TssPreprocessing")
    wlsPreRun = ilInternalBehavior.Runnables.Item("WlsPreprocessing")
    logicRun = ilInternalBehavior.Runnables.Item("Logic")
    toggleRun = ilInternalBehavior.Runnables.Item("Toggle")
    ifTss = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_tss")
    ifWls = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_wls")
    ifBulb = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_bulb")

    # Data Access
    Utilities.CreateDataReadAccess(tssPreRun, \
        ilSwcType.Ports.Item("tss"), \
        ifTss.DataElements.Item("value"))
    Utilities.CreateDataReceivePointByArguments(wlsPreRun, \
        ilSwcType.Ports.Item("wls"), \
        ifWls.DataElements.Item("value"))
    Utilities.CreateDataWriteAccess(toggleRun, \
        ilSwcType.Ports.Item("left"), \
        ifBulb.DataElements.Item("signal"))
    Utilities.CreateDataWriteAccess(toggleRun, \
        ilSwcType.Ports.Item("right"), \
        ifBulb.DataElements.Item("signal"))

    # InterRunnableVariable accesses
    Utilities.CreateWrittenLocalVariable(tssPreRun, \
        ilInternalBehavior.ImplicitInterRunnableVariables.Item("tss_status"))
    Utilities.CreateWrittenLocalVariable(wlsPreRun, \
        ilInternalBehavior.ImplicitInterRunnableVariables.Item("wls_status"))
    Utilities.CreateReadLocalVariable(logicRun, \
        ilInternalBehavior.ImplicitInterRunnableVariables.Item("tss_status"))
    Utilities.CreateReadLocalVariable(logicRun, \
        ilInternalBehavior.ImplicitInterRunnableVariables.Item("wls_status"))
    Utilities.CreateWrittenLocalVariable(logicRun, \
        ilInternalBehavior.ImplicitInterRunnableVariables.Item("indicator_status"))
    Utilities.CreateReadLocalVariable(toggleRun, \
        ilInternalBehavior.ImplicitInterRunnableVariables.Item("indicator_status"))


def CreateOtherInternalBehaviors():
    """
    Creates the InternalBehaviors and Implementations for all SWCs except IndicatorLogic.
    """

    # Get existing project elements.
    ifTss = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_tss")
    ifTssIo = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_tss_io")
    ifWls = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_wls")
    ifWlsIo = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_wls_io")
    ifBulb = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_bulb")
    ifBulbIo = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_bulb_io")
    tssSwcType = Utilities.GetElementByPath("/SwComponentTypes/TurnSwitchSensor/TurnSwitchSensor")
    wlsSwcType = Utilities.GetElementByPath("/SwComponentTypes/WarnLightsSensor/WarnLightsSensor")
    bulbSwcType = Utilities.GetElementByPath("/SwComponentTypes/BulbActuator/BulbActuator")

    # tssInternalBehavior
    tssInternalBehavior = tssSwcType.InternalBehaviors.AddNew("IB_TurnSwitchSensor")
    tssInternalBehavior.SupportsMultipleInstantiation = False
    tssInternalBehavior.HandleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.NoSupport
    # tssRun
    tssRun = tssInternalBehavior.Runnables.AddNew("TssRunnable")
    tssRun.MinimumStartInterval = 0.0
    tssRun.CanBeInvokedConcurrently = False
    tssRun.Symbol = tssRun.ShortName
    Utilities.SetDescription(tssRun, "Reads turn switch sensor signal from IO Hardware Abstraction.")
    # tssEvent
    tssEvent = tssInternalBehavior.Events.AddNewTimingEvent("TssCyclic20ms")
    tssEvent.Period = 0.02
    tssEvent.StartOnEventRef = tssRun
    # Data accesses and server call points.
    Utilities.CreateSynchronousServerCallPoint(tssRun, \
        tssSwcType.Ports.Item("io_tss"), \
        ifTssIo.Operations.Item("OP_GET"))
    Utilities.CreateDataWriteAccess(tssRun, \
        tssSwcType.Ports.Item("out_tss"), \
        ifTss.DataElements.Item("value"))

    # wlsInternalBehavior
    wlsInternalBehavior = wlsSwcType.InternalBehaviors.AddNew("IB_WarnLightsSensor")
    wlsInternalBehavior.SupportsMultipleInstantiation = False
    wlsInternalBehavior.HandleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.NoSupport
    # wlsRun
    wlsRun = wlsInternalBehavior.Runnables.AddNew("WlsRunnable")
    wlsRun.MinimumStartInterval = 0.0
    wlsRun.CanBeInvokedConcurrently = False
    wlsRun.Symbol = wlsRun.ShortName
    Utilities.SetDescription(wlsRun, "Reads warn lights sensor signal from IO Hardware Abstraction.")
    # wlsEvent
    wlsEvent = wlsInternalBehavior.Events.AddNewDataReceivedEvent("WlsReceivedEvent")
    wlsEventDataIref = wlsEvent.SetNewDataIref()
    wlsEventDataIref.ContextRPortRef = wlsSwcType.Ports.Item("io_wls")
    wlsEventDataIref.TargetDataElementRef = ifWlsIo.DataElements.Item("value")
    wlsEvent.StartOnEventRef = wlsRun
    # Data accesses.
    Utilities.CreateDataReceivePointByArguments(wlsRun, \
        wlsSwcType.Ports.Item("io_wls"), \
        ifWlsIo.DataElements.Item("value"))
    Utilities.CreateDataSendPoint(wlsRun, \
        wlsSwcType.Ports.Item("out_wls"), \
        ifWls.DataElements.Item("value"))

    # bulbInternalBehavior
    bulbInternalBehavior = bulbSwcType.InternalBehaviors.AddNew("IB_BulbActuator")
    bulbInternalBehavior.SupportsMultipleInstantiation = True
    bulbInternalBehavior.HandleTerminationAndRestart = SystemDeskEnums.HandleTerminationAndRestartEnum.NoSupport
    # bulbRun
    bulbRun = bulbInternalBehavior.Runnables.AddNew("BulbRunnable")
    bulbRun.MinimumStartInterval = 0.0
    bulbRun.CanBeInvokedConcurrently = False
    bulbRun.Symbol = bulbRun.ShortName
    Utilities.SetDescription(bulbRun, "Writes bulb command to IO Hardware Abstraction.")
    # bulbEvent
    bulbEvent = bulbInternalBehavior.Events.AddNewTimingEvent("BulbCyclic100ms")
    bulbEvent.Period = 0.1
    bulbEvent.StartOnEventRef = bulbRun
    # Data accesses and server call points.
    Utilities.CreateDataReadAccess(bulbRun, \
        bulbSwcType.Ports.Item("bulb"), \
        ifBulb.DataElements.Item("signal"))
    Utilities.CreateSynchronousServerCallPoint(bulbRun, \
        bulbSwcType.Ports.Item("io_bulb"), \
        ifBulbIo.Operations.Item("OP_SET"))


"""
##################
Lesson6_Complete()
##################
"""
def CreateMeasurements():
    """
    Defines some data elements in sender/receiver interfaces as measurement variables.
    """
    print("Creating measurements")

    # Get existing project elements.
    ifTss = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_tss")
    ifBulb = Utilities.GetElementByPath("/SharedElements/PortInterfaces/if_bulb")

    # Define measurements.
    Utilities.SetSwCalibrationAccess(ifTss.DataElements.Item("value"), \
        SystemDeskEnums.SwCalibrationAccessEnum.ReadOnly, \
        displayFormat="%6.3f")
    Utilities.SetSwCalibrationAccess(ifBulb.DataElements.Item("signal"), \
        SystemDeskEnums.SwCalibrationAccessEnum.ReadOnly, \
        displayFormat="%1d")


def CreateCalibrationParameters():
    """
    Defines some shared calibration parameters.
    """
    print("Creating calibration parameters")

    # Get existing project elements.
    ilSwcType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IndicatorLogic")
    ilInternalBehavior = ilSwcType.InternalBehaviors.Item("IB_IndicatorLogic")
    toggleRunnable = ilInternalBehavior.Runnables.Item("Toggle")

    # SharedParameter: maxCountPrm
    maxCountPrm = ilInternalBehavior.SharedParameters.AddNew("max_count")
    maxCountPrm.Category = "VALUE"
    Utilities.SetDescription(maxCountPrm, "Determines the duration of the on/off state of the indicator lights.")
    Utilities.SetSwImplPolicy(maxCountPrm, SystemDeskEnums.SwImplPolicyEnum.Standard)
    Utilities.SetSwCalibrationAccess(maxCountPrm, \
        SystemDeskEnums.SwCalibrationAccessEnum.ReadWrite, \
        displayFormat="%3d")
    maxCountAdt = Utilities.GetOrCreateApplicationPrimitiveDataType(maxCountPrm, "adt_max_count")
    ## maxCountCm = Utilities.GetOrCreateCompuMethod(maxCountAdt, "CM_IDENTICAL")
    maxCountCm = Utilities.GetOrCreateCompuMethod(maxCountAdt, "cm_max_count")
    Utilities.SetLinearCompuMethod(maxCountCm, 1.0, 0.0)
    maxCountDc = Utilities.GetOrCreateDataConstr(maxCountAdt)
    Utilities.SetPhysicalConstraints(maxCountDc, 10, 200)
    maxCountConst = Utilities.GetOrCreateInitValueConstant(maxCountPrm)
    Utilities.SetApplicationPrimitiveValueSpecification(maxCountConst, 50)

    # Add access to shared parameter.
    Utilities.CreateSharedParameterAccess(toggleRunnable, maxCountPrm)


"""
##################
Lesson6_Complete()
##################
"""
def CreateDataTypeMappingSets():
    """
    Creates DataTypeMappingSets for the SwcInternalBehaviors.
    """
    print("Creating data type mapping sets")

    # Get existing project elements.
    adtTss = Utilities.GetElementByPath("/SharedElements/ApplicationDataTypes/adt_tss")
    adtTssIo = Utilities.GetElementByPath("/SharedElements/ApplicationDataTypes/adt_tss_io")
    adtWls = Utilities.GetElementByPath("/SharedElements/ApplicationDataTypes/adt_wls")
    adtBulb = Utilities.GetElementByPath("/SharedElements/ApplicationDataTypes/adt_bulb")
    adtIs = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/ApplicationDataTypes/adt_is")
    adtMaxCount = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/ApplicationDataTypes/adt_max_count")
    idtBoolean = Utilities.GetElementByPath("/AUTOSAR_Platform/ImplementationDataTypes/boolean")
    idtSInt8 = Utilities.GetElementByPath("/AUTOSAR_Platform/ImplementationDataTypes/sint8")
    idtUInt8 = Utilities.GetElementByPath("/AUTOSAR_Platform/ImplementationDataTypes/uint8")
    tssSwcType = Utilities.GetElementByPath("/SwComponentTypes/TurnSwitchSensor/TurnSwitchSensor")
    tssInternalBehavior = tssSwcType.InternalBehaviors.Item("IB_TurnSwitchSensor")
    wlsSwcType = Utilities.GetElementByPath("/SwComponentTypes/WarnLightsSensor/WarnLightsSensor")
    wlsInternalBehavior = wlsSwcType.InternalBehaviors.Item("IB_WarnLightsSensor")
    ilSwcType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IndicatorLogic")
    ilInternalBehavior = ilSwcType.InternalBehaviors.Item("IB_IndicatorLogic")
    bulbSwcType = Utilities.GetElementByPath("/SwComponentTypes/BulbActuator/BulbActuator")
    bulbInternalBehavior = bulbSwcType.InternalBehaviors.Item("IB_BulbActuator")

    # DataTypeMappingSet: tssDtms
    tssDtms = Utilities.GetOrCreateDataTypeMappingSet(tssInternalBehavior)
    Utilities.CreateDataTypeMap(tssDtms, adtTssIo, idtSInt8)
    Utilities.CreateDataTypeMap(tssDtms, adtTss, idtSInt8)

    # DataTypeMappingSet: wlsDtms
    wlsDtms = Utilities.GetOrCreateDataTypeMappingSet(wlsInternalBehavior)
    Utilities.CreateDataTypeMap(wlsDtms, adtWls, idtBoolean)

    # DataTypeMappingSet: ilDtms
    ilDtms = Utilities.GetOrCreateDataTypeMappingSet(ilInternalBehavior)
    Utilities.CreateDataTypeMap(ilDtms, adtTss, idtSInt8)
    Utilities.CreateDataTypeMap(ilDtms, adtWls, idtBoolean)
    Utilities.CreateDataTypeMap(ilDtms, adtBulb, idtBoolean)
    Utilities.CreateDataTypeMap(ilDtms, adtIs, idtUInt8)
    Utilities.CreateDataTypeMap(ilDtms, adtMaxCount, idtUInt8)

    # DataTypeMappingSet: bulbDtms
    bulbDtms = Utilities.GetOrCreateDataTypeMappingSet(bulbInternalBehavior)
    Utilities.CreateDataTypeMap(bulbDtms, adtBulb, idtBoolean)


def CreateConstantSpecificationMappingSets():
    """
    Creates ConstantSpecificationMappingSets for the SwcInternalBehaviors.
    """

    # Get existing project elements.
    tssSwcType = Utilities.GetElementByPath("/SwComponentTypes/TurnSwitchSensor/TurnSwitchSensor")
    tssInternalBehavior = tssSwcType.InternalBehaviors.Item("IB_TurnSwitchSensor")
    ilSwcType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IndicatorLogic")
    ilInternalBehavior = ilSwcType.InternalBehaviors.Item("IB_IndicatorLogic")
    bulbSwcType = Utilities.GetElementByPath("/SwComponentTypes/BulbActuator/BulbActuator")
    bulbInternalBehavior = bulbSwcType.InternalBehaviors.Item("IB_BulbActuator")

    # Application and implementation constants for TurnSwitchSensor.
    acOutTssValue = Utilities.GetElementByPath("/SwComponentTypes/TurnSwitchSensor/ConstantSpecifications/CONST_out_tss_value")
    icOutTssValue = Utilities.CreateImplConstantForApplConstant(acOutTssValue, 0)

    # ConstantSpecificationMappingSet: tssCsms
    tssCsms = Utilities.GetOrCreateConstantSpecificationMappingSet(tssInternalBehavior)
    Utilities.CreateConstantSpecificationMapping(tssCsms, acOutTssValue, icOutTssValue)

    # Application and implementation constants for IndicatorLogic.
    acTssValue = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/ConstantSpecifications/CONST_tss_value")
    acTssStatus = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/ConstantSpecifications/CONST_tss_status")
    acWlsStatus = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/ConstantSpecifications/CONST_wls_status")
    acIndicatorStatus = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/ConstantSpecifications/CONST_indicator_status")
    acMaxCount = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/ConstantSpecifications/CONST_max_count")
    acLeftSignal = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/ConstantSpecifications/CONST_left_signal")
    acRightSignal = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/ConstantSpecifications/CONST_right_signal")
    icTssValue = Utilities.CreateImplConstantForApplConstant(acTssValue, 0)
    icTssStatus = Utilities.CreateImplConstantForApplConstant(acTssStatus, 0)
    icWlsStatus = Utilities.CreateImplConstantForApplConstant(acWlsStatus, 0)
    icIndicatorStatus = Utilities.CreateImplConstantForApplConstant(acIndicatorStatus, 0)
    icMaxCount = Utilities.CreateImplConstantForApplConstant(acMaxCount, 50)
    icLeftSignal = Utilities.CreateImplConstantForApplConstant(acLeftSignal, 0)
    icRightSignal = Utilities.CreateImplConstantForApplConstant(acRightSignal, 0)

    # ConstantSpecificationMappingSet: ilCsms
    ilCsms = Utilities.GetOrCreateConstantSpecificationMappingSet(ilInternalBehavior)
    Utilities.CreateConstantSpecificationMapping(ilCsms, acTssValue, icTssValue)
    Utilities.CreateConstantSpecificationMapping(ilCsms, acTssStatus, icTssStatus)
    Utilities.CreateConstantSpecificationMapping(ilCsms, acWlsStatus, icWlsStatus)
    Utilities.CreateConstantSpecificationMapping(ilCsms, acIndicatorStatus, icIndicatorStatus)
    Utilities.CreateConstantSpecificationMapping(ilCsms, acMaxCount, icMaxCount)
    Utilities.CreateConstantSpecificationMapping(ilCsms, acLeftSignal, icLeftSignal)
    Utilities.CreateConstantSpecificationMapping(ilCsms, acRightSignal, icRightSignal)

    # Application and implementation constants for BulbActuator.
    acBulb = Utilities.GetElementByPath("/SwComponentTypes/BulbActuator/ConstantSpecifications/CONST_bulb_signal")
    icBulb = Utilities.CreateImplConstantForApplConstant(acBulb, 0)

    # ConstantSpecificationMappingSet: bulbCsms
    bulbCsms = Utilities.GetOrCreateConstantSpecificationMappingSet(bulbInternalBehavior)
    Utilities.CreateConstantSpecificationMapping(bulbCsms, acBulb, icBulb)


"""
##################
Lesson8_Complete()
##################
"""
def CreateImplementations():
    """
    Creates SwcImplementations for all SWCs.
    """
    print("Creating SWC implementations")

    # Get existing project elements.
    tssSwcType = Utilities.GetElementByPath("/SwComponentTypes/TurnSwitchSensor/TurnSwitchSensor")
    wlsSwcType = Utilities.GetElementByPath("/SwComponentTypes/WarnLightsSensor/WarnLightsSensor")
    ilSwcType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IndicatorLogic")
    bulbSwcType = Utilities.GetElementByPath("/SwComponentTypes/BulbActuator/BulbActuator")
    tssInternalBehavior = tssSwcType.InternalBehaviors.Item("IB_TurnSwitchSensor")
    wlsInternalBehavior = wlsSwcType.InternalBehaviors.Item("IB_WarnLightsSensor")
    ilInternalBehavior = ilSwcType.InternalBehaviors.Item("IB_IndicatorLogic")
    bulbInternalBehavior = bulbSwcType.InternalBehaviors.Item("IB_BulbActuator")

    # Create an SwcImplementation for IndicatorLogic.
    ilImplementation = Utilities.GetOrCreateSwcImplementation(ilInternalBehavior, "IMPL_IndicatorLogic")
    ilImplementation.ProgrammingLanguage = SystemDeskEnums.ProgramminglanguageEnum.C
    ilImplementation.SwVersion = "1.0.0"
    ilImplementation.UsedCodeGenerator = "TargetLink"
    ilImplementation.VendorId = 35
    ilImplementation.SetNewResourceConsumption() ## For strict schema / EB tresos.
    ilCodeDescriptor = ilImplementation.CodeDescriptors.AddNew("SourceCode")
    Utilities.CreateArtifactDescriptor(ilCodeDescriptor, "IndicatorLogic.c", "SWSRC")
    Utilities.CreateArtifactDescriptor(ilCodeDescriptor, "IndicatorLogic.h", "SWHDR")

    # tssImplementation
    tssImplementation = Utilities.GetOrCreateSwcImplementation(tssInternalBehavior, "IMPL_TurnSwitchSensor")
    tssImplementation.ProgrammingLanguage = SystemDeskEnums.ProgramminglanguageEnum.C
    tssImplementation.SwVersion = "1.0.0"
    tssImplementation.UsedCodeGenerator = "TargetLink"
    tssImplementation.VendorId = 35
    tssImplementation.SetNewResourceConsumption() ## For strict schema / EB tresos.
    tssCodeDescriptor = tssImplementation.CodeDescriptors.AddNew("SourceCode")
    Utilities.CreateArtifactDescriptor(tssCodeDescriptor, "TurnSwitchSensor.c", "SWSRC")
    Utilities.CreateArtifactDescriptor(tssCodeDescriptor, "TurnSwitchSensor.h", "SWHDR")

    # wlsImplementation
    wlsImplementation = Utilities.GetOrCreateSwcImplementation(wlsInternalBehavior, "IMPL_WarnLightsSensor")
    wlsImplementation.ProgrammingLanguage = SystemDeskEnums.ProgramminglanguageEnum.C
    wlsImplementation.SwVersion = "1.0.0"
    wlsImplementation.UsedCodeGenerator = "TargetLink"
    wlsImplementation.VendorId = 35
    wlsImplementation.SetNewResourceConsumption() ## For strict schema / EB tresos.
    wlsCodeDescriptor = wlsImplementation.CodeDescriptors.AddNew("SourceCode")
    Utilities.CreateArtifactDescriptor(wlsCodeDescriptor, "WarnLightsSensor.c", "SWSRC")
    Utilities.CreateArtifactDescriptor(wlsCodeDescriptor, "WarnLightsSensor.h", "SWHDR")

    # bulbImplementation
    bulbImplementation = Utilities.GetOrCreateSwcImplementation(bulbInternalBehavior, "IMPL_BulbActuator")
    bulbImplementation.ProgrammingLanguage = SystemDeskEnums.ProgramminglanguageEnum.C
    bulbImplementation.SwVersion = "1.0.0"
    bulbImplementation.UsedCodeGenerator = "TargetLink"
    bulbImplementation.VendorId = 35
    bulbImplementation.SetNewResourceConsumption() ## For strict schema / EB tresos.
    bulbCodeDescriptor = bulbImplementation.CodeDescriptors.AddNew("SourceCode")
    Utilities.CreateArtifactDescriptor(bulbCodeDescriptor, "BulbActuator.c", "SWSRC")
    Utilities.CreateArtifactDescriptor(bulbCodeDescriptor, "BulbActuator.h", "SWHDR")


"""
##################
Lesson9_Complete()
##################
"""
def CreateCentralBodyEcu():
    """
    Creates an EcuInstance "CentralBodyEcu".
    """
    print("Creating CentralBodyEcu")

    # Delete package MyEcu, which was imported from template "PackageStructure.arxml".
    myEcu = Utilities.GetElementByPath("/EcuInstances/MyEcu")
    if myEcu != None:
        myEcu.Delete()

    # Create a package for ECU instances.
    pkgEcuInstances = Utilities.GetOrCreatePackage("/EcuInstances/CentralBodyEcu")

    # Create an EcuInstance.
    ecuInstance = pkgEcuInstances.Elements.AddNewEcuInstance("CentralBodyEcu")
    Utilities.SetDescription(ecuInstance, "Reads sensor signals and computes the indicator logic.")
    ecuInstance.ComConfigurationGwTimeBase = 0.010
    ecuInstance.ComConfigurationRxTimeBase = 0.010
    ecuInstance.ComConfigurationTxTimeBase = 0.010
    ecuInstance.SleepModeSupported = False
    ecuInstance.WakeUpOverBusSupported = False

    if Options.UseFrontIndicatorEcus:
        # CanController and CanConnector.
        canCommController = ecuInstance.CommControllers.AddNewCanCommunicationController("CanCommunicationController")
        canCommControllerConditional = canCommController.CanCommunicationControllerVariants.AddNew()
        canControllerConfiguration = canCommControllerConditional.SetNewCanControllerAttributesCanControllerConfiguration()
        canControllerConfiguration.SyncJumpWidth = 3
        canControllerConfiguration.TimeSeg1 = 13
        canControllerConfiguration.TimeSeg2 = 3
        canBodyConnector = ecuInstance.Connectors.AddNewCanCommunicationConnector("CanBodyConnector")
        canBodyConnector.CommControllerRef = canCommController

        # FramePorts.
        canBodyFramePortOut = canBodyConnector.EcuCommPortInstances.AddNewFramePort("CanBodyFramePortOut")
        canBodyFramePortOut.CommunicationDirection = SystemDeskEnums.CommunicationDirectionTypeEnum.Out
        # IPduPorts.
        canBodyIPduPortOut = canBodyConnector.EcuCommPortInstances.AddNewIPduPort("CanBodyIPduPortOut")
        canBodyIPduPortOut.CommunicationDirection = SystemDeskEnums.CommunicationDirectionTypeEnum.Out
        # ISignalPorts.
        canBodyISignalPortOut = canBodyConnector.EcuCommPortInstances.AddNewISignalPort("CanBodyISignalPortOut")
        canBodyISignalPortOut.CommunicationDirection = SystemDeskEnums.CommunicationDirectionTypeEnum.Out


def CreateFrontLeftIndicatorEcu():
    """
    Creates an EcuInstance "FrontLeftIndicatorEcu".
    """
    print("Creating FrontLeftIndicatorEcu")

    # Create a package for ECU instances.
    pkgEcuInstances = Utilities.GetOrCreatePackage("/EcuInstances/FrontLeftIndicatorEcu")

    # Create an EcuInstance.
    ecuInstance = pkgEcuInstances.Elements.AddNewEcuInstance("FrontLeftIndicatorEcu")
    Utilities.SetDescription(ecuInstance, "Controls the front-left bulb actuator.")
    ecuInstance.ComConfigurationGwTimeBase = 0.010
    ecuInstance.ComConfigurationRxTimeBase = 0.010
    ecuInstance.ComConfigurationTxTimeBase = 0.010
    ecuInstance.SleepModeSupported = False
    ecuInstance.WakeUpOverBusSupported = False

    # CanController and CanConnector.
    canCommController = ecuInstance.CommControllers.AddNewCanCommunicationController("CanCommunicationController")
    canCommControllerConditional = canCommController.CanCommunicationControllerVariants.AddNew()
    canControllerConfiguration = canCommControllerConditional.SetNewCanControllerAttributesCanControllerConfiguration()
    canControllerConfiguration.SyncJumpWidth = 3
    canControllerConfiguration.TimeSeg1 = 13
    canControllerConfiguration.TimeSeg2 = 3
    canBodyConnector = ecuInstance.Connectors.AddNewCanCommunicationConnector("CanBodyConnector")
    canBodyConnector.CommControllerRef = canCommController

    # FramePorts.
    canBodyFramePortIn = canBodyConnector.EcuCommPortInstances.AddNewFramePort("CanBodyFramePortIn")
    canBodyFramePortIn.CommunicationDirection = SystemDeskEnums.CommunicationDirectionTypeEnum.In
    # IPduPorts.
    canBodyIPduPortIn = canBodyConnector.EcuCommPortInstances.AddNewIPduPort("CanBodyIPduPortIn")
    canBodyIPduPortIn.CommunicationDirection = SystemDeskEnums.CommunicationDirectionTypeEnum.In
    # ISignalPorts.
    canBodyISignalPortIn = canBodyConnector.EcuCommPortInstances.AddNewISignalPort("CanBodyISignalPortIn")
    canBodyISignalPortIn.CommunicationDirection = SystemDeskEnums.CommunicationDirectionTypeEnum.In


def CreateFrontRightIndicatorEcu():
    """
    Creates an EcuInstance "FrontRightIndicatorEcu".
    """
    print("Creating FrontRightIndicatorEcu")

    # Create a package for ECU instances.
    pkgEcuInstances = Utilities.GetOrCreatePackage("/EcuInstances/FrontRightIndicatorEcu")

    # Create an EcuInstance.
    ecuInstance = pkgEcuInstances.Elements.AddNewEcuInstance("FrontRightIndicatorEcu")
    Utilities.SetDescription(ecuInstance, "Controls the front-right bulb actuator.")
    ecuInstance.ComConfigurationGwTimeBase = 0.010
    ecuInstance.ComConfigurationRxTimeBase = 0.010
    ecuInstance.ComConfigurationTxTimeBase = 0.010
    ecuInstance.SleepModeSupported = False
    ecuInstance.WakeUpOverBusSupported = False

    # CanController and CanConnector.
    canCommController = ecuInstance.CommControllers.AddNewCanCommunicationController("CanCommunicationController")
    canCommControllerConditional = canCommController.CanCommunicationControllerVariants.AddNew()
    canControllerConfiguration = canCommControllerConditional.SetNewCanControllerAttributesCanControllerConfiguration()
    canControllerConfiguration.SyncJumpWidth = 3
    canControllerConfiguration.TimeSeg1 = 13
    canControllerConfiguration.TimeSeg2 = 3
    canBodyConnector = ecuInstance.Connectors.AddNewCanCommunicationConnector("CanBodyConnector")
    canBodyConnector.CommControllerRef = canCommController

    # FramePorts.
    canBodyFramePortIn = canBodyConnector.EcuCommPortInstances.AddNewFramePort("CanBodyFramePortIn")
    canBodyFramePortIn.CommunicationDirection = SystemDeskEnums.CommunicationDirectionTypeEnum.In
    # IPduPorts.
    canBodyIPduPortIn = canBodyConnector.EcuCommPortInstances.AddNewIPduPort("CanBodyIPduPortIn")
    canBodyIPduPortIn.CommunicationDirection = SystemDeskEnums.CommunicationDirectionTypeEnum.In
    # ISignalPorts.
    canBodyISignalPortIn = canBodyConnector.EcuCommPortInstances.AddNewISignalPort("CanBodyISignalPortIn")
    canBodyISignalPortIn.CommunicationDirection = SystemDeskEnums.CommunicationDirectionTypeEnum.In


"""
##################
Lesson10_Complete()
##################
"""
def CreateNetworkCommunicationElements():
    """
    Create network communication elements.
    """
    print("Creating network communication (Fibex) elements")

    # Elements needed for the network communication.
    centralBodyEcu = Utilities.GetElementByPath("/EcuInstances/CentralBodyEcu/CentralBodyEcu")
    frontLeftIndicatorEcu = Utilities.GetElementByPath("/EcuInstances/FrontLeftIndicatorEcu/FrontLeftIndicatorEcu")
    frontRightIndicatorEcu = Utilities.GetElementByPath("/EcuInstances/FrontRightIndicatorEcu/FrontRightIndicatorEcu")

    # Create packages for the network communication elements.
    pkgClusters = Utilities.GetOrCreatePackage("/Communication/CommunicationClusters")
    pkgFrames = Utilities.GetOrCreatePackage("/Communication/Frames")  # pylint: disable=unused-variable
    pkgISignalIPdus = Utilities.GetOrCreatePackage("/Communication/Pdus")
    pkgISignals = Utilities.GetOrCreatePackage("/Communication/ISignals")  # pylint: disable=unused-variable
    pkgSystemSignals = Utilities.GetOrCreatePackage("/Communication/SystemSignals")

    # CanController and CanConnector.
    centralBodyEcuCanConnector = centralBodyEcu.Connectors.Item("CanBodyConnector")
    centralBodyEcuCanISignalPortOut = centralBodyEcuCanConnector.EcuCommPortInstances.Item("CanBodyISignalPortOut")
    centralBodyEcuCanIPduPortOut = centralBodyEcuCanConnector.EcuCommPortInstances.Item("CanBodyIPduPortOut")
    centralBodyEcuCanFramePortOut = centralBodyEcuCanConnector.EcuCommPortInstances.Item("CanBodyFramePortOut")
    frontLeftIndicatorEcuCanConnector = frontLeftIndicatorEcu.Connectors.Item("CanBodyConnector")
    frontLeftIndicatorEcuCanISignalPortIn = frontLeftIndicatorEcuCanConnector.EcuCommPortInstances.Item("CanBodyISignalPortIn")
    frontLeftIndicatorEcuCanIPduPortIn = frontLeftIndicatorEcuCanConnector.EcuCommPortInstances.Item("CanBodyIPduPortIn")
    frontLeftIndicatorEcuCanFramePortIn = frontLeftIndicatorEcuCanConnector.EcuCommPortInstances.Item("CanBodyFramePortIn")
    frontRightIndicatorEcuCanConnector = frontRightIndicatorEcu.Connectors.Item("CanBodyConnector")
    frontRightIndicatorEcuCanISignalPortIn = frontRightIndicatorEcuCanConnector.EcuCommPortInstances.Item("CanBodyISignalPortIn")
    frontRightIndicatorEcuCanIPduPortIn = frontRightIndicatorEcuCanConnector.EcuCommPortInstances.Item("CanBodyIPduPortIn")
    frontRightIndicatorEcuCanFramePortIn = frontRightIndicatorEcuCanConnector.EcuCommPortInstances.Item("CanBodyFramePortIn")

    #-----------------------------------
    # Create SystemSignals and ISignals.
    #-----------------------------------
    # systemSignalLeft
    systemSignalLeft = pkgSystemSignals.Elements.AddNewSystemSignal("Left")
    Utilities.SetDescription(systemSignalLeft, "Left bulb command.")
    systemSignalLeft.DynamicLength = False
    iSignalLeft = Utilities.CreateISignal(systemSignalLeft)
    iSignalLeft.Length = 1
    iSignalLeft.DataTypePolicy = SystemDeskEnums.DataTypePolicyEnum.NetworkRepresentationFromComSpec
    # systemSignalRight
    systemSignalRight = pkgSystemSignals.Elements.AddNewSystemSignal("Right")
    Utilities.SetDescription(systemSignalRight, "Right bulb command.")
    systemSignalRight.DynamicLength = False
    iSignalRight = Utilities.CreateISignal(systemSignalRight)
    iSignalRight.Length = 1
    iSignalRight.DataTypePolicy = SystemDeskEnums.DataTypePolicyEnum.NetworkRepresentationFromComSpec

    #--------------------
    # Create ISignalIPdu.
    #--------------------
    indicatorIPdu = pkgISignalIPdus.Elements.AddNewISignalIPdu("IndicatorIPdu")
    Utilities.SetDescription(indicatorIPdu, "Containing bulb command signals for front left/right indicator")
    indicatorIPdu.Length = 1  ## Bytes
    indicatorIPdu.UnusedBitPattern = 85

    # Map ISignals into IPdu.
    # iSignalLeft
    indicatorIPduSignalLeftToPduMapping = indicatorIPdu.ISignalToPduMappings.AddNew(iSignalLeft.ShortName)
    indicatorIPduSignalLeftToPduMapping.ISignalRef = iSignalLeft
    indicatorIPduSignalLeftToPduMapping.StartPosition = 0
    indicatorIPduSignalLeftToPduMapping.PackingByteOrder = SystemDeskEnums.ByteOrderEnum.MostSignificantByteLast ## LittleEndian
    indicatorIPduSignalLeftToPduMapping.TransferProperty = SystemDeskEnums.TransferPropertyEnum.Triggered

    # iSignalRight
    indicatorIPduSignalRightToPduMapping = indicatorIPdu.ISignalToPduMappings.AddNew(iSignalRight.ShortName)
    indicatorIPduSignalRightToPduMapping.ISignalRef = iSignalRight
    indicatorIPduSignalRightToPduMapping.StartPosition = 1
    indicatorIPduSignalRightToPduMapping.PackingByteOrder = SystemDeskEnums.ByteOrderEnum.MostSignificantByteLast ## LittleEndian
    indicatorIPduSignalRightToPduMapping.TransferProperty = SystemDeskEnums.TransferPropertyEnum.Triggered

    # IPduTiming
    Utilities.SetISignalIPduEventControlledTiming(indicatorIPdu, \
        transmissionMode=True, \
        minimumDelay=0.0, \
        numOfRepetitions=1, \
        repetitionPeriod=0.010, \
        transmissionModeConditions=((SystemDeskEnums.DataFilterTypeEnum.Always, indicatorIPduSignalRightToPduMapping),))

    #-----------------------------------
    # Create Frame for each ISignalIPdu.
    #-----------------------------------
    indicatorFrame = Utilities.CreateFrame(indicatorIPdu)

    #---------------------
    # Create a CanCluster.
    #---------------------
    canBodyCluster = pkgClusters.Elements.AddNewCanCluster("CanBodyCluster")
    Utilities.SetDescription(canBodyCluster, "CAN cluster for body signals.")
    canBodyClusterConditional = canBodyCluster.CanClusterVariants.AddNew()
    canBodyClusterConditional.ProtocolName = "CAN"
    canBodyClusterConditional.ProtocolVersion = "2.0B"
    canBodyClusterConditional.BaudRate = 125000
    # PhysicalChannels.
    canBodyPhysicalChannel = canBodyClusterConditional.PhysicalChannels.AddNewCanPhysicalChannel("CanBodyPhysicalChannel")
    Utilities.SetDescription(canBodyPhysicalChannel, "Physical CAN channel for body signals.")
    centralBodyEcuCanConnectorRefConditional = canBodyPhysicalChannel.CommConnectors.AddNew()
    centralBodyEcuCanConnectorRefConditional.CommunicationConnectorRef = centralBodyEcuCanConnector
    frontLeftIndicatorEcuCanConnectorRefConditional = canBodyPhysicalChannel.CommConnectors.AddNew()
    frontLeftIndicatorEcuCanConnectorRefConditional.CommunicationConnectorRef = frontLeftIndicatorEcuCanConnector
    frontRightIndicatorEcuCanConnectorRefConditional = canBodyPhysicalChannel.CommConnectors.AddNew()
    frontRightIndicatorEcuCanConnectorRefConditional.CommunicationConnectorRef = frontRightIndicatorEcuCanConnector

    #-----------------------------------------
    # Add triggerings to the CAN channel.
    #-----------------------------------------

    # Add ISignalTriggerings to the CAN channel.
    stIndicatorLeft = Utilities.CreateISignalTriggering(canBodyPhysicalChannel, iSignalLeft, \
        (centralBodyEcuCanISignalPortOut, frontLeftIndicatorEcuCanISignalPortIn))
    stIndicatorRight = Utilities.CreateISignalTriggering(canBodyPhysicalChannel, iSignalRight, \
        (centralBodyEcuCanISignalPortOut, frontRightIndicatorEcuCanISignalPortIn))

   # Add PduTriggerings to the CAN channel.
    ptIndicator = Utilities.CreatePduTriggering(canBodyPhysicalChannel, indicatorIPdu, (stIndicatorLeft, stIndicatorRight,), \
        (centralBodyEcuCanIPduPortOut, frontLeftIndicatorEcuCanIPduPortIn, frontRightIndicatorEcuCanIPduPortIn))

    # Add FrameTriggerings to the CAN channel.
    Utilities.CreateFrameTriggering("CAN", canBodyPhysicalChannel, indicatorFrame, 0x0100, (ptIndicator,), \
        (centralBodyEcuCanFramePortOut, frontLeftIndicatorEcuCanFramePortIn, frontRightIndicatorEcuCanFramePortIn))


def ImportNetworkCommunicationElements():
    """
    Import network communication elements.
    """
    print("Importing network communication (Fibex) elements")

    # Determine the name of the AUTOSAR file containing the Fibex elements for the CanBodyCluster.
    canBodyClusterFile = os.path.join("<ProjectDir>", "_SystemFiles", "IndicatorSystem", "CanBodyCluster.arxml")

    # Now import the file.
    Utilities.ImportAutosarFiles(canBodyClusterFile, \
        importDiagrams=False, \
        optionShowImportDialog=False)


"""
##################
Lesson11_Complete()
##################
"""
def CreateSystem():
    """
    Creates the Tutorial system.
    """
    print("Creating system")

    # Delete package MySystem, which was imported from template "PackageStructure.arxml".
    mySystem = Utilities.GetElementByPath("/Systems/MySystem")
    if mySystem != None:
        mySystem.Delete()

    # Create a package for the system.
    pkgSystemsTutorial = Utilities.GetOrCreatePackage("/Systems/" + Options.SystemName)

    # Elements needed by this system.
    rootSwComposition = Utilities.GetElementByPath("/SwComponentTypes/RootSwComposition/RootSwComposition")
    centralBodyEcu = Utilities.GetElementByPath("/EcuInstances/CentralBodyEcu/CentralBodyEcu")
    if Options.UseFrontIndicatorEcus:
        frontLeftIndicatorEcu = Utilities.GetElementByPath("/EcuInstances/FrontLeftIndicatorEcu/FrontLeftIndicatorEcu")
        frontRightIndicatorEcu = Utilities.GetElementByPath("/EcuInstances/FrontRightIndicatorEcu/FrontRightIndicatorEcu")
        canBodyCluster = Utilities.GetElementByPath("/Communication/CommunicationClusters/CanBodyCluster")

    #--------------------
    # System: sysTutorial
    #--------------------
    sysTutorial = pkgSystemsTutorial.Elements.AddNewSystem(Options.SystemName)
    Utilities.SetDescription(sysTutorial, "AUTOSAR System. " + \
        "Describes a indicator system.")
    sysTutorial.Category = "SYSTEM_DESCRIPTION"
    sysTutorial.SystemVersion = "1.0.0"

    # Set the RootSwComposition.
    sysTutorial.AddNewRootSwCompositionPrototype(rootSwComposition)

    # Add EcuInstances to the System.
    sysTutorial.AddEcuInstance(centralBodyEcu)
    if Options.UseFrontIndicatorEcus:
        sysTutorial.AddEcuInstance(frontLeftIndicatorEcu)
        sysTutorial.AddEcuInstance(frontRightIndicatorEcu)

    if Options.UseFrontIndicatorEcus:
        # Add CanCluster to the system.
        fibexElementConditional = sysTutorial.FibexElements.AddNew()
        fibexElementConditional.FibexElementRef = canBodyCluster

    # Open the System Manager view.
    sysTutorial.OpenInSystemView()


def CreateSystemMappings():
    """
    Creates the mappings for the Tutorial system.
    """
    print("Creating system mappings")

    # Get packages.
    pkgSystemsTutorial = Utilities.GetOrCreatePackage("/Systems/" + Options.SystemName)
    pkgInterfaces = Utilities.GetOrCreatePackage("/SharedElements/PortInterfaces")
    pkgSystemSignals = Utilities.GetElementByPath("/Communication/SystemSignals")

    # Elements needed by this system.
    rootSwComposition = Utilities.GetElementByPath("/SwComponentTypes/RootSwComposition/RootSwComposition")
    ilSwcType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IndicatorLogic")
    centralBodyEcu = Utilities.GetElementByPath("/EcuInstances/CentralBodyEcu/CentralBodyEcu")
    if Options.UseFrontIndicatorEcus:
        frontLeftIndicatorEcu = Utilities.GetElementByPath("/EcuInstances/FrontLeftIndicatorEcu/FrontLeftIndicatorEcu")
        frontRightIndicatorEcu = Utilities.GetElementByPath("/EcuInstances/FrontRightIndicatorEcu/FrontRightIndicatorEcu")
    tssSwcPrototype = rootSwComposition.Components.Item("TurnSwitchSensor")
    wlsSwcPrototype = rootSwComposition.Components.Item("WarnLightsSensor")
    icPrototype = rootSwComposition.Components.Item("IndicatorComposition")
    icType = Utilities.GetElementByPath("/SwComponentTypes/IndicatorComposition/IndicatorComposition")
    ilSwcPrototype = icType.Components.Item("IndicatorLogic")
    flaSwcPrototype = rootSwComposition.Components.Item("FrontLeftActuator")
    fraSwcPrototype = rootSwComposition.Components.Item("FrontRightActuator")
    tssImplementation = Utilities.GetElementByPath("/SwComponentTypes/TurnSwitchSensor/IMPL_TurnSwitchSensor")
    wlsImplementation = Utilities.GetElementByPath("/SwComponentTypes/WarnLightsSensor/IMPL_WarnLightsSensor")
    ilImplementation = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic/IMPL_IndicatorLogic")
    bulbImplementation = Utilities.GetElementByPath("/SwComponentTypes/BulbActuator/IMPL_BulbActuator")

    # System: sysTutorial
    sysTutorial = pkgSystemsTutorial.Elements.Item(Options.SystemName)

    # SWC to ECU mappings.
    sysTutorial.MapSwcToEcu(centralBodyEcu, [tssSwcPrototype])
    sysTutorial.MapSwcToEcu(centralBodyEcu, [wlsSwcPrototype])
    sysTutorial.MapSwcToEcu(centralBodyEcu, [icPrototype, ilSwcPrototype])
    if Options.UseFrontIndicatorEcus:
        sysTutorial.MapSwcToEcu(frontLeftIndicatorEcu, [flaSwcPrototype])
        sysTutorial.MapSwcToEcu(frontRightIndicatorEcu, [fraSwcPrototype])
    else:
        sysTutorial.MapSwcToEcu(centralBodyEcu, [flaSwcPrototype])
        sysTutorial.MapSwcToEcu(centralBodyEcu, [fraSwcPrototype])

    # SWC to Implementation mappings.
    sysTutorial.MapSwcToImpl(tssImplementation, [tssSwcPrototype])
    sysTutorial.MapSwcToImpl(wlsImplementation, [wlsSwcPrototype])
    sysTutorial.MapSwcToImpl(ilImplementation, [icPrototype, ilSwcPrototype])
    sysTutorial.MapSwcToImpl(bulbImplementation, [flaSwcPrototype])
    sysTutorial.MapSwcToImpl(bulbImplementation, [fraSwcPrototype])

    if Options.UseFrontIndicatorEcus:
        #--------------
        # DataMappings.
        #--------------
        # IndicatorLogic -> left
        leftMapping = sysTutorial.CreateSenderReceiverToSignalMapping( \
            [icPrototype, ilSwcPrototype], \
            ilSwcType.Ports.Item("left"), \
            pkgInterfaces.Elements.Item("if_bulb").DataElements.Item("signal"))
        leftMapping.SystemsignalRef = pkgSystemSignals.Elements.Item("Left")
        # IndicatorLogic -> Right
        rightMapping = sysTutorial.CreateSenderReceiverToSignalMapping( \
            [icPrototype, ilSwcPrototype], \
            ilSwcType.Ports.Item("right"), \
            pkgInterfaces.Elements.Item("if_bulb").DataElements.Item("signal"))
        rightMapping.SystemsignalRef = pkgSystemSignals.Elements.Item("Right")


"""
##################
Lesson12_Complete()
##################
"""
def CreateMasterFiles():
    """
    Assigns all AUTOSAR elements to master files.
    """
    print("Defining master files")

    # Get existing project elements.
    sdProject = SdApplication.ActiveProject
    arPlatformPackage = Utilities.GetElementByPath("/AUTOSAR_Platform")
    arGenDefPackage = Utilities.GetElementByPath("/AUTOSAR_GenDef")
    arStdPackage = Utilities.GetElementByPath("/AUTOSAR_Std")
    arPhysPackage = Utilities.GetElementByPath("/AUTOSAR_PhysicalUnits/PhysicalDimensions")
    arUnitsPackage = Utilities.GetElementByPath("/AUTOSAR_PhysicalUnits/Units")
    sharedElementsPackage = Utilities.GetElementByPath("/SharedElements")
    tssPackage = Utilities.GetElementByPath("/SwComponentTypes/TurnSwitchSensor")
    wlsPackage = Utilities.GetElementByPath("/SwComponentTypes/WarnLightsSensor")
    ilPackage = Utilities.GetElementByPath("/SwComponentTypes/IndicatorLogic")
    bulbPackage = Utilities.GetElementByPath("/SwComponentTypes/BulbActuator")
    rswcPackage = Utilities.GetElementByPath("/SwComponentTypes/RootSwComposition")
    icPackage = Utilities.GetElementByPath("/SwComponentTypes/IndicatorComposition")
    ic = Utilities.GetElementByPath("/SwComponentTypes/IndicatorComposition/IndicatorComposition")
    ecusPackage = Utilities.GetElementByPath("/EcuInstances")
    if Options.UseFrontIndicatorEcus:
        canBodyPackage = Utilities.GetElementByPath("/Communication")
    indicatorSystemPackage = Utilities.GetElementByPath("/Systems/" + Options.SystemName)

    # Create directory for master files.
    projectRootDir = Utilities.GetProjectRootDir()
    masterFilePath = os.path.join(projectRootDir, "MasterFiles")
    if not os.path.exists(masterFilePath):
        os.mkdir(masterFilePath)

    # Define master files and add packages/elements.
    arGenDefFile = sdProject.MasterFiles.Add("<ProjectDir>\\_StandardFiles\\AUTOSAR_GenDef.arxml")
    arGenDefFile.AddPackage(arGenDefPackage)
    arPlatformFile = sdProject.MasterFiles.Add("<ProjectDir>\\_StandardFiles\\AUTOSAR_Platform.arxml")
    arPlatformFile.AddPackage(arPlatformPackage)
    arStdFile = sdProject.MasterFiles.Add("<ProjectDir>\\_StandardFiles\\AUTOSAR_Std.arxml")
    arStdFile.AddPackage(arStdPackage)
    arPhysFile = sdProject.MasterFiles.Add("<ProjectDir>\\_StandardFiles\\AUTOSAR_PhysicalDimensions.arxml")
    arPhysFile.AddPackage(arPhysPackage)
    arUnitsFile = sdProject.MasterFiles.Add("<ProjectDir>\\_StandardFiles\\AUTOSAR_Units.arxml")
    arUnitsFile.AddPackage(arUnitsPackage)
    sharedElementsFile = sdProject.MasterFiles.Add("<ProjectDir>\\_SharedFiles\\SharedElements.arxml")
    sharedElementsFile.AddPackage(sharedElementsPackage)
    tssFile = sdProject.MasterFiles.Add("<ProjectDir>\\_ComponentFiles\\TurnswitchSensor\\TurnSwitchSensor.arxml")
    tssFile.AddPackage(tssPackage)
    wlsFile = sdProject.MasterFiles.Add("<ProjectDir>\\_ComponentFiles\\WarnLightsSensor\\WarnLightsSensor.arxml")
    wlsFile.AddPackage(wlsPackage)
    bulbFile = sdProject.MasterFiles.Add("<ProjectDir>\\_ComponentFiles\\BulbActuator\\BulbActuator.arxml")
    bulbFile.AddPackage(bulbPackage)
    ilFile = sdProject.MasterFiles.Add("<ProjectDir>\\_ComponentFiles\\IndicatorLogic\\IndicatorLogic.arxml")
    ilFile.AddPackage(ilPackage)
    rswcFile = sdProject.MasterFiles.Add("<ProjectDir>\\MasterFiles\\RootSwComposition.arxml")
    rswcFile.AddPackage(rswcPackage)
    icFile = sdProject.MasterFiles.Add("<ProjectDir>\\MasterFiles\\IndicatorComposition.arxml")
    icFile.AddPackage(icPackage)
    icInternalFile = sdProject.MasterFiles.Add("<ProjectDir>\\MasterFiles\\IndicatorComposition_Internal.arxml")
    ic.MasterFiles.Add(icInternalFile)
    ic.AssignNewChildElementsMasterFile = icInternalFile
    for swc in ic.Components.Elements:
        swc.MoveAssignedSplits(icFile, icInternalFile)
    for connector in ic.Connectors.Elements:
        connector.MoveAssignedSplits(icFile, icInternalFile)
    if Options.UseFrontIndicatorEcus:
        # arComtypePackage = Utilities.GetElementByPath("/AUTOSAR_Comtype")
        # arComtypeFile = sdProject.MasterFiles.Add("<ProjectDir>\\_StandardFiles\\AUTOSAR_Comtype.arxml")
        # arComtypeFile.AddPackage(arComtypePackage)
        canBodyClusterFile = sdProject.MasterFiles.Add("<ProjectDir>\\MasterFiles\\CanBodyCluster.arxml")
        canBodyClusterFile.AddPackage(ecusPackage)
        canBodyClusterFile.AddPackage(canBodyPackage)
    else:
        ecusFile = sdProject.MasterFiles.Add("<ProjectDir>\\MasterFiles\\Ecus.arxml")
        ecusFile.AddPackage(ecusPackage)
    indicatorSystemFile = sdProject.MasterFiles.Add("<ProjectDir>\\MasterFiles\\IndicatorSystem.arxml")
    indicatorSystemFile.AddPackage(indicatorSystemPackage)


def SaveMasterFiles():
    """
    Saves all defined master files.
    """
    print("Saving master files")

    sdProject = SdApplication.ActiveProject
    sdProject.Serializer.SaveMasterFiles(sdProject.MasterFiles.Elements)


def ExportSystemExtract():
    """
    Exports an AUTOSAR system extract for the Central Body ECU.
    """
    print("Exporting AUTOSAR system extract for CentralBodyEcu")

    # Get existing project elements.
    pkgSystemsTutorial = Utilities.GetOrCreatePackage("/Systems/" + Options.SystemName)
    centralBodyEcu = Utilities.GetElementByPath("/EcuInstances/CentralBodyEcu/CentralBodyEcu")
    sysTutorial = pkgSystemsTutorial.Elements.Item(Options.SystemName)

    # Create directory for the system extract if necessary.
    projectRootDir = Utilities.GetProjectRootDir()
    systemExtractDir = os.path.join(projectRootDir, "_SystemFiles", "SystemExtracts")
    if not os.path.exists(systemExtractDir):
        os.mkdir(systemExtractDir)

    # Export the system extract.
    includedEcus = [centralBodyEcu]
    includeNotMappedSWCs = False
    systemExtractFile = os.path.join(systemExtractDir, "CentralBodyEcuSystemExtract.arxml")
    if os.path.exists(systemExtractFile):
        os.remove(systemExtractFile)
    sysTutorial.CreateSystemExtract(includedEcus, includeNotMappedSWCs, systemExtractFile)


def LoadMasterFiles():
    """
    Loads master files into an empty SystemDesk project.
    """

    # Create a SystemDesk project and import template files.
    CreateProjectAndPackages()
    # Remove unnecessary elements which have been imported from the template files.
    CleanupProjectAndPackages()
    SdProject = SdApplication.ActiveProject


    # Check existence of directory with master files.
    projectRootDir = Utilities.GetProjectRootDir()
    masterFilesPath = os.path.join(projectRootDir, "MasterFiles")
    if not os.path.exists(masterFilesPath):
        raise Exception(f"Directory {masterFilesPath} for master files does not exist.")

    # Define master files.
    SdProject.MasterFiles.Add("<ProjectDir>\\_SharedFiles\\SharedElements.arxml")
    SdProject.MasterFiles.Add("<ProjectDir>\\_ComponentFiles\\TurnSwitchSensor\\TurnSwitchSensor.arxml")
    SdProject.MasterFiles.Add("<ProjectDir>\\_ComponentFiles\\WarnLightsSensor\\WarnLightsSensor.arxml")
    SdProject.MasterFiles.Add("<ProjectDir>\\_ComponentFiles\\BulbActuator\\BulbActuator.arxml")
    SdProject.MasterFiles.Add("<ProjectDir>\\_ComponentFiles\\IndicatorLogic\\IndicatorLogic.arxml")
    SdProject.MasterFiles.Add("<ProjectDir>\\MasterFiles\\RootSwComposition.arxml")
    SdProject.MasterFiles.Add("<ProjectDir>\\MasterFiles\\IndicatorComposition.arxml")
    SdProject.MasterFiles.Add("<ProjectDir>\\MasterFiles\\IndicatorComposition_Internal.arxml")
    if Options.UseFrontIndicatorEcus:
        SdProject.MasterFiles.Add("<ProjectDir>\\MasterFiles\\CanBodyCluster.arxml")
    else:
        SdProject.MasterFiles.Add("<ProjectDir>\\MasterFiles\\Ecus.arxml")
    SdProject.MasterFiles.Add("<ProjectDir>\\MasterFiles\\IndicatorSystem.arxml")

    # Load the master files.
    print("Loading master files")
    SdProject.Serializer.LoadMasterFiles(SdProject.MasterFiles.Elements)


"""
##################
Lesson13_Complete()
##################
"""
def CreateCentralBodyEcuConfiguration():
    """
    Creates an ECU configuration and an ECU software composition for CentralBodyEcu.
    """
    # Elements needed by this ECU configuration.
    pkgSystems = Utilities.GetOrCreatePackage("/Systems/" + Options.SystemName)
    system = pkgSystems.Elements.Item(Options.SystemName)
    ecuInstance = Utilities.GetElementByPath("/EcuInstances/CentralBodyEcu/CentralBodyEcu")

    # Create a new ECU configuration.
    ecuConfigurationManager = SdApplication.EcuConfigurationManager
    ecuConfiguration = ecuConfigurationManager.CreateNewEcuConfiguration(system, ecuInstance)
    ecuConfiguration.Name = "CentralBodyEcuConfig"
    print(f"Creating ECU configuration {ecuConfiguration.Name}.")

    # The Simulator Abstraction module (Sab) is required for Simulation.
    sabConfiguration = Utilities.AddModuleConfiguration(ecuConfiguration, "Sab")
    sabConfiguration.SabStateManagement.SabAutostart = True
    sabConfiguration.SabStateManagement.SabStartupFunction = "EcuM_Init"

    # Create the Platform module. Needed for compilation with MCU.
    platformConfiguration = Utilities.AddModuleConfiguration(ecuConfiguration, "Platform")
    platformConfiguration.PlatformBaseTypes.PlatformGeneratePlatformTypes = True
    platformConfiguration.PlatformStandardTypes.PlatformGenerateStandardTypes = True
    platformConfiguration.PlatformCompilerAbstraction.PlatformGenerateCompilerAbstraction = True

    # Create module configuration for ECU State Manager (EcuM).
    ecuMConfiguration = Utilities.AddModuleConfiguration(ecuConfiguration, "EcuM")
    ecuMConfiguration.EcuMGeneral.EcuMMinimumMode = True
    ecuMConfiguration.EcuMGeneral.EcuMMainFunctionPeriod = 0.020

    # Create module configurations for OS and RTE.
    Utilities.AddModuleConfiguration(ecuConfiguration, "Os")
    Utilities.AddModuleConfiguration(ecuConfiguration, "Rte")

    # Create MemMap module.
    Utilities.AddModuleConfiguration(ecuConfiguration, "MemMap")

    # Create the COM stack modules.
    if Options.UseFrontIndicatorEcus:
        platformConfiguration.PlatformComStackTypes.PlatformGenerateComStackTypes = True
        Utilities.AddModuleConfiguration(ecuConfiguration, "EcuC")
        Utilities.AddModuleConfiguration(ecuConfiguration, "Com")
        Utilities.AddModuleConfiguration(ecuConfiguration, "CanIf")
        Utilities.AddModuleConfiguration(ecuConfiguration, "Can")
        Utilities.AddModuleConfiguration(ecuConfiguration, "PduR")

    # Create the modules for IO.
    Utilities.AddModuleConfiguration(ecuConfiguration, "IoHwAb")
    Utilities.AddModuleConfiguration(ecuConfiguration, "Dap")


def CreateCentralBodyIoHwAb():
    """
    Creates the IO hardware abstraction component for the CentralBodyEcu.
    Also connects the IoHwAb component to the SW architecture.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("CentralBodyEcuConfig")
    ioHwAbConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "IoHwAb")

    # Determine the data elements which shall be connected to the IO hardware abstraction
    ecuFlatView = ecuConfiguration.EcuExtractSystem.RootSwCompositionPrototype
    rootSwComposition = ecuFlatView.SoftwareCompositionTref
    ioSignalTss = Utilities.GetOperationIRef(rootSwComposition, "TurnSwitchSensor", "io_tss", "OP_GET")
    ioSignalWls = Utilities.GetDataElementIRef(rootSwComposition, "WarnLightsSensor", "io_wls", "value")
    ioSignals = [ioSignalTss, ioSignalWls]
    if not Options.UseFrontIndicatorEcus:
        ioSignalFla = Utilities.GetOperationIRef(rootSwComposition, "FrontLeftActuator", "io_bulb", "OP_SET")
        ioSignalFra = Utilities.GetOperationIRef(rootSwComposition, "FrontRightActuator", "io_bulb", "OP_SET")
        ioSignals += [ioSignalFla, ioSignalFra]

    # Select interface elements for the IoHwAb module.
    Utilities.RunBswPlugin(ioHwAbConfiguration, "Select Interface Elements", ioSignals)

    # Set signal age.
    ioHwAbConfiguration.IoHwAbGeneral.DefaultSampleFunctionSampleTime = 0.010
    for ioHwAbSignal in ioHwAbConfiguration.IoHwAbSignal.SenderReceivers.Elements:
        ioHwAbSignal.Age = 0.010
    for ioHwAbSignal in ioHwAbConfiguration.IoHwAbSignal.ClientServers.Elements:
        ioHwAbSignal.Age = 0.010

    # Run plugin methods of IoHwAb and Dap module.
    Utilities.StartBswGeneration(ecuConfiguration, "1 Update Configurations")


def CreateCentralBodyComConfiguration():
    """
    Create the COM configuration for CentralBodyEcu.
    """
    # Configure the COM stack modules (EcuC, Com, PduR, CanIf, Can).
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("CentralBodyEcuConfig")
    canConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Can")
    canConfiguration.CanGeneral.CanMainFunctionModePeriod = 0.010


def CreateCentralBodyEcuMConfiguration():
    """
    Create ECU State Manager (EcuM) configuration for CentralBodyEcu.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("CentralBodyEcuConfig")

    # Configure the EcuM module.
    ecuMConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "EcuM")
    ecuMConfiguration.EcuMGeneral.EcuMMinimumMode = True
    ecuMConfiguration.EcuMGeneral.EcuMMainFunctionPeriod = 0.020

    # This method also modifies Rte, Os.
    Utilities.StartBswGeneration(ecuConfiguration, "2 Update Components")


def CreateCentralBodyOsConfiguration():
    """
    Create the OS configuration for CentralBodyEcu.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("CentralBodyEcuConfig")
    osConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Os")

    # Get enum definitions for the OS configuration.
    osEnums = __import__(osConfiguration.PythonEnumerationFile)

    # OSEK application mode.
    applicationMode = osConfiguration.OsAppModes.Item("OSDEFAULTAPPMODE")
    if not applicationMode:
        applicationMode = osConfiguration.OsAppModes.Add("OSDEFAULTAPPMODE")

    # Create Task_10ms
    task10ms = osConfiguration.OsTasks.Add("Task_10ms")
    task10ms.OsTaskPriority = 7  ## priority higher than 20ms-task but lower than BSW tasks.
    task10ms.OsTaskSchedule = osEnums.OsTaskSchedule.FULL
    task10ms.OsTaskActivation = 1
    task10ms.OsTaskPeriod = 0.010

    # Create an event to trigger runnable 'WlsRunnable' in extended task 'Task_WlsPreprocessing'
    eventWlsRunnable = osConfiguration.OsEvents.Add("Event_WlsRunnable")
    eventWlsRunnable.OsEventMask = 0x01

    # Create an event to trigger runnable 'WlsPreprocessing' in extended task 'Task_WlsPreprocessing'
    eventWlsPreprocessing = osConfiguration.OsEvents.Add("Event_WlsPreprocessing")
    eventWlsPreprocessing.OsEventMask = 0x02

    # Create Task_WlsPreprocessing
    taskWlsPreprocessing = osConfiguration.OsTasks.Add("Task_WlsPreprocessing")
    taskWlsPreprocessing.OsTaskPriority = 20  ## Highest priority of all application tasks.
    taskWlsPreprocessing.OsTaskSchedule = osEnums.OsTaskSchedule.FULL
    taskWlsPreprocessing.OsTaskActivation = 1
    taskWlsPreprocessing.OsTaskEventRefs.Add(eventWlsRunnable)
    taskWlsPreprocessing.OsTaskEventRefs.Add(eventWlsPreprocessing)
    # Start the extended task when the OS starts and let it wait for events.
    taskWlsPreprocessing.AddOsTaskAutostart()
    taskWlsPreprocessing.OsTaskAutoStart.OsTaskAppModeRefs.Add(applicationMode)

    # Create task for FrontLeft/RightActuator runnables if FLA / FRA runs on this ECU.
    if not Options.UseFrontIndicatorEcus:
        # Create Task_100ms
        task100ms = osConfiguration.OsTasks.Add("Task_100ms")
        task100ms.OsTaskPriority = 1 ## Lowest priority.
        task100ms.OsTaskSchedule = osEnums.OsTaskSchedule.FULL
        task100ms.OsTaskActivation = 1
        task100ms.OsTaskPeriod = 0.100


def CreateCentralBodyRunnableMapping():
    """
    Create the runnable mapping for the CentralBodyEcu.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("CentralBodyEcuConfig")

    # Get Rte module and Os module.
    rteConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Rte")
    rteEnums = __import__(rteConfiguration.PythonEnumerationFile)
    osConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Os")

    # Update the Rte configuration to initialize the list of SwComponentInstances.
    Utilities.RunBswPlugin(rteConfiguration, "Update Rte Configuration")

    # Map runnables and BSW main functions.
    task10ms = osConfiguration.OsTasks.Item("Task_10ms")
    rteTask10ms = rteConfiguration.RteOsInteractions.Elements[0].RteUsedOsActivations.Item("Task_10ms")
    rteTask10ms.RteActivationOsTaskRef = task10ms
    rteTask10ms.RteExpectedTickDuration = 0.010
    rteTask10ms.RteExpectedTaskType = rteEnums.RteExpectedTaskType.BASIC
    Utilities.AddRteEventMapping(ecuConfiguration, \
        task10ms, "TurnSwitchSensor", "TssCyclic20ms")
    Utilities.AddRteEventMapping(ecuConfiguration, \
        task10ms, "IndicatorLogic", "TssCyclic10ms")
    Utilities.AddRteEventMapping(ecuConfiguration, \
        task10ms, "IndicatorLogic", "LogicCyclic10ms")
    Utilities.AddRteEventMapping(ecuConfiguration, \
        task10ms, "IndicatorLogic", "ToggleCyclic10ms")

    # Map runnables on Task_WlsPreprocessing.
    taskWlsPreprocessing = osConfiguration.OsTasks.Item("Task_WlsPreprocessing")
    rteTaskWlsPreprocessing = rteConfiguration.RteOsInteractions.Elements[0].RteUsedOsActivations.Item("Task_WlsPreprocessing")
    rteTaskWlsPreprocessing.RteActivationOsTaskRef = taskWlsPreprocessing
    rteTaskWlsPreprocessing.RteExpectedTickDuration = -1
    rteTaskWlsPreprocessing.RteExpectedTaskType = rteEnums.RteExpectedTaskType.EXTENDED
    # Trigger 'WlsRunnable' with OS event 'Event_WlsRunnable'.
    Utilities.AddRteEventMapping(ecuConfiguration, \
        taskWlsPreprocessing, "WarnLightsSensor", "WlsReceivedEvent", \
        osConfiguration.OsEvents.Item("Event_WlsRunnable"))
    # Trigger 'WlsPreprocessing' with OS event 'Event_WlsPreprocessing'.
    Utilities.AddRteEventMapping(ecuConfiguration, \
        taskWlsPreprocessing, "IndicatorLogic", "WlsReceivedEvent", \
        osConfiguration.OsEvents.Item("Event_WlsPreprocessing"))

    # Create mapping for FrontLeftActuator (FrontRightActuator) runnables if FLA (FRA) runs on this ECU.
    if not Options.UseFrontIndicatorEcus:
        # Map runnables on Task_100ms.
        task100ms = osConfiguration.OsTasks.Item("Task_100ms")
        rteTask100ms = rteConfiguration.RteOsInteractions.Elements[0].RteUsedOsActivations.Item("Task_100ms")
        rteTask100ms.RteActivationOsTaskRef = task100ms
        rteTask100ms.RteExpectedTickDuration = 0.100
        rteTask100ms.RteExpectedTaskType = rteEnums.RteExpectedTaskType.BASIC
        Utilities.AddRteEventMapping(ecuConfiguration, \
            task100ms, "FrontLeftActuator", "BulbCyclic100ms")
        Utilities.AddRteEventMapping(ecuConfiguration, \
            task100ms, "FrontRightActuator", "BulbCyclic100ms")

def GenerateCodeForCentralBodyEcu():
    """
    Generates the RTE for CentralBodyEcu.
    """
    ecuConfigurations = SdApplication.ActiveProject.EcuConfigurations

    # Set RTE options for CentralBodyEcu.
    centralBodyEcuConfiguration = ecuConfigurations.Item("CentralBodyEcuConfig")
    centralBodyRteConfiguration = Utilities.FindModuleConfiguration(centralBodyEcuConfiguration, "Rte")
    rteEnums = __import__(centralBodyRteConfiguration.PythonEnumerationFile)
    centralBodyRteConfiguration.RteGeneration.RteCompilerAbstractionEnabled = True
    centralBodyRteConfiguration.RteGeneration.RteGeneratePlatformTypes = False
    centralBodyRteConfiguration.RteGeneration.RteGenerateStdTypes = False
    centralBodyRteConfiguration.RteGeneration.RteGenerateStdAutosarTypes = False
    centralBodyRteConfiguration.RteGeneration.RteMeasurementSupport = True
    centralBodyRteConfiguration.RteGeneration.RteCalibrationSupport = rteEnums.RteCalibrationSupport.INITIALIZED_RAM
    centralBodyRteConfiguration.RteGeneration.RteTreatUnconnectedPortAsWarning = True
    centralBodyRteConfiguration.RteGeneration.RteMemoryMappingEnabled = False
    centralBodyRteConfiguration.RteGeneration.RteFunctionOptimization = True

    # Generate V-ECU implementation for CentralBodyEcu.
    print(f"Generating RTE for {centralBodyEcuConfiguration.Name}.")
    ##Utilities.StartBswGeneration(centralBodyEcuConfiguration, "1 Update Configurations")
    ##Utilities.StartBswGeneration(centralBodyEcuConfiguration, "2 Update Components")
    Utilities.StartBswGeneration(centralBodyEcuConfiguration, "3 Generate Code")
    ##Utilities.StartBswGeneration(centralBodyEcuConfiguration, "V-ECU Implementation")


def CreateFrontLeftIndicatorEcuConfiguration():
    """
    Creates an ECU configuration and an ECU software composition for FrontLeftIndicatorEcu.
    """
    # Elements needed by this ECU configuration.
    pkgSystems = Utilities.GetOrCreatePackage("/Systems/" + Options.SystemName)
    system = pkgSystems.Elements.Item(Options.SystemName)
    ecuInstance = Utilities.GetElementByPath("/EcuInstances/FrontLeftIndicatorEcu/FrontLeftIndicatorEcu")

    # Create a new ECU configuration.
    ecuConfigurationManager = SdApplication.EcuConfigurationManager
    ecuConfiguration = ecuConfigurationManager.CreateNewEcuConfiguration(system, ecuInstance)
    ecuConfiguration.Name = "FrontLeftIndicatorEcuConfig"
    print(f"Creating ECU configuration {ecuConfiguration.Name}.")

    # The Simulator Abstraction module (Sab) is required for Simulation.
    sabConfiguration = Utilities.AddModuleConfiguration(ecuConfiguration, "Sab")
    sabConfiguration.SabStateManagement.SabAutostart = True
    sabConfiguration.SabStateManagement.SabStartupFunction = "EcuM_Init"

    # Create the Platform module. Needed for compilation with MCU.
    platformConfiguration = Utilities.AddModuleConfiguration(ecuConfiguration, "Platform")
    platformConfiguration.PlatformBaseTypes.PlatformGeneratePlatformTypes = True
    platformConfiguration.PlatformStandardTypes.PlatformGenerateStandardTypes = True
    platformConfiguration.PlatformCompilerAbstraction.PlatformGenerateCompilerAbstraction = True

    # Create module configuration for ECU State Manager (EcuM).
    Utilities.AddModuleConfiguration(ecuConfiguration, "EcuM")

    # Create module configurations for OS and RTE.
    Utilities.AddModuleConfiguration(ecuConfiguration, "Os")
    Utilities.AddModuleConfiguration(ecuConfiguration, "Rte")

    # Create MemMap module.
    Utilities.AddModuleConfiguration(ecuConfiguration, "MemMap")

    # Create the COM stack modules.
    if Options.UseFrontIndicatorEcus:
        platformConfiguration.PlatformComStackTypes.PlatformGenerateComStackTypes = True
        Utilities.AddModuleConfiguration(ecuConfiguration, "EcuC")
        Utilities.AddModuleConfiguration(ecuConfiguration, "Com")
        Utilities.AddModuleConfiguration(ecuConfiguration, "CanIf")
        Utilities.AddModuleConfiguration(ecuConfiguration, "Can")
        Utilities.AddModuleConfiguration(ecuConfiguration, "PduR")

    # Create the modules for IO.
    Utilities.AddModuleConfiguration(ecuConfiguration, "IoHwAb")
    Utilities.AddModuleConfiguration(ecuConfiguration, "Dap")


def CreateFrontLeftIndicatorIoHwAb():
    """
    Creates the IO hardware abstraction component for the FrontLeftIndicatorEcu.
    Also connects the IoHwAb component to the SW architecture.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("FrontLeftIndicatorEcuConfig")
    ioHwAbConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "IoHwAb")

    # Determine the data elements which shall be connected to the IO hardware abstraction
    ecuFlatView = ecuConfiguration.EcuExtractSystem.RootSwCompositionPrototype
    rootSwComposition = ecuFlatView.SoftwareCompositionTref
    ioSignalBulb = Utilities.GetOperationIRef(rootSwComposition, "FrontLeftActuator", "io_bulb", "OP_SET")
    ioSignals = [ioSignalBulb]

    # Select interface elements for the IoHwAb module.
    Utilities.RunBswPlugin(ioHwAbConfiguration, "Select Interface Elements", ioSignals)

    # Set signal age.
    ioHwAbConfiguration.IoHwAbGeneral.DefaultSampleFunctionSampleTime = 0.100
    for ioHwAbSignal in ioHwAbConfiguration.IoHwAbSignal.ClientServers.Elements:
        ioHwAbSignal.Age = 0.100

    # Run plugin methods of IoHwAb and Dap module.
    Utilities.StartBswGeneration(ecuConfiguration, "1 Update Configurations")


def CreateFrontLeftIndicatorComConfiguration():
    """
    Create the COM configuration for FrontLeftIndicatorEcu.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("FrontLeftIndicatorEcuConfig")

    # The EcuC module has been updated after IoHwAb-Select-Signals.

    # Generate the AUTOSAR COM Configuration (ComIPduGroups, ComIPdus, ComSignals, PDUs, ...)
    comConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Com")
    comConfiguration.ComGeneral.ComConfigurationTimeBase = 0.100

    # Use ComDataInvalidAction REPLACE, because we don't have a notification callback in this demo.
    comEnums = __import__(comConfiguration.PythonEnumerationFile)
    comConfiguration.ComConfig.ComSignals.Item("ComLeftISignal").ComDataInvalidAction = comEnums.ComDataInvalidAction.REPLACE
    comConfiguration.ComConfig.ComSignals.Item("ComRightISignal").ComDataInvalidAction = comEnums.ComDataInvalidAction.REPLACE

    # Configuring Can
    canConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Can")
    canConfiguration.CanGeneral.CanMainFunctionModePeriod = 0.010


def CreateFrontLeftIndicatorEcuMConfiguration():
    """
    Create ECU State Manager (EcuM) configuration for FrontLeftIndicatorEcu.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("FrontLeftIndicatorEcuConfig")

    # Configure the EcuM module.
    ecuMConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "EcuM")
    ecuMConfiguration.EcuMGeneral.EcuMMinimumMode = True
    ecuMConfiguration.EcuMGeneral.EcuMMainFunctionPeriod = 0.100

    # This method also modifies Rte, Os.
    Utilities.StartBswGeneration(ecuConfiguration, "2 Update Components")


def CreateFrontLeftIndicatorOsConfiguration():
    """
    Create the OS configuration for FrontLeftIndicatorEcu.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("FrontLeftIndicatorEcuConfig")
    osConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Os")

    # Get enum definitions for the OS configuration.
    osEnums = __import__(osConfiguration.PythonEnumerationFile)

    # OSEK application mode.
    applicationMode = osConfiguration.OsAppModes.Item("OSDEFAULTAPPMODE")
    if not applicationMode:
        applicationMode = osConfiguration.OsAppModes.Add("OSDEFAULTAPPMODE")

    # Create Task_100ms
    task100ms = osConfiguration.OsTasks.Add("Task_100ms")
    task100ms.OsTaskPriority = 2  ## Highest cyclic priority for application tasks.
    task100ms.OsTaskSchedule = osEnums.OsTaskSchedule.FULL
    task100ms.OsTaskActivation = 1
    task100ms.OsTaskPeriod = 0.100


def CreateFrontLeftIndicatorRunnableMapping():
    """
    Create the runnable mapping for FrontLeftIndicatorEcu.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("FrontLeftIndicatorEcuConfig")

    # Get Rte module and Os module.
    rteConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Rte")
    rteEnums = __import__(rteConfiguration.PythonEnumerationFile)
    osConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Os")

    # Update the Rte configuration to initialize the list of SwComponentInstances.
    Utilities.RunBswPlugin(rteConfiguration, "Update Rte Configuration")

     # Map runnables on Task_100ms.
    task100ms = osConfiguration.OsTasks.Item("Task_100ms")
    rteTask100ms = rteConfiguration.RteOsInteractions.Elements[0].RteUsedOsActivations.Item("Task_100ms")
    rteTask100ms.RteActivationOsTaskRef = task100ms
    rteTask100ms.RteExpectedTickDuration = 0.100
    rteTask100ms.RteExpectedTaskType = rteEnums.RteExpectedTaskType.BASIC
    Utilities.AddRteEventMapping(ecuConfiguration, \
        task100ms, "FrontLeftActuator", "BulbCyclic100ms")


def GenerateCodeForFrontLeftIndicatorEcu():
    """
    Generates the RTE for FrontLeftIndicatorEcu.
    """
    ecuConfigurations = SdApplication.ActiveProject.EcuConfigurations

    # Set RTE options for FrontLeftIndicatorEcu.
    frontLeftIndicatorEcuConfiguration = ecuConfigurations.Item("FrontLeftIndicatorEcuConfig")
    frontLeftIndicatorRteConfiguration = Utilities.FindModuleConfiguration(frontLeftIndicatorEcuConfiguration, "Rte")
    rteEnums = __import__(frontLeftIndicatorRteConfiguration.PythonEnumerationFile)
    frontLeftIndicatorRteConfiguration.RteGeneration.RteCompilerAbstractionEnabled = True
    frontLeftIndicatorRteConfiguration.RteGeneration.RteGeneratePlatformTypes = False
    frontLeftIndicatorRteConfiguration.RteGeneration.RteGenerateStdTypes = False
    frontLeftIndicatorRteConfiguration.RteGeneration.RteGenerateStdAutosarTypes = False
    frontLeftIndicatorRteConfiguration.RteGeneration.RteMeasurementSupport = True
    frontLeftIndicatorRteConfiguration.RteGeneration.RteCalibrationSupport = rteEnums.RteCalibrationSupport.INITIALIZED_RAM
    frontLeftIndicatorRteConfiguration.RteGeneration.RteTreatUnconnectedPortAsWarning = True
    frontLeftIndicatorRteConfiguration.RteGeneration.RteMemoryMappingEnabled = False
    frontLeftIndicatorRteConfiguration.RteGeneration.RteFunctionOptimization = True

    # Generate the RTE for FrontLeftIndicatorEcu.
    print(f"Generating RTE for {frontLeftIndicatorEcuConfiguration.Name}.")
    Utilities.StartBswGeneration(frontLeftIndicatorEcuConfiguration, "3 Generate Code")


def CreateFrontRightIndicatorEcuConfiguration():
    """
    Creates an ECU configuration and an ECU software composition for FrontRightIndicatorEcu.
    """

    # Elements needed by this ECU configuration.
    pkgSystems = Utilities.GetOrCreatePackage("/Systems/" + Options.SystemName)
    system = pkgSystems.Elements.Item(Options.SystemName)
    ecuInstance = Utilities.GetElementByPath("/EcuInstances/FrontRightIndicatorEcu/FrontRightIndicatorEcu")

    # Create a new ECU configuration.
    ecuConfigurationManager = SdApplication.EcuConfigurationManager
    ecuConfiguration = ecuConfigurationManager.CreateNewEcuConfiguration(system, ecuInstance)
    ecuConfiguration.Name = "FrontRightIndicatorEcuConfig"
    print(f"Creating ECU configuration {ecuConfiguration.Name}.")

    # The Simulator Abstraction module (Sab) is required for Simulation.
    sabConfiguration = Utilities.AddModuleConfiguration(ecuConfiguration, "Sab")
    sabConfiguration.SabStateManagement.SabAutostart = True
    sabConfiguration.SabStateManagement.SabStartupFunction = "EcuM_Init"

    # Create the Platform module. Needed for compilation with MCU.
    platformConfiguration = Utilities.AddModuleConfiguration(ecuConfiguration, "Platform")
    platformConfiguration.PlatformBaseTypes.PlatformGeneratePlatformTypes = True
    platformConfiguration.PlatformStandardTypes.PlatformGenerateStandardTypes = True
    platformConfiguration.PlatformCompilerAbstraction.PlatformGenerateCompilerAbstraction = True

    # Create module configuration for ECU State Manager (EcuM).
    Utilities.AddModuleConfiguration(ecuConfiguration, "EcuM")

    # Create module configurations for OS and RTE.
    Utilities.AddModuleConfiguration(ecuConfiguration, "Os")
    Utilities.AddModuleConfiguration(ecuConfiguration, "Rte")

    # Create MemMap module.
    Utilities.AddModuleConfiguration(ecuConfiguration, "MemMap")

    # Create the COM stack modules.
    if Options.UseFrontIndicatorEcus:
        platformConfiguration.PlatformComStackTypes.PlatformGenerateComStackTypes = True
        Utilities.AddModuleConfiguration(ecuConfiguration, "EcuC")
        Utilities.AddModuleConfiguration(ecuConfiguration, "Com")
        Utilities.AddModuleConfiguration(ecuConfiguration, "CanIf")
        Utilities.AddModuleConfiguration(ecuConfiguration, "Can")
        Utilities.AddModuleConfiguration(ecuConfiguration, "PduR")

    # Create the modules for IO.
    Utilities.AddModuleConfiguration(ecuConfiguration, "IoHwAb")
    Utilities.AddModuleConfiguration(ecuConfiguration, "Dap")


def CreateFrontRightIndicatorIoHwAb():
    """
    Creates the IO hardware abstraction component for the FrontRightIndicatorEcu.
    Also connects the IoHwAb component to the SW architecture.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("FrontRightIndicatorEcuConfig")
    ioHwAbConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "IoHwAb")

    # Determine the data elements which shall be connected to the IO hardware abstraction
    ecuFlatView = ecuConfiguration.EcuExtractSystem.RootSwCompositionPrototype
    rootSwComposition = ecuFlatView.SoftwareCompositionTref
    ioSignalBulb = Utilities.GetOperationIRef(rootSwComposition, "FrontRightActuator", "io_bulb", "OP_SET")
    ioSignals = [ioSignalBulb]

    # Select interface elements for the IoHwAb module.
    Utilities.RunBswPlugin(ioHwAbConfiguration, "Select Interface Elements", ioSignals)

    # Set signal age.
    ioHwAbConfiguration.IoHwAbGeneral.DefaultSampleFunctionSampleTime = 0.100
    for ioHwAbSignal in ioHwAbConfiguration.IoHwAbSignal.ClientServers.Elements:
        ioHwAbSignal.Age = 0.100

    # Run plugin methods of IoHwAb and Dap module.
    Utilities.StartBswGeneration(ecuConfiguration, "1 Update Configurations")


def CreateFrontRightIndicatorComConfiguration():
    """
    Create the COM configuration for FrontRightIndicatorEcu.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("FrontRightIndicatorEcuConfig")

    # The EcuC module has been updated after IoHwAb-Select-Signals.

    # Generate the AUTOSAR COM Configuration (ComIPduGroups, ComIPdus, ComSignals, PDUs, ...)
    comConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Com")
    comConfiguration.ComGeneral.ComConfigurationTimeBase = 0.100

    # Use ComDataInvalidAction REPLACE, because we don't have a notification callback in this demo.
    comEnums = __import__(comConfiguration.PythonEnumerationFile)
    comConfiguration.ComConfig.ComSignals.Item("ComLeftISignal").ComDataInvalidAction = comEnums.ComDataInvalidAction.REPLACE
    comConfiguration.ComConfig.ComSignals.Item("ComRightISignal").ComDataInvalidAction = comEnums.ComDataInvalidAction.REPLACE

    # Configuring Can
    canConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Can")
    canConfiguration.CanGeneral.CanMainFunctionModePeriod = 0.010


def CreateFrontRightIndicatorEcuMConfiguration():
    """
    Create ECU State Manager (EcuM) configuration for FrontRightIndicatorEcu.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("FrontRightIndicatorEcuConfig")

    # Configure the EcuM module.
    ecuMConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "EcuM")
    ecuMConfiguration.EcuMGeneral.EcuMMinimumMode = True
    ecuMConfiguration.EcuMGeneral.EcuMMainFunctionPeriod = 0.100

    # This method also modifies Rte, Os.
    Utilities.StartBswGeneration(ecuConfiguration, "2 Update Components")


def CreateFrontRightIndicatorOsConfiguration():
    """
    Create the OS configuration for FrontRightIndicatorEcu.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("FrontRightIndicatorEcuConfig")
    osConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Os")

    # Get enum definitions for the OS configuration.
    osEnums = __import__(osConfiguration.PythonEnumerationFile)

    # OSEK application mode.
    applicationMode = osConfiguration.OsAppModes.Item("OSDEFAULTAPPMODE")
    if not applicationMode:
        applicationMode = osConfiguration.OsAppModes.Add("OSDEFAULTAPPMODE")

    # Create Task_100ms
    task100ms = osConfiguration.OsTasks.Add("Task_100ms")
    task100ms.OsTaskPriority = 2  ## Highest cyclic priority for application tasks.
    task100ms.OsTaskSchedule = osEnums.OsTaskSchedule.FULL
    task100ms.OsTaskActivation = 1
    task100ms.OsTaskPeriod = 0.100


def CreateFrontRightIndicatorRunnableMapping():
    """
    Create the runnable mapping for FrontRightIndicatorEcu.
    """
    ecuConfiguration = SdApplication.ActiveProject.EcuConfigurations.Item("FrontRightIndicatorEcuConfig")

    # Get Rte module and Os module.
    rteConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Rte")
    rteEnums = __import__(rteConfiguration.PythonEnumerationFile)
    osConfiguration = Utilities.FindModuleConfiguration(ecuConfiguration, "Os")

    # Update the Rte configuration to initialize the list of SwComponentInstances.
    Utilities.RunBswPlugin(rteConfiguration, "Update Rte Configuration")

     # Map runnables on Task_100ms.
    task100ms = osConfiguration.OsTasks.Item("Task_100ms")
    rteTask100ms = rteConfiguration.RteOsInteractions.Elements[0].RteUsedOsActivations.Item("Task_100ms")
    rteTask100ms.RteActivationOsTaskRef = task100ms
    rteTask100ms.RteExpectedTickDuration = 0.100
    rteTask100ms.RteExpectedTaskType = rteEnums.RteExpectedTaskType.BASIC
    Utilities.AddRteEventMapping(ecuConfiguration, \
        task100ms, "FrontRightActuator", "BulbCyclic100ms")


def GenerateCodeForFrontRightIndicatorEcu():
    """
    Generates the RTE for FrontRightIndicatorEcu.
    """
    ecuConfigurations = SdApplication.ActiveProject.EcuConfigurations

    # Set RTE options for FrontRightIndicatorEcu.
    frontRightIndicatorEcuConfiguration = ecuConfigurations.Item("FrontRightIndicatorEcuConfig")
    frontRightIndicatorRteConfiguration = Utilities.FindModuleConfiguration(frontRightIndicatorEcuConfiguration, "Rte")
    rteEnums = __import__(frontRightIndicatorRteConfiguration.PythonEnumerationFile)
    frontRightIndicatorRteConfiguration.RteGeneration.RteCompilerAbstractionEnabled = True
    frontRightIndicatorRteConfiguration.RteGeneration.RteGeneratePlatformTypes = False
    frontRightIndicatorRteConfiguration.RteGeneration.RteGenerateStdTypes = False
    frontRightIndicatorRteConfiguration.RteGeneration.RteGenerateStdAutosarTypes = False
    frontRightIndicatorRteConfiguration.RteGeneration.RteMeasurementSupport = True
    frontRightIndicatorRteConfiguration.RteGeneration.RteCalibrationSupport = rteEnums.RteCalibrationSupport.INITIALIZED_RAM
    frontRightIndicatorRteConfiguration.RteGeneration.RteTreatUnconnectedPortAsWarning = True
    frontRightIndicatorRteConfiguration.RteGeneration.RteMemoryMappingEnabled = False
    frontRightIndicatorRteConfiguration.RteGeneration.RteFunctionOptimization = True

    # Generate the RTE for FrontRightIndicatorEcu.
    print(f"Generating RTE for {frontRightIndicatorEcuConfiguration.Name}.")
    Utilities.StartBswGeneration(frontRightIndicatorEcuConfiguration, "3 Generate Code")


"""
###################
Lesson14_Complete()
###################
"""
def CreateVEcus():
    """
    Creates new V-ECUs for each EcuInstance if not existing yet
    """
    project = SdApplication.ActiveProject
    project.ClassicVEcus.Clear()

    for ecuConfiguration in project.EcuConfigurations.Elements:
        project.ClassicVEcus.AddNewModelBased(ecuConfiguration)

def GetVEcuXcpServicePort(vEcu):
    """
    Return the XCP port number for given V-ECU
    """
    if vEcu.Name == "CentralBodyEcu":
        return 30300
    if vEcu.Name == "FrontLeftIndicatorEcu":
        return 30302
    # FrontRightIndicatorEcu
    return 30304

def GetVeosOsaDirectory():
    """
    Returns the OSA directory.
    """
    return os.path.join(Utilities.GetProjectRootDir(), "..\\VEOS", "IndicatorSystem")

def GetVeosOsaPath():
    """
    Returns the full path of the OSA file.
    """
    return os.path.join(GetVeosOsaDirectory(), "IndicatorSystem.osa")

def GetVEcuExportPath(vEcu):
    """
    Returns the path where the V-ECU will be exported to.
    """
    exportDir = os.path.join(Utilities.GetProjectRootDir(), Options.ProjectName)
    return os.path.abspath(os.path.join(exportDir, vEcu.Name + ".vecu"))

def BuildForVeos():
    """
    Build an Offline Simulation Application (OSA) for VEOS.
    """
    print("Building simulation system.")

    project = SdApplication.ActiveProject

    # "<ProjectDir>\\..\\VEOS\\<ProjectName>"
    osaDir = GetVeosOsaDirectory()

    try:
        vpApplication = Utilities.ConnectToVeosPlayer()
    except Exception:
        print("VEOS Player could not be dispatched.")
        return False

    # Always create new osa
    osaFile = GetVeosOsaPath()
    SdApplication.SubmitInfoMessage('VEOS Build', f"Building '{osaFile}' in VEOS Player...")

    vpProject = vpApplication.Projects.CreateNew(osaFile)
    if (not vpProject):
        SdApplication.SubmitInfoMessage('VEOS Build', f"OSA file '{osaFile}' could not be created.")
        raise Exception(f"OSA file '{osaFile}' could not be created.")

    success = True
    for vEcu in project.ClassicVEcus.Elements:
        buildStatus = Utilities.BuildForVeosUsingVeosPlayer(osaDir, GetVEcuExportPath(vEcu), vEcu.Name, GetVEcuXcpServicePort(vEcu))
        if buildStatus == Utilities.VpEnums.BuildStatusEnum.Invalid:
            success = False
        print(("Build finished with status: " + str(buildStatus)))

    SdApplication.SubmitInfoMessage('VEOS Build', f"Build finished with status: '{str(buildStatus)}'")

    if success:

        # Create CommunicationController elements and connect them
        vpProject.ConnectUnconnectedCommunicationControllers()

    if success and Options.SaveProject:
        vpProject.Save()

    return success


def ExportVEcuImplementations():
    """
    Exports V-ECU Implementation files (*.vecu) for all V-ECUs in a simulation system.
    """
    project = SdApplication.ActiveProject

    oldBatchMode = SdApplication.BatchMode
    try:
        SdApplication.BatchMode = True
        for vEcu in project.ClassicVEcus.Elements:
            vecuAbsPath = GetVEcuExportPath(vEcu)
            print(("Exporting V-ECU implementation " + vecuAbsPath))
            vEcu.ExportContainer(vecuAbsPath)
    finally:
        SdApplication.BatchMode = oldBatchMode

"""
################
Main entry point
################
"""
def Main():
    """
    Run the tutorial up to lesson 14.
    """
    Lesson14_Complete()

    # Save the SystemDesk project.
    if Options.SaveProject:
        Utilities.SaveProject()
        print("*** Saving " + Options.ProjectName + " project. ***")
    else:
        print("*** Project " + Options.ProjectName + " not saved. ***")


#-------------
# Run the demo
#-------------
if (__name__ == "__main__"):
    Main()
    print("Ready")
