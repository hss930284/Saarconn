import re

def convert_to_snake_case(text):
    """Convert hyphenated strings inside global_elements to snake_case."""
    if isinstance(text, str):
        return re.sub(r'[-]', '_', text).lower()
    return text

def process_global_elements(code_lines):
    processed_lines = []
    
    for line in code_lines:
        # Find all occurrences of global_elements and process the string inside ['']
        matches = re.findall(r"global_elements\['(.*?)'\]", line)
        
        # For each match found, convert it to snake_case
        for match in matches:
            converted = convert_to_snake_case(match)
            line = line.replace(f"global_elements['{match}']", converted)

        # Append processed line
        processed_lines.append(line)

    return processed_lines

def convert_to_uppercase_in_subelement(line):
    """Convert the string inside single quotes inside ET.SubElement() to uppercase, keeping the quotes."""
    # This will find strings inside ET.SubElement and convert them to uppercase
    return re.sub(r"ET\.SubElement\([^,]*, '([^']*)'", lambda match: f"ET.SubElement({match.group(1)}, '{match.group(1).upper()}'", line)

def process_code_for_uppercase_in_subelement(code):
    # Process each line for ET.SubElement to convert strings inside quotes to uppercase
    processed_lines = []
    for line in code:
        # Convert strings inside ET.SubElement and single quotes to uppercase
        line = convert_to_uppercase_in_subelement(line)
        processed_lines.append(line)

    # Return processed lines as a string to maintain line breaks and indentation
    return ''.join(processed_lines)

def process_file(file_path):
    # Read the Python file
    with open(file_path, 'r') as file:
        code_lines = file.readlines()

    # Process the code lines for global_elements
    processed_lines = process_global_elements(code_lines)

    # Return the processed code lines as a string to maintain line breaks and indentation
    return processed_lines

# Provide the path to your Python file
file_path = 'Eliminating_SystemDesk\\trash\\harshit\\Saarconn\\enhanced_arelements\\4_1_2.py'
output_file = 'Eliminating_SystemDesk\\trash\\harshit\\Saarconn\\remove_GE_ARELE\\_4_1_2.py'

# Step 1: Process the code for global_elements (change to snake_case)
processed_code = process_file(file_path)

# Step 2: Process the code for uppercase conversion inside ET.SubElement
final_code = process_code_for_uppercase_in_subelement(processed_code)

# Step 3: Write the final code to the output file
with open(output_file, 'w') as file:
    file.write(final_code)
