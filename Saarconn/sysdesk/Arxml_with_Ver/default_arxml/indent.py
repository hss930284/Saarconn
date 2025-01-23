import xml.etree.ElementTree as ET

def remove_namespaces(element):
    """
    Removes namespace prefixes from element tags.

    Args:
        element: The root element of the XML tree.

    Returns:
        The modified element with namespaces removed.
    """
    for elem in element.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]  # Remove namespace prefix
    return element

def indent(elem, level=0):
    """
    Adds indentation to the XML tree.
    """
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def pretty_print_arxml(input_file, output_file):
    """
    Reads an ARXML file, removes namespaces, adds indentation, and writes it to a new file.

    Args:
        input_file: Path to the input ARXML file.
        output_file: Path to the output ARXML file with indentation.
    """
    try:
        tree = ET.parse(input_file)
        root = tree.getroot()

        # Remove namespaces
        root = remove_namespaces(root)

        # Add indentation
        indent(root)

        # Write the XML declaration with double quotes
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            tree.write(f, encoding='unicode', xml_declaration=False)

        print(f"Successfully created {output_file} with proper indentation and XML declaration.")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please enter a valid ARXML file path.")

if __name__ == "__main__":
    input_arxml = input("Enter the path to your ARXML file: ")
    output_arxml = "output_indented1.arxml"  # You can change this if needed
    # Write to file with double quotes in the XML declaration
   

    pretty_print_arxml(input_arxml, output_arxml)