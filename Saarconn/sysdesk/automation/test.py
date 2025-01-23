import win32com.client

# The win32com.client module is part of the pywin32 library, which provides access to many of the Windows APIs from Python. 
# This module allows you to interact with COM (Component Object Model) objects, enabling automation of Windows applications.

application=win32com.client.Dispatch("SystemDesk.Application")

# opening systemdesk

application.Visible=True

# visibility




