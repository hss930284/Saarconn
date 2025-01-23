

# Usage
root = ET.Element('ROOT')
arxml_structure = ARXMLStructure()
arxml_structure.create_default_pkg_struct(root)
print(arxml_structure.get_variable('root'))  # prints the value of 'root'
print(arxml_structure.get_variable('autosar_folder'))  # prints the value of 'autosar_folder'