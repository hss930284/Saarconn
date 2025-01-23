from collections import OrderedDict

def remove_duplicate_lines(input_file, output_file):
    """
    Removes duplicate lines from a text file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    unique_lines = OrderedDict((line, None) for line in lines)
    with open(output_file, 'w') as f_out:
        f_out.writelines(unique_lines.keys())

# Example usage:
input_file = 'Pkg_struct_dup.py'
output_file = 'Pkg_struct.py'
remove_duplicate_lines(input_file, output_file)