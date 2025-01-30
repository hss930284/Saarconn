import re

def convert_to_uppercase_in_subelement(line):
    """Finds and converts ONLY the string inside single quotes in ET.SubElement() to uppercase."""
    return re.sub(
        r"(ET\.SubElement\([^,]+, ')([^']*)('\))",  # Captures only the string inside single quotes
        lambda match: f"{match.group(1)}{match.group(2).upper()}{match.group(3)}",
        line
    )

def process_file_for_uppercase_in_subelement(file_path):
    """Reads a Python file, processes ET.SubElement(), and writes the modified content."""
    with open(file_path, 'r') as file:
        code_lines = file.readlines()  # Read file as list of lines

    # Process each line
    processed_lines = [convert_to_uppercase_in_subelement(line) for line in code_lines]

    # Return modified code as a string
    return ''.join(processed_lines)

# Provide the path to your Python file
file_path = 'Eliminating_SystemDesk\\trash\\harshit\\Saarconn\\Updated_ARELE_Versions\\22_11.py'  # Change this to your actual file path
output_file = 'Eliminating_SystemDesk\\trash\\harshit\\Saarconn\\Enhanced_arele\\22_11.py'  # Output file path

# Process the Python file
processed_code = process_file_for_uppercase_in_subelement(file_path)

# Write the final processed code to the output file
with open(output_file, 'w') as file:
    file.write(processed_code)

# Print output for verification
# print(processed_code)
