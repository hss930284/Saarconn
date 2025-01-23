import xml.etree.ElementTree as ET
import xml.dom.minidom


# Create the root element

root = ET.Element("AUTOSAR", 
                     attrib={
                         "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                         "xmlns": "http://autosar.org/schema/r4.0",
                         "xsi:schemaLocation": "http://autosar.org/schema/r4.0 AUTOSAR_4-0-2.xsd"
                     })







def ApplicationArrayDataType_Fixed():



    global elements1, ar_packages3, ar_packages2
    ar_packages1=ET.SubElement(root,'AR-PACKAGES')
    ar_package1=ET.SubElement(ar_packages1,'AR-PACKAGE')
    short_name1=ET.SubElement(ar_package1,'SHORT-NAME')
    short_name1.text='SharedElements'
    ar_packages2=ET.SubElement(ar_package1,'AR-PACKAGES')
    ar_package2=ET.SubElement(ar_packages2,'AR-PACKAGE')
    short_name2=ET.SubElement(ar_package2,'SHORT-NAME')
    short_name2.text='ApplicationDataTypes'
    ar_packages3=ET.SubElement(ar_package2,'AR-PACKAGES')
    ar_package3=ET.SubElement(ar_packages3,'AR-PACKAGE')
    ar_package3.attrib={'UUID':'035a8ab9-015a-426c-8766-e4b58e5c5a98'}
    short_name3=ET.SubElement(ar_package3,'SHORT-NAME')
    short_name3.text='Array'
    
    elements1=ET.SubElement(ar_package3.Array_folder,'ELEMENTS')
    application_array_data_type1=ET.SubElement(elements1,'APPLICATION-ARRAY-DATA-TYPE')
    application_array_data_type1.attrib={'UUID':'99540e2c-05ec-4a85-94bb-9a3999ac57fe'}
    short_name4=ET.SubElement(application_array_data_type1,'SHORT-NAME')
    short_name4.text='ApplicationArrayDataType_Fixed'
    category1=ET.SubElement(application_array_data_type1,'CATEGORY')
    category1.text='ARRAY'
    element1=ET.SubElement(application_array_data_type1,'ELEMENT')
    element1.attrib={'UUID':'7391c5fe-50b6-4b88-bc63-ec1975221a4f'}
    short_name5=ET.SubElement(element1,'SHORT-NAME')
    short_name5.text='Element'
    category2=ET.SubElement(element1,'CATEGORY')
    category2.text='VALUE'
    type_tref1=ET.SubElement(element1,'TYPE-TREF')
    type_tref1.text='/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref1.attrib={'DEST':'APPLICATION-PRIMITIVE-DATA-TYPE'}
    array_size_semantics1=ET.SubElement(element1,'ARRAY-SIZE-SEMANTICS')
    array_size_semantics1.text='FIXED-SIZE'
    max_number_of_elements1=ET.SubElement(element1,'MAX-NUMBER-OF-ELEMENTS')
    max_number_of_elements1.text='15'
        
        
    
def ApplicationArrayDataType_Variable ():
    global ar_package4
    application_array_data_type2=ET.SubElement(elements1,'APPLICATION-ARRAY-DATA-TYPE')
    application_array_data_type2.attrib={'UUID':'d5f3c7e9-dd94-4d37-888e-b6e44b01cc5a'}
    short_name6=ET.SubElement(application_array_data_type2,'SHORT-NAME')
    short_name6.text='ApplicationArrayDataType_Variable'
    category3=ET.SubElement(application_array_data_type2,'CATEGORY')
    category3.text='ARRAY'
    element2=ET.SubElement(application_array_data_type2,'ELEMENT')
    element2.attrib={'UUID':'fef3f4b8-d9bd-4cb1-94b8-4403e665c4fa'}
    short_name7=ET.SubElement(element2,'SHORT-NAME')
    short_name7.text='Element'
    category4=ET.SubElement(element2,'CATEGORY')
    category4.text='VALUE'
    type_tref2=ET.SubElement(element2,'TYPE-TREF')
    type_tref2.text='/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref2.attrib={'DEST':'APPLICATION-PRIMITIVE-DATA-TYPE'}
    array_size_semantics2=ET.SubElement(element2,'ARRAY-SIZE-SEMANTICS')
    array_size_semantics2.text='VARIABLE-SIZE'
    max_number_of_elements2=ET.SubElement(element2,'MAX-NUMBER-OF-ELEMENTS')
    max_number_of_elements2.text='15'
    ar_package4 = ET.SubElement(ar_packages3, 'AR-PACKAGE')
    ar_package4.attrib = {'UUID': 'b142aaa0-2671-41cd-bbc6-78cc30cf22c4'}
    



