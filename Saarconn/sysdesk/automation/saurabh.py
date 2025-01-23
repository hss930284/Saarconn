import pandas as pd

def Function_to_Extract_Value_from_Excel(file_path, sheet_index, header_cell, stop_condition_value):
    """
    Extract values from the specified Excel sheet, starting after a header value,
    and stopping when a specified condition is met.

    Parameters:
        file_path (str): The path to the Excel file.
        sheet_index (int): The index of the sheet to read from.
        header_cell (str): The cell reference (e.g., 'G2') for the header value.
        stop_condition_value (str): The value at which to stop extraction.

    Returns:
        tuple: A list of extracted values and the cell range.
    """

    # Read the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_index, header=None)

    # Convert header_cell (e.g., 'G2') to row and column indices
    header_col = ord(header_cell[0].upper()) - 65  # Convert column letter to index (A=0, B=1, ...)
    header_row = int(header_cell[1:]) - 1  # Convert row to 0-based index

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
            current_value = row.iloc[header_col]  # Use the same column for extraction
            
            # Combined condition: Check if current value is blank 
            # and the next value matches the stop condition
            if pd.isnull(current_value) and index + 1 < len(df):
                next_value = df.iloc[index + 1, header_col]
                if next_value == stop_condition_value:
                    break  # Stop collecting if the condition is met

            # If the current value is not blank, add the value to the extracted list
            if not pd.isnull(current_value):
                if first_cell is None:
                    first_cell = f'{chr(65 + header_col)}{index + 2}'  # Convert column index to letter
                last_cell = f'{chr(65 + header_col)}{index + 2}'  # Convert column index to letter
                extracted_values.append(current_value)  # Add the value to the list

    # Construct the cell range string
    cell_range = f'{first_cell}:{last_cell}' if first_cell and last_cell else None

    # Return the extracted values list and cell range
    return extracted_values, cell_range

# Excel file name
file_path = 'demoarch.xlsx'
sheet_index = 1  # Index for the second sheet

# Specify the parameters for the first extraction
header_cell = 'F2'  # The header cell reference
stop_condition_value = "Interface Type"  # You can change this as needed

# Extracted value list and cell range for the first extraction
extracted_values, cell_range = Function_to_Extract_Value_from_Excel(file_path, sheet_index, header_cell, stop_condition_value)

# Print the extracted values list
# print("Extracted Values:", extracted_values)

# Create output sentences for the first extraction
output_sentences = [f"{value}" for value in extracted_values]
print(output_sentences)

# # Print each output sentence on a new line
# print("Formatted Output:")
# for sentence in output_sentences:
#     print(sentence)

# # 2nd extraction example
# header_cell = 'G2'  # The header cell reference for the second extraction
# stop_condition_value = "DataElement"  # Change this as needed

# # Extracted value list and cell range for the second extraction
# extracted_values, cell_range = Function_to_Extract_Value_from_Excel(file_path, sheet_index, header_cell, stop_condition_value)

# # Print the extracted values list for the second extraction
# print("2nd Extracted Values:", extracted_values)

# # Create output sentences for the second extraction
# output_sentences = [f"{value}" for value in extracted_values]

# # Print each output sentence on a new line for the second extraction
# print("2nd Formatted Output:")
# for sentence in output_sentences:
#     print(sentence)


# Extracted value list and cell range for the second extraction
# extracted_values, cell_range = Function_to_Extract_Value_from_Excel(file_path, sheet_index, header_cell="G2", stop_condition_value= "DataElement")
# output_sentences = [f"{value}" for value in extracted_values]
# print(output_sentences)
