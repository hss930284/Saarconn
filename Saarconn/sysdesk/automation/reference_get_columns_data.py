# --------------------------- --------function to get 1columns ends------------------------------------------------
def get_one_column_value(CellNo, NextTableCellValue):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return []  # Return an empty list for the column

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letters to index
    col_index = ord(start_col) - ord('A')
    
    # Initialize list to store values
    values_first_col = []
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            # Get value from the first column
            if col_index < current_sheet.shape[1]:
                cell_value = current_sheet.iloc[row, col_index]
                values_first_col.append(cell_value if not pd.isna(cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {start_col} is out of bounds.")
                values_first_col.append("")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
            values_first_col.append("")
    
    return values_first_col
# --------------------------- --------function to get 1columns ends------------------------------------------------



# --------------------------- --------function to get 2columns------------------------------------------------
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
    next_col_index = col_index + 1  # Index for the second column
    
    # Initialize lists to store values
    values_first_col = []
    values_second_col = []
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            # Get value from the first column
            if col_index < current_sheet.shape[1]:
                cell_value = current_sheet.iloc[row, col_index]
                values_first_col.append(cell_value if not pd.isna(cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {start_col} is out of bounds.")
                values_first_col.append("")
            
            # Get value from the second column
            if next_col_index < current_sheet.shape[1]:
                next_cell_value = current_sheet.iloc[row, next_col_index]
                values_second_col.append(next_cell_value if not pd.isna(next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 1)} is out of bounds.")
                values_second_col.append("")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
            values_first_col.append("")
            values_second_col.append("")
    
    return values_first_col, values_second_col
# --------------------------- --------function to get 2columns ends------------------------------------------------


# --------------------------- --------function to get 3columns ends------------------------------------------------

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
# --------------------------- --------function to get 3columns ends------------------------------------------------




# --------------------------- --------function to get 4columns------------------------------------------------
def get_four_column_values(CellNo, NextTableCellValue):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return [], [], [], []  # Return four empty lists for the four columns

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letters to indices
    col_index = ord(start_col) - ord('A')
    next_col_index = col_index + 1  # Index for the second column
    next_next_col_index = col_index + 2  # Index for the third column
    next_next_next_col_index = col_index + 3  # Index for the fourth column
    
    values_first_col = []
    values_second_col = []
    values_third_col = []
    values_fourth_col = []
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            # Get value from the first column
            if col_index < current_sheet.shape[1]:
                cell_value = current_sheet.iloc[row, col_index]
                values_first_col.append(cell_value if not pd.isna(cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {start_col} is out of bounds.")
                values_first_col.append("")
            
            # Get value from the second column
            if next_col_index < current_sheet.shape[1]:
                next_cell_value = current_sheet.iloc[row, next_col_index]
                values_second_col.append(next_cell_value if not pd.isna(next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 1)} is out of bounds.")
                values_second_col.append("")
            
            # Get value from the third column
            if next_next_col_index < current_sheet.shape[1]:
                next_next_cell_value = current_sheet.iloc[row, next_next_col_index]
                values_third_col.append(next_next_cell_value if not pd.isna(next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 2)} is out of bounds.")
                values_third_col.append("")
            
            # Get value from the fourth column
            if next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_cell_value = current_sheet.iloc[row, next_next_next_col_index]
                values_fourth_col.append(next_next_next_cell_value if not pd.isna(next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 3)} is out of bounds.")
                values_fourth_col.append("")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
            values_first_col.append("")
            values_second_col.append("")
            values_third_col.append("")
            values_fourth_col.append("")
    
    return values_first_col, values_second_col, values_third_col, values_fourth_col
# --------------------------- --------function to get 4columns ends------------------------------------------------




# --------------------------- --------function to get 5columns------------------------------------------------
def get_five_column_values(CellNo, NextTableCellValue):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return [], [], [], [], []  # Return five empty lists for the five columns

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letters to indices
    col_index = ord(start_col) - ord('A')
    next_col_index = col_index + 1      # Index for the second column
    next_next_col_index = col_index + 2  # Index for the third column
    next_next_next_col_index = col_index + 3  # Index for the fourth column
    next_next_next_next_col_index = col_index + 4  # Index for the fifth column
    
    # Initialize lists to store values
    values_first_col = []
    values_second_col = []
    values_third_col = []
    values_fourth_col = []
    values_fifth_col = []
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            # Get value from the first column
            if col_index < current_sheet.shape[1]:
                cell_value = current_sheet.iloc[row, col_index]
                values_first_col.append(cell_value if not pd.isna(cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {start_col} is out of bounds.")
                values_first_col.append("")
            
            # Get value from the second column
            if next_col_index < current_sheet.shape[1]:
                next_cell_value = current_sheet.iloc[row, next_col_index]
                values_second_col.append(next_cell_value if not pd.isna(next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 1)} is out of bounds.")
                values_second_col.append("")
            
            # Get value from the third column
            if next_next_col_index < current_sheet.shape[1]:
                next_next_cell_value = current_sheet.iloc[row, next_next_col_index]
                values_third_col.append(next_next_cell_value if not pd.isna(next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 2)} is out of bounds.")
                values_third_col.append("")
            
            # Get value from the fourth column
            if next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_cell_value = current_sheet.iloc[row, next_next_next_col_index]
                values_fourth_col.append(next_next_next_cell_value if not pd.isna(next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 3)} is out of bounds.")
                values_fourth_col.append("")
            
            # Get value from the fifth column
            if next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_col_index]
                values_fifth_col.append(next_next_next_next_cell_value if not pd.isna(next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 4)} is out of bounds.")
                values_fifth_col.append("")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
            values_first_col.append("")
            values_second_col.append("")
            values_third_col.append("")
            values_fourth_col.append("")
            values_fifth_col.append("")
    
    return values_first_col, values_second_col, values_third_col, values_fourth_col, values_fifth_col
# --------------------------- --------function to get 5columns ends------------------------------------------------




# --------------------------- --------function to get 6columns------------------------------------------------
def get_six_column_values(CellNo, NextTableCellValue):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return [], [], [], [], [], []  # Return six empty lists for the six columns

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letters to indices
    col_index = ord(start_col) - ord('A')
    next_col_index = col_index + 1      # Index for the second column
    next_next_col_index = col_index + 2  # Index for the third column
    next_next_next_col_index = col_index + 3  # Index for the fourth column
    next_next_next_next_col_index = col_index + 4  # Index for the fifth column
    next_next_next_next_next_col_index = col_index + 5  # Index for the sixth column
    
    # Initialize lists to store values
    values_first_col = []
    values_second_col = []
    values_third_col = []
    values_fourth_col = []
    values_fifth_col = []
    values_sixth_col = []
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            # Get value from the first column
            if col_index < current_sheet.shape[1]:
                cell_value = current_sheet.iloc[row, col_index]
                values_first_col.append(cell_value if not pd.isna(cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {start_col} is out of bounds.")
                values_first_col.append("")
            
            # Get value from the second column
            if next_col_index < current_sheet.shape[1]:
                next_cell_value = current_sheet.iloc[row, next_col_index]
                values_second_col.append(next_cell_value if not pd.isna(next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 1)} is out of bounds.")
                values_second_col.append("")
            
            # Get value from the third column
            if next_next_col_index < current_sheet.shape[1]:
                next_next_cell_value = current_sheet.iloc[row, next_next_col_index]
                values_third_col.append(next_next_cell_value if not pd.isna(next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 2)} is out of bounds.")
                values_third_col.append("")
            
            # Get value from the fourth column
            if next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_cell_value = current_sheet.iloc[row, next_next_next_col_index]
                values_fourth_col.append(next_next_next_cell_value if not pd.isna(next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 3)} is out of bounds.")
                values_fourth_col.append("")
            
            # Get value from the fifth column
            if next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_col_index]
                values_fifth_col.append(next_next_next_next_cell_value if not pd.isna(next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 4)} is out of bounds.")
                values_fifth_col.append("")
            
            # Get value from the sixth column
            if next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_col_index]
                values_sixth_col.append(next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 5)} is out of bounds.")
                values_sixth_col.append("")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
            values_first_col.append("")
            values_second_col.append("")
            values_third_col.append("")
            values_fourth_col.append("")
            values_fifth_col.append("")
            values_sixth_col.append("")
    
    return values_first_col, values_second_col, values_third_col, values_fourth_col, values_fifth_col, values_sixth_col
# --------------------------- --------function to get 6columns ends------------------------------------------------




# --------------------------- --------function to get 7columns------------------------------------------------
def get_seven_column_values(CellNo, NextTableCellValue):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return [], [], [], [], [], [], []  # Return seven empty lists for the seven columns

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letters to indices
    col_index = ord(start_col) - ord('A')
    next_col_index = col_index + 1      # Index for the second column
    next_next_col_index = col_index + 2  # Index for the third column
    next_next_next_col_index = col_index + 3  # Index for the fourth column
    next_next_next_next_col_index = col_index + 4  # Index for the fifth column
    next_next_next_next_next_col_index = col_index + 5  # Index for the sixth column
    next_next_next_next_next_next_col_index = col_index + 6  # Index for the seventh column
    
    # Initialize lists to store values
    values_first_col = []
    values_second_col = []
    values_third_col = []
    values_fourth_col = []
    values_fifth_col = []
    values_sixth_col = []
    values_seventh_col = []
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            # Get value from the first column
            if col_index < current_sheet.shape[1]:
                cell_value = current_sheet.iloc[row, col_index]
                values_first_col.append(cell_value if not pd.isna(cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {start_col} is out of bounds.")
                values_first_col.append("")
            
            # Get value from the second column
            if next_col_index < current_sheet.shape[1]:
                next_cell_value = current_sheet.iloc[row, next_col_index]
                values_second_col.append(next_cell_value if not pd.isna(next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 1)} is out of bounds.")
                values_second_col.append("")
            
            # Get value from the third column
            if next_next_col_index < current_sheet.shape[1]:
                next_next_cell_value = current_sheet.iloc[row, next_next_col_index]
                values_third_col.append(next_next_cell_value if not pd.isna(next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 2)} is out of bounds.")
                values_third_col.append("")
            
            # Get value from the fourth column
            if next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_cell_value = current_sheet.iloc[row, next_next_next_col_index]
                values_fourth_col.append(next_next_next_cell_value if not pd.isna(next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 3)} is out of bounds.")
                values_fourth_col.append("")
            
            # Get value from the fifth column
            if next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_col_index]
                values_fifth_col.append(next_next_next_next_cell_value if not pd.isna(next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 4)} is out of bounds.")
                values_fifth_col.append("")
            
            # Get value from the sixth column
            if next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_col_index]
                values_sixth_col.append(next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 5)} is out of bounds.")
                values_sixth_col.append("")
            
            # Get value from the seventh column
            if next_next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_next_col_index]
                values_seventh_col.append(next_next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 6)} is out of bounds.")
                values_seventh_col.append("")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
            values_first_col.append("")
            values_second_col.append("")
            values_third_col.append("")
            values_fourth_col.append("")
            values_fifth_col.append("")
            values_sixth_col.append("")
            values_seventh_col.append("")
    
    return values_first_col, values_second_col, values_third_col, values_fourth_col, values_fifth_col, values_sixth_col, values_seventh_col
# --------------------------- --------function to get 7columns ends------------------------------------------------



# --------------------------- --------function to get 8columns------------------------------------------------
def get_eight_column_values(CellNo, NextTableCellValue):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return [], [], [], [], [], [], [], []  # Return eight empty lists for the eight columns

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letters to indices
    col_index = ord(start_col) - ord('A')
    next_col_index = col_index + 1      # Index for the second column
    next_next_col_index = col_index + 2  # Index for the third column
    next_next_next_col_index = col_index + 3  # Index for the fourth column
    next_next_next_next_col_index = col_index + 4  # Index for the fifth column
    next_next_next_next_next_col_index = col_index + 5  # Index for the sixth column
    next_next_next_next_next_next_col_index = col_index + 6  # Index for the seventh column
    next_next_next_next_next_next_next_col_index = col_index + 7  # Index for the eighth column
    
    # Initialize lists to store values
    values_first_col = []
    values_second_col = []
    values_third_col = []
    values_fourth_col = []
    values_fifth_col = []
    values_sixth_col = []
    values_seventh_col = []
    values_eighth_col = []
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            # Get value from the first column
            if col_index < current_sheet.shape[1]:
                cell_value = current_sheet.iloc[row, col_index]
                values_first_col.append(cell_value if not pd.isna(cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {start_col} is out of bounds.")
                values_first_col.append("")
            
            # Get value from the second column
            if next_col_index < current_sheet.shape[1]:
                next_cell_value = current_sheet.iloc[row, next_col_index]
                values_second_col.append(next_cell_value if not pd.isna(next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 1)} is out of bounds.")
                values_second_col.append("")
            
            # Get value from the third column
            if next_next_col_index < current_sheet.shape[1]:
                next_next_cell_value = current_sheet.iloc[row, next_next_col_index]
                values_third_col.append(next_next_cell_value if not pd.isna(next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 2)} is out of bounds.")
                values_third_col.append("")
            
            # Get value from the fourth column
            if next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_cell_value = current_sheet.iloc[row, next_next_next_col_index]
                values_fourth_col.append(next_next_next_cell_value if not pd.isna(next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 3)} is out of bounds.")
                values_fourth_col.append("")
            
            # Get value from the fifth column
            if next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_col_index]
                values_fifth_col.append(next_next_next_next_cell_value if not pd.isna(next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 4)} is out of bounds.")
                values_fifth_col.append("")
            
            # Get value from the sixth column
            if next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_col_index]
                values_sixth_col.append(next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 5)} is out of bounds.")
                values_sixth_col.append("")
            
            # Get value from the seventh column
            if next_next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_next_col_index]
                values_seventh_col.append(next_next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 6)} is out of bounds.")
                values_seventh_col.append("")
            
            # Get value from the eighth column
            if next_next_next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_next_next_col_index]
                values_eighth_col.append(next_next_next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 7)} is out of bounds.")
                values_eighth_col.append("")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
            values_first_col.append("")
            values_second_col.append("")
            values_third_col.append("")
            values_fourth_col.append("")
            values_fifth_col.append("")
            values_sixth_col.append("")
            values_seventh_col.append("")
            values_eighth_col.append("")
    
    return (values_first_col, values_second_col, values_third_col, 
            values_fourth_col, values_fifth_col, values_sixth_col, 
            values_seventh_col, values_eighth_col)