def ApplicationPrimitiveDataType():
    global elements2
    short_name8 = ET.SubElement(ar_package4, 'SHORT-NAME')
    short_name8.text = 'Primitive'
    elements2 = ET.SubElement(ar_package4, 'ELEMENTS')
    application_primitive_data_type1 = ET.SubElement(elements2, 'APPLICATION-PRIMITIVE-DATA-TYPE')
    application_primitive_data_type1.attrib = {'UUID': '18357165-e774-4282-90db-fcb76c7c6727'}
    short_name9 = ET.SubElement(application_primitive_data_type1, 'SHORT-NAME')
    short_name9.text = 'ApplicationPrimitiveDataType'
    category5 = ET.SubElement(application_primitive_data_type1, 'CATEGORY')
    category5.text = 'VALUE'
    sw_data_def_props1 = ET.SubElement(application_primitive_data_type1, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants1 = ET.SubElement(sw_data_def_props1, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional1 = ET.SubElement(sw_data_def_props_variants1, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access1 = ET.SubElement(sw_data_def_props_conditional1, 'SW-CALIBRATION-ACCESS')
    sw_calibration_access1.text = 'NOT-ACCESSIBLE'
    compu_method_ref1 = ET.SubElement(sw_data_def_props_conditional1, 'COMPU-METHOD-REF')
    compu_method_ref1.text = '/SharedElements/CompuMethods/CompuMethod'
    compu_method_ref1.attrib = {'DEST': 'COMPU-METHOD'}
    data_constr_ref1 = ET.SubElement(sw_data_def_props_conditional1, 'DATA-CONSTR-REF')
    data_constr_ref1.text = '/SharedElements/DataConstr/DataConstr'
    data_constr_ref1.attrib = {'DEST': 'DATA-CONSTR'}
    invalid_value1 = ET.SubElement(sw_data_def_props_conditional1, 'INVALID-VALUE')
    application_value_specification1 = ET.SubElement(invalid_value1, 'APPLICATION-VALUE-SPECIFICATION')
    category6 = ET.SubElement(application_value_specification1, 'CATEGORY')
    category6.text = 'VALUE'
    sw_value_cont1 = ET.SubElement(application_value_specification1, 'SW-VALUE-CONT')
    sw_values_phys1 = ET.SubElement(sw_value_cont1, 'SW-VALUES-PHYS')
    v1 = ET.SubElement(sw_values_phys1, 'V')
    v1.text = '8'
    unit_ref1 = ET.SubElement(sw_data_def_props_conditional1, 'UNIT-REF')
    unit_ref1.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref1.attrib = {'DEST': 'UNIT'}

def Bool_ApplicationPrimitiveDataType():
    
    application_primitive_data_type2=ET.SubElement(elements2,'APPLICATION-PRIMITIVE-DATA-TYPE')
    application_primitive_data_type2.attrib={'UUID':'14c56edb-9cf8-48cc-92d7-4cc1ca683a0f'}
    short_name10=ET.SubElement(application_primitive_data_type2,'SHORT-NAME')
    short_name10.text='Bool_ApplicationPrimitiveDataType'
    category7=ET.SubElement(application_primitive_data_type2,'CATEGORY')
    category7.text='BOOLEAN'
    sw_data_def_props2=ET.SubElement(application_primitive_data_type2,'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants2=ET.SubElement(sw_data_def_props2,'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional2=ET.SubElement(sw_data_def_props_variants2,'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access2=ET.SubElement(sw_data_def_props_conditional2,'SW-CALIBRATION-ACCESS')
    sw_calibration_access2.text='NOT-ACCESSIBLE'
    compu_method_ref2=ET.SubElement(sw_data_def_props_conditional2,'COMPU-METHOD-REF')
    compu_method_ref2.text='/SharedElements/CompuMethods/CompuMethod'
    compu_method_ref2.attrib={'DEST':'COMPU-METHOD'}
    data_constr_ref2=ET.SubElement(sw_data_def_props_conditional2,'DATA-CONSTR-REF')
    data_constr_ref2.text='/SharedElements/DataConstr/DataConstr'
    data_constr_ref2.attrib={'DEST':'DATA-CONSTR'}
    unit_ref2=ET.SubElement(sw_data_def_props_conditional2,'UNIT-REF')
    unit_ref2.text='/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref2.attrib={'DEST':'UNIT'}



def Copy_ApplicationPrimitiveDataType():

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

    application_primitive_data_type4=ET.SubElement(elements2,'APPLICATION-PRIMITIVE-DATA-TYPE')
    application_primitive_data_type4.attrib={'UUID':'decc899e-e751-4907-998b-8769b6445a38'}
    short_name12=ET.SubElement(application_primitive_data_type4,'SHORT-NAME')
    short_name12.text='String_ApplicationPrimitiveDataType'
    category9=ET.SubElement(application_primitive_data_type4,'CATEGORY')
    category9.text='STRING'
    sw_data_def_props4=ET.SubElement(application_primitive_data_type4,'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants4=ET.SubElement(sw_data_def_props4,'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional4=ET.SubElement(sw_data_def_props_variants4,'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access4=ET.SubElement(sw_data_def_props_conditional4,'SW-CALIBRATION-ACCESS')
    sw_calibration_access4.text='NOT-ACCESSIBLE'
    sw_text_props1=ET.SubElement(sw_data_def_props_conditional4,'SW-TEXT-PROPS')
    array_size_semantics3=ET.SubElement(sw_text_props1,'ARRAY-SIZE-SEMANTICS')
    array_size_semantics3.text='VARIABLE-SIZE'
    sw_max_text_size1=ET.SubElement(sw_text_props1,'SW-MAX-TEXT-SIZE')
    sw_max_text_size1.text='16'
    unit_ref4=ET.SubElement(sw_data_def_props_conditional4,'UNIT-REF')
    unit_ref4.text='/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref4.attrib={'DEST':'UNIT'}




def ApplicationRecordDataType():

    ar_package5 = ET.SubElement(ar_packages3, 'AR-PACKAGE')
    ar_package5.attrib = {'UUID': '65217d8d-3662-4a20-a643-ec9ee94de7a0'}
    short_name13 = ET.SubElement(ar_package5, 'SHORT-NAME')
    short_name13.text = 'Record'
    elements3 = ET.SubElement(ar_package5, 'ELEMENTS')
    application_record_data_type1 = ET.SubElement(elements3, 'APPLICATION-RECORD-DATA-TYPE')
    application_record_data_type1.attrib = {'UUID': 'd20b1ec6-9940-43c7-beda-f773a805fab6'}
    short_name14 = ET.SubElement(application_record_data_type1, 'SHORT-NAME')
    short_name14.text = 'ApplicationRecordDataType'
    category10 = ET.SubElement(application_record_data_type1, 'CATEGORY')
    category10.text = 'STRUCTURE'
    elements4 = ET.SubElement(application_record_data_type1, 'ELEMENTS')
    application_record_element1 = ET.SubElement(elements4, 'APPLICATION-RECORD-ELEMENT')
    application_record_element1.attrib = {'UUID': 'bd5079b0-6ac0-4d72-a63a-afd373f2bcc5'}
    short_name15 = ET.SubElement(application_record_element1, 'SHORT-NAME')
    short_name15.text = 'Element'
    type_tref3 = ET.SubElement(application_record_element1, 'TYPE-TREF')
    type_tref3.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref3.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    application_record_element2 = ET.SubElement(elements4, 'APPLICATION-RECORD-ELEMENT')
    application_record_element2.attrib = {'UUID': '12021f0e-9ad1-4df2-bffa-197611387a0a'}
    short_name16 = ET.SubElement(application_record_element2, 'SHORT-NAME')
    short_name16.text = 'Element1'
    type_tref4 = ET.SubElement(application_record_element2, 'TYPE-TREF')
    type_tref4.text = '/SharedElements/ApplicationDataTypes/Array/ApplicationArrayDataType_Fixed'
    type_tref4.attrib = {'DEST': 'APPLICATION-ARRAY-DATA-TYPE'}



def BITFIELD_TEXTTABLE_CompuMethod():
    
    
    global elements5
    
    ar_package6 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    short_name17 = ET.SubElement(ar_package6, 'SHORT-NAME')
    short_name17.text = 'CompuMethods'
    elements5 = ET.SubElement(ar_package6, 'ELEMENTS')
    compu_method1 = ET.SubElement(elements5, 'COMPU-METHOD')
    compu_method1.attrib = {'UUID': 'e51fd87b-fe38-48d5-b94a-c11851da3006'}
    short_name18 = ET.SubElement(compu_method1, 'SHORT-NAME')
    short_name18.text = 'BITFIELD_TEXTTABLE_CompuMethod'
    category11 = ET.SubElement(compu_method1, 'CATEGORY')
    category11.text = 'BITFIELD_TEXTTABLE'
    unit_ref5 = ET.SubElement(compu_method1, 'UNIT-REF')
    unit_ref5.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref5.attrib = {'DEST': 'UNIT'}
    compu_internal_to_phys1 = ET.SubElement(compu_method1, 'COMPU-INTERNAL-TO-PHYS')
    compu_scales1 = ET.SubElement(compu_internal_to_phys1, 'COMPU-SCALES')
    compu_scale1 = ET.SubElement(compu_scales1, 'COMPU-SCALE')
    mask1 = ET.SubElement(compu_scale1, 'MASK')
    mask1.text = '0'
    lower_limit1 = ET.SubElement(compu_scale1, 'LOWER-LIMIT')
    lower_limit1.text = '0'
    upper_limit1 = ET.SubElement(compu_scale1, 'UPPER-LIMIT')
    upper_limit1.text = '0'
    compu_const1 = ET.SubElement(compu_scale1, 'COMPU-CONST')
    vt1 = ET.SubElement(compu_const1, 'VT')
    vt1.text = 'xyz'
    compu_scale2 = ET.SubElement(compu_scales1, 'COMPU-SCALE')
    mask2 = ET.SubElement(compu_scale2, 'MASK')
    mask2.text = '0'
    lower_limit2 = ET.SubElement(compu_scale2, 'LOWER-LIMIT')
    lower_limit2.text = '1'
    upper_limit2 = ET.SubElement(compu_scale2, 'UPPER-LIMIT')
    upper_limit2.text = '1'
    compu_const2 = ET.SubElement(compu_scale2, 'COMPU-CONST')
    vt2 = ET.SubElement(compu_const2, 'VT')
    vt2.text = 'xyz1'
    compu_scale3 = ET.SubElement(compu_scales1, 'COMPU-SCALE')
    mask3 = ET.SubElement(compu_scale3, 'MASK')
    mask3.text = '0'
    lower_limit3 = ET.SubElement(compu_scale3, 'LOWER-LIMIT')
    lower_limit3.text = '2'
    upper_limit3 = ET.SubElement(compu_scale3, 'UPPER-LIMIT')
    upper_limit3.text = '2'
    compu_const3 = ET.SubElement(compu_scale3, 'COMPU-CONST')
    vt3 = ET.SubElement(compu_const3, 'VT')
    vt3.text = 'xyz2'
    compu_scale4 = ET.SubElement(compu_scales1, 'COMPU-SCALE')
    mask4 = ET.SubElement(compu_scale4, 'MASK')
    mask4.text = '0'
    lower_limit4 = ET.SubElement(compu_scale4, 'LOWER-LIMIT')
    lower_limit4.text = '3'
    upper_limit4 = ET.SubElement(compu_scale4, 'UPPER-LIMIT')
    upper_limit4.text = '3'
    compu_const4 = ET.SubElement(compu_scale4, 'COMPU-CONST')
    vt4 = ET.SubElement(compu_const4, 'VT')
    vt4.text = 'xyz3'
    compu_scale5 = ET.SubElement(compu_scales1, 'COMPU-SCALE')
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
    global compu_method3
    compu_method2 = ET.SubElement(elements5, 'COMPU-METHOD')
    compu_method2.attrib = {'UUID': 'a65ae6b6-3eab-43ff-907b-2c8276c8528b'}
    short_name19 = ET.SubElement(compu_method2, 'SHORT-NAME')
    short_name19.text = 'CompuMethod'
    category12 = ET.SubElement(compu_method2, 'CATEGORY')
    category12.text = 'IDENTICAL'
    unit_ref6 = ET.SubElement(compu_method2, 'UNIT-REF')
    unit_ref6.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref6.attrib = {'DEST': 'UNIT'}
    compu_method3 = ET.SubElement(elements5, 'COMPU-METHOD')
    compu_method3.attrib = {'UUID': '386978fd-a90f-4003-b63e-f9e35b6d76b8'}
    short_name20 = ET.SubElement(compu_method3, 'SHORT-NAME')
    short_name20.text = 'LINEAR_CompuMethod'
    category13 = ET.SubElement(compu_method3, 'CATEGORY')
    category13.text = 'LINEAR'
    unit_ref7 = ET.SubElement(compu_method3, 'UNIT-REF')
    unit_ref7.text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref7.attrib = {'DEST': 'UNIT'}



def LINEAR_CompuMethod():

    compu_internal_to_phys2 = ET.SubElement(compu_method3, 'COMPU-INTERNAL-TO-PHYS')
    compu_scales2 = ET.SubElement(compu_internal_to_phys2, 'COMPU-SCALES')
    compu_scale6 = ET.SubElement(compu_scales2, 'COMPU-SCALE')
    compu_rational_coeffs1 = ET.SubElement(compu_scale6, 'COMPU-RATIONAL-COEFFS')
    compu_numerator1 = ET.SubElement(compu_rational_coeffs1, 'COMPU-NUMERATOR')
    v2 = ET.SubElement(compu_numerator1, 'V')
    v2.text = '0'
    v3 = ET.SubElement(compu_numerator1, 'V')
    v3.text = '1'
    compu_denominator1 = ET.SubElement(compu_rational_coeffs1, 'COMPU-DENOMINATOR')
    v4 = ET.SubElement(compu_denominator1, 'V')
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
    desc1 = ET.SubElement(compu_method5, 'DESC')
    l_21 = ET.SubElement(desc1, 'L-2')
    l_21.text = 'S'
    l_21.attrib = {'L': 'FOR-ALL'}
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
    lower_limit7 = ET.SubElement(compu_scale9, 'LOWER-LIMIT')
    lower_limit7.text = '16'
    upper_limit7 = ET.SubElement(compu_scale9, 'UPPER-LIMIT')
    upper_limit7.text = '16'
    compu_const6 = ET.SubElement(compu_scale9, 'COMPU-CONST')
    vt6 = ET.SubElement(compu_const6, 'VT')
    vt6.text = 'sdcd'
    compu_scale10 = ET.SubElement(compu_scales4, 'COMPU-SCALE')
    lower_limit8 = ET.SubElement(compu_scale10, 'LOWER-LIMIT')
    lower_limit8.text = '17'
    upper_limit8 = ET.SubElement(compu_scale10, 'UPPER-LIMIT')
    upper_limit8.text = '17'
    compu_const7 = ET.SubElement(compu_scale10, 'COMPU-CONST')
    vt7 = ET.SubElement(compu_const7, 'VT')
    vt7.text = 'sdcd1'
    compu_default_value1 = ET.SubElement(compu_internal_to_phys4, 'COMPU-DEFAULT-VALUE')
    v17 = ET.SubElement(compu_default_value1, 'V')
    v17.text = '17'
	


def Scale_linear_And_texttable_CompuMethod():

    compu_method6=ET.SubElement(elements5,'COMPU-METHOD')
    compu_method6.attrib={'UUID':'19ee54ef-4447-4987-bcbe-a9d2a743d569'}
    short_name23=ET.SubElement(compu_method6,'SHORT-NAME')
    short_name23.text='Scale_linear_And_texttable_CompuMethod'
    desc2=ET.SubElement(compu_method6,'DESC')
    l_22=ET.SubElement(desc2,'L-2')
    l_22.text='Scale_linear_And_texttable_CompuMethod'
    l_22.attrib={'L':'FOR-ALL'}
    category16=ET.SubElement(compu_method6,'CATEGORY')
    category16.text='SCALE_LINEAR_AND_TEXTTABLE'
    unit_ref10=ET.SubElement(compu_method6,'UNIT-REF')
    unit_ref10.text='/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    unit_ref10.attrib={'DEST':'UNIT'}
    compu_internal_to_phys5=ET.SubElement(compu_method6,'COMPU-INTERNAL-TO-PHYS')
    compu_scales5=ET.SubElement(compu_internal_to_phys5,'COMPU-SCALES')
    compu_scale11=ET.SubElement(compu_scales5,'COMPU-SCALE')
    lower_limit9=ET.SubElement(compu_scale11,'LOWER-LIMIT')
    lower_limit9.text='0'
    upper_limit9=ET.SubElement(compu_scale11,'UPPER-LIMIT')
    upper_limit9.text='7'
    compu_rational_coeffs4=ET.SubElement(compu_scale11,'COMPU-RATIONAL-COEFFS')
    compu_numerator4=ET.SubElement(compu_rational_coeffs4,'COMPU-NUMERATOR')
    v18=ET.SubElement(compu_numerator4,'V')
    v18.text='0'
    v19=ET.SubElement(compu_numerator4,'V')
    v19.text='1'
    compu_denominator4=ET.SubElement(compu_rational_coeffs4,'COMPU-DENOMINATOR')
    v20=ET.SubElement(compu_denominator4,'V')
    v20.text='1'
    compu_scale12=ET.SubElement(compu_scales5,'COMPU-SCALE')
    lower_limit10=ET.SubElement(compu_scale12,'LOWER-LIMIT')
    lower_limit10.text='8'
    upper_limit10=ET.SubElement(compu_scale12,'UPPER-LIMIT')
    upper_limit10.text='8'
    compu_const8=ET.SubElement(compu_scale12,'COMPU-CONST')
    vt8=ET.SubElement(compu_const8,'VT')
    vt8.text='abcd'
    compu_scale13=ET.SubElement(compu_scales5,'COMPU-SCALE')
    lower_limit11=ET.SubElement(compu_scale13,'LOWER-LIMIT')
    lower_limit11.text='9'
    upper_limit11=ET.SubElement(compu_scale13,'UPPER-LIMIT')
    upper_limit11.text='9'
    compu_const9=ET.SubElement(compu_scale13,'COMPU-CONST')
    vt9=ET.SubElement(compu_const9,'VT')
    vt9.text='abcd1'
    compu_default_value2=ET.SubElement(compu_internal_to_phys5,'COMPU-DEFAULT-VALUE')
    v21=ET.SubElement(compu_default_value2,'V')
    v21.text='8'


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
    vf1 = ET.SubElement(compu_default_value3, 'VF')
    vf1.text = '0'
	


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
    lower_limit15 = ET.SubElement(compu_scale17, 'LOWER-LIMIT')
    lower_limit15.text = '0'
    upper_limit15 = ET.SubElement(compu_scale17, 'UPPER-LIMIT')
    upper_limit15.text = '0'
    compu_const13 = ET.SubElement(compu_scale17, 'COMPU-CONST')
    vt10 = ET.SubElement(compu_const13, 'VT')
    vt10.text = 'text1'
    compu_scale18 = ET.SubElement(compu_scales7, 'COMPU-SCALE')
    lower_limit16 = ET.SubElement(compu_scale18, 'LOWER-LIMIT')
    lower_limit16.text = '1'
    upper_limit16 = ET.SubElement(compu_scale18, 'UPPER-LIMIT')
    upper_limit16.text = '1'
    compu_const14 = ET.SubElement(compu_scale18, 'COMPU-CONST')
    vt11 = ET.SubElement(compu_const14, 'VT')
    vt11.text = 'text2'
    compu_scale19 = ET.SubElement(compu_scales7, 'COMPU-SCALE')
    lower_limit17 = ET.SubElement(compu_scale19, 'LOWER-LIMIT')
    lower_limit17.text = '2'
    upper_limit17 = ET.SubElement(compu_scale19, 'UPPER-LIMIT')
    upper_limit17.text = '2'
    compu_const15 = ET.SubElement(compu_scale19, 'COMPU-CONST')
    vt12 = ET.SubElement(compu_const15, 'VT')
    vt12.text = 'text3'
    compu_scale20 = ET.SubElement(compu_scales7, 'COMPU-SCALE')
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

	
    ar_package7 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    short_name26 = ET.SubElement(ar_package7, 'SHORT-NAME')
    short_name26.text = 'ConstantSpecifications'
    global elements6
    elements6 = ET.SubElement(ar_package7, 'ELEMENTS')
    constant_specification1 = ET.SubElement(elements6, 'CONSTANT-SPECIFICATION')
    constant_specification1.attrib = {'UUID': '5679b253-a22a-4532-8116-7ce8ac35a562'}
    short_name27 = ET.SubElement(constant_specification1, 'SHORT-NAME')
    short_name27.text = 'ApplicationSwComponentType_ExplicitInterRunnableVariable'
    value_spec1 = ET.SubElement(constant_specification1, 'VALUE-SPEC')
    numerical_value_specification1 = ET.SubElement(value_spec1, 'NUMERICAL-VALUE-SPECIFICATION')
    short_label1 = ET.SubElement(numerical_value_specification1, 'SHORT-LABEL')
    short_label1.text = 'Value'
    value1 = ET.SubElement(numerical_value_specification1, 'VALUE')
    value1.text = '0'
	


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

    ar_package8 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    ar_package8.attrib = {'UUID': '6fcb326d-7f82-4cd3-9429-fa90f212d1e8'}
    short_name31 = ET.SubElement(ar_package8, 'SHORT-NAME')
    short_name31.text = 'ConstantTypeMappingSets'
    elements7 = ET.SubElement(ar_package8, 'ELEMENTS')
    constant_specification_mapping_set1 = ET.SubElement(elements7, 'CONSTANT-SPECIFICATION-MAPPING-SET')
    constant_specification_mapping_set1.attrib = {'UUID': '4f3bdbd1-af02-46e6-a3ba-411118807380'}
    short_name32 = ET.SubElement(constant_specification_mapping_set1, 'SHORT-NAME')
    short_name32.text = 'ConstantSpecificationMappingSet'


def DataConstr():

    ar_package9 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    ar_package9.attrib = {'UUID': '5b7c99d1-d4ef-481b-95e4-0d6975de4f3b'}
    short_name33 = ET.SubElement(ar_package9, 'SHORT-NAME')
    short_name33.text = 'DataConstr'
    elements8 = ET.SubElement(ar_package9, 'ELEMENTS')
    data_constr1 = ET.SubElement(elements8, 'DATA-CONSTR')
    data_constr1.attrib = {'UUID': '78b9384e-7f45-4396-b617-a03a03aaf3ce'}
    short_name34 = ET.SubElement(data_constr1, 'SHORT-NAME')
    short_name34.text = 'DataConstr'
    data_constr_rules1 = ET.SubElement(data_constr1, 'DATA-CONSTR-RULES')
    data_constr_rule1 = ET.SubElement(data_constr_rules1, 'DATA-CONSTR-RULE')
    phys_constrs1 = ET.SubElement(data_constr_rule1, 'PHYS-CONSTRS')
    lower_limit19 = ET.SubElement(phys_constrs1, 'LOWER-LIMIT')
    lower_limit19.text = '0'
    upper_limit19 = ET.SubElement(phys_constrs1, 'UPPER-LIMIT')
    upper_limit19.text = '7'
	


def DataTypemappingSets():

	
    ar_package10 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    ar_package10.attrib = {'UUID': '463cbb86-4f8e-463e-8bb3-dafc528ccbdf'}
    short_name35 = ET.SubElement(ar_package10, 'SHORT-NAME')
    short_name35.text = 'DataTypemappingSets'
    elements9 = ET.SubElement(ar_package10, 'ELEMENTS')
    data_type_mapping_set1 = ET.SubElement(elements9, 'DATA-TYPE-MAPPING-SET')
    data_type_mapping_set1.attrib = {'UUID': '84bab728-8c47-495c-a5d4-5290c3551358'}
    short_name36 = ET.SubElement(data_type_mapping_set1, 'SHORT-NAME')
    short_name36.text = 'DataTypeMappingSet'
    data_type_maps1 = ET.SubElement(data_type_mapping_set1, 'DATA-TYPE-MAPS')
    data_type_map1 = ET.SubElement(data_type_maps1, 'DATA-TYPE-MAP')
    application_data_type_ref1 = ET.SubElement(data_type_map1, 'APPLICATION-DATA-TYPE-REF')
    application_data_type_ref1.text = '/SharedElements/ApplicationDataTypes/Array/ApplicationArrayDataType_Fixed'
    application_data_type_ref1.attrib = {'DEST': 'APPLICATION-ARRAY-DATA-TYPE'}
    implementation_data_type_ref1 = ET.SubElement(data_type_map1, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref1.text = '/SharedElements/ImplementationDataTypes/ARRAY_ImplementationDataType'
    implementation_data_type_ref1.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    data_type_map2 = ET.SubElement(data_type_maps1, 'DATA-TYPE-MAP')
    application_data_type_ref2 = ET.SubElement(data_type_map2, 'APPLICATION-DATA-TYPE-REF')
    application_data_type_ref2.text = '/SharedElements/ApplicationDataTypes/Record/ApplicationRecordDataType'
    application_data_type_ref2.attrib = {'DEST': 'APPLICATION-RECORD-DATA-TYPE'}
    implementation_data_type_ref2 = ET.SubElement(data_type_map2, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref2.text = '/SharedElements/ImplementationDataTypes/STRUCTURE_ImplementationDataType1'
    implementation_data_type_ref2.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    data_type_map3 = ET.SubElement(data_type_maps1, 'DATA-TYPE-MAP')
    application_data_type_ref3 = ET.SubElement(data_type_map3, 'APPLICATION-DATA-TYPE-REF')
    application_data_type_ref3.text = '/SharedElements/ApplicationDataTypes/Array/ApplicationArrayDataType_Variable'
    application_data_type_ref3.attrib = {'DEST': 'APPLICATION-ARRAY-DATA-TYPE'}
    implementation_data_type_ref3 = ET.SubElement(data_type_map3, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref3.text = '/SharedElements/ImplementationDataTypes/Struct_Array_ImplementationDataType'
    implementation_data_type_ref3.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    data_type_map4 = ET.SubElement(data_type_maps1, 'DATA-TYPE-MAP')
    application_data_type_ref4 = ET.SubElement(data_type_map4, 'APPLICATION-DATA-TYPE-REF')
    application_data_type_ref4.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    application_data_type_ref4.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    implementation_data_type_ref4 = ET.SubElement(data_type_map4, 'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref4.text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    implementation_data_type_ref4.attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
	



def ARRAY_ImplementationDataType():

    global elements10
    ar_package11 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    short_name37 = ET.SubElement(ar_package11, 'SHORT-NAME')
    short_name37.text = 'ImplementationDataTypes'
    elements10 = ET.SubElement(ar_package11, 'ELEMENTS')
    implementation_data_type1 = ET.SubElement(elements10, 'IMPLEMENTATION-DATA-TYPE')
    implementation_data_type1.attrib = {'UUID': '21f9a013-317d-4a6a-8c1d-cdc72f7df8f5'}
    short_name38 = ET.SubElement(implementation_data_type1, 'SHORT-NAME')
    short_name38.text = 'ARRAY_ImplementationDataType'
    category19 = ET.SubElement(implementation_data_type1, 'CATEGORY')
    category19.text = 'ARRAY'
    sw_data_def_props5 = ET.SubElement(implementation_data_type1, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants5 = ET.SubElement(sw_data_def_props5, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional5 = ET.SubElement(sw_data_def_props_variants5, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sub_elements1 = ET.SubElement(implementation_data_type1, 'SUB-ELEMENTS')
    implementation_data_type_element1 = ET.SubElement(sub_elements1, 'IMPLEMENTATION-DATA-TYPE-ELEMENT')
    implementation_data_type_element1.attrib = {'UUID': '5512b8b7-a43f-436f-bb18-47a903ad1e17'}
    short_name39 = ET.SubElement(implementation_data_type_element1, 'SHORT-NAME')
    short_name39.text = 'SubElement'
    category20 = ET.SubElement(implementation_data_type_element1, 'CATEGORY')
    category20.text = 'TYPE_REFERENCE'
    array_size1 = ET.SubElement(implementation_data_type_element1, 'ARRAY-SIZE')
    array_size1.text = '15'
    array_size_semantics4 = ET.SubElement(implementation_data_type_element1, 'ARRAY-SIZE-SEMANTICS')
    array_size_semantics4.text = 'FIXED-SIZE'
    sw_data_def_props6 = ET.SubElement(implementation_data_type_element1, 'SW-DATA-DEF-PROPS')
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


def ImplementationDataTypes():

	
    implementation_data_type3 = ET.SubElement(elements10, 'IMPLEMENTATION-DATA-TYPE')
    implementation_data_type3.attrib = {'UUID': '77ef0bea-be4b-4dea-b5ea-114e5a3f3d26'}
    short_name42 = ET.SubElement(implementation_data_type3, 'SHORT-NAME')
    short_name42.text = 'ImplementationDataType'
    category23 = ET.SubElement(implementation_data_type3, 'CATEGORY')
    category23.text = 'VALUE'
    sw_data_def_props8 = ET.SubElement(implementation_data_type3, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants8 = ET.SubElement(sw_data_def_props8, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional8 = ET.SubElement(sw_data_def_props_variants8, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    base_type_ref1 = ET.SubElement(sw_data_def_props_conditional8, 'BASE-TYPE-REF')
    base_type_ref1.text = '/AUTOSAR/AUTOSAR_Platform/BaseTypes/uint8'
    base_type_ref1.attrib = {'DEST': 'SW-BASE-TYPE'}
	




def STRUCTURE_ImplementationDataType1():

    global sub_elements3
    implementation_data_type4 = ET.SubElement(elements10, 'IMPLEMENTATION-DATA-TYPE')
    implementation_data_type4.attrib = {'UUID': '53ec3bfc-5a92-4d42-b31b-8e29e99a2b46'}
    short_name43 = ET.SubElement(implementation_data_type4, 'SHORT-NAME')
    short_name43.text = 'STRUCTURE_ImplementationDataType1'
    category24 = ET.SubElement(implementation_data_type4, 'CATEGORY')
    category24.text = 'STRUCTURE'
    sub_elements3 = ET.SubElement(implementation_data_type4, 'SUB-ELEMENTS')
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


def IMPLEMENTATIONDATATYPEELEMENTSUBELEMENT():
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

	
    global sub_elements4
    implementation_data_type5 = ET.SubElement(elements10, 'IMPLEMENTATION-DATA-TYPE')
    implementation_data_type5.attrib = {'UUID': 'ccd15817-26a8-424d-8c87-3f3d70b5ee9d'}
    short_name46 = ET.SubElement(implementation_data_type5, 'SHORT-NAME')
    short_name46.text = 'Struct_Array_ImplementationDataType'
    category27 = ET.SubElement(implementation_data_type5, 'CATEGORY')
    category27.text = 'STRUCTURE'
    sub_elements4 = ET.SubElement(implementation_data_type5, 'SUB-ELEMENTS')
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




def IMPLEMENTATIONDATATYPEELEMENT():
    
    
    implementation_data_type_element6 = ET.SubElement(sub_elements4, 'IMPLEMENTATION-DATA-TYPE-ELEMENT')
    implementation_data_type_element6.attrib = {'UUID': 'dc530c9c-3b65-4707-99c3-842e2d2b7788'}
    short_name48 = ET.SubElement(implementation_data_type_element6, 'SHORT-NAME')
    short_name48.text = 'SubElement'
    category29 = ET.SubElement(implementation_data_type_element6, 'CATEGORY')
    category29.text = 'ARRAY'
    sub_elements5 = ET.SubElement(implementation_data_type_element6, 'SUB-ELEMENTS')
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
    
    
def portinterface():
    
    global client_server_operation2, elements11
    ar_package12 = ET.SubElement(ar_packages2, 'AR-PACKAGE')
    short_name51 = ET.SubElement(ar_package12, 'SHORT-NAME')
    short_name51.text = 'PortInterfaces'
    ar_packages4 = ET.SubElement(ar_package12, 'AR-PACKAGES')
    ar_package13 = ET.SubElement(ar_packages4, 'AR-PACKAGE')
    ar_package13.attrib = {'UUID': 'a0d0a13a-15e8-47a3-8169-5f11ad6c7d3f'}
    short_name52 = ET.SubElement(ar_package13, 'SHORT-NAME')
    short_name52.text = 'ClientServer'
    elements11 = ET.SubElement(ar_package13, 'ELEMENTS')
    client_server_interface1 = ET.SubElement(elements11, 'CLIENT-SERVER-INTERFACE')
    client_server_interface1.attrib = {'UUID': 'de068aa3-6af8-4bad-a17f-893dbfa6d08d'}
    short_name53 = ET.SubElement(client_server_interface1, 'SHORT-NAME')
    short_name53.text = 'ClientServerInterface'
    is_service1 = ET.SubElement(client_server_interface1, 'IS-SERVICE')
    is_service1.text = 'false'
    operations1 = ET.SubElement(client_server_interface1, 'OPERATIONS')
    client_server_operation1 = ET.SubElement(operations1, 'CLIENT-SERVER-OPERATION')
    client_server_operation1.attrib = {'UUID': 'f963f5c2-07f7-439d-be71-e8ffb77736cb'}
    short_name54 = ET.SubElement(client_server_operation1, 'SHORT-NAME')
    short_name54.text = 'Operation'
    arguments1 = ET.SubElement(client_server_operation1, 'ARGUMENTS')
    argument_data_prototype1 = ET.SubElement(arguments1, 'ARGUMENT-DATA-PROTOTYPE')
    argument_data_prototype1.attrib = {'UUID': '0757643f-ef26-4951-9974-c0ad09b5c8d0'}
    short_name55 = ET.SubElement(argument_data_prototype1, 'SHORT-NAME')
    short_name55.text = 'Argument'
    sw_data_def_props15 = ET.SubElement(argument_data_prototype1, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants15 = ET.SubElement(sw_data_def_props15, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional15 = ET.SubElement(sw_data_def_props_variants15, 'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy1 = ET.SubElement(sw_data_def_props_conditional15, 'SW-IMPL-POLICY')
    sw_impl_policy1.text = 'STANDARD'
    type_tref5 = ET.SubElement(argument_data_prototype1, 'TYPE-TREF')
    type_tref5.text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    type_tref5.attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    direction1 = ET.SubElement(argument_data_prototype1, 'DIRECTION')
    direction1.text = 'IN'
    server_argument_impl_policy1 = ET.SubElement(argument_data_prototype1, 'SERVER-ARGUMENT-IMPL-POLICY')
    server_argument_impl_policy1.text = 'USE-ARGUMENT-TYPE'
    client_server_operation2 = ET.SubElement(operations1, 'CLIENT-SERVER-OPERATION')
    client_server_operation2.attrib = {'UUID': '9d946ffc-e827-4a3b-9217-80ae67bdce09'}    
    
def CLIENTSERVEROPERATION():
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
    operations2 = ET.SubElement(client_server_interface2, 'OPERATIONS')    
    
    # Call all functions to build up the XML structure
  
      