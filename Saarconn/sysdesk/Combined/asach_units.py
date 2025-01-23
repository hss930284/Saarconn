import re

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Dictionary to store the mapping between unitX and short_nameX.text
    unit_mapping = {}

    # Iterate through the lines to find unitX and short_nameX.text
    for i, line in enumerate(lines):
        # Check if the line starts with 'unitX'
        if line.strip().startswith('unit'):
            # Extract the number X from 'unitX'
            match = re.match(r'unit(\d+)', line.strip())
            if match:
                unit_number = match.group(1)
                # Look ahead 2 lines to find the corresponding short_nameX.text
                if i + 2 < len(lines):
                    short_name_line = lines[i + 2].strip()
                    # Extract the value from short_nameX.text
                    short_name_match = re.match(r'short_name\d+\.text\s*=\s*\'(.*?)\'', short_name_line)
                    if short_name_match:
                        short_name_value = short_name_match.group(1)
                        # Map the unit number to the short name value
                        unit_mapping[unit_number] = short_name_value

    # Replace patterns within the scope of each unitX block
    current_unit = None
    for i, line in enumerate(lines):
        # Check if the line starts with 'unitX'
        if line.strip().startswith('unit'):
            match = re.match(r'unit(\d+)', line.strip())
            if match:
                unit_number = match.group(1)
                if unit_number in unit_mapping:
                    # Update the current unit being processed
                    current_unit = unit_number
                    # Replace unitX with unit_short_name_value
                    short_name_value = unit_mapping[unit_number]
                    new_line = line.replace(f'unit{unit_number}', f'unit_{short_name_value}')
                    lines[i] = new_line
        # If we are in the scope of a unitX, replace all occurrences of the specified patterns
        elif current_unit is not None:
            # Get the short name value for the current unit
            short_name_value = unit_mapping[current_unit]
            # Define the patterns to replace
            patterns = [
                (r'short_name(\d+)', f'unit_{short_name_value}_short_name'),
                (r'long_name(\d+)', f'unit_{short_name_value}_long_name'),
                (r'l_4(\d+)', f'unit_{short_name_value}_l_4'),
                (r'display_name(\d+)', f'unit_{short_name_value}_display_name'),
                (r'factor_si_to_unit(\d+)', f'unit_{short_name_value}_factor_si_to_unit'),
                (r'offset_si_to_unit(\d+)', f'unit_{short_name_value}_offset_si_to_unit'),
                (r'physical_dimension_ref(\d+)', f'unit_{short_name_value}_physical_dimension_ref'),
            ]
            # Replace each pattern in the line
            for pattern, replacement in patterns:
                lines[i] = re.sub(pattern, replacement, lines[i])
            # Replace unitX with unit_short_name_value in the line
            lines[i] = lines[i].replace(f'unit{current_unit}', f'unit_{short_name_value}')

    # Write the modified lines to the output file
    with open(output_file, 'w') as file:
        file.writelines(lines)

# Example usage
input_file = 'input.txt'
output_file = 'output.txt'
process_file(input_file, output_file)