# --------------------------- --------function to get 8columns ends------------------------------------------------




# --------------------------- --------function to get 9columns------------------------------------------------
def get_nine_column_values(CellNo, NextTableCellValue):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return [], [], [], [], [], [], [], [], []  # Return nine empty lists for the nine columns

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letters to indices
    col_index = ord(start_col) - ord('A')
    next_col_index = col_index + 1      # Index for the second column
    next_next_col_index = col_index + 2  # Index for the third column
    next_next_next_col_index = col_index + 3  # Index for the fourth column
    next_next_next_next_col_index = col_index + 4  # Index for the fifth column
    next_next_next_next_next_col_index = col_index + 5  # Index for the sixth column
    next_next_next_next_next_next_col_index = col_index + 6  # Index for the seventh column
    next_next_next_next_next_next_next_col_index = col_index + 7  # Index for the eighth column
    next_next_next_next_next_next_next_next_col_index = col_index + 8  # Index for the ninth column
    
    # Initialize lists to store values
    values_first_col = []
    values_second_col = []
    values_third_col = []
    values_fourth_col = []
    values_fifth_col = []
    values_sixth_col = []
    values_seventh_col = []
    values_eighth_col = []
    values_ninth_col = []
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            # Get value from the first column
            if col_index < current_sheet.shape[1]:
                cell_value = current_sheet.iloc[row, col_index]
                values_first_col.append(cell_value if not pd.isna(cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {start_col} is out of bounds.")
                values_first_col.append("")
            
            # Get value from the second column
            if next_col_index < current_sheet.shape[1]:
                next_cell_value = current_sheet.iloc[row, next_col_index]
                values_second_col.append(next_cell_value if not pd.isna(next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 1)} is out of bounds.")
                values_second_col.append("")
            
            # Get value from the third column
            if next_next_col_index < current_sheet.shape[1]:
                next_next_cell_value = current_sheet.iloc[row, next_next_col_index]
                values_third_col.append(next_next_cell_value if not pd.isna(next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 2)} is out of bounds.")
                values_third_col.append("")
            
            # Get value from the fourth column
            if next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_cell_value = current_sheet.iloc[row, next_next_next_col_index]
                values_fourth_col.append(next_next_next_cell_value if not pd.isna(next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 3)} is out of bounds.")
                values_fourth_col.append("")
            
            # Get value from the fifth column
            if next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_col_index]
                values_fifth_col.append(next_next_next_next_cell_value if not pd.isna(next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 4)} is out of bounds.")
                values_fifth_col.append("")
            
            # Get value from the sixth column
            if next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_col_index]
                values_sixth_col.append(next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 5)} is out of bounds.")
                values_sixth_col.append("")
            
            # Get value from the seventh column
            if next_next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_next_col_index]
                values_seventh_col.append(next_next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 6)} is out of bounds.")
                values_seventh_col.append("")
            
            # Get value from the eighth column
            if next_next_next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_next_next_col_index]
                values_eighth_col.append(next_next_next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 7)} is out of bounds.")
                values_eighth_col.append("")
            
            # Get value from the ninth column
            if next_next_next_next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_next_next_next_col_index]
                values_ninth_col.append(next_next_next_next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 8)} is out of bounds.")
                values_ninth_col.append("")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
            values_first_col.append("")
            values_second_col.append("")
            values_third_col.append("")
            values_fourth_col.append("")
            values_fifth_col.append("")
            values_sixth_col.append("")
            values_seventh_col.append("")
            values_eighth_col.append("")
            values_ninth_col.append("")
    
    return (values_first_col, values_second_col, values_third_col, 
            values_fourth_col, values_fifth_col, values_sixth_col, 
            values_seventh_col, values_eighth_col, values_ninth_col)
