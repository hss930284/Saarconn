import xml.etree.ElementTree as ET
global_elements = {}

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



# Create the root element
root = ET.Element('AUTOSAR', attrib={
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns': "http://autosar.org/schema/r4.0",
    'xsi:schemaLocation': "http://autosar.org/schema/r4.0 AUTOSAR_4-1-1.xsd"
})

global_elements = {
    'root': root
}


def ApplicationDataTypes():
    global global_elements
    global_elements['ar-packages'] = ET.SubElement(global_elements['root'], 'ar-packages')
    global_elements['ar-package'] = ET.SubElement(global_elements['ar-packages'], 'ar-package')
    global_elements['short-name'] = ET.SubElement(global_elements['ar-package'], 'short-name')
    global_elements['short-name'].text = 'SharedElements'
    global_elements['ar-packages2'] = ET.SubElement(global_elements['ar-package'], 'ar-packages')
    global_elements['ar-package2'] = ET.SubElement(global_elements['ar-packages2'], 'ar-package')
    global_elements['short-name2'] = ET.SubElement(global_elements['ar-package2'], 'short-name')
    global_elements['short-name2'].text = 'ApplicationDataTypes'
    global_elements['ar-packages3'] = ET.SubElement(global_elements['ar-package2'], 'ar-packages')
    global_elements['ar-package3'] = ET.SubElement(global_elements['ar-packages3'], 'ar-package')
    global_elements['ar-package3'].attrib = {'UUID': '035a8ab9-015a-426c-8766-e4b58e5c5a98'}
    global_elements['short-name3'] = ET.SubElement(global_elements['ar-package3'], 'short-name')
    global_elements['short-name3'].text = 'Array'
    global_elements['elements'] = ET.SubElement(global_elements['ar-package3'], 'elements')

