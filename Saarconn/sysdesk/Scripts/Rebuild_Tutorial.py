"""
--------------------------------------------------------------------------------
File:        Rebuild_Tutorial.py

Description: Opens the SystemDesk project file TutorialProject.sdp and
             regenerates RTE and BSW module code. Creates a simulation system
             and builds an Offline Simulation Application (OSA) for VEOS.

Tip/Remarks: You can configure different variants of this demo with the
             options in line 55++.

Limitations: -

Version:     2023-B

Since:       2012-06-28

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

# Import python modules.
import importlib
import Utilities
import Tutorial
importlib.reload(Utilities)
importlib.reload(Tutorial)


def Main():
    """
    Configure the Tutorial project for one ECU.
    """
    # Get global configuration options (shared with Utilities).
    Options = Utilities.Options

    # Set True to open an existing SystemDesk project (SDP). Otherwise, the SystemDesk project is created from scratch.
    Options.OpenExistingProject = True

    # Run the demo script with the configured options.
    Tutorial.Main()


#-------------
# Run the demo
#-------------
if (__name__ == "__main__"):
    Main()
    print("Ready")