# --------------------------- --------function to get 9columns ends------------------------------------------------




# --------------------------- --------function to get 10columns------------------------------------------------
def get_ten_column_values(CellNo, NextTableCellValue):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return [], [], [], [], [], [], [], [], [], []  # Return ten empty lists for the ten columns

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letters to indices
    col_index = ord(start_col) - ord('A')
    next_col_index = col_index + 1          # Index for the second column
    next_next_col_index = col_index + 2     # Index for the third column
    next_next_next_col_index = col_index + 3  # Index for the fourth column
    next_next_next_next_col_index = col_index + 4  # Index for the fifth column
    next_next_next_next_next_col_index = col_index + 5  # Index for the sixth column
    next_next_next_next_next_next_col_index = col_index + 6  # Index for the seventh column
    next_next_next_next_next_next_next_col_index = col_index + 7  # Index for the eighth column
    next_next_next_next_next_next_next_next_col_index = col_index + 8  # Index for the ninth column
    next_next_next_next_next_next_next_next_next_col_index = col_index + 9  # Index for the tenth column
    
    # Initialize lists to store values
    values_first_col = []
    values_second_col = []
    values_third_col = []
    values_fourth_col = []
    values_fifth_col = []
    values_sixth_col = []
    values_seventh_col = []
    values_eighth_col = []
    values_ninth_col = []
    values_tenth_col = []
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            # Get value from the first column
            if col_index < current_sheet.shape[1]:
                cell_value = current_sheet.iloc[row, col_index]
                values_first_col.append(cell_value if not pd.isna(cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {start_col} is out of bounds.")
                values_first_col.append("")
            
            # Get value from the second column
            if next_col_index < current_sheet.shape[1]:
                next_cell_value = current_sheet.iloc[row, next_col_index]
                values_second_col.append(next_cell_value if not pd.isna(next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 1)} is out of bounds.")
                values_second_col.append("")
            
            # Get value from the third column
            if next_next_col_index < current_sheet.shape[1]:
                next_next_cell_value = current_sheet.iloc[row, next_next_col_index]
                values_third_col.append(next_next_cell_value if not pd.isna(next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 2)} is out of bounds.")
                values_third_col.append("")
            
            # Get value from the fourth column
            if next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_cell_value = current_sheet.iloc[row, next_next_next_col_index]
                values_fourth_col.append(next_next_next_cell_value if not pd.isna(next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 3)} is out of bounds.")
                values_fourth_col.append("")
            
            # Get value from the fifth column
            if next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_col_index]
                values_fifth_col.append(next_next_next_next_cell_value if not pd.isna(next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 4)} is out of bounds.")
                values_fifth_col.append("")
            
            # Get value from the sixth column
            if next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_col_index]
                values_sixth_col.append(next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 5)} is out of bounds.")
                values_sixth_col.append("")
            
            # Get value from the seventh column
            if next_next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_next_col_index]
                values_seventh_col.append(next_next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 6)} is out of bounds.")
                values_seventh_col.append("")
            
            # Get value from the eighth column
            if next_next_next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_next_next_col_index]
                values_eighth_col.append(next_next_next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 7)} is out of bounds.")
                values_eighth_col.append("")
            
            # Get value from the ninth column
            if next_next_next_next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_next_next_next_col_index]
                values_ninth_col.append(next_next_next_next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 8)} is out of bounds.")
                values_ninth_col.append("")
            
            # Get value from the tenth column
            if next_next_next_next_next_next_next_next_next_col_index < current_sheet.shape[1]:
                next_next_next_next_next_next_next_next_next_cell_value = current_sheet.iloc[row, next_next_next_next_next_next_next_next_next_col_index]
                values_tenth_col.append(next_next_next_next_next_next_next_next_next_cell_value if not pd.isna(next_next_next_next_next_next_next_next_next_cell_value) else "")
            else:
                print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + 9)} is out of bounds.")
                values_tenth_col.append("")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
            values_first_col.append("")
            values_second_col.append("")
            values_third_col.append("")
            values_fourth_col.append("")
            values_fifth_col.append("")
            values_sixth_col.append("")
            values_seventh_col.append("")
            values_eighth_col.append("")
            values_ninth_col.append("")
            values_tenth_col.append("")
    
    return (values_first_col, values_second_col, values_third_col, 
            values_fourth_col, values_fifth_col, values_sixth_col, 
            values_seventh_col, values_eighth_col, values_ninth_col, values_tenth_col)