def ApplicationArrayDataType_Fixed():
    global_elements['application-array-data-type'] = ET.SubElement(global_elements['elements'], 'application-array-data-type')
    global_elements['application-array-data-type'].attrib = {'UUID': '99540e2c-05ec-4a85-94bb-9a3999ac57fe'}
    global_elements['short-name4'] = ET.SubElement(global_elements['application-array-data-type'], 'short-name')
    global_elements['short-name4'].text = 'ApplicationArrayDataType_Fixed'
    global_elements['category'] = ET.SubElement(global_elements['application-array-data-type'], 'category')
    global_elements['category'].text = 'ARRAY'
    global_elements['element'] = ET.SubElement(global_elements['application-array-data-type'], 'element')
    global_elements['element'].attrib = {'UUID': '7391c5fe-50b6-4b88-bc63-ec1975221a4f'}
    global_elements['short-name5'] = ET.SubElement(global_elements['element'], 'short-name')
    global_elements['short-name5'].text = 'Element'
    global_elements['category2'] = ET.SubElement(global_elements['element'], 'category')
    global_elements['category2'].text = 'VALUE'
    global_elements['type-tref'] = ET.SubElement(global_elements['element'], 'type-tref')
    global_elements['type-tref'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['array-size-semantics'] = ET.SubElement(global_elements['element'], 'array-size-semantics')
    global_elements['array-size-semantics'].text = 'FIXED-SIZE'
    global_elements['max-number-of-elements'] = ET.SubElement(global_elements['element'], 'max-number-of-elements')
    global_elements['max-number-of-elements'].text = '15'

def ApplicationArrayDataType_Variable():
    application_array_data_type2 = ET.SubElement(elements1, 'APPLICATION-ARRAY-DATA-TYPE')
    application_array_data_type2.attrib = {'UUID': 'd5f3c7e9-dd94-4d37-888e-b6e44b01cc5a'}
    short_name6 = ET.SubElement(application_array_data_type2, 'SHORT-NAME')
    short_name6.text = 'ApplicationArrayDataType_Variable'
    category3 = ET.SubElement(application_array_data_type2, 'CATEGORY')
    category3.text = 'ARRAY'
    dynamic_array_size_profile1 = ET.SubElement(application_array_data_type2, 'DYNAMIC-ARRAY-SIZE-PROFILE')
    dynamic_array_size_profile1.text = 'VSA_LINEAR'
    element2 = ET.SubElement(application_array_data_type2, 'ELEMENT')
    element2.attrib = {'UUID': 'fef3f4b8-d9bd-4cb1-94b8-4403e665c4fa'}
    short_name7 = ET.SubElement(element2, 'SHORT-NAME')
    short_name7.text = 'Element'
    category4 = ET.SubElement(element2, 'CATEGORY')
    category4.text = 'VALUE'
    type_tref2 = ET.SubElement(element2, 'TYPE-TREF')
    type_tref2.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref2.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    array_size_handling1 = ET.SubElement(element2, 'ARRAY-SIZE-HANDLING')
    array_size_handling1.text = 'ALL-INDICES-SAME-ARRAY-SIZE'
    array_size_semantics2 = ET.SubElement(element2, 'ARRAY-SIZE-SEMANTICS')
    array_size_semantics2.text = 'VARIABLE-SIZE'
    max_number_of_elements2 = ET.SubElement(element2, 'MAX-NUMBER-OF-ELEMENTS')
    max_number_of_elements2.text = '15'  

def ApplicationPrimitiveDataType():
    global global_elements
    global_elements['ar-package4'] = ET.SubElement(global_elements['ar-packages3'], 'ar-package')
    global_elements['ar-package4'].attrib = {'UUID': 'b142aaa0-2671-41cd-bbc6-78cc30cf22c4'}
    global_elements['short-name8'] = ET.SubElement(global_elements['ar-package4'], 'short-name')
    global_elements['short-name8'].text = 'Primitive'
    global_elements['elements2'] = ET.SubElement(global_elements['ar-package4'], 'elements')
    global_elements['application-primitive-data-type'] = ET.SubElement(global_elements['elements2'], 'application-primitive-data-type')
    global_elements['application-primitive-data-type'].attrib = {'UUID': '18357165-e774-4282-90db-fcb76c7c6727'}
    global_elements['short-name9'] = ET.SubElement(global_elements['application-primitive-data-type'], 'short-name')
    global_elements['short-name9'].text = 'ApplicationPrimitiveDataType'
    global_elements['category5'] = ET.SubElement(global_elements['application-primitive-data-type'], 'category')
    global_elements['category5'].text = 'VALUE'
    global_elements['sw-data-def-props'] = ET.SubElement(global_elements['application-primitive-data-type'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants'] = ET.SubElement(global_elements['sw-data-def-props'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional'] = ET.SubElement(global_elements['sw-data-def-props-variants'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access'] = ET.SubElement(global_elements['sw-data-def-props-conditional'], 'sw-calibration-access')
    global_elements['sw-calibration-access'].text = 'NOT-ACCESSIBLE'
    global_elements['compu-method-ref'] = ET.SubElement(global_elements['sw-data-def-props-conditional'], 'compu-method-ref')
    global_elements['compu-method-ref'].text = '/SharedElements/CompuMethods/CompuMethod'
    global_elements['compu-method-ref'].attrib = {'DEST': 'COMPU-METHOD'}
    global_elements['data-constr-ref'] = ET.SubElement(global_elements['sw-data-def-props-conditional'], 'data-constr-ref')
    global_elements['data-constr-ref'].text = '/SharedElements/DataConstr/DataConstr'
    global_elements['data-constr-ref'].attrib = {'DEST': 'DATA-CONSTR'}
    global_elements['invalid-value'] = ET.SubElement(global_elements['sw-data-def-props-conditional'], 'invalid-value')
    global_elements['application-value-specification'] = ET.SubElement(global_elements['invalid-value'], 'application-value-specification')
    global_elements['category6'] = ET.SubElement(global_elements['application-value-specification'], 'category')
    global_elements['category6'].text = 'VALUE'
    global_elements['sw-value-cont'] = ET.SubElement(global_elements['application-value-specification'], 'sw-value-cont')
    global_elements['sw-values-phys'] = ET.SubElement(global_elements['sw-value-cont'], 'sw-values-phys')
    global_elements['v'] = ET.SubElement(global_elements['sw-values-phys'], 'v')
    global_elements['v'].text = '8'
    global_elements['unit-ref'] = ET.SubElement(global_elements['sw-data-def-props-conditional'], 'unit-ref')
    global_elements['unit-ref'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref'].attrib = {'DEST': 'UNIT'}



def Bool_ApplicationPrimitiveDataType():
    global global_elements
    global_elements['application-primitive-data-type2'] = ET.SubElement(global_elements['elements2'], 'application-primitive-data-type')
    global_elements['application-primitive-data-type2'].attrib = {'UUID': '14c56edb-9cf8-48cc-92d7-4cc1ca683a0f'}
    global_elements['short-name10'] = ET.SubElement(global_elements['application-primitive-data-type2'], 'short-name')
    global_elements['short-name10'].text = 'Bool_ApplicationPrimitiveDataType'
    global_elements['category7'] = ET.SubElement(global_elements['application-primitive-data-type2'], 'category')
    global_elements['category7'].text = 'BOOLEAN'
    global_elements['sw-data-def-props2'] = ET.SubElement(global_elements['application-primitive-data-type2'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants2'] = ET.SubElement(global_elements['sw-data-def-props2'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional2'] = ET.SubElement(global_elements['sw-data-def-props-variants2'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access2'] = ET.SubElement(global_elements['sw-data-def-props-conditional2'], 'sw-calibration-access')
    global_elements['sw-calibration-access2'].text = 'NOT-ACCESSIBLE'
    global_elements['compu-method-ref2'] = ET.SubElement(global_elements['sw-data-def-props-conditional2'], 'compu-method-ref')
    global_elements['compu-method-ref2'].text = '/SharedElements/CompuMethods/CompuMethod'
    global_elements['compu-method-ref2'].attrib = {'DEST': 'COMPU-METHOD'}
    global_elements['data-constr-ref2'] = ET.SubElement(global_elements['sw-data-def-props-conditional2'], 'data-constr-ref')
    global_elements['data-constr-ref2'].text = '/SharedElements/DataConstr/DataConstr'
    global_elements['data-constr-ref2'].attrib = {'DEST': 'DATA-CONSTR'}
    global_elements['unit-ref2'] = ET.SubElement(global_elements['sw-data-def-props-conditional2'], 'unit-ref')
    global_elements['unit-ref2'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref2'].attrib = {'DEST': 'UNIT'}

def Copy_ApplicationPrimitiveDataType():
    global global_elements
    global_elements['application-primitive-data-type3'] = ET.SubElement(global_elements['elements2'], 'application-primitive-data-type')
    global_elements['application-primitive-data-type3'].attrib = {'UUID': 'a799e394-8020-4e26-abaf-804ce312d6c0'}
    global_elements['short-name11'] = ET.SubElement(global_elements['application-primitive-data-type3'], 'short-name')
    global_elements['short-name11'].text = 'Copy_ApplicationPrimitiveDataType'
    global_elements['category8'] = ET.SubElement(global_elements['application-primitive-data-type3'], 'category')
    global_elements['category8'].text = 'VALUE'
    global_elements['sw-data-def-props3'] = ET.SubElement(global_elements['application-primitive-data-type3'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants3'] = ET.SubElement(global_elements['sw-data-def-props3'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional3'] = ET.SubElement(global_elements['sw-data-def-props-variants3'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access3'] = ET.SubElement(global_elements['sw-data-def-props-conditional3'], 'sw-calibration-access')
    global_elements['sw-calibration-access3'].text = 'NOT-ACCESSIBLE'
    global_elements['compu-method-ref3'] = ET.SubElement(global_elements['sw-data-def-props-conditional3'], 'compu-method-ref')
    global_elements['compu-method-ref3'].text = '/SharedElements/CompuMethods/CompuMethod'
    global_elements['compu-method-ref3'].attrib = {'DEST': 'COMPU-METHOD'}
    global_elements['data-constr-ref3'] = ET.SubElement(global_elements['sw-data-def-props-conditional3'], 'data-constr-ref')
    global_elements['data-constr-ref3'].text = '/SharedElements/DataConstr/DataConstr'
    global_elements['data-constr-ref3'].attrib = {'DEST': 'DATA-CONSTR'}
    global_elements['unit-ref3'] = ET.SubElement(global_elements['sw-data-def-props-conditional3'], 'unit-ref')
    global_elements['unit-ref3'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref3'].attrib = {'DEST': 'UNIT'}


def String_ApplicationPrimitiveDataType():
    global global_elements
    global_elements['application-primitive-data-type4'] = ET.SubElement(global_elements['elements2'], 'application-primitive-data-type')
    global_elements['application-primitive-data-type4'].attrib = {'UUID': 'decc899e-e751-4907-998b-8769b6445a38'}
    global_elements['short-name12'] = ET.SubElement(global_elements['application-primitive-data-type4'], 'short-name')
    global_elements['short-name12'].text = 'String_ApplicationPrimitiveDataType'
    global_elements['category9'] = ET.SubElement(global_elements['application-primitive-data-type4'], 'category')
    global_elements['category9'].text = 'STRING'
    global_elements['sw-data-def-props4'] = ET.SubElement(global_elements['application-primitive-data-type4'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants4'] = ET.SubElement(global_elements['sw-data-def-props4'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional4'] = ET.SubElement(global_elements['sw-data-def-props-variants4'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access4'] = ET.SubElement(global_elements['sw-data-def-props-conditional4'], 'sw-calibration-access')
    global_elements['sw-calibration-access4'].text = 'NOT-ACCESSIBLE'
    global_elements['sw-text-props'] = ET.SubElement(global_elements['sw-data-def-props-conditional4'], 'sw-text-props')
    global_elements['array-size-semantics3'] = ET.SubElement(global_elements['sw-text-props'], 'array-size-semantics')
    global_elements['array-size-semantics3'].text = 'VARIABLE-SIZE'
    global_elements['sw-max-text-size'] = ET.SubElement(global_elements['sw-text-props'], 'sw-max-text-size')
    global_elements['sw-max-text-size'].text = '16'
    global_elements['unit-ref4'] = ET.SubElement(global_elements['sw-data-def-props-conditional4'], 'unit-ref')
    global_elements['unit-ref4'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref4'].attrib = {'DEST': 'UNIT'}

def ApplicationRecordDataType():
    global global_elements
    global_elements['ar-package5'] = ET.SubElement(global_elements['ar-packages3'], 'ar-package')
    global_elements['ar-package5'].attrib = {'UUID': '65217d8d-3662-4a20-a643-ec9ee94de7a0'}
    global_elements['short-name13'] = ET.SubElement(global_elements['ar-package5'], 'short-name')
    global_elements['short-name13'].text = 'Record'
    global_elements['elements3'] = ET.SubElement(global_elements['ar-package5'], 'elements')
    global_elements['application-record-data-type'] = ET.SubElement(global_elements['elements3'], 'application-record-data-type')
    global_elements['application-record-data-type'].attrib = {'UUID': 'd20b1ec6-9940-43c7-beda-f773a805fab6'}
    global_elements['short-name14'] = ET.SubElement(global_elements['application-record-data-type'], 'short-name')
    global_elements['short-name14'].text = 'ApplicationRecordDataType'
    global_elements['category10'] = ET.SubElement(global_elements['application-record-data-type'], 'category')
    global_elements['category10'].text = 'STRUCTURE'
    global_elements['elements4'] = ET.SubElement(global_elements['application-record-data-type'], 'elements')
    global_elements['application-record-element'] = ET.SubElement(global_elements['elements4'], 'application-record-element')
    global_elements['application-record-element'].attrib = {'UUID': 'bd5079b0-6ac0-4d72-a63a-afd373f2bcc5'}
    global_elements['short-name15'] = ET.SubElement(global_elements['application-record-element'], 'short-name')
    global_elements['short-name15'].text = 'Element'
    global_elements['type-tref3'] = ET.SubElement(global_elements['application-record-element'], 'type-tref')
    global_elements['type-tref3'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref3'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['application-record-element2'] = ET.SubElement(global_elements['elements4'], 'application-record-element')
    global_elements['application-record-element2'].attrib = {'UUID': '12021f0e-9ad1-4df2-bffa-197611387a0a'}
    global_elements['short-name16'] = ET.SubElement(global_elements['application-record-element2'], 'short-name')
    global_elements['short-name16'].text = 'Element1'
    global_elements['type-tref4'] = ET.SubElement(global_elements['application-record-element2'], 'type-tref')
    global_elements['type-tref4'].text = '/SharedElements/ApplicationDataTypes/Array/ApplicationArrayDataType_Fixed'
    global_elements['type-tref4'].attrib = {'DEST': 'APPLICATION-ARRAY-DATA-TYPE'}

def CompuMethods():
    global_elements['ar-package6'] = ET.SubElement(global_elements['ar-packages2'], 'ar-package')
    global_elements['short-name17'] = ET.SubElement(global_elements['ar-package6'], 'short-name')
    global_elements['short-name17'].text = 'CompuMethods'
    global_elements['elements5'] = ET.SubElement(global_elements['ar-package6'], 'elements')

def BITFIELD_TEXTTABLE_CompuMethod():
    global_elements['compu-method'] = ET.SubElement(global_elements['elements5'], 'compu-method')
    global_elements['compu-method'].attrib = {'UUID': 'e51fd87b-fe38-48d5-b94a-c11851da3006'}
    global_elements['short-name18'] = ET.SubElement(global_elements['compu-method'], 'short-name')
    global_elements['short-name18'].text = 'BITFIELD_TEXTTABLE_CompuMethod'
    global_elements['category11'] = ET.SubElement(global_elements['compu-method'], 'category')
    global_elements['category11'].text = 'BITFIELD_TEXTTABLE'
    global_elements['unit-ref5'] = ET.SubElement(global_elements['compu-method'], 'unit-ref')
    global_elements['unit-ref5'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref5'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys'] = ET.SubElement(global_elements['compu-method'], 'compu-internal-to-phys')
    global_elements['compu-scales'] = ET.SubElement(global_elements['compu-internal-to-phys'], 'compu-scales')
    global_elements['compu-scale'] = ET.SubElement(global_elements['compu-scales'], 'compu-scale')
    global_elements['mask'] = ET.SubElement(global_elements['compu-scale'], 'mask')
    global_elements['mask'].text = '0'
    global_elements['lower-limit'] = ET.SubElement(global_elements['compu-scale'], 'lower-limit')
    global_elements['lower-limit'].text = '0'
    global_elements['upper-limit'] = ET.SubElement(global_elements['compu-scale'], 'upper-limit')
    global_elements['upper-limit'].text = '0'
    global_elements['compu-const'] = ET.SubElement(global_elements['compu-scale'], 'compu-const')
    global_elements['vt'] = ET.SubElement(global_elements['compu-const'], 'vt')
    global_elements['vt'].text = 'xyz'
    global_elements['compu-scale2'] = ET.SubElement(global_elements['compu-scales'], 'compu-scale')
    global_elements['mask2'] = ET.SubElement(global_elements['compu-scale2'], 'mask')
    global_elements['mask2'].text = '0'
    global_elements['lower-limit2'] = ET.SubElement(global_elements['compu-scale2'], 'lower-limit')
    global_elements['lower-limit2'].text = '1'
    global_elements['upper-limit2'] = ET.SubElement(global_elements['compu-scale2'], 'upper-limit')
    global_elements['upper-limit2'].text = '1'
    global_elements['compu-const2'] = ET.SubElement(global_elements['compu-scale2'], 'compu-const')
    global_elements['vt2'] = ET.SubElement(global_elements['compu-const2'], 'vt')
    global_elements['vt2'].text = 'xyz1'
    global_elements['compu-scale3'] = ET.SubElement(global_elements['compu-scales'], 'compu-scale')
    global_elements['mask3'] = ET.SubElement(global_elements['compu-scale3'], 'mask')
    global_elements['mask3'].text = '0'
    global_elements['lower-limit3'] = ET.SubElement(global_elements['compu-scale3'], 'lower-limit')
    global_elements['lower-limit3'].text = '2'
    global_elements['upper-limit3'] = ET.SubElement(global_elements['compu-scale3'], 'upper-limit')
    global_elements['upper-limit3'].text = '2'
    global_elements['compu-const3'] = ET.SubElement(global_elements['compu-scale3'], 'compu-const')
    global_elements['vt3'] = ET.SubElement(global_elements['compu-const3'], 'vt')
    global_elements['vt3'].text = 'xyz2'
    global_elements['compu-scale4'] = ET.SubElement(global_elements['compu-scales'], 'compu-scale')
    global_elements['mask4'] = ET.SubElement(global_elements['compu-scale4'], 'mask')
    global_elements['mask4'].text = '0'
    global_elements['lower-limit4'] = ET.SubElement(global_elements['compu-scale4'], 'lower-limit')
    global_elements['lower-limit4'].text = '3'
    global_elements['upper-limit4'] = ET.SubElement(global_elements['compu-scale4'], 'upper-limit')
    global_elements['upper-limit4'].text = '3'
    global_elements['compu-const4'] = ET.SubElement(global_elements['compu-scale4'], 'compu-const')
    global_elements['vt4'] = ET.SubElement(global_elements['compu-const4'], 'vt')
    global_elements['vt4'].text = 'xyz3'
    global_elements['compu-scale5'] = ET.SubElement(global_elements['compu-scales'], 'compu-scale')
    global_elements['mask5'] = ET.SubElement(global_elements['compu-scale5'], 'mask')
    global_elements['mask5'].text = '0'
    global_elements['lower-limit5'] = ET.SubElement(global_elements['compu-scale5'], 'lower-limit')
    global_elements['lower-limit5'].text = '4'
    global_elements['upper-limit5'] = ET.SubElement(global_elements['compu-scale5'], 'upper-limit')
    global_elements['upper-limit5'].text = '4'
    global_elements['compu-const5'] = ET.SubElement(global_elements['compu-scale5'], 'compu-const')
    global_elements['vt5'] = ET.SubElement(global_elements['compu-const5'], 'vt')
    global_elements['vt5'].text = 'xyz4'

def CompuMethod():
    global_elements['compu-method2'] = ET.SubElement(global_elements['elements5'], 'compu-method')
    global_elements['compu-method2'].attrib = {'UUID': 'a65ae6b6-3eab-43ff-907b-2c8276c8528b'}
    global_elements['short-name19'] = ET.SubElement(global_elements['compu-method2'], 'short-name')
    global_elements['short-name19'].text = 'CompuMethod'
    global_elements['category12'] = ET.SubElement(global_elements['compu-method2'], 'category')
    global_elements['category12'].text = 'IDENTICAL'
    global_elements['unit-ref6'] = ET.SubElement(global_elements['compu-method2'], 'unit-ref')
    global_elements['unit-ref6'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref6'].attrib = {'DEST': 'UNIT'}

def LINEAR_CompuMethod():
    global_elements['compu-method3'] = ET.SubElement(global_elements['elements5'], 'compu-method')
    global_elements['compu-method3'].attrib = {'UUID': '386978fd-a90f-4003-b63e-f9e35b6d76b8'}
    global_elements['short-name20'] = ET.SubElement(global_elements['compu-method3'], 'short-name')
    global_elements['short-name20'].text = 'LINEAR_CompuMethod'
    global_elements['category13'] = ET.SubElement(global_elements['compu-method3'], 'category')
    global_elements['category13'].text = 'LINEAR'
    global_elements['unit-ref7'] = ET.SubElement(global_elements['compu-method3'], 'unit-ref')
    global_elements['unit-ref7'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref7'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys2'] = ET.SubElement(global_elements['compu-method3'], 'compu-internal-to-phys')
    global_elements['compu-scales2'] = ET.SubElement(global_elements['compu-internal-to-phys2'], 'compu-scales')
    global_elements['compu-scale6'] = ET.SubElement(global_elements['compu-scales2'], 'compu-scale')
    global_elements['compu-rational-coeffs'] = ET.SubElement(global_elements['compu-scale6'], 'compu-rational-coeffs')
    global_elements['compu-numerator'] = ET.SubElement(global_elements['compu-rational-coeffs'], 'compu-numerator')
    global_elements['v2'] = ET.SubElement(global_elements['compu-numerator'], 'v')
    global_elements['v2'].text = '0'
    global_elements['v3'] = ET.SubElement(global_elements['compu-numerator'], 'v')
    global_elements['v3'].text = '1'
    global_elements['compu-denominator'] = ET.SubElement(global_elements['compu-rational-coeffs'], 'compu-denominator')
    global_elements['v4'] = ET.SubElement(global_elements['compu-denominator'], 'v')
    global_elements['v4'].text = '1'
    

def RAT_FUNC_CompuMethod():
    global_elements['compu-method4'] = ET.SubElement(global_elements['elements5'], 'compu-method')
    global_elements['compu-method4'].attrib = {'UUID': '74ea35c5-6b05-40a2-b22c-3c1a179a095b'}
    global_elements['short-name21'] = ET.SubElement(global_elements['compu-method4'], 'short-name')
    global_elements['short-name21'].text = 'RAT_FUNC_CompuMethod'
    global_elements['category14'] = ET.SubElement(global_elements['compu-method4'], 'category')
    global_elements['category14'].text = 'RAT_FUNC'
    global_elements['unit-ref8'] = ET.SubElement(global_elements['compu-method4'], 'unit-ref')
    global_elements['unit-ref8'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref8'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys3'] = ET.SubElement(global_elements['compu-method4'], 'compu-internal-to-phys')
    global_elements['compu-scales3'] = ET.SubElement(global_elements['compu-internal-to-phys3'], 'compu-scales')
    global_elements['compu-scale7'] = ET.SubElement(global_elements['compu-scales3'], 'compu-scale')
    global_elements['compu-rational-coeffs2'] = ET.SubElement(global_elements['compu-scale7'], 'compu-rational-coeffs')
    global_elements['compu-numerator2'] = ET.SubElement(global_elements['compu-rational-coeffs2'], 'compu-numerator')
    global_elements['v5'] = ET.SubElement(global_elements['compu-numerator2'], 'v')
    global_elements['v5'].text = '0'
    global_elements['v6'] = ET.SubElement(global_elements['compu-numerator2'], 'v')
    global_elements['v6'].text = '1'
    global_elements['v7'] = ET.SubElement(global_elements['compu-numerator2'], 'v')
    global_elements['v7'].text = '0'
    global_elements['compu-denominator2'] = ET.SubElement(global_elements['compu-rational-coeffs2'], 'compu-denominator')
    global_elements['v8'] = ET.SubElement(global_elements['compu-denominator2'], 'v')
    global_elements['v8'].text = '1'
    global_elements['v9'] = ET.SubElement(global_elements['compu-denominator2'], 'v')
    global_elements['v9'].text = '0'
    global_elements['v10'] = ET.SubElement(global_elements['compu-denominator2'], 'v')
    global_elements['v10'].text = '0'


def SCALE_RATIONAL_AND_TEXTTABLE_CompuMethod():
    global_elements['compu-method5'] = ET.SubElement(global_elements['elements5'], 'compu-method')
    global_elements['compu-method5'].attrib = {'UUID': 'cb57246c-cf48-448f-b8a5-5f319b76ee49'}
    global_elements['short-name22'] = ET.SubElement(global_elements['compu-method5'], 'short-name')
    global_elements['short-name22'].text = 'SCALE_RATIONAL_AND_TEXTTABLE_CompuMethod'
    global_elements['desc'] = ET.SubElement(global_elements['compu-method5'], 'desc')
    global_elements['l-2'] = ET.SubElement(global_elements['desc'], 'l-2')
    global_elements['l-2'].text = 'S'
    global_elements['l-2'].attrib = {'L': 'FOR-ALL'}
    global_elements['category15'] = ET.SubElement(global_elements['compu-method5'], 'category')
    global_elements['category15'].text = 'SCALE_RATIONAL_AND_TEXTTABLE'
    global_elements['unit-ref9'] = ET.SubElement(global_elements['compu-method5'], 'unit-ref')
    global_elements['unit-ref9'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref9'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys4'] = ET.SubElement(global_elements['compu-method5'], 'compu-internal-to-phys')
    global_elements['compu-scales4'] = ET.SubElement(global_elements['compu-internal-to-phys4'], 'compu-scales')
    global_elements['compu-scale8'] = ET.SubElement(global_elements['compu-scales4'], 'compu-scale')
    global_elements['lower-limit6'] = ET.SubElement(global_elements['compu-scale8'], 'lower-limit')
    global_elements['lower-limit6'].text = '0'
    global_elements['upper-limit6'] = ET.SubElement(global_elements['compu-scale8'], 'upper-limit')
    global_elements['upper-limit6'].text = '15'
    global_elements['compu-rational-coeffs3'] = ET.SubElement(global_elements['compu-scale8'], 'compu-rational-coeffs')
    global_elements['compu-numerator3'] = ET.SubElement(global_elements['compu-rational-coeffs3'], 'compu-numerator')
    global_elements['v11'] = ET.SubElement(global_elements['compu-numerator3'], 'v')
    global_elements['v11'].text = '0'
    global_elements['v12'] = ET.SubElement(global_elements['compu-numerator3'], 'v')
    global_elements['v12'].text = '1'
    global_elements['v13'] = ET.SubElement(global_elements['compu-numerator3'], 'v')
    global_elements['v13'].text = '0'
    global_elements['compu-denominator3'] = ET.SubElement(global_elements['compu-rational-coeffs3'], 'compu-denominator')
    global_elements['v14'] = ET.SubElement(global_elements['compu-denominator3'], 'v')
    global_elements['v14'].text = '1'
    global_elements['v15'] = ET.SubElement(global_elements['compu-denominator3'], 'v')
    global_elements['v15'].text = '0'
    global_elements['v16'] = ET.SubElement(global_elements['compu-denominator3'], 'v')
    global_elements['v16'].text = '0'
    global_elements['compu-scale9'] = ET.SubElement(global_elements['compu-scales4'], 'compu-scale')
    global_elements['symbol'] = ET.SubElement(global_elements['compu-scale9'], 'symbol')
    global_elements['symbol'].text = 'sdcd'
    global_elements['lower-limit7'] = ET.SubElement(global_elements['compu-scale9'], 'lower-limit')
    global_elements['lower-limit7'].text = '16'
    global_elements['upper-limit7'] = ET.SubElement(global_elements['compu-scale9'], 'upper-limit')
    global_elements['upper-limit7'].text = '16'
    global_elements['compu-const6'] = ET.SubElement(global_elements['compu-scale9'], 'compu-const')
    global_elements['vt6'] = ET.SubElement(global_elements['compu-const6'], 'vt')
    global_elements['vt6'].text = 'sdcd'
    global_elements['compu-scale10'] = ET.SubElement(global_elements['compu-scales4'], 'compu-scale')
    global_elements['symbol2'] = ET.SubElement(global_elements['compu-scale10'], 'symbol')
    global_elements['symbol2'].text = 'sdcd1'
    global_elements['lower-limit8'] = ET.SubElement(global_elements['compu-scale10'], 'lower-limit')
    global_elements['lower-limit8'].text = '17'
    global_elements['upper-limit8'] = ET.SubElement(global_elements['compu-scale10'], 'upper-limit')
    global_elements['upper-limit8'].text = '17'
    global_elements['compu-const7'] = ET.SubElement(global_elements['compu-scale10'], 'compu-const')
    global_elements['vt7'] = ET.SubElement(global_elements['compu-const7'], 'vt')
    global_elements['vt7'].text = 'sdcd1'
    global_elements['compu-default-value'] = ET.SubElement(global_elements['compu-internal-to-phys4'], 'compu-default-value')
    global_elements['v17'] = ET.SubElement(global_elements['compu-default-value'], 'v')
    global_elements['v17'].text = '17'

def Scale_linear_And_texttable_CompuMethod():
    global_elements['compu-method6'] = ET.SubElement(global_elements['elements5'], 'compu-method')
    global_elements['compu-method6'].attrib = {'UUID': '19ee54ef-4447-4987-bcbe-a9d2a743d569'}
    global_elements['short-name23'] = ET.SubElement(global_elements['compu-method6'], 'short-name')
    global_elements['short-name23'].text = 'Scale_linear_And_texttable_CompuMethod'
    global_elements['desc2'] = ET.SubElement(global_elements['compu-method6'], 'desc')
    global_elements['l-22'] = ET.SubElement(global_elements['desc2'], 'l-2')
    global_elements['l-22'].text = 'Scale_linear _And_texttable_CompuMethod'
    global_elements['l-22'].attrib = {'L': 'FOR-ALL'}
    global_elements['category16'] = ET.SubElement(global_elements['compu-method6'], 'category')
    global_elements['category16'].text = 'SCALE_LINEAR_AND_TEXTTABLE'
    global_elements['unit-ref10'] = ET.SubElement(global_elements['compu-method6'], 'unit-ref')
    global_elements['unit-ref10'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref10'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys5'] = ET.SubElement(global_elements['compu-method6'], 'compu-internal-to-phys')
    global_elements['compu-scales5'] = ET.SubElement(global_elements['compu-internal-to-phys5'], 'compu-scales')
    global_elements['compu-scale11'] = ET.SubElement(global_elements['compu-scales5'], 'compu-scale')
    global_elements['lower-limit9'] = ET.SubElement(global_elements['compu-scale11'], 'lower-limit')
    global_elements['lower-limit9'].text = '0'
    global_elements['upper-limit9'] = ET.SubElement(global_elements['compu-scale11'], 'upper-limit')
    global_elements['upper-limit9'].text = '7'
    global_elements['compu-rational-coeffs4'] = ET.SubElement(global_elements['compu-scale11'], 'compu-rational-coeffs')
    global_elements['compu-numerator4'] = ET.SubElement(global_elements['compu-rational-coeffs4'], 'compu-numerator')
    global_elements['v18'] = ET.SubElement(global_elements['compu-numerator4'], 'v')
    global_elements['v18'].text = '0'
    global_elements['v19'] = ET.SubElement(global_elements['compu-numerator4'], 'v')
    global_elements['v19'].text = '1'
    global_elements['compu-denominator4'] = ET.SubElement(global_elements['compu-rational-coeffs4'], 'compu-denominator')
    global_elements['v20'] = ET.SubElement(global_elements['compu-denominator4'], 'v')
    global_elements['v20'].text = '1'
    global_elements['compu-scale12'] = ET.SubElement(global_elements['compu-scales5'], 'compu-scale')
    global_elements['symbol3'] = ET.SubElement(global_elements['compu-scale12'], 'symbol')
    global_elements['symbol3'].text = 'abcd'
    global_elements['lower-limit10'] = ET.SubElement(global_elements['compu-scale12'], 'lower-limit')
    global_elements['lower-limit10'].text = '8'
    global_elements['upper-limit10'] = ET.SubElement(global_elements['compu-scale12'], 'upper-limit')
    global_elements['upper-limit10'].text = '8'
    global_elements['compu-const8'] = ET.SubElement(global_elements['compu-scale12'], 'compu-const')
    global_elements['vt8'] = ET.SubElement(global_elements['compu-const8'], 'vt')
    global_elements['vt8'].text = 'abcd'
    global_elements['compu-scale13'] = ET.SubElement(global_elements['compu-scales5'], 'compu-scale')
    global_elements['symbol4'] = ET.SubElement(global_elements['compu-scale13'], 'symbol')
    global_elements['symbol4'].text = 'abcd1'
    global_elements['lower-limit11'] = ET.SubElement(global_elements['compu-scale13'], 'lower-limit')
    global_elements['lower-limit11'].text = '9'
    global_elements['upper-limit11'] = ET.SubElement(global_elements['compu-scale13'], 'upper-limit')
    global_elements['upper-limit11'].text = '9'
    global_elements['compu-const9'] = ET.SubElement(global_elements['compu-scale13'], 'compu-const')
    global_elements['vt9'] = ET.SubElement(global_elements['compu-const9'], 'vt')
    global_elements['vt9'].text = 'abcd1'
    global_elements['compu-default-value2'] = ET.SubElement(global_elements['compu-internal-to-phys5'], 'compu-default-value')
    global_elements['v21'] = ET.SubElement(global_elements['compu-default-value2'], 'v')
    global_elements['v21'].text = '8'


def TAB_NOINTP_CompuMethod():
    global_elements['compu-method7'] = ET.SubElement(global_elements['elements5'], 'compu-method')
    global_elements['compu-method7'].attrib = {'UUID': 'd4a62613-2238-4523-b274-2677c5a2235a'}
    global_elements['short-name24'] = ET.SubElement(global_elements['compu-method7'], 'short-name')
    global_elements['short-name24'].text = 'TAB_NOINTP_CompuMethod'
    global_elements['desc3'] = ET.SubElement(global_elements['compu-method7'], 'desc')
    global_elements['category17'] = ET.SubElement(global_elements['compu-method7'], 'category')
    global_elements['category17'].text = 'TAB_NOINTP'
    global_elements['unit-ref11'] = ET.SubElement(global_elements['compu-method7'], 'unit-ref')
    global_elements['unit-ref11'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref11'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys6'] = ET.SubElement(global_elements['compu-method7'], 'compu-internal-to-phys')
    global_elements['compu-scales6'] = ET.SubElement(global_elements['compu-internal-to-phys6'], 'compu-scales')
    global_elements['compu-scale14'] = ET.SubElement(global_elements['compu-scales6'], 'compu-scale')
    global_elements['desc4'] = ET.SubElement(global_elements['compu-scale14'], 'desc')
    global_elements['l-23'] = ET.SubElement(global_elements['desc4'], 'l-2')
    global_elements['l-23'].attrib = {'L': 'AA'}
    global_elements['lower-limit12'] = ET.SubElement(global_elements['compu-scale14'], 'lower-limit')
    global_elements['lower-limit12'].text = '0'
    global_elements['upper-limit12'] = ET.SubElement(global_elements['compu-scale14'], 'upper-limit')
    global_elements['upper-limit12'].text = '0'
    global_elements['compu-const10'] = ET.SubElement(global_elements['compu-scale14'], 'compu-const')
    global_elements['v22'] = ET.SubElement(global_elements['compu-const10'], 'v')
    global_elements['v22'].text = '10'
    global_elements['compu-scale15'] = ET.SubElement(global_elements['compu-scales6'], 'compu-scale')
    global_elements['lower-limit13'] = ET.SubElement(global_elements['compu-scale15'], 'lower-limit')
    global_elements['lower-limit13'].text = '1'
    global_elements['upper-limit13'] = ET.SubElement(global_elements['compu-scale15'], 'upper-limit')
    global_elements['upper-limit13'].text = '1'
    global_elements['compu-const11'] = ET.SubElement(global_elements['compu-scale15'], 'compu-const')
    global_elements['v23'] = ET.SubElement(global_elements['compu-const11'], 'v')
    global_elements['v23'].text = '9'
    global_elements['compu-scale16'] = ET.SubElement(global_elements['compu-scales6'], 'compu-scale')
    global_elements['lower-limit14'] = ET.SubElement(global_elements['compu-scale16'], 'lower-limit')
    global_elements['lower-limit14'].text = '2'
    global_elements['upper-limit14'] = ET.SubElement(global_elements['compu-scale16'], 'upper-limit')
    global_elements['upper-limit14'].text = '2'
    global_elements['compu-const12'] = ET.SubElement(global_elements['compu-scale16'], 'compu-const')
    global_elements['v24'] = ET.SubElement(global_elements['compu-const12'], 'v')
    global_elements['v24'].text = '8'
    global_elements['compu-default-value3'] = ET.SubElement(global_elements['compu-internal-to-phys6'], 'compu-default-value')
    global_elements['vf'] = ET.SubElement(global_elements['compu-default-value3'], 'vf')
    global_elements['vf'].text = '0'

def TEXTTABLE_CompuMethod():
    global_elements['compu-method8'] = ET.SubElement(global_elements['elements5'], 'compu-method')
    global_elements['compu-method8'].attrib = {'UUID': '6ef51214-688c-4e48-a115-d80fcf62bffc'}
    global_elements['short-name25'] = ET.SubElement(global_elements['compu-method8'], 'short-name')
    global_elements['short-name25'].text = 'TEXTTABLE_CompuMethod'
    global_elements['category18'] = ET.SubElement(global_elements['compu-method8'], 'category')
    global_elements['category18'].text = 'TEXTTABLE'
    global_elements['unit-ref12'] = ET.SubElement(global_elements['compu-method8'], 'unit-ref')
    global_elements['unit-ref12'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref12'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys7'] = ET.SubElement(global_elements['compu-method8'], 'compu-internal-to-phys')
    global_elements['compu-scales7'] = ET.SubElement(global_elements['compu-internal-to-phys7'], 'compu-scales')
    global_elements['compu-scale17'] = ET.SubElement(global_elements['compu-scales7'], 'compu-scale')
    global_elements['symbol5'] = ET.SubElement(global_elements['compu-scale17'], 'symbol')
    global_elements['symbol5'].text = 'text1'
    global_elements['lower-limit15'] = ET.SubElement(global_elements['compu-scale17'], 'lower-limit')
    global_elements['lower-limit15'].text = '0'
    global_elements['upper-limit15'] = ET.SubElement(global_elements['compu-scale17'], 'upper-limit')
    global_elements['upper-limit15'].text = '0'
    global_elements['compu-const13'] = ET.SubElement(global_elements['compu-scale17'], 'compu-const')
    global_elements['vt10'] = ET.SubElement(global_elements['compu-const13'], 'vt')
    global_elements['vt10'].text = 'text1'
    global_elements['compu-scale18'] = ET.SubElement(global_elements['compu-scales7'], 'compu-scale')
    global_elements['symbol6'] = ET.SubElement(global_elements['compu-scale18'], 'symbol')
    global_elements['symbol6'].text = 'text2'
    global_elements['lower-limit16'] = ET.SubElement(global_elements['compu-scale18'], 'lower-limit')
    global_elements['lower-limit16'].text = '1'
    global_elements['upper-limit16'] = ET.SubElement(global_elements['compu-scale18'], 'upper-limit')
    global_elements['upper-limit16'].text = '1'
    global_elements['compu-const14'] = ET.SubElement(global_elements['compu-scale18'], 'compu-const')
    global_elements['vt11'] = ET.SubElement(global_elements['compu-const14'], 'vt')
    global_elements['vt11'].text = 'text2'
    global_elements['compu-scale19'] = ET.SubElement(global_elements['compu-scales7'], 'compu-scale')
    global_elements['symbol7'] = ET.SubElement(global_elements['compu-scale19'], 'symbol')
    global_elements['symbol7'].text = 'text3'
    global_elements['lower-limit17'] = ET.SubElement(global_elements['compu-scale19'], 'lower-limit')
    global_elements['lower-limit17'].text = '2'
    global_elements['upper-limit17'] = ET.SubElement(global_elements['compu-scale19'], 'upper-limit')
    global_elements['upper-limit17'].text = '2'
    global_elements['compu-const15'] = ET.SubElement(global_elements['compu-scale19'], 'compu-const')
    global_elements['vt12'] = ET.SubElement(global_elements['compu-const15'], 'vt')
    global_elements['vt12'].text = 'text3'
    global_elements['compu-scale20'] = ET.SubElement(global_elements['compu-scales7'], 'compu-scale')
    global_elements['symbol8'] = ET.SubElement(global_elements['compu-scale20'], 'symbol')
    global_elements['symbol8'].text = 'text4'
    global_elements['lower-limit18'] = ET.SubElement(global_elements['compu-scale20'], 'lower-limit')
    global_elements['lower-limit18'].text = '3'
    global_elements['upper-limit18'] = ET.SubElement(global_elements['compu-scale20'], 'upper-limit')
    global_elements['upper-limit18'].text = '3'
    global_elements['compu-const16'] = ET.SubElement(global_elements['compu-scale20'], 'compu-const')
    global_elements['vt13'] = ET.SubElement(global_elements['compu-const16'], 'vt')
    global_elements['vt13'].text = 'text4'
    global_elements['compu-default-value4'] = ET.SubElement(global_elements['compu-internal-to-phys7'], 'compu-default-value')
    global_elements['v25'] = ET.SubElement(global_elements['compu-default-value4'], 'v')
    global_elements['v25'].text = '0'

def ApplicationSwComponentType_ExplicitInterRunnableVariable():
    # global_elements['ar-package7'] = ET.SubElement(global_elements['ar-packages2'], 'ar-package')
    # global_elements['short-name26'] = ET.SubElement(global_elements['ar-package7'], 'short-name')
    # global_elements['short-name26'].text = 'ConstantSpecifications'
    # global_elements['elements6'] = ET.SubElement(global_elements['ar-package7'], 'elements')
    global_elements['constant-specification'] = ET.SubElement(global_elements['elements6'], 'constant-specification')
    global_elements['constant-specification'].attrib = {'UUID': '5679b253-a22a-4532-8116-7ce8ac35a562'}
    global_elements['short-name27'] = ET.SubElement(global_elements['constant-specification'], 'short-name')
    global_elements['short-name27'].text = 'ApplicationSwComponentType_ExplicitInterRunnableVariable'
    global_elements['value-spec'] = ET.SubElement(global_elements['constant-specification'], 'value-spec')
    global_elements['numerical-value-specification'] = ET.SubElement(global_elements['value-spec'], 'numerical-value-specification')
    global_elements['short-label'] = ET.SubElement(global_elements['numerical-value-specification'], 'short-label')
    global_elements['short-label'].text = 'Value'
    global_elements['value'] = ET.SubElement(global_elements['numerical-value-specification'], 'value')
    global_elements['value'].text = '0'


def ApplicationSwComponentType_SharedParameter():
    global_elements['constant-specification2'] = ET.SubElement(global_elements['elements6'], 'constant-specification')
    global_elements['constant-specification2'].attrib = {'UUID': '82a61fa2-2547-4ce8-a0d4-c583629db923'}
    global_elements['short-name28'] = ET.SubElement(global_elements['constant-specification2'], 'short-name')
    global_elements['short-name28'].text = 'ApplicationSwComponentType_SharedParameter'
    global_elements['value-spec2'] = ET.SubElement(global_elements['constant-specification2'], 'value-spec')
    global_elements['numerical-value-specification2'] = ET.SubElement(global_elements['value-spec2'], 'numerical-value-specification')
    global_elements['short-label2'] = ET.SubElement(global_elements['numerical-value-specification2'], 'short-label')
    global_elements['short-label2'].text = 'Value'
    global_elements['value2'] = ET.SubElement(global_elements['numerical-value-specification2'], 'value')
    global_elements['value2'].text = '5.5'


def ApplicationSwComponentType_StaticMemory():
    global_elements['constant-specification3'] = ET.SubElement(global_elements['elements6'], 'constant-specification')
    global_elements['constant-specification3'].attrib = {'UUID': 'e3a2b67f-9cda-465d-8b6f-f31127e7b3a1'}
    global_elements['short-name29'] = ET.SubElement(global_elements['constant-specification3'], 'short-name')
    global_elements['short-name29'].text = 'ApplicationSwComponentType_StaticMemory'
    global_elements['value-spec3'] = ET.SubElement(global_elements['constant-specification3'], 'value-spec')
    global_elements['numerical-value-specification3'] = ET.SubElement(global_elements['value-spec3'], 'numerical-value-specification')
    global_elements['short-label3'] = ET.SubElement(global_elements['numerical-value-specification3'], 'short-label')
    global_elements['short-label3'].text = 'Value'
    global_elements['value3'] = ET.SubElement(global_elements['numerical-value-specification3'], 'value')
    global_elements['value3'].text = '9'


def ConstantSpecification():
    global_elements['constant-specification4'] = ET.SubElement(global_elements['elements6'], 'constant-specification')
    global_elements['constant-specification4'].attrib = {'UUID': '3c303401-cc30-49f7-a7cb-0cf2844a3f18'}
    global_elements['short-name30'] = ET.SubElement(global_elements['constant-specification4'], 'short-name')
    global_elements['short-name30'].text = 'ConstantSpecification'


def ConstantSpecificationMappingSet():
    # global_elements['ar-package8'] = ET.SubElement(global_elements['ar-packages2'], 'ar-package')
    # global_elements['ar-package8'].attrib = {'UUID': '6fcb326d-7f82-4cd3-9429-fa90f212d1e8'}
    # global_elements['short-name31'] = ET.SubElement(global_elements['ar-package8'], 'short-name')
    # global_elements['short-name31'].text = 'ConstantTypeMappingSets'
    # global_elements['elements7'] = ET.SubElement(global_elements['ar-package8'], 'elements')
    global_elements['constant-specification-mapping-set'] = ET.SubElement(global_elements['elements7'], 'constant-specification-mapping-set')
    global_elements['constant-specification-mapping-set'].attrib = {'UUID': '4f3bdbd1-af02-46e6-a3ba-411118807380'}
    global_elements['short-name32'] = ET.SubElement(global_elements['constant-specification-mapping-set'], 'short-name')
    global_elements['short-name32'].text = 'ConstantSpecificationMappingSet'

def DataConstr():
    # global_elements['ar-package9'] = ET.SubElement(global_elements['ar-packages2'], 'ar-package')
    # global_elements['ar-package9'].attrib = {'UUID': '5b7c99d1-d4ef-481b-95e4-0d6975de4f3b'}
    # global_elements['short-name33'] = ET.SubElement(global_elements['ar-package9'], 'short-name')
    # global_elements['short-name33'].text = 'DataConstr'
    # global_elements['elements8'] = ET.SubElement(global_elements['ar-package9'], 'elements')
    global_elements['data-constr'] = ET.SubElement(global_elements['elements8'], 'data-constr')
    global_elements['data-constr'].attrib = {'UUID': '78b9384e-7f45-4396-b617-a03a03aaf3ce'}
    global_elements['short-name34'] = ET.SubElement(global_elements['data-constr'], 'short-name')
    global_elements['short-name34'].text = 'DataConstr'
    global_elements['data-constr-rules'] = ET.SubElement(global_elements['data-constr'], 'data-constr-rules')
    global_elements['data-constr-rule'] = ET.SubElement(global_elements['data-constr-rules'], 'data-constr-rule')
    global_elements['constr-level'] = ET.SubElement(global_elements['data-constr-rule'], 'constr-level')
    global_elements['constr-level'].text = '0'
    global_elements['phys-constrs'] = ET.SubElement(global_elements['data-constr-rule'], 'phys-constrs')
    global_elements['lower-limit19'] = ET.SubElement(global_elements['phys-constrs'], 'lower-limit')
    global_elements['lower-limit19'].text = '0'
    global_elements['upper-limit19'] = ET.SubElement(global_elements['phys-constrs'], 'upper-limit')
    global_elements['upper-limit19'].text = '7'

def DataTypemappingSets():
    # global_elements['ar-package10'] = ET.SubElement(global_elements['ar-packages2'], 'ar-package')
    # global_elements['ar-package10'].attrib = {'UUID': '463cbb86-4f8e-463e-8bb3-dafc528ccbdf'}
    # global_elements['short-name35'] = ET.SubElement(global_elements['ar-package10'], 'short-name')
    # global_elements['short-name35'].text = 'DataTypemappingSets'
    # global_elements['elements9'] = ET.SubElement(global_elements['ar-package10'], 'elements')
    global_elements['data-type-mapping-set'] = ET.SubElement(global_elements['elements9'], 'data-type-mapping-set')
    global_elements['data-type-mapping-set'].attrib = {'UUID': '84bab728-8c47-495c-a5d4-5290c3551358'}
    global_elements['short-name36'] = ET.SubElement(global_elements['data-type-mapping-set'], 'short-name')
    global_elements['short-name36'].text = 'DataTypeMappingSet'
    global_elements['data-type-maps'] = ET.SubElement(global_elements['data-type-mapping-set'], 'data-type-maps')
    global_elements['data-type-map'] = ET.SubElement(global_elements['data-type-maps'], 'data-type-map')
    global_elements['application-data-type-ref'] = ET.SubElement(global_elements['data-type-map'], 'application-data-type-ref')
    global_elements['application-data-type-ref'].text = '/SharedElements/ApplicationDataTypes/Array/ApplicationArrayDataType_Fixed'
    global_elements['application-data-type-ref'].attrib = {'DEST': 'APPLICATION-ARRAY-DATA-TYPE'}
    global_elements['implementation-data-type-ref'] = ET.SubElement(global_elements['data-type-map'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref'].text = '/SharedElements/ImplementationDataTypes/ARRAY_ImplementationDataType'
    global_elements['implementation-data-type-ref'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['data-type-map2'] = ET.SubElement(global_elements['data-type-maps'], 'data-type-map')
    global_elements['application-data-type-ref2'] = ET.SubElement(global_elements['data-type-map2'], 'application-data-type-ref')
    global_elements['application-data-type-ref2'].text = '/SharedElements/ApplicationDataTypes/Record/ApplicationRecordDataType'
    global_elements['application-data-type-ref2'].attrib = {'DEST': 'APPLICATION-RECORD-DATA-TYPE'}
    global_elements['implementation-data-type-ref2'] = ET.SubElement(global_elements['data-type-map2'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref2'].text = '/SharedElements/ImplementationDataTypes/STRUCTURE_ImplementationDataType1'
    global_elements['implementation-data-type-ref2'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['data-type-map3'] = ET.SubElement(global_elements['data-type-maps'], 'data-type-map')
    global_elements['application-data-type-ref3'] = ET.SubElement(global_elements['data-type-map3'], 'application-data-type-ref')
    global_elements['application-data-type-ref3'].text = '/SharedElements/ApplicationDataTypes/Array/ApplicationArrayDataType_Variable'
    global_elements['application-data-type-ref3'].attrib = {'DEST': 'APPLICATION-ARRAY-DATA-TYPE'}
    global_elements['implementation-data-type-ref3'] = ET.SubElement(global_elements['data-type-map3'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref3'].text = '/SharedElements/ImplementationDataTypes/Struct_Array_ImplementationDataType'
    global_elements['implementation-data-type-ref3'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['data-type-map4'] = ET.SubElement(global_elements['data-type-maps'], 'data-type-map')
    global_elements['application-data-type-ref4'] = ET.SubElement(global_elements['data-type-map4'], 'application-data-type-ref')
    global_elements['application-data-type-ref4'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['application-data-type-ref4'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['implementation-data-type-ref4'] = ET.SubElement(global_elements['data-type-map4'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref4'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    global_elements['implementation-data-type-ref4'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def ImplementationDataTypes():
    # global_elements['ar-package11'] = ET.SubElement(global_elements['ar-packages2'], 'ar-package')
    # global_elements['short-name37'] = ET.SubElement(global_elements['ar-package11'], 'short-name')
    # global_elements['short-name37'].text = 'ImplementationDataTypes'
    # global_elements['elements10'] = ET.SubElement(global_elements['ar-package11'], 'elements')
    global_elements['implementation-data-type'] = ET.SubElement(global_elements['elements10'], 'implementation-data-type')
    global_elements['implementation-data-type'].attrib = {'UUID': '21f9a013-317d-4a6a-8c1d-cdc72f7df8f5'}
    global_elements['short-name38'] = ET.SubElement(global_elements['implementation-data-type'], 'short-name')
    global_elements['short-name38'].text = 'ARRAY_ImplementationDataType'
    global_elements['category19'] = ET.SubElement(global_elements['implementation-data-type'], 'category')
    global_elements['category19'].text = 'ARRAY'
    global_elements['sw-data-def-props5'] = ET.SubElement(global_elements['implementation-data-type'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants5'] = ET.SubElement(global_elements['sw-data-def-props5'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional5'] = ET.SubElement(global_elements['sw-data-def-props-variants5'], 'sw-data-def-props-conditional')
    global_elements['sub-elements'] = ET.SubElement(global_elements['implementation-data-type'], 'sub-elements')
    global_elements['implementation-data-type-element'] = ET.SubElement(global_elements['sub-elements'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element'].attrib = {'UUID': '5512b8b7-a43f-436f-bb18-47a903ad1e17'}
    global_elements['short-name39'] = ET.SubElement(global_elements['implementation-data-type-element'], 'short-name')
    global_elements['short-name39'].text = 'SubElement'
    global_elements['category20'] = ET.SubElement(global_elements['implementation-data-type-element'], 'category')
    global_elements['category20'].text = 'TYPE_REFERENCE'
    global_elements['array-size'] = ET.SubElement(global_elements['implementation-data-type-element'], 'array-size')
    global_elements['array-size'].text = '15'
    global_elements['array-size-semantics4'] = ET.SubElement(global_elements['implementation-data-type-element'], 'array-size-semantics')
    global_elements['array-size-semantics4'].text = 'FIXED-SIZE'
    global_elements['sw-data-def-props6'] = ET.SubElement(global_elements['implementation-data-type-element'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants6'] = ET.SubElement(global_elements['sw-data-def-props6'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional6'] = ET.SubElement(global_elements['sw-data-def-props-variants6'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref5'] = ET.SubElement(global_elements['sw-data-def-props-conditional6'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref5'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    global_elements['implementation-data-type-ref5'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def ARRAY_ImplementationDataType1():
    global_elements['implementation-data-type2'] = ET.SubElement(global_elements['elements10'], 'implementation-data-type')
    global_elements['implementation-data-type2'].attrib = {'UUID': 'f01098ff-1c78-439e-9476-11d641870637'}
    global_elements['short-name40'] = ET.SubElement(global_elements['implementation-data-type2'], 'short-name')
    global_elements['short-name40'].text = 'ARRAY_ImplementationDataType1'
    global_elements['category21'] = ET.SubElement(global_elements['implementation-data-type2'], 'category')
    global_elements['category21'].text = 'ARRAY'
    global_elements['sub-elements2'] = ET.SubElement(global_elements['implementation-data-type2'], 'sub-elements')
    global_elements['implementation-data-type-element2'] = ET.SubElement(global_elements['sub-elements2'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element2'].attrib = {'UUID': 'ee36cc86-25eb-4048-8698-d1ec326fda32'}
    global_elements['short-name41'] = ET.SubElement(global_elements['implementation-data-type-element2'], 'short-name')
    global_elements['short-name41'].text = 'SubElement'
    global_elements['category22'] = ET.SubElement(global_elements['implementation-data-type-element2'], 'category')
    global_elements['category22'].text = 'TYPE_REFERENCE'
    global_elements['array-size2'] = ET.SubElement(global_elements['implementation-data-type-element2'], 'array-size')
    global_elements['array-size2'].text = '15'
    global_elements['array-size-semantics5'] = ET.SubElement(global_elements['implementation-data-type-element2'], 'array-size-semantics')
    global_elements['array-size-semantics5'].text = 'VARIABLE-SIZE'
    global_elements['sw-data-def-props7'] = ET.SubElement(global_elements['implementation-data-type-element2'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants7'] = ET.SubElement(global_elements['sw-data-def-props7'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional7'] = ET.SubElement(global_elements['sw-data-def-props-variants7'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref6'] = ET.SubElement(global_elements['sw-data-def-props-conditional7'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref6'].text = '/SharedElements/ImplementationDataTypes/STRUCTURE_ImplementationDataType1'
    global_elements['implementation-data-type-ref6'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def ImplementationDataType():
    global_elements['implementation-data-type3'] = ET.SubElement(global_elements['elements10'], 'implementation-data-type')
    global_elements['implementation-data-type3'].attrib = {'UUID': '77ef0bea-be4b-4dea-b5ea-114e5a3f3d26'}
    global_elements['short-name42'] = ET.SubElement(global_elements['implementation-data-type3'], 'short-name')
    global_elements['short-name42'].text = 'ImplementationDataType'
    global_elements['category23'] = ET.SubElement(global_elements['implementation-data-type3'], 'category')
    global_elements['category23'].text = 'VALUE'
    global_elements['sw-data-def-props8'] = ET.SubElement(global_elements['implementation-data-type3'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants8'] = ET.SubElement(global_elements['sw-data-def-props8'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional8'] = ET.SubElement(global_elements['sw-data-def-props-variants8'], 'sw-data-def-props-conditional')
    global_elements['base-type-ref'] = ET.SubElement(global_elements['sw-data-def-props-conditional8'], 'base-type-ref')
    global_elements['base-type-ref'].text = '/AUTOSAR/AUTOSAR_Platform/BaseTypes/uint8'
    global_elements['base-type-ref'].attrib = {'DEST': 'SW-BASE-TYPE'}

def STRUCTURE_ImplementationDataType1():
    global_elements['implementation-data-type4'] = ET.SubElement(global_elements['elements10'], 'implementation-data-type')
    global_elements['implementation-data-type4'].attrib = {'UUID': '53ec3bfc-5a92-4d42-b31b-8e29e99a2b46'}
    global_elements['short-name43'] = ET.SubElement(global_elements['implementation-data-type4'], 'short-name')
    global_elements['short-name43'].text = 'STRUCTURE_ImplementationDataType1'
    global_elements['category24'] = ET.SubElement(global_elements['implementation-data-type4'], 'category')
    global_elements['category24'].text = 'STRUCTURE'
    global_elements['sub-elements3'] = ET.SubElement(global_elements['implementation-data-type4'], 'sub-elements')

def STRUCTURE_ImplementationDataType1_SubElement():
    global_elements['implementation-data-type-element3'] = ET.SubElement(global_elements['sub-elements3'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element3'].attrib = {'UUID': '31f01782-3ce8-4dbe-81d1-0d5fb89bef99'}
    global_elements['short-name44'] = ET.SubElement(global_elements['implementation-data-type-element3'], 'short-name')
    global_elements['short-name44'].text = 'SubElement'
    global_elements['category25'] = ET.SubElement(global_elements['implementation-data-type-element3'], 'category')
    global_elements['category25'].text = 'TYPE_REFERENCE'
    global_elements['sw-data-def-props9'] = ET.SubElement(global_elements['implementation-data-type-element3'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants9'] = ET.SubElement(global_elements['sw-data-def-props9'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional9'] = ET.SubElement(global_elements['sw-data-def-props-variants9'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref7'] = ET.SubElement(global_elements['sw-data-def-props-conditional9'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref7'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    global_elements['implementation-data-type-ref7'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def STRUCTURE_ImplementationDataType1_SubElement1():
    global_elements['implementation-data-type-element4'] = ET.SubElement(global_elements['sub-elements3'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element4'].attrib = {'UUID': '83bd06cb-a4ff-4d55-bd3d-1a691b582d46'}
    global_elements['short-name45'] = ET.SubElement(global_elements['implementation-data-type-element4'], 'short-name')
    global_elements['short-name45'].text = 'SubElement1'
    global_elements['category26'] = ET.SubElement(global_elements['implementation-data-type-element4'], 'category')
    global_elements['category26'].text = 'TYPE_REFERENCE'
    global_elements['sw-data-def-props10'] = ET.SubElement(global_elements['implementation-data-type-element4'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants10'] = ET.SubElement(global_elements['sw-data-def-props10'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional10'] = ET.SubElement(global_elements['sw-data-def-props-variants10'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref8'] = ET.SubElement(global_elements['sw-data-def-props-conditional10'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref8'].text = '/SharedElements/ImplementationDataTypes/ARRAY_ImplementationDataType'
    global_elements['implementation-data-type-ref8'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Struct_Array_ImplementationDataType():
    global_elements['implementation-data-type5'] = ET.SubElement(global_elements['elements10'], 'implementation-data-type')
    global_elements['implementation-data-type5'].attrib = {'UUID': 'ccd15817-26a8-424d-8c87-3f3d70b5ee9d'}
    global_elements['short-name46'] = ET.SubElement(global_elements['implementation-data-type5'], 'short-name')
    global_elements['short-name46'].text = 'Struct_Array_ImplementationDataType'
    global_elements['category27'] = ET.SubElement(global_elements['implementation-data-type5'], 'category')
    global_elements['category27'].text = 'STRUCTURE'
    dynamic_array_size_profile2 = ET.SubElement(implementation_data_type5, 'DYNAMIC-ARRAY-SIZE-PROFILE')
    dynamic_array_size_profile2.text = 'VSA_LINEAR'     
    global_elements['sub-elements4'] = ET.SubElement(global_elements['implementation-data-type5'], 'sub-elements')

def Struct_Array_ImplementationDataType_SubElement1():
    global_elements['implementation-data-type-element5'] = ET.SubElement(global_elements['sub-elements4'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element5'].attrib = {'UUID': '3f61bc0d-d829-4ab0-9e22-7de6a25972e3'}
    global_elements['short-name47'] = ET.SubElement(global_elements['implementation-data-type-element5'], 'short-name')
    global_elements['short-name47'].text = 'SubElement1'
    global_elements['category28'] = ET.SubElement(global_elements['implementation-data-type-element5'], 'category')
    global_elements['category28'].text = 'TYPE_REFERENCE'
    global_elements['sw-data-def-props11'] = ET.SubElement(global_elements['implementation-data-type-element5'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants11'] = ET.SubElement(global_elements['sw-data-def-props11'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional11'] = ET.SubElement(global_elements['sw-data-def-props-variants11'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref9'] = ET.SubElement(global_elements['sw-data-def-props-conditional11'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref9'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['implementation-data-type-ref9'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Struct_Array_ImplementationDataType_SubElement():
    global_elements['implementation-data-type-element6'] = ET.SubElement(global_elements['sub-elements4'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element6'].attrib = {'UUID': 'dc530c9c-3b65-4707-99c3-842e2d2b7788'}
    global_elements['short-name48'] = ET.SubElement(global_elements['implementation-data-type-element6'], 'short-name')
    global_elements['short-name48'].text = 'SubElement'
    global_elements['category29'] = ET.SubElement(global_elements['implementation-data-type-element6'], 'category')
    global_elements['category29'].text = 'ARRAY'
    global_elements['sub-elements5'] = ET.SubElement(global_elements['implementation-data-type-element6'], 'sub-elements')

def Struct_Array_ImplementationDataType_SubElement_TYPE_REFERENCE():
    global_elements['implementation-data-type-element7'] = ET.SubElement(global_elements['sub-elements5'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element7'].attrib = {'UUID': 'af21d788-9aea-4789-b7d0-8665f2d0c8c7'}
    global_elements['short-name49'] = ET.SubElement(global_elements['implementation-data-type-element7'], 'short-name')
    global_elements['short-name49'].text = 'SubElement'
    global_elements['category30'] = ET.SubElement(global_elements['implementation-data-type-element7'], 'category')
    global_elements['category30'].text = 'TYPE_REFERENCE'
    global_elements['array-size3'] = ET.SubElement(global_elements['implementation-data-type-element7'], 'array-size')
    global_elements['array-size3'].text = '15'
    array_size_handling2 = ET.SubElement(implementation_data_type_element7, 'ARRAY-SIZE-HANDLING')
    array_size_handling2.text = 'ALL-INDICES-SAME-ARRAY-SIZE'
    global_elements['array-size-semantics6'] = ET.SubElement(global_elements['implementation-data-type-element7'], 'array-size-semantics')
    global_elements['array-size-semantics6'].text = 'VARIABLE-SIZE'
    global_elements['sw-data-def-props12'] = ET.SubElement(global_elements['implementation-data-type-element7'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants12'] = ET.SubElement(global_elements['sw-data-def-props12'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional12'] = ET.SubElement(global_elements['sw-data-def-props-variants12'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref10'] = ET.SubElement(global_elements['sw-data-def-props-conditional12'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref10'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    global_elements['implementation-data-type-ref10'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['sw-data-def-props13'] = ET.SubElement(global_elements['implementation-data-type-element6'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants13'] = ET.SubElement(global_elements['sw-data-def-props13'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional13'] = ET.SubElement(global_elements['sw-data-def-props-variants13'], 'sw-data-def-props-conditional')

def TypeTref_ImplementationDataType():
    global_elements['implementation-data-type6'] = ET.SubElement(global_elements['elements10'], 'implementation-data-type')
    global_elements['implementation-data-type6'].attrib = {'UUID': '79fa9e8f-a805-43da-b4b5-ac42d2a23ff0'}
    global_elements['short-name50'] = ET.SubElement(global_elements['implementation-data-type6'], 'short-name')
    global_elements['short-name50'].text = 'TypeTref_ImplementationDataType'
    global_elements['category31'] = ET.SubElement(global_elements['implementation-data-type6'], 'category')
    global_elements['category31'].text = 'TYPE_REFERENCE'
    global_elements['sw-data-def-props14'] = ET.SubElement(global_elements['implementation-data-type6'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants14'] = ET.SubElement(global_elements['sw-data-def-props14'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional14'] = ET.SubElement(global_elements['sw-data-def-props-variants14'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref11'] = ET.SubElement(global_elements['sw-data-def-props-conditional14'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref11'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float32'
    global_elements['implementation-data-type-ref11'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

# def PortInterfaces():
#     global_elements['ar-package12'] = ET.SubElement(global_elements['ar-packages2'], 'ar-package')
#     global_elements['short-name51'] = ET.SubElement(global_elements['ar-package12'], 'short-name')
#     global_elements['short-name51'].text = 'PortInterfaces'
#     global_elements['ar-packages4'] = ET.SubElement(global_elements['ar-package12'], 'ar-packages')
#     global_elements['ar-package13'] = ET.SubElement(global_elements['ar-packages4'], 'ar-package')

# def ClientServer():
#     global_elements['ar-package13'].attrib = {'UUID': 'a0d0a13a-15e8-47a3-8169-5f11ad6c7d3f'}
#     global_elements['short-name52'] = ET.SubElement(global_elements['ar-package13'], 'short-name')#     global_elements['short-name52'].text = 'ClientServer'
#     global_elements['elements11'] = ET.SubElement(global_elements['ar-package13'], 'elements')

def ClientServerInterface():  
    global_elements['client-server-interface'] = ET.SubElement(global_elements['elements11'], 'client-server-interface')
    global_elements['client-server-interface'].attrib = {'UUID': 'de068aa3-6af8-4bad-a17f-893dbfa6d08d'}
    global_elements['short-name53'] = ET.SubElement(global_elements['client-server-interface'], 'short-name')
    global_elements['short-name53'].text = 'ClientServerInterface'
    global_elements['is-service'] = ET.SubElement(global_elements['client-server-interface'], 'is-service')
    global_elements['is-service'].text = 'false'

def ClientServerInterface_ClientServereOperation():
    global_elements['operations'] = ET.SubElement(global_elements['client-server-interface'], 'operations')
    global_elements['client-server-operation'] = ET.SubElement(global_elements['operations'], 'client-server-operation')
    global_elements['client-server-operation'].attrib = {'UUID': 'f963f5c2-07f7-439d-be71-e8ffb77736cb'}
    global_elements['short-name54'] = ET.SubElement(global_elements['client-server-operation'], 'short-name')
    global_elements['short-name54'].text = 'Operation'
    global_elements['arguments'] = ET.SubElement(global_elements['client-server-operation'], 'arguments')
    global_elements['argument-data-prototype'] = ET.SubElement(global_elements['arguments'], 'argument-data-prototype')
    global_elements['argument-data-prototype'].attrib = {'UUID': '0757643f-ef26-4951-9974-c0ad09b5c8d0'}
    global_elements['short-name55'] = ET.SubElement(global_elements['argument-data-prototype'], 'short-name')
    global_elements['short-name55'].text = 'Argument'
    global_elements['sw-data-def-props15'] = ET.SubElement(global_elements['argument-data-prototype'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants15'] = ET.SubElement(global_elements['sw-data-def-props15'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional15'] = ET.SubElement(global_elements['sw-data-def-props-variants15'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy'] = ET.SubElement(global_elements['sw-data-def-props-conditional15'], 'sw-impl-policy')
    global_elements['sw-impl-policy'].text = 'STANDARD'
    global_elements['type-tref5'] = ET.SubElement(global_elements['argument-data-prototype'], 'type-tref')
    global_elements['type-tref5'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref5'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['direction'] = ET.SubElement(global_elements['argument-data-prototype'], 'direction')
    global_elements['direction'].text = 'IN'
    global_elements['server-argument-impl-policy'] = ET.SubElement(global_elements['argument-data-prototype'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy'].text = 'USE-ARGUMENT-TYPE'
  
def ClientServerInterface_ClientServereOperation1():
    global_elements['client-server-operation2'] = ET.SubElement(global_elements['operations'], 'client-server-operation')
    global_elements['client-server-operation2'].attrib = {'UUID': '9d946ffc-e827-4a3b-9217-80ae67bdce09'}
    global_elements['short-name56'] = ET.SubElement(global_elements['client-server-operation2'], 'short-name')
    global_elements['short-name56'].text = 'Operation1'
    global_elements['arguments2'] = ET.SubElement(global_elements['client-server-operation2'], 'arguments')
    global_elements['argument-data-prototype2'] = ET.SubElement(global_elements['arguments2'], 'argument-data-prototype')
    global_elements['argument-data-prototype2'].attrib = {'UUID': 'fbd7c03a-e379-467c-9efb-5818113f5e64'}
    global_elements['short-name57'] = ET.SubElement(global_elements['argument-data-prototype2'], 'short-name')
    global_elements['short-name57'].text = 'Argument'
    global_elements['sw-data-def-props16'] = ET.SubElement(global_elements['argument-data-prototype2'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants16'] = ET.SubElement(global_elements['sw-data-def-props16'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional16'] = ET.SubElement(global_elements['sw-data-def-props-variants16'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy2'] = ET.SubElement(global_elements['sw-data-def-props-conditional16'], 'sw-impl-policy')
    global_elements['sw-impl-policy2'].text = 'STANDARD'
    global_elements['type-tref6'] = ET.SubElement(global_elements['argument-data-prototype2'], 'type-tref')
    global_elements['type-tref6'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref6'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['direction2'] = ET.SubElement(global_elements['argument-data-prototype2'], 'direction')
    global_elements['direction2'].text = 'OUT'
    global_elements['server-argument-impl-policy2'] = ET.SubElement(global_elements['argument-data-prototype2'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy2'].text = 'USE-ARGUMENT-TYPE'

def Copy2_ClientServerInterface():
    global_elements['client-server-interface2'] = ET.SubElement(global_elements['elements11'], 'client-server-interface')
    global_elements['client-server-interface2'].attrib = {'UUID': '68861440-758d-43f6-92a2-fed7438de313'}
    global_elements['short-name58'] = ET.SubElement(global_elements['client-server-interface2'], 'short-name')
    global_elements['short-name58'].text = 'Copy2_ClientServerInterface'
    global_elements['is-service2'] = ET.SubElement(global_elements['client-server-interface2'], 'is-service')
    global_elements['is-service2'].text = 'false'

def Copy2_ClientServerInterface_ClientServereOperation():
    global_elements['operations2'] = ET.SubElement(global_elements['client-server-interface2'], 'operations')
    global_elements['client-server-operation3'] = ET.SubElement(global_elements['operations2'], 'client-server-operation')
    global_elements['client-server-operation3'].attrib = {'UUID': 'dd8cf435-bddb-45bb-a59d-cffcdd11cedd'}
    global_elements['short-name59'] = ET.SubElement(global_elements['client-server-operation3'], 'short-name')
    global_elements['short-name59'].text = 'Operation'
    global_elements['arguments3'] = ET.SubElement(global_elements['client-server-operation3'], 'arguments')
    global_elements['argument-data-prototype3'] = ET.SubElement(global_elements['arguments3'], 'argument-data-prototype')
    global_elements['argument-data-prototype3'].attrib = {'UUID': '474b5949-0760-4780-9d06-6d2b549c40e3'}
    global_elements['short-name60'] = ET.SubElement(global_elements['argument-data-prototype3'], 'short-name')
    global_elements['short-name60'].text = 'Argument'
    global_elements['sw-data-def-props17'] = ET.SubElement(global_elements['argument-data-prototype3'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants17'] = ET.SubElement(global_elements['sw-data-def-props17'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional17'] = ET.SubElement(global_elements['sw-data-def-props-variants17'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy3'] = ET.SubElement(global_elements['sw-data-def-props-conditional17'], 'sw-impl-policy')
    global_elements['sw-impl-policy3'].text = 'STANDARD'
    global_elements['type-tref7'] = ET.SubElement(global_elements['argument-data-prototype3'], 'type-tref')
    global_elements['type-tref7'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref7'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['direction3'] = ET.SubElement(global_elements['argument-data-prototype3'], 'direction')
    global_elements['direction3'].text = 'IN'
    global_elements['server-argument-impl-policy3'] = ET.SubElement(global_elements['argument-data-prototype3'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy3'].text = 'USE-ARGUMENT-TYPE'

def Copy2_ClientServerInterface_ClientServereOperation1():
    global_elements['client-server-operation4'] = ET.SubElement(global_elements['operations2'], 'client-server-operation')
    global_elements['client-server-operation4'].attrib = {'UUID': 'ceba0008-a280-4915-acc8-c4b28afc10c4'}
    global_elements['short-name61'] = ET.SubElement(global_elements['client-server-operation4'], 'short-name')
    global_elements['short-name61'].text = 'Operation1'
    global_elements['arguments4'] = ET.SubElement(global_elements['client-server-operation4'], 'arguments')
    global_elements['argument-data-prototype4'] = ET.SubElement(global_elements['arguments4'], 'argument-data-prototype')
    global_elements['argument-data-prototype4'].attrib = {'UUID': '48e7b87f-8674-441c-bc3e-b6143e20802e'}
    global_elements['short-name62'] = ET.SubElement(global_elements['argument-data-prototype4'], 'short-name')
    global_elements['short-name62'].text = 'Argument'
    global_elements['sw-data-def-props18'] = ET.SubElement(global_elements['argument-data-prototype4'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants18'] = ET.SubElement(global_elements['sw-data-def-props18'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional18'] = ET.SubElement(global_elements['sw-data-def-props-variants18'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy4'] = ET.SubElement(global_elements['sw-data-def-props-conditional18'], 'sw-impl-policy')
    global_elements['sw-impl-policy4'].text = 'STANDARD'
    global_elements['type-tref8'] = ET.SubElement(global_elements['argument-data-prototype4'], 'type-tref')
    global_elements['type-tref8'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref8'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['direction4'] = ET.SubElement(global_elements['argument-data-prototype4'], 'direction')
    global_elements['direction4'].text = 'OUT'
    global_elements['server-argument-impl-policy4'] = ET.SubElement(global_elements['argument-data-prototype4'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy4'].text = 'USE-ARGUMENT-TYPE'

def Copy3_ClientServerInterface():
    global_elements['client-server-interface3'] = ET.SubElement(global_elements['elements11'], 'client-server-interface')
    global_elements['client-server-interface3'].attrib = {'UUID': '9b8ada7b-e7a9-49d6-a945-db726b3bd1f9'}
    global_elements['short-name63'] = ET.SubElement(global_elements['client-server-interface3'], 'short-name')
    global_elements['short-name63'].text = 'Copy3_ClientServerInterface'
    global_elements['is-service3'] = ET.SubElement(global_elements['client-server-interface3'], 'is-service')
    global_elements['is-service3'].text = 'false'

def Copy3_ClientServerInterface_ClientServereOperation():
    global_elements['operations3'] = ET.SubElement(global_elements['client-server-interface3'], 'operations')
    global_elements['client-server-operation5'] = ET.SubElement(global_elements['operations3'], 'client-server-operation')
    global_elements['client-server-operation5'].attrib = {'UUID': '8b64e196-a577-4332-a8f2-8e907214f2ac'}
    global_elements['short-name64'] = ET.SubElement(global_elements['client-server-operation5'], 'short-name')
    global_elements['short-name64'].text = 'Operation'
    global_elements['arguments5'] = ET.SubElement(global_elements['client-server-operation5'], 'arguments')
    global_elements['argument-data-prototype5'] = ET.SubElement(global_elements['arguments5'], 'argument-data-prototype')
    global_elements['argument-data-prototype5'].attrib = {'UUID': 'cf106dae-c79b-4cea-a011-2d5ff268ac3e'}
    global_elements['short-name65'] = ET.SubElement(global_elements['argument-data-prototype5'], 'short-name')
    global_elements['short-name65'].text = 'Argument'
    global_elements['sw-data-def-props19'] = ET.SubElement(global_elements['argument-data-prototype5'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants19'] = ET.SubElement(global_elements['sw-data-def-props19'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional19'] = ET.SubElement(global_elements['sw-data-def-props-variants19'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy5'] = ET.SubElement(global_elements['sw-data-def-props-conditional19'], 'sw-impl-policy')
    global_elements['sw-impl-policy5'].text = 'STANDARD'
    global_elements['type-tref9'] = ET.SubElement(global_elements['argument-data-prototype5'], 'type-tref')
    global_elements['type-tref9'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref9'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['direction5'] = ET.SubElement(global_elements['argument-data-prototype5'], 'direction')
    global_elements['direction5'].text = 'IN'
    global_elements['server-argument-impl-policy5'] = ET.SubElement(global_elements['argument-data-prototype5'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy5'].text = 'USE-ARGUMENT-TYPE'

def Copy3_ClientServerInterface_ClientServereOperation1():
    global_elements['client-server-operation6'] = ET.SubElement(global_elements['operations3'], 'client-server-operation')
    global_elements['client-server-operation6'].attrib = {'UUID': '03f0b7d8-222c-465d-9663-185446b9f092'}
    global_elements['short-name66'] = ET.SubElement(global_elements['client-server-operation6'], 'short-name')
    global_elements['short-name66'].text = 'Operation1'
    global_elements['arguments6'] = ET.SubElement(global_elements['client-server-operation6'], 'arguments')
    global_elements['argument-data-prototype6'] = ET.SubElement(global_elements['arguments6'], 'argument-data-prototype')
    global_elements['argument-data-prototype6'].attrib = {'UUID': '9fe53cee-82db-4c74-887a-137d3260eae6'}
    global_elements['short-name67'] = ET.SubElement(global_elements['argument-data-prototype6'], 'short-name')
    global_elements['short-name67'].text = 'Argument'
    global_elements['sw-data-def-props20'] = ET.SubElement(global_elements['argument-data-prototype6'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants20'] = ET.SubElement(global_elements['sw-data-def-props20'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional20'] = ET.SubElement(global_elements['sw-data-def-props-variants20'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy6'] = ET.SubElement(global_elements['sw-data-def-props-conditional20'], 'sw-impl-policy')
    global_elements['sw-impl-policy6'].text = 'STANDARD'
    global_elements['type-tref10'] = ET.SubElement(global_elements['argument-data-prototype6'], 'type-tref')
    global_elements['type-tref10'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref10'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['direction6'] = ET.SubElement(global_elements['argument-data-prototype6'], 'direction')
    global_elements['direction6'].text = 'OUT'
    global_elements['server-argument-impl-policy6'] = ET.SubElement(global_elements['argument-data-prototype6'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy6'].text = 'USE-ARGUMENT-TYPE'

def Copy4_ClientServerInterface():
    global_elements['client-server-interface4'] = ET.SubElement(global_elements['elements11'], 'client-server-interface')
    global_elements['client-server-interface4'].attrib = {'UUID': 'bc94762b-35e3-49e1-ae8b-70bc63394d9c'}
    global_elements['short-name68'] = ET.SubElement(global_elements['client-server-interface4'], 'short-name')
    global_elements['short-name68'].text = 'Copy4_ClientServerInterface'
    global_elements['is-service4'] = ET.SubElement(global_elements['client-server-interface4'], 'is-service')
    global_elements['is-service4'].text = 'false'

def Copy4_ClientServerInterface_ClientServereOperation():
    global_elements['operations4'] = ET.SubElement(global_elements['client-server-interface4'], 'operations')
    global_elements['client-server-operation7'] = ET.SubElement(global_elements['operations4'], 'client-server-operation')
    global_elements['client-server-operation7'].attrib = {'UUID': '4f953ec5-5e57-4a1c-bcf2-9eba8fde4ddd'}
    global_elements['short-name69'] = ET.SubElement(global_elements['client-server-operation7'], 'short-name')
    global_elements['short-name69'].text = 'Operation'
    global_elements['arguments7'] = ET.SubElement(global_elements['client-server-operation7'], 'arguments')
    global_elements['argument-data-prototype7'] = ET.SubElement(global_elements['arguments7'], 'argument-data-prototype')
    global_elements['argument-data-prototype7'].attrib = {'UUID': '573e55c4-304e-48a7-ae98-47c7744d4415'}
    global_elements['short-name70'] = ET.SubElement(global_elements['argument-data-prototype7'], 'short-name')
    global_elements['short-name70'].text = 'Argument'
    global_elements['sw-data-def-props21'] = ET.SubElement(global_elements['argument-data-prototype7'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants21'] = ET.SubElement(global_elements['sw-data-def-props21'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional21'] = ET.SubElement(global_elements['sw-data-def-props-variants21'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy7'] = ET.SubElement(global_elements['sw-data-def-props-conditional21'], 'sw-impl-policy')
    global_elements['sw-impl-policy7'].text = 'STANDARD'
    global_elements['type-tref11'] = ET.SubElement(global_elements['argument-data-prototype7'], 'type-tref')
    global_elements['type-tref11'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref11'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['direction7'] = ET.SubElement(global_elements['argument-data-prototype7'], 'direction')
    global_elements['direction7'].text = 'IN'
    global_elements['server-argument-impl-policy7'] = ET.SubElement(global_elements['argument-data-prototype7'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy7'].text = 'USE-ARGUMENT-TYPE'

def Copy4_ClientServerInterface_ClientServereOperation1():
    global_elements['client-server-operation8'] = ET.SubElement(global_elements['operations4'], 'client-server-operation')
    global_elements['client-server-operation8'].attrib = {'UUID': '32dd33c4-e167-4858-93d3-bc02d325d12c'}
    global_elements['short-name71'] = ET.SubElement(global_elements['client-server-operation8'], 'short-name')
    global_elements['short-name71'].text = 'Operation1'
    global_elements['arguments8'] = ET.SubElement(global_elements['client-server-operation8'], 'arguments')
    global_elements['argument-data-prototype8'] = ET.SubElement(global_elements['arguments8'], 'argument-data-prototype')
    global_elements['argument-data-prototype8'].attrib = {'UUID': '28cc5664-0a70-4275-b1a3-3cb7a40597db'}
    global_elements['short-name72'] = ET.SubElement(global_elements['argument-data-prototype8'], 'short-name')
    global_elements['short-name72'].text = 'Argument'
    global_elements['sw-data-def-props22'] = ET.SubElement(global_elements['argument-data-prototype8'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants22'] = ET.SubElement(global_elements['sw-data-def-props22'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional22'] = ET.SubElement(global_elements['sw-data-def-props-variants22'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy8'] = ET.SubElement(global_elements['sw-data-def-props-conditional22'], 'sw-impl-policy')
    global_elements['sw-impl-policy8'].text = 'STANDARD'
    global_elements['type-tref12'] = ET.SubElement(global_elements['argument-data-prototype8'], 'type-tref')
    global_elements['type-tref12'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref12'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['direction8'] = ET.SubElement(global_elements['argument-data-prototype8'], 'direction')
    global_elements['direction8'].text = 'OUT'
    global_elements['server-argument-impl-policy8'] = ET.SubElement(global_elements['argument-data-prototype8'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy8'].text = 'USE-ARGUMENT-TYPE'

def Copy_ClientServerInterface():
    global_elements['client-server-interface5'] = ET.SubElement(global_elements['elements11'], 'client-server-interface')
    global_elements['client-server-interface5'].attrib = {'UUID': 'ad797ff8-41de-49b7-a6c3-c2dd864f60dd'}
    global_elements['short-name73'] = ET.SubElement(global_elements['client-server-interface5'], 'short-name')
    global_elements['short-name73'].text = 'Copy_ClientServerInterface'
    global_elements['is-service5'] = ET.SubElement(global_elements['client-server-interface5'], 'is-service')
    global_elements['is-service5'].text = 'false'

def Copy_ClientServerInterface_ClientServereOperation():
    global_elements['operations5'] = ET.SubElement(global_elements['client-server-interface5'], 'operations')
    global_elements['client-server-operation9'] = ET.SubElement(global_elements['operations5'], 'client-server-operation')
    global_elements['client-server-operation9'].attrib = {'UUID': '5d536ac2-edd2-4788-b233-5b0ef32a2022'}
    global_elements['short-name74'] = ET.SubElement(global_elements['client-server-operation9'], 'short-name')
    global_elements['short-name74'].text = 'Operation'
    global_elements['arguments9'] = ET.SubElement(global_elements['client-server-operation9'], 'arguments')
    global_elements['argument-data-prototype9'] = ET.SubElement(global_elements['arguments9'], 'argument-data-prototype')
    global_elements['argument-data-prototype9'].attrib = {'UUID': '174674f0-498e-41bc-9667-2459277f62ea'}
    global_elements['short-name75'] = ET.SubElement(global_elements['argument-data-prototype9'], 'short-name')
    global_elements['short-name75'].text = 'Argument'
    global_elements['sw-data-def-props23'] = ET.SubElement(global_elements['argument-data-prototype9'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants23'] = ET.SubElement(global_elements['sw-data-def-props23'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional23'] = ET.SubElement(global_elements['sw-data-def-props-variants23'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy9'] = ET.SubElement(global_elements['sw-data-def-props-conditional23'], 'sw-impl-policy')
    global_elements['sw-impl-policy9'].text = 'STANDARD'
    global_elements['type-tref13'] = ET.SubElement(global_elements['argument-data-prototype9'], 'type-tref')
    global_elements['type-tref13'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref13'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['direction9'] = ET.SubElement(global_elements['argument-data-prototype9'], 'direction')
    global_elements['direction9'].text = 'IN'
    global_elements['server-argument-impl-policy9'] = ET.SubElement(global_elements['argument-data-prototype9'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy9'].text = 'USE-ARGUMENT-TYPE'

def Copy_ClientServerInterface_ClientServereOperation1():
    global_elements['client-server-operation10'] = ET.SubElement(global_elements['operations5'], 'client-server-operation')
    global_elements['client-server-operation10'].attrib = {'UUID': 'be00c41e-3412-411d-ad74-a6a0feee0ecd'}
    global_elements['short-name76'] = ET.SubElement(global_elements['client-server-operation10'], 'short-name')
    global_elements['short-name76'].text = 'Operation1'
    global_elements['arguments10'] = ET.SubElement(global_elements['client-server-operation10'], 'arguments')
    global_elements['argument-data-prototype10'] = ET.SubElement(global_elements['arguments10'], 'argument-data-prototype')
    global_elements['argument-data-prototype10'].attrib = {'UUID': '8c68ce17-1680-4ec1-951d-9d9c871aca06'}
    global_elements['short-name77'] = ET.SubElement(global_elements['argument-data-prototype10'], 'short-name')
    global_elements['short-name77'].text = 'Argument'
    global_elements['sw-data-def-props24'] = ET.SubElement(global_elements['argument-data-prototype10'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants24'] = ET.SubElement(global_elements['sw-data-def-props24'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional24'] = ET.SubElement(global_elements['sw-data-def-props-variants24'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy10'] = ET.SubElement(global_elements['sw-data-def-props-conditional24'], 'sw-impl-policy')
    global_elements['sw-impl-policy10'].text = 'STANDARD'
    global_elements['type-tref14'] = ET.SubElement(global_elements['argument-data-prototype10'], 'type-tref')
    global_elements['type-tref14'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref14'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['direction10'] = ET.SubElement(global_elements['argument-data-prototype10'], 'direction')
    global_elements['direction10'].text = 'OUT'
    global_elements['server-argument-impl-policy10'] = ET.SubElement(global_elements['argument-data-prototype10'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy10'].text = 'USE-ARGUMENT-TYPE'


def Copy_ModeDeclarationGroup():
    # global_elements['ar-package14'] = ET.SubElement(global_elements['ar-packages4'], 'ar-package')
    # global_elements['ar-package14'].attrib = {'UUID': '3503a605-12c8-44be-96cf-4ad548d5d58f'}
    # global_elements['short-name78'] = ET.SubElement(global_elements['ar-package14'], 'short-name')
    # global_elements['short-name78'].text = 'ModeSwitch'
    # global_elements['elements12'] = ET.SubElement(global_elements['ar-package14'], 'elements')
    global_elements['mode-declaration-group'] = ET.SubElement(global_elements['elements12'], 'mode-declaration-group')
    global_elements['mode-declaration-group'].attrib = {'UUID': 'd1db93d0-7154-468f-b3bc-872d23a7385f'}
    global_elements['short-name79'] = ET.SubElement(global_elements['mode-declaration-group'], 'short-name')
    global_elements['short-name79'].text = 'Copy_ModeDeclarationGroup'
    global_elements['category32'] = ET.SubElement(global_elements['mode-declaration-group'], 'category')
    global_elements['category32'].text = 'EXPLICIT_ORDER'
    global_elements['initial-mode-ref'] = ET.SubElement(global_elements['mode-declaration-group'], 'initial-mode-ref')
    global_elements['initial-mode-ref'].text = '/SharedElements/PortInterfaces/ModeSwitch/Copy_ModeDeclarationGroup/ModeDeclaration'
    global_elements['initial-mode-ref'].attrib = {'DEST': 'MODE-DECLARATION'}

def Copy_ModeDeclarationGroup_ModeDeclaration():
    global_elements['mode-declarations'] = ET.SubElement(global_elements['mode-declaration-group'], 'mode-declarations')
    global_elements['mode-declaration'] = ET.SubElement(global_elements['mode-declarations'], 'mode-declaration')
    global_elements['mode-declaration'].attrib = {'UUID': '2608f59c-87b0-47b2-8cee-8e9c3ba94cac'}
    global_elements['short-name80'] = ET.SubElement(global_elements['mode-declaration'], 'short-name')
    global_elements['short-name80'].text = 'ModeDeclaration'
    global_elements['value4'] = ET.SubElement(global_elements['mode-declaration'], 'value')
    global_elements['value4'].text = '0'

def Copy_ModeDeclarationGroup_ModeDeclaration1():
    global_elements['mode-declaration2'] = ET.SubElement(global_elements['mode-declarations'], 'mode-declaration')
    global_elements['mode-declaration2'].attrib = {'UUID': '7cc2e588-342f-40a3-ad77-b3d49457e996'}
    global_elements['short-name81'] = ET.SubElement(global_elements['mode-declaration2'], 'short-name')
    global_elements['short-name81'].text = 'ModeDeclaration1'
    global_elements['value5'] = ET.SubElement(global_elements['mode-declaration2'], 'value')
    global_elements['value5'].text = '1'

def Copy_ModeDeclarationGroup_ModeDeclaration2():
    global_elements['mode-declaration3'] = ET.SubElement(global_elements['mode-declarations'], 'mode-declaration')
    global_elements['mode-declaration3'].attrib = {'UUID': '278335ee-b40e-4f50-9fc3-164297dafbfd'}
    global_elements['short-name82'] = ET.SubElement(global_elements['mode-declaration3'], 'short-name')
    global_elements['short-name82'].text = 'ModeDeclaration2'
    global_elements['value6'] = ET.SubElement(global_elements['mode-declaration3'], 'value')
    global_elements['value6'].text = '2'
    global_elements['on-transition-value'] = ET.SubElement(global_elements['mode-declaration-group'], 'on-transition-value')
    global_elements['on-transition-value'].text = '3'

def Copy_ModeSwitchInterface():
    global_elements['mode-switch-interface'] = ET.SubElement(global_elements['elements12'], 'mode-switch-interface')
    global_elements['mode-switch-interface'].attrib = {'UUID': '359238c5-e830-44a4-b8a0-362c11b6864f'}
    global_elements['short-name83'] = ET.SubElement(global_elements['mode-switch-interface'], 'short-name')
    global_elements['short-name83'].text = 'Copy_ModeSwitchInterface'
    global_elements['is-service6'] = ET.SubElement(global_elements['mode-switch-interface'], 'is-service')
    global_elements['is-service6'].text = 'false'
    global_elements['mode-group'] = ET.SubElement(global_elements['mode-switch-interface'], 'mode-group')
    global_elements['mode-group'].attrib = {'UUID': '5de6bb25-e952-4b16-ad52-f4692d7da6d9'}
    global_elements['short-name84'] = ET.SubElement(global_elements['mode-group'], 'short-name')
    global_elements['short-name84'].text = 'ModeGroup'
    global_elements['type-tref15'] = ET.SubElement(global_elements['mode-group'], 'type-tref')
    global_elements['type-tref15'].text = '/SharedElements/PortInterfaces/ModeSwitch/Copy_ModeDeclarationGroup'
    global_elements['type-tref15'].attrib = {'DEST': 'MODE-DECLARATION-GROUP'}

def ModeDeclarationGroup():
    global_elements['mode-declaration-group2'] = ET.SubElement(global_elements['elements12'], 'mode-declaration-group')
    global_elements['mode-declaration-group2'].attrib = {'UUID': 'b9ed1cc5-6caf-43d0-b094-3c763b6cbb9a'}
    global_elements['short-name85'] = ET.SubElement(global_elements['mode-declaration-group2'], 'short-name')
    global_elements['short-name85'].text = 'ModeDeclarationGroup'
    global_elements['category33'] = ET.SubElement(global_elements['mode-declaration-group2'], 'category')
    global_elements['category33'].text = 'ALPHABETIC_ORDER'
    global_elements['initial-mode-ref2'] = ET.SubElement(global_elements['mode-declaration-group2'], 'initial-mode-ref')
    global_elements['initial-mode-ref2'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeDeclarationGroup/ModeDeclaration'
    global_elements['initial-mode-ref2'].attrib = {'DEST': 'MODE-DECLARATION'}
    global_elements['mode-declarations2'] = ET.SubElement(global_elements['mode-declaration-group2'], 'mode-declarations')

def ModeDeclarationGroup_ModeDeclaration():
    global_elements['mode-declaration4'] = ET.SubElement(global_elements['mode-declarations2'], 'mode-declaration')
    global_elements['mode-declaration4'].attrib = {'UUID': 'c1fb19b0-d635-4deb-a718-37e3d20b8878'}
    global_elements['short-name86'] = ET.SubElement(global_elements['mode-declaration4'], 'short-name')
    global_elements['short-name86'].text = 'ModeDeclaration'

def ModeDeclarationGroup_ModeDeclaration1():
    global_elements['mode-declaration5'] = ET.SubElement(global_elements['mode-declarations2'], 'mode-declaration')
    global_elements['mode-declaration5'].attrib = {'UUID': 'a586eb27-c099-42ab-b553-a0fd227d1fe5'}
    global_elements['short-name87'] = ET.SubElement(global_elements['mode-declaration5'], 'short-name')
    global_elements['short-name87'].text = 'ModeDeclaration1'

def ModeDeclarationGroup_ModeDeclaration2():
    global_elements['mode-declaration6'] = ET.SubElement(global_elements['mode-declarations2'], 'mode-declaration')
    global_elements['mode-declaration6'].attrib = {'UUID': 'a891dd23-e1f6-41f0-b669-b383af7bd17e'}
    global_elements['short-name88'] = ET.SubElement(global_elements['mode-declaration6'], 'short-name')
    global_elements['short-name88'].text = 'ModeDeclaration2'


def ModeSwitchInterface():
    global_elements['mode-switch-interface2'] = ET.SubElement(global_elements['elements12'], 'mode-switch-interface')
    global_elements['mode-switch-interface2'].attrib = {'UUID': '949dcf4f-08eb-4d99-8504-1c613d93f5e9'}
    global_elements['short-name89'] = ET.SubElement(global_elements['mode-switch-interface2'], 'short-name')
    global_elements['short-name89'].text = 'ModeSwitchInterface'
    global_elements['is-service7'] = ET.SubElement(global_elements['mode-switch-interface2'], 'is-service')
    global_elements['is-service7'].text = 'false'
    global_elements['mode-group2'] = ET.SubElement(global_elements['mode-switch-interface2'], 'mode-group')
    global_elements['mode-group2'].attrib = {'UUID': '26ede937-ce36-4065-93e5-d8bca12d51cd'}
    global_elements['short-name90'] = ET.SubElement(global_elements['mode-group2'], 'short-name')
    global_elements['short-name90'].text = 'ModeGroup'
    global_elements['type-tref16'] = ET.SubElement(global_elements['mode-group2'], 'type-tref')
    global_elements['type-tref16'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeDeclarationGroup'
    global_elements['type-tref16'].attrib = {'DEST': 'MODE-DECLARATION-GROUP'}

def NvDataInterface():
    # global_elements['ar-package15'] = ET.SubElement(global_elements['ar-packages4'], 'ar-package')
    # global_elements['ar-package15'].attrib = {'UUID': '07677b4a-bc79-4c7b-afa1-581ad642a3dd'}
    # global_elements['short-name91'] = ET.SubElement(global_elements['ar-package15'], 'short-name')
    # global_elements['short-name91'].text = 'NvData'
    # global_elements['elements13'] = ET.SubElement(global_elements['ar-package15'], 'elements')

    global_elements['nv-data-interface'] = ET.SubElement(global_elements['elements13'], 'nv-data-interface')
    global_elements['nv-data-interface'].attrib = {'UUID': '8a4989b3-88e2-4e47-b98f-591e75c76b17'}
    global_elements['short-name92'] = ET.SubElement(global_elements['nv-data-interface'], 'short-name')
    global_elements['short-name92'].text = 'NvDataInterface'
    global_elements['is-service8'] = ET.SubElement(global_elements['nv-data-interface'], 'is-service')
    global_elements['is-service8'].text = 'false'

def VariableDataPrototype_NvData():
    global_elements['nv-datas'] = ET.SubElement(global_elements['nv-data-interface'], 'nv-datas')
    global_elements['variable-data-prototype'] = ET.SubElement(global_elements['nv-datas'], 'variable-data-prototype')
    global_elements['variable-data-prototype'].attrib = {'UUID': '8a84bf2f-0e49-4923-bbc2-7a6606812ef4'}
    global_elements['short-name93'] = ET.SubElement(global_elements['variable-data-prototype'], 'short-name')
    global_elements['short-name93'].text = 'NvData'
    global_elements['sw-data-def-props25'] = ET.SubElement(global_elements['variable-data-prototype'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants25'] = ET.SubElement(global_elements['sw-data-def-props25'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional25'] = ET.SubElement(global_elements['sw-data-def-props-variants25'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy11'] = ET.SubElement(global_elements['sw-data-def-props-conditional25'], 'sw-impl-policy')
    global_elements['sw-impl-policy11'].text = 'STANDARD'
    global_elements['type-tref17'] = ET.SubElement(global_elements['variable-data-prototype'], 'type-tref')
    global_elements['type-tref17'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref17'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def VariableDataPrototype_NvData1():
    global_elements['variable-data-prototype2'] = ET.SubElement(global_elements['nv-datas'], 'variable-data-prototype')
    global_elements['variable-data-prototype2'].attrib = {'UUID': '4437f330-788c-4fb4-92e5-9545dfdbd9f0'}
    global_elements['short-name94'] = ET.SubElement(global_elements['variable-data-prototype2'], 'short-name')
    global_elements['short-name94'].text = 'NvData1'
    global_elements['sw-data-def-props26'] = ET.SubElement(global_elements['variable-data-prototype2'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants26'] = ET.SubElement(global_elements['sw-data-def-props26'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional26'] = ET.SubElement(global_elements['sw-data-def-props-variants26'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy12'] = ET.SubElement(global_elements['sw-data-def-props-conditional26'], 'sw-impl-policy')
    global_elements['sw-impl-policy12'].text = 'STANDARD'
    global_elements['type-tref18'] = ET.SubElement(global_elements['variable-data-prototype2'], 'type-tref')
    global_elements['type-tref18'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float64'
    global_elements['type-tref18'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def ParameterInterface():
    # global_elements['ar-package16'] = ET.SubElement(global_elements['ar-packages4'], 'ar-package')
    # global_elements['ar-package16'].attrib = {'UUID': '9b48ec34-87aa-4f84-9080-1d3f919ca090'}
    # global_elements['short-name95'] = ET.SubElement(global_elements['ar-package16'], 'short-name')
    # global_elements['short-name95'].text = 'Parameter'
    # global_elements['elements14'] = ET.SubElement(global_elements['ar-package16'], 'elements')
    global_elements['parameter-interface'] = ET.SubElement(global_elements['elements14'], 'parameter-interface')
    global_elements['parameter-interface'].attrib = {'UUID': '618ca0ee-adf8-43c1-b898-33ea5ca916d8'}
    global_elements['short-name96'] = ET.SubElement(global_elements['parameter-interface'], 'short-name')
    global_elements['short-name96'].text = 'ParameterInterface'
    global_elements['is-service9'] = ET.SubElement(global_elements['parameter-interface'], 'is-service')
    global_elements['is-service9'].text = 'false'
    global_elements['parameters'] = ET.SubElement(global_elements['parameter-interface'], 'parameters')

def ParameterDataPrototype_Parameter():
    global_elements['parameter-data-prototype'] = ET.SubElement(global_elements['parameters'], 'parameter-data-prototype')
    global_elements['parameter-data-prototype'].attrib = {'UUID': 'd359a294-51b2-461a-b7fb-0de80cf2598a'}
    global_elements['short-name97'] = ET.SubElement(global_elements['parameter-data-prototype'], 'short-name')
    global_elements['short-name97'].text = 'Parameter'
    global_elements['sw-data-def-props27'] = ET.SubElement(global_elements['parameter-data-prototype'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants27'] = ET.SubElement(global_elements['sw-data-def-props27'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional27'] = ET.SubElement(global_elements['sw-data-def-props-variants27'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access5'] = ET.SubElement(global_elements['sw-data-def-props-conditional27'], 'sw-calibration-access')
    global_elements['sw-calibration-access5'].text = 'READ-WRITE'
    global_elements['sw-impl-policy13'] = ET.SubElement(global_elements['sw-data-def-props-conditional27'], 'sw-impl-policy')
    global_elements['sw-impl-policy13'].text = 'STANDARD'
    global_elements['type-tref19'] = ET.SubElement(global_elements['parameter-data-prototype'], 'type-tref')
    global_elements['type-tref19'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float32'
    global_elements['type-tref19'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def ParameterDataPrototype_Parameter1():
    global_elements['parameter-data-prototype2'] = ET.SubElement(global_elements['parameters'], 'parameter-data-prototype')
    global_elements['parameter-data-prototype2'].attrib = {'UUID': 'a60e4821-63b4-4fa4-9f04-983264b2a55f'}
    global_elements['short-name98'] = ET.SubElement(global_elements['parameter-data-prototype2'], 'short-name')
    global_elements['short-name98'].text = 'Parameter1'
    global_elements['sw-data-def-props28'] = ET.SubElement(global_elements['parameter-data-prototype2'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants28'] = ET.SubElement(global_elements['sw-data-def-props28'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional28'] = ET.SubElement(global_elements['sw-data-def-props-variants28'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access6'] = ET.SubElement(global_elements['sw-data-def-props-conditional28'], 'sw-calibration-access')
    global_elements['sw-calibration-access6'].text = 'READ-WRITE'
    global_elements['sw-impl-policy14'] = ET.SubElement(global_elements['sw-data-def-props-conditional28'], 'sw-impl-policy')
    global_elements['sw-impl-policy14'].text = 'STANDARD'
    global_elements['type-tref20'] = ET.SubElement(global_elements['parameter-data-prototype2'], 'type-tref')
    global_elements['type-tref20'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref20'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy2_SenderReceiverInterface():
    # global_elements['ar-package17'] = ET.SubElement(global_elements['ar-packages4'], 'ar-package')
    # global_elements['ar-package17'].attrib = {'UUID': '304f7bbd-15e6-4f85-b22f-4b02c9a5631c'}
    # global_elements['short-name99'] = ET.SubElement(global_elements['ar-package17'], 'short-name')
    # global_elements['short-name99'].text = 'SenderReceiver'
    # global_elements['elements15'] = ET.SubElement(global_elements['ar-package17'], 'elements')
    global_elements['sender-receiver-interface'] = ET.SubElement(global_elements['elements15'], 'sender-receiver-interface')
    global_elements['sender-receiver-interface'].attrib = {'UUID': '5301b51c-ab80-4717-880a-f53963ebb47d'}
    global_elements['short-name100'] = ET.SubElement(global_elements['sender-receiver-interface'], 'short-name')
    global_elements['short-name100'].text = 'Copy2_SenderReceiverInterface'
    global_elements['is-service10'] = ET.SubElement(global_elements['sender-receiver-interface'], 'is-service')
    global_elements['is-service10'].text = 'false'
    global_elements['data-elements'] = ET.SubElement(global_elements['sender-receiver-interface'], 'data-elements')

def Copy2_SenderReceiverInterface_VariableDataPrototype_DataElement():
    global_elements['variable-data-prototype3'] = ET.SubElement(global_elements['data-elements'], 'variable-data-prototype')
    global_elements['variable-data-prototype3'].attrib = {'UUID': 'd071c034-64ed-44d0-81f0-a0735e373ce3'}
    global_elements['short-name101'] = ET.SubElement(global_elements['variable-data-prototype3'], 'short-name')
    global_elements['short-name101'].text = 'DataElement'
    global_elements['sw-data-def-props29'] = ET.SubElement(global_elements['variable-data-prototype3'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants29'] = ET.SubElement(global_elements['sw-data-def-props29'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional29'] = ET.SubElement(global_elements['sw-data-def-props-variants29'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access7'] = ET.SubElement(global_elements['sw-data-def-props-conditional29'], 'sw-calibration-access')
    global_elements['sw-calibration-access7'].text = 'READ-WRITE'
    global_elements['sw-impl-policy15'] = ET.SubElement(global_elements['sw-data-def-props-conditional29'], 'sw-impl-policy')
    global_elements['sw-impl-policy15'].text = 'STANDARD'
    global_elements['type-tref21'] = ET.SubElement(global_elements['variable-data-prototype3'], 'type-tref')
    global_elements['type-tref21'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    global_elements['type-tref21'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy2_SenderReceiverInterface_VariableDataPrototype_DataElement1():
    global_elements['variable-data-prototype4'] = ET.SubElement(global_elements['data-elements'], 'variable-data-prototype')
    global_elements['variable-data-prototype4'].attrib = {'UUID': '3afe6629-f986-4006-9ecf-b2902644f64e'}
    global_elements['short-name102'] = ET.SubElement(global_elements['variable-data-prototype4'], 'short-name')
    global_elements['short-name102'].text = 'DataElement1'
    global_elements['sw-data-def-props30'] = ET.SubElement(global_elements['variable-data-prototype4'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants30'] = ET.SubElement(global_elements['sw-data-def-props30'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional30'] = ET.SubElement(global_elements['sw-data-def-props-variants30'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy16'] = ET.SubElement(global_elements['sw-data-def-props-conditional30'], 'sw-impl-policy')
    global_elements['sw-impl-policy16'].text = 'STANDARD'
    global_elements['type-tref22'] = ET.SubElement(global_elements['variable-data-prototype4'], 'type-tref')
    global_elements['type-tref22'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    global_elements['type-tref22'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy3_SenderReceiverInterface():
    global_elements['sender-receiver-interface2'] = ET.SubElement(global_elements['elements15'], 'sender-receiver-interface')
    global_elements['sender-receiver-interface2'].attrib = {'UUID': 'b4591ad1-c21f-4706-8eac-55f6169b8c96'}
    global_elements['short-name103'] = ET.SubElement(global_elements['sender-receiver-interface2'], 'short-name')
    global_elements['short-name103'].text = 'Copy3_SenderReceiverInterface'
    global_elements['is-service11'] = ET.SubElement(global_elements['sender-receiver-interface2'], 'is-service')
    global_elements['is-service11'].text = 'false'
    global_elements['data-elements2'] = ET.SubElement(global_elements['sender-receiver-interface2'], 'data-elements')

def Copy3_SenderReceiverInterface_VariableDataPrototype_DataElement():
    global_elements['variable-data-prototype5'] = ET.SubElement(global_elements['data-elements2'], 'variable-data-prototype')
    global_elements['variable-data-prototype5'].attrib = {'UUID': 'dd322790-2f29-43dc-93a0-10c5addc7871'}
    global_elements['short-name104'] = ET.SubElement(global_elements['variable-data-prototype5'], 'short-name')
    global_elements['short-name104'].text = 'DataElement'
    global_elements['sw-data-def-props31'] = ET.SubElement(global_elements['variable-data-prototype5'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants31'] = ET.SubElement(global_elements['sw-data-def-props31'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional31'] = ET.SubElement(global_elements['sw-data-def-props-variants31'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access8'] = ET.SubElement(global_elements['sw-data-def-props-conditional31'], 'sw-calibration-access')
    global_elements['sw-calibration-access8'].text = 'READ-WRITE'
    global_elements['sw-impl-policy17'] = ET.SubElement(global_elements['sw-data-def-props-conditional31'], 'sw-impl-policy')
    global_elements['sw-impl-policy17'].text = 'STANDARD'
    global_elements['type-tref23'] = ET.SubElement(global_elements['variable-data-prototype5'], 'type-tref')
    global_elements['type-tref23'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    global_elements['type-tref23'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy3_SenderReceiverInterface_VariableDataPrototype_DataElement1():
    global_elements['variable-data-prototype6'] = ET.SubElement(global_elements['data-elements2'], 'variable-data-prototype')
    global_elements['variable-data-prototype6'].attrib = {'UUID': '27292aab-8793-404f-b1d0-3128a4ab29bf'}
    global_elements['short-name105'] = ET.SubElement(global_elements['variable-data-prototype6'], 'short-name')
    global_elements['short-name105'].text = 'DataElement1'
    global_elements['sw-data-def-props32'] = ET.SubElement(global_elements['variable-data-prototype6'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants32'] = ET.SubElement(global_elements['sw-data-def-props32'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional32'] = ET.SubElement(global_elements['sw-data-def-props-variants32'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy18'] = ET.SubElement(global_elements['sw-data-def-props-conditional32'], 'sw-impl-policy')
    global_elements['sw-impl-policy18'].text = 'STANDARD'
    global_elements['type-tref24'] = ET.SubElement(global_elements['variable-data-prototype6'], 'type-tref')
    global_elements['type-tref24'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    global_elements['type-tref24'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def Copy4_SenderReceiverInterface():
    global_elements['sender-receiver-interface3'] = ET.SubElement(global_elements['elements15'], 'sender-receiver-interface')
    global_elements['sender-receiver-interface3'].attrib = {'UUID': 'e5b1f8fc-9e46-4d58-b278-cb3461917783'}
    global_elements['short-name106'] = ET.SubElement(global_elements['sender-receiver-interface3'], 'short-name')
    global_elements['short-name106'].text = 'Copy4_SenderReceiverInterface'
    global_elements['is-service12'] = ET.SubElement(global_elements['sender-receiver-interface3'], 'is-service')
    global_elements['is-service12'].text = 'false'
    global_elements['data-elements3'] = ET.SubElement(global_elements['sender-receiver-interface3'], 'data-elements')

def Copy4_SenderReceiverInterface_VariableDataPrototype_DataElement():
    global_elements['variable-data-prototype7'] = ET.SubElement(global_elements['data-elements3'], 'variable-data-prototype')
    global_elements['variable-data-prototype7'].attrib = {'UUID': '81fa7709-76a3-4e64-8ab6-0302340d9596'}
    global_elements['short-name107'] = ET.SubElement(global_elements['variable-data-prototype7'], 'short-name')
    global_elements['short-name107'].text = 'DataElement'
    global_elements['sw-data-def-props33'] = ET.SubElement(global_elements['variable-data-prototype7'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants33'] = ET.SubElement(global_elements['sw-data-def-props33'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional33'] = ET.SubElement(global_elements['sw-data-def-props-variants33'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access9'] = ET.SubElement(global_elements['sw-data-def-props-conditional33'], 'sw-calibration-access')
    global_elements['sw-calibration-access9'].text = 'READ-WRITE'
    global_elements['sw-impl-policy19'] = ET.SubElement(global_elements['sw-data-def-props-conditional33'], 'sw-impl-policy')
    global_elements['sw-impl-policy19'].text = 'STANDARD'
    global_elements['type-tref25'] = ET.SubElement(global_elements['variable-data-prototype7'], 'type-tref')
    global_elements['type-tref25'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    global_elements['type-tref25'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy4_SenderReceiverInterface_VariableDataPrototype_DataElement1():
    global_elements['variable-data-prototype8'] = ET.SubElement(global_elements['data-elements3'], 'variable-data-prototype')
    global_elements['variable-data-prototype8'].attrib = {'UUID': '4139b239-b260-44f9-a1b9-26592a9702b7'}
    global_elements['short-name108'] = ET.SubElement(global_elements['variable-data-prototype8'], 'short-name')
    global_elements['short-name108'].text = 'DataElement1'
    global_elements['sw-data-def-props34'] = ET.SubElement(global_elements['variable-data-prototype8'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants34'] = ET.SubElement(global_elements['sw-data-def-props34'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional34'] = ET.SubElement(global_elements['sw-data-def-props-variants34'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy20'] = ET.SubElement(global_elements['sw-data-def-props-conditional34'], 'sw-impl-policy')
    global_elements['sw-impl-policy20'].text = 'STANDARD'
    global_elements['type-tref26'] = ET.SubElement(global_elements['variable-data-prototype8'], 'type-tref')
    global_elements['type-tref26'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    global_elements['type-tref26'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def Copy5_SenderReceiverInterface():
    global_elements['sender-receiver-interface4'] = ET.SubElement(global_elements['elements15'], 'sender-receiver-interface')
    global_elements['sender-receiver-interface4'].attrib = {'UUID': '67583438-372e-4f89-aad7-44d221ba987e'}
    global_elements['short-name109'] = ET.SubElement(global_elements['sender-receiver-interface4'], 'short-name')
    global_elements['short-name109'].text = 'Copy5_SenderReceiverInterface'
    global_elements['is-service13'] = ET.SubElement(global_elements['sender-receiver-interface4'], 'is-service')
    global_elements['is-service13'].text = 'false'
    global_elements['data-elements4'] = ET.SubElement(global_elements['sender-receiver-interface4'], 'data-elements')

def Copy5_SenderReceiverInterface_VariableDataPrototype_DataElement():
    global_elements['variable-data-prototype9'] = ET.SubElement(global_elements['data-elements4'], 'variable-data-prototype')
    global_elements['variable-data-prototype9'].attrib = {'UUID': 'b67450ea-eee7-49cd-9e1b-696114cdc06b'}
    global_elements['short-name110'] = ET.SubElement(global_elements['variable-data-prototype9'], 'short-name')
    global_elements['short-name110'].text = 'DataElement'
    global_elements['sw-data-def-props35'] = ET.SubElement(global_elements['variable-data-prototype9'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants35'] = ET.SubElement(global_elements['sw-data-def-props35'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional35'] = ET.SubElement(global_elements['sw-data-def-props-variants35'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access10'] = ET.SubElement(global_elements['sw-data-def-props-conditional35'], 'sw-calibration-access')
    global_elements['sw-calibration-access10'].text = 'READ-WRITE'
    global_elements['sw-impl-policy21'] = ET.SubElement(global_elements['sw-data-def-props-conditional35'], 'sw-impl-policy')
    global_elements['sw-impl-policy21'].text = 'STANDARD'
    global_elements['type-tref27'] = ET.SubElement(global_elements['variable-data-prototype9'], 'type-tref')
    global_elements['type-tref27'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    global_elements['type-tref27'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy5_SenderReceiverInterface_VariableDataPrototype_DataElement1():
    global_elements['variable-data-prototype10'] = ET.SubElement(global_elements['data-elements4'], 'variable-data-prototype')
    global_elements['variable-data-prototype10'].attrib = {'UUID': '6616174f-78ab-48e5-b54f-f0ac623eefa6'}
    global_elements['short-name111'] = ET.SubElement(global_elements['variable-data-prototype10'], 'short-name')
    global_elements['short-name111'].text = 'DataElement1'
    global_elements['sw-data-def-props36'] = ET.SubElement(global_elements['variable-data-prototype10'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants36'] = ET.SubElement(global_elements['sw-data-def-props36'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional36'] = ET.SubElement(global_elements['sw-data-def-props-variants36'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy22'] = ET.SubElement(global_elements['sw-data-def-props-conditional36'], 'sw-impl-policy')
    global_elements['sw-impl-policy22'].text = 'STANDARD'
    global_elements['type-tref28'] = ET.SubElement(global_elements['variable-data-prototype10'], 'type-tref')
    global_elements['type-tref28'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    global_elements['type-tref28'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy_SenderReceiverInterface():
    global_elements['sender-receiver-interface5'] = ET.SubElement(global_elements['elements15'], 'sender-receiver-interface')
    global_elements['sender-receiver-interface5'].attrib = {'UUID': 'c0a51d5f-0a8c-4bdc-a77d-03a338508c6b'}
    global_elements['short-name112'] = ET.SubElement(global_elements['sender-receiver-interface5'], 'short-name')
    global_elements['short-name112'].text = 'Copy_SenderReceiverInterface'
    global_elements['is-service14'] = ET.SubElement(global_elements['sender-receiver-interface5'], 'is-service')
    global_elements['is-service14'].text = 'false'
    global_elements['data-elements5'] = ET.SubElement(global_elements['sender-receiver-interface5'], 'data-elements')

def Copy_SenderReceiverInterface_VariableDataPrototype_DataElement():
    global_elements['variable-data-prototype11'] = ET.SubElement(global_elements['data-elements5'], 'variable-data-prototype')
    global_elements['variable-data-prototype11'].attrib = {'UUID': 'b7a89eaf-844f-4e6d-b357-dc9976ba211e'}
    global_elements['short-name113'] = ET.SubElement(global_elements['variable-data-prototype11'], 'short-name')
    global_elements['short-name113'].text = 'DataElement'
    global_elements['sw-data-def-props37'] = ET.SubElement(global_elements['variable-data-prototype11'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants37'] = ET.SubElement(global_elements['sw-data-def-props37'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional37'] = ET.SubElement(global_elements['sw-data-def-props-variants37'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access11'] = ET.SubElement(global_elements['sw-data-def-props-conditional37'], 'sw-calibration-access')
    global_elements['sw-calibration-access11'].text = 'READ-WRITE'
    global_elements['sw-impl-policy23'] = ET.SubElement(global_elements['sw-data-def-props-conditional37'], 'sw-impl-policy')
    global_elements['sw-impl-policy23'].text = 'STANDARD'
    global_elements['type-tref29'] = ET.SubElement(global_elements['variable-data-prototype11'], 'type-tref')
    global_elements['type-tref29'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    global_elements['type-tref29'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy_SenderReceiverInterface_VariableDataPrototype_DataElement1():
    global_elements['variable-data-prototype12'] = ET.SubElement(global_elements['data-elements5'], 'variable-data-prototype')
    global_elements['variable-data-prototype12'].attrib = {'UUID': '373c6d56-b664-4bba-b6bf-37630aed9fef'}
    global_elements['short-name114'] = ET.SubElement(global_elements['variable-data-prototype12'], 'short-name')
    global_elements['short-name114'].text = 'DataElement1'
    global_elements['sw-data-def-props38'] = ET.SubElement(global_elements['variable-data-prototype12'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants38'] = ET.SubElement(global_elements['sw-data-def-props38'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional38'] = ET.SubElement(global_elements['sw-data-def-props-variants38'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy24'] = ET.SubElement(global_elements['sw-data-def-props-conditional38'], 'sw-impl-policy')
    global_elements['sw-impl-policy24'].text = 'STANDARD'
    global_elements['type-tref30'] = ET.SubElement(global_elements['variable-data-prototype12'], 'type-tref')
    global_elements['type-tref30'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    global_elements['type-tref30'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def SenderReceiverInterface():
    global_elements['sender-receiver-interface6'] = ET.SubElement(global_elements['elements15'], 'sender-receiver-interface')
    global_elements['sender-receiver-interface6'].attrib = {'UUID': '5f56a3f5-0f22-429f-a8b9-003d68bbc759'}
    global_elements['short-name115'] = ET.SubElement(global_elements['sender-receiver-interface6'], 'short-name')
    global_elements['short-name115'].text = 'SenderReceiverInterface'
    global_elements['is-service15'] = ET.SubElement(global_elements['sender-receiver-interface6'], 'is-service')
    global_elements['is-service15'].text = 'false'
    global_elements['data-elements6'] = ET.SubElement(global_elements['sender-receiver-interface6'], 'data-elements')

def SenderReceiverInterface_VariableDataPrototype_DataElement():
    global_elements['variable-data-prototype13'] = ET.SubElement(global_elements['data-elements6'], 'variable-data-prototype')
    global_elements['variable-data-prototype13'].attrib = {'UUID': 'c448fbc4-20d2-443d-bb7a-87585742cfcf'}
    global_elements['short-name116'] = ET.SubElement(global_elements['variable-data-prototype13'], 'short-name')
    global_elements['short-name116'].text = 'DataElement'
    global_elements['sw-data-def-props39'] = ET.SubElement(global_elements['variable-data-prototype13'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants39'] = ET.SubElement(global_elements['sw-data-def-props39'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional39'] = ET.SubElement(global_elements['sw-data-def-props-variants39'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access12'] = ET.SubElement(global_elements['sw-data-def-props-conditional39'], 'sw-calibration-access')
    global_elements['sw-calibration-access12'].text = 'READ-WRITE'
    global_elements['sw-impl-policy25'] = ET.SubElement(global_elements['sw-data-def-props-conditional39'], 'sw-impl-policy')
    global_elements['sw-impl-policy25'].text = 'STANDARD'
    global_elements['type-tref31'] = ET.SubElement(global_elements['variable-data-prototype13'], 'type-tref')
    global_elements['type-tref31'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref31'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}

def SenderReceiverInterface_VariableDataPrototype_DataElement1():
    global_elements['variable-data-prototype14'] = ET.SubElement(global_elements['data-elements6'], 'variable-data-prototype')
    global_elements['variable-data-prototype14'].attrib = {'UUID': '6862a5ea-8794-4906-9f54-50624e9d6044'}
    global_elements['short-name117'] = ET.SubElement(global_elements['variable-data-prototype14'], 'short-name')
    global_elements['short-name117'].text = 'DataElement1'
    global_elements['sw-data-def-props40'] = ET.SubElement(global_elements['variable-data-prototype14'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants40'] = ET.SubElement(global_elements['sw-data-def-props40'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional40'] = ET.SubElement(global_elements['sw-data-def-props-variants40'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy26'] = ET.SubElement(global_elements['sw-data-def-props-conditional40'], 'sw-impl-policy')
    global_elements['sw-impl-policy26'].text = 'STANDARD'
    global_elements['type-tref32'] = ET.SubElement(global_elements['variable-data-prototype14'], 'type-tref')
    global_elements['type-tref32'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    global_elements['type-tref32'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['invalidation-policys'] = ET.SubElement(global_elements['sender-receiver-interface6'], 'invalidation-policys')
    global_elements['invalidation-policy'] = ET.SubElement(global_elements['invalidation-policys'], 'invalidation-policy')
    global_elements['data-element-ref'] = ET.SubElement(global_elements['invalidation-policy'], 'data-element-ref')
    global_elements['data-element-ref'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    global_elements['data-element-ref'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['handle-invalid'] = ET.SubElement(global_elements['invalidation-policy'], 'handle-invalid')
    global_elements['handle-invalid'].text = 'KEEP'

def Trigger():
    # global_elements['ar-package18'] = ET.SubElement(global_elements['ar-packages4'], 'ar-package')
    # global_elements['ar-package18'].attrib = {'UUID': '00421379-584f-4dbb-8c9f-d70ad66b8e41'}
    # global_elements['short-name118'] = ET.SubElement(global_elements['ar-package18'], 'short-name')
    # global_elements['short-name118'].text = 'Trigger'
    # global_elements['elements16'] = ET.SubElement(global_elements['ar-package18'], 'elements')
    global_elements['trigger-interface'] = ET.SubElement(global_elements['elements16'], 'trigger-interface')
    global_elements['trigger-interface'].attrib = {'UUID': '97d54491-56c6-49b9-9812-bb5eadaefa82'}
    global_elements['short-name119'] = ET.SubElement(global_elements['trigger-interface'], 'short-name')
    global_elements['short-name119'].text = 'TriggerInterface'
    global_elements['is-service16'] = ET.SubElement(global_elements['trigger-interface'], 'is-service')
    global_elements['is-service16'].text = 'false'
    global_elements['triggers'] = ET.SubElement(global_elements['trigger-interface'], 'triggers')
    global_elements['trigger'] = ET.SubElement(global_elements['triggers'], 'trigger')
    global_elements['trigger'].attrib = {'UUID': '06d545dc-664d-45fb-be23-8a076bded4b5'}
    global_elements['short-name120'] = ET.SubElement(global_elements['trigger'], 'short-name')
    global_elements['short-name120'].text = 'Trigger'
    global_elements['sw-impl-policy27'] = ET.SubElement(global_elements['trigger'], 'sw-impl-policy')
    global_elements['sw-impl-policy27'].text = 'STANDARD'
    global_elements['trigger-period'] = ET.SubElement(global_elements['trigger'], 'trigger-period')
    global_elements['cse-code'] = ET.SubElement(global_elements['trigger-period'], 'cse-code')
    global_elements['cse-code'].text = '6'
    global_elements['cse-code-factor'] = ET.SubElement(global_elements['trigger-period'], 'cse-code-factor')
    global_elements['cse-code-factor'].text = '15'
    
def SwcImplementation():
    # global_elements['ar-package19'] = ET.SubElement(global_elements['ar-packages2'], 'ar-package')
    # global_elements['ar-package19'].attrib = {'UUID': 'a21c4095-c5dd-41b4-8a15-aa23a460a3e9'}
    # global_elements['short-name121'] = ET.SubElement(global_elements['ar-package19'], 'short-name')
    # global_elements['short-name121'].text = 'SWCImpl'
    # global_elements['elements17'] = ET.SubElement(global_elements['ar-package19'], 'elements')
    global_elements['swc-implementation'] = ET.SubElement(global_elements['elements17'], 'swc-implementation')
    global_elements['swc-implementation'].attrib = {'UUID': 'a8e1b9bd-bc2d-4bba-8d84-7fb588da487b'}
    global_elements['short-name122'] = ET.SubElement(global_elements['swc-implementation'], 'short-name')
    global_elements['short-name122'].text = 'SwcImplementation'
    global_elements['programming-language'] = ET.SubElement(global_elements['swc-implementation'], 'programming-language')
    global_elements['programming-language'].text = 'C'
    global_elements['sw-version'] = ET.SubElement(global_elements['swc-implementation'], 'sw-version')
    global_elements['sw-version'].text = '1.0.0.0'
    global_elements['behavior-ref'] = ET.SubElement(global_elements['swc-implementation'], 'behavior-ref')
    global_elements['behavior-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl'
    global_elements['behavior-ref'].attrib = {'DEST': 'SWC-INTERNAL-BEHAVIOR'}

def ResourceConsumption():
    global_elements['resource-consumption'] = ET.SubElement(global_elements['swc-implementation'], 'resource-consumption')
    global_elements['resource-consumption'].attrib = {'UUID': '664bf3d9-9efc-49d1-a4fd-9936922aa5f9'}
    global_elements['short-name123'] = ET.SubElement(global_elements['resource-consumption'], 'short-name')
    global_elements['short-name123'].text = 'ResourceConsumption'

def SwAddrMethods_Copy2_SwAddrMethod():
    # global_elements['ar-package20'] = ET.SubElement(global_elements['ar-packages2'], 'ar-package')
    # global_elements['ar-package20'].attrib = {'UUID': 'fc8b946c-31d4-49d6-8e0c-ff6847ede7f5'}
    # global_elements['short-name124'] = ET.SubElement(global_elements['ar-package20'], 'short-name')
    # global_elements['short-name124'].text = 'SwAddrMethods'
    # global_elements['elements18'] = ET.SubElement(global_elements['ar-package20'], 'elements')
    global_elements['sw-addr-method'] = ET.SubElement(global_elements['elements18'], 'sw-addr-method')
    global_elements['sw-addr-method'].attrib = {'UUID': '8a973d95-6644-4157-ab41-c78f7ccbcb2c'}
    global_elements['short-name125'] = ET.SubElement(global_elements['sw-addr-method'], 'short-name')
    global_elements['short-name125'].text = 'Copy2_SwAddrMethod'
    global_elements['memory-allocation-keyword-policy'] = ET.SubElement(global_elements['sw-addr-method'], 'memory-allocation-keyword-policy')
    global_elements['memory-allocation-keyword-policy'].text = 'ADDR-METHOD-SHORT-NAME'
    global_elements['section-type'] = ET.SubElement(global_elements['sw-addr-method'], 'section-type')
    global_elements['section-type'].text = 'CODE'

def SwAddrMethods_Copy_SwAddrMethod():
    global_elements['sw-addr-method2'] = ET.SubElement(global_elements['elements18'], 'sw-addr-method')
    global_elements['sw-addr-method2'].attrib = {'UUID': '73ccfb92-d7eb-4aee-b724-b520ed1a3e84'}
    global_elements['short-name126'] = ET.SubElement(global_elements['sw-addr-method2'], 'short-name')
    global_elements['short-name126'].text = 'Copy_SwAddrMethod'
    global_elements['memory-allocation-keyword-policy2'] = ET.SubElement(global_elements['sw-addr-method2'], 'memory-allocation-keyword-policy')
    global_elements['memory-allocation-keyword-policy2'].text = 'ADDR-METHOD-SHORT-NAME-AND-ALIGNMENT'
    global_elements['section-type2'] = ET.SubElement(global_elements['sw-addr-method2'], 'section-type')
    global_elements['section-type2'].text = 'CALIBRATION-VARIABLES'

def SwAddrMethods_SwAddrMethod():
    global_elements['sw-addr-method3'] = ET.SubElement(global_elements['elements18'], 'sw-addr-method')
    global_elements['sw-addr-method3'].attrib = {'UUID': '59a8a159-68d8-4804-8d3b-76f1a5d48b3c'}
    global_elements['short-name127'] = ET.SubElement(global_elements['sw-addr-method3'], 'short-name')
    global_elements['short-name127'].text = 'SwAddrMethod'
    global_elements['memory-allocation-keyword-policy3'] = ET.SubElement(global_elements['sw-addr-method3'], 'memory-allocation-keyword-policy')
    global_elements['memory-allocation-keyword-policy3'].text = 'ADDR-METHOD-SHORT-NAME'
    global_elements['section-type3'] = ET.SubElement(global_elements['sw-addr-method3'], 'section-type')
    global_elements['section-type3'].text = 'CALIBRATION-VARIABLES'

def ApplSWC():
#     global_elements['ar-package21'] = ET.SubElement(global_elements['ar-packages'], 'ar-package')
#     global_elements['short-name128'] = ET.SubElement(global_elements['ar-package21'], 'short-name')
#     global_elements['short-name128'].text = 'SwComponentTypes'
#     global_elements['ar-packages5'] = ET.SubElement(global_elements['ar-package21'], 'ar-packages')

    
    global_elements['ar-package22'] = ET.SubElement(global_elements['ar-packages5'], 'ar-package')
    global_elements['ar-package22'].attrib = {'UUID': '7e1cfec7-fc85-4615-9df0-46ddc1fdaa09'}
    global_elements['short-name129'] = ET.SubElement(global_elements['ar-package22'], 'short-name')
    global_elements['short-name129'].text = 'ApplSWC'
    global_elements['elements19'] = ET.SubElement(global_elements['ar-package22'], 'elements')

def ApplicationSwComponentType():
    global_elements['application-sw-component-type'] = ET.SubElement(global_elements['elements19'], 'application-sw-component-type')
    global_elements['application-sw-component-type'].attrib = {'UUID': 'e74b1e65-d39d-460c-8d4d-d95c8a9e12dd'}
    global_elements['short-name130'] = ET.SubElement(global_elements['application-sw-component-type'], 'short-name')
    global_elements['short-name130'].text = 'ApplicationSwComponentType'
    global_elements['ports'] = ET.SubElement(global_elements['application-sw-component-type'], 'ports')

def RPort_SR():
    global_elements['r-port-prototype'] = ET.SubElement(global_elements['ports'], 'r-port-prototype')
    global_elements['r-port-prototype'].attrib = {'UUID': '1ecadefd-df18-4c05-a2d5-803778e62ae1'}
    global_elements['short-name131'] = ET.SubElement(global_elements['r-port-prototype'], 'short-name')
    global_elements['short-name131'].text = 'RPort_SR'
    global_elements['required-interface-tref'] = ET.SubElement(global_elements['r-port-prototype'], 'required-interface-tref')
    global_elements['required-interface-tref'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface'
    global_elements['required-interface-tref'].attrib = {'DEST': 'SENDER-RECEIVER-INTERFACE'}

def PPort_SR():
    global_elements['p-port-prototype'] = ET.SubElement(global_elements['ports'], 'p-port-prototype')
    global_elements['p-port-prototype'].attrib = {'UUID': 'a3e8969f-1dde-4749-af9a-f337b0f053d8'}
    global_elements['short-name132'] = ET.SubElement(global_elements['p-port-prototype'], 'short-name')
    global_elements['short-name132'].text = 'PPort_SR'
    global_elements['provided-interface-tref'] = ET.SubElement(global_elements['p-port-prototype'], 'provided-interface-tref')
    global_elements['provided-interface-tref'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface'
    global_elements['provided-interface-tref'].attrib = {'DEST': 'SENDER-RECEIVER-INTERFACE'}

def RPort_CS():
    global_elements['r-port-prototype2'] = ET.SubElement(global_elements['ports'], 'r-port-prototype')
    global_elements['r-port-prototype2'].attrib = {'UUID': '933a7736-19ea-4662-8301-3fe9991367bc'}
    global_elements['short-name133'] = ET.SubElement(global_elements['r-port-prototype2'], 'short-name')
    global_elements['short-name133'].text = 'RPort_CS'
    global_elements['required-interface-tref2'] = ET.SubElement(global_elements['r-port-prototype2'], 'required-interface-tref')
    global_elements['required-interface-tref2'].text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface'
    global_elements['required-interface-tref2'].attrib = {'DEST': 'CLIENT-SERVER-INTERFACE'}

def PPort_CS():
    global_elements['p-port-prototype2'] = ET.SubElement(global_elements['ports'], 'p-port-prototype')
    global_elements['p-port-prototype2'].attrib = {'UUID': '38b3145f-1dd8-4a0f-943b-2f6b2d0a4221'}
    global_elements['short-name134'] = ET.SubElement(global_elements['p-port-prototype2'], 'short-name')
    global_elements['short-name134'].text = 'PPort_CS'
    global_elements['provided-interface-tref2'] = ET.SubElement(global_elements['p-port-prototype2'], 'provided-interface-tref')
    global_elements['provided-interface-tref2'].text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface'
    global_elements['provided-interface-tref2'].attrib = {'DEST': 'CLIENT-SERVER-INTERFACE'}

def RPort_msi():
    global_elements['r-port-prototype3'] = ET.SubElement(global_elements['ports'], 'r-port-prototype')
    global_elements['r-port-prototype3'].attrib = {'UUID': '08e53a34-e89a-4c1c-a2d4-9536c0e123af'}
    global_elements['short-name135'] = ET.SubElement(global_elements['r-port-prototype3'], 'short-name')
    global_elements['short-name135'].text = 'RPort_msi'
    global_elements['required-interface-tref3'] = ET.SubElement(global_elements['r-port-prototype3'], 'required-interface-tref')
    global_elements['required-interface-tref3'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface'
    global_elements['required-interface-tref3'].attrib = {'DEST': 'MODE-SWITCH-INTERFACE'}

def PPort_msi():
    global_elements['p-port-prototype3'] = ET.SubElement(global_elements['ports'], 'p-port-prototype')
    global_elements['p-port-prototype3'].attrib = {'UUID': '8ed933c7-270b-45cf-8a3e-206782153f61'}
    global_elements['short-name136'] = ET.SubElement(global_elements['p-port-prototype3'], 'short-name')
    global_elements['short-name136'].text = 'PPort_msi'
    global_elements['provided-interface-tref3'] = ET.SubElement(global_elements['p-port-prototype3'], 'provided-interface-tref')
    global_elements['provided-interface-tref3'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface'
    global_elements['provided-interface-tref3'].attrib = {'DEST': 'MODE-SWITCH-INTERFACE'}

def RPort_nvd():
    global_elements['r-port-prototype4'] = ET.SubElement(global_elements['ports'], 'r-port-prototype')
    global_elements['r-port-prototype4'].attrib = {'UUID': '52c8bb91-6599-4bdd-a556-e2b22ab9c73b'}
    global_elements['short-name137'] = ET.SubElement(global_elements['r-port-prototype4'], 'short-name')
    global_elements['short-name137'].text = 'RPort_nvd'
    global_elements['required-interface-tref4'] = ET.SubElement(global_elements['r-port-prototype4'], 'required-interface-tref')
    global_elements['required-interface-tref4'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface'
    global_elements['required-interface-tref4'].attrib = {'DEST': 'NV-DATA-INTERFACE'}

def PPort_nvd():
    global_elements['p-port-prototype4'] = ET.SubElement(global_elements['ports'], 'p-port-prototype')
    global_elements['p-port-prototype4'].attrib = {'UUID': 'a69f810c-0a9d-4729-9b49-5b4be2f55ffa'}
    global_elements['short-name138'] = ET.SubElement(global_elements['p-port-prototype4'], 'short-name')
    global_elements['short-name138'].text = 'PPort_nvd'
    global_elements['provided-interface-tref4'] = ET.SubElement(global_elements['p-port-prototype4'], 'provided-interface-tref')
    global_elements['provided-interface-tref4'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface'
    global_elements['provided-interface-tref4'].attrib = {'DEST': 'NV-DATA-INTERFACE'}

def RPort_prm():
    global_elements['r-port-prototype5'] = ET.SubElement(global_elements['ports'], 'r-port-prototype')
    global_elements['r-port-prototype5'].attrib = {'UUID': '7bee2832-df48-4712-a0cf-9b2f095db921'}
    global_elements['short-name139'] = ET.SubElement(global_elements['r-port-prototype5'], 'short-name')
    global_elements['short-name139'].text = 'RPort_prm'
    global_elements['required-interface-tref5'] = ET.SubElement(global_elements['r-port-prototype5'], 'required-interface-tref')
    global_elements['required-interface-tref5'].text = '/SharedElements/PortInterfaces/Parameter/ParameterInterface'
    global_elements['required-interface-tref5'].attrib = {'DEST': 'PARAMETER-INTERFACE'}

def RPort_trigger():
    global_elements['r-port-prototype6'] = ET.SubElement(global_elements['ports'], 'r-port-prototype')
    global_elements['r-port-prototype6'].attrib = {'UUID': '9194fa9f-f535-4ef4-ad71-379f00251a5f'}
    global_elements['short-name140'] = ET.SubElement(global_elements['r-port-prototype6'], 'short-name')
    global_elements['short-name140'].text = 'RPort_trigger'
    global_elements['required-interface-tref6'] = ET.SubElement(global_elements['r-port-prototype6'], 'required-interface-tref')
    global_elements['required-interface-tref6'].text = '/SharedElements/PortInterfaces/Trigger/TriggerInterface'
    global_elements['required-interface-tref6'].attrib = {'DEST': 'TRIGGER-INTERFACE'}

def IB_Appl():
    # global_elements['internal-behaviors'] = ET.SubElement(global_elements['application-sw-component-type'], 'internal-behaviors')
    global_elements['swc-internal-behavior'] = ET.SubElement(global_elements['internal-behaviors'], 'swc-internal-behavior')
    global_elements['swc-internal-behavior'].attrib = {'UUID': 'd0c29733-8863-4bcd-af6a-1579e0a29746'}
    global_elements['short-name141'] = ET.SubElement(global_elements['swc-internal-behavior'], 'short-name')
    global_elements['short-name141'].text = 'IB_Appl'
    global_elements['constant-memorys'] = ET.SubElement(global_elements['swc-internal-behavior'], 'constant-memorys')

def ConstantMemory_PDP():
    global_elements['parameter-data-prototype3'] = ET.SubElement(global_elements['constant-memorys'], 'parameter-data-prototype')
    global_elements['parameter-data-prototype3'].attrib = {'UUID': '666c53b0-408c-4084-8002-71810ad2bea7'}
    global_elements['short-name142'] = ET.SubElement(global_elements['parameter-data-prototype3'], 'short-name')
    global_elements['short-name142'].text = 'ConstantMemory'
    global_elements['sw-data-def-props41'] = ET.SubElement(global_elements['parameter-data-prototype3'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants41'] = ET.SubElement(global_elements['sw-data-def-props41'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional41'] = ET.SubElement(global_elements['sw-data-def-props-variants41'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access13'] = ET.SubElement(global_elements['sw-data-def-props-conditional41'], 'sw-calibration-access')
    global_elements['sw-calibration-access13'].text = 'READ-WRITE'
    global_elements['sw-impl-policy28'] = ET.SubElement(global_elements['sw-data-def-props-conditional41'], 'sw-impl-policy')
    global_elements['sw-impl-policy28'].text = 'STANDARD'
    global_elements['type-tref33'] = ET.SubElement(global_elements['parameter-data-prototype3'], 'type-tref')
    global_elements['type-tref33'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint64'
    global_elements['type-tref33'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value'] = ET.SubElement(global_elements['parameter-data-prototype3'], 'init-value')
    global_elements['numerical-value-specification4'] = ET.SubElement(global_elements['init-value'], 'numerical-value-specification')
    global_elements['short-label4'] = ET.SubElement(global_elements['numerical-value-specification4'], 'short-label')
    global_elements['short-label4'].text = 'Value'
    global_elements['value7'] = ET.SubElement(global_elements['numerical-value-specification4'], 'value')
    global_elements['value7'].text = '3'

def DataTypeMappingSet():
    global_elements['data-type-mapping-refs'] = ET.SubElement(global_elements['swc-internal-behavior'], 'data-type-mapping-refs')
    global_elements['data-type-mapping-ref'] = ET.SubElement(global_elements['data-type-mapping-refs'], 'data-type-mapping-ref')
    global_elements['data-type-mapping-ref'].text = '/SharedElements/DataTypemappingSets/DataTypeMappingSet'
    global_elements['data-type-mapping-ref'].attrib = {'DEST': 'DATA-TYPE-MAPPING-SET'}

def StaticMemory():
    global_elements['static-memorys'] = ET.SubElement(global_elements['swc-internal-behavior'], 'static-memorys')
    global_elements['variable-data-prototype15'] = ET.SubElement(global_elements['static-memorys'], 'variable-data-prototype')
    global_elements['variable-data-prototype15'].attrib = {'UUID': '0a83fe83-959c-49d2-abf1-981ac4641b7d'}
    global_elements['short-name143'] = ET.SubElement(global_elements['variable-data-prototype15'], 'short-name')
    global_elements['short-name143'].text = 'StaticMemory'
    global_elements['sw-data-def-props42'] = ET.SubElement(global_elements['variable-data-prototype15'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants42'] = ET.SubElement(global_elements['sw-data-def-props42'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional42'] = ET.SubElement(global_elements['sw-data-def-props-variants42'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy29'] = ET.SubElement(global_elements['sw-data-def-props-conditional42'], 'sw-impl-policy')
    global_elements['sw-impl-policy29'].text = 'STANDARD'
    global_elements['type-tref34'] = ET.SubElement(global_elements['variable-data-prototype15'], 'type-tref')
    global_elements['type-tref34'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref34'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value2'] = ET.SubElement(global_elements['variable-data-prototype15'], 'init-value')
    global_elements['constant-reference'] = ET.SubElement(global_elements['init-value2'], 'constant-reference')
    global_elements['short-label5'] = ET.SubElement(global_elements['constant-reference'], 'short-label')
    global_elements['short-label5'].text = 'ReferenceToConstant'
    global_elements['constant-ref'] = ET.SubElement(global_elements['constant-reference'], 'constant-ref')
    global_elements['constant-ref'].text = '/SharedElements/ConstantSpecifications/ApplicationSwComponentType_StaticMemory'
    global_elements['constant-ref'].attrib = {'DEST': 'CONSTANT-SPECIFICATION'}

def ArTypedPerInstanceMemory():
    global_elements['ar-typed-per-instance-memorys'] = ET.SubElement(global_elements['swc-internal-behavior'], 'ar-typed-per-instance-memorys')
    global_elements['variable-data-prototype16'] = ET.SubElement(global_elements['ar-typed-per-instance-memorys'], 'variable-data-prototype')
    global_elements['variable-data-prototype16'].attrib = {'UUID': 'c2401b62-709c-4a61-a9d7-5f540d144075'}
    global_elements['short-name144'] = ET.SubElement(global_elements['variable-data-prototype16'], 'short-name')
    global_elements['short-name144'].text = 'ArTypedPerInstanceMemory'
    global_elements['sw-data-def-props43'] = ET.SubElement(global_elements['variable-data-prototype16'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants43'] = ET.SubElement(global_elements['sw-data-def-props43'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional43'] = ET.SubElement(global_elements['sw-data-def-props-variants43'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy30'] = ET.SubElement(global_elements['sw-data-def-props-conditional43'], 'sw-impl-policy')
    global_elements['sw-impl-policy30'].text = 'STANDARD'
    global_elements['type-tref35'] = ET.SubElement(global_elements['variable-data-prototype16'], 'type-tref')
    global_elements['type-tref35'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/sint16'
    global_elements['type-tref35'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value3'] = ET.SubElement(global_elements['variable-data-prototype16'], 'init-value')
    global_elements['numerical-value-specification5'] = ET.SubElement(global_elements['init-value3'], 'numerical-value-specification')
    global_elements['short-label6'] = ET.SubElement(global_elements['numerical-value-specification5'], 'short-label')
    global_elements['short-label6'].text = 'Value'
    global_elements['value8'] = ET.SubElement(global_elements['numerical-value-specification5'], 'value')
    global_elements['value8'].text = '-3'


def AsynchronousServerCallReturnsEvent():
    global_elements['events'] = ET.SubElement(global_elements['swc-internal-behavior'], 'events')
    global_elements['asynchronous-server-call-returns-event'] = ET.SubElement(global_elements['events'], 'asynchronous-server-call-returns-event')
    global_elements['asynchronous-server-call-returns-event'].attrib = {'UUID': '98e66756-7475-4549-94ba-bd68dca85e27'}
    global_elements['short-name145'] = ET.SubElement(global_elements['asynchronous-server-call-returns-event'], 'short-name')
    global_elements['short-name145'].text = 'AsynchronousServerCallReturnsEvent'
    global_elements['start-on-event-ref'] = ET.SubElement(global_elements['asynchronous-server-call-returns-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable'
    global_elements['start-on-event-ref'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['event-source-ref'] = ET.SubElement(global_elements['asynchronous-server-call-returns-event'], 'event-source-ref')
    global_elements['event-source-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable/AsynchronousServerCallResultPoint'
    global_elements['event-source-ref'].attrib = {'DEST': 'ASYNCHRONOUS-SERVER-CALL-RESULT-POINT'}

def BackgroundEvent():
    global_elements['background-event'] = ET.SubElement(global_elements['events'], 'background-event')
    global_elements['background-event'].attrib = {'UUID': '878975ea-f390-4f62-a34f-05ca7fd73896'}
    global_elements['short-name146'] = ET.SubElement(global_elements['background-event'], 'short-name')
    global_elements['short-name146'].text = 'BackgroundEvent'
    global_elements['start-on-event-ref2'] = ET.SubElement(global_elements['background-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable1'
    global_elements['start-on-event-ref2'].attrib = {'DEST': 'RUNNABLE-ENTITY'}

def DataReceiveErrorEvent():
    global_elements['data-receive-error-event'] = ET.SubElement(global_elements['events'], 'data-receive-error-event')
    global_elements['data-receive-error-event'].attrib = {'UUID': '733de305-2dc6-4ac2-be25-134d242372ad'}
    global_elements['short-name147'] = ET.SubElement(global_elements['data-receive-error-event'], 'short-name')
    global_elements['short-name147'].text = 'DataReceiveErrorEvent'
    global_elements['start-on-event-ref3'] = ET.SubElement(global_elements['data-receive-error-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref3'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable2'
    global_elements['start-on-event-ref3'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['data-iref'] = ET.SubElement(global_elements['data-receive-error-event'], 'data-iref')
    global_elements['context-r-port-ref'] = ET.SubElement(global_elements['data-iref'], 'context-r-port-ref')
    global_elements['context-r-port-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    global_elements['context-r-port-ref'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-element-ref'] = ET.SubElement(global_elements['data-iref'], 'target-data-element-ref')
    global_elements['target-data-element-ref'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    global_elements['target-data-element-ref'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def DataReceivedEvent():
    global_elements['data-received-event'] = ET.SubElement(global_elements['events'], 'data-received-event')
    global_elements['data-received-event'].attrib = {'UUID': '30fc9c83-5302-44fc-a25d-0d77e2b3d112'}
    global_elements['short-name148'] = ET.SubElement(global_elements['data-received-event'], 'short-name')
    global_elements['short-name148'].text = 'DataReceivedEvent'
    global_elements['start-on-event-ref4'] = ET.SubElement(global_elements['data-received-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref4'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable3'
    global_elements['start-on-event-ref4'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['data-iref2'] = ET.SubElement(global_elements['data-received-event'], 'data-iref')
    global_elements['context-r-port-ref2'] = ET.SubElement(global_elements['data-iref2'], 'context-r-port-ref')
    global_elements['context-r-port-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    global_elements['context-r-port-ref2'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-element-ref2'] = ET.SubElement(global_elements['data-iref2'], 'target-data-element-ref')
    global_elements['target-data-element-ref2'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    global_elements['target-data-element-ref2'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def DataSendCompletedEvent():
    global_elements['data-send-completed-event'] = ET.SubElement(global_elements['events'], 'data-send-completed-event')
    global_elements['data-send-completed-event'].attrib = {'UUID': 'aefde323-2cf9-4226-aedb-0a1a33876a55'}
    global_elements['short-name149'] = ET.SubElement(global_elements['data-send-completed-event'], 'short-name')
    global_elements['short-name149'].text = 'DataSendCompletedEvent'
    global_elements['start-on-event-ref5'] = ET.SubElement(global_elements['data-send-completed-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref5'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable4'
    global_elements['start-on-event-ref5'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['event-source-ref2'] = ET.SubElement(global_elements['data-send-completed-event'], 'event-source-ref')
    global_elements['event-source-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable4/DSP_PPort_SR_DataElement'
    global_elements['event-source-ref2'].attrib = {'DEST': 'VARIABLE-ACCESS'}

def DataWriteCompletedEvent():
    global_elements['data-write-completed-event'] = ET.SubElement(global_elements['events'], 'data-write-completed-event')
    global_elements['data-write-completed-event'].attrib = {'UUID': '0da70404-5ab6-4651-ad56-e1c3adab06e5'}
    global_elements['short-name150'] = ET.SubElement(global_elements['data-write-completed-event'], 'short-name')
    global_elements['short-name150'].text = 'DataWriteCompletedEvent'
    global_elements['start-on-event-ref6'] = ET.SubElement(global_elements['data-write-completed-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref6'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable5'
    global_elements['start-on-event-ref6'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['event-source-ref3'] = ET.SubElement(global_elements['data-write-completed-event'], 'event-source-ref')
    global_elements['event-source-ref3'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable5/DWA_PPort_SR_DataElement1'
    global_elements['event-source-ref3'].attrib = {'DEST': 'VARIABLE-ACCESS'}

def ExternalTriggerOccurredEvent():
    global_elements['external-trigger-occurred-event'] = ET.SubElement(global_elements['events'], 'external-trigger-occurred-event')
    global_elements['external-trigger-occurred-event'].attrib = {'UUID': '7f122189-5a69-4e28-af84-b5a1e73c9206'}
    global_elements['short-name151'] = ET.SubElement(global_elements['external-trigger-occurred-event'], 'short-name')
    global_elements['short-name151'].text = 'ExternalTriggerOccurredEvent'
    global_elements['start-on-event-ref7'] = ET.SubElement(global_elements['external-trigger-occurred-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref7'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable6'
    global_elements['start-on-event-ref7'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['trigger-iref'] = ET.SubElement(global_elements['external-trigger-occurred-event'], 'trigger-iref')
    global_elements['context-r-port-ref3'] = ET.SubElement(global_elements['trigger-iref'], 'context-r-port-ref')
    global_elements['context-r-port-ref3'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_trigger'
    global_elements['context-r-port-ref3'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-trigger-ref'] = ET.SubElement(global_elements['trigger-iref'], 'target-trigger-ref')
    global_elements['target-trigger-ref'].text = '/SharedElements/PortInterfaces/Trigger/TriggerInterface/Trigger'
    global_elements['target-trigger-ref'].attrib = {'DEST': 'TRIGGER'}

def InitEvent():
    global_elements['init-event'] = ET.SubElement(global_elements['events'], 'init-event')
    global_elements['init-event'].attrib = {'UUID': '6febdb10-eefc-44b9-adad-fdef91bbef72'}
    global_elements['short-name498'] = ET.SubElement(global_elements['init-event'], 'short-name')
    global_elements['short-name498'].text = 'InitEvent'
    global_elements['start-on-event-ref8'] = ET.SubElement(global_elements['init-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref8'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable7'
    global_elements['start-on-event-ref8'].attrib = {'DEST': 'RUNNABLE-ENTITY'}

def ModeSwitchedAckEvent():
    global_elements['mode-switched-ack-event'] = ET.SubElement(global_elements['events'], 'mode-switched-ack-event')
    global_elements['mode-switched-ack-event'].attrib = {'UUID': '2f5c24be-60cf-4249-bfde-ceabef6d00d4'}
    global_elements['short-name152'] = ET.SubElement(global_elements['mode-switched-ack-event'], 'short-name')
    global_elements['short-name152'].text = 'ModeSwitchedAckEvent'
    global_elements['start-on-event-ref8'] = ET.SubElement(global_elements['mode-switched-ack-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref8'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable9'
    global_elements['start-on-event-ref8'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['event-source-ref4'] = ET.SubElement(global_elements['mode-switched-ack-event'], 'event-source-ref')
    global_elements['event-source-ref4'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable9/MSP_PPort_msi_ModeGroup'
    global_elements['event-source-ref4'].attrib = {'DEST': 'MODE-SWITCH-POINT'}

def OperationInvokedEvent():
    global_elements['operation-invoked-event'] = ET.SubElement(global_elements['events'], 'operation-invoked-event')
    global_elements['operation-invoked-event'].attrib = {'UUID': '02646a86-1109-43a4-8e09-cb8878e932a5'}
    global_elements['short-name153'] = ET.SubElement(global_elements['operation-invoked-event'], 'short-name')
    global_elements['short-name153'].text = 'OperationInvokedEvent'
    global_elements['start-on-event-ref9'] = ET.SubElement(global_elements['operation-invoked-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref9'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable10'
    global_elements['start-on-event-ref9'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['operation-iref'] = ET.SubElement(global_elements['operation-invoked-event'], 'operation-iref')
    global_elements['context-p-port-ref'] = ET.SubElement(global_elements['operation-iref'], 'context-p-port-ref')
    global_elements['context-p-port-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_CS'
    global_elements['context-p-port-ref'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-provided-operation-ref'] = ET.SubElement(global_elements['operation-iref'], 'target-provided-operation-ref')
    global_elements['target-provided-operation-ref'].text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface/Operation1'
    global_elements['target-provided-operation-ref'].attrib = {'DEST': 'CLIENT-SERVER-OPERATION'}

def SwcModeManagerErrorEvent():
    global_elements['swc-mode-manager-error-event'] = ET.SubElement(global_elements['events'], 'swc-mode-manager-error-event')
    global_elements['swc-mode-manager-error-event'].attrib = {'UUID': '2e3337be-0df8-4dce-a65a-ca8bb234754a'}
    global_elements['short-name501'] = ET.SubElement(global_elements['swc-mode-manager-error-event'], 'short-name')
    global_elements['short-name501'].text = 'SwcModeManagerErrorEvent'
    global_elements['start-on-event-ref11'] = ET.SubElement(global_elements['swc-mode-manager-error-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref11'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable11'
    global_elements['start-on-event-ref11'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['mode-group-iref'] = ET.SubElement(global_elements['swc-mode-manager-error-event'], 'mode-group-iref')
    global_elements['context-p-port-ref2'] = ET.SubElement(global_elements['mode-group-iref'], 'context-p-port-ref')
    global_elements['context-p-port-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_msi'
    global_elements['context-p-port-ref2'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-mode-group-ref'] = ET.SubElement(global_elements['mode-group-iref'], 'target-mode-group-ref')
    global_elements['target-mode-group-ref'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
    global_elements['target-mode-group-ref'].attrib = {'DEST': 'MODE-DECLARATION-GROUP-PROTOTYPE'}

def SwcModeSwitchEvent():
    global_elements['swc-mode-switch-event'] = ET.SubElement(global_elements['events'], 'swc-mode-switch-event')
    global_elements['swc-mode-switch-event'].attrib = {'UUID': '5bebf915-dc23-4d8d-ac15-4af9a83cb9f1'}
    global_elements['short-name154'] = ET.SubElement(global_elements['swc-mode-switch-event'], 'short-name')
    global_elements['short-name154'].text = 'SwcModeSwitchEvent'
    global_elements['start-on-event-ref10'] = ET.SubElement(global_elements['swc-mode-switch-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref10'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable12'
    global_elements['start-on-event-ref10'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['activation'] = ET.SubElement(global_elements['swc-mode-switch-event'], 'activation')
    global_elements['activation'].text = 'ON-TRANSITION'
    global_elements['mode-irefs'] = ET.SubElement(global_elements['swc-mode-switch-event'], 'mode-irefs')
    global_elements['mode-iref'] = ET.SubElement(global_elements['mode-irefs'], 'mode-iref')
    global_elements['context-port-ref'] = ET.SubElement(global_elements['mode-iref'], 'context-port-ref')
    global_elements['context-port-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_msi'
    global_elements['context-port-ref'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['context-mode-declaration-group-prototype-ref'] = ET.SubElement(global_elements['mode-iref'], 'context-mode-declaration-group-prototype-ref')
    global_elements['context-mode-declaration-group-prototype-ref'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
    global_elements['context-mode-declaration-group-prototype-ref'].attrib = {'DEST': 'MODE-DECLARATION-GROUP-PROTOTYPE'}
    global_elements['target-mode-declaration-ref'] = ET.SubElement(global_elements['mode-iref'], 'target-mode-declaration-ref')
    global_elements['target-mode-declaration-ref'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeDeclarationGroup/ModeDeclaration2'
    global_elements['target-mode-declaration-ref'].attrib = {'DEST': 'MODE-DECLARATION'}
    global_elements['mode-iref2'] = ET.SubElement(global_elements['mode-irefs'], 'mode-iref')
    global_elements['context-port-ref2'] = ET.SubElement(global_elements['mode-iref2'], 'context-port-ref')
    global_elements['context-port-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_msi'
    global_elements['context-port-ref2'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['context-mode-declaration-group-prototype-ref2'] = ET.SubElement(global_elements['mode-iref2'], 'context-mode-declaration-group-prototype-ref')
    global_elements['context-mode-declaration-group-prototype-ref2'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
    global_elements['context-mode-declaration-group-prototype-ref2'].attrib = {'DEST': 'MODE-DECLARATION-GROUP-PROTOTYPE'}
    global_elements['target-mode-declaration-ref2'] = ET.SubElement(global_elements['mode-iref2'], 'target-mode-declaration-ref')
    global_elements['target-mode-declaration-ref2'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeDeclarationGroup/ModeDeclaration'
    global_elements['target-mode-declaration-ref2'].attrib = {'DEST': 'MODE-DECLARATION'}

def TimingEvent():
    global_elements['timing-event'] = ET.SubElement(global_elements['events'], 'timing-event')
    global_elements['timing-event'].attrib = {'UUID': 'a761b6cb-cd31-4a99-b2f8-21c5a132097e'}
    global_elements['short-name155'] = ET.SubElement(global_elements['timing-event'], 'short-name')
    global_elements['short-name155'].text = 'TimingEvent'
    global_elements['start-on-event-ref11'] = ET.SubElement(global_elements['timing-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref11'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable13'
    global_elements['start-on-event-ref11'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['period'] = ET.SubElement(global_elements['timing-event'], 'period')
    global_elements['period'].text = '0.01'

def TransformerHardErrorEvent():
    transformer_hard_error_event1 = ET.SubElement(events1, 'TRANSFORMER-HARD-ERROR-EVENT')
    transformer_hard_error_event1.attrib = {'UUID': '0cb20425-8704-4215-9df9-3cc6aa1d60c1'}
    short_name158 = ET.SubElement(transformer_hard_error_event1, 'SHORT-NAME')
    short_name158.text = 'TransformerHardErrorEvent'
    start_on_event_ref14 = ET.SubElement(transformer_hard_error_event1, 'START-ON-EVENT-REF')
    start_on_event_ref14.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable14'
    start_on_event_ref14.attrib = {'DEST': 'RUNNABLE-ENTITY'}

def TimingEvent1():
    global_elements['timing-event2'] = ET.SubElement(global_elements['events'], 'timing-event')
    global_elements['timing-event2'].attrib = {'UUID': '0faaa505-7947-4b84-b8ea-4086fa60a54c'}
    global_elements['short-name156'] = ET.SubElement(global_elements['timing-event2'], 'short-name')
    global_elements['short-name156'].text = 'TimingEvent1'
    global_elements['start-on-event-ref12'] = ET.SubElement(global_elements['timing-event2'], 'start-on-event-ref')
    global_elements['start-on-event-ref12'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable15'
    global_elements['start-on-event-ref12'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['period2'] = ET.SubElement(global_elements['timing-event2'], 'period')
    global_elements['period2'].text = '0.01'

def ExplicitInterRunnableVariable():
    global_elements['explicit-inter-runnable-variables'] = ET.SubElement(global_elements['swc-internal-behavior'], 'explicit-inter-runnable-variables')
    global_elements['variable-data-prototype17'] = ET.SubElement(global_elements['explicit-inter-runnable-variables'], 'variable-data-prototype')
    global_elements['variable-data-prototype17'].attrib = {'UUID': '46bf0c15-16f3-428f-92de-ce374a9faf1c'}
    global_elements['short-name157'] = ET.SubElement(global_elements['variable-data-prototype17'], 'short-name')
    global_elements['short-name157'].text = 'ExplicitInterRunnableVariable'
    global_elements['sw-data-def-props44'] = ET.SubElement(global_elements['variable-data-prototype17'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants44'] = ET.SubElement(global_elements['sw-data-def-props44'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional44'] = ET.SubElement(global_elements['sw-data-def-props-variants44'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy31'] = ET.SubElement(global_elements['sw-data-def-props-conditional44'], 'sw-impl-policy')
    global_elements['sw-impl-policy31'].text = 'STANDARD'
    global_elements['type-tref36'] = ET.SubElement(global_elements['variable-data-prototype17'], 'type-tref')
    global_elements['type-tref36'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    global_elements['type-tref36'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value4'] = ET.SubElement(global_elements['variable-data-prototype17'], 'init-value')
    global_elements['constant-reference2'] = ET.SubElement(global_elements['init-value4'], 'constant-reference')
    global_elements['short-label7'] = ET.SubElement(global_elements['constant-reference2'], 'short-label')
    global_elements['short-label7'].text = 'ReferenceToConstant'
    global_elements['constant-ref2'] = ET.SubElement(global_elements['constant-reference2'], 'constant-ref')
    global_elements['constant-ref2'].text = '/SharedElements/ConstantSpecifications/ApplicationSwComponentType_ExplicitInterRunnableVariable'
    global_elements['constant-ref2'].attrib = {'DEST': 'CONSTANT-SPECIFICATION'}

# def NoSupport():
#     global_elements['handle-termination-and-restart'] = ET.SubElement(global_elements['swc-internal-behavior'], 'handle-termination-and-restart')
#     global_elements['handle-termination-and-restart'].text = 'NO-SUPPORT'


def ImplicitInterRunnableVariable():
    global_elements['implicit-inter-runnable-variables'] = ET.SubElement(global_elements['swc-internal-behavior'], 'implicit-inter-runnable-variables')
    global_elements['variable-data-prototype18'] = ET.SubElement(global_elements['implicit-inter-runnable-variables'], 'variable-data-prototype')
    global_elements['variable-data-prototype18'].attrib = {'UUID': '100df329-69ca-4527-945c-b23a59017964'}
    global_elements['short-name158'] = ET.SubElement(global_elements['variable-data-prototype18'], 'short-name')
    global_elements['short-name158'].text = 'ImplicitInterRunnableVariable'
    global_elements['sw-data-def-props45'] = ET.SubElement(global_elements['variable-data-prototype18'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants45'] = ET.SubElement(global_elements['sw-data-def-props45'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional45'] = ET.SubElement(global_elements['sw-data-def-props-variants45'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy32'] = ET.SubElement(global_elements['sw-data-def-props-conditional45'], 'sw-impl-policy')
    global_elements['sw-impl-policy32'].text = 'STANDARD'
    global_elements['type-tref37'] = ET.SubElement(global_elements['variable-data-prototype18'], 'type-tref')
    global_elements['type-tref37'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/sint16'
    global_elements['type-tref37'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value5'] = ET.SubElement(global_elements['variable-data-prototype18'], 'init-value')
    global_elements['numerical-value-specification6'] = ET.SubElement(global_elements['init-value5'], 'numerical-value-specification')
    global_elements['short-label8'] = ET.SubElement(global_elements['numerical-value-specification6'], 'short-label')
    global_elements['short-label8'].text = 'Value'
    global_elements['value9'] = ET.SubElement(global_elements['numerical-value-specification6'], 'value')
    global_elements['value9'].text = '0'

def PerInstanceParameter():
    global_elements['per-instance-parameters'] = ET.SubElement(global_elements['swc-internal-behavior'], 'per-instance-parameters')
    global_elements['parameter-data-prototype4'] = ET.SubElement(global_elements['per-instance-parameters'], 'parameter-data-prototype')
    global_elements['parameter-data-prototype4'].attrib = {'UUID': 'a2509010-a816-4ea4-b0ed-c5ba10c3ca78'}
    global_elements['short-name159'] = ET.SubElement(global_elements['parameter-data-prototype4'], 'short-name')
    global_elements['short-name159'].text = 'PerInstanceParameter'
    global_elements['sw-data-def-props46'] = ET.SubElement(global_elements['parameter-data-prototype4'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants46'] = ET.SubElement(global_elements['sw-data-def-props46'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional46'] = ET.SubElement(global_elements['sw-data-def-props-variants46'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access14'] = ET.SubElement(global_elements['sw-data-def-props-conditional46'], 'sw-calibration-access')
    global_elements['sw-calibration-access14'].text = 'READ-WRITE'
    global_elements['sw-impl-policy33'] = ET.SubElement(global_elements['sw-data-def-props-conditional46'], 'sw-impl-policy')
    global_elements['sw-impl-policy33'].text = 'STANDARD'
    global_elements['type-tref38'] = ET.SubElement(global_elements['parameter-data-prototype4'], 'type-tref')
    global_elements['type-tref38'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref38'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value6'] = ET.SubElement(global_elements['parameter-data-prototype4'], 'init-value')
    global_elements['numerical-value-specification7'] = ET.SubElement(global_elements['init-value6'], 'numerical-value-specification')
    global_elements['short-label9'] = ET.SubElement(global_elements['numerical-value-specification7'], 'short-label')
    global_elements['short-label9'].text = 'Value'
    global_elements['value10'] = ET.SubElement(global_elements['numerical-value-specification7'], 'value')
    global_elements['value10'].text = '5'
  
def Runnable():
    global_elements['runnables'] = ET.SubElement(global_elements['swc-internal-behavior'], 'runnables')
    global_elements['runnable-entity'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity'].attrib = {'UUID': 'bfb2d01b-9082-4a58-a929-6d7a860a2d9a'}
    global_elements['short-name160'] = ET.SubElement(global_elements['runnable-entity'], 'short-name')
    global_elements['short-name160'].text = 'Runnable'
    global_elements['minimum-start-interval'] = ET.SubElement(global_elements['runnable-entity'], 'minimum-start-interval')
    global_elements['minimum-start-interval'].text = '0'
    global_elements['sw-addr-method-ref'] = ET.SubElement(global_elements['runnable-entity'], 'sw-addr-method-ref')
    global_elements['sw-addr-method-ref'].text = '/SharedElements/SwAddrMethods/Copy2_SwAddrMethod'
    global_elements['sw-addr-method-ref'].attrib = {'DEST': 'SW-ADDR-METHOD'}

def AsynchronousServerCallResultPoint():
    global_elements['asynchronous-server-call-result-points'] = ET.SubElement(global_elements['runnable-entity'], 'asynchronous-server-call-result-points')
    global_elements['asynchronous-server-call-result-point'] = ET.SubElement(global_elements['asynchronous-server-call-result-points'], 'asynchronous-server-call-result-point')
    global_elements['asynchronous-server-call-result-point'].attrib = {'UUID': 'f857d505-3c25-43b2-b929-36e0e40f1177'}
    global_elements['short-name161'] = ET.SubElement(global_elements['asynchronous-server-call-result-point'], 'short-name')
    global_elements['short-name161'].text = 'AsynchronousServerCallResultPoint'
    global_elements['asynchronous-server-call-point-ref'] = ET.SubElement(global_elements['asynchronous-server-call-result-point'], 'asynchronous-server-call-point-ref')
    global_elements['asynchronous-server-call-point-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable/ASCP_RPort_CS_Operation'
    global_elements['asynchronous-server-call-point-ref'].attrib = {'DEST': 'ASYNCHRONOUS-SERVER-CALL-POINT'}


def ASCP_RPort_CS_Operation():
    global_elements['asynchronous-server-call-point'] = ET.SubElement(global_elements['server-call-points'], 'asynchronous-server-call-point')
    global_elements['asynchronous-server-call-point'].attrib = {'UUID': 'e7aacef3-56e7-4964-b0b6-5569dd4abc09'}
    global_elements['short-name162'] = ET.SubElement(global_elements['asynchronous-server-call-point'], 'short-name')
    global_elements['short-name162'].text = 'ASCP_RPort_CS_Operation'
    global_elements['operation-iref2'] = ET.SubElement(global_elements['asynchronous-server-call-point'], 'operation-iref')
    global_elements['context-r-port-ref4'] = ET.SubElement(global_elements['operation-iref2'], 'context-r-port-ref')
    global_elements['context-r-port-ref4'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_CS'
    global_elements['context-r-port-ref4'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-required-operation-ref'] = ET.SubElement(global_elements['operation-iref2'], 'target-required-operation-ref')
    global_elements['target-required-operation-ref'].text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface/Operation'
    global_elements['target-required-operation-ref'].attrib = {'DEST': 'CLIENT-SERVER-OPERATION'}
    global_elements['timeout'] = ET.SubElement(global_elements['asynchronous-server-call-point'], 'timeout')
    global_elements['timeout'].text = '0'
    global_elements['symbol9'] = ET.SubElement(global_elements['runnable-entity'], 'symbol')
    global_elements['symbol9'].text = 'ApplicationSwComponentType_Runnable'  
  
  
def ApplicationSwComponentType_Runnable1():
    global_elements['runnable-entity2'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity2'].attrib = {'UUID': '4a40f3ec-f4dd-4ab0-8562-6a5174f2901e'}
    global_elements['short-name163'] = ET.SubElement(global_elements['runnable-entity2'], 'short-name')
    global_elements['short-name163'].text = 'Runnable1'
    global_elements['minimum-start-interval2'] = ET.SubElement(global_elements['runnable-entity2'], 'minimum-start-interval')
    global_elements['minimum-start-interval2'].text = '0'
    global_elements['can-be-invoked-concurrently2'] = ET.SubElement(global_elements['runnable-entity2'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently2'].text = 'false'
    global_elements['symbol10'] = ET.SubElement(global_elements['runnable-entity2'], 'symbol')
    global_elements['symbol10'].text = 'ApplicationSwComponentType_Runnable1'

def ApplicationSwComponentType_Runnable2():
    global_elements['runnable-entity3'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity3'].attrib = {'UUID': '83eca00a-85d5-4f04-9573-3d997cd29b67'}
    global_elements['short-name164'] = ET.SubElement(global_elements['runnable-entity3'], 'short-name')
    global_elements['short-name164'].text = 'Runnable2'
    global_elements['minimum-start-interval3'] = ET.SubElement(global_elements['runnable-entity3'], 'minimum-start-interval')
    global_elements['minimum-start-interval3'].text = '0'
    global_elements['can-be-invoked-concurrently3'] = ET.SubElement(global_elements['runnable-entity3'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently3'].text = 'false'
    global_elements['symbol11'] = ET.SubElement(global_elements['runnable-entity3'], 'symbol')
    global_elements['symbol11'].text = 'ApplicationSwComponentType_Runnable2'

def ApplicationSwComponentType_Runnable3():
    global_elements['runnable-entity4'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity4'].attrib = {'UUID': '20bfd5e2-a118-4324-97fd-dcd5bf5f0a46'}
    global_elements['short-name165'] = ET.SubElement(global_elements['runnable-entity4'], 'short-name')
    global_elements['short-name165'].text = 'Runnable3'
    global_elements['minimum-start-interval4'] = ET.SubElement(global_elements['runnable-entity4'], 'minimum-start-interval')
    global_elements['minimum-start-interval4'].text = '0'
    global_elements['can-be-invoked-concurrently4'] = ET.SubElement(global_elements['runnable-entity4'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently4'].text = 'false'
    global_elements['symbol12'] = ET.SubElement(global_elements['runnable-entity4'], 'symbol')
    global_elements['symbol12'].text = 'ApplicationSwComponentType_Runnable3'

def ApplicationSwComponentType_Runnable4():
    global_elements['runnable-entity5'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity5'].attrib = {'UUID': 'ae315d13-a18a-4515-b02d-f1b207f85e47'}
    global_elements['short-name166'] = ET.SubElement(global_elements['runnable-entity5'], 'short-name')
    global_elements['short-name166'].text = 'Runnable4'
    global_elements['minimum-start-interval5'] = ET.SubElement(global_elements['runnable-entity5'], 'minimum-start-interval')
    global_elements['minimum-start-interval5'].text = '0'
    global_elements['can-be-invoked-concurrently5'] = ET.SubElement(global_elements['runnable-entity5'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently5'].text = 'false'

def DSP_PPort_SR_DataElement():
    global_elements['data-send-points'] = ET.SubElement(global_elements['runnable-entity5'], 'data-send-points')
    global_elements['variable-access'] = ET.SubElement(global_elements['data-send-points'], 'variable-access')
    global_elements['variable-access'].attrib = {'UUID': '2a04aecc-a1b6-494f-838e-29671adb5210'}
    global_elements['short-name167'] = ET.SubElement(global_elements['variable-access'], 'short-name')
    global_elements['short-name167'].text = 'DSP_PPort_SR_DataElement'
    global_elements['accessed-variable'] = ET.SubElement(global_elements['variable-access'], 'accessed-variable')
    global_elements['autosar-variable-iref'] = ET.SubElement(global_elements['accessed-variable'], 'autosar-variable-iref')
    global_elements['port-prototype-ref'] = ET.SubElement(global_elements['autosar-variable-iref'], 'port-prototype-ref')
    global_elements['port-prototype-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    global_elements['port-prototype-ref'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref'] = ET.SubElement(global_elements['autosar-variable-iref'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    global_elements['target-data-prototype-ref'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['symbol13'] = ET.SubElement(global_elements['runnable-entity5'], 'symbol')
    global_elements['symbol13'].text = 'ApplicationSwComponentType_Runnable4'

def ApplicationSwComponentType_Runnable5():
    global_elements['runnable-entity6'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity6'].attrib = {'UUID': '3ea0641c-9d79-4f93-8287-e34956b5c134'}
    global_elements['short-name168'] = ET.SubElement(global_elements['runnable-entity6'], 'short-name')
    global_elements['short-name168'].text = 'Runnable5'
    global_elements['minimum-start-interval6'] = ET.SubElement(global_elements['runnable-entity6'], 'minimum-start-interval')
    global_elements['minimum-start-interval6'].text = '0'
    global_elements['can-be-invoked-concurrently6'] = ET.SubElement(global_elements['runnable-entity6'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently6'].text = 'false'

def DWA_PPort_SR_DataElement1():
    global_elements['data-write-accesss'] = ET.SubElement(global_elements['runnable-entity6'], 'data-write-accesss')
    global_elements['variable-access2'] = ET.SubElement(global_elements['data-write-accesss'], 'variable-access')
    global_elements['variable-access2'].attrib = {'UUID': '326a474d-8d28-41bc-bd9e-91de9802f682'}
    global_elements['short-name169'] = ET.SubElement(global_elements['variable-access2'], 'short-name')
    global_elements['short-name169'].text = 'DWA_PPort_SR_DataElement1'
    global_elements['accessed-variable2'] = ET.SubElement(global_elements['variable-access2'], 'accessed-variable')
    global_elements['autosar-variable-iref2'] = ET.SubElement(global_elements['accessed-variable2'], 'autosar-variable-iref')
    global_elements['port-prototype-ref2'] = ET.SubElement(global_elements['autosar-variable-iref2'], 'port-prototype-ref')
    global_elements['port-prototype-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    global_elements['port-prototype-ref2'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref2'] = ET.SubElement(global_elements['autosar-variable-iref2'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref2'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    global_elements['target-data-prototype-ref2'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['symbol14'] = ET.SubElement(global_elements['runnable-entity6'], 'symbol')
    global_elements['symbol14'].text = 'ApplicationSwComponentType_Runnable5'
  
def ApplicationSwComponentType_Runnable6():
    global_elements['runnable-entity7'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity7'].attrib = {'UUID': 'd7adad0b-22d1-4b37-9691-0677036197aa'}
    global_elements['short-name170'] = ET.SubElement(global_elements['runnable-entity7'], 'short-name')
    global_elements['short-name170'].text = 'Runnable6'
    global_elements['minimum-start-interval7'] = ET.SubElement(global_elements['runnable-entity7'], 'minimum-start-interval')
    global_elements['minimum-start-interval7'].text = '0'
    global_elements['can-be-invoked-concurrently7'] = ET.SubElement(global_elements['runnable-entity7'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently7'].text = 'false'
    global_elements['symbol15'] = ET.SubElement(global_elements['runnable-entity7'], 'symbol')
    global_elements['symbol15'].text = 'ApplicationSwComponentType_Runnable6'

def ApplicationSwComponentType_Runnable7():
    global_elements['runnable-entity8'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity8'].attrib = {'UUID': '98d30ebd-bbcb-4780-bc4a-27e6fd798a5a'}
    global_elements['short-name171'] = ET.SubElement(global_elements['runnable-entity8'], 'short-name')
    global_elements['short-name171'].text = 'Runnable7'
    global_elements['minimum-start-interval8'] = ET.SubElement(global_elements['runnable-entity8'], 'minimum-start-interval')
    global_elements['minimum-start-interval8'].text = '0'
    global_elements['can-be-invoked-concurrently8'] = ET.SubElement(global_elements['runnable-entity8'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently8'].text = 'false'
    global_elements['symbol16'] = ET.SubElement(global_elements['runnable-entity8'], 'symbol')
    global_elements['symbol16'].text = 'ApplicationSwComponentType_Runnable7'

def ApplicationSwComponentType_Runnable9():
    global_elements['runnable-entity9'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity9'].attrib = {'UUID': 'a6d9d7cb-1d57-45f2-b36a-1e1ab717fb1e'}
    global_elements['short-name172'] = ET.SubElement(global_elements['runnable-entity9'], 'short-name')
    global_elements['short-name172'].text = 'Runnable9'
    global_elements['minimum-start-interval9'] = ET.SubElement(global_elements['runnable-entity9'], 'minimum-start-interval')
    global_elements['minimum-start-interval9'].text = '0'
    global_elements['can-be-invoked-concurrently9'] = ET.SubElement(global_elements['runnable-entity9'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently9'].text = 'false'

def MSP_PPort_msi_ModeGroup():
    global_elements['mode-switch-points'] = ET.SubElement(global_elements['runnable-entity9'], 'mode-switch-points')
    global_elements['mode-switch-point'] = ET.SubElement(global_elements['mode-switch-points'], 'mode-switch-point')
    global_elements['mode-switch-point'].attrib = {'UUID': 'dd700e44-3e29-4b21-901f-c2e36c719f6a'}
    global_elements['short-name173'] = ET.SubElement(global_elements['mode-switch-point'], 'short-name')
    global_elements['short-name173'].text = 'MSP_PPort_msi_ModeGroup'
    global_elements['mode-group-iref'] = ET.SubElement(global_elements['mode-switch-point'], 'mode-group-iref')
    global_elements['context-p-port-ref2'] = ET.SubElement(global_elements['mode-group-iref'], 'context-p-port-ref')
    global_elements['context-p-port-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_msi'
    global_elements['context-p-port-ref2'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-mode-group-ref'] = ET.SubElement(global_elements['mode-group-iref'], 'target-mode-group-ref')
    global_elements['target-mode-group-ref'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
    global_elements['target-mode-group-ref'].attrib = {'DEST': 'MODE-DECLARATION-GROUP-PROTOTYPE'}
    global_elements['symbol17'] = ET.SubElement(global_elements['runnable-entity9'], 'symbol')
    global_elements['symbol17'].text = 'ApplicationSwComponentType_Runnable9'

def ApplicationSwComponentType_Runnable10():
    global_elements['runnable-entity10'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity10'].attrib = {'UUID': '3d515ac9-9c51-4cb8-a6af-ea16d3afd01d'}
    global_elements['short-name174'] = ET.SubElement(global_elements['runnable-entity10'], 'short-name')
    global_elements['short-name174'].text = 'Runnable10'
    global_elements['minimum-start-interval10'] = ET.SubElement(global_elements['runnable-entity10'], 'minimum-start-interval')
    global_elements['minimum-start-interval10'].text = '0'
    global_elements['can-be-invoked-concurrently10'] = ET.SubElement(global_elements['runnable-entity10'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently10'].text = 'false'
    global_elements['symbol18'] = ET.SubElement(global_elements['runnable-entity10'], 'symbol')
    global_elements['symbol18'].text = 'ApplicationSwComponentType_Runnable10'

def ApplicationSwComponentType_Runnable11():
    global_elements['runnable-entity11'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity11'].attrib = {'UUID': '9bddd887-575d-463b-b09d-d1b63ec1352b'}
    global_elements['short-name175'] = ET.SubElement(global_elements['runnable-entity11'], 'short-name')
    global_elements['short-name175'].text = 'Runnable11'
    global_elements['minimum-start-interval11'] = ET.SubElement(global_elements['runnable-entity11'], 'minimum-start-interval')
    global_elements['minimum-start-interval11'].text = '0'
    global_elements['can-be-invoked-concurrently11'] = ET.SubElement(global_elements['runnable-entity11'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently11'].text = 'false'
    global_elements['symbol19'] = ET.SubElement(global_elements['runnable-entity11'], 'symbol')
    global_elements['symbol19'].text = 'ApplicationSwComponentType_Runnable11'

def ApplicationSwComponentType_Runnable12():
    global_elements['runnable-entity12'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity12'].attrib = {'UUID': 'fa96688f-7ffe-4b3b-aa43-c124847e2efd'}
    global_elements['short-name176'] = ET.SubElement(global_elements['runnable-entity12'], 'short-name')
    global_elements['short-name176'].text = 'Runnable12'
    global_elements['minimum-start-interval12'] = ET.SubElement(global_elements['runnable-entity12'], 'minimum-start-interval')
    global_elements['minimum-start-interval12'].text = '0'
    global_elements['can-be-invoked-concurrently12'] = ET.SubElement(global_elements['runnable-entity12'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently12'].text = 'false'
    global_elements['symbol20'] = ET.SubElement(global_elements['runnable-entity12'], 'symbol')
    global_elements['symbol20'].text = 'ApplicationSwComponentType_Runnable12'

def ApplicationSwComponentType_Runnable13():
    global_elements['runnable-entity13'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity13'].attrib = {'UUID': 'e967670f-46d8-4d91-b4b9-62c85a17843e'}
    global_elements['short-name177'] = ET.SubElement(global_elements['runnable-entity13'], 'short-name')
    global_elements['short-name177'].text = 'Runnable13'
    global_elements['minimum-start-interval13'] = ET.SubElement(global_elements['runnable-entity13'], 'minimum-start-interval')
    global_elements['minimum-start-interval13'].text = '0'
    global_elements['can-be-invoked-concurrently13'] = ET.SubElement(global_elements['runnable-entity13'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently13'].text = 'false'

def ApplicationSwComponentType_Runnable13_DRA_RPort_SR_DataElement():
    global_elements['data-read-accesss'] = ET.SubElement(global_elements['runnable-entity13'], 'data-read-accesss')
    global_elements['variable-access3'] = ET.SubElement(global_elements['data-read-accesss'], 'variable-access')
    global_elements['variable-access3'].attrib = {'UUID': '9bf42611-5276-4ce4-92b5-36c024121479'}
    global_elements['short-name178'] = ET.SubElement(global_elements['variable-access3'], 'short-name')
    global_elements['short-name178'].text = 'DRA_RPort_SR_DataElement'
    global_elements['accessed-variable3'] = ET.SubElement(global_elements['variable-access3'], 'accessed-variable')
    global_elements['autosar-variable-iref3'] = ET.SubElement(global_elements['accessed-variable3'], 'autosar-variable-iref')
    global_elements['port-prototype-ref3'] = ET.SubElement(global_elements['autosar-variable-iref3'], 'port-prototype-ref')
    global_elements['port-prototype-ref3'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    global_elements['port-prototype-ref3'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DRA_RPort_SR_DataElement1():
    global_elements['target-data-prototype-ref3'] = ET.SubElement(global_elements['autosar-variable-iref3'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref3'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    global_elements['target-data-prototype-ref3'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access4'] = ET.SubElement(global_elements['data-read-accesss'], 'variable-access')
    global_elements['variable-access4'].attrib = {'UUID': '9eef2638-b3d9-47c1-9e18-37822b089dd4'}
    global_elements['short-name179'] = ET.SubElement(global_elements['variable-access4'], 'short-name')
    global_elements['short-name179'].text = 'DRA_RPort_SR_DataElement1'
    global_elements['accessed-variable4'] = ET.SubElement(global_elements['variable-access4'], 'accessed-variable')
    global_elements['autosar-variable-iref4'] = ET.SubElement(global_elements['accessed-variable4'], 'autosar-variable-iref')
    global_elements['port-prototype-ref4'] = ET.SubElement(global_elements['autosar-variable-iref4'], 'port-prototype-ref')
    global_elements['port-prototype-ref4'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    global_elements['port-prototype-ref4'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref4'] = ET.SubElement(global_elements['autosar-variable-iref4'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref4'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    global_elements['target-data-prototype-ref4'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DRA_RPort_nvd_NvData():
    global_elements['variable-access5'] = ET.SubElement(global_elements['data-read-accesss'], 'variable-access')
    global_elements['variable-access5'].attrib = {'UUID': '26ad84a0-bc71-4cae-92f7-69d3d1bc91ff'}
    global_elements['short-name180'] = ET.SubElement(global_elements['variable-access5'], 'short-name')
    global_elements['short-name180'].text = 'DRA_RPort_nvd_NvData'
    global_elements['accessed-variable5'] = ET.SubElement(global_elements['variable-access5'], 'accessed-variable')
    global_elements['autosar-variable-iref5'] = ET.SubElement(global_elements['accessed-variable5'], 'autosar-variable-iref')
    global_elements['port-prototype-ref5'] = ET.SubElement(global_elements['autosar-variable-iref5'], 'port-prototype-ref')
    global_elements['port-prototype-ref5'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref5'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DRA_RPort_nvd_NvData1():
    global_elements['target-data-prototype-ref5'] = ET.SubElement(global_elements['autosar-variable-iref5'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref5'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    global_elements['target-data-prototype-ref5'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access6'] = ET.SubElement(global_elements['data-read-accesss'], 'variable-access')
    global_elements['variable-access6'].attrib = {'UUID': '067aa426-f94d-4f7c-b471-a3631398a8a6'}
    global_elements['short-name181'] = ET.SubElement(global_elements['variable-access6'], 'short-name')
    global_elements['short-name181'].text = 'DRA_RPort_nvd_NvData1'
    global_elements['accessed-variable6'] = ET.SubElement(global_elements['variable-access6'], 'accessed-variable')
    global_elements['autosar-variable-iref6'] = ET.SubElement(global_elements['accessed-variable6'], 'autosar-variable-iref')
    global_elements['port-prototype-ref6'] = ET.SubElement(global_elements['autosar-variable-iref6'], 'port-prototype-ref')
    global_elements['port-prototype-ref6'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref6'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DWA_PPort_SR_DataElement():
    global_elements['target-data-prototype-ref6'] = ET.SubElement(global_elements['autosar-variable-iref6'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref6'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    global_elements['target-data-prototype-ref6'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['data-write-accesss2'] = ET.SubElement(global_elements['runnable-entity13'], 'data-write-accesss')
    global_elements['variable-access7'] = ET.SubElement(global_elements['data-write-accesss2'], 'variable-access')
    global_elements['variable-access7'].attrib = {'UUID': 'a0b4f337-7b3c-4ade-bc28-db75b0882305'}
    global_elements['short-name182'] = ET.SubElement(global_elements['variable-access7'], 'short-name')
    global_elements['short-name182'].text = 'DWA_PPort_SR_DataElement'
    global_elements['accessed-variable7'] = ET.SubElement(global_elements['variable-access7'], 'accessed-variable')
    global_elements['autosar-variable-iref7'] = ET.SubElement(global_elements['accessed-variable7'], 'autosar-variable-iref')
    global_elements['port-prototype-ref7'] = ET.SubElement(global_elements['autosar-variable-iref7'], 'port-prototype-ref')
    global_elements['port-prototype-ref7'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    global_elements['port-prototype-ref7'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DWA_PPort_SR_DataElement1():
    global_elements['target-data-prototype-ref7'] = ET.SubElement(global_elements['autosar-variable-iref7'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref7'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    global_elements['target-data-prototype-ref7'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access8'] = ET.SubElement(global_elements['data-write-accesss2'], 'variable-access')
    global_elements['variable-access8'].attrib = {'UUID': '839b63ac-ec02-4b70-aca8-f974d2ab728c'}
    global_elements['short-name183'] = ET.SubElement(global_elements['variable-access8'], 'short-name')
    global_elements['short-name183'].text = 'DWA_PPort_SR_DataElement1'
    global_elements['accessed-variable8'] = ET.SubElement(global_elements['variable-access8'], 'accessed-variable')
    global_elements['autosar-variable-iref8'] = ET.SubElement(global_elements['accessed-variable8'], 'autosar-variable-iref')
    global_elements['port-prototype-ref8'] = ET.SubElement(global_elements['autosar-variable-iref8'], 'port-prototype-ref')
    global_elements['port-prototype-ref8'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    global_elements['port-prototype-ref8'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DWA_PPort_nvd_NvData():
    global_elements['target-data-prototype-ref8'] = ET.SubElement(global_elements['autosar-variable-iref8'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref8'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    global_elements['target-data-prototype-ref8'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access9'] = ET.SubElement(global_elements['data-write-accesss2'], 'variable-access')
    global_elements['variable-access9'].attrib = {'UUID': 'b68d4be0-8b3f-4259-9c8a-2901c17454d7'}
    global_elements['short-name184'] = ET.SubElement(global_elements['variable-access9'], 'short-name')
    global_elements['short-name184'].text = 'DWA_PPort_nvd_NvData'
    global_elements['accessed-variable9'] = ET.SubElement(global_elements['variable-access9'], 'accessed-variable')
    global_elements['autosar-variable-iref9'] = ET.SubElement(global_elements['accessed-variable9'], 'autosar-variable-iref')
    global_elements['port-prototype-ref9'] = ET.SubElement(global_elements['autosar-variable-iref9'], 'port-prototype-ref')
    global_elements['port-prototype-ref9'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
    global_elements['port-prototype-ref9'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref9'] = ET.SubElement(global_elements['autosar-variable-iref9'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref9'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    global_elements['target-data-prototype-ref9'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DWA_PPort_nvd_NvData1():
    global_elements['variable-access10'] = ET.SubElement(global_elements['data-write-accesss2'], 'variable-access')
    global_elements['variable-access10'].attrib = {'UUID': '3e84de24-a491-4152-b344-8c5e44e9197e'}
    global_elements['short-name185'] = ET.SubElement(global_elements['variable-access10'], 'short-name')
    global_elements['short-name185'].text = 'DWA_PPort_nvd_NvData1'
    global_elements['accessed-variable10'] = ET.SubElement(global_elements['variable-access10'], 'accessed-variable')
    global_elements['autosar-variable-iref10'] = ET.SubElement(global_elements['accessed-variable10'], 'autosar-variable-iref')
    global_elements['port-prototype-ref10'] = ET.SubElement(global_elements['autosar-variable-iref10'], 'port-prototype-ref')
    global_elements['port-prototype-ref10'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
    global_elements['port-prototype-ref10'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}

def IRVRA_ExplicitInterRunnableVariable():
    global_elements['target-data-prototype-ref10'] = ET.SubElement(global_elements['autosar-variable-iref10'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref10'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    global_elements['target-data-prototype-ref10'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['read-local-variables'] = ET.SubElement(global_elements['runnable-entity13'], 'read-local-variables')
    global_elements['variable-access11'] = ET.SubElement(global_elements['read-local-variables'], 'variable-access')
    global_elements['variable-access11'].attrib = {'UUID': 'c8972fdb-f78a-4e12-9a30-4faf0daa6c23'}
    global_elements['short-name186'] = ET.SubElement(global_elements['variable-access11'], 'short-name')
    global_elements['short-name186'].text = 'IRVRA_ExplicitInterRunnableVariable'
    global_elements['accessed-variable11'] = ET.SubElement(global_elements['variable-access11'], 'accessed-variable')
    global_elements['local-variable-ref'] = ET.SubElement(global_elements['accessed-variable11'], 'local-variable-ref')
    global_elements['local-variable-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ExplicitInterRunnableVariable'
    global_elements['local-variable-ref'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def IRVRA_ImplicitInterRunnableVariable():
    global_elements['variable-access12'] = ET.SubElement(global_elements['read-local-variables'], 'variable-access')
    global_elements['variable-access12'].attrib = {'UUID': 'bf16d1d1-6833-4572-8830-6e31aa069454'}
    global_elements['short-name187'] = ET.SubElement(global_elements['variable-access12'], 'short-name')
    global_elements['short-name187'].text = 'IRVRA_ImplicitInterRunnableVariable'
    global_elements['accessed-variable12'] = ET.SubElement(global_elements['variable-access12'], 'accessed-variable')
    global_elements['local-variable-ref2'] = ET.SubElement(global_elements['accessed-variable12'], 'local-variable-ref')
    global_elements['local-variable-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ImplicitInterRunnableVariable'
    global_elements['local-variable-ref2'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['symbol21'] = ET.SubElement(global_elements['runnable-entity13'], 'symbol')
    global_elements['symbol21'].text = 'ApplicationSwComponentType_Runnable13'

def ApplicationSwComponentType_Runnable14():
    global_elements['runnable-entity14'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity14'].attrib = {'UUID': '1c2e8cb0-fdf5-45ee-9257-dee6f42d2ad4'}
    global_elements['short-name188'] = ET.SubElement(global_elements['runnable-entity14'], 'short-name')
    global_elements['short-name188'].text = 'Runnable14'
    global_elements['minimum-start-interval14'] = ET.SubElement(global_elements['runnable-entity14'], 'minimum-start-interval')
    global_elements['minimum-start-interval14'].text = '0'
    global_elements['can-be-invoked-concurrently14'] = ET.SubElement(global_elements['runnable-entity14'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently14'].text = 'false'
    global_elements['symbol22'] = ET.SubElement(global_elements['runnable-entity14'], 'symbol')
    global_elements['symbol22'].text = 'ApplicationSwComponentType_Runnable14'
  
def ApplicationSwComponentType_Runnable15():
    global_elements['runnable-entity15'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity15'].attrib = {'UUID': '6debf2b3-9c4c-455e-9cbc-0c7cfaca4d43'}
    global_elements['short-name189'] = ET.SubElement(global_elements['runnable-entity15'], 'short-name')
    global_elements['short-name189'].text = 'Runnable15'
    global_elements['minimum-start-interval15'] = ET.SubElement(global_elements['runnable-entity15'], 'minimum-start-interval')
    global_elements['minimum-start-interval15'].text = '0'
    global_elements['can-be-invoked-concurrently15'] = ET.SubElement(global_elements['runnable-entity15'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently15'].text = 'false'

def ApplicationSwComponentType_Runnable15_DRA_RPort_nvd_NvData():
    global_elements['data-read-accesss2'] = ET.SubElement(global_elements['runnable-entity15'], 'data-read-accesss')
    global_elements['variable-access13'] = ET.SubElement(global_elements['data-read-accesss2'], 'variable-access')
    global_elements['variable-access13'].attrib = {'UUID': '5648b05b-23f8-4729-9fdd-25a617e2d17b'}
    global_elements['short-name190'] = ET.SubElement(global_elements['variable-access13'], 'short-name')
    global_elements['short-name190'].text = 'DRA_RPort_nvd_NvData'
    global_elements['accessed-variable13'] = ET.SubElement(global_elements['variable-access13'], 'accessed-variable')
    global_elements['autosar-variable-iref11'] = ET.SubElement(global_elements['accessed-variable13'], 'autosar-variable-iref')
    global_elements['port-prototype-ref11'] = ET.SubElement(global_elements['autosar-variable-iref11'], 'port-prototype-ref')
    global_elements['port-prototype-ref11'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref11'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref11'] = ET.SubElement(global_elements['autosar-variable-iref11'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref11'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    global_elements['target-data-prototype-ref11'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DRA_RPort_nvd_NvData1():
    global_elements['variable-access14'] = ET.SubElement(global_elements['data-read-accesss2'], 'variable-access')
    global_elements['variable-access14'].attrib = {'UUID': 'b355b0ac-1fa9-43f7-b5ab-240eae2c3694'}
    global_elements['short-name191'] = ET.SubElement(global_elements['variable-access14'], 'short-name')
    global_elements['short-name191'].text = 'DRA_RPort_nvd_NvData1'
    global_elements['accessed-variable14'] = ET.SubElement(global_elements['variable-access14'], 'accessed-variable')
    global_elements['autosar-variable-iref12'] = ET.SubElement(global_elements['accessed-variable14'], 'autosar-variable-iref')
    global_elements['port-prototype-ref12'] = ET.SubElement(global_elements['autosar-variable-iref12'], 'port-prototype-ref')
    global_elements['port-prototype-ref12'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref12'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref12'] = ET.SubElement(global_elements['autosar-variable-iref12'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref12'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    global_elements['target-data-prototype-ref12'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DRP_RPort_SR_DataElement():
    global_elements['data-receive-point-by-arguments'] = ET.SubElement(global_elements['runnable-entity15'], 'data-receive-point-by-arguments')
    global_elements['variable-access15'] = ET.SubElement(global_elements['data-receive-point-by-arguments'], 'variable-access')
    global_elements['variable-access15'].attrib = {'UUID': '86796258-06a6-480e-8a39-e01411743a56'}
    global_elements['short-name192'] = ET.SubElement(global_elements['variable-access15'], 'short-name')
    global_elements['short-name192'].text = 'DRP_RPort_SR_DataElement'
    global_elements['accessed-variable15'] = ET.SubElement(global_elements['variable-access15'], 'accessed-variable')
    global_elements['autosar-variable-iref13'] = ET.SubElement(global_elements['accessed-variable15'], 'autosar-variable-iref')
    global_elements['port-prototype-ref13'] = ET.SubElement(global_elements['autosar-variable-iref13'], 'port-prototype-ref')
    global_elements['port-prototype-ref13'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    global_elements['port-prototype-ref13'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref13'] = ET.SubElement(global_elements['autosar-variable-iref13'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref13'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    global_elements['target-data-prototype-ref13'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DRP_RPort_nvd_NvData():
    global_elements['variable-access16'] = ET.SubElement(global_elements['data-receive-point-by-arguments'], 'variable-access')
    global_elements['variable-access16'].attrib = {'UUID': '88c27605-b9a2-4db7-af10-2a0953c5110b'}
    global_elements['short-name193'] = ET.SubElement(global_elements['variable-access16'], 'short-name')
    global_elements['short-name193'].text = 'DRP_RPort_nvd_NvData'
    global_elements['accessed-variable16'] = ET.SubElement(global_elements['variable-access16'], 'accessed-variable')
    global_elements['autosar-variable-iref14'] = ET.SubElement(global_elements['accessed-variable16'], 'autosar-variable-iref')
    global_elements['port-prototype-ref14'] = ET.SubElement(global_elements['autosar-variable-iref14'], 'port-prototype-ref')
    global_elements['port-prototype-ref14'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref14'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref14'] = ET.SubElement(global_elements['autosar-variable-iref14'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref14'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    global_elements['target-data-prototype-ref14'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DRP_RPort_nvd_NvData1():
    global_elements['variable-access17'] = ET.SubElement(global_elements['data-receive-point-by-arguments'], 'variable-access')
    global_elements['variable-access17'].attrib = {'UUID': 'b69ad602-c226-42a5-9bbb-acbbc5c16743'}
    global_elements['short-name194'] = ET.SubElement(global_elements['variable-access17'], 'short-name')
    global_elements['short-name194'].text = 'DRP_RPort_nvd_NvData1'
    global_elements['accessed-variable17'] = ET.SubElement(global_elements['variable-access17'], 'accessed-variable')
    global_elements['autosar-variable-iref15'] = ET.SubElement(global_elements['accessed-variable17'], 'autosar-variable-iref')
    global_elements['port-prototype-ref15'] = ET.SubElement(global_elements['autosar-variable-iref15'], 'port-prototype-ref')
    global_elements['port-prototype-ref15'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref15'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref15'] = ET.SubElement(global_elements['autosar-variable-iref15'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref15'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    global_elements['target-data-prototype-ref15'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DRPV_RPort_SR_DataElement1():
    global_elements['data-receive-point-by-values'] = ET.SubElement(global_elements['runnable-entity15'], 'data-receive-point-by-values')
    global_elements['variable-access18'] = ET.SubElement(global_elements['data-receive-point-by-values'], 'variable-access')
    global_elements['variable-access18'].attrib = {'UUID': '38ed8447-65f1-48a9-b075-fa613c1267d2'}
    global_elements['short-name195'] = ET.SubElement(global_elements['variable-access18'], 'short-name')
    global_elements['short-name195'].text = 'DRPV_RPort_SR_DataElement1'
    global_elements['accessed-variable18'] = ET.SubElement(global_elements['variable-access18'], 'accessed-variable')
    global_elements['autosar-variable-iref16'] = ET.SubElement(global_elements['accessed-variable18'], 'autosar-variable-iref')
    global_elements['port-prototype-ref16'] = ET.SubElement(global_elements['autosar-variable-iref16'], 'port-prototype-ref')
    global_elements['port-prototype-ref16'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    global_elements['port-prototype-ref16'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref16'] = ET.SubElement(global_elements['autosar-variable-iref16'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref16'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    global_elements['target-data-prototype-ref16'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DRPV_RPort_nvd_NvData():
    global_elements['variable-access19'] = ET.SubElement(global_elements['data-receive-point-by-values'], 'variable-access')
    global_elements['variable-access19'].attrib = {'UUID': 'd07d7e6b-0d9c-4475-bbb9-2ccfc3e60c33'}
    global_elements['short-name196'] = ET.SubElement(global_elements['variable-access19'], 'short-name')
    global_elements['short-name196'].text = 'DRPV_RPort_nvd_NvData'
    global_elements['accessed-variable19'] = ET.SubElement(global_elements['variable-access19'], 'accessed-variable')
    global_elements['autosar-variable-iref17'] = ET.SubElement(global_elements['accessed-variable19'], 'autosar-variable-iref')
    global_elements['port-prototype-ref17'] = ET.SubElement(global_elements['autosar-variable-iref17'], 'port-prototype-ref')
    global_elements['port-prototype-ref17'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref17'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref17'] = ET.SubElement(global_elements['autosar-variable-iref17'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref17'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    global_elements['target-data-prototype-ref17'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DSP_PPort_SR_DataElement():
    global_elements['data-send-points2'] = ET.SubElement(global_elements['runnable-entity15'], 'data-send-points')
    global_elements['variable-access20'] = ET.SubElement(global_elements['data-send-points2'], 'variable-access')
    global_elements['variable-access20'].attrib = {'UUID': '2fc872c8-d598-4d11-8502-1a70e9104bc9'}
    global_elements['short-name197'] = ET.SubElement(global_elements['variable-access20'], 'short-name')
    global_elements['short-name197'].text = 'DSP_PPort_SR_DataElement'
    global_elements['accessed-variable20'] = ET.SubElement(global_elements['variable-access20'], 'accessed-variable')
    global_elements['autosar-variable-iref18'] = ET.SubElement(global_elements['accessed-variable20'], 'autosar-variable-iref')
    global_elements['port-prototype-ref18'] = ET.SubElement(global_elements['autosar-variable-iref18'], 'port-prototype-ref')
    global_elements['port-prototype-ref18'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    global_elements['port-prototype-ref18'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref18'] = ET.SubElement(global_elements['autosar-variable-iref18'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref18'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    global_elements['target-data-prototype-ref18'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DSP_PPort_SR_DataElement1():
    global_elements['variable-access21'] = ET.SubElement(global_elements['data-send-points2'], 'variable-access')
    global_elements['variable-access21'].attrib = {'UUID': 'a2f22836-4cd0-4c2e-8040-1abdf8935ac0'}
    global_elements['short-name198'] = ET.SubElement(global_elements['variable-access21'], 'short-name')
    global_elements['short-name198'].text = 'DSP_PPort_SR_DataElement1'
    global_elements['accessed-variable21'] = ET.SubElement(global_elements['variable-access21'], 'accessed-variable')
    global_elements['autosar-variable-iref19'] = ET.SubElement(global_elements['accessed-variable21'], 'autosar-variable-iref')
    global_elements['port-prototype-ref19'] = ET.SubElement(global_elements['autosar-variable-iref19'], 'port-prototype-ref')
    global_elements['port-prototype-ref19'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    global_elements['port-prototype-ref19'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref19'] = ET.SubElement(global_elements['autosar-variable-iref19'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref19'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    global_elements['target-data-prototype-ref19'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DSP_PPort_nvd_NvData():
    global_elements['variable-access22'] = ET.SubElement(global_elements['data-send-points2'], 'variable-access')
    global_elements['variable-access22'].attrib = {'UUID': 'c0c41eb1-b5bf-4e30-9569-24d7316b64c8'}
    global_elements['short-name199'] = ET.SubElement(global_elements['variable-access22'], 'short-name')
    global_elements['short-name199'].text = 'DSP_PPort_nvd_NvData'
    global_elements['accessed-variable22'] = ET.SubElement(global_elements['variable-access22'], 'accessed-variable')
    global_elements['autosar-variable-iref20'] = ET.SubElement(global_elements['accessed-variable22'], 'autosar-variable-iref')
    global_elements['port-prototype-ref20'] = ET.SubElement(global_elements['autosar-variable-iref20'], 'port-prototype-ref')
    global_elements['port-prototype-ref20'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
    global_elements['port-prototype-ref20'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref20'] = ET.SubElement(global_elements['autosar-variable-iref20'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref20'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    global_elements['target-data-prototype-ref20'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DSP_PPort_nvd_NvData1():
    global_elements['variable-access23'] = ET.SubElement(global_elements['data-send-points2'], 'variable-access')
    global_elements['variable-access23'].attrib = {'UUID': '96f66382-5f86-4a47-bd5b-9f95f81fc3c9'}
    global_elements['short-name200'] = ET.SubElement(global_elements['variable-access23'], 'short-name')
    global_elements['short-name200'].text = 'DSP_PPort_nvd_NvData1'
    global_elements['accessed-variable23'] = ET.SubElement(global_elements['variable-access23'], 'accessed-variable')
    global_elements['autosar-variable-iref21'] = ET.SubElement(global_elements['accessed-variable23'], 'autosar-variable-iref')
    global_elements['port-prototype-ref21'] = ET.SubElement(global_elements['autosar-variable-iref21'], 'port-prototype-ref')
    global_elements['port-prototype-ref21'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
    global_elements['port-prototype-ref21'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref21'] = ET.SubElement(global_elements['autosar-variable-iref21'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref21'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    global_elements['target-data-prototype-ref21'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DWA_PPort_SR_DataElement1():
    global_elements['data-write-accesss3'] = ET.SubElement(global_elements['runnable-entity15'], 'data-write-accesss')
    global_elements['variable-access24'] = ET.SubElement(global_elements['data-write-accesss3'], 'variable-access')
    global_elements['variable-access24'].attrib = {'UUID': 'd40a6e94-d8e5-48e5-8a1a-c7debe02592f'}
    global_elements['short-name201'] = ET.SubElement(global_elements['variable-access24'], 'short-name')
    global_elements['short-name201'].text = 'DWA_PPort_SR_DataElement1'
    global_elements['accessed-variable24'] = ET.SubElement(global_elements['variable-access24'], 'accessed-variable')
    global_elements['autosar-variable-iref22'] = ET.SubElement(global_elements['accessed-variable24'], 'autosar-variable-iref')
    global_elements['port-prototype-ref22'] = ET.SubElement(global_elements['autosar-variable-iref22'], 'port-prototype-ref')
    global_elements['port-prototype-ref22'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    global_elements['port-prototype-ref22'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref22'] = ET.SubElement(global_elements['autosar-variable-iref22'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref22'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    global_elements['target-data-prototype-ref22'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_MSP_PPort_msi_ModeGroup():
    global_elements['mode-switch-points2'] = ET.SubElement(global_elements['runnable-entity15'], 'mode-switch-points')
    global_elements['mode-switch-point2'] = ET.SubElement(global_elements['mode-switch-points2'], 'mode-switch-point')
    global_elements['mode-switch-point2'].attrib = {'UUID': '8f7d9801-a32d-4e5f-85cd-fbcf669d921a'}
    global_elements['short-name202'] = ET.SubElement(global_elements['mode-switch-point2'], 'short-name')
    global_elements['short-name202'].text = 'MSP_PPort_msi_ModeGroup'
    global_elements['mode-group-iref2'] = ET.SubElement(global_elements['mode-switch-point2'], 'mode-group-iref')
    global_elements['context-p-port-ref3'] = ET.SubElement(global_elements['mode-group-iref2'], 'context-p-port-ref')
    global_elements['context-p-port-ref3'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_msi'
    global_elements['context-p-port-ref3'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-mode-group-ref2'] = ET.SubElement(global_elements['mode-group-iref2'], 'target-mode-group-ref')
    global_elements['target-mode-group-ref2'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
    global_elements['target-mode-group-ref2'].attrib = {'DEST': 'MODE-DECLARATION-GROUP-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_ParameterAccess():
    global_elements['parameter-accesss'] = ET.SubElement(global_elements['runnable-entity15'], 'parameter-accesss')
    global_elements['parameter-access'] = ET.SubElement(global_elements['parameter-accesss'], 'parameter-access')
    global_elements['parameter-access'].attrib = {'UUID': '92d672aa-34ea-4fcb-a0a2-ab2431d59c0a'}
    global_elements['short-name203'] = ET.SubElement(global_elements['parameter-access'], 'short-name')
    global_elements['short-name203'].text = 'ParameterAccess'
    global_elements['accessed-parameter'] = ET.SubElement(global_elements['parameter-access'], 'accessed-parameter')
    global_elements['local-parameter-ref'] = ET.SubElement(global_elements['accessed-parameter'], 'local-parameter-ref')
    global_elements['local-parameter-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ConstantMemory'
    global_elements['local-parameter-ref'].attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_PICPVA_PerInstanceParameter():
    global_elements['parameter-access2'] = ET.SubElement(global_elements['parameter-accesss'], 'parameter-access')
    global_elements['parameter-access2'].attrib = {'UUID': '391726ca-20e2-4c02-b063-65244a9e523a'}
    global_elements['short-name204'] = ET.SubElement(global_elements['parameter-access2'], 'short-name')
    global_elements['short-name204'].text = 'PICPVA_PerInstanceParameter'
    global_elements['accessed-parameter2'] = ET.SubElement(global_elements['parameter-access2'], 'accessed-parameter')
    global_elements['local-parameter-ref2'] = ET.SubElement(global_elements['accessed-parameter2'], 'local-parameter-ref')
    global_elements['local-parameter-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/PerInstanceParameter'
    global_elements['local-parameter-ref2'].attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_CPA_RPort_prm_Parameter():
    global_elements['parameter-access3'] = ET.SubElement(global_elements['parameter-accesss'], 'parameter-access')
    global_elements['parameter-access3'].attrib = {'UUID': '19d7aee6-82b8-4233-a787-b84bdb562167'}
    global_elements['short-name205'] = ET.SubElement(global_elements['parameter-access3'], 'short-name')
    global_elements['short-name205'].text = 'CPA_RPort_prm_Parameter'
    global_elements['accessed-parameter3'] = ET.SubElement(global_elements['parameter-access3'], 'accessed-parameter')
    global_elements['autosar-parameter-iref'] = ET.SubElement(global_elements['accessed-parameter3'], 'autosar-parameter-iref')
    global_elements['port-prototype-ref23'] = ET.SubElement(global_elements['autosar-parameter-iref'], 'port-prototype-ref')
    global_elements['port-prototype-ref23'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_prm'
    global_elements['port-prototype-ref23'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref23'] = ET.SubElement(global_elements['autosar-parameter-iref'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref23'].text = '/SharedElements/PortInterfaces/Parameter/ParameterInterface/Parameter'
    global_elements['target-data-prototype-ref23'].attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_CPA_RPort_prm_Parameter1():
    global_elements['parameter-access4'] = ET.SubElement(global_elements['parameter-accesss'], 'parameter-access')
    global_elements['parameter-access4'].attrib = {'UUID': 'ab7c5c59-47f3-4fee-a310-f64cb2c00c48'}
    global_elements['short-name206'] = ET.SubElement(global_elements['parameter-access4'], 'short-name')
    global_elements['short-name206'].text = 'CPA_RPort_prm_Parameter1'
    global_elements['accessed-parameter4'] = ET.SubElement(global_elements['parameter-access4'], 'accessed-parameter')
    global_elements['autosar-parameter-iref2'] = ET.SubElement(global_elements['accessed-parameter4'], 'autosar-parameter-iref')
    global_elements['port-prototype-ref24'] = ET.SubElement(global_elements['autosar-parameter-iref2'], 'port-prototype-ref')
    global_elements['port-prototype-ref24'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_prm'
    global_elements['port-prototype-ref24'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref24'] = ET.SubElement(global_elements['autosar-parameter-iref2'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref24'].text = '/SharedElements/PortInterfaces/Parameter/ParameterInterface/Parameter1'
    global_elements['target-data-prototype-ref24'].attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_SCPVA_SharedParameter():
    global_elements['parameter-access5'] = ET.SubElement(global_elements['parameter-accesss'], 'parameter-access')
    global_elements['parameter-access5'].attrib = {'UUID': 'f7d2bfa9-92c5-4627-b238-86aadd05585b'}
    global_elements['short-name207'] = ET.SubElement(global_elements['parameter-access5'], 'short-name')
    global_elements['short-name207'].text = 'SCPVA_SharedParameter'
    global_elements['accessed-parameter5'] = ET.SubElement(global_elements['parameter-access5'], 'accessed-parameter')
    global_elements['local-parameter-ref3'] = ET.SubElement(global_elements['accessed-parameter5'], 'local-parameter-ref')
    global_elements['local-parameter-ref3'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/SharedParameter'
    global_elements['local-parameter-ref3'].attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_SSCP_RPort_CS_Operation1():
    global_elements['server-call-points2'] = ET.SubElement(global_elements['runnable-entity15'], 'server-call-points')
    global_elements['synchronous-server-call-point'] = ET.SubElement(global_elements['server-call-points2'], 'synchronous-server-call-point')
    global_elements['synchronous-server-call-point'].attrib = {'UUID': 'd6a93f51-be57-4a77-bd8f-e25d3e0ba149'}
    global_elements['short-name208'] = ET.SubElement(global_elements['synchronous-server-call-point'], 'short-name')
    global_elements['short-name208'].text = 'SSCP_RPort_CS_Operation1'
    global_elements['operation-iref3'] = ET.SubElement(global_elements['synchronous-server-call-point'], 'operation-iref')
    global_elements['context-r-port-ref5'] = ET.SubElement(global_elements['operation-iref3'], 'context-r-port-ref')
    global_elements['context-r-port-ref5'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_CS'
    global_elements['context-r-port-ref5'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-required-operation-ref2'] = ET.SubElement(global_elements['operation-iref3'], 'target-required-operation-ref')
    global_elements['target-required-operation-ref2'].text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface/Operation1'
    global_elements['target-required-operation-ref2'].attrib = {'DEST': 'CLIENT-SERVER-OPERATION'}
    global_elements['timeout2'] = ET.SubElement(global_elements['synchronous-server-call-point'], 'timeout')
    global_elements['timeout2'].text = '0'
    global_elements['symbol23'] = ET.SubElement(global_elements['runnable-entity15'], 'symbol')
    global_elements['symbol23'].text = 'ApplicationSwComponentType_Runnable15'

def ApplicationSwComponentType_Runnable15_IRVWA_ExplicitInterRunnableVariable():
    global_elements['written-local-variables'] = ET.SubElement(global_elements['runnable-entity15'], 'written-local-variables')
    global_elements['variable-access25'] = ET.SubElement(global_elements['written-local-variables'], 'variable-access')
    global_elements['variable-access25'].attrib = {'UUID': '7e246e9c-b78a-47be-8798-02887c881e6e'}
    global_elements['short-name209'] = ET.SubElement(global_elements['variable-access25'], 'short-name')
    global_elements['short-name209'].text = 'IRVWA_ExplicitInterRunnableVariable'
    global_elements['accessed-variable25'] = ET.SubElement(global_elements['variable-access25'], 'accessed-variable')
    global_elements['local-variable-ref3'] = ET.SubElement(global_elements['accessed-variable25'], 'local-variable-ref')
    global_elements['local-variable-ref3'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ExplicitInterRunnableVariable'
    global_elements['local-variable-ref3'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_IRVWA_ImplicitInterRunnableVariable():
    global_elements['variable-access26'] = ET.SubElement(global_elements['written-local-variables'], 'variable-access')
    global_elements['variable-access26'].attrib = {'UUID': 'd976bba9-3132-4e15-ac45-88b85facf508'}
    global_elements['short-name210'] = ET.SubElement(global_elements['variable-access26'], 'short-name')
    global_elements['short-name210'].text = 'IRVWA_ImplicitInterRunnableVariable'
    global_elements['accessed-variable26'] = ET.SubElement(global_elements['variable-access26'], 'accessed-variable')
    global_elements['local-variable-ref4'] = ET.SubElement(global_elements['accessed-variable26'], 'local-variable-ref')
    global_elements['local-variable-ref4'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ImplicitInterRunnableVariable'
    global_elements['local-variable-ref4'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'} 
  
def ApplicationSwComponentType_SharedParameter():
    global_elements['shared-parameters'] = ET.SubElement(global_elements['swc-internal-behavior'], 'shared-parameters')
    global_elements['parameter-data-prototype5'] = ET.SubElement(global_elements['shared-parameters'], 'parameter-data-prototype')
    global_elements['parameter-data-prototype5'].attrib = {'UUID': 'edf877b4-19ea-4e47-8180-a74099cfff0f'}
    global_elements['short-name211'] = ET.SubElement(global_elements['parameter-data-prototype5'], 'short-name')
    global_elements['short-name211'].text = 'SharedParameter'
    global_elements['sw-data-def-props47'] = ET.SubElement(global_elements['parameter-data-prototype5'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants47'] = ET.SubElement(global_elements['sw-data-def-props47'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional47'] = ET.SubElement(global_elements['sw-data-def-props-variants47'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access15'] = ET.SubElement(global_elements['sw-data-def-props-conditional47'], 'sw-calibration-access')
    global_elements['sw-calibration-access15'].text = 'READ-WRITE'
    global_elements['sw-impl-policy34'] = ET.SubElement(global_elements['sw-data-def-props-conditional47'], 'sw-impl-policy')
    global_elements['sw-impl-policy34'].text = 'STANDARD'
    global_elements['type-tref39'] = ET.SubElement(global_elements['parameter-data-prototype5'], 'type-tref')
    global_elements['type-tref39'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float32'
    global_elements['type-tref39'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value7'] = ET.SubElement(global_elements['parameter-data-prototype5'], 'init-value')
    global_elements['constant-reference3'] = ET.SubElement(global_elements['init-value7'], 'constant-reference')
    global_elements['short-label10'] = ET.SubElement(global_elements['constant-reference3'], 'short-label')
    global_elements['short-label10'].text = 'ReferenceToConstant'
    global_elements['constant-ref3'] = ET.SubElement(global_elements['constant-reference3'], 'constant-ref')
    global_elements['constant-ref3'].text = '/SharedElements/ConstantSpecifications/ApplicationSwComponentType_SharedParameter'
    global_elements['constant-ref3'].attrib = {'DEST': 'CONSTANT-SPECIFICATION'}
    global_elements['supports-multiple-instantiation'] = ET.SubElement(global_elements['swc-internal-behavior'], 'supports-multiple-instantiation')
    global_elements['supports-multiple-instantiation'].text = 'false'
    global_elements['ar-packages6'] = ET.SubElement(global_elements['ar-package22'], 'ar-packages')
    global_elements['ar-package23'] = ET.SubElement(global_elements['ar-packages6'], 'ar-package')
    global_elements['ar-package23'].attrib = {'UUID': '0f00b99f-27e3-434f-9d85-398fc7c29067'}
    global_elements['short-name212'] = ET.SubElement(global_elements['ar-package23'], 'short-name')
    global_elements['short-name212'].text = 'ConstantSpecifications'

def ComplexDeviceDriverSwComponentType():
    # global_elements['ar-package24'] = ET.SubElement(global_elements['ar-packages5'], 'ar-package')
    # global_elements['ar-package24'].attrib = {'UUID': '7f0b665f-81ab-462f-aeab-1777b0f9dfd8'}
    # global_elements['short-name213'] = ET.SubElement(global_elements['ar-package24'], 'short-name')
    # global_elements['short-name213'].text = 'CddSWC'
    global_elements['elements20'] = ET.SubElement(global_elements['ar-package24'], 'elements')
    global_elements['complex-device-driver-sw-component-type'] = ET.SubElement(global_elements['elements20'], 'complex-device-driver-sw-component-type')
    global_elements['complex-device-driver-sw-component-type'].attrib = {'UUID': '27755bdf-1bfe-447f-bfdf-54402e4f4db3'}
    global_elements['short-name214'] = ET.SubElement(global_elements['complex-device-driver-sw-component-type'], 'short-name')
    global_elements['short-name214'].text = 'ComplexDeviceDriverSwComponentType'
    
def CompositionSwComponentType():
    # global_elements['ar-package25'] = ET.SubElement(global_elements['ar-packages5'], 'ar-package')
    # global_elements['ar-package25'].attrib = {'UUID': 'a9d129de-eda4-4cda-9025-70a56f38fb59'}
    # global_elements['short-name215'] = ET.SubElement(global_elements['ar-package25'], 'short-name')
    # global_elements['short-name215'].text = 'CompSWC'
    global_elements['elements21'] = ET.SubElement(global_elements['ar-package25'], 'elements')
    global_elements['composition-sw-component-type'] = ET.SubElement(global_elements['elements21'], 'composition-sw-component-type')
    global_elements['composition-sw-component-type'].attrib = {'UUID': '9e886193-6d1b-454f-98b2-d0347db57ace'}
    global_elements['short-name216'] = ET.SubElement(global_elements['composition-sw-component-type'], 'short-name')
    global_elements['short-name216'].text = 'CompositionSwComponentType'
 
 
def EcuAbstractionSwComponentType():
    # global_elements['ar-package26'] = ET.SubElement(global_elements['ar-packages5'], 'ar-package')
    # global_elements['ar-package26'].attrib = {'UUID': '28aa9cf2-4118-4878-8504-271a3ed4600b'}
    # global_elements['short-name217'] = ET.SubElement(global_elements['ar-package26'], 'short-name')
    # global_elements['short-name217'].text = 'EcuAbSWC'
    global_elements['elements22'] = ET.SubElement(global_elements['ar-package26'], 'elements')
    global_elements['ecu-abstraction-sw-component-type'] = ET.SubElement(global_elements['elements22'], 'ecu-abstraction-sw-component-type')
    global_elements['ecu-abstraction-sw-component-type'].attrib = {'UUID': '0dc33c67-8b23-4896-b6a3-8a537f1cd166'}
    global_elements['short-name218'] = ET.SubElement(global_elements['ecu-abstraction-sw-component-type'], 'short-name')
    global_elements['short-name218'].text = 'EcuAbstractionSwComponentType'

def NvBlockSwComponentType():
    # global_elements['ar-package27'] = ET.SubElement(global_elements['ar-packages5'], 'ar-package')
    # global_elements['ar-package27'].attrib = {'UUID': '8562405a-26a1-4c3d-861f-eb0745310572'}
    # global_elements['short-name219'] = ET.SubElement(global_elements['ar-package27'], 'short-name')
    # global_elements['short-name219'].text = 'NvDataSWC'
    global_elements['elements23'] = ET.SubElement(global_elements['ar-package27'], 'elements')
    global_elements['nv-block-sw-component-type'] = ET.SubElement(global_elements['elements23'], 'nv-block-sw-component-type')
    global_elements['nv-block-sw-component-type'].attrib = {'UUID': '9a2c1578-3f64-4af0-b953-7b81f28434cf'}
    global_elements['short-name220'] = ET.SubElement(global_elements['nv-block-sw-component-type'], 'short-name')
    global_elements['short-name220'].text = 'NvBlockSwComponentType'

def ParameterSwComponentType():
    # global_elements['ar-package28'] = ET.SubElement(global_elements['ar-packages5'], 'ar-package')
    # global_elements['ar-package28'].attrib = {'UUID': '0a54c44d-f71e-4ec3-bbf1-410c0b885915'}
    # global_elements['short-name221'] = ET.SubElement(global_elements['ar-package28'], 'short-name')
    # global_elements['short-name221'].text = 'PrmSWC'
    global_elements['elements24'] = ET.SubElement(global_elements['ar-package28'], 'elements')
    global_elements['parameter-sw-component-type'] = ET.SubElement(global_elements['elements24'], 'parameter-sw-component-type')
    global_elements['parameter-sw-component-type'].attrib = {'UUID': 'c21a6d07-19ae-40ac-affe-f4aa3b5acb25'}
    global_elements['short-name222'] = ET.SubElement(global_elements['parameter-sw-component-type'], 'short-name')
    global_elements['short-name222'].text = 'ParameterSwComponentType'

def SensorActuatorSwComponentType():
    # global_elements['ar-package29'] = ET.SubElement(global_elements['ar-packages5'], 'ar-package')
    # global_elements['ar-package29'].attrib = {'UUID': 'f142ef66-4dce-4750-8568-a7e836f462da'}
    # global_elements['short-name223'] = ET.SubElement(global_elements['ar-package29'], 'short-name')
    # global_elements['short-name223'].text = 'SnsrActSWC'
    global_elements['elements25'] = ET.SubElement(global_elements['ar-package29'], 'elements')
    global_elements['sensor-actuator-sw-component-type'] = ET.SubElement(global_elements['elements25'], 'sensor-actuator-sw-component-type')
    global_elements['sensor-actuator-sw-component-type'].attrib = {'UUID': 'e631e3e3-9a52-4bbe-a762-4311d8f45934'}
    global_elements['short-name224'] = ET.SubElement(global_elements['sensor-actuator-sw-component-type'], 'short-name')
    global_elements['short-name224'].text = 'SensorActuatorSwComponentType'

def ServiceProxySwComponentType():
    # global_elements['ar-package30'] = ET.SubElement(global_elements['ar-packages5'], 'ar-package')
    # global_elements['ar-package30'].attrib = {'UUID': '60bb3f96-0a5c-4e30-bdda-5205f3a1cdb6'}
    # global_elements['short-name225'] = ET.SubElement(global_elements['ar-package30'], 'short-name')
    # global_elements['short-name225'].text = 'SrvcPrxySWC'
    global_elements['elements26'] = ET.SubElement(global_elements['ar-package30'], 'elements')
    global_elements['service-proxy-sw-component-type'] = ET.SubElement(global_elements['elements26'], 'service-proxy-sw-component-type')
    global_elements['service-proxy-sw-component-type'].attrib = {'UUID': '7e09780f-aad2-4f70-8c22-e5e19f1a82e8'}
    global_elements['short-name226'] = ET.SubElement(global_elements['service-proxy-sw-component-type'], 'short-name')
    global_elements['short-name226'].text = 'ServiceProxySwComponentType'

def ServiceSwComponentType():
    # global_elements['ar-package31'] = ET.SubElement(global_elements['ar-packages5'], 'ar-package')
    # global_elements['ar-package31'].attrib = {'UUID': '2ed6bb1a-c9d6-46c0-ae8b-0743080405b6'}
    # global_elements['short-name227'] = ET.SubElement(global_elements['ar-package31'], 'short-name')
    # global_elements['short-name227'].text = 'SrvcSWC'
    global_elements['elements27'] = ET.SubElement(global_elements['ar-package31'], 'elements')
    global_elements['service-sw-component-type'] = ET.SubElement(global_elements['elements27'], 'service-sw-component-type')
    global_elements['service-sw-component-type'].attrib = {'UUID': '1da8de22-a6ec-4cab-829a-56300097c5ac'}
    global_elements['short-name228'] = ET.SubElement(global_elements['service-sw-component-type'], 'short-name')
    global_elements['short-name228'].text = 'ServiceSwComponentType'
    
def Systems():
    global_elements['ar-package32'] = ET.SubElement(global_elements['ar-packages'], 'ar-package')
    global_elements['short-name229'] = ET.SubElement(global_elements['ar-package32'], 'short-name')
    global_elements['short-name229'].text = 'Systems'


    indent(global_elements['root'])
    tree = ET.ElementTree(global_elements['root'])
    tree.write('output.arxml', encoding='utf-8', xml_declaration=True)

    print("ARXML file has been created and saved as 'output.arxml'.")

if __name__ == '__main__':
    
    ApplicationDataTypes()
    ApplicationArrayDataType_Variable()
    ApplicationPrimitiveDataType()
    Bool_ApplicationPrimitiveDataType()
    Copy_ApplicationPrimitiveDataType()
    String_ApplicationPrimitiveDataType()
    ApplicationRecordDataType()
    CompuMethods()
    CompuMethod()
    LINEAR_CompuMethod()
    RAT_FUNC_CompuMethod()
    SCALE_RATIONAL_AND_TEXTTABLE_CompuMethod()
    Scale_linear_And_texttable_CompuMethod()
    TAB_NOINTP_CompuMethod()
    TEXTTABLE_CompuMethod()
    ApplicationSwComponentType_ExplicitInterRunnableVariable()
    ApplicationSwComponentType_SharedParameter()
    ApplicationSwComponentType_StaticMemory()
    ConstantSpecification()
    ConstantTypeMappingSets()
    DataConstr()
    DataTypemappingSets()
    ImplementationDataTypes()
    PortInterfaces()
    ClientServer()
    ClientServerInterface()
    ClientServerOperation()
    Copy2_ClientServerInterface()
    Copy3_ClientServerInterface()
    Copy4_ClientServerInterface()
    Copy_ClientServerInterface()
    Copy_ModeDeclarationGroup()
    Copy_ModeSwitchInterface()
    ModeDeclarationGroup()
    ModeSwitchInterface()
    NvData()
    Parameter()
    Copy2_SenderReceiverInterface()
    Copy3_SenderReceiverInterface()
    Copy4_SenderReceiverInterface()
    Copy5_SenderReceiverInterface()
    Copy_SenderReceiverInterface()
    SenderReceiverInterface()
    Trigger()
    SWCImpl()
    SwAddrMethods()
    SwComponentTypes()
    ConstantMemory()
    DataTypeMappingSet()
    StaticMemory()
    ArTypedPerInstanceMemory()
    AsynchronousServerCallReturnsEvent()
    ExplicitInterRunnableVariable()
    NoSupport()
    ImplicitInterRunnableVariable()
    PerInstanceParameter()
    Runnable()
    ApplicationSwComponentType_Runnable1()
    ApplicationSwComponentType_Runnable2()
    ApplicationSwComponentType_Runnable3()
    ApplicationSwComponentType_Runnable4()
    ApplicationSwComponentType_Runnable5()
    ApplicationSwComponentType_Runnable6()
    ApplicationSwComponentType_Runnable7()
    ApplicationSwComponentType_Runnable9()
    ApplicationSwComponentType_Runnable10()
    ApplicationSwComponentType_Runnable11()
    ApplicationSwComponentType_Runnable12()
    ApplicationSwComponentType_Runnable13()
    ApplicationSwComponentType_Runnable14()
    ApplicationSwComponentType_Runnable15()
    IRVWA_ExplicitInterRunnableVariable()
    SharedParameter()
    CddSWC()
    CompSWC()
    EcuAbSWC()
    NvDataSWC()
    PrmSWC()
    SnsrActSWC()
    SrvcPrxySWC()
    SrvcSWC()
    Systems()