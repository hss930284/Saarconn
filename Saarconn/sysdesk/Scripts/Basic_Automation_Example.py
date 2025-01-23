"""
--------------------------------------------------------------------------------
File:        Basic_Automation_Example.py

Description: Demonstrates how to create a (very simple) project with
             automation commands.

Tip/Remarks: -

Limitations: -

Version:     2023-B

Since:       2013-09-11

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
import sys
import os
from win32com.client import Dispatch

"""
###############################################
Connect to SystemDesk and create a new project.
###############################################
"""

# Open a COM connection to SystemDesk.
systemDeskApplication = Dispatch("SystemDesk.Application.2023-B")

# Project file name.
scriptDir = os.path.abspath(os.path.dirname(sys.argv[0]))
projectFile = os.path.dirname(scriptDir) + r"\Basic_Automation_Example.sdp"

# Create a new SystemDesk project
print(f"Using project file {projectFile}")
project = systemDeskApplication.CreateProject(projectFile)

"""
########################
Create project elements.
########################
"""
print("Creating project elements")

# Create a new package.
rootPackage = project.RootAUTOSAR
newPackage = rootPackage.ARPackages.AddNew()
newPackage.ShortName = "MyPackage"

# Create a new application software component with one port.
swc = newPackage.Elements.AddNewApplicationSwComponentType("SWC")
port = swc.Ports.AddNewPPortPrototype("Port")

print("Ready")
