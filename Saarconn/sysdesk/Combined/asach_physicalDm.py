import re

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Dictionary to store the mapping between physical_dimensionX and short_nameX.text
    dimension_mapping = {}

    # Iterate through the lines to find physical_dimensionX and short_nameX.text
    for i, line in enumerate(lines):
        # Check if the line starts with 'physical_dimensionX'
        if line.strip().startswith('physical_dimension'):
            # Extract the number X from 'physical_dimensionX'
            match = re.match(r'physical_dimension(\d+)', line.strip())
            if match:
                dimension_number = match.group(1)
                # Look ahead 3 lines to find the corresponding short_nameX.text
                if i + 2 < len(lines):
                    short_name_line = lines[i + 2].strip()
                    # Extract the value from short_nameX.text
                    short_name_match = re.match(r'short_name\d+\.text\s*=\s*\'(.*?)\'', short_name_line)
                    if short_name_match:
                        short_name_value = short_name_match.group(1)
                        # Map the dimension number to the short name value
                        dimension_mapping[dimension_number] = short_name_value

    # Replace patterns within the scope of each physical_dimensionX block
    current_dimension = None
    for i, line in enumerate(lines):
        # Check if the line starts with 'physical_dimensionX'
        if line.strip().startswith('physical_dimension'):
            match = re.match(r'physical_dimension(\d+)', line.strip())
            if match:
                dimension_number = match.group(1)
                if dimension_number in dimension_mapping:
                    # Update the current dimension being processed
                    current_dimension = dimension_number
                    # Replace physical_dimensionX with physical_dimension_short_name_value
                    short_name_value = dimension_mapping[dimension_number]
                    new_line = line.replace(f'physical_dimension{dimension_number}', f'physical_dimension_{short_name_value}')
                    lines[i] = new_line
        # If we are in the scope of a physical_dimensionX, replace all occurrences of the specified patterns
        elif current_dimension is not None:
            # Get the short name value for the current dimension
            short_name_value = dimension_mapping[current_dimension]
            # Define the patterns to replace
            patterns = [
                (r'short_name(\d+)', f'physical_dimension_{short_name_value}_short_name'),
                (r'long_name(\d+)', f'physical_dimension_{short_name_value}_long_name'),
                (r'l_4(\d+)', f'physical_dimension_{short_name_value}_l_4'),
                (r'length_exp(\d+)', f'physical_dimension_{short_name_value}_length_exp'),
                (r'mass_exp(\d+)', f'physical_dimension_{short_name_value}_mass_exp'),
                (r'time_exp(\d+)', f'physical_dimension_{short_name_value}_time_exp'),
                (r'current_exp(\d+)', f'physical_dimension_{short_name_value}_current_exp'),
                (r'temperature_exp(\d+)', f'physical_dimension_{short_name_value}_temperature_exp'),
                (r'molar_amount_exp(\d+)', f'physical_dimension_{short_name_value}_molar_amount_exp'),
                (r'luminous_intensity_exp(\d+)', f'physical_dimension_{short_name_value}_luminous_intensity_exp'),
            ]
            # Replace each pattern in the line
            for pattern, replacement in patterns:
                lines[i] = re.sub(pattern, replacement, lines[i])
            # Replace physical_dimensionX with physical_dimension_short_name_value in the line
            lines[i] = lines[i].replace(f'physical_dimension{current_dimension}', f'physical_dimension_{short_name_value}')

    # Write the modified lines to the output file
    with open(output_file, 'w') as file:
        file.writelines(lines)

# Example usage
input_file = 'input.txt'
output_file = 'output.txt'
process_file(input_file, output_file)