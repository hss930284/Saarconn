"""
--------------------------------------------------------------------------------
File:        Tutorial_Simulation_1Ecu.py

Description: Configures the Tutorial demo project for implementation on one ECU
             and builds an Offline Simulation Application (OSA) for VEOS.
             This is the simplest variant of the demo without network communication.
             All components are mapped to CentralBodyEcu.

Tip/Remarks: -

Limitations: -

Version:     2023-B

Since:       2007-06-04

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
import Utilities
import Tutorial
importlib.reload(Utilities)
importlib.reload(Tutorial)


def Main():
    """
    Configure the Tutorial project for one ECU.
    """
    # Global configuration options (shared with Utilities).
    Options = Utilities.Options

    # Name of this project.
    Options.ProjectName = "TutorialProject_1Ecu"
    # Name of the AUTOSAR system.
    Options.SystemName = "IndicatorSystem_1Ecu"
    # Set True to create a separate ECUs for the front-left- and front-right-indicators.
    Options.UseFrontIndicatorEcus = False
    # Set True to import the network communication (Fibex) elements from a AUTOSAR System Description file.
    Options.ImportNetworkCommunicationElements = False

    # Run the Tutorial demo.
    Tutorial.Main()


#-------------
# Run the demo
#-------------
if (__name__ == "__main__"):
    Main()
    print("Ready")