# --------------------------- --------function to get 10columns ends------------------------------------------------


# --------------------------- --------function to get 13columns------------------------------------------------
def get_thirteen_column_values(CellNo, NextTableCellValue):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return [], [], [], [], [], [], [], [], [], [], [], [], []  # Return thirteen empty lists for the thirteen columns

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letters to indices
    col_index = ord(start_col) - ord('A')
    col_indices = [col_index + i for i in range(13)]  # Generate indices for 13 columns
    
    # Initialize lists to store values for each column
    values = [[] for _ in range(13)]
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            for i, col_idx in enumerate(col_indices):
                if col_idx < current_sheet.shape[1]:
                    cell_value = current_sheet.iloc[row, col_idx]
                    values[i].append(cell_value if not pd.isna(cell_value) else "")
                else:
                    print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + i)} is out of bounds.")
                    values[i].append("")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
            for col_values in values:
                col_values.append("")
    
    # Return tuple of all column value lists
    return tuple(values)
# --------------------------- --------function to get 13columns ends------------------------------------------------






# --------------------------- --------function to get multiple columns ends------------------------------------------------
def get_multiple_column_values(CellNo, NextTableCellValue, num_columns=3):
    # Get start and end cell references using GetColumnValidIndex
    start_cell, end_cell = GetColumnValidIndex(CellNo, NextTableCellValue)
    
    if start_cell is None or end_cell is None:
        print("Error: Could not determine valid cell range")
        return [[] for _ in range(num_columns)]  # Return a list of empty lists for the columns

    # Extract column letter and row numbers
    start_col = ''.join(filter(str.isalpha, start_cell))
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    
    # Convert column letters to index
    col_index = ord(start_col) - ord('A')
    
    # Initialize lists to store values for each column
    column_values = [[] for _ in range(num_columns)]
    
    for row in range(start_row - 1, end_row):  # Subtract 1 from start_row because pandas is 0-indexed
        if row < current_sheet.shape[0]:
            for col in range(num_columns):  # Loop through the desired columns
                current_col_index = col_index + col
                if current_col_index < current_sheet.shape[1]:
                    cell_value = current_sheet.iloc[row, current_col_index]
                    column_values[col].append(cell_value if not pd.isna(cell_value) else "")
                else:
                    print(f"Warning: Cell at row {row+1}, column {chr(ord(start_col) + col)} is out of bounds.")
                    column_values[col].append("")
        else:
            print(f"Warning: Row {row+1} is out of bounds.")
            for col in range(num_columns):  # Fill missing rows with empty values
                column_values[col].append("")
    
    return column_values
