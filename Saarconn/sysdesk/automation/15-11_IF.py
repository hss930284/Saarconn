# Standard library imports
import importlib
import os
import re
import openpyxl
from pathlib import Path

# Third-party library imports
import pandas as pd  # Import pandas

# Local module imports
import Utilities
import SystemDeskEnums  # type: ignore # pylint: disable=wrong-import-position

# Reloading modules
importlib.reload(Utilities)  # Reloading Utilities
importlib.reload(SystemDeskEnums)  # Reloading SystemDeskEnums

# Connecting to SystemDesk (get COM object)
SdApplication = Utilities.ConnectToSystemDesk()

####################################----------*********** Excel related definitions *************--------------######################################

def ReadUserDefinedExcel():
    # Load the user defined Excel file
    global Input_Excel_File, current_sheet, sheet_name
    Input_Excel_File = input("Please provide the path of input Excel file (e.g., E:\\sysdesk\\automation): ")

    # Referring xls variable as entire excel
    global xls
    xls = pd.ExcelFile(Input_Excel_File)

    global first_sheet
    first_sheet = pd.read_excel(Input_Excel_File, sheet_name=0,header=None)
    global sd_project
    sd_project = first_sheet.iloc[4,3] # Get the project name from cell D5

    for sheet_name in xls.sheet_names[1:]:  # This will skip the first sheet
        current_sheet = pd.read_excel(Input_Excel_File, sheet_name=sheet_name, header=None)

def GetColumnValidIndex(CellNo, NextTableCellValue):
    global column_index
    # Extract column and row from the cell reference
    column_letter = ''.join(filter(str.isalpha, CellNo))
    row_number = int(''.join(filter(str.isdigit, CellNo)))

    # Convert column letter to a zero-based index
    column_index = ord(column_letter) - ord('A')

    # Initialize c and d
    first_valid_cell_reference = CellNo  # c is the current cell
    last_valid_cell_reference = None  # d will be determined later

    # Check if row_number is within bounds
    if row_number >= current_sheet.shape[0]:
        print(f"Warning: Row number {row_number} exceeds the DataFrame size {current_sheet.shape[0]}.")
        return first_valid_cell_reference, last_valid_cell_reference

    # Start checking from the row of cell a
    for row in range(row_number - 1, current_sheet.shape[0]):  # Adjust for 0-based indexing
        if row >= current_sheet.shape[0]:
            print(f"Warning: Row index {row} exceeds the DataFrame size {current_sheet.shape[0]}.")
            break
        
        if column_index >= current_sheet.shape[1]:
            print(f"Warning: Column index {column_index} exceeds the DataFrame width {current_sheet.shape[1]}.")
            break

        current_cell_value = current_sheet.iat[row, column_index]

        # Check for empty cell
        if pd.isna(current_cell_value):
            # Check the next cell
            next_cell_value = current_sheet.iat[row + 1, column_index] if row + 1 < current_sheet.shape[0] else None
            
            if next_cell_value == NextTableCellValue:
                # Assign d to the cell above the empty cell
                last_valid_cell_reference = f"{column_letter}{row}"  # Adjust for 1-indexing
                # last_valid_cell_reference = f"{column_letter}{row + 1}"  # Adjust for 1-indexing
                break
        
    return first_valid_cell_reference, last_valid_cell_reference

def get_column_values(CellNo, NextTableCellValue):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return []

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letter to index
    col_index = ord(start_col) - ord('A')
    
    values = []
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0] and col_index < current_sheet.shape[1]:
            cell_value = current_sheet.iloc[row, col_index]
            if not pd.isna(cell_value):  # Check if the cell is not empty
                values.append(cell_value)
        else:
            print(f"Warning: Cell at row {row+1}, column {start_col} is out of bounds.")
    
    return values

def get_two_column_values(CellNo, NextTableCellValue):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return [], []  # Return two empty lists for the two columns

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letters to indices
    col_index = ord(start_col) - ord('A')
    next_col_index = col_index + 1  # Index for the next column
    
    values_first_col = []
    values_second_col = []
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            # Get value from first column
            if col_index < current_sheet.shape[1]:
                cell_value = current_sheet.iloc[row, col_index]
                if not pd.isna(cell_value):  # Check if the cell is not empty
                    values_first_col.append(cell_value)
            else:
                print(f"Warning: Cell at row {row+1}, column {start_col} is out of bounds.")
            
            # Get value from second column
            if next_col_index < current_sheet.shape[1]:
                next_cell_value = current_sheet.iloc[row, next_col_index]
                if not pd.isna(next_cell_value):  # Check if the cell is not empty
                    values_second_col.append(next_cell_value)
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 1)} is out of bounds.")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
    
    return values_first_col, values_second_col

