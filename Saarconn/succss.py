import xml.etree.ElementTree as ET

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
  ar_packages = ET.SubElement(root, "AR-PACKAGES")

  ar_package1 = ET.SubElement(ar_packages, "AR-PACKAGE")
  ET.SubElement(ar_package1, "SHORT-NAME").text = "AUTOSAR_GenDef"

  ar_packages_inner = ET.SubElement(ar_package1, "AR-PACKAGES")
  ar_package2 = ET.SubElement(ar_packages_inner, "AR-PACKAGE")
  ET.SubElement(ar_package2, "SHORT-NAME").text = "BaseTypes"
  ET.SubElement(ar_package2, "CATEGORY").text = "STANDARD"

  elements = ET.SubElement(ar_package2, "ELEMENTS")
  sw_base_type = ET.SubElement(elements, "SW-BASE-TYPE")
  ET.SubElement(sw_base_type, "SHORT-NAME").text = "void"

  long_name = ET.SubElement(sw_base_type, "LONG-NAME")
  l4 = ET.SubElement(long_name, "L-4", attrib={"L": "EN"})
  l4.text = "void"

  ET.SubElement(sw_base_type, "CATEGORY").text = "VOID"
  ET.SubElement(sw_base_type, "BASE-TYPE-ENCODING").text = "VOID"
  ET.SubElement(sw_base_type, "NATIVE-DECLARATION").text = "void"

  indent(root)

  # Save the XML tree to an ARXML file
  tree = ET.ElementTree(root)
  tree.write('output.arxml', encoding='utf-8', xml_declaration=True) 

if __name__ == "__main__":
  create_arxml()