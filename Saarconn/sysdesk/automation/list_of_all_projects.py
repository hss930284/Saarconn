from win32com.client import Dispatch

# Initialize SystemDesk COM connection
systemDeskApplication = Dispatch("SystemDesk.Application")

def check_active_project():
    """
    Check and display the active project in the SystemDesk application.
    """
    try:
        active_project = systemDeskApplication.ActiveProject
        if active_project:
            print(f"Active Project: {active_project.Name}")
        else:
            print("No active project found.")
    except Exception as e:
        print(f"Error retrieving active project: {e}")

def main():
    # Check for active project
    check_active_project()

# Run the script
if __name__ == "__main__":
    main()
