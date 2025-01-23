import os
import pandas as pd
import win32com.client

# Initialize SystemDesk COM connection
systemDeskApplication = win32com.client.Dispatch("SystemDesk.Application")

def create_project(project_name):
    """
    Create a new project in SystemDesk using the CreateProject method.
    """
    project_path = os.path.join("E:/sysdesk/automation/projects", project_name + ".sdp")
    project = systemDeskApplication.CreateProject(project_path)
    print(f"Project '{project_name}' created successfully.")
    return project

def create_systems_package(project, excel_file):
    """
    Create a 'Systems' package in the project based on Excel data.
    """
    root_package = project.RootAutosar.ArPackages

    # Check if the 'Systems' package already exists
    systems_package_name = "Systems"
    existing_package = None
    for pkg in root_package.Elements:
        if pkg.ShortName == systems_package_name:
            existing_package = pkg
            break

    # If the package doesn't exist, create it
    if not existing_package:
        systems_package = root_package.Add(systems_package_name, "APackage")
        print("Package 'Systems' created successfully.")
    else:
        systems_package = existing_package
        print("Package 'Systems' already exists.")

    # Read data from Excel
    data = pd.read_excel(excel_file)

    # Create compositions and components from Excel data
    compositions = {}

    for index, row in data.iterrows():
        composition_name = row['CompositionName']
        component_name = row['ComponentName']
        port_name = row['PortName']

        # Create composition if it doesn't exist
        if composition_name not in compositions:
            compositions[composition_name] = systems_package.Add(composition_name, "AComposition")
            print(f"Composition '{composition_name}' created.")

        # Add component to the composition
        component = compositions[composition_name].Components.Add(component_name, "AComponent")
        print(f"Component '{component_name}' added to composition '{composition_name}'.")

        # You can add ports or additional properties as needed
        port = component.Ports.Add(port_name, "APort")
        print(f"Port '{port_name}' added to component '{component_name}'.")

def main():
    project_name = "test_project2"  # Change this to your desired project name
    excel_file = "E:/sysdesk/automation/package_data.xlsx"  # Path to your Excel file

    # Always create a new project
    project = create_project(project_name)
    create_systems_package(project, excel_file)  # Create the 'Systems' package based on Excel data

# Run the script
if __name__ == "__main__":
    systemDeskApplication.Visible = True
    main()
