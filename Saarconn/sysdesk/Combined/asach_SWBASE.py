import re

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Dictionary to store the mapping between sw_base_typeX and short_nameX.text
    sw_base_type_mapping = {}

    # Iterate through the lines to find sw_base_typeX and their corresponding short_nameX.text
    for i, line in enumerate(lines):
        # Check if the line starts with 'sw_base_typeX'
        if line.strip().startswith('sw_base_type'):
            # Extract the number X from 'sw_base_typeX'
            match = re.match(r'sw_base_type(\d+)', line.strip())
            if match:
                sw_base_type_number = match.group(1)
                # Look ahead 2 lines to find the corresponding short_nameX.text
                if i + 2 < len(lines):
                    short_name_line = lines[i + 2].strip()
                    # Extract the value from short_nameX.text
                    short_name_match = re.match(r'short_name\d+\.text\s*=\s*\'(.*?)\'', short_name_line)
                    if short_name_match:
                        short_name_value = short_name_match.group(1)
                        # Map the sw_base_type number to the short name value
                        sw_base_type_mapping[sw_base_type_number] = short_name_value

    # Replace patterns within the scope of each sw_base_typeX block
    current_sw_base_type = None
    for i, line in enumerate(lines):
        # Check if the line starts with 'sw_base_typeX'
        if line.strip().startswith('sw_base_type'):
            match = re.match(r'sw_base_type(\d+)', line.strip())
            if match:
                sw_base_type_number = match.group(1)
                if sw_base_type_number in sw_base_type_mapping:
                    # Update the current sw_base_type being processed
                    current_sw_base_type = sw_base_type_number
                    # Replace sw_base_typeX with sw_base_type_short_name_value
                    short_name_value = sw_base_type_mapping[sw_base_type_number]
                    new_line = line.replace(f'sw_base_type{sw_base_type_number}', f'sw_base_type_{short_name_value}')
                    lines[i] = new_line
        # If we are in the scope of a sw_base_typeX, replace all occurrences of the specified patterns
        elif current_sw_base_type is not None:
            short_name_value = sw_base_type_mapping[current_sw_base_type]
            patterns = [
                (r'short_name(\d+)', f'sw_base_type_{short_name_value}_short_name'),
                (r'long_name(\d+)', f'sw_base_type_{short_name_value}_long_name'),
                (r'l_4(\d+)', f'sw_base_type_{short_name_value}_l_4'),
                (r'category(\d+)', f'sw_base_type_{short_name_value}_category'),
                (r'base_type_size(\d+)', f'sw_base_type_{short_name_value}_base_type_size'),
                (r'base_type_encoding(\d+)', f'sw_base_type_{short_name_value}_base_type_encoding'),
            ]
            for pattern, replacement in patterns:
                lines[i] = re.sub(pattern, replacement, lines[i])
            lines[i] = lines[i].replace(f'sw_base_type{current_sw_base_type}', f'sw_base_type_{short_name_value}')

    # Write the modified lines to the output file
    with open(output_file, 'w') as file:
        file.writelines(lines)

# Example usage
input_file = 'input.txt'
output_file = 'output.txt'
process_file(input_file, output_file)