# values = get_multiple_column_values('A1', 'E10', num_columns=5)
# --------------------------- --------function to get  multiple columns ends------------------------------------------------




# --------------------------- function to get any number of column --------------------------------------


def get_column_values(start_row, end_row, col_indices, current_sheet):
    """
    Reads values from specified columns within a given row range.
    
    Parameters:
    - start_row (int): Starting row (1-based index).
    - end_row (int): Ending row (1-based index).
    - col_indices (list of int): List of column indices (0-based index).
    - current_sheet (DataFrame): Pandas DataFrame representing the sheet.
    
    Returns:
    - dict: A dictionary with column index as keys and their respective values as lists.
    """
    result = {}
    for col_index in col_indices:
        col_values = []
        for row in range(start_row - 1, end_row):  
            if row < current_sheet.shape[0] and col_index < current_sheet.shape[1]:
                cell_value = current_sheet.iloc[row, col_index]
                col_values.append(cell_value if not pd.isna(cell_value) else "")
            else:
                col_values.append("")  
        result[col_index] = col_values
    return result



    # Reading  values for column 1, 2, and 3 (3 column 5 rows )
result = get_column_values(start_row=1, end_row=5, col_indices=[0, 1, 2], current_sheet=current_sheet)

# Print results
for col_index, values in result.items():
    print(f"Column {col_index + 1}: {values}")

