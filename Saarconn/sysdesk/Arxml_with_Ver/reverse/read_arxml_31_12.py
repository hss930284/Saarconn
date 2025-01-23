import xml.etree.ElementTree as ET
import pandas as pd # type: ignore

def parse_arxml(arxml_file, excel_file):
    # Parse the .arxml file using ElementTree
    tree = ET.parse(arxml_file)
    root = tree.getroot()

    # Lists to store Type, Short Name, and UUID data
    types = []
    short_names = []
    uuids = []

    # Define namespaces in the XML (to avoid issues with XML namespace prefixes)
    namespaces = {'': 'http://autosar.org/schema/r4.0'}

    # Iterate over all elements and collect necessary information
    def extract_data(element):
        # If the element has a SHORT-NAME tag, we collect the data
        for child in element:
            if child.tag.endswith('SHORT-NAME'):  # Handle namespace
                # Get the short name text
                short_name = child.text.strip() if child.text else "No Name"
                short_names.append(short_name)
                
                # Get the parent type (the element tag of the parent node)
                parent_type = element.tag.split('}')[1] if '}' in element.tag else element.tag  # Clean namespace
                types.append(parent_type)
                
                # Check if UUID is present for this element
                uuid = element.get('UUID', "No UUID")  # Get UUID if exists
                uuids.append(uuid)

            # Recurse into the child elements
            extract_data(child)

    # Start the extraction from the root element
    extract_data(root)

    # Create a DataFrame to store the results with columns: Type, Short Name, UUID
    data = {
        "Type": types,
        "Short Name": short_names,
        "UUID": uuids
    }
    df = pd.DataFrame(data)

    # Sort the DataFrame by the "Type" column
    df_sorted = df.sort_values(by="Type").reset_index(drop=True)

    # Save the sorted DataFrame to the provided Excel file with the custom sheet name
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        df_sorted.to_excel(writer, sheet_name='arxml_elements', index=False)

    print(f"Excel file saved at {excel_file}")

# Prompt the user to provide the .arxml file and Excel file paths
arxml_file = input("Please provide the full path to the .arxml file: ")
excel_file = input("Please provide the full path to save the Excel file (e.g., output.xlsx): ")

# Run the function
parse_arxml(arxml_file, excel_file)
