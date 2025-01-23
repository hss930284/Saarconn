# Load the first sheet to extract project information
    first_sheet = pd.read_excel(Input_Excel_File, sheet_name=0)
    sd_project = first_sheet.iloc[4, 3]  # Get project name from cell C4

    # Load subsequent sheets
    for sheet_name in xls.sheet_names[1:]:
        current_sheet = pd.read_excel(Input_Excel_File, sheet_name=sheet_name)