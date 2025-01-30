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
    'xsi:schemaLocation': "http://autosar.org/schema/r4.0 AUTOSAR_4-1-3.xsd"
})

global_elements = {
    'root': root
}


def ApplicationDataTypes():
    global global_elements
    ar_packages = ET.SubElement(root, 'AR-PACKAGES')
    ar_package = ET.SubElement(ar_packages, 'AR-PACKAGE')
    short_name = ET.SubElement(ar_package, 'SHORT-NAME')
    short_name.text = 'SharedElements'
    ar_packages2 = ET.SubElement(ar_package, 'AR-PACKAGES')
    ar_package2 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    short_name2 = ET.SubElement(ar_package2, 'SHORT-NAME')
    short_name2.text = 'ApplicationDataTypes'
    ar_packages3 = ET.SubElement(ar_package2, 'AR-PACKAGES')
    ar_package3 = ET.SubElement(ar_packages3, 'AR-PACKAGE')
    ar_package3.attrib = {'UUID': '035a8ab9-015a-426c-8766-e4b58e5c5a98'}
    short_name3 = ET.SubElement(ar_package3, 'SHORT-NAME')
    short_name3.text = 'Array'
    elements = ET.SubElement(ar_package3, 'ELEMENTS')

def ApplicationArrayDataType_Fixed():
    application_array_data_type = ET.SubElement(elements, 'APPLICATION-ARRAY-DATA-TYPE')
    application_array_data_type.attrib = {'UUID': '99540e2c-05ec-4a85-94bb-9a3999ac57fe'}
    short_name4 = ET.SubElement(application_array_data_type, 'SHORT-NAME')
    short_name4.text = 'ApplicationArrayDataType_Fixed'
    category = ET.SubElement(application_array_data_type, 'CATEGORY')
    category.text = 'ARRAY'
    element = ET.SubElement(application_array_data_type, 'ELEMENT')
    element.attrib = {'UUID': '7391c5fe-50b6-4b88-bc63-ec1975221a4f'}
    short_name5 = ET.SubElement(element, 'SHORT-NAME')
    short_name5.text = 'Element'
    category2 = ET.SubElement(element, 'CATEGORY')
    category2.text = 'VALUE'
    type_tref = ET.SubElement(element, 'TYPE-TREF')
    type_tref.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    array_size_semantics = ET.SubElement(element, 'ARRAY-SIZE-SEMANTICS')
    array_size_semantics.text = 'FIXED-SIZE'
    max_number_of_elements = ET.SubElement(element, 'MAX-NUMBER-OF-ELEMENTS')
    max_number_of_elements.text = '15'

def ApplicationArrayDataType_Variable():
    application_array_data_type2 = ET.SubElement(elements1, 'APPLICATION-ARRAY-DATA-TYPE')
    application_array_data_type2.attrib = {'UUID': 'd5f3c7e9-dd94-4d37-888e-b6e44b01cc5a'}
    short_name6 = ET.SubElement(application_array_data_type2, 'SHORT-NAME')
    short_name6.text = 'ApplicationArrayDataType_Variable'
    category3 = ET.SubElement(application_array_data_type2, 'CATEGORY')
    category3.text = 'ARRAY'
    element2 = ET.SubElement(application_array_data_type2, 'ELEMENT')
    element2.attrib = {'UUID': 'fef3f4b8-d9bd-4cb1-94b8-4403e665c4fa'}
    short_name7 = ET.SubElement(element2, 'SHORT-NAME')
    short_name7.text = 'Element'
    category4 = ET.SubElement(element2, 'CATEGORY')
    category4.text = 'VALUE'
    type_tref2 = ET.SubElement(element2, 'TYPE-TREF')
    type_tref2.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref2.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    array_size_semantics2 = ET.SubElement(element2, 'ARRAY-SIZE-SEMANTICS')
    array_size_semantics2.text = 'VARIABLE-SIZE'
    max_number_of_elements2 = ET.SubElement(element2, 'MAX-NUMBER-OF-ELEMENTS')
    max_number_of_elements2.text = '15'  

