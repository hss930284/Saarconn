import pandas as pd

def Function_to_Extract_Value_from_Excel(file_path, sheet_index, header_row, header_col, stop_condition_value, value_col):
    """
    Extract values from the specified Excel sheet, starting after a header value,
    and stopping when a specified condition is met.

    Parameters:
        file_path (str): The path to the Excel file.
        sheet_index (int): The index of the sheet to read from.
        header_row (int): The row index (0-based) to get the header value from.
        header_col (int): The column index (0-based) to get the header value from.
        stop_condition_value (str): The value at which to stop extraction.
        value_col (int): The column index (0-based) from which to extract values.

    Returns:
        tuple: A list of extracted values, the cell range, the first cell, and the last cell.
    """

    # Read the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_index, header=None)

    # Get the value from the specified header cell to use as the header
    header_value = df.iloc[header_row, header_col]

    # Variables to store the values and cell range
    extracted_values = []
    start_collecting = False
    first_cell = None
    last_cell = None

    # Iteration through the DataFrame
    for index, row in df.iterrows():
        # Check for header value in the specified column
        if row.iloc[header_col] == header_value:
            start_collecting = True
            continue  # Continue to the next row

        # If we are collecting values
        if start_collecting:
            current_value = row.iloc[value_col]  # Get the current value from the specified column
            
            # Combined condition: Check if current value is blank 
            # and the next value matches the stop condition
            if pd.isnull(current_value) and index + 1 < len(df):
                next_value = df.iloc[index + 1, value_col]
                if next_value == stop_condition_value:
                    break  # Stop collecting if the condition is met

            # If the current value is not blank, add the value to the extracted list
            if not pd.isnull(current_value):
                if first_cell is None:
                    first_cell = f'{chr(65 + value_col)}{index + 2}'  # Convert column index to letter
                last_cell = f'{chr(65 + value_col)}{index + 2}'  # Convert column index to letter
                extracted_values.append(current_value)  # Add the value to the list

    # Construct the cell range string
    cell_range = f'{first_cell}:{last_cell}' if first_cell and last_cell else None

    # Return the extracted values list, cell range, first cell, and last cell
    return extracted_values, cell_range, first_cell, last_cell

# Excel file name
file_path = 'demoarch.xlsx'
sheet_index = 1  # Index for the second sheet

# Specify the parameters for the first extraction
header_row = 1  # Row index for the header value (0-based)
header_col = 5  # Column index for the header value (0-based, F is 5)
stop_condition_value = "Interface Type"  # You can change this as needed
value_col = 5  # Column index from which to extract values (0-based, F is 5)

# Extracted value list and cell range for the first extraction
extracted_values, cell_range, first_cell, last_cell = Function_to_Extract_Value_from_Excel(file_path, sheet_index, header_row, header_col, stop_condition_value, value_col)

# Print the extracted values list
print("Extracted Values:", extracted_values)

# Print the first and last cell references
print("First Cell:", first_cell)
print("Last Cell:", last_cell)

# Create output sentences for the first extraction
output_sentences = [f"my name is {value}" for value in extracted_values]

# Print each output sentence on a new line
print("Formatted Output:")
for sentence in output_sentences:
    print(sentence)
