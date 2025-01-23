import xml.etree.ElementTree as ET

def indent(elem, level=0):
    """Adds indentation to the XML tree."""
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def group_elements(input_file, output_file):
    """
    Groups elements with the same tags and inserts blank lines between different groups.
    :param input_file: Path to the input ARXML file.
    :param output_file: Path to the output ARXML file.
    """
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Create a new root for the output ARXML
    output_root = ET.Element('AUTOSAR', attrib={
        'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'xmlns': "http://autosar.org/schema/r4.0",
        'xsi:schemaLocation': "http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd"
    })

    # Dictionary to group elements by tag
    grouped_elements = {}

    for elem in root.findall(".//ELEMENTS/*"):
        tag = elem.tag
        if tag not in grouped_elements:
            grouped_elements[tag] = []
        grouped_elements[tag].append(elem)

    # Add grouped elements to the output
    for tag, elements in grouped_elements.items():
        parent = ET.SubElement(output_root, 'ELEMENTS')
        for elem in elements:
            new_elem = ET.SubElement(parent, elem.tag, attrib=elem.attrib)
            for child in elem:
                sub_elem = ET.SubElement(new_elem, child.tag)
                sub_elem.text = child.text
                sub_elem.attrib = child.attrib

        # Add a blank line after each group
        ET.SubElement(output_root, 'BLANK-LINE')

    # Remove the trailing blank line (if present)
    blank_lines = output_root.findall("BLANK-LINE")
    if blank_lines:
        output_root.remove(blank_lines[-1])

    # Add indentation for readability
    indent(output_root)

    # Write the output ARXML
    output_tree = ET.ElementTree(output_root)
    output_tree.write(output_file, encoding="utf-8", xml_declaration=True)

# if __name__ == "__main__":
#     input_arxml = "path/to/4_0_3_onlyelements.arxml"  # Replace with your input ARXML file path
#     output_arxml = "path/to/output.arxml"  # Replace with your output ARXML file path
#     group_elements(input_arxml, output_arxml)



if __name__ == "__main__":
    # Example usage
    input_arxml = "D:\\MyProjects\\Saarconn\\4_0_3_onlyelements.arxml"  # Replace with your ARXML file path
    output_arxml = "D:\\MyProjects\\Saarconn\\genTest.py"  # Replace with your output Python file path
    group_elements(input_arxml, output_arxml)
