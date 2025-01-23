# import openpyxl

# def find_valid_cells(CellNo, NextTableCellValue, workbook_path):
#     # Load the workbook and the active sheet
#     wb = openpyxl.load_workbook(workbook_path)
#     sheet = wb.active

#     # Extract column and row from the cell reference
#     column_letter = ''.join(filter(str.isalpha, CellNo))
#     row_number = int(''.join(filter(str.isdigit, CellNo)))

#     column_index = ord(column_letter) - ord('A')

#     print(column_index)

#     # Initialize c and d
#     first_valid_cell_reference = CellNo  # c is the current cell
#     last_valid_cell_reference = None  # d will be determined later

#     # Start checking from the row of cell a
#     for row in range(row_number + 1, sheet.max_row + 1):
#         current_cell_value = sheet[f"{column_letter}{row}"].value

#         # Check for empty cell
#         if current_cell_value is None:
#             # Check the next cell
#             next_cell_value = sheet[f"{column_letter}{row + 1}"].value if row + 1 <= sheet.max_row else None
            
#             if next_cell_value == NextTableCellValue:
#                 # Assign d to the cell above the empty cell
#                 last_valid_cell_reference = f"{column_letter}{row - 1}"
#                 break

#     return first_valid_cell_reference, last_valid_cell_reference

# # Example usage
# # Assuming you have an Excel file 'example.xlsx' and you want to find valid cells for 'G9' and 'SomeText'
# first_valid_cell_reference, last_valid_cell_reference = find_valid_cells('E8', 'Compu Method Category', 'thirty_Oct.xlsx')
# print(f"First valid cell: {first_valid_cell_reference}, Last valid cell: {last_valid_cell_reference}")



# def find_valid_cells(a, b):
#     # Extract column and row from the cell reference
#     column_letter = ''.join(filter(str.isalpha, a))
#     row_number = int(''.join(filter(str.isdigit, a)))

#     # Convert column letter to a zero-based index
#     column_index = ord(column_letter) - ord('A')

#     # Initialize c and d
#     c = a  # c is the current cell
#     d = None  # d will be determined later

#     # Start checking from the row of cell a
#     for row in range(row_number, first_sheet.shape[0]):  # Adjust for zero-indexing
#         current_cell_value = first_sheet.iat[row, column_index]

#         # Check for empty cell
#         if pd.isna(current_cell_value):
#             # Check the next cell
#             next_cell_value = first_sheet.iat[row + 1, column_index] if row + 1 < first_sheet.shape[0] else None
            
#             if next_cell_value == b:
#                 # Assign d to the cell above the empty cell
#                 d = f"{column_letter}{row}"  # Adjust for 1-indexing
#                 break

#     return c, d




import pandas as pd

# def read_excel_and_get_project_name(file_path):
#     # Load the Excel file
#     xls = pd.ExcelFile(file_path)

#     # Read the first sheet to get the project name from cell D5
#     first_sheet = pd.read_excel(xls, sheet_name=0, header=None)
#     sd_project = first_sheet.iloc[4, 3]  # Cell D5 corresponds to row index 4, column index 3

#     print(f"Project Name: {sd_project}")

#     # Read subsequent sheets from the 2nd to the last
#     sheets_data = {}
#     for sheet_name in xls.sheet_names[1:]:  # Skip the first sheet
#         current_sheet = pd.read_excel(xls, sheet_name=sheet_name, header=None)
#         sheets_data[sheet_name] = current_sheet

#     return sd_project, sheets_data

# # Example usage
# file_path = input("Please provide the path of the input Excel file: ")
# project_name, sheets = read_excel_and_get_project_name(file_path)

# # You can now use the project_name and sheets as needed



def ReadUserDefinedExcel():
        # Load the user defined Excel file
    global Input_Excel_File,current_sheet,sheet_name
    Input_Excel_File = input("Please provide the path of input Excel file (e.g., E:\\sysdesk\\automation): ")

    # Referring xls variable as entire excel
    global xls
    xls = pd.ExcelFile(Input_Excel_File)

    for sheet_name in xls.sheet_names[1:]:  # This will skip the first sheet #move this excel part to perticular section of this code
        current_sheet = pd.read_excel(Input_Excel_File, sheet_name=sheet_name,header=None)

    # Read the first sheet
    # global first_sheet
    # first_sheet = pd.read_excel(Input_Excel_File, sheet_name=0, header=None)

    # Get the project name from cell D5
    # global sd_project
    # sd_project = first_sheet.iloc[4, 3]  # Cell D5


    

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

    # Start checking from the row of cell a
    
    for row in range(row_number, current_sheet.shape[0]):  # Adjust for zero-indexing
        current_cell_value = current_sheet.iat[row, column_index]

        # Check for empty cell
        if pd.isna(current_cell_value):
            # Check the next cell
            next_cell_value = current_sheet.iat[row + 1, column_index] if row + 1 < current_sheet.shape[0] else None
            
            if next_cell_value == NextTableCellValue:
                # Assign d to the cell above the empty cell
                last_valid_cell_reference = f"{column_letter}{row}"  # Adjust for 1-indexing
                break

    return first_valid_cell_reference, last_valid_cell_reference

ReadUserDefinedExcel()
a,b=GetColumnValidIndex('E8', 'Compu Method Category')

print(f"First valid cell: {a}, Last valid cell: {b}")
