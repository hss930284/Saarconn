import xml.etree.ElementTree as ET

class ARXMLStructure:
    def __init__(self):
        self.variables = {}

    def create_default_pkg_struct(self, root):
        """
        Creates an ARXML file with the specified structure.
        """
        self.variables['root'] = root

        self.root_folders = ET.SubElement(root, 'AR-PACKAGES')
        self.variables['root_folders'] = self.root_folders

        self.autosar_folder = ET.SubElement(self.root_folders, 'AR-PACKAGE')
        self.autosar_folder.attrib = {'UUID': '5983c226-f5b2-4ba1-958d-32fe5f2fde51'}
        self.variables['autosar_folder'] = self.autosar_folder

        self.autosar_folder_short_name = ET.SubElement(self.autosar_folder, 'SHORT-NAME')
        self.autosar_folder_short_name.text = 'AUTOSAR'
        self.variables['autosar_folder_short_name'] = self.autosar_folder_short_name

        self.autosar_subfolders = ET.SubElement(self.autosar_folder, 'AR-PACKAGES')
        self.variables['autosar_subfolders'] = self.autosar_subfolders

        self.AUTOSAR_GenDef_folder = ET.SubElement(self.autosar_subfolders, 'AR-PACKAGE')
        self.variables['AUTOSAR_GenDef_folder'] = self.AUTOSAR_GenDef_folder

        self.AUTOSAR_GenDef_folder_short_name = ET.SubElement(self.AUTOSAR_GenDef_folder, 'SHORT-NAME')
        self.AUTOSAR_GenDef_folder_short_name.text = 'AUTOSAR_GenDef'
        self.variables['AUTOSAR_GenDef_folder_short_name'] = self.AUTOSAR_GenDef_folder_short_name


        

    def get_variable(self, name):
        return self.variables.get(name)