def get_three_column_values(CellNo, NextTableCellValue):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return [], [], []  # Return three empty lists for the three columns

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letters to indices
    col_index = ord(start_col) - ord('A')
    next_col_index = col_index + 1  # Index for the next column
    next_next_col_index = col_index + 2  # Index for the next next column
    
    values_first_col = []
    values_second_col = []
    values_third_col = []
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            # Get value from first column
            if col_index < current_sheet.shape[1]:
                cell_value = current_sheet.iloc[row, col_index]
                values_first_col.append(cell_value if not pd.isna(cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {start_col} is out of bounds.")
                values_first_col.append("")
            
            # Get value from second column
            if next_col_index < current_sheet.shape[1]:
                next_cell_value = current_sheet.iloc[row, next_col_index]
                values_second_col.append(next_cell_value if not pd.isna(next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 1)} is out of bounds.")
                values_second_col.append("")
            
            # Get value from third column
            if next_next_col_index < current_sheet.shape[1]:
                next_next_cell_value = current_sheet.iloc[row, next_next_col_index]
                values_third_col.append(next_next_cell_value if not pd.isna(next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 2)} is out of bounds.")
                values_third_col.append("")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
            values_first_col.append("")
            values_second_col.append("")
            values_third_col.append("")
    
    return values_first_col, values_second_col, values_third_col

def get_cell_reference(row_num, col_num):
    """
    Convert row and column numbers to Excel-style cell reference (e.g., 'C12').
    """
    column_letter = chr(65 + col_num)  
    return f"{column_letter}{row_num + 1}"  

def Get_table_started_cell_number():
    global global_table1_cell, global_table2_cell, global_table3_cell, global_table4_cell,table1_headers,table2_headers,table3_headers,table4_headers,table1_position,table2_position,table3_position,table4_position
    global_table1_cell = None
    global_table2_cell = None
    global_table3_cell = None
    global_table4_cell = None

    # HEADER ARRAY
    table1_headers = ["Sr. No.", "Software Component Name", "SWC Type", "Internal Behavior", "Runnable", "RTE Event", "Event Type"]
    table2_headers = ["Sr. No.", "Port Name", "Port Type", "Interface Name", "Interface Type", "DataElement", "Application Data Type", "Description"]
    table3_headers = ["Sr. No.", "Application Data Type", "Compu Method", "Compu Method Category", "Compu Scale", "Enum States", "Data Constraint", "Unit", "Mapped Implementation Data Type"]
    table4_headers = ["Sr. No.", "Application Data Types", "Data Constraint", "Data Constraint Type", "Minimum Value", "Maximum Value"]

    for sheet_name in xls.sheet_names[1:]:  # Skipping the first sheet
        current_sheet = pd.read_excel(Input_Excel_File, sheet_name=sheet_name, header=None)
        
        table1_position = None
        table2_position = None
        table3_position = None
        table4_position = None
        
        # Find the position of all tables
        for row_num, row in current_sheet.iterrows():
            # For Table 1:
            if all(header in row.values for header in table1_headers) and table1_position is None:
                table1_position = row_num  
            
            # For Table 2:
            if all(header in row.values for header in table2_headers) and table2_position is None:
                table2_position = row_num  
            
            # For Table 3:
            if all(header in row.values for header in table3_headers) and table3_position is None:
                table3_position = row_num  
            
            # For Table 4:
            if all(header in row.values for header in table4_headers) and table4_position is None:
                table4_position = row_num  
            
            # Break if all tables are found
            if table1_position is not None and table2_position is not None and table3_position is not None and table4_position is not None:
                break
        
        # Check Table 1
        if table1_position is not None:
            table1_start_col = current_sheet.iloc[table1_position].tolist().index(table1_headers[0])
            global_table1_cell = get_cell_reference(table1_position, table1_start_col) 
            # print(f"Table 1 found in sheet '{sheet_name}' at {global_table1_cell}")
        
        # Check Table 2
        if table2_position is not None:
            table2_start_col = current_sheet.iloc[table2_position].tolist().index(table2_headers[0])
            global_table2_cell = get_cell_reference(table2_position, table2_start_col)
            # print(f"Table 2 found in sheet '{sheet_name}' at {global_table2_cell}")
            
            # Find the value below table2_headers[4] (Interface Type)
            value_below_table2_header_4 = get_first_value_below_header(current_sheet, table2_position, table2_headers[4])
            # print(f"First value below '{table2_headers[4]}' found at: {value_below_table2_header_4}")
        
        # Check Table 3
        if table3_position is not None:
            table3_start_col = current_sheet.iloc[table3_position].tolist().index(table3_headers[0])
            global_table3_cell = get_cell_reference(table3_position, table3_start_col)  
            # print(f"Table 3 found in sheet '{sheet_name}' at {global_table3_cell}")
        
        # Check Table 4
        if table4_position is not None:
            table4_start_col = current_sheet.iloc[table4_position].tolist().index(table4_headers[0])
            global_table4_cell = get_cell_reference(table4_position, table4_start_col)  
            # print(f"Table 4 found in sheet '{sheet_name}' at {global_table4_cell}")
            
            # Find the first value below the header of Table 4
            # value_below_table4_header_4 = get_first_value_below_header(current_sheet, table4_position, table4_headers[4])
            # print(f"First value below '{table4_headers[4]}' found at: {value_below_table4_header_4}")

    return global_table1_cell, global_table2_cell, global_table3_cell, global_table4_cell

def get_first_value_below_header(sheet, header_row, header_name):
    """
    This function finds the first non-empty cell below the given header name.
    """
    header_row_values = sheet.iloc[header_row].tolist()
    
    # Find the column index of the given header name
    if header_name in header_row_values:
        header_col = header_row_values.index(header_name)
    else:
        return None  # Return None if header_name not found
    
    # Start looking right after the header row
    row_num = header_row + 1
    while pd.isna(sheet.iloc[row_num, header_col]):  # Loop until a non-empty cell is found
        row_num += 1
    
    first_value_cell = get_cell_reference(row_num, header_col)
    return first_value_cell

####################################----------*********** Project related definitions *************--------------######################################

def ProjectConfig():
    """
    #####################################
    Configuring project
    #####################################
    """
    # Global configuration options (shared with Utilities).
    global Options
    Options = Utilities.Options

    # Name of this project.
    Options.ProjectName = sd_project   # < %%%--- Change this to your project name.%%%

    # Set True to open an existing SystemDesk project (SDP). Otherwise, the SystemDesk project is created from scratch.
    Options.OpenExistingProject = False

    # Name of the AUTOSAR system.
    Options.SystemName = "System"

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
    templateFiles = [os.path.join(applRootDir, r"Templates\FolderStructure.arxml")]

    # Now import the files.
    Utilities.ImportAutosarFilesAtProject(templateFiles)

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
    if mySwc is not None:
        mySwc.Delete()
    myComposition = swComponentTypesPackage.ArPackages.Item("MyComposition")
    if myComposition is not None:
        myComposition.Delete()

####################################----------*********** SWC creation related definitions *************--------------######################################

def CreateSwcs():
    global rootPackage, value_d3
    rootPackage = SdApplication.ActiveProject.RootAutosar
    value_d3 = current_sheet.iloc[2, 3]  # D3 corresponds to row 2, column 3

    if value_d3 == 'ApplicationSwComponentType':
        ApplicationSwComponentType()
    elif value_d3 == 'ComplexDeviceDriverSwComponentType':
        ComplexDeviceDriverSwComponentType()
    elif value_d3 == 'EcuAbstractionSwComponentType':
        EcuAbstractionSwComponentType()
    elif value_d3 == 'NvBlockSwComponentType':
        NvBlockSwComponentType()
    elif value_d3 == 'ParameterSwComponentType':
        ParameterSwComponentType()
    elif value_d3 == 'SensorActuatorSwComponentType':
        SensorActuatorSwComponentType()
    elif value_d3 == 'ServiceProxySwComponentType':
        ServiceProxySwComponentType()
    elif value_d3 == 'ServiceSwComponentType':
        ServiceSwComponentType()
    else:
        print(f"In sheet '{sheet_name}', Please provide correct software component type")

def ApplicationSwComponentType():
    global CurrentswComponentTypesPackage, CurrentApplSWCPkg, CurrentSWC, CurrentInternalBehaviors, CurrentRunnable

    CurrentswComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")
    CurrentApplSWCPkg = CurrentswComponentTypesPackage.ArPackages.Item("ApplSWC")
    CurrentSWC = CurrentApplSWCPkg.Elements.AddNewApplicationSwComponentType(current_sheet.iloc[2, 2])
    CurrentInternalBehaviors = CurrentSWC.InternalBehaviors.AddNew(current_sheet.iloc[2, 4])

    first_runnable, last_runnable = GetColumnValidIndex('F3', 'Interface Type')
    # print(f"First runnable: {first_runnable}, Last runnable: {last_runnable}")

    if first_runnable and last_runnable:
        first_row_index = int(first_runnable[1:]) - 1
        last_row_index = int(last_runnable[1:]) - 1

        for row_index in range(first_row_index, last_row_index + 1):
            if row_index >= current_sheet.shape[0]:
                print(f"Warning: Row index {row_index} is out of bounds. Skipping.")
                continue

            runnable_name = current_sheet.iloc[row_index, column_index]
            if pd.isna(runnable_name):
                print(f"Warning: Empty runnable name at row {row_index + 1}. Skipping.")
                continue

            CurrentRunnable = CurrentInternalBehaviors.Runnables.AddNew(str(runnable_name))
            CurrentRunnable.MinimumStartInterval = 0.0
            CurrentRunnable.CanBeInvokedConcurrently = False
            CurrentRunnable.Symbol = CurrentRunnable.ShortName
            createrteevent(row_index, column_index)
    
    CreatePorts()
    createsharedinterfaces()

def ComplexDeviceDriverSwComponentType():
    global swComponentTypesPackage, CddSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    CddSWC= swComponentTypesPackage.ArPackages.Item("CddSWC")
   
    CurrentSWC = CddSWC.Elements.AddNewComplexDeviceDriverSwComponentType(current_sheet.iloc[2,2])

def EcuAbstractionSwComponentType():
    global swComponentTypesPackage, EcuAbSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    EcuAbSWC= swComponentTypesPackage.ArPackages.Item("EcuAbSWC")
   
    CurrentSWC = EcuAbSWC.Elements.AddNewEcuAbstractionSwComponentType(current_sheet.iloc[2,2])

def NvBlockSwComponentType():
    global swComponentTypesPackage, NvDataSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    NvDataSWC= swComponentTypesPackage.ArPackages.Item("NvDataSWC")
   
    CurrentSWC = NvDataSWC.Elements.AddNewNvBlockSwComponentType(current_sheet.iloc[2,2])

def ParameterSwComponentType():
    global swComponentTypesPackage, PrmSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    PrmSWC= swComponentTypesPackage.ArPackages.Item("PrmSWC")
   
    CurrentSWC = PrmSWC.Elements.AddNewParameterSwComponentType(current_sheet.iloc[2,2])

def SensorActuatorSwComponentType():
    global swComponentTypesPackage, SnsrActSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    SnsrActSWC= swComponentTypesPackage.ArPackages.Item("SnsrActSWC")
   
    CurrentSWC = SnsrActSWC.Elements.AddNewSensorActuatorSwComponentType(current_sheet.iloc[2,2])

def ServiceProxySwComponentType():
    global swComponentTypesPackage, SrvcPrxySWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    SrvcPrxySWC= swComponentTypesPackage.ArPackages.Item("SrvcPrxySWC")
   
    CurrentSWC = SrvcPrxySWC.Elements.AddNewServiceProxySwComponentType(current_sheet.iloc[2,2])

def ServiceSwComponentType():
    global swComponentTypesPackage, SrvcSWC, CurrentSWC

    swComponentTypesPackage = rootPackage.ArPackages.Item("SwComponentTypes")

    SrvcSWC= swComponentTypesPackage.ArPackages.Item("SrvcSWC")
   
    CurrentSWC = SrvcSWC.Elements.AddNewServiceSwComponentType(current_sheet.iloc[2,2])

####################################----------*********** RTE Event creation related definitions *************--------------######################################

def createrteevent(row_index, Actual_CellNo_Colomn):
    a = row_index
    b = Actual_CellNo_Colomn + 2
    c = Actual_CellNo_Colomn + 1

    if a < current_sheet.shape[0] and b < current_sheet.shape[1]:
        cell_value = current_sheet.iloc[a, b]

        if cell_value == 'AsynchronousServerCallReturnsEvent':
            AsynchronousServerCallReturnsEvent(a, c)
        elif cell_value == 'InitEvent':
            InitEvent(a, c)
        elif cell_value == 'TimingEvent':
            TimingEvent(a, c)
        else:
            print(f"In sheet '{sheet_name}', Unrecognized event type: {cell_value}")
    else:
        print(f"Warning: Indices ({a}, {b}) are out of bounds for the DataFrame.")

def InitEvent(CurrentRteEvent,currenteventcell):
    CurrentEvent = CurrentInternalBehaviors.Events.AddNewInitEvent(current_sheet.iloc[CurrentRteEvent,currenteventcell])
    # Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    CurrentEvent.StartOnEventRef = CurrentRunnable

def TimingEvent(CurrentRteEvent,currenteventcell):
    CurrentEvent = CurrentInternalBehaviors.Events.AddNewTimingEvent(current_sheet.iloc[CurrentRteEvent,currenteventcell])
    # Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    CurrentEvent.Period = 0.01
    CurrentEvent.StartOnEventRef = CurrentRunnable

def AsynchronousServerCallReturnsEvent(CurrentRteEvent,currenteventcell):
    CurrentEvent = CurrentInternalBehaviors.Events.AddNewInitEvent(current_sheet.iloc[CurrentRteEvent,currenteventcell])
    # Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    CurrentEvent.StartOnEventRef = CurrentRunnable

def BackgroundEvent(CurrentRteEvent,currenteventcell):
    CurrentEvent = CurrentInternalBehaviors.Events.AddNewInitEvent(current_sheet.iloc[CurrentRteEvent,currenteventcell])
    # Utilities.SetDescription(tssEvent, "TimingEvent for TssPreprocessing Runnable [10 ms period].")
    CurrentEvent.StartOnEventRef = CurrentRunnable

####################################----------*********** Ports creation related definitions *************--------------######################################

def CreatePorts():
    # Get the values from column I3 until the next table cell value "Interface Type"
    # value_below_table2_header_2=None 
    value_below_table2_header_2 = get_first_value_below_header(current_sheet, table2_position, table2_headers[1])
    # print(f"First value bcghbelow '{table2_headers[1]}' found at: {value_below_table2_header_2}")

    

    
    # a=get_table_and_e_cell('table2', 'Port Name')

    port_name_col, port_type_col = get_two_column_values(value_below_table2_header_2, 'Application Data Type')
    
    # Iterate through both columns simultaneously using zip
    for port_name, port_type in zip(port_name_col, port_type_col):
        # Check if it's a receiver port
        if port_type == 'dataReceiverPort':
            CurrentRport = CurrentSWC.Ports.AddNewRPortPrototype(port_name)
            # print(f"Created R-Port: {port_name}")
            
        # Check if it's a sender port
        elif port_type == 'dataSenderPort':
            CurrentPport = CurrentSWC.Ports.AddNewPPortPrototype(port_name)
            # print(f"Created P-Port: {port_name}")
        
        else:
            print(f"Unknown port type: {port_type} for port {port_name}")

####################################----------*********** Interface creation related definitions *************--------------######################################

def createsharedinterfaces():
    # Get the first value below the header
    value_below_table2_header_4 = get_first_value_below_header(current_sheet, table2_position, table2_headers[3])

    # Extract the interface name, type, and data elements
    IF_name_col, IF_type_col, DE_col = get_three_column_values(value_below_table2_header_4, 'Compu Method Category')

    current_IF_name = None
    current_IF_type = None
    data_elements = []

    for IF_name, IF_type, DE in zip(IF_name_col, IF_type_col, DE_col):
        
        # If a new interface is found (non-empty name)
        if IF_name and IF_type in ['SenderReceiverInterface', 'NvDataInterface', 'ParameterInterface']:
            # If there's a previous interface collected, process it
            if current_IF_name and data_elements:
                if current_IF_type == 'SenderReceiverInterface':
                    SenderReceiverInterface(current_IF_name, data_elements)
                elif current_IF_type == 'NvDataInterface':
                    NvDataInterface(current_IF_name, data_elements)
                elif current_IF_type == 'ParameterInterface':
                    ParameterInterface(current_IF_name, data_elements)
            
            # Reset for the new interface
            current_IF_name = IF_name
            current_IF_type = IF_type
            data_elements = [DE]  # Start with the first data element
        
        # If the interface name is empty but we're continuing the same interface type
        elif IF_name == '' and current_IF_type in ['SenderReceiverInterface', 'NvDataInterface', 'ParameterInterface']:
            # Append additional data elements
            data_elements.append(DE)

        elif IF_type in ['ModeSwitchInterface', 'ClientServerInterface', 'TriggerInterface']:
            # Handle other interface types accordingly
            handle_other_interfaces(IF_name, IF_type, DE)
        
        else:
            print(f"Unknown or unhandled interface type: {IF_type} for interface {IF_name}")

    # Process the last interface after the loop
    if current_IF_name and data_elements:
        if current_IF_type == 'SenderReceiverInterface':
            SenderReceiverInterface(current_IF_name, data_elements)
        elif current_IF_type == 'NvDataInterface':
            NvDataInterface(current_IF_name, data_elements)
        elif current_IF_type == 'ParameterInterface':
            ParameterInterface(current_IF_name, data_elements)

# Function to handle other interfaces (extend this if needed)
def handle_other_interfaces(IF_name, IF_type, DE):
    if IF_type == 'ModeSwitchInterface':
        ModeSwitchInterface(IF_name, DE)
    elif IF_type == 'ClientServerInterface':
        ClientServerInterface(IF_name, DE)
    elif IF_type == 'TriggerInterface':
        TriggerInterface(IF_name, DE)
    else:
        print(f"Unknown interface type: {IF_type} for interface {IF_name}")

# Function to create SenderReceiverInterface
def SenderReceiverInterface(currentIF_name, DataElements):

    
    SharedIFpkg = Utilities.GetElementByPath("/SharedElements/PortInterfaces/SenderReceiver")
    currentSRIF = SharedIFpkg.Elements.AddNewSenderReceiverInterface(currentIF_name)
    
    # Set the interface as non-service
    currentSRIF.SetNewIsService().SetValue(False)
    
    # Add each data element to this interface
    for itsDE in DataElements:
        currentSRIFDE = currentSRIF.DataElements.AddNew(itsDE)
        Utilities.SetDescription(currentSRIFDE, "Turn switch sensor position [left, off, right]")
        Utilities.SetInvalidationPolicy(currentSRIF, currentSRIFDE, SystemDeskEnums.HandleInvalidEnum.DontInvalidate)

def NvDataInterface(currentIF_name, NvDatas):
    SharedIFpkg = Utilities.GetElementByPath("/SharedElements/PortInterfaces/NvData")
    currentNVIF = SharedIFpkg.Elements.AddNewNvDataInterface(currentIF_name)
    # Utilities.SetDescription(currentNVIF, "TurnSwitchSensor signals")
    currentNVIF.SetNewIsService().SetValue(False)
    for itsDE in NvDatas:
        currentNVIFDE = currentNVIF.NvDatas.AddNew(itsDE)
        Utilities.SetDescription(currentNVIFDE, "Turn switch sensor position [left, off, right]")
        
def ParameterInterface(currentIF_name, Parameters):
    SharedIFpkg = Utilities.GetElementByPath("/SharedElements/PortInterfaces/Parameter")
    currentPRMIF = SharedIFpkg.Elements.AddNewParameterInterface(currentIF_name)
    # Utilities.SetDescription(currentPRMIF, "TurnSwitchSensor signals")
    currentPRMIF.SetNewIsService().SetValue(False)
    for itsDE in Parameters:
        currentPRMIFDE = currentPRMIF.Parameters.AddNew(itsDE)
        Utilities.SetDescription(currentPRMIFDE, "Turn switch sensor position [left, off, right]")
       
def ModeSwitchInterface(currentIF_name, itsDE):
    SharedIFpkg = Utilities.GetElementByPath("/SharedElements/PortInterfaces/ModeSwitch")
    
def ClientServerInterface(currentIF_name, itsDE):
    SharedIFpkg = Utilities.GetElementByPath("/SharedElements/PortInterfaces/ClientServer")
    
def TriggerInterface(currentIF_name, itsDE):
    SharedIFpkg = Utilities.GetElementByPath("/SharedElements/PortInterfaces/Trigger")
    
#########################----------*********** Application data type creation related definitions *************--------------###########################

def createADTs():
    # Create ADTs
    value_below_table2_header_4 = get_first_value_below_header(current_sheet, table2_position, table2_headers[3])
    
    IF_name_col, IF_type_col = get_three_column_values(value_below_table2_header_4, 'Compu Method Category')

    SharedIFpkg = Utilities.GetElementByPath("/SharedElements/ApplicationDataTypes/Primitive")







####################################----------***********+++++++===== Main Function ++++++++=====*************--------------######################################

def Main():
    ReadUserDefinedExcel()
    Get_table_started_cell_number()
    ProjectConfig()
    CreateProjectAndPackages()
    CleanupProjectAndPackages()
    CreateSwcs()

if __name__ == "__main__":
    Main()
    print("Ready")