"""
--------------------------------------------------------------------------------
File:        BasicProjectReport.py

Description: Creates a simple project report.

Tip/Remarks: -

Limitations: A SystemDesk project (e.g. Tutorial.sdp) must be open, when you
             run this script.

Version:     2023-B

Since:       2007-06-22

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

# Import required modules.
from win32com.client import Dispatch
# Open a COM connection to SystemDesk.
systemDeskApplication = Dispatch("SystemDesk.Application.2023-B")


def ReportComposition(composition, indent=""):
    """
    Creates a report for a composition.
    """
    swcCount = 0
    # Print the composition name.
    print(indent + "+ " + composition.ShortName)
    for swComponentPrototype in composition.Components.Elements:
        swComponentType = swComponentPrototype.TypeTRef
        if swComponentType.ElementType == "ICompositionSwComponentType":
            swcCount += ReportComposition(swComponentType, indent + "  ")
        else:
            # Print the component name.
            print(indent + "  | " + swComponentPrototype.ShortName)
            swcCount += 1
    return swcCount


def FindSystems(package):
    """
    Returns a tuple with all System elements in the given package and it's subpackages.
    """
    systems = ()
    for element in package.Elements.Elements:
        if element.ElementType == "ISystem":
            systems += (element,)
    for subpackage in package.ArPackages.Elements:
        systems += FindSystems(subpackage)
    return systems


def Main():
    """
    Main function.
    Iterates over all software architectures in a project and lists the
    contained compositions.
    """
    # Print the version of SystemDesk.
    version = systemDeskApplication.Version
    print("SystemDesk " + version)
    # Access the active project.
    project = systemDeskApplication.ActiveProject
    if not project:
        print("No active project found.")
        print("SCRIPT ABORTED.")
        return
    # Package containing AUTOSAR Systems.
    systemsPackage = project.RootAutosar.ArPackages.Item("Systems")
    if not systemsPackage:
        print("Package /Systems does not exist. No systems found.")
        print("SCRIPT ABORTED.")
        return
    # Count the number of systems in the active project.
    systems = FindSystems(systemsPackage)
    print(f"Number of systems in project {project.Name}: {len(systems)}")
    # Loop over all systems in package /Systems.
    for system in systems:
        # Print the system name.
        print("SYSTEM: " + system.ShortName)
        # Get the root software composition in the system.
        for rootSwCompositionPrototype in system.RootSoftwareCompositions.Elements:
            # Get the referenced composition.
            rootSwCompositionType = rootSwCompositionPrototype.SoftwareCompositionTref
            # Call the report function for the RootSwCompositionPrototype (top level composition)
            swcCount = ReportComposition(rootSwCompositionType)
            print(f"  {rootSwCompositionPrototype.ShortName} contains {swcCount} atomic software components.")

# Call the main routine.
if __name__ == "__main__":
    Main()
