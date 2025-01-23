import xml.etree.ElementTree as ET

def get_user_input(prompt):
    """
    Gets user input for the specified prompt.
    """
    while True:
        value = input(prompt)
        if value:
            return value
        else:
            print("Please enter a valid value.")

def generate_python_script(arxml_file, output_file, sample_script):
    """
    Generates a Python script that defines the XML structure from an ARXML file,
    aligning with the provided sample Python script.

    Args:
        arxml_file: Path to the input ARXML file (provided by user).
        output_file: Path to the output Python script file.
        sample_script: Path to the sample Python script for alignment.
    """
    try:
        # Parse the ARXML file
        tree = ET.parse(arxml_file)
        root = tree.getroot()

        # Read the sample script to understand its structure
        with open(sample_script, 'r', encoding='utf-8') as sample_f:
            sample_content = sample_f.read()

        # Generate the Python script
        with open(output_file, 'w', encoding='utf-8') as f:
            # Write the sample script's header or any fixed content
            f.write(sample_content.split("def create_arxml()")[0])

            # Write the function to create ARXML
            f.write("def create_arxml():\n")
            f.write("    \"\"\"\n")
            f.write("    Creates an ARXML file with the specified structure.\n")
            f.write("    \"\"\"\n")

            # Strip namespace from the root tag
            root_tag = root.tag.split('}')[-1]  # Remove namespace prefix
            f.write(f"    root = ET.Element('{root_tag}', attrib={repr(root.attrib)})\n")
            _generate_children(root, f, 1)  # Adjust indentation level as per sample script

            # Write the sample script's footer or any fixed content
            f.write("\n    # Save the XML tree to an ARXML file\n")
            f.write("    tree = ET.ElementTree(root)\n")
            f.write("    tree.write('output.arxml', encoding='utf-8', xml_declaration=True)\n\n")
            f.write("if __name__ == '__main__':\n")
            f.write("    create_arxml()\n")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please enter a valid ARXML file path.")

def _generate_children(parent, f, level):
    """
    Recursively generates Python code for child elements, aligning with the sample script's style.
    """
    for child in parent:
        indent = "    " * level  # Adjust indentation as per sample script
        tag = child.tag.split('}')[-1]  # Remove namespace prefix
        var_name = tag.replace('-', '_').lower()  # Convert to lowercase and replace hyphens with underscores

        # Write the SubElement creation
        f.write(f"{indent}{var_name} = ET.SubElement({parent.tag.split('}')[-1].replace('-', '_').lower()}, '{tag}')\n")

        # Handle text content
        if child.text and child.text.strip():  # Only write text if it's not just whitespace
            try:
                f.write(f"{indent}{var_name}.text = {repr(child.text.strip())}\n")
            except UnicodeEncodeError:
                escaped_text = child.text.encode('utf-8', 'xmlcharref').decode('utf-8')
                f.write(f"{indent}{var_name}.text = {repr(escaped_text.strip())}\n")

        # Handle attributes
        if child.attrib:
            # Strip namespace from attribute keys if present
            stripped_attrib = {k.split('}')[-1]: v for k, v in child.attrib.items()}
            f.write(f"{indent}{var_name}.attrib = {repr(stripped_attrib)}\n")

        # Recursively handle child elements
        if len(child):
            _generate_children(child, f, level + 1)  # Pass the current child as the new parent

if __name__ == '__main__':
    input_arxml = get_user_input("Enter the path to your ARXML file: ")
    output_python = "generated_script.py"  # Replace with the desired output file name
    sample_script = get_user_input("Enter the path to your sample Python script: ")

    generate_python_script(input_arxml, output_python, sample_script)