# If we dont know the end_row
#  result = get_column_values(start_row=1, end_row=None, col_indices=[0, 1, 2], current_sheet=current_sheet)
       
# --------------------------- function to get any number of column ends--------------------------------------





def get_selected_cells_values(sheet, cells):
    """
    Extracts the values from specified cell references in a pandas DataFrame.

    Parameters:
        sheet (pd.DataFrame): The DataFrame representing the spreadsheet.
        cells (list): A list of cell references (e.g., ['A1', 'B1', 'C1']).

    Returns:
        list: A list of values from the specified cells.
    """
    values = []
    for cell in cells:
        # Extract column letter and row number
        col_letter = ''.join(filter(str.isalpha, cell))  # Get column (e.g., 'A')
        row_number = int(''.join(filter(str.isdigit, cell))) - 1  # Get row (convert to 0-indexed)
        
        # Convert column letter to index (A=0, B=1, etc.)
        col_index = ord(col_letter.upper()) - ord('A')
        
        # Get value if within bounds
        if row_number < sheet.shape[0] and col_index < sheet.shape[1]:
            values.append(sheet.iloc[row_number, col_index])
        else:
            values.append(None)  # Return None for out-of-bounds cells

    return values

# Specify the cells you want to extract
cell_references = ['A1', 'B2', 'C3', 'D1']  # Example input

# Get the values from the specified cells
selected_values = get_selected_cells_values(current_sheet, cell_references)

print(f"Values for {cell_references}: {selected_values}")