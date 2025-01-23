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


def create_arxml():
    """
    Creates an ARXML file with the specified structure and proper indentation.
    """
    root = ET.Element("AUTOSAR", 
                        attrib={
                            "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                            "xmlns": "http://autosar.org/schema/r4.0",
                            "xsi:schemaLocation": "http://autosar.org/schema/r4.0 AUTOSAR_00051.xsd"
                        })
    root_folders = ET.SubElement(root, 'AR-PACKAGES')
    autosar_folder = ET.SubElement(root_folders, 'AR-PACKAGE')
    autosar_folder.attrib = {'UUID': '5983c226-f5b2-4ba1-958d-32fe5f2fde51'}
    autosar_folder_short_name = ET.SubElement(autosar_folder, 'SHORT-NAME')
    autosar_folder_short_name.text = 'AUTOSAR'
    autosar_subfolders = ET.SubElement(autosar_folder, 'AR-PACKAGES')
    AUTOSAR_GenDef_folder = ET.SubElement(autosar_subfolders, 'AR-PACKAGE')
    AUTOSAR_GenDef_folder_short_name = ET.SubElement(AUTOSAR_GenDef_folder, 'SHORT-NAME')
    AUTOSAR_GenDef_folder_short_name.text = 'AUTOSAR_GenDef'
    AUTOSAR_GenDef_subfolders = ET.SubElement(AUTOSAR_GenDef_folder, 'AR-PACKAGES')
    BaseTypes_folder = ET.SubElement(AUTOSAR_GenDef_subfolders, 'AR-PACKAGE')
    BaseTypes_folder_short_name = ET.SubElement(BaseTypes_folder, 'SHORT-NAME')
    BaseTypes_folder_short_name.text = 'BaseTypes'
    BaseTypes_folder_category = ET.SubElement(BaseTypes_folder, 'CATEGORY')
    BaseTypes_folder_category.text = 'STANDARD'
    BaseTypes_folder_elements = ET.SubElement(BaseTypes_folder, 'ELEMENTS')
    Void_basetype = ET.SubElement(BaseTypes_folder_elements, 'SW-BASE-TYPE')
    Void_basetype_short_name = ET.SubElement(Void_basetype, 'SHORT-NAME')
    Void_basetype_short_name.text = 'void'
    Void_basetype_long_name = ET.SubElement(Void_basetype, 'LONG-NAME')
    Void_basetype_l_4 = ET.SubElement(Void_basetype_long_name, 'L-4')
    Void_basetype_l_4.text = 'void'
    Void_basetype_l_4.attrib = {'L': 'EN'}
    Void_basetype_category = ET.SubElement(Void_basetype, 'CATEGORY')
    Void_basetype_category.text = 'VOID'
    Void_basetype_base_type_encoding = ET.SubElement(Void_basetype, 'BASE-TYPE-ENCODING')
    Void_basetype_base_type_encoding.text = 'VOID'
    Void_basetypenative_declaration = ET.SubElement(Void_basetype, 'NATIVE-DECLARATION')
    Void_basetypenative_declaration.text = 'void'

    # Save the XML tree to an ARXML file
    tree = ET.ElementTree(root)
    # tree.write('output.arxml', encoding='utf-8', xml_declaration=True)
    try:
        root1 = tree.getroot()

        # Remove namespaces
        root2 = remove_namespaces(root1)

        # Add indentation
        indent(root2)

        # Write the XML declaration with double quotes
        with open("output6.arxml", "wb") as f:
            f.write(b'<?xml version="1.0" encoding="utf-8"?>\n')
            tree.write(f, encoding="utf-8", xml_declaration=False)

        print(f"Successfully created with proper indentation and XML declaration.")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please enter a valid ARXML file path.")

if __name__ == '__main__':
    create_arxml()