def ApplicationPrimitiveDataType():
    global global_elements
    ar_package4 = ET.SubElement(ar_packages3, 'AR-PACKAGE')
    ar_package4.attrib = {'UUID': 'b142aaa0-2671-41cd-bbc6-78cc30cf22c4'}
    short_name8 = ET.SubElement(ar_package4, 'SHORT-NAME')
    short_name8.text = 'Primitive'
    elements2 = ET.SubElement(ar_package4, 'ELEMENTS')
    application_primitive_data_type = ET.SubElement(elements2, 'APPLICATION-PRIMITIVE-DATA-TYPE')
    application_primitive_data_type.attrib = {'UUID': '18357165-e774-4282-90db-fcb76c7c6727'}
    short_name9 = ET.SubElement(application_primitive_data_type, 'SHORT-NAME')
    short_name9.text = 'ApplicationPrimitiveDataType'
    category5 = ET.SubElement(application_primitive_data_type, 'CATEGORY')
    category5.text = 'VALUE'
    sw_data_def_props = ET.SubElement(application_primitive_data_type, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants = ET.SubElement(sw_data_def_props, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional = ET.SubElement(sw_data_def_props_variants, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access = ET.SubElement(sw_data_def_props_conditional, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access.text = 'NOT-ACCESSIBLE'
    compu_method_ref = ET.SubElement(sw_data_def_props_conditional, 'COMPU-METHOD-REF')
    compu_method_ref.text = '/SharedElements/CompuMethods/CompuMethod'
    compu_method_ref.attrib = {'DEST': 'COMPU-METHOD'}
    data_constr_ref = ET.SubElement(sw_data_def_props_conditional, 'DATA-CONSTR-REF')
    data_constr_ref.text = '/SharedElements/DataConstr/DataConstr'
    data_constr_ref.attrib = {'DEST': 'DATA-CONSTR'}
    invalid_value = ET.SubElement(sw_data_def_props_conditional, 'INVALID-VALUE')
    application_value_specification = ET.SubElement(invalid_value, 'APPLICATION-VALUE-SPECIFICATION')
    category6 = ET.SubElement(application_value_specification, 'CATEGORY')
    category6.text = 'VALUE'
    sw_value_cont = ET.SubElement(application_value_specification, 'SW-VALUE-CONT')
    sw_values_phys = ET.SubElement(sw_value_cont, 'SW-VALUES-PHYS')
    v = ET.SubElement(sw_values_phys, 'V')
    v.text = '8'
    unit_ref = ET.SubElement(sw_data_def_props_conditional, 'UNIT-REF')
    unit_ref.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref.attrib = {'DEST': 'UNIT'}



def Bool_ApplicationPrimitiveDataType():
    global global_elements
    application_primitive_data_type2 = ET.SubElement(elements2, 'APPLICATION-PRIMITIVE-DATA-TYPE')
    application_primitive_data_type2.attrib = {'UUID': '14c56edb-9cf8-48cc-92d7-4cc1ca683a0f'}
    short_name10 = ET.SubElement(application_primitive_data_type2, 'SHORT-NAME')
    short_name10.text = 'Bool_ApplicationPrimitiveDataType'
    category7 = ET.SubElement(application_primitive_data_type2, 'CATEGORY')
    category7.text = 'BOOLEAN'
    sw_data_def_props2 = ET.SubElement(application_primitive_data_type2, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants2 = ET.SubElement(sw_data_def_props2, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional2 = ET.SubElement(sw_data_def_props_variants2, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access2 = ET.SubElement(sw_data_def_props_conditional2, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access2.text = 'NOT-ACCESSIBLE'
    compu_method_ref2 = ET.SubElement(sw_data_def_props_conditional2, 'COMPU-METHOD-REF')
    compu_method_ref2.text = '/SharedElements/CompuMethods/CompuMethod'
    compu_method_ref2.attrib = {'DEST': 'COMPU-METHOD'}
    data_constr_ref2 = ET.SubElement(sw_data_def_props_conditional2, 'DATA-CONSTR-REF')
    data_constr_ref2.text = '/SharedElements/DataConstr/DataConstr'
    data_constr_ref2.attrib = {'DEST': 'DATA-CONSTR'}
    unit_ref2 = ET.SubElement(sw_data_def_props_conditional2, 'UNIT-REF')
    unit_ref2.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref2.attrib = {'DEST': 'UNIT'}

def Copy_ApplicationPrimitiveDataType():
    global global_elements
    application_primitive_data_type3 = ET.SubElement(elements2, 'APPLICATION-PRIMITIVE-DATA-TYPE')
    application_primitive_data_type3.attrib = {'UUID': 'a799e394-8020-4e26-abaf-804ce312d6c0'}
    short_name11 = ET.SubElement(application_primitive_data_type3, 'SHORT-NAME')
    short_name11.text = 'Copy_ApplicationPrimitiveDataType'
    category8 = ET.SubElement(application_primitive_data_type3, 'CATEGORY')
    category8.text = 'VALUE'
    sw_data_def_props3 = ET.SubElement(application_primitive_data_type3, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants3 = ET.SubElement(sw_data_def_props3, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional3 = ET.SubElement(sw_data_def_props_variants3, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access3 = ET.SubElement(sw_data_def_props_conditional3, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access3.text = 'NOT-ACCESSIBLE'
    compu_method_ref3 = ET.SubElement(sw_data_def_props_conditional3, 'COMPU-METHOD-REF')
    compu_method_ref3.text = '/SharedElements/CompuMethods/CompuMethod'
    compu_method_ref3.attrib = {'DEST': 'COMPU-METHOD'}
    data_constr_ref3 = ET.SubElement(sw_data_def_props_conditional3, 'DATA-CONSTR-REF')
    data_constr_ref3.text = '/SharedElements/DataConstr/DataConstr'
    data_constr_ref3.attrib = {'DEST': 'DATA-CONSTR'}
    unit_ref3 = ET.SubElement(sw_data_def_props_conditional3, 'UNIT-REF')
    unit_ref3.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref3.attrib = {'DEST': 'UNIT'}


def String_ApplicationPrimitiveDataType():
    global global_elements
    application_primitive_data_type4 = ET.SubElement(elements2, 'APPLICATION-PRIMITIVE-DATA-TYPE')
    application_primitive_data_type4.attrib = {'UUID': 'decc899e-e751-4907-998b-8769b6445a38'}
    short_name12 = ET.SubElement(application_primitive_data_type4, 'SHORT-NAME')
    short_name12.text = 'String_ApplicationPrimitiveDataType'
    category9 = ET.SubElement(application_primitive_data_type4, 'CATEGORY')
    category9.text = 'STRING'
    sw_data_def_props4 = ET.SubElement(application_primitive_data_type4, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants4 = ET.SubElement(sw_data_def_props4, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional4 = ET.SubElement(sw_data_def_props_variants4, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access4 = ET.SubElement(sw_data_def_props_conditional4, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access4.text = 'NOT-ACCESSIBLE'
    sw_text_props = ET.SubElement(sw_data_def_props_conditional4, 'SW-TEXT-PROPS')
    array_size_semantics3 = ET.SubElement(sw_text_props, 'ARRAY-SIZE-SEMANTICS')
    array_size_semantics3.text = 'VARIABLE-SIZE'
    sw_max_text_size = ET.SubElement(sw_text_props, 'SW-MAX-TEXT-SIZE')
    sw_max_text_size.text = '16'
    unit_ref4 = ET.SubElement(sw_data_def_props_conditional4, 'UNIT-REF')
    unit_ref4.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref4.attrib = {'DEST': 'UNIT'}

def ApplicationRecordDataType():
    global global_elements
    ar_package5 = ET.SubElement(ar_packages3, 'AR-PACKAGE')
    ar_package5.attrib = {'UUID': '65217d8d-3662-4a20-a643-ec9ee94de7a0'}
    short_name13 = ET.SubElement(ar_package5, 'SHORT-NAME')
    short_name13.text = 'Record'
    elements3 = ET.SubElement(ar_package5, 'ELEMENTS')
    application_record_data_type = ET.SubElement(elements3, 'APPLICATION-RECORD-DATA-TYPE')
    application_record_data_type.attrib = {'UUID': 'd20b1ec6-9940-43c7-beda-f773a805fab6'}
    short_name14 = ET.SubElement(application_record_data_type, 'SHORT-NAME')
    short_name14.text = 'ApplicationRecordDataType'
    category10 = ET.SubElement(application_record_data_type, 'CATEGORY')
    category10.text = 'STRUCTURE'
    elements4 = ET.SubElement(application_record_data_type, 'ELEMENTS')
    application_record_element = ET.SubElement(elements4, 'APPLICATION-RECORD-ELEMENT')
    application_record_element.attrib = {'UUID': 'bd5079b0-6ac0-4d72-a63a-afd373f2bcc5'}
    short_name15 = ET.SubElement(application_record_element, 'SHORT-NAME')
    short_name15.text = 'Element'
    type_tref3 = ET.SubElement(application_record_element, 'TYPE-TREF')
    type_tref3.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref3.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    application_record_element2 = ET.SubElement(elements4, 'APPLICATION-RECORD-ELEMENT')
    application_record_element2.attrib = {'UUID': '12021f0e-9ad1-4df2-bffa-197611387a0a'}
    short_name16 = ET.SubElement(application_record_element2, 'SHORT-NAME')
    short_name16.text = 'Element1'
    type_tref4 = ET.SubElement(application_record_element2, 'TYPE-TREF')
    type_tref4.text = '/SharedElements/ApplicationDataTypes/Array/ApplicationArrayDataType_Fixed'
    type_tref4.attrib = {'DEST': 'APPLICATION-ARRAY-DATA-TYPE'}

def CompuMethods():
    ar_package6 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    short_name17 = ET.SubElement(ar_package6, 'SHORT-NAME')
    short_name17.text = 'CompuMethods'
    elements5 = ET.SubElement(ar_package6, 'ELEMENTS')

def BITFIELD_TEXTTABLE_CompuMethod():
    compu_method = ET.SubElement(elements5, 'COMPU-METHOD')
    compu_method.attrib = {'UUID': 'e51fd87b-fe38-48d5-b94a-c11851da3006'}
    short_name18 = ET.SubElement(compu_method, 'SHORT-NAME')
    short_name18.text = 'BITFIELD_TEXTTABLE_CompuMethod'
    category11 = ET.SubElement(compu_method, 'CATEGORY')
    category11.text = 'BITFIELD_TEXTTABLE'
    unit_ref5 = ET.SubElement(compu_method, 'UNIT-REF')
    unit_ref5.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref5.attrib = {'DEST': 'UNIT'}
    compu_internal_to_phys = ET.SubElement(compu_method, 'COMPU-INTERNAL-TO-PHYS')
    compu_scales = ET.SubElement(compu_internal_to_phys, 'COMPU-SCALES')
    compu_scale = ET.SubElement(compu_scales, 'COMPU-SCALE')
    mask = ET.SubElement(compu_scale, 'MASK')
    mask.text = '0'
    lower_limit = ET.SubElement(compu_scale, 'LOWER-LIMIT')
    lower_limit.text = '0'
    upper_limit = ET.SubElement(compu_scale, 'UPPER-LIMIT')
    upper_limit.text = '0'
    compu_const = ET.SubElement(compu_scale, 'COMPU-CONST')
    vt = ET.SubElement(compu_const, 'VT')
    vt.text = 'xyz'
    compu_scale2 = ET.SubElement(compu_scales, 'COMPU-SCALE')
    mask2 = ET.SubElement(compu_scale2, 'MASK')
    mask2.text = '0'
    lower_limit2 = ET.SubElement(compu_scale2, 'LOWER-LIMIT')
    lower_limit2.text = '1'
    upper_limit2 = ET.SubElement(compu_scale2, 'UPPER-LIMIT')
    upper_limit2.text = '1'
    compu_const2 = ET.SubElement(compu_scale2, 'COMPU-CONST')
    vt2 = ET.SubElement(compu_const2, 'VT')
    vt2.text = 'xyz1'
    compu_scale3 = ET.SubElement(compu_scales, 'COMPU-SCALE')
    mask3 = ET.SubElement(compu_scale3, 'MASK')
    mask3.text = '0'
    lower_limit3 = ET.SubElement(compu_scale3, 'LOWER-LIMIT')
    lower_limit3.text = '2'
    upper_limit3 = ET.SubElement(compu_scale3, 'UPPER-LIMIT')
    upper_limit3.text = '2'
    compu_const3 = ET.SubElement(compu_scale3, 'COMPU-CONST')
    vt3 = ET.SubElement(compu_const3, 'VT')
    vt3.text = 'xyz2'
    compu_scale4 = ET.SubElement(compu_scales, 'COMPU-SCALE')
    mask4 = ET.SubElement(compu_scale4, 'MASK')
    mask4.text = '0'
    lower_limit4 = ET.SubElement(compu_scale4, 'LOWER-LIMIT')
    lower_limit4.text = '3'
    upper_limit4 = ET.SubElement(compu_scale4, 'UPPER-LIMIT')
    upper_limit4.text = '3'
    compu_const4 = ET.SubElement(compu_scale4, 'COMPU-CONST')
    vt4 = ET.SubElement(compu_const4, 'VT')
    vt4.text = 'xyz3'
    compu_scale5 = ET.SubElement(compu_scales, 'COMPU-SCALE')
    mask5 = ET.SubElement(compu_scale5, 'MASK')
    mask5.text = '0'
    lower_limit5 = ET.SubElement(compu_scale5, 'LOWER-LIMIT')
    lower_limit5.text = '4'
    upper_limit5 = ET.SubElement(compu_scale5, 'UPPER-LIMIT')
    upper_limit5.text = '4'
    compu_const5 = ET.SubElement(compu_scale5, 'COMPU-CONST')
    vt5 = ET.SubElement(compu_const5, 'VT')
    vt5.text = 'xyz4'

def CompuMethod():
    compu_method2 = ET.SubElement(elements5, 'COMPU-METHOD')
    compu_method2.attrib = {'UUID': 'a65ae6b6-3eab-43ff-907b-2c8276c8528b'}
    short_name19 = ET.SubElement(compu_method2, 'SHORT-NAME')
    short_name19.text = 'CompuMethod'
    category12 = ET.SubElement(compu_method2, 'CATEGORY')
    category12.text = 'IDENTICAL'
    unit_ref6 = ET.SubElement(compu_method2, 'UNIT-REF')
    unit_ref6.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref6.attrib = {'DEST': 'UNIT'}

def LINEAR_CompuMethod():
    compu_method3 = ET.SubElement(elements5, 'COMPU-METHOD')
    compu_method3.attrib = {'UUID': '386978fd-a90f-4003-b63e-f9e35b6d76b8'}
    short_name20 = ET.SubElement(compu_method3, 'SHORT-NAME')
    short_name20.text = 'LINEAR_CompuMethod'
    category13 = ET.SubElement(compu_method3, 'CATEGORY')
    category13.text = 'LINEAR'
    unit_ref7 = ET.SubElement(compu_method3, 'UNIT-REF')
    unit_ref7.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref7.attrib = {'DEST': 'UNIT'}
    compu_internal_to_phys2 = ET.SubElement(compu_method3, 'COMPU-INTERNAL-TO-PHYS')
    compu_scales2 = ET.SubElement(compu_internal_to_phys2, 'COMPU-SCALES')
    compu_scale6 = ET.SubElement(compu_scales2, 'COMPU-SCALE')
    compu_rational_coeffs = ET.SubElement(compu_scale6, 'COMPU-RATIONAL-COEFFS')
    compu_numerator = ET.SubElement(compu_rational_coeffs, 'COMPU-NUMERATOR')
    v2 = ET.SubElement(compu_numerator, 'V')
    v2.text = '0'
    v3 = ET.SubElement(compu_numerator, 'V')
    v3.text = '1'
    compu_denominator = ET.SubElement(compu_rational_coeffs, 'COMPU-DENOMINATOR')
    v4 = ET.SubElement(compu_denominator, 'V')
    v4.text = '1'
    

def RAT_FUNC_CompuMethod():
    compu_method4 = ET.SubElement(elements5, 'COMPU-METHOD')
    compu_method4.attrib = {'UUID': '74ea35c5-6b05-40a2-b22c-3c1a179a095b'}
    short_name21 = ET.SubElement(compu_method4, 'SHORT-NAME')
    short_name21.text = 'RAT_FUNC_CompuMethod'
    category14 = ET.SubElement(compu_method4, 'CATEGORY')
    category14.text = 'RAT_FUNC'
    unit_ref8 = ET.SubElement(compu_method4, 'UNIT-REF')
    unit_ref8.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref8.attrib = {'DEST': 'UNIT'}
    compu_internal_to_phys3 = ET.SubElement(compu_method4, 'COMPU-INTERNAL-TO-PHYS')
    compu_scales3 = ET.SubElement(compu_internal_to_phys3, 'COMPU-SCALES')
    compu_scale7 = ET.SubElement(compu_scales3, 'COMPU-SCALE')
    compu_rational_coeffs2 = ET.SubElement(compu_scale7, 'COMPU-RATIONAL-COEFFS')
    compu_numerator2 = ET.SubElement(compu_rational_coeffs2, 'COMPU-NUMERATOR')
    v5 = ET.SubElement(compu_numerator2, 'V')
    v5.text = '0'
    v6 = ET.SubElement(compu_numerator2, 'V')
    v6.text = '1'
    v7 = ET.SubElement(compu_numerator2, 'V')
    v7.text = '0'
    compu_denominator2 = ET.SubElement(compu_rational_coeffs2, 'COMPU-DENOMINATOR')
    v8 = ET.SubElement(compu_denominator2, 'V')
    v8.text = '1'
    v9 = ET.SubElement(compu_denominator2, 'V')
    v9.text = '0'
    v10 = ET.SubElement(compu_denominator2, 'V')
    v10.text = '0'


def SCALE_RATIONAL_AND_TEXTTABLE_CompuMethod():
    compu_method5 = ET.SubElement(elements5, 'COMPU-METHOD')
    compu_method5.attrib = {'UUID': 'cb57246c-cf48-448f-b8a5-5f319b76ee49'}
    short_name22 = ET.SubElement(compu_method5, 'SHORT-NAME')
    short_name22.text = 'SCALE_RATIONAL_AND_TEXTTABLE_CompuMethod'
    desc = ET.SubElement(compu_method5, 'DESC')
    l_2 = ET.SubElement(desc, 'L-2')
    l_2.text = 'S'
    l_2.attrib = {'L': 'FOR-ALL'}
    category15 = ET.SubElement(compu_method5, 'CATEGORY')
    category15.text = 'SCALE_RATIONAL_AND_TEXTTABLE'
    unit_ref9 = ET.SubElement(compu_method5, 'UNIT-REF')
    unit_ref9.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref9.attrib = {'DEST': 'UNIT'}
    compu_internal_to_phys4 = ET.SubElement(compu_method5, 'COMPU-INTERNAL-TO-PHYS')
    compu_scales4 = ET.SubElement(compu_internal_to_phys4, 'COMPU-SCALES')
    compu_scale8 = ET.SubElement(compu_scales4, 'COMPU-SCALE')
    lower_limit6 = ET.SubElement(compu_scale8, 'LOWER-LIMIT')
    lower_limit6.text = '0'
    upper_limit6 = ET.SubElement(compu_scale8, 'UPPER-LIMIT')
    upper_limit6.text = '15'
    compu_rational_coeffs3 = ET.SubElement(compu_scale8, 'COMPU-RATIONAL-COEFFS')
    compu_numerator3 = ET.SubElement(compu_rational_coeffs3, 'COMPU-NUMERATOR')
    v11 = ET.SubElement(compu_numerator3, 'V')
    v11.text = '0'
    v12 = ET.SubElement(compu_numerator3, 'V')
    v12.text = '1'
    v13 = ET.SubElement(compu_numerator3, 'V')
    v13.text = '0'
    compu_denominator3 = ET.SubElement(compu_rational_coeffs3, 'COMPU-DENOMINATOR')
    v14 = ET.SubElement(compu_denominator3, 'V')
    v14.text = '1'
    v15 = ET.SubElement(compu_denominator3, 'V')
    v15.text = '0'
    v16 = ET.SubElement(compu_denominator3, 'V')
    v16.text = '0'
    compu_scale9 = ET.SubElement(compu_scales4, 'COMPU-SCALE')
    symbol = ET.SubElement(compu_scale9, 'SYMBOL')
    symbol.text = 'sdcd'
    lower_limit7 = ET.SubElement(compu_scale9, 'LOWER-LIMIT')
    lower_limit7.text = '16'
    upper_limit7 = ET.SubElement(compu_scale9, 'UPPER-LIMIT')
    upper_limit7.text = '16'
    compu_const6 = ET.SubElement(compu_scale9, 'COMPU-CONST')
    vt6 = ET.SubElement(compu_const6, 'VT')
    vt6.text = 'sdcd'
    compu_scale10 = ET.SubElement(compu_scales4, 'COMPU-SCALE')
    symbol2 = ET.SubElement(compu_scale10, 'SYMBOL')
    symbol2.text = 'sdcd1'
    lower_limit8 = ET.SubElement(compu_scale10, 'LOWER-LIMIT')
    lower_limit8.text = '17'
    upper_limit8 = ET.SubElement(compu_scale10, 'UPPER-LIMIT')
    upper_limit8.text = '17'
    compu_const7 = ET.SubElement(compu_scale10, 'COMPU-CONST')
    vt7 = ET.SubElement(compu_const7, 'VT')
    vt7.text = 'sdcd1'
    compu_default_value = ET.SubElement(compu_internal_to_phys4, 'COMPU-DEFAULT-VALUE')
    v17 = ET.SubElement(compu_default_value, 'V')
    v17.text = '17'

def Scale_linear_And_texttable_CompuMethod():
    compu_method6 = ET.SubElement(elements5, 'COMPU-METHOD')
    compu_method6.attrib = {'UUID': '19ee54ef-4447-4987-bcbe-a9d2a743d569'}
    short_name23 = ET.SubElement(compu_method6, 'SHORT-NAME')
    short_name23.text = 'Scale_linear_And_texttable_CompuMethod'
    desc2 = ET.SubElement(compu_method6, 'DESC')
    l_22 = ET.SubElement(desc2, 'L-2')
    l_22.text = 'Scale_linear _And_texttable_CompuMethod'
    l_22.attrib = {'L': 'FOR-ALL'}
    category16 = ET.SubElement(compu_method6, 'CATEGORY')
    category16.text = 'SCALE_LINEAR_AND_TEXTTABLE'
    unit_ref10 = ET.SubElement(compu_method6, 'UNIT-REF')
    unit_ref10.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref10.attrib = {'DEST': 'UNIT'}
    compu_internal_to_phys5 = ET.SubElement(compu_method6, 'COMPU-INTERNAL-TO-PHYS')
    compu_scales5 = ET.SubElement(compu_internal_to_phys5, 'COMPU-SCALES')
    compu_scale11 = ET.SubElement(compu_scales5, 'COMPU-SCALE')
    lower_limit9 = ET.SubElement(compu_scale11, 'LOWER-LIMIT')
    lower_limit9.text = '0'
    upper_limit9 = ET.SubElement(compu_scale11, 'UPPER-LIMIT')
    upper_limit9.text = '7'
    compu_rational_coeffs4 = ET.SubElement(compu_scale11, 'COMPU-RATIONAL-COEFFS')
    compu_numerator4 = ET.SubElement(compu_rational_coeffs4, 'COMPU-NUMERATOR')
    v18 = ET.SubElement(compu_numerator4, 'V')
    v18.text = '0'
    v19 = ET.SubElement(compu_numerator4, 'V')
    v19.text = '1'
    compu_denominator4 = ET.SubElement(compu_rational_coeffs4, 'COMPU-DENOMINATOR')
    v20 = ET.SubElement(compu_denominator4, 'V')
    v20.text = '1'
    compu_scale12 = ET.SubElement(compu_scales5, 'COMPU-SCALE')
    symbol3 = ET.SubElement(compu_scale12, 'SYMBOL')
    symbol3.text = 'abcd'
    lower_limit10 = ET.SubElement(compu_scale12, 'LOWER-LIMIT')
    lower_limit10.text = '8'
    upper_limit10 = ET.SubElement(compu_scale12, 'UPPER-LIMIT')
    upper_limit10.text = '8'
    compu_const8 = ET.SubElement(compu_scale12, 'COMPU-CONST')
    vt8 = ET.SubElement(compu_const8, 'VT')
    vt8.text = 'abcd'
    compu_scale13 = ET.SubElement(compu_scales5, 'COMPU-SCALE')
    symbol4 = ET.SubElement(compu_scale13, 'SYMBOL')
    symbol4.text = 'abcd1'
    lower_limit11 = ET.SubElement(compu_scale13, 'LOWER-LIMIT')
    lower_limit11.text = '9'
    upper_limit11 = ET.SubElement(compu_scale13, 'UPPER-LIMIT')
    upper_limit11.text = '9'
    compu_const9 = ET.SubElement(compu_scale13, 'COMPU-CONST')
    vt9 = ET.SubElement(compu_const9, 'VT')
    vt9.text = 'abcd1'
    compu_default_value2 = ET.SubElement(compu_internal_to_phys5, 'COMPU-DEFAULT-VALUE')
    v21 = ET.SubElement(compu_default_value2, 'V')
    v21.text = '8'


def TAB_NOINTP_CompuMethod():
    compu_method7 = ET.SubElement(elements5, 'COMPU-METHOD')
    compu_method7.attrib = {'UUID': 'd4a62613-2238-4523-b274-2677c5a2235a'}
    short_name24 = ET.SubElement(compu_method7, 'SHORT-NAME')
    short_name24.text = 'TAB_NOINTP_CompuMethod'
    desc3 = ET.SubElement(compu_method7, 'DESC')
    category17 = ET.SubElement(compu_method7, 'CATEGORY')
    category17.text = 'TAB_NOINTP'
    unit_ref11 = ET.SubElement(compu_method7, 'UNIT-REF')
    unit_ref11.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref11.attrib = {'DEST': 'UNIT'}
    compu_internal_to_phys6 = ET.SubElement(compu_method7, 'COMPU-INTERNAL-TO-PHYS')
    compu_scales6 = ET.SubElement(compu_internal_to_phys6, 'COMPU-SCALES')
    compu_scale14 = ET.SubElement(compu_scales6, 'COMPU-SCALE')
    desc4 = ET.SubElement(compu_scale14, 'DESC')
    l_23 = ET.SubElement(desc4, 'L-2')
    l_23.attrib = {'L': 'AA'}
    lower_limit12 = ET.SubElement(compu_scale14, 'LOWER-LIMIT')
    lower_limit12.text = '0'
    upper_limit12 = ET.SubElement(compu_scale14, 'UPPER-LIMIT')
    upper_limit12.text = '0'
    compu_const10 = ET.SubElement(compu_scale14, 'COMPU-CONST')
    v22 = ET.SubElement(compu_const10, 'V')
    v22.text = '10'
    compu_scale15 = ET.SubElement(compu_scales6, 'COMPU-SCALE')
    lower_limit13 = ET.SubElement(compu_scale15, 'LOWER-LIMIT')
    lower_limit13.text = '1'
    upper_limit13 = ET.SubElement(compu_scale15, 'UPPER-LIMIT')
    upper_limit13.text = '1'
    compu_const11 = ET.SubElement(compu_scale15, 'COMPU-CONST')
    v23 = ET.SubElement(compu_const11, 'V')
    v23.text = '9'
    compu_scale16 = ET.SubElement(compu_scales6, 'COMPU-SCALE')
    lower_limit14 = ET.SubElement(compu_scale16, 'LOWER-LIMIT')
    lower_limit14.text = '2'
    upper_limit14 = ET.SubElement(compu_scale16, 'UPPER-LIMIT')
    upper_limit14.text = '2'
    compu_const12 = ET.SubElement(compu_scale16, 'COMPU-CONST')
    v24 = ET.SubElement(compu_const12, 'V')
    v24.text = '8'
    compu_default_value3 = ET.SubElement(compu_internal_to_phys6, 'COMPU-DEFAULT-VALUE')
    vf = ET.SubElement(compu_default_value3, 'VF')
    vf.text = '0'

def TEXTTABLE_CompuMethod():
    compu_method8 = ET.SubElement(elements5, 'COMPU-METHOD')
    compu_method8.attrib = {'UUID': '6ef51214-688c-4e48-a115-d80fcf62bffc'}
    short_name25 = ET.SubElement(compu_method8, 'SHORT-NAME')
    short_name25.text = 'TEXTTABLE_CompuMethod'
    category18 = ET.SubElement(compu_method8, 'CATEGORY')
    category18.text = 'TEXTTABLE'
    unit_ref12 = ET.SubElement(compu_method8, 'UNIT-REF')
    unit_ref12.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref12.attrib = {'DEST': 'UNIT'}
    compu_internal_to_phys7 = ET.SubElement(compu_method8, 'COMPU-INTERNAL-TO-PHYS')
    compu_scales7 = ET.SubElement(compu_internal_to_phys7, 'COMPU-SCALES')
    compu_scale17 = ET.SubElement(compu_scales7, 'COMPU-SCALE')
    symbol5 = ET.SubElement(compu_scale17, 'SYMBOL')
    symbol5.text = 'text1'
    lower_limit15 = ET.SubElement(compu_scale17, 'LOWER-LIMIT')
    lower_limit15.text = '0'
    upper_limit15 = ET.SubElement(compu_scale17, 'UPPER-LIMIT')
    upper_limit15.text = '0'
    compu_const13 = ET.SubElement(compu_scale17, 'COMPU-CONST')
    vt10 = ET.SubElement(compu_const13, 'VT')
    vt10.text = 'text1'
    compu_scale18 = ET.SubElement(compu_scales7, 'COMPU-SCALE')
    symbol6 = ET.SubElement(compu_scale18, 'SYMBOL')
    symbol6.text = 'text2'
    lower_limit16 = ET.SubElement(compu_scale18, 'LOWER-LIMIT')
    lower_limit16.text = '1'
    upper_limit16 = ET.SubElement(compu_scale18, 'UPPER-LIMIT')
    upper_limit16.text = '1'
    compu_const14 = ET.SubElement(compu_scale18, 'COMPU-CONST')
    vt11 = ET.SubElement(compu_const14, 'VT')
    vt11.text = 'text2'
    compu_scale19 = ET.SubElement(compu_scales7, 'COMPU-SCALE')
    symbol7 = ET.SubElement(compu_scale19, 'SYMBOL')
    symbol7.text = 'text3'
    lower_limit17 = ET.SubElement(compu_scale19, 'LOWER-LIMIT')
    lower_limit17.text = '2'
    upper_limit17 = ET.SubElement(compu_scale19, 'UPPER-LIMIT')
    upper_limit17.text = '2'
    compu_const15 = ET.SubElement(compu_scale19, 'COMPU-CONST')
    vt12 = ET.SubElement(compu_const15, 'VT')
    vt12.text = 'text3'
    compu_scale20 = ET.SubElement(compu_scales7, 'COMPU-SCALE')
    symbol8 = ET.SubElement(compu_scale20, 'SYMBOL')
    symbol8.text = 'text4'
    lower_limit18 = ET.SubElement(compu_scale20, 'LOWER-LIMIT')
    lower_limit18.text = '3'
    upper_limit18 = ET.SubElement(compu_scale20, 'UPPER-LIMIT')
    upper_limit18.text = '3'
    compu_const16 = ET.SubElement(compu_scale20, 'COMPU-CONST')
    vt13 = ET.SubElement(compu_const16, 'VT')
    vt13.text = 'text4'
    compu_default_value4 = ET.SubElement(compu_internal_to_phys7, 'COMPU-DEFAULT-VALUE')
    v25 = ET.SubElement(compu_default_value4, 'V')
    v25.text = '0'

def ApplicationSwComponentType_ExplicitInterRunnableVariable():
    # ar_package7 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    # short_name26 = ET.SubElement(ar_package7, 'SHORT-NAME')
    # short_name26.text = 'ConstantSpecifications'
    # elements6 = ET.SubElement(ar_package7, 'ELEMENTS')
    constant_specification = ET.SubElement(elements6, 'CONSTANT-SPECIFICATION')
    constant_specification.attrib = {'UUID': '5679b253-a22a-4532-8116-7ce8ac35a562'}
    short_name27 = ET.SubElement(constant_specification, 'SHORT-NAME')
    short_name27.text = 'ApplicationSwComponentType_ExplicitInterRunnableVariable'
    value_spec = ET.SubElement(constant_specification, 'VALUE-SPEC')
    numerical_value_specification = ET.SubElement(value_spec, 'NUMERICAL-VALUE-SPECIFICATION')
    short_label = ET.SubElement(numerical_value_specification, 'SHORT-LABEL')
    short_label.text = 'Value'
    value = ET.SubElement(numerical_value_specification, 'VALUE')
    value.text = '0'


def ApplicationSwComponentType_SharedParameter():
    constant_specification2 = ET.SubElement(elements6, 'CONSTANT-SPECIFICATION')
    constant_specification2.attrib = {'UUID': '82a61fa2-2547-4ce8-a0d4-c583629db923'}
    short_name28 = ET.SubElement(constant_specification2, 'SHORT-NAME')
    short_name28.text = 'ApplicationSwComponentType_SharedParameter'
    value_spec2 = ET.SubElement(constant_specification2, 'VALUE-SPEC')
    numerical_value_specification2 = ET.SubElement(value_spec2, 'NUMERICAL-VALUE-SPECIFICATION')
    short_label2 = ET.SubElement(numerical_value_specification2, 'SHORT-LABEL')
    short_label2.text = 'Value'
    value2 = ET.SubElement(numerical_value_specification2, 'VALUE')
    value2.text = '5.5'


def ApplicationSwComponentType_StaticMemory():
    constant_specification3 = ET.SubElement(elements6, 'CONSTANT-SPECIFICATION')
    constant_specification3.attrib = {'UUID': 'e3a2b67f-9cda-465d-8b6f-f31127e7b3a1'}
    short_name29 = ET.SubElement(constant_specification3, 'SHORT-NAME')
    short_name29.text = 'ApplicationSwComponentType_StaticMemory'
    value_spec3 = ET.SubElement(constant_specification3, 'VALUE-SPEC')
    numerical_value_specification3 = ET.SubElement(value_spec3, 'NUMERICAL-VALUE-SPECIFICATION')
    short_label3 = ET.SubElement(numerical_value_specification3, 'SHORT-LABEL')
    short_label3.text = 'Value'
    value3 = ET.SubElement(numerical_value_specification3, 'VALUE')
    value3.text = '9'


def ConstantSpecification():
    constant_specification4 = ET.SubElement(elements6, 'CONSTANT-SPECIFICATION')
    constant_specification4.attrib = {'UUID': '3c303401-cc30-49f7-a7cb-0cf2844a3f18'}
    short_name30 = ET.SubElement(constant_specification4, 'SHORT-NAME')
    short_name30.text = 'ConstantSpecification'


def ConstantSpecificationMappingSet():
    # ar_package8 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    # ar_package8.attrib = {'UUID': '6fcb326d-7f82-4cd3-9429-fa90f212d1e8'}
    # short_name31 = ET.SubElement(ar_package8, 'SHORT-NAME')
    # short_name31.text = 'ConstantTypeMappingSets'
    # elements7 = ET.SubElement(ar_package8, 'ELEMENTS')
    constant_specification_mapping_set = ET.SubElement(elements7, 'CONSTANT-SPECIFICATION-MAPPING-SET')
    constant_specification_mapping_set.attrib = {'UUID': '4f3bdbd1-af02-46e6-a3ba-411118807380'}
    short_name32 = ET.SubElement(constant_specification_mapping_set, 'SHORT-NAME')
    short_name32.text = 'ConstantSpecificationMappingSet'

def DataConstr():
    # ar_package9 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    # ar_package9.attrib = {'UUID': '5b7c99d1-d4ef-481b-95e4-0d6975de4f3b'}
    # short_name33 = ET.SubElement(ar_package9, 'SHORT-NAME')
    # short_name33.text = 'DataConstr'
    # elements8 = ET.SubElement(ar_package9, 'ELEMENTS')
    data_constr = ET.SubElement(elements8, 'DATA-CONSTR')
    data_constr.attrib = {'UUID': '78b9384e-7f45-4396-b617-a03a03aaf3ce'}
    short_name34 = ET.SubElement(data_constr, 'SHORT-NAME')
    short_name34.text = 'DataConstr'
    data_constr_rules = ET.SubElement(data_constr, 'DATA-CONSTR-RULES')
    data_constr_rule = ET.SubElement(data_constr_rules, 'DATA-CONSTR-RULE')
    constr_level = ET.SubElement(data_constr_rule, 'CONSTR-LEVEL')
    constr_level.text = '0'
    phys_constrs = ET.SubElement(data_constr_rule, 'PHYS-CONSTRS')
    lower_limit19 = ET.SubElement(phys_constrs, 'LOWER-LIMIT')
    lower_limit19.text = '0'
    upper_limit19 = ET.SubElement(phys_constrs, 'UPPER-LIMIT')
    upper_limit19.text = '7'

def DataTypemappingSets():
    # ar_package10 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    # ar_package10.attrib = {'UUID': '463cbb86-4f8e-463e-8bb3-dafc528ccbdf'}
    # short_name35 = ET.SubElement(ar_package10, 'SHORT-NAME')
    # short_name35.text = 'DataTypemappingSets'
    # elements9 = ET.SubElement(ar_package10, 'ELEMENTS')
    data_type_mapping_set = ET.SubElement(elements9, 'DATA-TYPE-MAPPING-SET')
    data_type_mapping_set.attrib = {'UUID': '84bab728-8c47-495c-a5d4-5290c3551358'}
    short_name36 = ET.SubElement(data_type_mapping_set, 'SHORT-NAME')
    short_name36.text = 'DataTypeMappingSet'
    data_type_maps = ET.SubElement(data_type_mapping_set, 'DATA-TYPE-MAPS')
    data_type_map = ET.SubElement(data_type_maps, 'DATA-TYPE-MAP')
    application_data_type_ref = ET.SubElement(data_type_map, 'APPLICATION-DATA-TYPE-REF')
    application_data_type_ref.text = '/SharedElements/ApplicationDataTypes/Array/ApplicationArrayDataType_Fixed'
    application_data_type_ref.attrib = {'DEST': 'APPLICATION-ARRAY-DATA-TYPE'}
    implementation_data_type_ref = ET.SubElement(data_type_map, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref.text = '/SharedElements/ImplementationDataTypes/ARRAY_ImplementationDataType'
    implementation_data_type_ref.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    data_type_map2 = ET.SubElement(data_type_maps, 'DATA-TYPE-MAP')
    application_data_type_ref2 = ET.SubElement(data_type_map2, 'APPLICATION-DATA-TYPE-REF')
    application_data_type_ref2.text = '/SharedElements/ApplicationDataTypes/Record/ApplicationRecordDataType'
    application_data_type_ref2.attrib = {'DEST': 'APPLICATION-RECORD-DATA-TYPE'}
    implementation_data_type_ref2 = ET.SubElement(data_type_map2, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref2.text = '/SharedElements/ImplementationDataTypes/STRUCTURE_ImplementationDataType1'
    implementation_data_type_ref2.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    data_type_map3 = ET.SubElement(data_type_maps, 'DATA-TYPE-MAP')
    application_data_type_ref3 = ET.SubElement(data_type_map3, 'APPLICATION-DATA-TYPE-REF')
    application_data_type_ref3.text = '/SharedElements/ApplicationDataTypes/Array/ApplicationArrayDataType_Variable'
    application_data_type_ref3.attrib = {'DEST': 'APPLICATION-ARRAY-DATA-TYPE'}
    implementation_data_type_ref3 = ET.SubElement(data_type_map3, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref3.text = '/SharedElements/ImplementationDataTypes/Struct_Array_ImplementationDataType'
    implementation_data_type_ref3.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    data_type_map4 = ET.SubElement(data_type_maps, 'DATA-TYPE-MAP')
    application_data_type_ref4 = ET.SubElement(data_type_map4, 'APPLICATION-DATA-TYPE-REF')
    application_data_type_ref4.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    application_data_type_ref4.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    implementation_data_type_ref4 = ET.SubElement(data_type_map4, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref4.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    implementation_data_type_ref4.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def ImplementationDataTypes():
    # ar_package11 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    # short_name37 = ET.SubElement(ar_package11, 'SHORT-NAME')
    # short_name37.text = 'ImplementationDataTypes'
    # elements10 = ET.SubElement(ar_package11, 'ELEMENTS')
    implementation_data_type = ET.SubElement(elements10, 'IMPLEMENTATION-DATA-TYPE')
    implementation_data_type.attrib = {'UUID': '21f9a013-317d-4a6a-8c1d-cdc72f7df8f5'}
    short_name38 = ET.SubElement(implementation_data_type, 'SHORT-NAME')
    short_name38.text = 'ARRAY_ImplementationDataType'
    category19 = ET.SubElement(implementation_data_type, 'CATEGORY')
    category19.text = 'ARRAY'
    sw_data_def_props5 = ET.SubElement(implementation_data_type, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants5 = ET.SubElement(sw_data_def_props5, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional5 = ET.SubElement(sw_data_def_props_variants5, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sub_elements = ET.SubElement(implementation_data_type, 'SUB-ELEMENTS')
    implementation_data_type_element = ET.SubElement(sub_elements, 'IMPLEMENTATION-DATA-TYPE-ELEMENT')
    implementation_data_type_element.attrib = {'UUID': '5512b8b7-a43f-436f-bb18-47a903ad1e17'}
    short_name39 = ET.SubElement(implementation_data_type_element, 'SHORT-NAME')
    short_name39.text = 'SubElement'
    category20 = ET.SubElement(implementation_data_type_element, 'CATEGORY')
    category20.text = 'TYPE_REFERENCE'
    array_size = ET.SubElement(implementation_data_type_element, 'ARRAY-SIZE')
    array_size.text = '15'
    array_size_semantics4 = ET.SubElement(implementation_data_type_element, 'ARRAY-SIZE-SEMANTICS')
    array_size_semantics4.text = 'FIXED-SIZE'
    sw_data_def_props6 = ET.SubElement(implementation_data_type_element, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants6 = ET.SubElement(sw_data_def_props6, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional6 = ET.SubElement(sw_data_def_props_variants6, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    implementation_data_type_ref5 = ET.SubElement(sw_data_def_props_conditional6, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref5.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    implementation_data_type_ref5.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def ARRAY_ImplementationDataType1():
    implementation_data_type2 = ET.SubElement(elements10, 'IMPLEMENTATION-DATA-TYPE')
    implementation_data_type2.attrib = {'UUID': 'f01098ff-1c78-439e-9476-11d641870637'}
    short_name40 = ET.SubElement(implementation_data_type2, 'SHORT-NAME')
    short_name40.text = 'ARRAY_ImplementationDataType1'
    category21 = ET.SubElement(implementation_data_type2, 'CATEGORY')
    category21.text = 'ARRAY'
    sub_elements2 = ET.SubElement(implementation_data_type2, 'SUB-ELEMENTS')
    implementation_data_type_element2 = ET.SubElement(sub_elements2, 'IMPLEMENTATION-DATA-TYPE-ELEMENT')
    implementation_data_type_element2.attrib = {'UUID': 'ee36cc86-25eb-4048-8698-d1ec326fda32'}
    short_name41 = ET.SubElement(implementation_data_type_element2, 'SHORT-NAME')
    short_name41.text = 'SubElement'
    category22 = ET.SubElement(implementation_data_type_element2, 'CATEGORY')
    category22.text = 'TYPE_REFERENCE'
    array_size2 = ET.SubElement(implementation_data_type_element2, 'ARRAY-SIZE')
    array_size2.text = '15'
    array_size_semantics5 = ET.SubElement(implementation_data_type_element2, 'ARRAY-SIZE-SEMANTICS')
    array_size_semantics5.text = 'VARIABLE-SIZE'
    sw_data_def_props7 = ET.SubElement(implementation_data_type_element2, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants7 = ET.SubElement(sw_data_def_props7, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional7 = ET.SubElement(sw_data_def_props_variants7, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    implementation_data_type_ref6 = ET.SubElement(sw_data_def_props_conditional7, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref6.text = '/SharedElements/ImplementationDataTypes/STRUCTURE_ImplementationDataType1'
    implementation_data_type_ref6.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def ImplementationDataType():
    implementation_data_type3 = ET.SubElement(elements10, 'IMPLEMENTATION-DATA-TYPE')
    implementation_data_type3.attrib = {'UUID': '77ef0bea-be4b-4dea-b5ea-114e5a3f3d26'}
    short_name42 = ET.SubElement(implementation_data_type3, 'SHORT-NAME')
    short_name42.text = 'ImplementationDataType'
    category23 = ET.SubElement(implementation_data_type3, 'CATEGORY')
    category23.text = 'VALUE'
    sw_data_def_props8 = ET.SubElement(implementation_data_type3, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants8 = ET.SubElement(sw_data_def_props8, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional8 = ET.SubElement(sw_data_def_props_variants8, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    base_type_ref = ET.SubElement(sw_data_def_props_conditional8, 'BASE-TYPE-REF')
    base_type_ref.text = '/AUTOSAR/AUTOSAR_Platform/BaseTypes/uint8'
    base_type_ref.attrib = {'DEST': 'SW-BASE-TYPE'}

def STRUCTURE_ImplementationDataType1():
    implementation_data_type4 = ET.SubElement(elements10, 'IMPLEMENTATION-DATA-TYPE')
    implementation_data_type4.attrib = {'UUID': '53ec3bfc-5a92-4d42-b31b-8e29e99a2b46'}
    short_name43 = ET.SubElement(implementation_data_type4, 'SHORT-NAME')
    short_name43.text = 'STRUCTURE_ImplementationDataType1'
    category24 = ET.SubElement(implementation_data_type4, 'CATEGORY')
    category24.text = 'STRUCTURE'
    sub_elements3 = ET.SubElement(implementation_data_type4, 'SUB-ELEMENTS')

def STRUCTURE_ImplementationDataType1_SubElement():
    implementation_data_type_element3 = ET.SubElement(sub_elements3, 'IMPLEMENTATION-DATA-TYPE-ELEMENT')
    implementation_data_type_element3.attrib = {'UUID': '31f01782-3ce8-4dbe-81d1-0d5fb89bef99'}
    short_name44 = ET.SubElement(implementation_data_type_element3, 'SHORT-NAME')
    short_name44.text = 'SubElement'
    category25 = ET.SubElement(implementation_data_type_element3, 'CATEGORY')
    category25.text = 'TYPE_REFERENCE'
    sw_data_def_props9 = ET.SubElement(implementation_data_type_element3, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants9 = ET.SubElement(sw_data_def_props9, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional9 = ET.SubElement(sw_data_def_props_variants9, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    implementation_data_type_ref7 = ET.SubElement(sw_data_def_props_conditional9, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref7.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    implementation_data_type_ref7.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def STRUCTURE_ImplementationDataType1_SubElement1():
    implementation_data_type_element4 = ET.SubElement(sub_elements3, 'IMPLEMENTATION-DATA-TYPE-ELEMENT')
    implementation_data_type_element4.attrib = {'UUID': '83bd06cb-a4ff-4d55-bd3d-1a691b582d46'}
    short_name45 = ET.SubElement(implementation_data_type_element4, 'SHORT-NAME')
    short_name45.text = 'SubElement1'
    category26 = ET.SubElement(implementation_data_type_element4, 'CATEGORY')
    category26.text = 'TYPE_REFERENCE'
    sw_data_def_props10 = ET.SubElement(implementation_data_type_element4, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants10 = ET.SubElement(sw_data_def_props10, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional10 = ET.SubElement(sw_data_def_props_variants10, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    implementation_data_type_ref8 = ET.SubElement(sw_data_def_props_conditional10, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref8.text = '/SharedElements/ImplementationDataTypes/ARRAY_ImplementationDataType'
    implementation_data_type_ref8.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Struct_Array_ImplementationDataType():
    implementation_data_type5 = ET.SubElement(elements10, 'IMPLEMENTATION-DATA-TYPE')
    implementation_data_type5.attrib = {'UUID': 'ccd15817-26a8-424d-8c87-3f3d70b5ee9d'}
    short_name46 = ET.SubElement(implementation_data_type5, 'SHORT-NAME')
    short_name46.text = 'Struct_Array_ImplementationDataType'
    category27 = ET.SubElement(implementation_data_type5, 'CATEGORY')
    category27.text = 'STRUCTURE'    
    sub_elements4 = ET.SubElement(implementation_data_type5, 'SUB-ELEMENTS')

def Struct_Array_ImplementationDataType_SubElement1():
    implementation_data_type_element5 = ET.SubElement(sub_elements4, 'IMPLEMENTATION-DATA-TYPE-ELEMENT')
    implementation_data_type_element5.attrib = {'UUID': '3f61bc0d-d829-4ab0-9e22-7de6a25972e3'}
    short_name47 = ET.SubElement(implementation_data_type_element5, 'SHORT-NAME')
    short_name47.text = 'SubElement1'
    category28 = ET.SubElement(implementation_data_type_element5, 'CATEGORY')
    category28.text = 'TYPE_REFERENCE'
    sw_data_def_props11 = ET.SubElement(implementation_data_type_element5, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants11 = ET.SubElement(sw_data_def_props11, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional11 = ET.SubElement(sw_data_def_props_variants11, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    implementation_data_type_ref9 = ET.SubElement(sw_data_def_props_conditional11, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref9.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    implementation_data_type_ref9.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Struct_Array_ImplementationDataType_SubElement():
    implementation_data_type_element6 = ET.SubElement(sub_elements4, 'IMPLEMENTATION-DATA-TYPE-ELEMENT')
    implementation_data_type_element6.attrib = {'UUID': 'dc530c9c-3b65-4707-99c3-842e2d2b7788'}
    short_name48 = ET.SubElement(implementation_data_type_element6, 'SHORT-NAME')
    short_name48.text = 'SubElement'
    category29 = ET.SubElement(implementation_data_type_element6, 'CATEGORY')
    category29.text = 'ARRAY'
    sub_elements5 = ET.SubElement(implementation_data_type_element6, 'SUB-ELEMENTS')

def Struct_Array_ImplementationDataType_SubElement_TYPE_REFERENCE():
    implementation_data_type_element7 = ET.SubElement(sub_elements5, 'IMPLEMENTATION-DATA-TYPE-ELEMENT')
    implementation_data_type_element7.attrib = {'UUID': 'af21d788-9aea-4789-b7d0-8665f2d0c8c7'}
    short_name49 = ET.SubElement(implementation_data_type_element7, 'SHORT-NAME')
    short_name49.text = 'SubElement'
    category30 = ET.SubElement(implementation_data_type_element7, 'CATEGORY')
    category30.text = 'TYPE_REFERENCE'
    array_size3 = ET.SubElement(implementation_data_type_element7, 'ARRAY-SIZE')
    array_size3.text = '15'
    array_size_semantics6 = ET.SubElement(implementation_data_type_element7, 'ARRAY-SIZE-SEMANTICS')
    array_size_semantics6.text = 'VARIABLE-SIZE'
    sw_data_def_props12 = ET.SubElement(implementation_data_type_element7, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants12 = ET.SubElement(sw_data_def_props12, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional12 = ET.SubElement(sw_data_def_props_variants12, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    implementation_data_type_ref10 = ET.SubElement(sw_data_def_props_conditional12, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref10.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    implementation_data_type_ref10.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    sw_data_def_props13 = ET.SubElement(implementation_data_type_element6, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants13 = ET.SubElement(sw_data_def_props13, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional13 = ET.SubElement(sw_data_def_props_variants13, 'SW-DATA-DEF-PROPS-CONDITIONAL')

def TypeTref_ImplementationDataType():
    implementation_data_type6 = ET.SubElement(elements10, 'IMPLEMENTATION-DATA-TYPE')
    implementation_data_type6.attrib = {'UUID': '79fa9e8f-a805-43da-b4b5-ac42d2a23ff0'}
    short_name50 = ET.SubElement(implementation_data_type6, 'SHORT-NAME')
    short_name50.text = 'TypeTref_ImplementationDataType'
    category31 = ET.SubElement(implementation_data_type6, 'CATEGORY')
    category31.text = 'TYPE_REFERENCE'
    sw_data_def_props14 = ET.SubElement(implementation_data_type6, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants14 = ET.SubElement(sw_data_def_props14, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional14 = ET.SubElement(sw_data_def_props_variants14, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    implementation_data_type_ref11 = ET.SubElement(sw_data_def_props_conditional14, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref11.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float32'
    implementation_data_type_ref11.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

# def PortInterfaces():
#     ar_package12 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
#     short_name51 = ET.SubElement(ar_package12, 'SHORT-NAME')
#     short_name51.text = 'PortInterfaces'
#     ar_packages4 = ET.SubElement(ar_package12, 'AR-PACKAGES')
#     ar_package13 = ET.SubElement(ar_packages4, 'AR-PACKAGE')

# def ClientServer():
#     ar_package13.attrib = {'UUID': 'a0d0a13a-15e8-47a3-8169-5f11ad6c7d3f'}
#     short_name52 = ET.SubElement(ar_package13, 'SHORT-NAME')#     short_name52.text = 'ClientServer'
#     elements11 = ET.SubElement(ar_package13, 'ELEMENTS')

def ClientServerInterface():  
    client_server_interface = ET.SubElement(elements11, 'CLIENT-SERVER-INTERFACE')
    client_server_interface.attrib = {'UUID': 'de068aa3-6af8-4bad-a17f-893dbfa6d08d'}
    short_name53 = ET.SubElement(client_server_interface, 'SHORT-NAME')
    short_name53.text = 'ClientServerInterface'
    is_service = ET.SubElement(client_server_interface, 'IS-SERVICE')
    is_service.text = 'false'

def ClientServerInterface_ClientServereOperation():
    operations = ET.SubElement(client_server_interface, 'OPERATIONS')
    client_server_operation = ET.SubElement(operations, 'CLIENT-SERVER-OPERATION')
    client_server_operation.attrib = {'UUID': 'f963f5c2-07f7-439d-be71-e8ffb77736cb'}
    short_name54 = ET.SubElement(client_server_operation, 'SHORT-NAME')
    short_name54.text = 'Operation'
    arguments = ET.SubElement(client_server_operation, 'ARGUMENTS')
    argument_data_prototype = ET.SubElement(arguments, 'ARGUMENT-DATA-PROTOTYPE')
    argument_data_prototype.attrib = {'UUID': '0757643f-ef26-4951-9974-c0ad09b5c8d0'}
    short_name55 = ET.SubElement(argument_data_prototype, 'SHORT-NAME')
    short_name55.text = 'Argument'
    sw_data_def_props15 = ET.SubElement(argument_data_prototype, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants15 = ET.SubElement(sw_data_def_props15, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional15 = ET.SubElement(sw_data_def_props_variants15, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy = ET.SubElement(sw_data_def_props_conditional15, 'SW-IMPL-POLICY')
    sw_impl_policy.text = 'STANDARD'
    type_tref5 = ET.SubElement(argument_data_prototype, 'TYPE-TREF')
    type_tref5.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref5.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    direction = ET.SubElement(argument_data_prototype, 'DIRECTION')
    direction.text = 'IN'
    server_argument_impl_policy = ET.SubElement(argument_data_prototype, 'SERVER-ARGUMENT-IMPL-POLICY')
    server_argument_impl_policy.text = 'USE-ARGUMENT-TYPE'
  
def ClientServerInterface_ClientServereOperation1():
    client_server_operation2 = ET.SubElement(operations, 'CLIENT-SERVER-OPERATION')
    client_server_operation2.attrib = {'UUID': '9d946ffc-e827-4a3b-9217-80ae67bdce09'}
    short_name56 = ET.SubElement(client_server_operation2, 'SHORT-NAME')
    short_name56.text = 'Operation1'
    arguments2 = ET.SubElement(client_server_operation2, 'ARGUMENTS')
    argument_data_prototype2 = ET.SubElement(arguments2, 'ARGUMENT-DATA-PROTOTYPE')
    argument_data_prototype2.attrib = {'UUID': 'fbd7c03a-e379-467c-9efb-5818113f5e64'}
    short_name57 = ET.SubElement(argument_data_prototype2, 'SHORT-NAME')
    short_name57.text = 'Argument'
    sw_data_def_props16 = ET.SubElement(argument_data_prototype2, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants16 = ET.SubElement(sw_data_def_props16, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional16 = ET.SubElement(sw_data_def_props_variants16, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy2 = ET.SubElement(sw_data_def_props_conditional16, 'SW-IMPL-POLICY')
    sw_impl_policy2.text = 'STANDARD'
    type_tref6 = ET.SubElement(argument_data_prototype2, 'TYPE-TREF')
    type_tref6.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    type_tref6.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    direction2 = ET.SubElement(argument_data_prototype2, 'DIRECTION')
    direction2.text = 'OUT'
    server_argument_impl_policy2 = ET.SubElement(argument_data_prototype2, 'SERVER-ARGUMENT-IMPL-POLICY')
    server_argument_impl_policy2.text = 'USE-ARGUMENT-TYPE'

def Copy2_ClientServerInterface():
    client_server_interface2 = ET.SubElement(elements11, 'CLIENT-SERVER-INTERFACE')
    client_server_interface2.attrib = {'UUID': '68861440-758d-43f6-92a2-fed7438de313'}
    short_name58 = ET.SubElement(client_server_interface2, 'SHORT-NAME')
    short_name58.text = 'Copy2_ClientServerInterface'
    is_service2 = ET.SubElement(client_server_interface2, 'IS-SERVICE')
    is_service2.text = 'false'

def Copy2_ClientServerInterface_ClientServereOperation():
    operations2 = ET.SubElement(client_server_interface2, 'OPERATIONS')
    client_server_operation3 = ET.SubElement(operations2, 'CLIENT-SERVER-OPERATION')
    client_server_operation3.attrib = {'UUID': 'dd8cf435-bddb-45bb-a59d-cffcdd11cedd'}
    short_name59 = ET.SubElement(client_server_operation3, 'SHORT-NAME')
    short_name59.text = 'Operation'
    arguments3 = ET.SubElement(client_server_operation3, 'ARGUMENTS')
    argument_data_prototype3 = ET.SubElement(arguments3, 'ARGUMENT-DATA-PROTOTYPE')
    argument_data_prototype3.attrib = {'UUID': '474b5949-0760-4780-9d06-6d2b549c40e3'}
    short_name60 = ET.SubElement(argument_data_prototype3, 'SHORT-NAME')
    short_name60.text = 'Argument'
    sw_data_def_props17 = ET.SubElement(argument_data_prototype3, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants17 = ET.SubElement(sw_data_def_props17, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional17 = ET.SubElement(sw_data_def_props_variants17, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy3 = ET.SubElement(sw_data_def_props_conditional17, 'SW-IMPL-POLICY')
    sw_impl_policy3.text = 'STANDARD'
    type_tref7 = ET.SubElement(argument_data_prototype3, 'TYPE-TREF')
    type_tref7.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref7.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    direction3 = ET.SubElement(argument_data_prototype3, 'DIRECTION')
    direction3.text = 'IN'
    server_argument_impl_policy3 = ET.SubElement(argument_data_prototype3, 'SERVER-ARGUMENT-IMPL-POLICY')
    server_argument_impl_policy3.text = 'USE-ARGUMENT-TYPE'

def Copy2_ClientServerInterface_ClientServereOperation1():
    client_server_operation4 = ET.SubElement(operations2, 'CLIENT-SERVER-OPERATION')
    client_server_operation4.attrib = {'UUID': 'ceba0008-a280-4915-acc8-c4b28afc10c4'}
    short_name61 = ET.SubElement(client_server_operation4, 'SHORT-NAME')
    short_name61.text = 'Operation1'
    arguments4 = ET.SubElement(client_server_operation4, 'ARGUMENTS')
    argument_data_prototype4 = ET.SubElement(arguments4, 'ARGUMENT-DATA-PROTOTYPE')
    argument_data_prototype4.attrib = {'UUID': '48e7b87f-8674-441c-bc3e-b6143e20802e'}
    short_name62 = ET.SubElement(argument_data_prototype4, 'SHORT-NAME')
    short_name62.text = 'Argument'
    sw_data_def_props18 = ET.SubElement(argument_data_prototype4, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants18 = ET.SubElement(sw_data_def_props18, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional18 = ET.SubElement(sw_data_def_props_variants18, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy4 = ET.SubElement(sw_data_def_props_conditional18, 'SW-IMPL-POLICY')
    sw_impl_policy4.text = 'STANDARD'
    type_tref8 = ET.SubElement(argument_data_prototype4, 'TYPE-TREF')
    type_tref8.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    type_tref8.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    direction4 = ET.SubElement(argument_data_prototype4, 'DIRECTION')
    direction4.text = 'OUT'
    server_argument_impl_policy4 = ET.SubElement(argument_data_prototype4, 'SERVER-ARGUMENT-IMPL-POLICY')
    server_argument_impl_policy4.text = 'USE-ARGUMENT-TYPE'

def Copy3_ClientServerInterface():
    client_server_interface3 = ET.SubElement(elements11, 'CLIENT-SERVER-INTERFACE')
    client_server_interface3.attrib = {'UUID': '9b8ada7b-e7a9-49d6-a945-db726b3bd1f9'}
    short_name63 = ET.SubElement(client_server_interface3, 'SHORT-NAME')
    short_name63.text = 'Copy3_ClientServerInterface'
    is_service3 = ET.SubElement(client_server_interface3, 'IS-SERVICE')
    is_service3.text = 'false'

def Copy3_ClientServerInterface_ClientServereOperation():
    operations3 = ET.SubElement(client_server_interface3, 'OPERATIONS')
    client_server_operation5 = ET.SubElement(operations3, 'CLIENT-SERVER-OPERATION')
    client_server_operation5.attrib = {'UUID': '8b64e196-a577-4332-a8f2-8e907214f2ac'}
    short_name64 = ET.SubElement(client_server_operation5, 'SHORT-NAME')
    short_name64.text = 'Operation'
    arguments5 = ET.SubElement(client_server_operation5, 'ARGUMENTS')
    argument_data_prototype5 = ET.SubElement(arguments5, 'ARGUMENT-DATA-PROTOTYPE')
    argument_data_prototype5.attrib = {'UUID': 'cf106dae-c79b-4cea-a011-2d5ff268ac3e'}
    short_name65 = ET.SubElement(argument_data_prototype5, 'SHORT-NAME')
    short_name65.text = 'Argument'
    sw_data_def_props19 = ET.SubElement(argument_data_prototype5, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants19 = ET.SubElement(sw_data_def_props19, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional19 = ET.SubElement(sw_data_def_props_variants19, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy5 = ET.SubElement(sw_data_def_props_conditional19, 'SW-IMPL-POLICY')
    sw_impl_policy5.text = 'STANDARD'
    type_tref9 = ET.SubElement(argument_data_prototype5, 'TYPE-TREF')
    type_tref9.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref9.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    direction5 = ET.SubElement(argument_data_prototype5, 'DIRECTION')
    direction5.text = 'IN'
    server_argument_impl_policy5 = ET.SubElement(argument_data_prototype5, 'SERVER-ARGUMENT-IMPL-POLICY')
    server_argument_impl_policy5.text = 'USE-ARGUMENT-TYPE'

def Copy3_ClientServerInterface_ClientServereOperation1():
    client_server_operation6 = ET.SubElement(operations3, 'CLIENT-SERVER-OPERATION')
    client_server_operation6.attrib = {'UUID': '03f0b7d8-222c-465d-9663-185446b9f092'}
    short_name66 = ET.SubElement(client_server_operation6, 'SHORT-NAME')
    short_name66.text = 'Operation1'
    arguments6 = ET.SubElement(client_server_operation6, 'ARGUMENTS')
    argument_data_prototype6 = ET.SubElement(arguments6, 'ARGUMENT-DATA-PROTOTYPE')
    argument_data_prototype6.attrib = {'UUID': '9fe53cee-82db-4c74-887a-137d3260eae6'}
    short_name67 = ET.SubElement(argument_data_prototype6, 'SHORT-NAME')
    short_name67.text = 'Argument'
    sw_data_def_props20 = ET.SubElement(argument_data_prototype6, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants20 = ET.SubElement(sw_data_def_props20, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional20 = ET.SubElement(sw_data_def_props_variants20, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy6 = ET.SubElement(sw_data_def_props_conditional20, 'SW-IMPL-POLICY')
    sw_impl_policy6.text = 'STANDARD'
    type_tref10 = ET.SubElement(argument_data_prototype6, 'TYPE-TREF')
    type_tref10.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    type_tref10.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    direction6 = ET.SubElement(argument_data_prototype6, 'DIRECTION')
    direction6.text = 'OUT'
    server_argument_impl_policy6 = ET.SubElement(argument_data_prototype6, 'SERVER-ARGUMENT-IMPL-POLICY')
    server_argument_impl_policy6.text = 'USE-ARGUMENT-TYPE'

def Copy4_ClientServerInterface():
    client_server_interface4 = ET.SubElement(elements11, 'CLIENT-SERVER-INTERFACE')
    client_server_interface4.attrib = {'UUID': 'bc94762b-35e3-49e1-ae8b-70bc63394d9c'}
    short_name68 = ET.SubElement(client_server_interface4, 'SHORT-NAME')
    short_name68.text = 'Copy4_ClientServerInterface'
    is_service4 = ET.SubElement(client_server_interface4, 'IS-SERVICE')
    is_service4.text = 'false'

def Copy4_ClientServerInterface_ClientServereOperation():
    operations4 = ET.SubElement(client_server_interface4, 'OPERATIONS')
    client_server_operation7 = ET.SubElement(operations4, 'CLIENT-SERVER-OPERATION')
    client_server_operation7.attrib = {'UUID': '4f953ec5-5e57-4a1c-bcf2-9eba8fde4ddd'}
    short_name69 = ET.SubElement(client_server_operation7, 'SHORT-NAME')
    short_name69.text = 'Operation'
    arguments7 = ET.SubElement(client_server_operation7, 'ARGUMENTS')
    argument_data_prototype7 = ET.SubElement(arguments7, 'ARGUMENT-DATA-PROTOTYPE')
    argument_data_prototype7.attrib = {'UUID': '573e55c4-304e-48a7-ae98-47c7744d4415'}
    short_name70 = ET.SubElement(argument_data_prototype7, 'SHORT-NAME')
    short_name70.text = 'Argument'
    sw_data_def_props21 = ET.SubElement(argument_data_prototype7, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants21 = ET.SubElement(sw_data_def_props21, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional21 = ET.SubElement(sw_data_def_props_variants21, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy7 = ET.SubElement(sw_data_def_props_conditional21, 'SW-IMPL-POLICY')
    sw_impl_policy7.text = 'STANDARD'
    type_tref11 = ET.SubElement(argument_data_prototype7, 'TYPE-TREF')
    type_tref11.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref11.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    direction7 = ET.SubElement(argument_data_prototype7, 'DIRECTION')
    direction7.text = 'IN'
    server_argument_impl_policy7 = ET.SubElement(argument_data_prototype7, 'SERVER-ARGUMENT-IMPL-POLICY')
    server_argument_impl_policy7.text = 'USE-ARGUMENT-TYPE'

def Copy4_ClientServerInterface_ClientServereOperation1():
    client_server_operation8 = ET.SubElement(operations4, 'CLIENT-SERVER-OPERATION')
    client_server_operation8.attrib = {'UUID': '32dd33c4-e167-4858-93d3-bc02d325d12c'}
    short_name71 = ET.SubElement(client_server_operation8, 'SHORT-NAME')
    short_name71.text = 'Operation1'
    arguments8 = ET.SubElement(client_server_operation8, 'ARGUMENTS')
    argument_data_prototype8 = ET.SubElement(arguments8, 'ARGUMENT-DATA-PROTOTYPE')
    argument_data_prototype8.attrib = {'UUID': '28cc5664-0a70-4275-b1a3-3cb7a40597db'}
    short_name72 = ET.SubElement(argument_data_prototype8, 'SHORT-NAME')
    short_name72.text = 'Argument'
    sw_data_def_props22 = ET.SubElement(argument_data_prototype8, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants22 = ET.SubElement(sw_data_def_props22, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional22 = ET.SubElement(sw_data_def_props_variants22, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy8 = ET.SubElement(sw_data_def_props_conditional22, 'SW-IMPL-POLICY')
    sw_impl_policy8.text = 'STANDARD'
    type_tref12 = ET.SubElement(argument_data_prototype8, 'TYPE-TREF')
    type_tref12.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    type_tref12.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    direction8 = ET.SubElement(argument_data_prototype8, 'DIRECTION')
    direction8.text = 'OUT'
    server_argument_impl_policy8 = ET.SubElement(argument_data_prototype8, 'SERVER-ARGUMENT-IMPL-POLICY')
    server_argument_impl_policy8.text = 'USE-ARGUMENT-TYPE'

def Copy_ClientServerInterface():
    client_server_interface5 = ET.SubElement(elements11, 'CLIENT-SERVER-INTERFACE')
    client_server_interface5.attrib = {'UUID': 'ad797ff8-41de-49b7-a6c3-c2dd864f60dd'}
    short_name73 = ET.SubElement(client_server_interface5, 'SHORT-NAME')
    short_name73.text = 'Copy_ClientServerInterface'
    is_service5 = ET.SubElement(client_server_interface5, 'IS-SERVICE')
    is_service5.text = 'false'

def Copy_ClientServerInterface_ClientServereOperation():
    operations5 = ET.SubElement(client_server_interface5, 'OPERATIONS')
    client_server_operation9 = ET.SubElement(operations5, 'CLIENT-SERVER-OPERATION')
    client_server_operation9.attrib = {'UUID': '5d536ac2-edd2-4788-b233-5b0ef32a2022'}
    short_name74 = ET.SubElement(client_server_operation9, 'SHORT-NAME')
    short_name74.text = 'Operation'
    arguments9 = ET.SubElement(client_server_operation9, 'ARGUMENTS')
    argument_data_prototype9 = ET.SubElement(arguments9, 'ARGUMENT-DATA-PROTOTYPE')
    argument_data_prototype9.attrib = {'UUID': '174674f0-498e-41bc-9667-2459277f62ea'}
    short_name75 = ET.SubElement(argument_data_prototype9, 'SHORT-NAME')
    short_name75.text = 'Argument'
    sw_data_def_props23 = ET.SubElement(argument_data_prototype9, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants23 = ET.SubElement(sw_data_def_props23, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional23 = ET.SubElement(sw_data_def_props_variants23, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy9 = ET.SubElement(sw_data_def_props_conditional23, 'SW-IMPL-POLICY')
    sw_impl_policy9.text = 'STANDARD'
    type_tref13 = ET.SubElement(argument_data_prototype9, 'TYPE-TREF')
    type_tref13.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref13.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    direction9 = ET.SubElement(argument_data_prototype9, 'DIRECTION')
    direction9.text = 'IN'
    server_argument_impl_policy9 = ET.SubElement(argument_data_prototype9, 'SERVER-ARGUMENT-IMPL-POLICY')
    server_argument_impl_policy9.text = 'USE-ARGUMENT-TYPE'

def Copy_ClientServerInterface_ClientServereOperation1():
    client_server_operation10 = ET.SubElement(operations5, 'CLIENT-SERVER-OPERATION')
    client_server_operation10.attrib = {'UUID': 'be00c41e-3412-411d-ad74-a6a0feee0ecd'}
    short_name76 = ET.SubElement(client_server_operation10, 'SHORT-NAME')
    short_name76.text = 'Operation1'
    arguments10 = ET.SubElement(client_server_operation10, 'ARGUMENTS')
    argument_data_prototype10 = ET.SubElement(arguments10, 'ARGUMENT-DATA-PROTOTYPE')
    argument_data_prototype10.attrib = {'UUID': '8c68ce17-1680-4ec1-951d-9d9c871aca06'}
    short_name77 = ET.SubElement(argument_data_prototype10, 'SHORT-NAME')
    short_name77.text = 'Argument'
    sw_data_def_props24 = ET.SubElement(argument_data_prototype10, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants24 = ET.SubElement(sw_data_def_props24, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional24 = ET.SubElement(sw_data_def_props_variants24, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy10 = ET.SubElement(sw_data_def_props_conditional24, 'SW-IMPL-POLICY')
    sw_impl_policy10.text = 'STANDARD'
    type_tref14 = ET.SubElement(argument_data_prototype10, 'TYPE-TREF')
    type_tref14.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    type_tref14.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    direction10 = ET.SubElement(argument_data_prototype10, 'DIRECTION')
    direction10.text = 'OUT'
    server_argument_impl_policy10 = ET.SubElement(argument_data_prototype10, 'SERVER-ARGUMENT-IMPL-POLICY')
    server_argument_impl_policy10.text = 'USE-ARGUMENT-TYPE'


def Copy_ModeDeclarationGroup():
    # ar_package14 = ET.SubElement(ar_packages4, 'AR-PACKAGE')
    # ar_package14.attrib = {'UUID': '3503a605-12c8-44be-96cf-4ad548d5d58f'}
    # short_name78 = ET.SubElement(ar_package14, 'SHORT-NAME')
    # short_name78.text = 'ModeSwitch'
    # elements12 = ET.SubElement(ar_package14, 'ELEMENTS')
    mode_declaration_group = ET.SubElement(elements12, 'MODE-DECLARATION-GROUP')
    mode_declaration_group.attrib = {'UUID': 'd1db93d0-7154-468f-b3bc-872d23a7385f'}
    short_name79 = ET.SubElement(mode_declaration_group, 'SHORT-NAME')
    short_name79.text = 'Copy_ModeDeclarationGroup'
    category32 = ET.SubElement(mode_declaration_group, 'CATEGORY')
    category32.text = 'EXPLICIT_ORDER'
    initial_mode_ref = ET.SubElement(mode_declaration_group, 'INITIAL-MODE-REF')
    initial_mode_ref.text = '/SharedElements/PortInterfaces/ModeSwitch/Copy_ModeDeclarationGroup/ModeDeclaration'
    initial_mode_ref.attrib = {'DEST': 'MODE-DECLARATION'}

def Copy_ModeDeclarationGroup_ModeDeclaration():
    mode_declarations = ET.SubElement(mode_declaration_group, 'MODE-DECLARATIONS')
    mode_declaration = ET.SubElement(mode_declarations, 'MODE-DECLARATION')
    mode_declaration.attrib = {'UUID': '2608f59c-87b0-47b2-8cee-8e9c3ba94cac'}
    short_name80 = ET.SubElement(mode_declaration, 'SHORT-NAME')
    short_name80.text = 'ModeDeclaration'
    value4 = ET.SubElement(mode_declaration, 'VALUE')
    value4.text = '0'

def Copy_ModeDeclarationGroup_ModeDeclaration1():
    mode_declaration2 = ET.SubElement(mode_declarations, 'MODE-DECLARATION')
    mode_declaration2.attrib = {'UUID': '7cc2e588-342f-40a3-ad77-b3d49457e996'}
    short_name81 = ET.SubElement(mode_declaration2, 'SHORT-NAME')
    short_name81.text = 'ModeDeclaration1'
    value5 = ET.SubElement(mode_declaration2, 'VALUE')
    value5.text = '1'

def Copy_ModeDeclarationGroup_ModeDeclaration2():
    mode_declaration3 = ET.SubElement(mode_declarations, 'MODE-DECLARATION')
    mode_declaration3.attrib = {'UUID': '278335ee-b40e-4f50-9fc3-164297dafbfd'}
    short_name82 = ET.SubElement(mode_declaration3, 'SHORT-NAME')
    short_name82.text = 'ModeDeclaration2'
    value6 = ET.SubElement(mode_declaration3, 'VALUE')
    value6.text = '2'
    on_transition_value = ET.SubElement(mode_declaration_group, 'ON-TRANSITION-VALUE')
    on_transition_value.text = '3'

def Copy_ModeSwitchInterface():
    mode_switch_interface = ET.SubElement(elements12, 'MODE-SWITCH-INTERFACE')
    mode_switch_interface.attrib = {'UUID': '359238c5-e830-44a4-b8a0-362c11b6864f'}
    short_name83 = ET.SubElement(mode_switch_interface, 'SHORT-NAME')
    short_name83.text = 'Copy_ModeSwitchInterface'
    is_service6 = ET.SubElement(mode_switch_interface, 'IS-SERVICE')
    is_service6.text = 'false'
    mode_group = ET.SubElement(mode_switch_interface, 'MODE-GROUP')
    mode_group.attrib = {'UUID': '5de6bb25-e952-4b16-ad52-f4692d7da6d9'}
    short_name84 = ET.SubElement(mode_group, 'SHORT-NAME')
    short_name84.text = 'ModeGroup'
    type_tref15 = ET.SubElement(mode_group, 'TYPE-TREF')
    type_tref15.text = '/SharedElements/PortInterfaces/ModeSwitch/Copy_ModeDeclarationGroup'
    type_tref15.attrib = {'DEST': 'MODE-DECLARATION-GROUP'}

def ModeDeclarationGroup():
    mode_declaration_group2 = ET.SubElement(elements12, 'MODE-DECLARATION-GROUP')
    mode_declaration_group2.attrib = {'UUID': 'b9ed1cc5-6caf-43d0-b094-3c763b6cbb9a'}
    short_name85 = ET.SubElement(mode_declaration_group2, 'SHORT-NAME')
    short_name85.text = 'ModeDeclarationGroup'
    category33 = ET.SubElement(mode_declaration_group2, 'CATEGORY')
    category33.text = 'ALPHABETIC_ORDER'
    initial_mode_ref2 = ET.SubElement(mode_declaration_group2, 'INITIAL-MODE-REF')
    initial_mode_ref2.text = '/SharedElements/PortInterfaces/ModeSwitch/ModeDeclarationGroup/ModeDeclaration'
    initial_mode_ref2.attrib = {'DEST': 'MODE-DECLARATION'}
    mode_declarations2 = ET.SubElement(mode_declaration_group2, 'MODE-DECLARATIONS')

def ModeDeclarationGroup_ModeDeclaration():
    mode_declaration4 = ET.SubElement(mode_declarations2, 'MODE-DECLARATION')
    mode_declaration4.attrib = {'UUID': 'c1fb19b0-d635-4deb-a718-37e3d20b8878'}
    short_name86 = ET.SubElement(mode_declaration4, 'SHORT-NAME')
    short_name86.text = 'ModeDeclaration'

def ModeDeclarationGroup_ModeDeclaration1():
    mode_declaration5 = ET.SubElement(mode_declarations2, 'MODE-DECLARATION')
    mode_declaration5.attrib = {'UUID': 'a586eb27-c099-42ab-b553-a0fd227d1fe5'}
    short_name87 = ET.SubElement(mode_declaration5, 'SHORT-NAME')
    short_name87.text = 'ModeDeclaration1'

def ModeDeclarationGroup_ModeDeclaration2():
    mode_declaration6 = ET.SubElement(mode_declarations2, 'MODE-DECLARATION')
    mode_declaration6.attrib = {'UUID': 'a891dd23-e1f6-41f0-b669-b383af7bd17e'}
    short_name88 = ET.SubElement(mode_declaration6, 'SHORT-NAME')
    short_name88.text = 'ModeDeclaration2'


def ModeSwitchInterface():
    mode_switch_interface2 = ET.SubElement(elements12, 'MODE-SWITCH-INTERFACE')
    mode_switch_interface2.attrib = {'UUID': '949dcf4f-08eb-4d99-8504-1c613d93f5e9'}
    short_name89 = ET.SubElement(mode_switch_interface2, 'SHORT-NAME')
    short_name89.text = 'ModeSwitchInterface'
    is_service7 = ET.SubElement(mode_switch_interface2, 'IS-SERVICE')
    is_service7.text = 'false'
    mode_group2 = ET.SubElement(mode_switch_interface2, 'MODE-GROUP')
    mode_group2.attrib = {'UUID': '26ede937-ce36-4065-93e5-d8bca12d51cd'}
    short_name90 = ET.SubElement(mode_group2, 'SHORT-NAME')
    short_name90.text = 'ModeGroup'
    type_tref16 = ET.SubElement(mode_group2, 'TYPE-TREF')
    type_tref16.text = '/SharedElements/PortInterfaces/ModeSwitch/ModeDeclarationGroup'
    type_tref16.attrib = {'DEST': 'MODE-DECLARATION-GROUP'}

def NvDataInterface():
    # ar_package15 = ET.SubElement(ar_packages4, 'AR-PACKAGE')
    # ar_package15.attrib = {'UUID': '07677b4a-bc79-4c7b-afa1-581ad642a3dd'}
    # short_name91 = ET.SubElement(ar_package15, 'SHORT-NAME')
    # short_name91.text = 'NvData'
    # elements13 = ET.SubElement(ar_package15, 'ELEMENTS')

    nv_data_interface = ET.SubElement(elements13, 'NV-DATA-INTERFACE')
    nv_data_interface.attrib = {'UUID': '8a4989b3-88e2-4e47-b98f-591e75c76b17'}
    short_name92 = ET.SubElement(nv_data_interface, 'SHORT-NAME')
    short_name92.text = 'NvDataInterface'
    is_service8 = ET.SubElement(nv_data_interface, 'IS-SERVICE')
    is_service8.text = 'false'

def VariableDataPrototype_NvData():
    nv_datas = ET.SubElement(nv_data_interface, 'NV-DATAS')
    variable_data_prototype = ET.SubElement(nv_datas, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype.attrib = {'UUID': '8a84bf2f-0e49-4923-bbc2-7a6606812ef4'}
    short_name93 = ET.SubElement(variable_data_prototype, 'SHORT-NAME')
    short_name93.text = 'NvData'
    sw_data_def_props25 = ET.SubElement(variable_data_prototype, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants25 = ET.SubElement(sw_data_def_props25, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional25 = ET.SubElement(sw_data_def_props_variants25, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy11 = ET.SubElement(sw_data_def_props_conditional25, 'SW-IMPL-POLICY')
    sw_impl_policy11.text = 'STANDARD'
    type_tref17 = ET.SubElement(variable_data_prototype, 'TYPE-TREF')
    type_tref17.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    type_tref17.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def VariableDataPrototype_NvData1():
    variable_data_prototype2 = ET.SubElement(nv_datas, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype2.attrib = {'UUID': '4437f330-788c-4fb4-92e5-9545dfdbd9f0'}
    short_name94 = ET.SubElement(variable_data_prototype2, 'SHORT-NAME')
    short_name94.text = 'NvData1'
    sw_data_def_props26 = ET.SubElement(variable_data_prototype2, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants26 = ET.SubElement(sw_data_def_props26, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional26 = ET.SubElement(sw_data_def_props_variants26, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy12 = ET.SubElement(sw_data_def_props_conditional26, 'SW-IMPL-POLICY')
    sw_impl_policy12.text = 'STANDARD'
    type_tref18 = ET.SubElement(variable_data_prototype2, 'TYPE-TREF')
    type_tref18.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float64'
    type_tref18.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def ParameterInterface():
    # ar_package16 = ET.SubElement(ar_packages4, 'AR-PACKAGE')
    # ar_package16.attrib = {'UUID': '9b48ec34-87aa-4f84-9080-1d3f919ca090'}
    # short_name95 = ET.SubElement(ar_package16, 'SHORT-NAME')
    # short_name95.text = 'Parameter'
    # elements14 = ET.SubElement(ar_package16, 'ELEMENTS')
    parameter_interface = ET.SubElement(elements14, 'PARAMETER-INTERFACE')
    parameter_interface.attrib = {'UUID': '618ca0ee-adf8-43c1-b898-33ea5ca916d8'}
    short_name96 = ET.SubElement(parameter_interface, 'SHORT-NAME')
    short_name96.text = 'ParameterInterface'
    is_service9 = ET.SubElement(parameter_interface, 'IS-SERVICE')
    is_service9.text = 'false'
    parameters = ET.SubElement(parameter_interface, 'PARAMETERS')

def ParameterDataPrototype_Parameter():
    parameter_data_prototype = ET.SubElement(parameters, 'PARAMETER-DATA-PROTOTYPE')
    parameter_data_prototype.attrib = {'UUID': 'd359a294-51b2-461a-b7fb-0de80cf2598a'}
    short_name97 = ET.SubElement(parameter_data_prototype, 'SHORT-NAME')
    short_name97.text = 'Parameter'
    sw_data_def_props27 = ET.SubElement(parameter_data_prototype, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants27 = ET.SubElement(sw_data_def_props27, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional27 = ET.SubElement(sw_data_def_props_variants27, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access5 = ET.SubElement(sw_data_def_props_conditional27, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access5.text = 'READ-WRITE'
    sw_impl_policy13 = ET.SubElement(sw_data_def_props_conditional27, 'SW-IMPL-POLICY')
    sw_impl_policy13.text = 'STANDARD'
    type_tref19 = ET.SubElement(parameter_data_prototype, 'TYPE-TREF')
    type_tref19.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float32'
    type_tref19.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def ParameterDataPrototype_Parameter1():
    parameter_data_prototype2 = ET.SubElement(parameters, 'PARAMETER-DATA-PROTOTYPE')
    parameter_data_prototype2.attrib = {'UUID': 'a60e4821-63b4-4fa4-9f04-983264b2a55f'}
    short_name98 = ET.SubElement(parameter_data_prototype2, 'SHORT-NAME')
    short_name98.text = 'Parameter1'
    sw_data_def_props28 = ET.SubElement(parameter_data_prototype2, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants28 = ET.SubElement(sw_data_def_props28, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional28 = ET.SubElement(sw_data_def_props_variants28, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access6 = ET.SubElement(sw_data_def_props_conditional28, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access6.text = 'READ-WRITE'
    sw_impl_policy14 = ET.SubElement(sw_data_def_props_conditional28, 'SW-IMPL-POLICY')
    sw_impl_policy14.text = 'STANDARD'
    type_tref20 = ET.SubElement(parameter_data_prototype2, 'TYPE-TREF')
    type_tref20.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    type_tref20.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy2_SenderReceiverInterface():
    # ar_package17 = ET.SubElement(ar_packages4, 'AR-PACKAGE')
    # ar_package17.attrib = {'UUID': '304f7bbd-15e6-4f85-b22f-4b02c9a5631c'}
    # short_name99 = ET.SubElement(ar_package17, 'SHORT-NAME')
    # short_name99.text = 'SenderReceiver'
    # elements15 = ET.SubElement(ar_package17, 'ELEMENTS')
    sender_receiver_interface = ET.SubElement(elements15, 'SENDER-RECEIVER-INTERFACE')
    sender_receiver_interface.attrib = {'UUID': '5301b51c-ab80-4717-880a-f53963ebb47d'}
    short_name100 = ET.SubElement(sender_receiver_interface, 'SHORT-NAME')
    short_name100.text = 'Copy2_SenderReceiverInterface'
    is_service10 = ET.SubElement(sender_receiver_interface, 'IS-SERVICE')
    is_service10.text = 'false'
    data_elements = ET.SubElement(sender_receiver_interface, 'DATA-ELEMENTS')

def Copy2_SenderReceiverInterface_VariableDataPrototype_DataElement():
    variable_data_prototype3 = ET.SubElement(data_elements, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype3.attrib = {'UUID': 'd071c034-64ed-44d0-81f0-a0735e373ce3'}
    short_name101 = ET.SubElement(variable_data_prototype3, 'SHORT-NAME')
    short_name101.text = 'DataElement'
    sw_data_def_props29 = ET.SubElement(variable_data_prototype3, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants29 = ET.SubElement(sw_data_def_props29, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional29 = ET.SubElement(sw_data_def_props_variants29, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access7 = ET.SubElement(sw_data_def_props_conditional29, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access7.text = 'READ-WRITE'
    sw_impl_policy15 = ET.SubElement(sw_data_def_props_conditional29, 'SW-IMPL-POLICY')
    sw_impl_policy15.text = 'STANDARD'
    type_tref21 = ET.SubElement(variable_data_prototype3, 'TYPE-TREF')
    type_tref21.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    type_tref21.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy2_SenderReceiverInterface_VariableDataPrototype_DataElement1():
    variable_data_prototype4 = ET.SubElement(data_elements, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype4.attrib = {'UUID': '3afe6629-f986-4006-9ecf-b2902644f64e'}
    short_name102 = ET.SubElement(variable_data_prototype4, 'SHORT-NAME')
    short_name102.text = 'DataElement1'
    sw_data_def_props30 = ET.SubElement(variable_data_prototype4, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants30 = ET.SubElement(sw_data_def_props30, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional30 = ET.SubElement(sw_data_def_props_variants30, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy16 = ET.SubElement(sw_data_def_props_conditional30, 'SW-IMPL-POLICY')
    sw_impl_policy16.text = 'STANDARD'
    type_tref22 = ET.SubElement(variable_data_prototype4, 'TYPE-TREF')
    type_tref22.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    type_tref22.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy3_SenderReceiverInterface():
    sender_receiver_interface2 = ET.SubElement(elements15, 'SENDER-RECEIVER-INTERFACE')
    sender_receiver_interface2.attrib = {'UUID': 'b4591ad1-c21f-4706-8eac-55f6169b8c96'}
    short_name103 = ET.SubElement(sender_receiver_interface2, 'SHORT-NAME')
    short_name103.text = 'Copy3_SenderReceiverInterface'
    is_service11 = ET.SubElement(sender_receiver_interface2, 'IS-SERVICE')
    is_service11.text = 'false'
    data_elements2 = ET.SubElement(sender_receiver_interface2, 'DATA-ELEMENTS')

def Copy3_SenderReceiverInterface_VariableDataPrototype_DataElement():
    variable_data_prototype5 = ET.SubElement(data_elements2, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype5.attrib = {'UUID': 'dd322790-2f29-43dc-93a0-10c5addc7871'}
    short_name104 = ET.SubElement(variable_data_prototype5, 'SHORT-NAME')
    short_name104.text = 'DataElement'
    sw_data_def_props31 = ET.SubElement(variable_data_prototype5, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants31 = ET.SubElement(sw_data_def_props31, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional31 = ET.SubElement(sw_data_def_props_variants31, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access8 = ET.SubElement(sw_data_def_props_conditional31, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access8.text = 'READ-WRITE'
    sw_impl_policy17 = ET.SubElement(sw_data_def_props_conditional31, 'SW-IMPL-POLICY')
    sw_impl_policy17.text = 'STANDARD'
    type_tref23 = ET.SubElement(variable_data_prototype5, 'TYPE-TREF')
    type_tref23.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    type_tref23.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy3_SenderReceiverInterface_VariableDataPrototype_DataElement1():
    variable_data_prototype6 = ET.SubElement(data_elements2, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype6.attrib = {'UUID': '27292aab-8793-404f-b1d0-3128a4ab29bf'}
    short_name105 = ET.SubElement(variable_data_prototype6, 'SHORT-NAME')
    short_name105.text = 'DataElement1'
    sw_data_def_props32 = ET.SubElement(variable_data_prototype6, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants32 = ET.SubElement(sw_data_def_props32, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional32 = ET.SubElement(sw_data_def_props_variants32, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy18 = ET.SubElement(sw_data_def_props_conditional32, 'SW-IMPL-POLICY')
    sw_impl_policy18.text = 'STANDARD'
    type_tref24 = ET.SubElement(variable_data_prototype6, 'TYPE-TREF')
    type_tref24.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    type_tref24.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def Copy4_SenderReceiverInterface():
    sender_receiver_interface3 = ET.SubElement(elements15, 'SENDER-RECEIVER-INTERFACE')
    sender_receiver_interface3.attrib = {'UUID': 'e5b1f8fc-9e46-4d58-b278-cb3461917783'}
    short_name106 = ET.SubElement(sender_receiver_interface3, 'SHORT-NAME')
    short_name106.text = 'Copy4_SenderReceiverInterface'
    is_service12 = ET.SubElement(sender_receiver_interface3, 'IS-SERVICE')
    is_service12.text = 'false'
    data_elements3 = ET.SubElement(sender_receiver_interface3, 'DATA-ELEMENTS')

def Copy4_SenderReceiverInterface_VariableDataPrototype_DataElement():
    variable_data_prototype7 = ET.SubElement(data_elements3, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype7.attrib = {'UUID': '81fa7709-76a3-4e64-8ab6-0302340d9596'}
    short_name107 = ET.SubElement(variable_data_prototype7, 'SHORT-NAME')
    short_name107.text = 'DataElement'
    sw_data_def_props33 = ET.SubElement(variable_data_prototype7, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants33 = ET.SubElement(sw_data_def_props33, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional33 = ET.SubElement(sw_data_def_props_variants33, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access9 = ET.SubElement(sw_data_def_props_conditional33, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access9.text = 'READ-WRITE'
    sw_impl_policy19 = ET.SubElement(sw_data_def_props_conditional33, 'SW-IMPL-POLICY')
    sw_impl_policy19.text = 'STANDARD'
    type_tref25 = ET.SubElement(variable_data_prototype7, 'TYPE-TREF')
    type_tref25.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    type_tref25.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy4_SenderReceiverInterface_VariableDataPrototype_DataElement1():
    variable_data_prototype8 = ET.SubElement(data_elements3, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype8.attrib = {'UUID': '4139b239-b260-44f9-a1b9-26592a9702b7'}
    short_name108 = ET.SubElement(variable_data_prototype8, 'SHORT-NAME')
    short_name108.text = 'DataElement1'
    sw_data_def_props34 = ET.SubElement(variable_data_prototype8, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants34 = ET.SubElement(sw_data_def_props34, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional34 = ET.SubElement(sw_data_def_props_variants34, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy20 = ET.SubElement(sw_data_def_props_conditional34, 'SW-IMPL-POLICY')
    sw_impl_policy20.text = 'STANDARD'
    type_tref26 = ET.SubElement(variable_data_prototype8, 'TYPE-TREF')
    type_tref26.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    type_tref26.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def Copy5_SenderReceiverInterface():
    sender_receiver_interface4 = ET.SubElement(elements15, 'SENDER-RECEIVER-INTERFACE')
    sender_receiver_interface4.attrib = {'UUID': '67583438-372e-4f89-aad7-44d221ba987e'}
    short_name109 = ET.SubElement(sender_receiver_interface4, 'SHORT-NAME')
    short_name109.text = 'Copy5_SenderReceiverInterface'
    is_service13 = ET.SubElement(sender_receiver_interface4, 'IS-SERVICE')
    is_service13.text = 'false'
    data_elements4 = ET.SubElement(sender_receiver_interface4, 'DATA-ELEMENTS')

def Copy5_SenderReceiverInterface_VariableDataPrototype_DataElement():
    variable_data_prototype9 = ET.SubElement(data_elements4, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype9.attrib = {'UUID': 'b67450ea-eee7-49cd-9e1b-696114cdc06b'}
    short_name110 = ET.SubElement(variable_data_prototype9, 'SHORT-NAME')
    short_name110.text = 'DataElement'
    sw_data_def_props35 = ET.SubElement(variable_data_prototype9, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants35 = ET.SubElement(sw_data_def_props35, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional35 = ET.SubElement(sw_data_def_props_variants35, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access10 = ET.SubElement(sw_data_def_props_conditional35, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access10.text = 'READ-WRITE'
    sw_impl_policy21 = ET.SubElement(sw_data_def_props_conditional35, 'SW-IMPL-POLICY')
    sw_impl_policy21.text = 'STANDARD'
    type_tref27 = ET.SubElement(variable_data_prototype9, 'TYPE-TREF')
    type_tref27.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    type_tref27.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy5_SenderReceiverInterface_VariableDataPrototype_DataElement1():
    variable_data_prototype10 = ET.SubElement(data_elements4, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype10.attrib = {'UUID': '6616174f-78ab-48e5-b54f-f0ac623eefa6'}
    short_name111 = ET.SubElement(variable_data_prototype10, 'SHORT-NAME')
    short_name111.text = 'DataElement1'
    sw_data_def_props36 = ET.SubElement(variable_data_prototype10, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants36 = ET.SubElement(sw_data_def_props36, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional36 = ET.SubElement(sw_data_def_props_variants36, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy22 = ET.SubElement(sw_data_def_props_conditional36, 'SW-IMPL-POLICY')
    sw_impl_policy22.text = 'STANDARD'
    type_tref28 = ET.SubElement(variable_data_prototype10, 'TYPE-TREF')
    type_tref28.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    type_tref28.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy_SenderReceiverInterface():
    sender_receiver_interface5 = ET.SubElement(elements15, 'SENDER-RECEIVER-INTERFACE')
    sender_receiver_interface5.attrib = {'UUID': 'c0a51d5f-0a8c-4bdc-a77d-03a338508c6b'}
    short_name112 = ET.SubElement(sender_receiver_interface5, 'SHORT-NAME')
    short_name112.text = 'Copy_SenderReceiverInterface'
    is_service14 = ET.SubElement(sender_receiver_interface5, 'IS-SERVICE')
    is_service14.text = 'false'
    data_elements5 = ET.SubElement(sender_receiver_interface5, 'DATA-ELEMENTS')

def Copy_SenderReceiverInterface_VariableDataPrototype_DataElement():
    variable_data_prototype11 = ET.SubElement(data_elements5, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype11.attrib = {'UUID': 'b7a89eaf-844f-4e6d-b357-dc9976ba211e'}
    short_name113 = ET.SubElement(variable_data_prototype11, 'SHORT-NAME')
    short_name113.text = 'DataElement'
    sw_data_def_props37 = ET.SubElement(variable_data_prototype11, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants37 = ET.SubElement(sw_data_def_props37, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional37 = ET.SubElement(sw_data_def_props_variants37, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access11 = ET.SubElement(sw_data_def_props_conditional37, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access11.text = 'READ-WRITE'
    sw_impl_policy23 = ET.SubElement(sw_data_def_props_conditional37, 'SW-IMPL-POLICY')
    sw_impl_policy23.text = 'STANDARD'
    type_tref29 = ET.SubElement(variable_data_prototype11, 'TYPE-TREF')
    type_tref29.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    type_tref29.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy_SenderReceiverInterface_VariableDataPrototype_DataElement1():
    variable_data_prototype12 = ET.SubElement(data_elements5, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype12.attrib = {'UUID': '373c6d56-b664-4bba-b6bf-37630aed9fef'}
    short_name114 = ET.SubElement(variable_data_prototype12, 'SHORT-NAME')
    short_name114.text = 'DataElement1'
    sw_data_def_props38 = ET.SubElement(variable_data_prototype12, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants38 = ET.SubElement(sw_data_def_props38, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional38 = ET.SubElement(sw_data_def_props_variants38, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy24 = ET.SubElement(sw_data_def_props_conditional38, 'SW-IMPL-POLICY')
    sw_impl_policy24.text = 'STANDARD'
    type_tref30 = ET.SubElement(variable_data_prototype12, 'TYPE-TREF')
    type_tref30.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    type_tref30.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def SenderReceiverInterface():
    sender_receiver_interface6 = ET.SubElement(elements15, 'SENDER-RECEIVER-INTERFACE')
    sender_receiver_interface6.attrib = {'UUID': '5f56a3f5-0f22-429f-a8b9-003d68bbc759'}
    short_name115 = ET.SubElement(sender_receiver_interface6, 'SHORT-NAME')
    short_name115.text = 'SenderReceiverInterface'
    is_service15 = ET.SubElement(sender_receiver_interface6, 'IS-SERVICE')
    is_service15.text = 'false'
    data_elements6 = ET.SubElement(sender_receiver_interface6, 'DATA-ELEMENTS')

def SenderReceiverInterface_VariableDataPrototype_DataElement():
    variable_data_prototype13 = ET.SubElement(data_elements6, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype13.attrib = {'UUID': 'c448fbc4-20d2-443d-bb7a-87585742cfcf'}
    short_name116 = ET.SubElement(variable_data_prototype13, 'SHORT-NAME')
    short_name116.text = 'DataElement'
    sw_data_def_props39 = ET.SubElement(variable_data_prototype13, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants39 = ET.SubElement(sw_data_def_props39, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional39 = ET.SubElement(sw_data_def_props_variants39, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access12 = ET.SubElement(sw_data_def_props_conditional39, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access12.text = 'READ-WRITE'
    sw_impl_policy25 = ET.SubElement(sw_data_def_props_conditional39, 'SW-IMPL-POLICY')
    sw_impl_policy25.text = 'STANDARD'
    type_tref31 = ET.SubElement(variable_data_prototype13, 'TYPE-TREF')
    type_tref31.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref31.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}

def SenderReceiverInterface_VariableDataPrototype_DataElement1():
    variable_data_prototype14 = ET.SubElement(data_elements6, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype14.attrib = {'UUID': '6862a5ea-8794-4906-9f54-50624e9d6044'}
    short_name117 = ET.SubElement(variable_data_prototype14, 'SHORT-NAME')
    short_name117.text = 'DataElement1'
    sw_data_def_props40 = ET.SubElement(variable_data_prototype14, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants40 = ET.SubElement(sw_data_def_props40, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional40 = ET.SubElement(sw_data_def_props_variants40, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy26 = ET.SubElement(sw_data_def_props_conditional40, 'SW-IMPL-POLICY')
    sw_impl_policy26.text = 'STANDARD'
    type_tref32 = ET.SubElement(variable_data_prototype14, 'TYPE-TREF')
    type_tref32.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    type_tref32.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    invalidation_policys = ET.SubElement(sender_receiver_interface6, 'INVALIDATION-POLICYS')
    invalidation_policy = ET.SubElement(invalidation_policys, 'INVALIDATION-POLICY')
    data_element_ref = ET.SubElement(invalidation_policy, 'DATA-ELEMENT-REF')
    data_element_ref.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    data_element_ref.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    handle_invalid = ET.SubElement(invalidation_policy, 'HANDLE-INVALID')
    handle_invalid.text = 'KEEP'

def Trigger():
    # ar_package18 = ET.SubElement(ar_packages4, 'AR-PACKAGE')
    # ar_package18.attrib = {'UUID': '00421379-584f-4dbb-8c9f-d70ad66b8e41'}
    # short_name118 = ET.SubElement(ar_package18, 'SHORT-NAME')
    # short_name118.text = 'Trigger'
    # elements16 = ET.SubElement(ar_package18, 'ELEMENTS')
    trigger_interface = ET.SubElement(elements16, 'TRIGGER-INTERFACE')
    trigger_interface.attrib = {'UUID': '97d54491-56c6-49b9-9812-bb5eadaefa82'}
    short_name119 = ET.SubElement(trigger_interface, 'SHORT-NAME')
    short_name119.text = 'TriggerInterface'
    is_service16 = ET.SubElement(trigger_interface, 'IS-SERVICE')
    is_service16.text = 'false'
    triggers = ET.SubElement(trigger_interface, 'TRIGGERS')
    trigger = ET.SubElement(triggers, 'TRIGGER')
    trigger.attrib = {'UUID': '06d545dc-664d-45fb-be23-8a076bded4b5'}
    short_name120 = ET.SubElement(trigger, 'SHORT-NAME')
    short_name120.text = 'Trigger'
    sw_impl_policy27 = ET.SubElement(trigger, 'SW-IMPL-POLICY')
    sw_impl_policy27.text = 'STANDARD'
    trigger_period = ET.SubElement(trigger, 'TRIGGER-PERIOD')
    cse_code = ET.SubElement(trigger_period, 'CSE-CODE')
    cse_code.text = '6'
    cse_code_factor = ET.SubElement(trigger_period, 'CSE-CODE-FACTOR')
    cse_code_factor.text = '15'
    
def SwcImplementation():
    # ar_package19 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    # ar_package19.attrib = {'UUID': 'a21c4095-c5dd-41b4-8a15-aa23a460a3e9'}
    # short_name121 = ET.SubElement(ar_package19, 'SHORT-NAME')
    # short_name121.text = 'SWCImpl'
    # elements17 = ET.SubElement(ar_package19, 'ELEMENTS')
    swc_implementation = ET.SubElement(elements17, 'SWC-IMPLEMENTATION')
    swc_implementation.attrib = {'UUID': 'a8e1b9bd-bc2d-4bba-8d84-7fb588da487b'}
    short_name122 = ET.SubElement(swc_implementation, 'SHORT-NAME')
    short_name122.text = 'SwcImplementation'
    programming_language = ET.SubElement(swc_implementation, 'PROGRAMMING-LANGUAGE')
    programming_language.text = 'C'
    sw_version = ET.SubElement(swc_implementation, 'SW-VERSION')
    sw_version.text = '1.0.0.0'
    behavior_ref = ET.SubElement(swc_implementation, 'BEHAVIOR-REF')
    behavior_ref.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl'
    behavior_ref.attrib = {'DEST': 'SWC-INTERNAL-BEHAVIOR'}

def ResourceConsumption():
    resource_consumption = ET.SubElement(swc_implementation, 'RESOURCE-CONSUMPTION')
    resource_consumption.attrib = {'UUID': '664bf3d9-9efc-49d1-a4fd-9936922aa5f9'}
    short_name123 = ET.SubElement(resource_consumption, 'SHORT-NAME')
    short_name123.text = 'ResourceConsumption'

def SwAddrMethods_Copy2_SwAddrMethod():
    # ar_package20 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    # ar_package20.attrib = {'UUID': 'fc8b946c-31d4-49d6-8e0c-ff6847ede7f5'}
    # short_name124 = ET.SubElement(ar_package20, 'SHORT-NAME')
    # short_name124.text = 'SwAddrMethods'
    # elements18 = ET.SubElement(ar_package20, 'ELEMENTS')
    sw_addr_method = ET.SubElement(elements18, 'SW-ADDR-METHOD')
    sw_addr_method.attrib = {'UUID': '8a973d95-6644-4157-ab41-c78f7ccbcb2c'}
    short_name125 = ET.SubElement(sw_addr_method, 'SHORT-NAME')
    short_name125.text = 'Copy2_SwAddrMethod'
    memory_allocation_keyword_policy = ET.SubElement(sw_addr_method, 'MEMORY-ALLOCATION-KEYWORD-POLICY')
    memory_allocation_keyword_policy.text = 'ADDR-METHOD-SHORT-NAME'
    section_type = ET.SubElement(sw_addr_method, 'SECTION-TYPE')
    section_type.text = 'CODE'

def SwAddrMethods_Copy_SwAddrMethod():
    sw_addr_method2 = ET.SubElement(elements18, 'SW-ADDR-METHOD')
    sw_addr_method2.attrib = {'UUID': '73ccfb92-d7eb-4aee-b724-b520ed1a3e84'}
    short_name126 = ET.SubElement(sw_addr_method2, 'SHORT-NAME')
    short_name126.text = 'Copy_SwAddrMethod'
    memory_allocation_keyword_policy2 = ET.SubElement(sw_addr_method2, 'MEMORY-ALLOCATION-KEYWORD-POLICY')
    memory_allocation_keyword_policy2.text = 'ADDR-METHOD-SHORT-NAME-AND-ALIGNMENT'
    section_type2 = ET.SubElement(sw_addr_method2, 'SECTION-TYPE')
    section_type2.text = 'CALIBRATION-VARIABLES'

def SwAddrMethods_SwAddrMethod():
    sw_addr_method3 = ET.SubElement(elements18, 'SW-ADDR-METHOD')
    sw_addr_method3.attrib = {'UUID': '59a8a159-68d8-4804-8d3b-76f1a5d48b3c'}
    short_name127 = ET.SubElement(sw_addr_method3, 'SHORT-NAME')
    short_name127.text = 'SwAddrMethod'
    memory_allocation_keyword_policy3 = ET.SubElement(sw_addr_method3, 'MEMORY-ALLOCATION-KEYWORD-POLICY')
    memory_allocation_keyword_policy3.text = 'ADDR-METHOD-SHORT-NAME'
    section_type3 = ET.SubElement(sw_addr_method3, 'SECTION-TYPE')
    section_type3.text = 'CALIBRATION-VARIABLES'

def ApplSWC():
#     ar_package21 = ET.SubElement(ar_packages, 'AR-PACKAGE')
#     short_name128 = ET.SubElement(ar_package21, 'SHORT-NAME')
#     short_name128.text = 'SwComponentTypes'
#     ar_packages5 = ET.SubElement(ar_package21, 'AR-PACKAGES')

    
    ar_package22 = ET.SubElement(ar_packages5, 'AR-PACKAGE')
    ar_package22.attrib = {'UUID': '7e1cfec7-fc85-4615-9df0-46ddc1fdaa09'}
    short_name129 = ET.SubElement(ar_package22, 'SHORT-NAME')
    short_name129.text = 'ApplSWC'
    elements19 = ET.SubElement(ar_package22, 'ELEMENTS')

def ApplicationSwComponentType():
    application_sw_component_type = ET.SubElement(elements19, 'APPLICATION-SW-COMPONENT-TYPE')
    application_sw_component_type.attrib = {'UUID': 'e74b1e65-d39d-460c-8d4d-d95c8a9e12dd'}
    short_name130 = ET.SubElement(application_sw_component_type, 'SHORT-NAME')
    short_name130.text = 'ApplicationSwComponentType'
    ports = ET.SubElement(application_sw_component_type, 'PORTS')

def RPort_SR():
    r_port_prototype = ET.SubElement(ports, 'R-PORT-PROTOTYPE')
    r_port_prototype.attrib = {'UUID': '1ecadefd-df18-4c05-a2d5-803778e62ae1'}
    short_name131 = ET.SubElement(r_port_prototype, 'SHORT-NAME')
    short_name131.text = 'RPort_SR'
    required_interface_tref = ET.SubElement(r_port_prototype, 'REQUIRED-INTERFACE-TREF')
    required_interface_tref.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface'
    required_interface_tref.attrib = {'DEST': 'SENDER-RECEIVER-INTERFACE'}

def PPort_SR():
    p_port_prototype = ET.SubElement(ports, 'P-PORT-PROTOTYPE')
    p_port_prototype.attrib = {'UUID': 'a3e8969f-1dde-4749-af9a-f337b0f053d8'}
    short_name132 = ET.SubElement(p_port_prototype, 'SHORT-NAME')
    short_name132.text = 'PPort_SR'
    provided_interface_tref = ET.SubElement(p_port_prototype, 'PROVIDED-INTERFACE-TREF')
    provided_interface_tref.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface'
    provided_interface_tref.attrib = {'DEST': 'SENDER-RECEIVER-INTERFACE'}

def RPort_CS():
    r_port_prototype2 = ET.SubElement(ports, 'R-PORT-PROTOTYPE')
    r_port_prototype2.attrib = {'UUID': '933a7736-19ea-4662-8301-3fe9991367bc'}
    short_name133 = ET.SubElement(r_port_prototype2, 'SHORT-NAME')
    short_name133.text = 'RPort_CS'
    required_interface_tref2 = ET.SubElement(r_port_prototype2, 'REQUIRED-INTERFACE-TREF')
    required_interface_tref2.text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface'
    required_interface_tref2.attrib = {'DEST': 'CLIENT-SERVER-INTERFACE'}

def PPort_CS():
    p_port_prototype2 = ET.SubElement(ports, 'P-PORT-PROTOTYPE')
    p_port_prototype2.attrib = {'UUID': '38b3145f-1dd8-4a0f-943b-2f6b2d0a4221'}
    short_name134 = ET.SubElement(p_port_prototype2, 'SHORT-NAME')
    short_name134.text = 'PPort_CS'
    provided_interface_tref2 = ET.SubElement(p_port_prototype2, 'PROVIDED-INTERFACE-TREF')
    provided_interface_tref2.text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface'
    provided_interface_tref2.attrib = {'DEST': 'CLIENT-SERVER-INTERFACE'}

def RPort_msi():
    r_port_prototype3 = ET.SubElement(ports, 'R-PORT-PROTOTYPE')
    r_port_prototype3.attrib = {'UUID': '08e53a34-e89a-4c1c-a2d4-9536c0e123af'}
    short_name135 = ET.SubElement(r_port_prototype3, 'SHORT-NAME')
    short_name135.text = 'RPort_msi'
    required_interface_tref3 = ET.SubElement(r_port_prototype3, 'REQUIRED-INTERFACE-TREF')
    required_interface_tref3.text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface'
    required_interface_tref3.attrib = {'DEST': 'MODE-SWITCH-INTERFACE'}

def PPort_msi():
    p_port_prototype3 = ET.SubElement(ports, 'P-PORT-PROTOTYPE')
    p_port_prototype3.attrib = {'UUID': '8ed933c7-270b-45cf-8a3e-206782153f61'}
    short_name136 = ET.SubElement(p_port_prototype3, 'SHORT-NAME')
    short_name136.text = 'PPort_msi'
    provided_interface_tref3 = ET.SubElement(p_port_prototype3, 'PROVIDED-INTERFACE-TREF')
    provided_interface_tref3.text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface'
    provided_interface_tref3.attrib = {'DEST': 'MODE-SWITCH-INTERFACE'}

def RPort_nvd():
    r_port_prototype4 = ET.SubElement(ports, 'R-PORT-PROTOTYPE')
    r_port_prototype4.attrib = {'UUID': '52c8bb91-6599-4bdd-a556-e2b22ab9c73b'}
    short_name137 = ET.SubElement(r_port_prototype4, 'SHORT-NAME')
    short_name137.text = 'RPort_nvd'
    required_interface_tref4 = ET.SubElement(r_port_prototype4, 'REQUIRED-INTERFACE-TREF')
    required_interface_tref4.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface'
    required_interface_tref4.attrib = {'DEST': 'NV-DATA-INTERFACE'}

def PPort_nvd():
    p_port_prototype4 = ET.SubElement(ports, 'P-PORT-PROTOTYPE')
    p_port_prototype4.attrib = {'UUID': 'a69f810c-0a9d-4729-9b49-5b4be2f55ffa'}
    short_name138 = ET.SubElement(p_port_prototype4, 'SHORT-NAME')
    short_name138.text = 'PPort_nvd'
    provided_interface_tref4 = ET.SubElement(p_port_prototype4, 'PROVIDED-INTERFACE-TREF')
    provided_interface_tref4.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface'
    provided_interface_tref4.attrib = {'DEST': 'NV-DATA-INTERFACE'}

def RPort_prm():
    r_port_prototype5 = ET.SubElement(ports, 'R-PORT-PROTOTYPE')
    r_port_prototype5.attrib = {'UUID': '7bee2832-df48-4712-a0cf-9b2f095db921'}
    short_name139 = ET.SubElement(r_port_prototype5, 'SHORT-NAME')
    short_name139.text = 'RPort_prm'
    required_interface_tref5 = ET.SubElement(r_port_prototype5, 'REQUIRED-INTERFACE-TREF')
    required_interface_tref5.text = '/SharedElements/PortInterfaces/Parameter/ParameterInterface'
    required_interface_tref5.attrib = {'DEST': 'PARAMETER-INTERFACE'}

def RPort_trigger():
    r_port_prototype6 = ET.SubElement(ports, 'R-PORT-PROTOTYPE')
    r_port_prototype6.attrib = {'UUID': '9194fa9f-f535-4ef4-ad71-379f00251a5f'}
    short_name140 = ET.SubElement(r_port_prototype6, 'SHORT-NAME')
    short_name140.text = 'RPort_trigger'
    required_interface_tref6 = ET.SubElement(r_port_prototype6, 'REQUIRED-INTERFACE-TREF')
    required_interface_tref6.text = '/SharedElements/PortInterfaces/Trigger/TriggerInterface'
    required_interface_tref6.attrib = {'DEST': 'TRIGGER-INTERFACE'}

def IB_Appl():
    # internal_behaviors = ET.SubElement(application_sw_component_type, 'INTERNAL-BEHAVIORS')
    swc_internal_behavior = ET.SubElement(internal_behaviors, 'SWC-INTERNAL-BEHAVIOR')
    swc_internal_behavior.attrib = {'UUID': 'd0c29733-8863-4bcd-af6a-1579e0a29746'}
    short_name141 = ET.SubElement(swc_internal_behavior, 'SHORT-NAME')
    short_name141.text = 'IB_Appl'
    constant_memorys = ET.SubElement(swc_internal_behavior, 'CONSTANT-MEMORYS')

def ConstantMemory_PDP():
    parameter_data_prototype3 = ET.SubElement(constant_memorys, 'PARAMETER-DATA-PROTOTYPE')
    parameter_data_prototype3.attrib = {'UUID': '666c53b0-408c-4084-8002-71810ad2bea7'}
    short_name142 = ET.SubElement(parameter_data_prototype3, 'SHORT-NAME')
    short_name142.text = 'ConstantMemory'
    sw_data_def_props41 = ET.SubElement(parameter_data_prototype3, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants41 = ET.SubElement(sw_data_def_props41, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional41 = ET.SubElement(sw_data_def_props_variants41, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access13 = ET.SubElement(sw_data_def_props_conditional41, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access13.text = 'READ-WRITE'
    sw_impl_policy28 = ET.SubElement(sw_data_def_props_conditional41, 'SW-IMPL-POLICY')
    sw_impl_policy28.text = 'STANDARD'
    type_tref33 = ET.SubElement(parameter_data_prototype3, 'TYPE-TREF')
    type_tref33.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint64'
    type_tref33.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    init_value = ET.SubElement(parameter_data_prototype3, 'INIT-VALUE')
    numerical_value_specification4 = ET.SubElement(init_value, 'NUMERICAL-VALUE-SPECIFICATION')
    short_label4 = ET.SubElement(numerical_value_specification4, 'SHORT-LABEL')
    short_label4.text = 'Value'
    value7 = ET.SubElement(numerical_value_specification4, 'VALUE')
    value7.text = '3'

def DataTypeMappingSet():
    data_type_mapping_refs = ET.SubElement(swc_internal_behavior, 'DATA-TYPE-MAPPING-REFS')
    data_type_mapping_ref = ET.SubElement(data_type_mapping_refs, 'DATA-TYPE-MAPPING-REF')
    data_type_mapping_ref.text = '/SharedElements/DataTypemappingSets/DataTypeMappingSet'
    data_type_mapping_ref.attrib = {'DEST': 'DATA-TYPE-MAPPING-SET'}

def StaticMemory():
    static_memorys = ET.SubElement(swc_internal_behavior, 'STATIC-MEMORYS')
    variable_data_prototype15 = ET.SubElement(static_memorys, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype15.attrib = {'UUID': '0a83fe83-959c-49d2-abf1-981ac4641b7d'}
    short_name143 = ET.SubElement(variable_data_prototype15, 'SHORT-NAME')
    short_name143.text = 'StaticMemory'
    sw_data_def_props42 = ET.SubElement(variable_data_prototype15, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants42 = ET.SubElement(sw_data_def_props42, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional42 = ET.SubElement(sw_data_def_props_variants42, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy29 = ET.SubElement(sw_data_def_props_conditional42, 'SW-IMPL-POLICY')
    sw_impl_policy29.text = 'STANDARD'
    type_tref34 = ET.SubElement(variable_data_prototype15, 'TYPE-TREF')
    type_tref34.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    type_tref34.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    init_value2 = ET.SubElement(variable_data_prototype15, 'INIT-VALUE')
    constant_reference = ET.SubElement(init_value2, 'CONSTANT-REFERENCE')
    short_label5 = ET.SubElement(constant_reference, 'SHORT-LABEL')
    short_label5.text = 'ReferenceToConstant'
    constant_ref = ET.SubElement(constant_reference, 'CONSTANT-REF')
    constant_ref.text = '/SharedElements/ConstantSpecifications/ApplicationSwComponentType_StaticMemory'
    constant_ref.attrib = {'DEST': 'CONSTANT-SPECIFICATION'}

def ArTypedPerInstanceMemory():
    ar_typed_per_instance_memorys = ET.SubElement(swc_internal_behavior, 'AR-TYPED-PER-INSTANCE-MEMORYS')
    variable_data_prototype16 = ET.SubElement(ar_typed_per_instance_memorys, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype16.attrib = {'UUID': 'c2401b62-709c-4a61-a9d7-5f540d144075'}
    short_name144 = ET.SubElement(variable_data_prototype16, 'SHORT-NAME')
    short_name144.text = 'ArTypedPerInstanceMemory'
    sw_data_def_props43 = ET.SubElement(variable_data_prototype16, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants43 = ET.SubElement(sw_data_def_props43, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional43 = ET.SubElement(sw_data_def_props_variants43, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy30 = ET.SubElement(sw_data_def_props_conditional43, 'SW-IMPL-POLICY')
    sw_impl_policy30.text = 'STANDARD'
    type_tref35 = ET.SubElement(variable_data_prototype16, 'TYPE-TREF')
    type_tref35.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/sint16'
    type_tref35.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    init_value3 = ET.SubElement(variable_data_prototype16, 'INIT-VALUE')
    numerical_value_specification5 = ET.SubElement(init_value3, 'NUMERICAL-VALUE-SPECIFICATION')
    short_label6 = ET.SubElement(numerical_value_specification5, 'SHORT-LABEL')
    short_label6.text = 'Value'
    value8 = ET.SubElement(numerical_value_specification5, 'VALUE')
    value8.text = '-3'


def AsynchronousServerCallReturnsEvent():
    events = ET.SubElement(swc_internal_behavior, 'EVENTS')
    asynchronous_server_call_returns_event = ET.SubElement(events, 'ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT')
    asynchronous_server_call_returns_event.attrib = {'UUID': '98e66756-7475-4549-94ba-bd68dca85e27'}
    short_name145 = ET.SubElement(asynchronous_server_call_returns_event, 'SHORT-NAME')
    short_name145.text = 'AsynchronousServerCallReturnsEvent'
    start_on_event_ref = ET.SubElement(asynchronous_server_call_returns_event, 'START-ON-EVENT-REF')
    start_on_event_ref.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable'
    start_on_event_ref.attrib = {'DEST': 'RUNNABLE-ENTITY'}
    event_source_ref = ET.SubElement(asynchronous_server_call_returns_event, 'EVENT-SOURCE-REF')
    event_source_ref.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable/AsynchronousServerCallResultPoint'
    event_source_ref.attrib = {'DEST': 'ASYNCHRONOUS-SERVER-CALL-RESULT-POINT'}

def BackgroundEvent():
    background_event = ET.SubElement(events, 'BACKGROUND-EVENT')
    background_event.attrib = {'UUID': '878975ea-f390-4f62-a34f-05ca7fd73896'}
    short_name146 = ET.SubElement(background_event, 'SHORT-NAME')
    short_name146.text = 'BackgroundEvent'
    start_on_event_ref2 = ET.SubElement(background_event, 'START-ON-EVENT-REF')
    start_on_event_ref2.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable1'
    start_on_event_ref2.attrib = {'DEST': 'RUNNABLE-ENTITY'}

def DataReceiveErrorEvent():
    data_receive_error_event = ET.SubElement(events, 'DATA-RECEIVE-ERROR-EVENT')
    data_receive_error_event.attrib = {'UUID': '733de305-2dc6-4ac2-be25-134d242372ad'}
    short_name147 = ET.SubElement(data_receive_error_event, 'SHORT-NAME')
    short_name147.text = 'DataReceiveErrorEvent'
    start_on_event_ref3 = ET.SubElement(data_receive_error_event, 'START-ON-EVENT-REF')
    start_on_event_ref3.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable2'
    start_on_event_ref3.attrib = {'DEST': 'RUNNABLE-ENTITY'}
    data_iref = ET.SubElement(data_receive_error_event, 'DATA-IREF')
    context_r_port_ref = ET.SubElement(data_iref, 'CONTEXT-R-PORT-REF')
    context_r_port_ref.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    context_r_port_ref.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_data_element_ref = ET.SubElement(data_iref, 'TARGET-DATA-ELEMENT-REF')
    target_data_element_ref.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    target_data_element_ref.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def DataReceivedEvent():
    data_received_event = ET.SubElement(events, 'DATA-RECEIVED-EVENT')
    data_received_event.attrib = {'UUID': '30fc9c83-5302-44fc-a25d-0d77e2b3d112'}
    short_name148 = ET.SubElement(data_received_event, 'SHORT-NAME')
    short_name148.text = 'DataReceivedEvent'
    start_on_event_ref4 = ET.SubElement(data_received_event, 'START-ON-EVENT-REF')
    start_on_event_ref4.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable3'
    start_on_event_ref4.attrib = {'DEST': 'RUNNABLE-ENTITY'}
    data_iref2 = ET.SubElement(data_received_event, 'DATA-IREF')
    context_r_port_ref2 = ET.SubElement(data_iref2, 'CONTEXT-R-PORT-REF')
    context_r_port_ref2.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    context_r_port_ref2.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_data_element_ref2 = ET.SubElement(data_iref2, 'TARGET-DATA-ELEMENT-REF')
    target_data_element_ref2.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    target_data_element_ref2.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def DataSendCompletedEvent():
    data_send_completed_event = ET.SubElement(events, 'DATA-SEND-COMPLETED-EVENT')
    data_send_completed_event.attrib = {'UUID': 'aefde323-2cf9-4226-aedb-0a1a33876a55'}
    short_name149 = ET.SubElement(data_send_completed_event, 'SHORT-NAME')
    short_name149.text = 'DataSendCompletedEvent'
    start_on_event_ref5 = ET.SubElement(data_send_completed_event, 'START-ON-EVENT-REF')
    start_on_event_ref5.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable4'
    start_on_event_ref5.attrib = {'DEST': 'RUNNABLE-ENTITY'}
    event_source_ref2 = ET.SubElement(data_send_completed_event, 'EVENT-SOURCE-REF')
    event_source_ref2.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable4/DSP_PPort_SR_DataElement'
    event_source_ref2.attrib = {'DEST': 'VARIABLE-ACCESS'}

def DataWriteCompletedEvent():
    data_write_completed_event = ET.SubElement(events, 'DATA-WRITE-COMPLETED-EVENT')
    data_write_completed_event.attrib = {'UUID': '0da70404-5ab6-4651-ad56-e1c3adab06e5'}
    short_name150 = ET.SubElement(data_write_completed_event, 'SHORT-NAME')
    short_name150.text = 'DataWriteCompletedEvent'
    start_on_event_ref6 = ET.SubElement(data_write_completed_event, 'START-ON-EVENT-REF')
    start_on_event_ref6.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable5'
    start_on_event_ref6.attrib = {'DEST': 'RUNNABLE-ENTITY'}
    event_source_ref3 = ET.SubElement(data_write_completed_event, 'EVENT-SOURCE-REF')
    event_source_ref3.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable5/DWA_PPort_SR_DataElement1'
    event_source_ref3.attrib = {'DEST': 'VARIABLE-ACCESS'}

def ExternalTriggerOccurredEvent():
    external_trigger_occurred_event = ET.SubElement(events, 'EXTERNAL-TRIGGER-OCCURRED-EVENT')
    external_trigger_occurred_event.attrib = {'UUID': '7f122189-5a69-4e28-af84-b5a1e73c9206'}
    short_name151 = ET.SubElement(external_trigger_occurred_event, 'SHORT-NAME')
    short_name151.text = 'ExternalTriggerOccurredEvent'
    start_on_event_ref7 = ET.SubElement(external_trigger_occurred_event, 'START-ON-EVENT-REF')
    start_on_event_ref7.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable6'
    start_on_event_ref7.attrib = {'DEST': 'RUNNABLE-ENTITY'}
    trigger_iref = ET.SubElement(external_trigger_occurred_event, 'TRIGGER-IREF')
    context_r_port_ref3 = ET.SubElement(trigger_iref, 'CONTEXT-R-PORT-REF')
    context_r_port_ref3.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_trigger'
    context_r_port_ref3.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_trigger_ref = ET.SubElement(trigger_iref, 'TARGET-TRIGGER-REF')
    target_trigger_ref.text = '/SharedElements/PortInterfaces/Trigger/TriggerInterface/Trigger'
    target_trigger_ref.attrib = {'DEST': 'TRIGGER'}

def InitEvent():
    init_event = ET.SubElement(events, 'INIT-EVENT')
    init_event.attrib = {'UUID': '6febdb10-eefc-44b9-adad-fdef91bbef72'}
    short_name498 = ET.SubElement(init_event, 'SHORT-NAME')
    short_name498.text = 'InitEvent'
    start_on_event_ref8 = ET.SubElement(init_event, 'START-ON-EVENT-REF')
    start_on_event_ref8.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable7'
    start_on_event_ref8.attrib = {'DEST': 'RUNNABLE-ENTITY'}

def ModeSwitchedAckEvent():
    mode_switched_ack_event = ET.SubElement(events, 'MODE-SWITCHED-ACK-EVENT')
    mode_switched_ack_event.attrib = {'UUID': '2f5c24be-60cf-4249-bfde-ceabef6d00d4'}
    short_name152 = ET.SubElement(mode_switched_ack_event, 'SHORT-NAME')
    short_name152.text = 'ModeSwitchedAckEvent'
    start_on_event_ref8 = ET.SubElement(mode_switched_ack_event, 'START-ON-EVENT-REF')
    start_on_event_ref8.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable9'
    start_on_event_ref8.attrib = {'DEST': 'RUNNABLE-ENTITY'}
    event_source_ref4 = ET.SubElement(mode_switched_ack_event, 'EVENT-SOURCE-REF')
    event_source_ref4.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable9/MSP_PPort_msi_ModeGroup'
    event_source_ref4.attrib = {'DEST': 'MODE-SWITCH-POINT'}

def OperationInvokedEvent():
    operation_invoked_event = ET.SubElement(events, 'OPERATION-INVOKED-EVENT')
    operation_invoked_event.attrib = {'UUID': '02646a86-1109-43a4-8e09-cb8878e932a5'}
    short_name153 = ET.SubElement(operation_invoked_event, 'SHORT-NAME')
    short_name153.text = 'OperationInvokedEvent'
    start_on_event_ref9 = ET.SubElement(operation_invoked_event, 'START-ON-EVENT-REF')
    start_on_event_ref9.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable10'
    start_on_event_ref9.attrib = {'DEST': 'RUNNABLE-ENTITY'}
    operation_iref = ET.SubElement(operation_invoked_event, 'OPERATION-IREF')
    context_p_port_ref = ET.SubElement(operation_iref, 'CONTEXT-P-PORT-REF')
    context_p_port_ref.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_CS'
    context_p_port_ref.attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    target_provided_operation_ref = ET.SubElement(operation_iref, 'TARGET-PROVIDED-OPERATION-REF')
    target_provided_operation_ref.text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface/Operation1'
    target_provided_operation_ref.attrib = {'DEST': 'CLIENT-SERVER-OPERATION'}

def SwcModeManagerErrorEvent():
    swc_mode_manager_error_event = ET.SubElement(events, 'SWC-MODE-MANAGER-ERROR-EVENT')
    swc_mode_manager_error_event.attrib = {'UUID': '2e3337be-0df8-4dce-a65a-ca8bb234754a'}
    short_name501 = ET.SubElement(swc_mode_manager_error_event, 'SHORT-NAME')
    short_name501.text = 'SwcModeManagerErrorEvent'
    start_on_event_ref11 = ET.SubElement(swc_mode_manager_error_event, 'START-ON-EVENT-REF')
    start_on_event_ref11.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable11'
    start_on_event_ref11.attrib = {'DEST': 'RUNNABLE-ENTITY'}
    mode_group_iref = ET.SubElement(swc_mode_manager_error_event, 'MODE-GROUP-IREF')
    context_p_port_ref2 = ET.SubElement(mode_group_iref, 'CONTEXT-P-PORT-REF')
    context_p_port_ref2.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_msi'
    context_p_port_ref2.attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    target_mode_group_ref = ET.SubElement(mode_group_iref, 'TARGET-MODE-GROUP-REF')
    target_mode_group_ref.text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
    target_mode_group_ref.attrib = {'DEST': 'MODE-DECLARATION-GROUP-PROTOTYPE'}

def SwcModeSwitchEvent():
    swc_mode_switch_event = ET.SubElement(events, 'SWC-MODE-SWITCH-EVENT')
    swc_mode_switch_event.attrib = {'UUID': '5bebf915-dc23-4d8d-ac15-4af9a83cb9f1'}
    short_name154 = ET.SubElement(swc_mode_switch_event, 'SHORT-NAME')
    short_name154.text = 'SwcModeSwitchEvent'
    start_on_event_ref10 = ET.SubElement(swc_mode_switch_event, 'START-ON-EVENT-REF')
    start_on_event_ref10.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable12'
    start_on_event_ref10.attrib = {'DEST': 'RUNNABLE-ENTITY'}
    activation = ET.SubElement(swc_mode_switch_event, 'ACTIVATION')
    activation.text = 'ON-TRANSITION'
    mode_irefs = ET.SubElement(swc_mode_switch_event, 'MODE-IREFS')
    mode_iref = ET.SubElement(mode_irefs, 'MODE-IREF')
    context_port_ref = ET.SubElement(mode_iref, 'CONTEXT-PORT-REF')
    context_port_ref.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_msi'
    context_port_ref.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    context_mode_declaration_group_prototype_ref = ET.SubElement(mode_iref, 'CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF')
    context_mode_declaration_group_prototype_ref.text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
    context_mode_declaration_group_prototype_ref.attrib = {'DEST': 'MODE-DECLARATION-GROUP-PROTOTYPE'}
    target_mode_declaration_ref = ET.SubElement(mode_iref, 'TARGET-MODE-DECLARATION-REF')
    target_mode_declaration_ref.text = '/SharedElements/PortInterfaces/ModeSwitch/ModeDeclarationGroup/ModeDeclaration2'
    target_mode_declaration_ref.attrib = {'DEST': 'MODE-DECLARATION'}
    mode_iref2 = ET.SubElement(mode_irefs, 'MODE-IREF')
    context_port_ref2 = ET.SubElement(mode_iref2, 'CONTEXT-PORT-REF')
    context_port_ref2.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_msi'
    context_port_ref2.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    context_mode_declaration_group_prototype_ref2 = ET.SubElement(mode_iref2, 'CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF')
    context_mode_declaration_group_prototype_ref2.text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
    context_mode_declaration_group_prototype_ref2.attrib = {'DEST': 'MODE-DECLARATION-GROUP-PROTOTYPE'}
    target_mode_declaration_ref2 = ET.SubElement(mode_iref2, 'TARGET-MODE-DECLARATION-REF')
    target_mode_declaration_ref2.text = '/SharedElements/PortInterfaces/ModeSwitch/ModeDeclarationGroup/ModeDeclaration'
    target_mode_declaration_ref2.attrib = {'DEST': 'MODE-DECLARATION'}

def TimingEvent():
    timing_event = ET.SubElement(events, 'TIMING-EVENT')
    timing_event.attrib = {'UUID': 'a761b6cb-cd31-4a99-b2f8-21c5a132097e'}
    short_name155 = ET.SubElement(timing_event, 'SHORT-NAME')
    short_name155.text = 'TimingEvent'
    start_on_event_ref11 = ET.SubElement(timing_event, 'START-ON-EVENT-REF')
    start_on_event_ref11.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable13'
    start_on_event_ref11.attrib = {'DEST': 'RUNNABLE-ENTITY'}
    period = ET.SubElement(timing_event, 'PERIOD')
    period.text = '0.01'

def TimingEvent1():
    timing_event2 = ET.SubElement(events, 'TIMING-EVENT')
    timing_event2.attrib = {'UUID': '0faaa505-7947-4b84-b8ea-4086fa60a54c'}
    short_name156 = ET.SubElement(timing_event2, 'SHORT-NAME')
    short_name156.text = 'TimingEvent1'
    start_on_event_ref12 = ET.SubElement(timing_event2, 'START-ON-EVENT-REF')
    start_on_event_ref12.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable15'
    start_on_event_ref12.attrib = {'DEST': 'RUNNABLE-ENTITY'}
    period2 = ET.SubElement(timing_event2, 'PERIOD')
    period2.text = '0.01'

def ExplicitInterRunnableVariable():
    explicit_inter_runnable_variables = ET.SubElement(swc_internal_behavior, 'EXPLICIT-INTER-RUNNABLE-VARIABLES')
    variable_data_prototype17 = ET.SubElement(explicit_inter_runnable_variables, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype17.attrib = {'UUID': '46bf0c15-16f3-428f-92de-ce374a9faf1c'}
    short_name157 = ET.SubElement(variable_data_prototype17, 'SHORT-NAME')
    short_name157.text = 'ExplicitInterRunnableVariable'
    sw_data_def_props44 = ET.SubElement(variable_data_prototype17, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants44 = ET.SubElement(sw_data_def_props44, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional44 = ET.SubElement(sw_data_def_props_variants44, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy31 = ET.SubElement(sw_data_def_props_conditional44, 'SW-IMPL-POLICY')
    sw_impl_policy31.text = 'STANDARD'
    type_tref36 = ET.SubElement(variable_data_prototype17, 'TYPE-TREF')
    type_tref36.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    type_tref36.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    init_value4 = ET.SubElement(variable_data_prototype17, 'INIT-VALUE')
    constant_reference2 = ET.SubElement(init_value4, 'CONSTANT-REFERENCE')
    short_label7 = ET.SubElement(constant_reference2, 'SHORT-LABEL')
    short_label7.text = 'ReferenceToConstant'
    constant_ref2 = ET.SubElement(constant_reference2, 'CONSTANT-REF')
    constant_ref2.text = '/SharedElements/ConstantSpecifications/ApplicationSwComponentType_ExplicitInterRunnableVariable'
    constant_ref2.attrib = {'DEST': 'CONSTANT-SPECIFICATION'}

# def NoSupport():
#     handle_termination_and_restart = ET.SubElement(swc_internal_behavior, 'HANDLE-TERMINATION-AND-RESTART')
#     handle_termination_and_restart.text = 'NO-SUPPORT'


def ImplicitInterRunnableVariable():
    implicit_inter_runnable_variables = ET.SubElement(swc_internal_behavior, 'IMPLICIT-INTER-RUNNABLE-VARIABLES')
    variable_data_prototype18 = ET.SubElement(implicit_inter_runnable_variables, 'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype18.attrib = {'UUID': '100df329-69ca-4527-945c-b23a59017964'}
    short_name158 = ET.SubElement(variable_data_prototype18, 'SHORT-NAME')
    short_name158.text = 'ImplicitInterRunnableVariable'
    sw_data_def_props45 = ET.SubElement(variable_data_prototype18, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants45 = ET.SubElement(sw_data_def_props45, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional45 = ET.SubElement(sw_data_def_props_variants45, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy32 = ET.SubElement(sw_data_def_props_conditional45, 'SW-IMPL-POLICY')
    sw_impl_policy32.text = 'STANDARD'
    type_tref37 = ET.SubElement(variable_data_prototype18, 'TYPE-TREF')
    type_tref37.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/sint16'
    type_tref37.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    init_value5 = ET.SubElement(variable_data_prototype18, 'INIT-VALUE')
    numerical_value_specification6 = ET.SubElement(init_value5, 'NUMERICAL-VALUE-SPECIFICATION')
    short_label8 = ET.SubElement(numerical_value_specification6, 'SHORT-LABEL')
    short_label8.text = 'Value'
    value9 = ET.SubElement(numerical_value_specification6, 'VALUE')
    value9.text = '0'

def PerInstanceParameter():
    per_instance_parameters = ET.SubElement(swc_internal_behavior, 'PER-INSTANCE-PARAMETERS')
    parameter_data_prototype4 = ET.SubElement(per_instance_parameters, 'PARAMETER-DATA-PROTOTYPE')
    parameter_data_prototype4.attrib = {'UUID': 'a2509010-a816-4ea4-b0ed-c5ba10c3ca78'}
    short_name159 = ET.SubElement(parameter_data_prototype4, 'SHORT-NAME')
    short_name159.text = 'PerInstanceParameter'
    sw_data_def_props46 = ET.SubElement(parameter_data_prototype4, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants46 = ET.SubElement(sw_data_def_props46, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional46 = ET.SubElement(sw_data_def_props_variants46, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access14 = ET.SubElement(sw_data_def_props_conditional46, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access14.text = 'READ-WRITE'
    sw_impl_policy33 = ET.SubElement(sw_data_def_props_conditional46, 'SW-IMPL-POLICY')
    sw_impl_policy33.text = 'STANDARD'
    type_tref38 = ET.SubElement(parameter_data_prototype4, 'TYPE-TREF')
    type_tref38.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    type_tref38.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    init_value6 = ET.SubElement(parameter_data_prototype4, 'INIT-VALUE')
    numerical_value_specification7 = ET.SubElement(init_value6, 'NUMERICAL-VALUE-SPECIFICATION')
    short_label9 = ET.SubElement(numerical_value_specification7, 'SHORT-LABEL')
    short_label9.text = 'Value'
    value10 = ET.SubElement(numerical_value_specification7, 'VALUE')
    value10.text = '5'
  
def Runnable():
    runnables = ET.SubElement(swc_internal_behavior, 'RUNNABLES')
    runnable_entity = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity.attrib = {'UUID': 'bfb2d01b-9082-4a58-a929-6d7a860a2d9a'}
    short_name160 = ET.SubElement(runnable_entity, 'SHORT-NAME')
    short_name160.text = 'Runnable'
    minimum_start_interval = ET.SubElement(runnable_entity, 'MINIMUM-START-INTERVAL')
    minimum_start_interval.text = '0'
    sw_addr_method_ref = ET.SubElement(runnable_entity, 'SW-ADDR-METHOD-REF')
    sw_addr_method_ref.text = '/SharedElements/SwAddrMethods/Copy2_SwAddrMethod'
    sw_addr_method_ref.attrib = {'DEST': 'SW-ADDR-METHOD'}

def AsynchronousServerCallResultPoint():
    asynchronous_server_call_result_points = ET.SubElement(runnable_entity, 'ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS')
    asynchronous_server_call_result_point = ET.SubElement(asynchronous_server_call_result_points, 'ASYNCHRONOUS-SERVER-CALL-RESULT-POINT')
    asynchronous_server_call_result_point.attrib = {'UUID': 'f857d505-3c25-43b2-b929-36e0e40f1177'}
    short_name161 = ET.SubElement(asynchronous_server_call_result_point, 'SHORT-NAME')
    short_name161.text = 'AsynchronousServerCallResultPoint'
    asynchronous_server_call_point_ref = ET.SubElement(asynchronous_server_call_result_point, 'ASYNCHRONOUS-SERVER-CALL-POINT-REF')
    asynchronous_server_call_point_ref.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable/ASCP_RPort_CS_Operation'
    asynchronous_server_call_point_ref.attrib = {'DEST': 'ASYNCHRONOUS-SERVER-CALL-POINT'}


def ASCP_RPort_CS_Operation():
    asynchronous_server_call_point = ET.SubElement(server_call_points, 'ASYNCHRONOUS-SERVER-CALL-POINT')
    asynchronous_server_call_point.attrib = {'UUID': 'e7aacef3-56e7-4964-b0b6-5569dd4abc09'}
    short_name162 = ET.SubElement(asynchronous_server_call_point, 'SHORT-NAME')
    short_name162.text = 'ASCP_RPort_CS_Operation'
    operation_iref2 = ET.SubElement(asynchronous_server_call_point, 'OPERATION-IREF')
    context_r_port_ref4 = ET.SubElement(operation_iref2, 'CONTEXT-R-PORT-REF')
    context_r_port_ref4.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_CS'
    context_r_port_ref4.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_required_operation_ref = ET.SubElement(operation_iref2, 'TARGET-REQUIRED-OPERATION-REF')
    target_required_operation_ref.text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface/Operation'
    target_required_operation_ref.attrib = {'DEST': 'CLIENT-SERVER-OPERATION'}
    timeout = ET.SubElement(asynchronous_server_call_point, 'TIMEOUT')
    timeout.text = '0'
    symbol9 = ET.SubElement(runnable_entity, 'SYMBOL')
    symbol9.text = 'ApplicationSwComponentType_Runnable'  
  
  
def ApplicationSwComponentType_Runnable1():
    runnable_entity2 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity2.attrib = {'UUID': '4a40f3ec-f4dd-4ab0-8562-6a5174f2901e'}
    short_name163 = ET.SubElement(runnable_entity2, 'SHORT-NAME')
    short_name163.text = 'Runnable1'
    minimum_start_interval2 = ET.SubElement(runnable_entity2, 'MINIMUM-START-INTERVAL')
    minimum_start_interval2.text = '0'
    can_be_invoked_concurrently2 = ET.SubElement(runnable_entity2, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently2.text = 'false'
    symbol10 = ET.SubElement(runnable_entity2, 'SYMBOL')
    symbol10.text = 'ApplicationSwComponentType_Runnable1'

def ApplicationSwComponentType_Runnable2():
    runnable_entity3 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity3.attrib = {'UUID': '83eca00a-85d5-4f04-9573-3d997cd29b67'}
    short_name164 = ET.SubElement(runnable_entity3, 'SHORT-NAME')
    short_name164.text = 'Runnable2'
    minimum_start_interval3 = ET.SubElement(runnable_entity3, 'MINIMUM-START-INTERVAL')
    minimum_start_interval3.text = '0'
    can_be_invoked_concurrently3 = ET.SubElement(runnable_entity3, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently3.text = 'false'
    symbol11 = ET.SubElement(runnable_entity3, 'SYMBOL')
    symbol11.text = 'ApplicationSwComponentType_Runnable2'

def ApplicationSwComponentType_Runnable3():
    runnable_entity4 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity4.attrib = {'UUID': '20bfd5e2-a118-4324-97fd-dcd5bf5f0a46'}
    short_name165 = ET.SubElement(runnable_entity4, 'SHORT-NAME')
    short_name165.text = 'Runnable3'
    minimum_start_interval4 = ET.SubElement(runnable_entity4, 'MINIMUM-START-INTERVAL')
    minimum_start_interval4.text = '0'
    can_be_invoked_concurrently4 = ET.SubElement(runnable_entity4, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently4.text = 'false'
    symbol12 = ET.SubElement(runnable_entity4, 'SYMBOL')
    symbol12.text = 'ApplicationSwComponentType_Runnable3'

def ApplicationSwComponentType_Runnable4():
    runnable_entity5 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity5.attrib = {'UUID': 'ae315d13-a18a-4515-b02d-f1b207f85e47'}
    short_name166 = ET.SubElement(runnable_entity5, 'SHORT-NAME')
    short_name166.text = 'Runnable4'
    minimum_start_interval5 = ET.SubElement(runnable_entity5, 'MINIMUM-START-INTERVAL')
    minimum_start_interval5.text = '0'
    can_be_invoked_concurrently5 = ET.SubElement(runnable_entity5, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently5.text = 'false'

def DSP_PPort_SR_DataElement():
    data_send_points = ET.SubElement(runnable_entity5, 'DATA-SEND-POINTS')
    variable_access = ET.SubElement(data_send_points, 'VARIABLE-ACCESS')
    variable_access.attrib = {'UUID': '2a04aecc-a1b6-494f-838e-29671adb5210'}
    short_name167 = ET.SubElement(variable_access, 'SHORT-NAME')
    short_name167.text = 'DSP_PPort_SR_DataElement'
    accessed_variable = ET.SubElement(variable_access, 'ACCESSED-VARIABLE')
    autosar_variable_iref = ET.SubElement(accessed_variable, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref = ET.SubElement(autosar_variable_iref, 'PORT-PROTOTYPE-REF')
    port_prototype_ref.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    port_prototype_ref.attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    target_data_prototype_ref = ET.SubElement(autosar_variable_iref, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    target_data_prototype_ref.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    symbol13 = ET.SubElement(runnable_entity5, 'SYMBOL')
    symbol13.text = 'ApplicationSwComponentType_Runnable4'

def ApplicationSwComponentType_Runnable5():
    runnable_entity6 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity6.attrib = {'UUID': '3ea0641c-9d79-4f93-8287-e34956b5c134'}
    short_name168 = ET.SubElement(runnable_entity6, 'SHORT-NAME')
    short_name168.text = 'Runnable5'
    minimum_start_interval6 = ET.SubElement(runnable_entity6, 'MINIMUM-START-INTERVAL')
    minimum_start_interval6.text = '0'
    can_be_invoked_concurrently6 = ET.SubElement(runnable_entity6, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently6.text = 'false'

def DWA_PPort_SR_DataElement1():
    data_write_accesss = ET.SubElement(runnable_entity6, 'DATA-WRITE-ACCESSS')
    variable_access2 = ET.SubElement(data_write_accesss, 'VARIABLE-ACCESS')
    variable_access2.attrib = {'UUID': '326a474d-8d28-41bc-bd9e-91de9802f682'}
    short_name169 = ET.SubElement(variable_access2, 'SHORT-NAME')
    short_name169.text = 'DWA_PPort_SR_DataElement1'
    accessed_variable2 = ET.SubElement(variable_access2, 'ACCESSED-VARIABLE')
    autosar_variable_iref2 = ET.SubElement(accessed_variable2, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref2 = ET.SubElement(autosar_variable_iref2, 'PORT-PROTOTYPE-REF')
    port_prototype_ref2.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    port_prototype_ref2.attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    target_data_prototype_ref2 = ET.SubElement(autosar_variable_iref2, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref2.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    target_data_prototype_ref2.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    symbol14 = ET.SubElement(runnable_entity6, 'SYMBOL')
    symbol14.text = 'ApplicationSwComponentType_Runnable5'
  
def ApplicationSwComponentType_Runnable6():
    runnable_entity7 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity7.attrib = {'UUID': 'd7adad0b-22d1-4b37-9691-0677036197aa'}
    short_name170 = ET.SubElement(runnable_entity7, 'SHORT-NAME')
    short_name170.text = 'Runnable6'
    minimum_start_interval7 = ET.SubElement(runnable_entity7, 'MINIMUM-START-INTERVAL')
    minimum_start_interval7.text = '0'
    can_be_invoked_concurrently7 = ET.SubElement(runnable_entity7, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently7.text = 'false'
    symbol15 = ET.SubElement(runnable_entity7, 'SYMBOL')
    symbol15.text = 'ApplicationSwComponentType_Runnable6'

def ApplicationSwComponentType_Runnable7():
    runnable_entity8 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity8.attrib = {'UUID': '98d30ebd-bbcb-4780-bc4a-27e6fd798a5a'}
    short_name171 = ET.SubElement(runnable_entity8, 'SHORT-NAME')
    short_name171.text = 'Runnable7'
    minimum_start_interval8 = ET.SubElement(runnable_entity8, 'MINIMUM-START-INTERVAL')
    minimum_start_interval8.text = '0'
    can_be_invoked_concurrently8 = ET.SubElement(runnable_entity8, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently8.text = 'false'
    symbol16 = ET.SubElement(runnable_entity8, 'SYMBOL')
    symbol16.text = 'ApplicationSwComponentType_Runnable7'

def ApplicationSwComponentType_Runnable9():
    runnable_entity9 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity9.attrib = {'UUID': 'a6d9d7cb-1d57-45f2-b36a-1e1ab717fb1e'}
    short_name172 = ET.SubElement(runnable_entity9, 'SHORT-NAME')
    short_name172.text = 'Runnable9'
    minimum_start_interval9 = ET.SubElement(runnable_entity9, 'MINIMUM-START-INTERVAL')
    minimum_start_interval9.text = '0'
    can_be_invoked_concurrently9 = ET.SubElement(runnable_entity9, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently9.text = 'false'

def MSP_PPort_msi_ModeGroup():
    mode_switch_points = ET.SubElement(runnable_entity9, 'MODE-SWITCH-POINTS')
    mode_switch_point = ET.SubElement(mode_switch_points, 'MODE-SWITCH-POINT')
    mode_switch_point.attrib = {'UUID': 'dd700e44-3e29-4b21-901f-c2e36c719f6a'}
    short_name173 = ET.SubElement(mode_switch_point, 'SHORT-NAME')
    short_name173.text = 'MSP_PPort_msi_ModeGroup'
    mode_group_iref = ET.SubElement(mode_switch_point, 'MODE-GROUP-IREF')
    context_p_port_ref2 = ET.SubElement(mode_group_iref, 'CONTEXT-P-PORT-REF')
    context_p_port_ref2.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_msi'
    context_p_port_ref2.attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    target_mode_group_ref = ET.SubElement(mode_group_iref, 'TARGET-MODE-GROUP-REF')
    target_mode_group_ref.text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
    target_mode_group_ref.attrib = {'DEST': 'MODE-DECLARATION-GROUP-PROTOTYPE'}
    symbol17 = ET.SubElement(runnable_entity9, 'SYMBOL')
    symbol17.text = 'ApplicationSwComponentType_Runnable9'

def ApplicationSwComponentType_Runnable10():
    runnable_entity10 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity10.attrib = {'UUID': '3d515ac9-9c51-4cb8-a6af-ea16d3afd01d'}
    short_name174 = ET.SubElement(runnable_entity10, 'SHORT-NAME')
    short_name174.text = 'Runnable10'
    minimum_start_interval10 = ET.SubElement(runnable_entity10, 'MINIMUM-START-INTERVAL')
    minimum_start_interval10.text = '0'
    can_be_invoked_concurrently10 = ET.SubElement(runnable_entity10, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently10.text = 'false'
    symbol18 = ET.SubElement(runnable_entity10, 'SYMBOL')
    symbol18.text = 'ApplicationSwComponentType_Runnable10'

def ApplicationSwComponentType_Runnable11():
    runnable_entity11 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity11.attrib = {'UUID': '9bddd887-575d-463b-b09d-d1b63ec1352b'}
    short_name175 = ET.SubElement(runnable_entity11, 'SHORT-NAME')
    short_name175.text = 'Runnable11'
    minimum_start_interval11 = ET.SubElement(runnable_entity11, 'MINIMUM-START-INTERVAL')
    minimum_start_interval11.text = '0'
    can_be_invoked_concurrently11 = ET.SubElement(runnable_entity11, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently11.text = 'false'
    symbol19 = ET.SubElement(runnable_entity11, 'SYMBOL')
    symbol19.text = 'ApplicationSwComponentType_Runnable11'

def ApplicationSwComponentType_Runnable12():
    runnable_entity12 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity12.attrib = {'UUID': 'fa96688f-7ffe-4b3b-aa43-c124847e2efd'}
    short_name176 = ET.SubElement(runnable_entity12, 'SHORT-NAME')
    short_name176.text = 'Runnable12'
    minimum_start_interval12 = ET.SubElement(runnable_entity12, 'MINIMUM-START-INTERVAL')
    minimum_start_interval12.text = '0'
    can_be_invoked_concurrently12 = ET.SubElement(runnable_entity12, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently12.text = 'false'
    symbol20 = ET.SubElement(runnable_entity12, 'SYMBOL')
    symbol20.text = 'ApplicationSwComponentType_Runnable12'

def ApplicationSwComponentType_Runnable13():
    runnable_entity13 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity13.attrib = {'UUID': 'e967670f-46d8-4d91-b4b9-62c85a17843e'}
    short_name177 = ET.SubElement(runnable_entity13, 'SHORT-NAME')
    short_name177.text = 'Runnable13'
    minimum_start_interval13 = ET.SubElement(runnable_entity13, 'MINIMUM-START-INTERVAL')
    minimum_start_interval13.text = '0'
    can_be_invoked_concurrently13 = ET.SubElement(runnable_entity13, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently13.text = 'false'

def ApplicationSwComponentType_Runnable13_DRA_RPort_SR_DataElement():
    data_read_accesss = ET.SubElement(runnable_entity13, 'DATA-READ-ACCESSS')
    variable_access3 = ET.SubElement(data_read_accesss, 'VARIABLE-ACCESS')
    variable_access3.attrib = {'UUID': '9bf42611-5276-4ce4-92b5-36c024121479'}
    short_name178 = ET.SubElement(variable_access3, 'SHORT-NAME')
    short_name178.text = 'DRA_RPort_SR_DataElement'
    accessed_variable3 = ET.SubElement(variable_access3, 'ACCESSED-VARIABLE')
    autosar_variable_iref3 = ET.SubElement(accessed_variable3, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref3 = ET.SubElement(autosar_variable_iref3, 'PORT-PROTOTYPE-REF')
    port_prototype_ref3.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    port_prototype_ref3.attrib = {'DEST': 'R-PORT-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DRA_RPort_SR_DataElement1():
    target_data_prototype_ref3 = ET.SubElement(autosar_variable_iref3, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref3.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    target_data_prototype_ref3.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    variable_access4 = ET.SubElement(data_read_accesss, 'VARIABLE-ACCESS')
    variable_access4.attrib = {'UUID': '9eef2638-b3d9-47c1-9e18-37822b089dd4'}
    short_name179 = ET.SubElement(variable_access4, 'SHORT-NAME')
    short_name179.text = 'DRA_RPort_SR_DataElement1'
    accessed_variable4 = ET.SubElement(variable_access4, 'ACCESSED-VARIABLE')
    autosar_variable_iref4 = ET.SubElement(accessed_variable4, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref4 = ET.SubElement(autosar_variable_iref4, 'PORT-PROTOTYPE-REF')
    port_prototype_ref4.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    port_prototype_ref4.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_data_prototype_ref4 = ET.SubElement(autosar_variable_iref4, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref4.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    target_data_prototype_ref4.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DRA_RPort_nvd_NvData():
    variable_access5 = ET.SubElement(data_read_accesss, 'VARIABLE-ACCESS')
    variable_access5.attrib = {'UUID': '26ad84a0-bc71-4cae-92f7-69d3d1bc91ff'}
    short_name180 = ET.SubElement(variable_access5, 'SHORT-NAME')
    short_name180.text = 'DRA_RPort_nvd_NvData'
    accessed_variable5 = ET.SubElement(variable_access5, 'ACCESSED-VARIABLE')
    autosar_variable_iref5 = ET.SubElement(accessed_variable5, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref5 = ET.SubElement(autosar_variable_iref5, 'PORT-PROTOTYPE-REF')
    port_prototype_ref5.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    port_prototype_ref5.attrib = {'DEST': 'R-PORT-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DRA_RPort_nvd_NvData1():
    target_data_prototype_ref5 = ET.SubElement(autosar_variable_iref5, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref5.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    target_data_prototype_ref5.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    variable_access6 = ET.SubElement(data_read_accesss, 'VARIABLE-ACCESS')
    variable_access6.attrib = {'UUID': '067aa426-f94d-4f7c-b471-a3631398a8a6'}
    short_name181 = ET.SubElement(variable_access6, 'SHORT-NAME')
    short_name181.text = 'DRA_RPort_nvd_NvData1'
    accessed_variable6 = ET.SubElement(variable_access6, 'ACCESSED-VARIABLE')
    autosar_variable_iref6 = ET.SubElement(accessed_variable6, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref6 = ET.SubElement(autosar_variable_iref6, 'PORT-PROTOTYPE-REF')
    port_prototype_ref6.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    port_prototype_ref6.attrib = {'DEST': 'R-PORT-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DWA_PPort_SR_DataElement():
    target_data_prototype_ref6 = ET.SubElement(autosar_variable_iref6, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref6.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    target_data_prototype_ref6.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    data_write_accesss2 = ET.SubElement(runnable_entity13, 'DATA-WRITE-ACCESSS')
    variable_access7 = ET.SubElement(data_write_accesss2, 'VARIABLE-ACCESS')
    variable_access7.attrib = {'UUID': 'a0b4f337-7b3c-4ade-bc28-db75b0882305'}
    short_name182 = ET.SubElement(variable_access7, 'SHORT-NAME')
    short_name182.text = 'DWA_PPort_SR_DataElement'
    accessed_variable7 = ET.SubElement(variable_access7, 'ACCESSED-VARIABLE')
    autosar_variable_iref7 = ET.SubElement(accessed_variable7, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref7 = ET.SubElement(autosar_variable_iref7, 'PORT-PROTOTYPE-REF')
    port_prototype_ref7.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    port_prototype_ref7.attrib = {'DEST': 'P-PORT-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DWA_PPort_SR_DataElement1():
    target_data_prototype_ref7 = ET.SubElement(autosar_variable_iref7, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref7.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    target_data_prototype_ref7.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    variable_access8 = ET.SubElement(data_write_accesss2, 'VARIABLE-ACCESS')
    variable_access8.attrib = {'UUID': '839b63ac-ec02-4b70-aca8-f974d2ab728c'}
    short_name183 = ET.SubElement(variable_access8, 'SHORT-NAME')
    short_name183.text = 'DWA_PPort_SR_DataElement1'
    accessed_variable8 = ET.SubElement(variable_access8, 'ACCESSED-VARIABLE')
    autosar_variable_iref8 = ET.SubElement(accessed_variable8, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref8 = ET.SubElement(autosar_variable_iref8, 'PORT-PROTOTYPE-REF')
    port_prototype_ref8.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    port_prototype_ref8.attrib = {'DEST': 'P-PORT-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DWA_PPort_nvd_NvData():
    target_data_prototype_ref8 = ET.SubElement(autosar_variable_iref8, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref8.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    target_data_prototype_ref8.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    variable_access9 = ET.SubElement(data_write_accesss2, 'VARIABLE-ACCESS')
    variable_access9.attrib = {'UUID': 'b68d4be0-8b3f-4259-9c8a-2901c17454d7'}
    short_name184 = ET.SubElement(variable_access9, 'SHORT-NAME')
    short_name184.text = 'DWA_PPort_nvd_NvData'
    accessed_variable9 = ET.SubElement(variable_access9, 'ACCESSED-VARIABLE')
    autosar_variable_iref9 = ET.SubElement(accessed_variable9, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref9 = ET.SubElement(autosar_variable_iref9, 'PORT-PROTOTYPE-REF')
    port_prototype_ref9.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
    port_prototype_ref9.attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    target_data_prototype_ref9 = ET.SubElement(autosar_variable_iref9, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref9.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    target_data_prototype_ref9.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable13_DWA_PPort_nvd_NvData1():
    variable_access10 = ET.SubElement(data_write_accesss2, 'VARIABLE-ACCESS')
    variable_access10.attrib = {'UUID': '3e84de24-a491-4152-b344-8c5e44e9197e'}
    short_name185 = ET.SubElement(variable_access10, 'SHORT-NAME')
    short_name185.text = 'DWA_PPort_nvd_NvData1'
    accessed_variable10 = ET.SubElement(variable_access10, 'ACCESSED-VARIABLE')
    autosar_variable_iref10 = ET.SubElement(accessed_variable10, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref10 = ET.SubElement(autosar_variable_iref10, 'PORT-PROTOTYPE-REF')
    port_prototype_ref10.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
    port_prototype_ref10.attrib = {'DEST': 'P-PORT-PROTOTYPE'}

def IRVRA_ExplicitInterRunnableVariable():
    target_data_prototype_ref10 = ET.SubElement(autosar_variable_iref10, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref10.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    target_data_prototype_ref10.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    read_local_variables = ET.SubElement(runnable_entity13, 'READ-LOCAL-VARIABLES')
    variable_access11 = ET.SubElement(read_local_variables, 'VARIABLE-ACCESS')
    variable_access11.attrib = {'UUID': 'c8972fdb-f78a-4e12-9a30-4faf0daa6c23'}
    short_name186 = ET.SubElement(variable_access11, 'SHORT-NAME')
    short_name186.text = 'IRVRA_ExplicitInterRunnableVariable'
    accessed_variable11 = ET.SubElement(variable_access11, 'ACCESSED-VARIABLE')
    local_variable_ref = ET.SubElement(accessed_variable11, 'LOCAL-VARIABLE-REF')
    local_variable_ref.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ExplicitInterRunnableVariable'
    local_variable_ref.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def IRVRA_ImplicitInterRunnableVariable():
    variable_access12 = ET.SubElement(read_local_variables, 'VARIABLE-ACCESS')
    variable_access12.attrib = {'UUID': 'bf16d1d1-6833-4572-8830-6e31aa069454'}
    short_name187 = ET.SubElement(variable_access12, 'SHORT-NAME')
    short_name187.text = 'IRVRA_ImplicitInterRunnableVariable'
    accessed_variable12 = ET.SubElement(variable_access12, 'ACCESSED-VARIABLE')
    local_variable_ref2 = ET.SubElement(accessed_variable12, 'LOCAL-VARIABLE-REF')
    local_variable_ref2.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ImplicitInterRunnableVariable'
    local_variable_ref2.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    symbol21 = ET.SubElement(runnable_entity13, 'SYMBOL')
    symbol21.text = 'ApplicationSwComponentType_Runnable13'

def ApplicationSwComponentType_Runnable14():
    runnable_entity14 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity14.attrib = {'UUID': '1c2e8cb0-fdf5-45ee-9257-dee6f42d2ad4'}
    short_name188 = ET.SubElement(runnable_entity14, 'SHORT-NAME')
    short_name188.text = 'Runnable14'
    minimum_start_interval14 = ET.SubElement(runnable_entity14, 'MINIMUM-START-INTERVAL')
    minimum_start_interval14.text = '0'
    can_be_invoked_concurrently14 = ET.SubElement(runnable_entity14, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently14.text = 'false'
    symbol22 = ET.SubElement(runnable_entity14, 'SYMBOL')
    symbol22.text = 'ApplicationSwComponentType_Runnable14'
  
def ApplicationSwComponentType_Runnable15():
    runnable_entity15 = ET.SubElement(runnables, 'RUNNABLE-ENTITY')
    runnable_entity15.attrib = {'UUID': '6debf2b3-9c4c-455e-9cbc-0c7cfaca4d43'}
    short_name189 = ET.SubElement(runnable_entity15, 'SHORT-NAME')
    short_name189.text = 'Runnable15'
    minimum_start_interval15 = ET.SubElement(runnable_entity15, 'MINIMUM-START-INTERVAL')
    minimum_start_interval15.text = '0'
    can_be_invoked_concurrently15 = ET.SubElement(runnable_entity15, 'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently15.text = 'false'

def ApplicationSwComponentType_Runnable15_DRA_RPort_nvd_NvData():
    data_read_accesss2 = ET.SubElement(runnable_entity15, 'DATA-READ-ACCESSS')
    variable_access13 = ET.SubElement(data_read_accesss2, 'VARIABLE-ACCESS')
    variable_access13.attrib = {'UUID': '5648b05b-23f8-4729-9fdd-25a617e2d17b'}
    short_name190 = ET.SubElement(variable_access13, 'SHORT-NAME')
    short_name190.text = 'DRA_RPort_nvd_NvData'
    accessed_variable13 = ET.SubElement(variable_access13, 'ACCESSED-VARIABLE')
    autosar_variable_iref11 = ET.SubElement(accessed_variable13, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref11 = ET.SubElement(autosar_variable_iref11, 'PORT-PROTOTYPE-REF')
    port_prototype_ref11.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    port_prototype_ref11.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_data_prototype_ref11 = ET.SubElement(autosar_variable_iref11, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref11.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    target_data_prototype_ref11.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DRA_RPort_nvd_NvData1():
    variable_access14 = ET.SubElement(data_read_accesss2, 'VARIABLE-ACCESS')
    variable_access14.attrib = {'UUID': 'b355b0ac-1fa9-43f7-b5ab-240eae2c3694'}
    short_name191 = ET.SubElement(variable_access14, 'SHORT-NAME')
    short_name191.text = 'DRA_RPort_nvd_NvData1'
    accessed_variable14 = ET.SubElement(variable_access14, 'ACCESSED-VARIABLE')
    autosar_variable_iref12 = ET.SubElement(accessed_variable14, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref12 = ET.SubElement(autosar_variable_iref12, 'PORT-PROTOTYPE-REF')
    port_prototype_ref12.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    port_prototype_ref12.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_data_prototype_ref12 = ET.SubElement(autosar_variable_iref12, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref12.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    target_data_prototype_ref12.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DRP_RPort_SR_DataElement():
    data_receive_point_by_arguments = ET.SubElement(runnable_entity15, 'DATA-RECEIVE-POINT-BY-ARGUMENTS')
    variable_access15 = ET.SubElement(data_receive_point_by_arguments, 'VARIABLE-ACCESS')
    variable_access15.attrib = {'UUID': '86796258-06a6-480e-8a39-e01411743a56'}
    short_name192 = ET.SubElement(variable_access15, 'SHORT-NAME')
    short_name192.text = 'DRP_RPort_SR_DataElement'
    accessed_variable15 = ET.SubElement(variable_access15, 'ACCESSED-VARIABLE')
    autosar_variable_iref13 = ET.SubElement(accessed_variable15, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref13 = ET.SubElement(autosar_variable_iref13, 'PORT-PROTOTYPE-REF')
    port_prototype_ref13.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    port_prototype_ref13.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_data_prototype_ref13 = ET.SubElement(autosar_variable_iref13, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref13.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    target_data_prototype_ref13.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DRP_RPort_nvd_NvData():
    variable_access16 = ET.SubElement(data_receive_point_by_arguments, 'VARIABLE-ACCESS')
    variable_access16.attrib = {'UUID': '88c27605-b9a2-4db7-af10-2a0953c5110b'}
    short_name193 = ET.SubElement(variable_access16, 'SHORT-NAME')
    short_name193.text = 'DRP_RPort_nvd_NvData'
    accessed_variable16 = ET.SubElement(variable_access16, 'ACCESSED-VARIABLE')
    autosar_variable_iref14 = ET.SubElement(accessed_variable16, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref14 = ET.SubElement(autosar_variable_iref14, 'PORT-PROTOTYPE-REF')
    port_prototype_ref14.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    port_prototype_ref14.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_data_prototype_ref14 = ET.SubElement(autosar_variable_iref14, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref14.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    target_data_prototype_ref14.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DRP_RPort_nvd_NvData1():
    variable_access17 = ET.SubElement(data_receive_point_by_arguments, 'VARIABLE-ACCESS')
    variable_access17.attrib = {'UUID': 'b69ad602-c226-42a5-9bbb-acbbc5c16743'}
    short_name194 = ET.SubElement(variable_access17, 'SHORT-NAME')
    short_name194.text = 'DRP_RPort_nvd_NvData1'
    accessed_variable17 = ET.SubElement(variable_access17, 'ACCESSED-VARIABLE')
    autosar_variable_iref15 = ET.SubElement(accessed_variable17, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref15 = ET.SubElement(autosar_variable_iref15, 'PORT-PROTOTYPE-REF')
    port_prototype_ref15.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    port_prototype_ref15.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_data_prototype_ref15 = ET.SubElement(autosar_variable_iref15, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref15.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    target_data_prototype_ref15.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DRPV_RPort_SR_DataElement1():
    data_receive_point_by_values = ET.SubElement(runnable_entity15, 'DATA-RECEIVE-POINT-BY-VALUES')
    variable_access18 = ET.SubElement(data_receive_point_by_values, 'VARIABLE-ACCESS')
    variable_access18.attrib = {'UUID': '38ed8447-65f1-48a9-b075-fa613c1267d2'}
    short_name195 = ET.SubElement(variable_access18, 'SHORT-NAME')
    short_name195.text = 'DRPV_RPort_SR_DataElement1'
    accessed_variable18 = ET.SubElement(variable_access18, 'ACCESSED-VARIABLE')
    autosar_variable_iref16 = ET.SubElement(accessed_variable18, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref16 = ET.SubElement(autosar_variable_iref16, 'PORT-PROTOTYPE-REF')
    port_prototype_ref16.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    port_prototype_ref16.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_data_prototype_ref16 = ET.SubElement(autosar_variable_iref16, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref16.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    target_data_prototype_ref16.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DRPV_RPort_nvd_NvData():
    variable_access19 = ET.SubElement(data_receive_point_by_values, 'VARIABLE-ACCESS')
    variable_access19.attrib = {'UUID': 'd07d7e6b-0d9c-4475-bbb9-2ccfc3e60c33'}
    short_name196 = ET.SubElement(variable_access19, 'SHORT-NAME')
    short_name196.text = 'DRPV_RPort_nvd_NvData'
    accessed_variable19 = ET.SubElement(variable_access19, 'ACCESSED-VARIABLE')
    autosar_variable_iref17 = ET.SubElement(accessed_variable19, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref17 = ET.SubElement(autosar_variable_iref17, 'PORT-PROTOTYPE-REF')
    port_prototype_ref17.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    port_prototype_ref17.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_data_prototype_ref17 = ET.SubElement(autosar_variable_iref17, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref17.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    target_data_prototype_ref17.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DSP_PPort_SR_DataElement():
    data_send_points2 = ET.SubElement(runnable_entity15, 'DATA-SEND-POINTS')
    variable_access20 = ET.SubElement(data_send_points2, 'VARIABLE-ACCESS')
    variable_access20.attrib = {'UUID': '2fc872c8-d598-4d11-8502-1a70e9104bc9'}
    short_name197 = ET.SubElement(variable_access20, 'SHORT-NAME')
    short_name197.text = 'DSP_PPort_SR_DataElement'
    accessed_variable20 = ET.SubElement(variable_access20, 'ACCESSED-VARIABLE')
    autosar_variable_iref18 = ET.SubElement(accessed_variable20, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref18 = ET.SubElement(autosar_variable_iref18, 'PORT-PROTOTYPE-REF')
    port_prototype_ref18.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    port_prototype_ref18.attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    target_data_prototype_ref18 = ET.SubElement(autosar_variable_iref18, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref18.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    target_data_prototype_ref18.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DSP_PPort_SR_DataElement1():
    variable_access21 = ET.SubElement(data_send_points2, 'VARIABLE-ACCESS')
    variable_access21.attrib = {'UUID': 'a2f22836-4cd0-4c2e-8040-1abdf8935ac0'}
    short_name198 = ET.SubElement(variable_access21, 'SHORT-NAME')
    short_name198.text = 'DSP_PPort_SR_DataElement1'
    accessed_variable21 = ET.SubElement(variable_access21, 'ACCESSED-VARIABLE')
    autosar_variable_iref19 = ET.SubElement(accessed_variable21, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref19 = ET.SubElement(autosar_variable_iref19, 'PORT-PROTOTYPE-REF')
    port_prototype_ref19.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    port_prototype_ref19.attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    target_data_prototype_ref19 = ET.SubElement(autosar_variable_iref19, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref19.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    target_data_prototype_ref19.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DSP_PPort_nvd_NvData():
    variable_access22 = ET.SubElement(data_send_points2, 'VARIABLE-ACCESS')
    variable_access22.attrib = {'UUID': 'c0c41eb1-b5bf-4e30-9569-24d7316b64c8'}
    short_name199 = ET.SubElement(variable_access22, 'SHORT-NAME')
    short_name199.text = 'DSP_PPort_nvd_NvData'
    accessed_variable22 = ET.SubElement(variable_access22, 'ACCESSED-VARIABLE')
    autosar_variable_iref20 = ET.SubElement(accessed_variable22, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref20 = ET.SubElement(autosar_variable_iref20, 'PORT-PROTOTYPE-REF')
    port_prototype_ref20.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
    port_prototype_ref20.attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    target_data_prototype_ref20 = ET.SubElement(autosar_variable_iref20, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref20.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    target_data_prototype_ref20.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DSP_PPort_nvd_NvData1():
    variable_access23 = ET.SubElement(data_send_points2, 'VARIABLE-ACCESS')
    variable_access23.attrib = {'UUID': '96f66382-5f86-4a47-bd5b-9f95f81fc3c9'}
    short_name200 = ET.SubElement(variable_access23, 'SHORT-NAME')
    short_name200.text = 'DSP_PPort_nvd_NvData1'
    accessed_variable23 = ET.SubElement(variable_access23, 'ACCESSED-VARIABLE')
    autosar_variable_iref21 = ET.SubElement(accessed_variable23, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref21 = ET.SubElement(autosar_variable_iref21, 'PORT-PROTOTYPE-REF')
    port_prototype_ref21.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
    port_prototype_ref21.attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    target_data_prototype_ref21 = ET.SubElement(autosar_variable_iref21, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref21.text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    target_data_prototype_ref21.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_DWA_PPort_SR_DataElement1():
    data_write_accesss3 = ET.SubElement(runnable_entity15, 'DATA-WRITE-ACCESSS')
    variable_access24 = ET.SubElement(data_write_accesss3, 'VARIABLE-ACCESS')
    variable_access24.attrib = {'UUID': 'd40a6e94-d8e5-48e5-8a1a-c7debe02592f'}
    short_name201 = ET.SubElement(variable_access24, 'SHORT-NAME')
    short_name201.text = 'DWA_PPort_SR_DataElement1'
    accessed_variable24 = ET.SubElement(variable_access24, 'ACCESSED-VARIABLE')
    autosar_variable_iref22 = ET.SubElement(accessed_variable24, 'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref22 = ET.SubElement(autosar_variable_iref22, 'PORT-PROTOTYPE-REF')
    port_prototype_ref22.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    port_prototype_ref22.attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    target_data_prototype_ref22 = ET.SubElement(autosar_variable_iref22, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref22.text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    target_data_prototype_ref22.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_MSP_PPort_msi_ModeGroup():
    mode_switch_points2 = ET.SubElement(runnable_entity15, 'MODE-SWITCH-POINTS')
    mode_switch_point2 = ET.SubElement(mode_switch_points2, 'MODE-SWITCH-POINT')
    mode_switch_point2.attrib = {'UUID': '8f7d9801-a32d-4e5f-85cd-fbcf669d921a'}
    short_name202 = ET.SubElement(mode_switch_point2, 'SHORT-NAME')
    short_name202.text = 'MSP_PPort_msi_ModeGroup'
    mode_group_iref2 = ET.SubElement(mode_switch_point2, 'MODE-GROUP-IREF')
    context_p_port_ref3 = ET.SubElement(mode_group_iref2, 'CONTEXT-P-PORT-REF')
    context_p_port_ref3.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_msi'
    context_p_port_ref3.attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    target_mode_group_ref2 = ET.SubElement(mode_group_iref2, 'TARGET-MODE-GROUP-REF')
    target_mode_group_ref2.text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
    target_mode_group_ref2.attrib = {'DEST': 'MODE-DECLARATION-GROUP-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_ParameterAccess():
    parameter_accesss = ET.SubElement(runnable_entity15, 'PARAMETER-ACCESSS')
    parameter_access = ET.SubElement(parameter_accesss, 'PARAMETER-ACCESS')
    parameter_access.attrib = {'UUID': '92d672aa-34ea-4fcb-a0a2-ab2431d59c0a'}
    short_name203 = ET.SubElement(parameter_access, 'SHORT-NAME')
    short_name203.text = 'ParameterAccess'
    accessed_parameter = ET.SubElement(parameter_access, 'ACCESSED-PARAMETER')
    local_parameter_ref = ET.SubElement(accessed_parameter, 'LOCAL-PARAMETER-REF')
    local_parameter_ref.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ConstantMemory'
    local_parameter_ref.attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_PICPVA_PerInstanceParameter():
    parameter_access2 = ET.SubElement(parameter_accesss, 'PARAMETER-ACCESS')
    parameter_access2.attrib = {'UUID': '391726ca-20e2-4c02-b063-65244a9e523a'}
    short_name204 = ET.SubElement(parameter_access2, 'SHORT-NAME')
    short_name204.text = 'PICPVA_PerInstanceParameter'
    accessed_parameter2 = ET.SubElement(parameter_access2, 'ACCESSED-PARAMETER')
    local_parameter_ref2 = ET.SubElement(accessed_parameter2, 'LOCAL-PARAMETER-REF')
    local_parameter_ref2.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/PerInstanceParameter'
    local_parameter_ref2.attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_CPA_RPort_prm_Parameter():
    parameter_access3 = ET.SubElement(parameter_accesss, 'PARAMETER-ACCESS')
    parameter_access3.attrib = {'UUID': '19d7aee6-82b8-4233-a787-b84bdb562167'}
    short_name205 = ET.SubElement(parameter_access3, 'SHORT-NAME')
    short_name205.text = 'CPA_RPort_prm_Parameter'
    accessed_parameter3 = ET.SubElement(parameter_access3, 'ACCESSED-PARAMETER')
    autosar_parameter_iref = ET.SubElement(accessed_parameter3, 'AUTOSAR-PARAMETER-IREF')
    port_prototype_ref23 = ET.SubElement(autosar_parameter_iref, 'PORT-PROTOTYPE-REF')
    port_prototype_ref23.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_prm'
    port_prototype_ref23.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_data_prototype_ref23 = ET.SubElement(autosar_parameter_iref, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref23.text = '/SharedElements/PortInterfaces/Parameter/ParameterInterface/Parameter'
    target_data_prototype_ref23.attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_CPA_RPort_prm_Parameter1():
    parameter_access4 = ET.SubElement(parameter_accesss, 'PARAMETER-ACCESS')
    parameter_access4.attrib = {'UUID': 'ab7c5c59-47f3-4fee-a310-f64cb2c00c48'}
    short_name206 = ET.SubElement(parameter_access4, 'SHORT-NAME')
    short_name206.text = 'CPA_RPort_prm_Parameter1'
    accessed_parameter4 = ET.SubElement(parameter_access4, 'ACCESSED-PARAMETER')
    autosar_parameter_iref2 = ET.SubElement(accessed_parameter4, 'AUTOSAR-PARAMETER-IREF')
    port_prototype_ref24 = ET.SubElement(autosar_parameter_iref2, 'PORT-PROTOTYPE-REF')
    port_prototype_ref24.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_prm'
    port_prototype_ref24.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_data_prototype_ref24 = ET.SubElement(autosar_parameter_iref2, 'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref24.text = '/SharedElements/PortInterfaces/Parameter/ParameterInterface/Parameter1'
    target_data_prototype_ref24.attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_SCPVA_SharedParameter():
    parameter_access5 = ET.SubElement(parameter_accesss, 'PARAMETER-ACCESS')
    parameter_access5.attrib = {'UUID': 'f7d2bfa9-92c5-4627-b238-86aadd05585b'}
    short_name207 = ET.SubElement(parameter_access5, 'SHORT-NAME')
    short_name207.text = 'SCPVA_SharedParameter'
    accessed_parameter5 = ET.SubElement(parameter_access5, 'ACCESSED-PARAMETER')
    local_parameter_ref3 = ET.SubElement(accessed_parameter5, 'LOCAL-PARAMETER-REF')
    local_parameter_ref3.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/SharedParameter'
    local_parameter_ref3.attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_SSCP_RPort_CS_Operation1():
    server_call_points2 = ET.SubElement(runnable_entity15, 'SERVER-CALL-POINTS')
    synchronous_server_call_point = ET.SubElement(server_call_points2, 'SYNCHRONOUS-SERVER-CALL-POINT')
    synchronous_server_call_point.attrib = {'UUID': 'd6a93f51-be57-4a77-bd8f-e25d3e0ba149'}
    short_name208 = ET.SubElement(synchronous_server_call_point, 'SHORT-NAME')
    short_name208.text = 'SSCP_RPort_CS_Operation1'
    operation_iref3 = ET.SubElement(synchronous_server_call_point, 'OPERATION-IREF')
    context_r_port_ref5 = ET.SubElement(operation_iref3, 'CONTEXT-R-PORT-REF')
    context_r_port_ref5.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_CS'
    context_r_port_ref5.attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    target_required_operation_ref2 = ET.SubElement(operation_iref3, 'TARGET-REQUIRED-OPERATION-REF')
    target_required_operation_ref2.text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface/Operation1'
    target_required_operation_ref2.attrib = {'DEST': 'CLIENT-SERVER-OPERATION'}
    timeout2 = ET.SubElement(synchronous_server_call_point, 'TIMEOUT')
    timeout2.text = '0'
    symbol23 = ET.SubElement(runnable_entity15, 'SYMBOL')
    symbol23.text = 'ApplicationSwComponentType_Runnable15'

def ApplicationSwComponentType_Runnable15_IRVWA_ExplicitInterRunnableVariable():
    written_local_variables = ET.SubElement(runnable_entity15, 'WRITTEN-LOCAL-VARIABLES')
    variable_access25 = ET.SubElement(written_local_variables, 'VARIABLE-ACCESS')
    variable_access25.attrib = {'UUID': '7e246e9c-b78a-47be-8798-02887c881e6e'}
    short_name209 = ET.SubElement(variable_access25, 'SHORT-NAME')
    short_name209.text = 'IRVWA_ExplicitInterRunnableVariable'
    accessed_variable25 = ET.SubElement(variable_access25, 'ACCESSED-VARIABLE')
    local_variable_ref3 = ET.SubElement(accessed_variable25, 'LOCAL-VARIABLE-REF')
    local_variable_ref3.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ExplicitInterRunnableVariable'
    local_variable_ref3.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def ApplicationSwComponentType_Runnable15_IRVWA_ImplicitInterRunnableVariable():
    variable_access26 = ET.SubElement(written_local_variables, 'VARIABLE-ACCESS')
    variable_access26.attrib = {'UUID': 'd976bba9-3132-4e15-ac45-88b85facf508'}
    short_name210 = ET.SubElement(variable_access26, 'SHORT-NAME')
    short_name210.text = 'IRVWA_ImplicitInterRunnableVariable'
    accessed_variable26 = ET.SubElement(variable_access26, 'ACCESSED-VARIABLE')
    local_variable_ref4 = ET.SubElement(accessed_variable26, 'LOCAL-VARIABLE-REF')
    local_variable_ref4.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ImplicitInterRunnableVariable'
    local_variable_ref4.attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'} 
  
def ApplicationSwComponentType_SharedParameter():
    shared_parameters = ET.SubElement(swc_internal_behavior, 'SHARED-PARAMETERS')
    parameter_data_prototype5 = ET.SubElement(shared_parameters, 'PARAMETER-DATA-PROTOTYPE')
    parameter_data_prototype5.attrib = {'UUID': 'edf877b4-19ea-4e47-8180-a74099cfff0f'}
    short_name211 = ET.SubElement(parameter_data_prototype5, 'SHORT-NAME')
    short_name211.text = 'SharedParameter'
    sw_data_def_props47 = ET.SubElement(parameter_data_prototype5, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants47 = ET.SubElement(sw_data_def_props47, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional47 = ET.SubElement(sw_data_def_props_variants47, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access15 = ET.SubElement(sw_data_def_props_conditional47, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access15.text = 'READ-WRITE'
    sw_impl_policy34 = ET.SubElement(sw_data_def_props_conditional47, 'SW-IMPL-POLICY')
    sw_impl_policy34.text = 'STANDARD'
    type_tref39 = ET.SubElement(parameter_data_prototype5, 'TYPE-TREF')
    type_tref39.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float32'
    type_tref39.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    init_value7 = ET.SubElement(parameter_data_prototype5, 'INIT-VALUE')
    constant_reference3 = ET.SubElement(init_value7, 'CONSTANT-REFERENCE')
    short_label10 = ET.SubElement(constant_reference3, 'SHORT-LABEL')
    short_label10.text = 'ReferenceToConstant'
    constant_ref3 = ET.SubElement(constant_reference3, 'CONSTANT-REF')
    constant_ref3.text = '/SharedElements/ConstantSpecifications/ApplicationSwComponentType_SharedParameter'
    constant_ref3.attrib = {'DEST': 'CONSTANT-SPECIFICATION'}
    supports_multiple_instantiation = ET.SubElement(swc_internal_behavior, 'SUPPORTS-MULTIPLE-INSTANTIATION')
    supports_multiple_instantiation.text = 'false'
    ar_packages6 = ET.SubElement(ar_package22, 'AR-PACKAGES')
    ar_package23 = ET.SubElement(ar_packages6, 'AR-PACKAGE')
    ar_package23.attrib = {'UUID': '0f00b99f-27e3-434f-9d85-398fc7c29067'}
    short_name212 = ET.SubElement(ar_package23, 'SHORT-NAME')
    short_name212.text = 'ConstantSpecifications'

def ComplexDeviceDriverSwComponentType():
    # ar_package24 = ET.SubElement(ar_packages5, 'AR-PACKAGE')
    # ar_package24.attrib = {'UUID': '7f0b665f-81ab-462f-aeab-1777b0f9dfd8'}
    # short_name213 = ET.SubElement(ar_package24, 'SHORT-NAME')
    # short_name213.text = 'CddSWC'
    elements20 = ET.SubElement(ar_package24, 'ELEMENTS')
    complex_device_driver_sw_component_type = ET.SubElement(elements20, 'COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE')
    complex_device_driver_sw_component_type.attrib = {'UUID': '27755bdf-1bfe-447f-bfdf-54402e4f4db3'}
    short_name214 = ET.SubElement(complex_device_driver_sw_component_type, 'SHORT-NAME')
    short_name214.text = 'ComplexDeviceDriverSwComponentType'
    
def CompositionSwComponentType():
    # ar_package25 = ET.SubElement(ar_packages5, 'AR-PACKAGE')
    # ar_package25.attrib = {'UUID': 'a9d129de-eda4-4cda-9025-70a56f38fb59'}
    # short_name215 = ET.SubElement(ar_package25, 'SHORT-NAME')
    # short_name215.text = 'CompSWC'
    elements21 = ET.SubElement(ar_package25, 'ELEMENTS')
    composition_sw_component_type = ET.SubElement(elements21, 'COMPOSITION-SW-COMPONENT-TYPE')
    composition_sw_component_type.attrib = {'UUID': '9e886193-6d1b-454f-98b2-d0347db57ace'}
    short_name216 = ET.SubElement(composition_sw_component_type, 'SHORT-NAME')
    short_name216.text = 'CompositionSwComponentType'
 
 
def EcuAbstractionSwComponentType():
    # ar_package26 = ET.SubElement(ar_packages5, 'AR-PACKAGE')
    # ar_package26.attrib = {'UUID': '28aa9cf2-4118-4878-8504-271a3ed4600b'}
    # short_name217 = ET.SubElement(ar_package26, 'SHORT-NAME')
    # short_name217.text = 'EcuAbSWC'
    elements22 = ET.SubElement(ar_package26, 'ELEMENTS')
    ecu_abstraction_sw_component_type = ET.SubElement(elements22, 'ECU-ABSTRACTION-SW-COMPONENT-TYPE')
    ecu_abstraction_sw_component_type.attrib = {'UUID': '0dc33c67-8b23-4896-b6a3-8a537f1cd166'}
    short_name218 = ET.SubElement(ecu_abstraction_sw_component_type, 'SHORT-NAME')
    short_name218.text = 'EcuAbstractionSwComponentType'

def NvBlockSwComponentType():
    # ar_package27 = ET.SubElement(ar_packages5, 'AR-PACKAGE')
    # ar_package27.attrib = {'UUID': '8562405a-26a1-4c3d-861f-eb0745310572'}
    # short_name219 = ET.SubElement(ar_package27, 'SHORT-NAME')
    # short_name219.text = 'NvDataSWC'
    elements23 = ET.SubElement(ar_package27, 'ELEMENTS')
    nv_block_sw_component_type = ET.SubElement(elements23, 'NV-BLOCK-SW-COMPONENT-TYPE')
    nv_block_sw_component_type.attrib = {'UUID': '9a2c1578-3f64-4af0-b953-7b81f28434cf'}
    short_name220 = ET.SubElement(nv_block_sw_component_type, 'SHORT-NAME')
    short_name220.text = 'NvBlockSwComponentType'

def ParameterSwComponentType():
    # ar_package28 = ET.SubElement(ar_packages5, 'AR-PACKAGE')
    # ar_package28.attrib = {'UUID': '0a54c44d-f71e-4ec3-bbf1-410c0b885915'}
    # short_name221 = ET.SubElement(ar_package28, 'SHORT-NAME')
    # short_name221.text = 'PrmSWC'
    elements24 = ET.SubElement(ar_package28, 'ELEMENTS')
    parameter_sw_component_type = ET.SubElement(elements24, 'PARAMETER-SW-COMPONENT-TYPE')
    parameter_sw_component_type.attrib = {'UUID': 'c21a6d07-19ae-40ac-affe-f4aa3b5acb25'}
    short_name222 = ET.SubElement(parameter_sw_component_type, 'SHORT-NAME')
    short_name222.text = 'ParameterSwComponentType'

def SensorActuatorSwComponentType():
    # ar_package29 = ET.SubElement(ar_packages5, 'AR-PACKAGE')
    # ar_package29.attrib = {'UUID': 'f142ef66-4dce-4750-8568-a7e836f462da'}
    # short_name223 = ET.SubElement(ar_package29, 'SHORT-NAME')
    # short_name223.text = 'SnsrActSWC'
    elements25 = ET.SubElement(ar_package29, 'ELEMENTS')
    sensor_actuator_sw_component_type = ET.SubElement(elements25, 'SENSOR-ACTUATOR-SW-COMPONENT-TYPE')
    sensor_actuator_sw_component_type.attrib = {'UUID': 'e631e3e3-9a52-4bbe-a762-4311d8f45934'}
    short_name224 = ET.SubElement(sensor_actuator_sw_component_type, 'SHORT-NAME')
    short_name224.text = 'SensorActuatorSwComponentType'

def ServiceProxySwComponentType():
    # ar_package30 = ET.SubElement(ar_packages5, 'AR-PACKAGE')
    # ar_package30.attrib = {'UUID': '60bb3f96-0a5c-4e30-bdda-5205f3a1cdb6'}
    # short_name225 = ET.SubElement(ar_package30, 'SHORT-NAME')
    # short_name225.text = 'SrvcPrxySWC'
    elements26 = ET.SubElement(ar_package30, 'ELEMENTS')
    service_proxy_sw_component_type = ET.SubElement(elements26, 'SERVICE-PROXY-SW-COMPONENT-TYPE')
    service_proxy_sw_component_type.attrib = {'UUID': '7e09780f-aad2-4f70-8c22-e5e19f1a82e8'}
    short_name226 = ET.SubElement(service_proxy_sw_component_type, 'SHORT-NAME')
    short_name226.text = 'ServiceProxySwComponentType'

def ServiceSwComponentType():
    # ar_package31 = ET.SubElement(ar_packages5, 'AR-PACKAGE')
    # ar_package31.attrib = {'UUID': '2ed6bb1a-c9d6-46c0-ae8b-0743080405b6'}
    # short_name227 = ET.SubElement(ar_package31, 'SHORT-NAME')
    # short_name227.text = 'SrvcSWC'
    elements27 = ET.SubElement(ar_package31, 'ELEMENTS')
    service_sw_component_type = ET.SubElement(elements27, 'SERVICE-SW-COMPONENT-TYPE')
    service_sw_component_type.attrib = {'UUID': '1da8de22-a6ec-4cab-829a-56300097c5ac'}
    short_name228 = ET.SubElement(service_sw_component_type, 'SHORT-NAME')
    short_name228.text = 'ServiceSwComponentType'
    
def Systems():
    ar_package32 = ET.SubElement(ar_packages, 'AR-PACKAGE')
    short_name229 = ET.SubElement(ar_package32, 'SHORT-NAME')
    short_name229.text = 'Systems'


    indent(root)
    tree = ET.ElementTree(root)
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