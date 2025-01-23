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

# Global dictionary for element references
global_elements = {}

def indent(elem, level=0):
    """
    Adds indentation to the XML tree to make it more readable.
    """
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for child in elem:
            indent(child, level+1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def generate_python_script(arxml_file, output_file, sample_script):
    """
    Generates a Python script that defines the XML structure from an ARXML file,
    aligning with the provided sample Python script.
    """
    try:
        tree = ET.parse(arxml_file)
        root = tree.getroot()

        with open(sample_script, 'r', encoding='utf-8') as sample_f:
            sample_content = sample_f.read()

        # Start of the generated Python script
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("import xml.etree.ElementTree as ET\n")
            f.write("global_elements = {}\n\n")
            f.write(sample_content.split("def create_arxml()")[0])
            f.write("def create_arxml():\n")
            f.write("    global global_elements\n")
            f.write("    root_tag = '{}'\n".format(root.tag.split('}')[-1]))
            f.write("    global_elements['root'] = ET.Element(root_tag, attrib={})\n".format(repr(root.attrib)))

            # Recursively generate children
            _generate_children(root, f, 1, {}, 'root')

            # Prettify and save the XML tree
            f.write("\n    indent(global_elements['root'])\n")
            f.write("    tree = ET.ElementTree(global_elements['root'])\n")
            f.write("    tree.write('output.arxml', encoding='utf-8', xml_declaration=True)\n")
            f.write("\nif __name__ == '__main__':\n")
            f.write("    create_arxml()\n")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please enter a valid ARXML file path.")

def _generate_children(parent, f, level, var_counts, parent_var_name):
    """
    Recursively generates Python code for child elements, aligning with the sample script's style.
    Each variable name will be more descriptive based on the element's tag and a key attribute.
    """
    for child in parent:
        indent = "    " * level
        tag = child.tag.split('}')[-1].lower()
        
        # Find 'SHORT-NAME' and use its content to generate a descriptive variable name.
        short_name_element = child.find('.//SHORT-NAME')
        if short_name_element is not None and short_name_element.text:
            descriptive_name = short_name_element.text.replace(' ', '_').replace('-', '_').lower()
            base_var_name = f"{descriptive_name}_{tag}"
        else:
            base_var_name = tag  # Fallback to just the tag name if no SHORT-NAME is available.

        # Ensure uniqueness of variable names.
        if base_var_name in var_counts:
            var_counts[base_var_name] += 1
            full_var_name = f"{base_var_name}{var_counts[base_var_name]}"
        else:
            var_counts[base_var_name] = 1
            full_var_name = base_var_name

        var_name = full_var_name

        # Write the element creation to the script
        f.write(f"{indent}global_elements['{var_name}'] = ET.SubElement(global_elements['{parent_var_name}'], '{tag}')\n")

        # Handle text content and attributes.
        if child.text and child.text.strip():
            f.write(f"{indent}global_elements['{var_name}'].text = {repr(child.text.strip())}\n")
        if child.attrib:
            stripped_attrib = {k.split('}')[-1]: v for k, v in child.attrib.items()}
            f.write(f"{indent}global_elements['{var_name}'].attrib = {repr(stripped_attrib)}\n")

        # Recursively handle child elements.
        if len(child):
            _generate_children(child, f, level + 1, var_counts, var_name)


if __name__ == '__main__':
    input_arxml = get_user_input("Enter the path to your ARXML file: ")
    output_python = "generated_script_with_global_elements.py"
    sample_script = get_user_input("Enter the path to your sample Python script: ")

    generate_python_script(input_arxml, output_python, sample_script)
