import re

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Dictionary to store the mapping between implementation_data_typeX and short_nameX.text
    data_type_mapping = {}

    # Iterate through the lines to find implementation_data_typeX and short_nameX.text
    for i, line in enumerate(lines):
        # Check if the line starts with 'implementation_data_typeX'
        if line.strip().startswith('implementation_data_type'):
            # Extract the number X from 'implementation_data_typeX'
            match = re.match(r'implementation_data_type(\d+)', line.strip())
            if match:
                data_type_number = match.group(1)
                # Look ahead 2 lines to find the corresponding short_nameX.text
                if i + 2 < len(lines):
                    short_name_line = lines[i + 2].strip()
                    # Extract the value from short_nameX.text
                    short_name_match = re.match(r'short_name\d+\.text\s*=\s*\'(.*?)\'', short_name_line)
                    if short_name_match:
                        short_name_value = short_name_match.group(1)
                        # Map the data type number to the short name value
                        data_type_mapping[data_type_number] = short_name_value

    # Replace patterns within the scope of each implementation_data_typeX block
    current_data_type = None
    for i, line in enumerate(lines):
        # Check if the line starts with 'implementation_data_typeX'
        if line.strip().startswith('implementation_data_type'):
            match = re.match(r'implementation_data_type(\d+)', line.strip())
            if match:
                data_type_number = match.group(1)
                if data_type_number in data_type_mapping:
                    # Update the current data type being processed
                    current_data_type = data_type_number
                    # Replace implementation_data_typeX with implementation_data_type_short_name_value
                    short_name_value = data_type_mapping[data_type_number]
                    new_line = line.replace(f'implementation_data_type{data_type_number}', f'implementation_data_type_{short_name_value}')
                    lines[i] = new_line
        # If we are in the scope of an implementation_data_typeX, replace all occurrences of the specified patterns
        elif current_data_type is not None:
            # Get the short name value for the current data type
            short_name_value = data_type_mapping[current_data_type]
            # Define the patterns to replace
            patterns = [
                (r'short_name(\d+)', f'implementation_data_type_{short_name_value}_short_name'),
                (r'long_name(\d+)', f'implementation_data_type_{short_name_value}_long_name'),
                (r'l_4(\d+)', f'implementation_data_type_{short_name_value}_l_4'),
                (r'category(\d+)', f'implementation_data_type_{short_name_value}_category'),
                (r'sw_data_def_props(\d+)', f'implementation_data_type_{short_name_value}_sw_data_def_props'),
                (r'sw_data_def_props_variants(\d+)', f'implementation_data_type_{short_name_value}_sw_data_def_props_variants'),
                (r'sw_data_def_props_conditional(\d+)', f'implementation_data_type_{short_name_value}_sw_data_def_props_conditional'),
                (r'sw_pointer_target_props(\d+)', f'implementation_data_type_{short_name_value}_sw_pointer_target_props'),
                (r'target_category(\d+)', f'implementation_data_type_{short_name_value}_target_category'),
                (r'base_type_ref(\d+)', f'implementation_data_type_{short_name_value}_base_type_ref'),
                (r'sw_impl_policy(\d+)', f'implementation_data_type_{short_name_value}_sw_impl_policy'),
                (r'type_emitter(\d+)', f'implementation_data_type_{short_name_value}_type_emitter'),
            ]
            # Replace each pattern in the line
            for pattern, replacement in patterns:
                lines[i] = re.sub(pattern, replacement, lines[i])
            # Replace implementation_data_typeX with implementation_data_type_short_name_value in the line
            lines[i] = lines[i].replace(f'implementation_data_type{current_data_type}', f'implementation_data_type_{short_name_value}')

    # Write the modified lines to the output file
    with open(output_file, 'w') as file:
        file.writelines(lines)

# Example usage
input_file = 'input.txt'
output_file = 'output.txt'
process_file(input_file, output_file)