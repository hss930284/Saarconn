import xml.etree.ElementTree as ET
import xml.dom.minidom
import rng
from data_type_utils import DataProcessor  # Import the DataProcessor class 

# Create an instance of the DataProcessor class
processor = DataProcessor()
# Create the root element




root = ET.Element("AUTOSAR", 
                     attrib={
                         "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                         "xmlns": "http://autosar.org/schema/r4.0",
                         "xsi:schemaLocation": "http://autosar.org/schema/r4.0 AUTOSAR_4-1-2.xsd"
                     })


########## application data type ########## 
def ApplicationArrayDataType_Fixed(Array_folder): #partially completed need to modify

    Array_folder_elements = ET.SubElement(Array_folder, 'ELEMENTS')
    application_array_data_type1=ET.SubElement(Array_folder_elements,'APPLICATION-ARRAY-DATA-TYPE')
    application_array_data_type1.attrib={'UUID':rng.generate_uuid()} #99540e2c-05ec-4a85-94bb-9a3999ac57fe'}
    short_name4=ET.SubElement(application_array_data_type1,'SHORT-NAME')
    short_name4.text='ApplicationArrayDataType_Fixed'
    category1=ET.SubElement(application_array_data_type1,'CATEGORY')
    category1.text='ARRAY'
    element1=ET.SubElement(application_array_data_type1,'ELEMENT')
    element1.attrib={'UUID':rng.generate_uuid()} #7391c5fe-50b6-4b88-bc63-ec1975221a4f'}
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
    return Array_folder_elements

def ApplicationArrayDataType_Variable():#remained
    
	application_array_data_type2=ET.SubElement(elements1,'APPLICATION-ARRAY-DATA-TYPE')
	application_array_data_type2.attrib={'UUID':rng.generate_uuid()} #d5f3c7e9-dd94-4d37-888e-b6e44b01cc5a'}
	short_name6=ET.SubElement(application_array_data_type2,'SHORT-NAME')
	short_name6.text='ApplicationArrayDataType_Variable'
	category3=ET.SubElement(application_array_data_type2,'CATEGORY')
	category3.text='ARRAY'
	element2=ET.SubElement(application_array_data_type2,'ELEMENT')
	element2.attrib={'UUID':rng.generate_uuid()} #fef3f4b8-d9bd-4cb1-94b8-4403e665c4fa'}
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

def ApplicationPrimitiveDataType_Val_Invalid(Primitive_folder_elements, ApplicationPrimitiveDataType_shortname, APDT_CompuMethod, APDT_DataConstr, APDT_unit, APDT_InvalidVal ):#completed
	a=processor.value_to_str(APDT_InvalidVal)
	application_primitive_data_type=ET.SubElement(Primitive_folder_elements,'APPLICATION-PRIMITIVE-DATA-TYPE')
	application_primitive_data_type.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(application_primitive_data_type,'SHORT-NAME')
	short_name.text=ApplicationPrimitiveDataType_shortname
	category=ET.SubElement(application_primitive_data_type,'CATEGORY')
	category.text='VALUE'
	sw_data_def_props=ET.SubElement(application_primitive_data_type,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text='NOT-ACCESSIBLE'
	compu_method_ref=ET.SubElement(sw_data_def_props_conditional,'COMPU-METHOD-REF')
	compu_method_ref.text=f'/SharedElements/CompuMethods/{APDT_CompuMethod}'
	compu_method_ref.attrib={'DEST':'COMPU-METHOD'}
	data_constr_ref=ET.SubElement(sw_data_def_props_conditional,'DATA-CONSTR-REF')
	data_constr_ref.text=f'/SharedElements/DataConstr/{APDT_DataConstr}'
	data_constr_ref.attrib={'DEST':'DATA-CONSTR'}
	invalid_value=ET.SubElement(sw_data_def_props_conditional,'INVALID-VALUE')
	application_value_specification=ET.SubElement(invalid_value,'APPLICATION-VALUE-SPECIFICATION')
	category=ET.SubElement(application_value_specification,'CATEGORY')
	category.text='VALUE'
	sw_value_cont=ET.SubElement(application_value_specification,'SW-VALUE-CONT')
	sw_values_phys=ET.SubElement(sw_value_cont,'SW-VALUES-PHYS')
	v=ET.SubElement(sw_values_phys,'V')
	v.text=a
	unit_ref=ET.SubElement(sw_data_def_props_conditional,'UNIT-REF')
	unit_ref.text=f'/AUTOSAR/AUTOSAR_PhysicalUnits/Units/{APDT_unit}'
	unit_ref.attrib={'DEST':'UNIT'}

def Bool_ApplicationPrimitiveDataType(Primitive_folder_elements, ApplicationPrimitiveDataType_shortname, APDT_CompuMethod, APDT_DataConstr, APDT_unit):#completed

	application_primitive_data_type=ET.SubElement(Primitive_folder_elements,'APPLICATION-PRIMITIVE-DATA-TYPE')
	application_primitive_data_type.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(application_primitive_data_type,'SHORT-NAME')
	short_name.text=ApplicationPrimitiveDataType_shortname
	category=ET.SubElement(application_primitive_data_type,'CATEGORY')
	category.text='BOOLEAN'
	sw_data_def_props=ET.SubElement(application_primitive_data_type,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text='NOT-ACCESSIBLE'
	compu_method_ref=ET.SubElement(sw_data_def_props_conditional,'COMPU-METHOD-REF')
	compu_method_ref.text=f'/SharedElements/CompuMethods/{APDT_CompuMethod}'
	compu_method_ref.attrib={'DEST':'COMPU-METHOD'}
	data_constr_ref=ET.SubElement(sw_data_def_props_conditional,'DATA-CONSTR-REF')
	data_constr_ref.text=f'/SharedElements/DataConstr/{APDT_DataConstr}'
	data_constr_ref.attrib={'DEST':'DATA-CONSTR'}
	unit_ref=ET.SubElement(sw_data_def_props_conditional,'UNIT-REF')
	unit_ref.text=f'/AUTOSAR/AUTOSAR_PhysicalUnits/Units/{APDT_unit}'
	unit_ref.attrib={'DEST':'UNIT'}

def ApplicationPrimitiveDataType_Val(Primitive_folder_elements, ApplicationPrimitiveDataType_shortname, APDT_CompuMethod, APDT_DataConstr, APDT_unit):#completed


	application_primitive_data_type=ET.SubElement(Primitive_folder_elements,'APPLICATION-PRIMITIVE-DATA-TYPE')
	application_primitive_data_type.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(application_primitive_data_type,'SHORT-NAME')
	short_name.text=ApplicationPrimitiveDataType_shortname
	category=ET.SubElement(application_primitive_data_type,'CATEGORY')
	category.text='VALUE'
	sw_data_def_props=ET.SubElement(application_primitive_data_type,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text='NOT-ACCESSIBLE'
	compu_method_ref=ET.SubElement(sw_data_def_props_conditional,'COMPU-METHOD-REF')
	compu_method_ref.text=f'/SharedElements/CompuMethods/{APDT_CompuMethod}'
	compu_method_ref.attrib={'DEST':'COMPU-METHOD'}
	data_constr_ref=ET.SubElement(sw_data_def_props_conditional,'DATA-CONSTR-REF')
	data_constr_ref.text=f'/SharedElements/DataConstr/{APDT_DataConstr}'
	data_constr_ref.attrib={'DEST':'DATA-CONSTR'}
	unit_ref=ET.SubElement(sw_data_def_props_conditional,'UNIT-REF')
	unit_ref.text=f'/AUTOSAR/AUTOSAR_PhysicalUnits/Units/{APDT_unit}'
	unit_ref.attrib={'DEST':'UNIT'}

def String_ApplicationPrimitiveDataType():#remained

	application_primitive_data_type4=ET.SubElement(elements2,'APPLICATION-PRIMITIVE-DATA-TYPE')
	application_primitive_data_type4.attrib={'UUID':rng.generate_uuid()} #decc899e-e751-4907-998b-8769b6445a38'}
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

def ApplicationRecordDataType(Record_folder_elements, ARDT_ShortName, ):#completed
	global ARDT_elements

	application_record_data_type=ET.SubElement(Record_folder_elements,'APPLICATION-RECORD-DATA-TYPE')
	application_record_data_type.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(application_record_data_type,'SHORT-NAME')
	short_name.text=ARDT_ShortName
	category=ET.SubElement(application_record_data_type,'CATEGORY')
	category.text='STRUCTURE'
	ARDT_elements=ET.SubElement(application_record_data_type,'ELEMENTS')

def ApplicationRecordDataType_elements(ARDT_element_shortname, ARDT_element_type, data_type):#completed 
	application_record_element=ET.SubElement(ARDT_elements,'APPLICATION-RECORD-ELEMENT')
	application_record_element.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(application_record_element,'SHORT-NAME')
	short_name.text=ARDT_element_shortname

	# ARDT_element_type = [APDT, ARDT, AADT, IDT]

	if ARDT_element_type == 'APDT':

		type_tref=ET.SubElement(application_record_element,'TYPE-TREF')
		type_tref.text=f'/SharedElements/ApplicationDataTypes/Primitive/{data_type}'
		type_tref.attrib={'DEST':'APPLICATION-PRIMITIVE-DATA-TYPE'}

	elif ARDT_element_type == 'AADT':

		type_tref=ET.SubElement(application_record_element,'TYPE-TREF')
		type_tref.text=f'/SharedElements/ApplicationDataTypes/Array/{data_type}'
		type_tref.attrib={'DEST':'APPLICATION-ARRAY-DATA-TYPE'}

	elif ARDT_element_type == 'ARDT':

		type_tref=ET.SubElement(application_record_element,'TYPE-TREF')
		type_tref.text=f'/SharedElements/ApplicationDataTypes/Record/{data_type}'
		type_tref.attrib={'DEST':'APPLICATION-RECORD-DATA-TYPE'}

	elif ARDT_element_type == 'IDT':
		type_tref=ET.SubElement(application_record_element,'TYPE-TREF')
		type_tref.text=f'/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/{data_type}'
		type_tref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}

	else :
		print ('Invalid ARDT_element_type')




####### Compu method #########

def CompuMethod_IDENTICAL(CompuMethods_shared_folder_elements, compu_method_shortname, unit):#completed

	compu_method=ET.SubElement(CompuMethods_shared_folder_elements,'COMPU-METHOD')
	compu_method.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(compu_method,'SHORT-NAME')
	short_name.text=compu_method_shortname
	category=ET.SubElement(compu_method,'CATEGORY')
	category.text='IDENTICAL'
	unit_ref=ET.SubElement(compu_method,'UNIT-REF')
	unit_ref.text=f'/AUTOSAR/AUTOSAR_PhysicalUnits/Units/{unit}'
	unit_ref.attrib={'DEST':'UNIT'}



def CompuMethod_bitfield_text(CompuMethods_shared_folder_elements, compu_method_shortname, unit):#completed
	global compu_scales
	
	compu_method=ET.SubElement(CompuMethods_shared_folder_elements,'COMPU-METHOD')
	compu_method.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(compu_method,'SHORT-NAME')
	short_name.text=compu_method_shortname
	category=ET.SubElement(compu_method,'CATEGORY')
	category.text='BITFIELD_TEXTTABLE'
	unit_ref=ET.SubElement(compu_method,'UNIT-REF')
	unit_ref.text=f'/AUTOSAR/AUTOSAR_PhysicalUnits/Units/{unit}'
	unit_ref.attrib={'DEST':'UNIT'}
	compu_internal_to_phys=ET.SubElement(compu_method,'COMPU-INTERNAL-TO-PHYS')
	compu_scales=ET.SubElement(compu_internal_to_phys,'COMPU-SCALES')
	
def bitfield_text_compu_scale(mask_val, ll, ul, enum):#completed
	c=processor.value_to_str(mask_val)
	d=processor.value_to_str(ll)
	e=processor.value_to_str(ul)
	f=processor.value_to_str(enum)
	compu_scale=ET.SubElement(compu_scales,'COMPU-SCALE')
	mask=ET.SubElement(compu_scale,'MASK')
	mask.text=c
	lower_limit=ET.SubElement(compu_scale,'LOWER-LIMIT')
	lower_limit.text=d
	upper_limit=ET.SubElement(compu_scale,'UPPER-LIMIT')
	upper_limit.text=e
	compu_const=ET.SubElement(compu_scale,'COMPU-CONST')
	vt=ET.SubElement(compu_const,'VT')
	vt.text=f

def CompuMethod_linear(CompuMethods_shared_folder_elements, compu_method_shortname, unit):#completed
	global compu_scales
	compu_method=ET.SubElement(CompuMethods_shared_folder_elements,'COMPU-METHOD')
	compu_method.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(compu_method,'SHORT-NAME')
	short_name.text=compu_method_shortname
	category=ET.SubElement(compu_method,'CATEGORY')
	category.text='LINEAR'
	unit_ref=ET.SubElement(compu_method,'UNIT-REF')
	unit_ref.text=f'/AUTOSAR/AUTOSAR_PhysicalUnits/Units/{unit}'
	unit_ref.attrib={'DEST':'UNIT'}
	compu_internal_to_phys=ET.SubElement(compu_method,'COMPU-INTERNAL-TO-PHYS')
	compu_scales=ET.SubElement(compu_internal_to_phys,'COMPU-SCALES')
	
def linear_compu_scale(num_a,num_b,den_a):#completed
	c=processor.value_to_str(num_a)
	d=processor.value_to_str(num_b)
	e=processor.value_to_str(den_a)

	compu_scale=ET.SubElement(compu_scales,'COMPU-SCALE')
	compu_rational_coeffs=ET.SubElement(compu_scale,'COMPU-RATIONAL-COEFFS')
	compu_numerator=ET.SubElement(compu_rational_coeffs,'COMPU-NUMERATOR')
	v2=ET.SubElement(compu_numerator,'V')
	v2.text=c
	v3=ET.SubElement(compu_numerator,'V')
	v3.text=d
	compu_denominator=ET.SubElement(compu_rational_coeffs,'COMPU-DENOMINATOR')
	v4=ET.SubElement(compu_denominator,'V')
	v4.text=e

def CompuMethod_rat_func(CompuMethods_shared_folder_elements, compu_method_shortname, unit):#completed
	global compu_scales
 
	compu_method=ET.SubElement(CompuMethods_shared_folder_elements,'COMPU-METHOD')
	compu_method.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(compu_method,'SHORT-NAME')
	short_name.text=compu_method_shortname
	category=ET.SubElement(compu_method,'CATEGORY')
	category.text='RAT_FUNC'
	unit_ref=ET.SubElement(compu_method,'UNIT-REF')
	unit_ref.text=f'/AUTOSAR/AUTOSAR_PhysicalUnits/Units/{unit}'
	unit_ref.attrib={'DEST':'UNIT'}
	compu_internal_to_phys=ET.SubElement(compu_method,'COMPU-INTERNAL-TO-PHYS')
	compu_scales=ET.SubElement(compu_internal_to_phys,'COMPU-SCALES')
	
def rat_func_compu_scale(num_a,num_b,num_c,den_a,den_b,den_c):#completed
	c=processor.value_to_str(num_a)
	d=processor.value_to_str(num_b)
	e=processor.value_to_str(num_c)
	f=processor.value_to_str(den_a)
	g=processor.value_to_str(den_b)
	h=processor.value_to_str(den_c)
	
	compu_scale=ET.SubElement(compu_scales,'COMPU-SCALE')
	compu_rational_coeffs=ET.SubElement(compu_scale,'COMPU-RATIONAL-COEFFS')
	compu_numerator=ET.SubElement(compu_rational_coeffs,'COMPU-NUMERATOR')
	v5=ET.SubElement(compu_numerator,'V')
	v5.text=c
	v6=ET.SubElement(compu_numerator,'V')
	v6.text=d
	v7=ET.SubElement(compu_numerator,'V')
	v7.text=e
	compu_denominator=ET.SubElement(compu_rational_coeffs,'COMPU-DENOMINATOR')
	v8=ET.SubElement(compu_denominator,'V')
	v8.text=f
	v9=ET.SubElement(compu_denominator,'V')
	v9.text=g
	v10=ET.SubElement(compu_denominator,'V')
	v10.text=h

def CompuMethod_Scale_rat_text(CompuMethods_shared_folder_elements, compu_method_shortname, unit):#completed
	global compu_scales, compu_internal_to_phys
	compu_method=ET.SubElement(CompuMethods_shared_folder_elements,'COMPU-METHOD')
	compu_method.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(compu_method,'SHORT-NAME')
	short_name.text=compu_method_shortname
	desc=ET.SubElement(compu_method,'DESC')
	l_2=ET.SubElement(desc,'L-2')
	l_2.text='S'
	l_2.attrib={'L':'FOR-ALL'}
	category=ET.SubElement(compu_method,'CATEGORY')
	category.text='SCALE_RATIONAL_AND_TEXTTABLE'
	unit_ref=ET.SubElement(compu_method,'UNIT-REF')
	unit_ref.text=f'/AUTOSAR/AUTOSAR_PhysicalUnits/Units/{unit}'
	unit_ref.attrib={'DEST':'UNIT'}
	compu_internal_to_phys=ET.SubElement(compu_method,'COMPU-INTERNAL-TO-PHYS')
	compu_scales=ET.SubElement(compu_internal_to_phys,'COMPU-SCALES')
	
def Scale_rat_text_compu_scale(ll,ul,num_a,num_b,num_c,den_a,den_b,den_c):#completed
	a=processor.value_to_str(ll)
	b=processor.value_to_str(ul)
	c=processor.value_to_str(num_a)
	d=processor.value_to_str(num_b)
	e=processor.value_to_str(num_c)
	f=processor.value_to_str(den_a)
	g=processor.value_to_str(den_b)
	h=processor.value_to_str(den_c)
	compu_scale=ET.SubElement(compu_scales,'COMPU-SCALE')
	lower_limit=ET.SubElement(compu_scale,'LOWER-LIMIT')
	lower_limit.text=a
	upper_limit=ET.SubElement(compu_scale,'UPPER-LIMIT')
	upper_limit.text=b
	compu_rational_coeffs=ET.SubElement(compu_scale,'COMPU-RATIONAL-COEFFS')
	compu_numerator=ET.SubElement(compu_rational_coeffs,'COMPU-NUMERATOR')
	v1=ET.SubElement(compu_numerator,'V')
	v1.text=c
	v2=ET.SubElement(compu_numerator,'V')
	v2.text=d
	v3=ET.SubElement(compu_numerator,'V')
	v3.text=e
	compu_denominator=ET.SubElement(compu_rational_coeffs,'COMPU-DENOMINATOR')
	v4=ET.SubElement(compu_denominator,'V')
	v4.text=f
	v5=ET.SubElement(compu_denominator,'V')
	v5.text=g
	v6=ET.SubElement(compu_denominator,'V')
	v6.text=h
	
	# compu_scale9=ET.SubElement(compu_scales4,'COMPU-SCALE')
	# symbol = ET.SubElement(compu_scale9, 'SYMBOL')
    # symbol.text = 'sdcd'
	# lower_limit7=ET.SubElement(compu_scale9,'LOWER-LIMIT')
	# lower_limit7.text='16'
	# upper_limit7=ET.SubElement(compu_scale9,'UPPER-LIMIT')
	# upper_limit7.text='16'
	# compu_const6=ET.SubElement(compu_scale9,'COMPU-CONST')
	# vt6=ET.SubElement(compu_const6,'VT')
	# vt6.text='sdcd'
	
	# compu_scale10=ET.SubElement(compu_scales4,'COMPU-SCALE')
	# symbol2 = ET.SubElement(compu_scale10, 'SYMBOL')
    # symbol2.text = 'sdcd1'
	# lower_limit8=ET.SubElement(compu_scale10,'LOWER-LIMIT')
	# lower_limit8.text='17'
	# upper_limit8=ET.SubElement(compu_scale10,'UPPER-LIMIT')
	# upper_limit8.text='17'
	# compu_const7=ET.SubElement(compu_scale10,'COMPU-CONST')
	# vt7=ET.SubElement(compu_const7,'VT')
	# vt7.text='sdcd1'
	
def Scale_rat_text_compu_default_value(cm_DefaultValue):#completed
	a=processor.value_to_str(cm_DefaultValue)
	compu_default_value=ET.SubElement(compu_internal_to_phys,'COMPU-DEFAULT-VALUE')
	v7=ET.SubElement(compu_default_value,'V')
	v7.text=a

def CompuMethod_Scale_linear_text(CompuMethods_shared_folder_elements, compu_method_shortname, unit):#completed
	global compu_scales, compu_internal_to_phys

	compu_method=ET.SubElement(CompuMethods_shared_folder_elements,'COMPU-METHOD')
	compu_method.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(compu_method,'SHORT-NAME')
	short_name.text=compu_method_shortname
	desc=ET.SubElement(compu_method,'DESC')
	l_2=ET.SubElement(desc,'L-2')
	l_2.text='Scale_linear_And_texttable_CompuMethod'
	l_2.attrib={'L':'FOR-ALL'}
	category=ET.SubElement(compu_method,'CATEGORY')
	category.text='SCALE_LINEAR_AND_TEXTTABLE'
	unit_ref=ET.SubElement(compu_method,'UNIT-REF')
	unit_ref.text=f'/AUTOSAR/AUTOSAR_PhysicalUnits/Units/{unit}'
	unit_ref.attrib={'DEST':'UNIT'}
	compu_internal_to_phys=ET.SubElement(compu_method,'COMPU-INTERNAL-TO-PHYS')
	compu_scales=ET.SubElement(compu_internal_to_phys,'COMPU-SCALES')

def Scale_linear_text_compu_scale(ll,ul,num_a,num_b,den_a):#completed
	a=processor.value_to_str(ll)
	b=processor.value_to_str(ul)
	c=processor.value_to_str(num_a)
	d=processor.value_to_str(num_b)
	e=processor.value_to_str(den_a)
	
	compu_scale=ET.SubElement(compu_scales,'COMPU-SCALE')

	''' #fetch
	symbol = ET.SubElement(compu_scale12, 'SYMBOL')
    symbol.text = 'abcd'
	'''

	lower_limit=ET.SubElement(compu_scale,'LOWER-LIMIT')
	lower_limit.text=a
	upper_limit=ET.SubElement(compu_scale,'UPPER-LIMIT')
	upper_limit.text=b
	compu_rational_coeffs=ET.SubElement(compu_scale,'COMPU-RATIONAL-COEFFS')
	compu_numerator=ET.SubElement(compu_rational_coeffs,'COMPU-NUMERATOR')
	v=ET.SubElement(compu_numerator,'V')
	v.text=c
	v1=ET.SubElement(compu_numerator,'V')
	v1.text=d
	compu_denominator=ET.SubElement(compu_rational_coeffs,'COMPU-DENOMINATOR')
	v2=ET.SubElement(compu_denominator,'V')
	v2.text=e

def Scale_linear_text_compu_DefaultValue(cm_DefaultValue):#completed
	a=processor.value_to_str(cm_DefaultValue)
	compu_default_value=ET.SubElement(compu_internal_to_phys,'COMPU-DEFAULT-VALUE')
	v=ET.SubElement(compu_default_value,'V')
	v.text=a

def CompuMethod_tab_nointp(CompuMethods_shared_folder_elements, compu_method_shortname, unit):#completed
	global compu_scales, compu_internal_to_phys
	compu_method=ET.SubElement(CompuMethods_shared_folder_elements,'COMPU-METHOD')
	compu_method.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(compu_method,'SHORT-NAME')
	short_name.text=compu_method_shortname
	desc3=ET.SubElement(compu_method,'DESC')
	category=ET.SubElement(compu_method,'CATEGORY')
	category.text='TAB_NOINTP'
	unit_ref=ET.SubElement(compu_method,'UNIT-REF')
	unit_ref.text=f'/AUTOSAR/AUTOSAR_PhysicalUnits/Units/{unit}'
	unit_ref.attrib={'DEST':'UNIT'}
	compu_internal_to_phys=ET.SubElement(compu_method,'COMPU-INTERNAL-TO-PHYS')
	compu_scales=ET.SubElement(compu_internal_to_phys,'COMPU-SCALES')

def tab_nointp_compu_Scale(value, enum):#completed
	a=processor.value_to_str(value)
	b=processor.value_to_str(enum)
	compu_scale=ET.SubElement(compu_scales,'COMPU-SCALE')
	# desc=ET.SubElement(compu_scale,'DESC')
	# l_2=ET.SubElement(desc,'L-2')
	# l_2.attrib={'L':'AA'}
	lower_limit=ET.SubElement(compu_scale,'LOWER-LIMIT')
	lower_limit.text=a
	upper_limit=ET.SubElement(compu_scale,'UPPER-LIMIT')
	upper_limit.text=a
	compu_const=ET.SubElement(compu_scale,'COMPU-CONST')
	v=ET.SubElement(compu_const,'V')
	v.text=b

def tab_nointp_compu_Scale_DefaultValue(cm_DefaultValue):#completed
	a=processor.value_to_str(cm_DefaultValue)
	compu_default_value=ET.SubElement(compu_internal_to_phys,'COMPU-DEFAULT-VALUE')
	vf=ET.SubElement(compu_default_value,'VF')
	vf.text=a

def CompuMethod_text(CompuMethods_shared_folder_elements, compu_method_shortname, unit):#completed
	global compu_scales, compu_internal_to_phys
	compu_method=ET.SubElement(CompuMethods_shared_folder_elements,'COMPU-METHOD')
	compu_method.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(compu_method,'SHORT-NAME')
	short_name.text=compu_method_shortname
	category=ET.SubElement(compu_method,'CATEGORY')
	category.text='TEXTTABLE'
	unit_ref=ET.SubElement(compu_method,'UNIT-REF')
	unit_ref.text=f'/AUTOSAR/AUTOSAR_PhysicalUnits/Units/{unit}'
	unit_ref.attrib={'DEST':'UNIT'}
	compu_internal_to_phys=ET.SubElement(compu_method,'COMPU-INTERNAL-TO-PHYS')
	compu_scales=ET.SubElement(compu_internal_to_phys,'COMPU-SCALES')

def text_compu_Scale(value,enum):#completed
	a=processor.value_to_str(value)
	b=processor.value_to_str(enum)
	
	compu_scale=ET.SubElement(compu_scales,'COMPU-SCALE')
	''' #fetch
	symbol5 = ET.SubElement(compu_scale17, 'SYMBOL')
    symbol5.text = 'text1'
	'''
	lower_limit=ET.SubElement(compu_scale,'LOWER-LIMIT')
	lower_limit.text=a
	upper_limit=ET.SubElement(compu_scale,'UPPER-LIMIT')
	upper_limit.text=a
	compu_const=ET.SubElement(compu_scale,'COMPU-CONST')
	vt=ET.SubElement(compu_const,'VT')
	vt.text=b

def text_compu_DefaultValue(cm_DefaultValue):#completed
	a=processor.value_to_str(cm_DefaultValue)
	compu_default_value=ET.SubElement(compu_internal_to_phys,'COMPU-DEFAULT-VALUE')
	v=ET.SubElement(compu_default_value,'V')
	v.text=a


########## other shared elements 	##############

def ConstantSpecification(ConstantSpecifications_folder_elements,constant_spec_shortname, constant_spec_Val):#completed
	a=processor.value_to_str(constant_spec_Val)
	constant_specification=ET.SubElement(ConstantSpecifications_folder_elements,'CONSTANT-SPECIFICATION')
	constant_specification.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(constant_specification,'SHORT-NAME')
	short_name.text=constant_spec_shortname
	value_spec=ET.SubElement(constant_specification,'VALUE-SPEC')
	numerical_value_specification=ET.SubElement(value_spec,'NUMERICAL-VALUE-SPECIFICATION')
	short_label=ET.SubElement(numerical_value_specification,'SHORT-LABEL')
	short_label.text='Value'
	value=ET.SubElement(numerical_value_specification,'VALUE')
	value.text=a

def DataConstr(DataConstr_folder_elements, DataConstr_shortname,ll,ul):#completed
	a=processor.value_to_str(ll)
	b=processor.value_to_str(ul)
	data_constr=ET.SubElement(DataConstr_folder_elements,'DATA-CONSTR')
	data_constr.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(data_constr,'SHORT-NAME')
	short_name.text=DataConstr_shortname
	data_constr_rules=ET.SubElement(data_constr,'DATA-CONSTR-RULES')
	data_constr_rule=ET.SubElement(data_constr_rules,'DATA-CONSTR-RULE')

	    #fetch
	'''
	constr_level = ET.SubElement(data_constr_rule, 'CONSTR-LEVEL')
    constr_level.text = '0'
	'''

	phys_constrs=ET.SubElement(data_constr_rule,'PHYS-CONSTRS')
	lower_limit=ET.SubElement(phys_constrs,'LOWER-LIMIT')
	lower_limit.text=a
	upper_limit=ET.SubElement(phys_constrs,'UPPER-LIMIT')
	upper_limit.text=b

def SwcImplementation(SwcImplementation_folder_elements,SwcImplementation_shortname,SWC_IB):#completed

	swc_implementation=ET.SubElement(SwcImplementation_folder_elements,'SWC-IMPLEMENTATION')
	swc_implementation.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(swc_implementation,'SHORT-NAME')
	short_name.text=SwcImplementation_shortname
	programming_language=ET.SubElement(swc_implementation,'PROGRAMMING-LANGUAGE')
	programming_language.text='C'
	resource_consumption=ET.SubElement(swc_implementation,'RESOURCE-CONSUMPTION')
	resource_consumption.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(resource_consumption,'SHORT-NAME')
	short_name.text='ResourceConsumption'
	sw_version=ET.SubElement(swc_implementation,'SW-VERSION')
	sw_version.text='1.0.0.0'
	behavior_ref=ET.SubElement(swc_implementation,'BEHAVIOR-REF')
	behavior_ref.text=f'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/{SWC_IB}' #run if else for each SWC type
	behavior_ref.attrib={'DEST':'SWC-INTERNAL-BEHAVIOR'}

def SwAddrMethod(SwAddrMethod_folder_elements, SwAddrMethod_shortname, mem_alloc_policy, mem_section_type):#completed
	sw_addr_method=ET.SubElement(SwAddrMethod_folder_elements,'SW-ADDR-METHOD')
	sw_addr_method.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(sw_addr_method,'SHORT-NAME')
	short_name.text=SwAddrMethod_shortname
	memory_allocation_keyword_policy=ET.SubElement(sw_addr_method,'MEMORY-ALLOCATION-KEYWORD-POLICY')
	memory_allocation_keyword_policy.text= mem_alloc_policy  #'ADDR-METHOD-SHORT-NAME', 'ADDR-METHOD-SHORT-NAME-AND-ALIGNMENT'
	section_type=ET.SubElement(sw_addr_method,'SECTION-TYPE')
	section_type.text= mem_section_type # 'CODE', 'CALIBRATION-VARIABLES', VAR, CONST, CALPARM, CONFIG-DATA, EXCLUDE-FROM-Flash
	

########## DATA type mapping set ##########

def DataTypeMappingSet(DataTypemappingSets_folder_elements, CurrentSWC_shortname): #completed
	global data_type_maps

	data_type_mapping_set=ET.SubElement(DataTypemappingSets_folder_elements,'DATA-TYPE-MAPPING-SET')
	data_type_mapping_set.attrib={'UUID': rng.generate_uuid()}
	short_name=ET.SubElement(data_type_mapping_set,'SHORT-NAME')
	short_name.text=f'DTMS_{CurrentSWC_shortname}'
	data_type_maps=ET.SubElement(data_type_mapping_set,'DATA-TYPE-MAPS')

def data_type_map(adt,idt): #completed
	data_type_map=ET.SubElement(data_type_maps,'DATA-TYPE-MAP')
	application_data_type_ref=ET.SubElement(data_type_map,'APPLICATION-DATA-TYPE-REF')
	application_data_type_ref.text=f'/SharedElements/ApplicationDataTypes/Array/{adt}'
	application_data_type_ref.attrib={'DEST':'APPLICATION-ARRAY-DATA-TYPE'}
	implementation_data_type_ref=ET.SubElement(data_type_map,'IMPLEMENTATION-DATA-TYPE-REF')
	implementation_data_type_ref.text=f'/SharedElements/ImplementationDataTypes/{idt}'
	implementation_data_type_ref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}

########## Implementation Data type ########## ApplicationArrayDataType_Fixed

def ImplementationDataType_ArrayFixed(ImplementationDataTypes_folder_elements, IDT_shortname, arraysize_fixed, IDT):#completed

	implementation_data_type=ET.SubElement(ImplementationDataTypes_folder_elements,'IMPLEMENTATION-DATA-TYPE')
	implementation_data_type.attrib={'UUID': rng.generate_uuid()}
	short_name=ET.SubElement(implementation_data_type,'SHORT-NAME')
	short_name.text=IDT_shortname
	category=ET.SubElement(implementation_data_type,'CATEGORY')
	category.text='ARRAY'
	sub_elements=ET.SubElement(implementation_data_type,'SUB-ELEMENTS')
	implementation_data_type_element=ET.SubElement(sub_elements,'IMPLEMENTATION-DATA-TYPE-ELEMENT')
	implementation_data_type_element.attrib={'UUID': rng.generate_uuid()}
	short_name=ET.SubElement(implementation_data_type_element,'SHORT-NAME')
	short_name.text='SubElement'
	category=ET.SubElement(implementation_data_type_element,'CATEGORY')
	category.text='TYPE_REFERENCE'
	array_size=ET.SubElement(implementation_data_type_element,'ARRAY-SIZE')
	array_size.text=arraysize_fixed
	array_size_semantics=ET.SubElement(implementation_data_type_element,'ARRAY-SIZE-SEMANTICS')
	array_size_semantics.text='FIXED-SIZE'
	sw_data_def_props=ET.SubElement(implementation_data_type_element,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	implementation_data_type_ref=ET.SubElement(sw_data_def_props_conditional,'IMPLEMENTATION-DATA-TYPE-REF')
	implementation_data_type_ref.text=f'/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/{IDT}'
	implementation_data_type_ref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}

def ImplementationDataType_ArrayVariable(ImplementationDataTypes_folder_elements, IDT_shortname, arraysize_fixed, IDT):#completed but need to revisit after actual implementation

	implementation_data_type=ET.SubElement(ImplementationDataTypes_folder_elements,'IMPLEMENTATION-DATA-TYPE')
	implementation_data_type.attrib={'UUID': rng.generate_uuid()}
	short_name=ET.SubElement(implementation_data_type,'SHORT-NAME')
	short_name.text=IDT_shortname
	category=ET.SubElement(implementation_data_type,'CATEGORY')
	category.text='ARRAY'
	sub_elements=ET.SubElement(implementation_data_type,'SUB-ELEMENTS')
	implementation_data_type_element=ET.SubElement(sub_elements,'IMPLEMENTATION-DATA-TYPE-ELEMENT')
	implementation_data_type_element.attrib={'UUID': rng.generate_uuid()}
	short_name=ET.SubElement(implementation_data_type_element,'SHORT-NAME')
	short_name.text='SubElement'
	category=ET.SubElement(implementation_data_type_element,'CATEGORY')
	category.text='TYPE_REFERENCE'
	array_size=ET.SubElement(implementation_data_type_element,'ARRAY-SIZE')
	array_size.text=arraysize_fixed
	array_size_semantics=ET.SubElement(implementation_data_type_element,'ARRAY-SIZE-SEMANTICS')
	array_size_semantics.text='VARIABLE-SIZE'
	sw_data_def_props=ET.SubElement(implementation_data_type_element,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	implementation_data_type_ref=ET.SubElement(sw_data_def_props_conditional,'IMPLEMENTATION-DATA-TYPE-REF')
	implementation_data_type_ref.text=f'/SharedElements/ImplementationDataTypes/{IDT}'
	implementation_data_type_ref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}

		# make a structure element with following structure 
		# <IMPLEMENTATION-DATA-TYPE UUID="53ec3bfc-5a92-4d42-b31b-8e29e99a2b46">
        #       <SHORT-NAME>STRUCTURE_ImplementationDataType1</SHORT-NAME>
        #       <CATEGORY>STRUCTURE</CATEGORY>
        #       <SUB-ELEMENTS>
        #         <IMPLEMENTATION-DATA-TYPE-ELEMENT UUID="31f01782-3ce8-4dbe-81d1-0d5fb89bef99">
        #           <SHORT-NAME>SubElement</SHORT-NAME>
        #           <CATEGORY>TYPE_REFERENCE</CATEGORY>
        #           <SW-DATA-DEF-PROPS>
        #             <SW-DATA-DEF-PROPS-VARIANTS>
        #               <SW-DATA-DEF-PROPS-CONDITIONAL>
        #                 <IMPLEMENTATION-DATA-TYPE-REF DEST="IMPLEMENTATION-DATA-TYPE">/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16</IMPLEMENTATION-DATA-TYPE-REF>
        #               </SW-DATA-DEF-PROPS-CONDITIONAL>
        #             </SW-DATA-DEF-PROPS-VARIANTS>
        #           </SW-DATA-DEF-PROPS>
        #         </IMPLEMENTATION-DATA-TYPE-ELEMENT>
        #         <IMPLEMENTATION-DATA-TYPE-ELEMENT UUID="83bd06cb-a4ff-4d55-bd3d-1a691b582d46">
        #           <SHORT-NAME>SubElement1</SHORT-NAME>
        #           <CATEGORY>TYPE_REFERENCE</CATEGORY>
        #           <SW-DATA-DEF-PROPS>
        #             <SW-DATA-DEF-PROPS-VARIANTS>
        #               <SW-DATA-DEF-PROPS-CONDITIONAL>
        #                 <IMPLEMENTATION-DATA-TYPE-REF DEST="IMPLEMENTATION-DATA-TYPE">/SharedElements/ImplementationDataTypes/ARRAY_ImplementationDataType</IMPLEMENTATION-DATA-TYPE-REF>
        #               </SW-DATA-DEF-PROPS-CONDITIONAL>
        #             </SW-DATA-DEF-PROPS-VARIANTS>
        #           </SW-DATA-DEF-PROPS>
        #         </IMPLEMENTATION-DATA-TYPE-ELEMENT>
        #       </SUB-ELEMENTS>
        #     </IMPLEMENTATION-DATA-TYPE>

		#   <IMPLEMENTATION-DATA-TYPE UUID="21f9a013-317d-4a6a-8c1d-cdc72f7df8f5">
		#   <SHORT-NAME>ARRAY_ImplementationDataType</SHORT-NAME>
		#   <CATEGORY>ARRAY</CATEGORY>
		#   <SW-DATA-DEF-PROPS>
		#     <SW-DATA-DEF-PROPS-VARIANTS>
		#       <SW-DATA-DEF-PROPS-CONDITIONAL />
		#     </SW-DATA-DEF-PROPS-VARIANTS>
		#   </SW-DATA-DEF-PROPS>
		#   <SUB-ELEMENTS>
		#     <IMPLEMENTATION-DATA-TYPE-ELEMENT UUID="5512b8b7-a43f-436f-bb18-47a903ad1e17">
		#       <SHORT-NAME>SubElement</SHORT-NAME>
		#       <CATEGORY>TYPE_REFERENCE</CATEGORY>
		#       <ARRAY-SIZE>15</ARRAY-SIZE>
		#       <ARRAY-SIZE-SEMANTICS>FIXED-SIZE</ARRAY-SIZE-SEMANTICS>
		#       <SW-DATA-DEF-PROPS>
		#         <SW-DATA-DEF-PROPS-VARIANTS>
		#           <SW-DATA-DEF-PROPS-CONDITIONAL>
		#             <IMPLEMENTATION-DATA-TYPE-REF DEST="IMPLEMENTATION-DATA-TYPE">/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16</IMPLEMENTATION-DATA-TYPE-REF>
		#           </SW-DATA-DEF-PROPS-CONDITIONAL>
		#         </SW-DATA-DEF-PROPS-VARIANTS>
		#       </SW-DATA-DEF-PROPS>
		#     </IMPLEMENTATION-DATA-TYPE-ELEMENT>
		#   </SUB-ELEMENTS>
		# </IMPLEMENTATION-DATA-TYPE>



		# for dtms

		# <APPLICATION-ARRAY-DATA-TYPE UUID="d5f3c7e9-dd94-4d37-888e-b6e44b01cc5a">
        #           <SHORT-NAME>ApplicationArrayDataType_Variable</SHORT-NAME>
        #           <CATEGORY>ARRAY</CATEGORY>
        #           <ELEMENT UUID="fef3f4b8-d9bd-4cb1-94b8-4403e665c4fa">
        #             <SHORT-NAME>Element</SHORT-NAME>
        #             <CATEGORY>VALUE</CATEGORY>
        #             <TYPE-TREF DEST="APPLICATION-PRIMITIVE-DATA-TYPE">/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType</TYPE-TREF>
        #             <ARRAY-SIZE-SEMANTICS>VARIABLE-SIZE</ARRAY-SIZE-SEMANTICS>
        #             <MAX-NUMBER-OF-ELEMENTS>15</MAX-NUMBER-OF-ELEMENTS>
        #           </ELEMENT>
        #         </APPLICATION-ARRAY-DATA-TYPE>

		#         <IMPLEMENTATION-DATA-TYPE UUID="ccd15817-26a8-424d-8c87-3f3d70b5ee9d">
		#   <SHORT-NAME>Struct_Array_ImplementationDataType</SHORT-NAME>
		#   <CATEGORY>STRUCTURE</CATEGORY>
		#   <SUB-ELEMENTS>
		#     <IMPLEMENTATION-DATA-TYPE-ELEMENT UUID="3f61bc0d-d829-4ab0-9e22-7de6a25972e3">
		#       <SHORT-NAME>SubElement1</SHORT-NAME>
		#       <CATEGORY>TYPE_REFERENCE</CATEGORY>
		#       <SW-DATA-DEF-PROPS>
		#         <SW-DATA-DEF-PROPS-VARIANTS>
		#           <SW-DATA-DEF-PROPS-CONDITIONAL>
		#             <IMPLEMENTATION-DATA-TYPE-REF DEST="IMPLEMENTATION-DATA-TYPE">/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8</IMPLEMENTATION-DATA-TYPE-REF>
		#           </SW-DATA-DEF-PROPS-CONDITIONAL>
		#         </SW-DATA-DEF-PROPS-VARIANTS>
		#       </SW-DATA-DEF-PROPS>
		#     </IMPLEMENTATION-DATA-TYPE-ELEMENT>
		#     <IMPLEMENTATION-DATA-TYPE-ELEMENT UUID="dc530c9c-3b65-4707-99c3-842e2d2b7788">
		#       <SHORT-NAME>SubElement</SHORT-NAME>
		#       <CATEGORY>ARRAY</CATEGORY>
		#       <SUB-ELEMENTS>
		#         <IMPLEMENTATION-DATA-TYPE-ELEMENT UUID="af21d788-9aea-4789-b7d0-8665f2d0c8c7">
		#           <SHORT-NAME>SubElement</SHORT-NAME>
		#           <CATEGORY>TYPE_REFERENCE</CATEGORY>
		#           <ARRAY-SIZE>15</ARRAY-SIZE>
		#           <ARRAY-SIZE-SEMANTICS>VARIABLE-SIZE</ARRAY-SIZE-SEMANTICS>
		#           <SW-DATA-DEF-PROPS>
		#             <SW-DATA-DEF-PROPS-VARIANTS>
		#               <SW-DATA-DEF-PROPS-CONDITIONAL>
		#                 <IMPLEMENTATION-DATA-TYPE-REF DEST="IMPLEMENTATION-DATA-TYPE">/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16</IMPLEMENTATION-DATA-TYPE-REF>
		#               </SW-DATA-DEF-PROPS-CONDITIONAL>
		#             </SW-DATA-DEF-PROPS-VARIANTS>
		#           </SW-DATA-DEF-PROPS>
		#         </IMPLEMENTATION-DATA-TYPE-ELEMENT>
		#       </SUB-ELEMENTS>
		#       <SW-DATA-DEF-PROPS>
		#         <SW-DATA-DEF-PROPS-VARIANTS>
		#           <SW-DATA-DEF-PROPS-CONDITIONAL />
		#         </SW-DATA-DEF-PROPS-VARIANTS>
		#       </SW-DATA-DEF-PROPS>
		#     </IMPLEMENTATION-DATA-TYPE-ELEMENT>
		#   </SUB-ELEMENTS>
		# </IMPLEMENTATION-DATA-TYPE>

		# def Struct_Array_ImplementationDataType():

		# 	implementation_data_type5=ET.SubElement(elements10,'IMPLEMENTATION-DATA-TYPE')
		# 	implementation_data_type5.attrib={'UUID':rng.generate_uuid()} #ccd15817-26a8-424d-8c87-3f3d70b5ee9d'}
		# 	short_name46=ET.SubElement(implementation_data_type5,'SHORT-NAME')
		# 	short_name46.text='Struct_Array_ImplementationDataType'
		# 	category27=ET.SubElement(implementation_data_type5,'CATEGORY')
		# 	category27.text='STRUCTURE'
		# 	sub_elements4=ET.SubElement(implementation_data_type5,'SUB-ELEMENTS')
		# 	implementation_data_type_element5=ET.SubElement(sub_elements4,'IMPLEMENTATION-DATA-TYPE-ELEMENT')
		# 	implementation_data_type_element5.attrib={'UUID':rng.generate_uuid()} #3f61bc0d-d829-4ab0-9e22-7de6a25972e3'}
		# 	short_name47=ET.SubElement(implementation_data_type_element5,'SHORT-NAME')
		# 	short_name47.text='SubElement1'
		# 	category28=ET.SubElement(implementation_data_type_element5,'CATEGORY')
		# 	category28.text='TYPE_REFERENCE'
		# 	sw_data_def_props11=ET.SubElement(implementation_data_type_element5,'SW-DATA-DEF-PROPS')
		# 	sw_data_def_props_variants11=ET.SubElement(sw_data_def_props11,'SW-DATA-DEF-PROPS-VARIANTS')
		# 	sw_data_def_props_conditional11=ET.SubElement(sw_data_def_props_variants11,'SW-DATA-DEF-PROPS-CONDITIONAL')
		# 	implementation_data_type_ref9=ET.SubElement(sw_data_def_props_conditional11,'IMPLEMENTATION-DATA-TYPE-REF')
		# 	implementation_data_type_ref9.text='/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
		# 	implementation_data_type_ref9.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}
		# 	implementation_data_type_element6=ET.SubElement(sub_elements4,'IMPLEMENTATION-DATA-TYPE-ELEMENT')
		# 	implementation_data_type_element6.attrib={'UUID':rng.generate_uuid()} #dc530c9c-3b65-4707-99c3-842e2d2b7788'}
		# 	short_name48=ET.SubElement(implementation_data_type_element6,'SHORT-NAME')
		# 	short_name48.text='SubElement'
		# 	category29=ET.SubElement(implementation_data_type_element6,'CATEGORY')
		# 	category29.text='ARRAY'
		# 	sub_elements5=ET.SubElement(implementation_data_type_element6,'SUB-ELEMENTS')
		# 	implementation_data_type_element7=ET.SubElement(sub_elements5,'IMPLEMENTATION-DATA-TYPE-ELEMENT')
		# 	implementation_data_type_element7.attrib={'UUID':rng.generate_uuid()} #af21d788-9aea-4789-b7d0-8665f2d0c8c7'}
		# 	short_name49=ET.SubElement(implementation_data_type_element7,'SHORT-NAME')
		# 	short_name49.text='SubElement'
		# 	category30=ET.SubElement(implementation_data_type_element7,'CATEGORY')
		# 	category30.text='TYPE_REFERENCE'
		# 	array_size3=ET.SubElement(implementation_data_type_element7,'ARRAY-SIZE')
		# 	array_size3.text='15'
		# 	array_size_semantics6=ET.SubElement(implementation_data_type_element7,'ARRAY-SIZE-SEMANTICS')
		# 	array_size_semantics6.text='VARIABLE-SIZE'
		# 	sw_data_def_props12=ET.SubElement(implementation_data_type_element7,'SW-DATA-DEF-PROPS')
		# 	sw_data_def_props_variants12=ET.SubElement(sw_data_def_props12,'SW-DATA-DEF-PROPS-VARIANTS')
		# 	sw_data_def_props_conditional12=ET.SubElement(sw_data_def_props_variants12,'SW-DATA-DEF-PROPS-CONDITIONAL')
		# 	implementation_data_type_ref10=ET.SubElement(sw_data_def_props_conditional12,'IMPLEMENTATION-DATA-TYPE-REF')
		# 	implementation_data_type_ref10.text='/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
		# 	implementation_data_type_ref10.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}
		# 	sw_data_def_props13=ET.SubElement(implementation_data_type_element6,'SW-DATA-DEF-PROPS')
		# 	sw_data_def_props_variants13=ET.SubElement(sw_data_def_props13,'SW-DATA-DEF-PROPS-VARIANTS')
		# 	sw_data_def_props_conditional13=ET.SubElement(sw_data_def_props_variants13,'SW-DATA-DEF-PROPS-CONDITIONAL')
		# 	implementation_data_type6=ET.SubElement(elements10,'IMPLEMENTATION-DATA-TYPE')
		# 	implementation_data_type6.attrib={'UUID':rng.generate_uuid()} #79fa9e8f-a805-43da-b4b5-ac42d2a23ff0'}
		# 	short_name50=ET.SubElement(implementation_data_type6,'SHORT-NAME')
		# 	short_name50.text='TypeTref_ImplementationDataType'
		# 	category31=ET.SubElement(implementation_data_type6,'CATEGORY')
		# 	category31.text='TYPE_REFERENCE'
		# 	sw_data_def_props14=ET.SubElement(implementation_data_type6,'SW-DATA-DEF-PROPS')
		# 	sw_data_def_props_variants14=ET.SubElement(sw_data_def_props14,'SW-DATA-DEF-PROPS-VARIANTS')
		# 	sw_data_def_props_conditional14=ET.SubElement(sw_data_def_props_variants14,'SW-DATA-DEF-PROPS-CONDITIONAL')
		# 	implementation_data_type_ref11=ET.SubElement(sw_data_def_props_conditional14,'IMPLEMENTATION-DATA-TYPE-REF')
		# 	implementation_data_type_ref11.text='/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float32'
		# 	implementation_data_type_ref11.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}

def ImplementationDataType(ImplementationDataTypes_folder_elements, IDT_shortname, IDT):#completed

	implementation_data_type=ET.SubElement(ImplementationDataTypes_folder_elements,'IMPLEMENTATION-DATA-TYPE')
	implementation_data_type.attrib={'UUID': rng.generate_uuid()}
	short_name=ET.SubElement(implementation_data_type,'SHORT-NAME')
	short_name.text=IDT_shortname
	category=ET.SubElement(implementation_data_type,'CATEGORY')
	category.text='VALUE'
	sw_data_def_props=ET.SubElement(implementation_data_type,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	base_type_ref=ET.SubElement(sw_data_def_props_conditional,'BASE-TYPE-REF')
	base_type_ref.text=f'/AUTOSAR/AUTOSAR_Platform/BaseTypes/{IDT}'
	base_type_ref.attrib={'DEST':'SW-BASE-TYPE'}

def ImplementationDataType_Structure(ImplementationDataTypes_folder_elements, IDT_shortname):#completed
	global IDT_elements
	implementation_data_type=ET.SubElement(ImplementationDataTypes_folder_elements,'IMPLEMENTATION-DATA-TYPE')
	implementation_data_type.attrib={'UUID': rng.generate_uuid()}
	short_name=ET.SubElement(implementation_data_type,'SHORT-NAME')
	short_name.text=IDT_shortname
	category=ET.SubElement(implementation_data_type,'CATEGORY')
	category.text='STRUCTURE'
	IDT_elements=ET.SubElement(implementation_data_type,'SUB-ELEMENTS')

def ApplicationRecordDataType_elements(IDT_element_shortname, IDT):#completed 
    implementation_data_type_element=ET.SubElement(IDT_elements,'IMPLEMENTATION-DATA-TYPE-ELEMENT')
    implementation_data_type_element.attrib={'UUID': rng.generate_uuid()}
    short_name=ET.SubElement(implementation_data_type_element,'SHORT-NAME')
    short_name.text=IDT_element_shortname
    category=ET.SubElement(implementation_data_type_element,'CATEGORY')
    category.text='TYPE_REFERENCE'
    sw_data_def_props=ET.SubElement(implementation_data_type_element,'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
    implementation_data_type_ref=ET.SubElement(sw_data_def_props_conditional,'IMPLEMENTATION-DATA-TYPE-REF')
    implementation_data_type_ref.text=f'/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/{IDT}'
    implementation_data_type_ref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}


############ Interfaces ##################### 

def ClientServerInterface(ClientServer_folder_elements, IF_Name):#completed
    global client_server_interface
    client_server_interface=ET.SubElement(ClientServer_folder_elements,'CLIENT-SERVER-INTERFACE')
    client_server_interface.attrib={'UUID':rng.generate_uuid()}
    short_name=ET.SubElement(client_server_interface,'SHORT-NAME')
    short_name.text= IF_Name
    is_service=ET.SubElement(client_server_interface,'IS-SERVICE')
    is_service.text='false'

def ClientServerInterface_Opr():#completed
	global operations
	operations=ET.SubElement(client_server_interface,'OPERATIONS')

def ClientServerInterface_CSOpr(Operation_shortname):#completed
	global client_server_operation
	client_server_operation=ET.SubElement(operations,'CLIENT-SERVER-OPERATION')
	client_server_operation.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(client_server_operation,'SHORT-NAME')
	short_name.text=Operation_shortname

def ClientServerInterface_Arg(Argument_shortname, type_tref_adt):#completed

    arguments=ET.SubElement(client_server_operation,'ARGUMENTS')
    argument_data_prototype=ET.SubElement(arguments,'ARGUMENT-DATA-PROTOTYPE')
    argument_data_prototype.attrib={'UUID':rng.generate_uuid()}
    short_name=ET.SubElement(argument_data_prototype,'SHORT-NAME')
    short_name.text=Argument_shortname
    sw_data_def_props=ET.SubElement(argument_data_prototype,'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_impl_policy=ET.SubElement(sw_data_def_props_conditional,'SW-IMPL-POLICY')
    sw_impl_policy.text='STANDARD'
    type_tref=ET.SubElement(argument_data_prototype,'TYPE-TREF')
    type_tref.text=f'/SharedElements/ApplicationDataTypes/Primitive/{type_tref_adt}'
    type_tref.attrib={'DEST':'APPLICATION-PRIMITIVE-DATA-TYPE'}
    direction=ET.SubElement(argument_data_prototype,'DIRECTION')
    direction.text='IN'
    server_argument_impl_policy=ET.SubElement(argument_data_prototype,'SERVER-ARGUMENT-IMPL-POLICY')
    server_argument_impl_policy.text='USE-ARGUMENT-TYPE'

def ModeDeclarationGroup(ModeSwitch_folder_elements, ModeDeclarationGroup_shortname, mode_Category,Init_Mode):#completed
	global mode_declarations
	mode_declaration_group=ET.SubElement(ModeSwitch_folder_elements,'MODE-DECLARATION-GROUP')
	mode_declaration_group.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(mode_declaration_group,'SHORT-NAME')
	short_name.text=ModeDeclarationGroup_shortname
	category=ET.SubElement(mode_declaration_group,'CATEGORY')
	category.text= mode_Category
	initial_mode_ref=ET.SubElement(mode_declaration_group,'INITIAL-MODE-REF')
	initial_mode_ref.text=f'/SharedElements/PortInterfaces/ModeSwitch/{short_name.text}/{Init_Mode}'
	initial_mode_ref.attrib={'DEST':'MODE-DECLARATION'}
	mode_declarations=ET.SubElement(mode_declaration_group,'MODE-DECLARATIONS')

	''' #fetch
		on_transition_value = ET.SubElement(mode_declaration_group, 'ON-TRANSITION-VALUE')
    	on_transition_value.text = '3'
	'''
    
def ModeDeclarationGroup_Exp(ModeDeclaration_shortname):#completed

    mode_declaration=ET.SubElement(mode_declarations,'MODE-DECLARATION')
    mode_declaration.attrib={'UUID':rng.generate_uuid()}
    short_name=ET.SubElement(mode_declaration,'SHORT-NAME')
    short_name.text=ModeDeclaration_shortname

	# ''' #fetch
	# value = ET.SubElement(mode_declaration, 'VALUE')
    # value.text = '0'
	# '''

def ModeSwitchInterface(ModeSwitch_folder_elements, ModeSwitchInterface_shortname, ModeDeclarationGroup_shortname):#completed

	mode_switch_interface=ET.SubElement(ModeSwitch_folder_elements,'MODE-SWITCH-INTERFACE')
	mode_switch_interface.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(mode_switch_interface,'SHORT-NAME')
	short_name.text=ModeSwitchInterface_shortname
	is_service=ET.SubElement(mode_switch_interface,'IS-SERVICE')
	is_service.text='false'
	mode_group=ET.SubElement(mode_switch_interface,'MODE-GROUP')
	mode_group.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(mode_group,'SHORT-NAME')
	short_name.text='ModeGroup'
	type_tref=ET.SubElement(mode_group,'TYPE-TREF')
	type_tref.text=f'/SharedElements/PortInterfaces/ModeSwitch/{ModeDeclarationGroup_shortname}'
	type_tref.attrib={'DEST':'MODE-DECLARATION-GROUP'}

def NvDataInterface(NvData_folder_elements, IF_Name):#completed
 
    global nv_data_interface


    nv_data_interface=ET.SubElement(NvData_folder_elements,'NV-DATA-INTERFACE')
    nv_data_interface.attrib={'UUID':rng.generate_uuid()} #8a4989b3-88e2-4e47-b98f-591e75c76b17'}
    short_name=ET.SubElement(nv_data_interface,'SHORT-NAME')
    short_name.text=IF_Name
    is_service=ET.SubElement(nv_data_interface,'IS-SERVICE')
    is_service.text='false'

def NvDataInterface_DE():#completed
	global nv_datas
	nv_datas=ET.SubElement(nv_data_interface,'NV-DATAS')

def NvDataInterface_VDP(nv_datas_shortname, type_tref_adt):#completed
    variable_data_prototype=ET.SubElement(nv_datas,'VARIABLE-DATA-PROTOTYPE')
    variable_data_prototype.attrib={'UUID':rng.generate_uuid()}
    short_name=ET.SubElement(variable_data_prototype,'SHORT-NAME')
    short_name.text=nv_datas_shortname
    sw_data_def_props=ET.SubElement(variable_data_prototype,'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
    sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
    sw_calibration_access.text='READ-WRITE'
    sw_impl_policy=ET.SubElement(sw_data_def_props_conditional,'SW-IMPL-POLICY')
    sw_impl_policy.text='STANDARD'
    type_tref=ET.SubElement(variable_data_prototype,'TYPE-TREF')
    type_tref.text=f'/SharedElements/ApplicationDataTypes/Primitive/{type_tref_adt}'
    type_tref.attrib={'DEST':'APPLICATION-PRIMITIVE-DATA-TYPE'}

def ParameterInterface(Parameter_folder_elements, IF_Name):#completed
	global parameter_interface
	parameter_interface=ET.SubElement(Parameter_folder_elements,'PARAMETER-INTERFACE')
	parameter_interface.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(parameter_interface,'SHORT-NAME')
	short_name.text= IF_Name
	is_service=ET.SubElement(parameter_interface,'IS-SERVICE')
	is_service.text='false'

def ParameterInterface_DE():#completed
	global parameters
	parameters=ET.SubElement(parameter_interface,'PARAMETERS')

def ParameterInterface_VDP(Parameter_shortname, type_tref_adt):#completed

	parameter_data_prototype=ET.SubElement(parameters,'PARAMETER-DATA-PROTOTYPE')
	parameter_data_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(parameter_data_prototype,'SHORT-NAME')
	short_name.text=Parameter_shortname
	sw_data_def_props=ET.SubElement(parameter_data_prototype,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text='READ-WRITE'
	sw_impl_policy=ET.SubElement(sw_data_def_props_conditional,'SW-IMPL-POLICY')
	sw_impl_policy.text='STANDARD'
	type_tref=ET.SubElement(parameter_data_prototype,'TYPE-TREF')
	type_tref.text=f'/SharedElements/ApplicationDataTypes/Primitive/{type_tref_adt}'
	type_tref.attrib={'DEST':'APPLICATION-PRIMITIVE-DATA-TYPE'}

def SenderReceiverInterface(SenderReceiver_folder_elements, IF_Name):#completed
	global sender_receiver_interface
	sender_receiver_interface=ET.SubElement(SenderReceiver_folder_elements,'SENDER-RECEIVER-INTERFACE')
	sender_receiver_interface.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(sender_receiver_interface,'SHORT-NAME')
	short_name.text= IF_Name
	is_service=ET.SubElement(sender_receiver_interface,'IS-SERVICE')
	is_service.text='false'

def SenderReceiverInterface_DE():#completed
	global data_elements
	data_elements=ET.SubElement(sender_receiver_interface,'DATA-ELEMENTS')

def SenderReceiverInterface_VDP(DataElement_shortname, type_tref_adt):#completed

	variable_data_prototype=ET.SubElement(data_elements,'VARIABLE-DATA-PROTOTYPE')
	variable_data_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(variable_data_prototype,'SHORT-NAME')
	short_name.text=DataElement_shortname
	sw_data_def_props=ET.SubElement(variable_data_prototype,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text='READ-WRITE'
	sw_impl_policy=ET.SubElement(sw_data_def_props_conditional,'SW-IMPL-POLICY')
	sw_impl_policy.text='STANDARD'
	type_tref=ET.SubElement(variable_data_prototype,'TYPE-TREF')
	type_tref.text=f'/SharedElements/ApplicationDataTypes/Primitive/{type_tref_adt}'
	type_tref.attrib={'DEST':'APPLICATION-PRIMITIVE-DATA-TYPE'}
	
	# variable_data_prototype14=ET.SubElement(data_elements6,'VARIABLE-DATA-PROTOTYPE')
	# variable_data_prototype14.attrib={'UUID':rng.generate_uuid()} #6862a5ea-8794-4906-9f54-50624e9d6044'}
	# short_name117=ET.SubElement(variable_data_prototype14,'SHORT-NAME')
	# short_name117.text='DataElement1'
	# sw_data_def_props40=ET.SubElement(variable_data_prototype14,'SW-DATA-DEF-PROPS')
	# sw_data_def_props_variants40=ET.SubElement(sw_data_def_props40,'SW-DATA-DEF-PROPS-VARIANTS')
	# sw_data_def_props_conditional40=ET.SubElement(sw_data_def_props_variants40,'SW-DATA-DEF-PROPS-CONDITIONAL')
	# sw_impl_policy26=ET.SubElement(sw_data_def_props_conditional40,'SW-IMPL-POLICY')
	# sw_impl_policy26.text='STANDARD'
	# type_tref32=ET.SubElement(variable_data_prototype14,'TYPE-TREF')
	# type_tref32.text='/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
	# type_tref32.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}
	# # invalidation_policys1=ET.SubElement(sender_receiver_interface,'INVALIDATION-POLICYS')
	# # invalidation_policy1=ET.SubElement(invalidation_policys1,'INVALIDATION-POLICY')
	# # data_element_ref1=ET.SubElement(invalidation_policy1,'DATA-ELEMENT-REF')
	# # data_element_ref1.text='/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
	# # data_element_ref1.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}
	# # handle_invalid1=ET.SubElement(invalidation_policy1,'HANDLE-INVALID')
	# # handle_invalid1.text='KEEP'

def TriggerInterface(Trigger_folder_elements, IF_Name):#completed
	global trigger_interface
	trigger_interface=ET.SubElement(Trigger_folder_elements,'TRIGGER-INTERFACE')
	trigger_interface.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(trigger_interface,'SHORT-NAME')
	short_name.text= IF_Name
	is_service=ET.SubElement(trigger_interface,'IS-SERVICE')
	is_service.text='false'

def TriggerInterface_trigs():#completed
	global triggers
	triggers=ET.SubElement(trigger_interface,'TRIGGERS')

def TriggerInterface_trig(trigger_shortname, cse_code, cse_code_factor):#completed
	a=processor.value_to_str(cse_code)
	b=processor.value_to_str(cse_code_factor)	
	
	trigger=ET.SubElement(triggers,'TRIGGER')
	trigger.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(trigger,'SHORT-NAME')
	short_name.text=trigger_shortname
	''' #fetch
		condition=ET.SubElement(trigger,'CONDITION')sw_impl_policy27 = ET.SubElement(trigger, 'SW-IMPL-POLICY')
		sw_impl_policy27.text = 'STANDARD'
	'''
	trigger_period=ET.SubElement(trigger,'TRIGGER-PERIOD')
	cse_code=ET.SubElement(trigger_period,'CSE-CODE')
	cse_code.text=a
	cse_code_factor=ET.SubElement(trigger_period,'CSE-CODE-FACTOR')
	cse_code_factor.text=b

########## PORTS ###########

# comspec of each port type (basically ports are categorised based on which type of interface they referenced) is different that is why we need to create each port type separately
# and this prt of the port , we will do it later

def create_ports(): #completed
    global ports
    ports=ET.SubElement(application_sw_component_type,'PORTS')

def RPort_SR(Port_shortname, referred_IF): 	#partially completed
	
    r_port_prototype=ET.SubElement(ports,'R-PORT-PROTOTYPE')
    r_port_prototype.attrib={'UUID':rng.generate_uuid()}
    short_name=ET.SubElement(r_port_prototype,'SHORT-NAME')
    short_name.text= Port_shortname
    required_interface_tref=ET.SubElement(r_port_prototype,'REQUIRED-INTERFACE-TREF')
    required_interface_tref.text=f'/SharedElements/PortInterfaces/SenderReceiver/{referred_IF}'
    required_interface_tref.attrib={'DEST':'SENDER-RECEIVER-INTERFACE'} 
 
def RPort_CS(Port_shortname, referred_IF):	#partially completed
 
	r_port_prototype=ET.SubElement(ports,'R-PORT-PROTOTYPE')
	r_port_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(r_port_prototype,'SHORT-NAME')
	short_name.text=Port_shortname
	required_interface_tref=ET.SubElement(r_port_prototype,'REQUIRED-INTERFACE-TREF')
	required_interface_tref.text=f'/SharedElements/PortInterfaces/ClientServer/{referred_IF}'
	required_interface_tref.attrib={'DEST':'CLIENT-SERVER-INTERFACE'}
 
def RPort_msi(Port_shortname, referred_IF): #partially completed
 
	r_port_prototype=ET.SubElement(ports,'R-PORT-PROTOTYPE')
	r_port_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(r_port_prototype,'SHORT-NAME')
	short_name.text=Port_shortname
	required_interface_tref=ET.SubElement(r_port_prototype,'REQUIRED-INTERFACE-TREF')
	required_interface_tref.text=f'/SharedElements/PortInterfaces/ModeSwitch/{referred_IF}'
	required_interface_tref.attrib={'DEST':'MODE-SWITCH-INTERFACE'}

def RPort_nvd(Port_shortname, referred_IF): #partially completed
 
	r_port_prototype=ET.SubElement(ports,'R-PORT-PROTOTYPE')
	r_port_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(r_port_prototype,'SHORT-NAME')
	short_name.text=Port_shortname
	required_interface_tref=ET.SubElement(r_port_prototype,'REQUIRED-INTERFACE-TREF')
	required_interface_tref.text=f'/SharedElements/PortInterfaces/NvData/{referred_IF}'
	required_interface_tref.attrib={'DEST':'NV-DATA-INTERFACE'}
 
def RPort_prm(Port_shortname, referred_IF): #partially completed
 
	r_port_prototype=ET.SubElement(ports,'R-PORT-PROTOTYPE')
	r_port_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(r_port_prototype,'SHORT-NAME')
	short_name.text=Port_shortname
	required_interface_tref=ET.SubElement(r_port_prototype,'REQUIRED-INTERFACE-TREF')
	required_interface_tref.text=f'/SharedElements/PortInterfaces/Parameter/{referred_IF}'
	required_interface_tref.attrib={'DEST':'PARAMETER-INTERFACE'}

def RPort_trigger(Port_shortname, referred_IF): #partially completed

	r_port_prototype=ET.SubElement(ports,'R-PORT-PROTOTYPE')
	r_port_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(r_port_prototype,'SHORT-NAME')
	short_name.text=Port_shortname
	required_interface_tref=ET.SubElement(r_port_prototype,'REQUIRED-INTERFACE-TREF')
	required_interface_tref.text=f'/SharedElements/PortInterfaces/Trigger/{referred_IF}'
	required_interface_tref.attrib={'DEST':'TRIGGER-INTERFACE'}
	
def PPort_SR(Port_shortname, referred_IF): #partially completed
     
	p_port_prototype=ET.SubElement(ports,'P-PORT-PROTOTYPE')
	p_port_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(p_port_prototype,'SHORT-NAME')
	short_name.text= Port_shortname
	provided_interface_tref=ET.SubElement(p_port_prototype,'PROVIDED-INTERFACE-TREF')
	provided_interface_tref.text=f'/SharedElements/PortInterfaces/SenderReceiver/{referred_IF}'
	provided_interface_tref.attrib={'DEST':'SENDER-RECEIVER-INTERFACE'} 
 
def PPort_CS(Port_shortname, referred_IF): #partially completed
 
	p_port_prototype=ET.SubElement(ports,'P-PORT-PROTOTYPE')
	p_port_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(p_port_prototype,'SHORT-NAME')
	short_name.text= Port_shortname
	provided_interface_tref=ET.SubElement(p_port_prototype,'PROVIDED-INTERFACE-TREF')
	provided_interface_tref.text=f'/SharedElements/PortInterfaces/ClientServer/{referred_IF}'
	provided_interface_tref.attrib={'DEST':'CLIENT-SERVER-INTERFACE'}

def PPort_msi(Port_shortname, referred_IF): #partially completed
 
	p_port_prototype=ET.SubElement(ports,'P-PORT-PROTOTYPE')
	p_port_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(p_port_prototype,'SHORT-NAME')
	short_name.text= Port_shortname
	provided_interface_tref=ET.SubElement(p_port_prototype,'PROVIDED-INTERFACE-TREF')
	provided_interface_tref.text=f'/SharedElements/PortInterfaces/ModeSwitch/{referred_IF}'
	provided_interface_tref.attrib={'DEST':'MODE-SWITCH-INTERFACE'}

def PPort_nvd(Port_shortname, referred_IF): #partially completed

	p_port_prototype=ET.SubElement(ports,'P-PORT-PROTOTYPE')
	p_port_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(p_port_prototype,'SHORT-NAME')
	short_name.text= Port_shortname
	provided_interface_tref=ET.SubElement(p_port_prototype,'PROVIDED-INTERFACE-TREF')
	provided_interface_tref.text=f'/SharedElements/PortInterfaces/NvData/{referred_IF}'
	provided_interface_tref.attrib={'DEST':'NV-DATA-INTERFACE'} 

########## IB ###########

def internal_behaviors(CurrentInternalBehaviors_shortname): #partially completed
    
    global swc_internal_behavior
    internal_behaviors=ET.SubElement(application_sw_component_type,'INTERNAL-BEHAVIORS')
    swc_internal_behavior=ET.SubElement(internal_behaviors,'SWC-INTERNAL-BEHAVIOR')
    swc_internal_behavior.attrib={'UUID':rng.generate_uuid()}
    short_name=ET.SubElement(swc_internal_behavior,'SHORT-NAME')
    short_name.text=CurrentInternalBehaviors_shortname


def ConstantMemory():#completed
	global constant_memorys
	constant_memorys=ET.SubElement(swc_internal_behavior,'CONSTANT-MEMORYS')

def ConstantMemory_PDP(ConstantMemory_shortname, type_tref_adt, Init_val, sw_calibration_access_Enum, sw_impl_policy_Enum): #completed
	a=processor.value_to_str(Init_val)
	parameter_data_prototype=ET.SubElement(constant_memorys,'PARAMETER-DATA-PROTOTYPE')
	parameter_data_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(parameter_data_prototype,'SHORT-NAME')
	short_name.text=ConstantMemory_shortname
	sw_data_def_props=ET.SubElement(parameter_data_prototype,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text=sw_calibration_access_Enum
	sw_impl_policy=ET.SubElement(sw_data_def_props_conditional,'SW-IMPL-POLICY')
	sw_impl_policy.text=sw_impl_policy_Enum
	type_tref=ET.SubElement(parameter_data_prototype,'TYPE-TREF')
	type_tref.text=f'/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/{type_tref_adt}'
	type_tref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}
	init_value=ET.SubElement(parameter_data_prototype,'INIT-VALUE')
	numerical_value_specification=ET.SubElement(init_value,'NUMERICAL-VALUE-SPECIFICATION')
	short_labe=ET.SubElement(numerical_value_specification,'SHORT-LABEL')
	short_labe.text='Value'
	value=ET.SubElement(numerical_value_specification,'VALUE')
	value.text=a

def DataTYPEMAPPINGREFS():#completed
	global data_type_mapping_refs
 
	data_type_mapping_refs=ET.SubElement(swc_internal_behavior,'DATA-TYPE-MAPPING-REFS')

def DataTYPEMAPPINGREF(CurrentSWC_shortname):#completed
 
	data_type_mapping_ref=ET.SubElement(data_type_mapping_refs,'DATA-TYPE-MAPPING-REF')
	data_type_mapping_ref.text=f'/SharedElements/DataTypemappingSets/DTMS_{CurrentSWC_shortname}'
	data_type_mapping_ref.attrib={'DEST':'DATA-TYPE-MAPPING-SET'}

def StaticMemory():#completed
	global static_memorys
	static_memorys=ET.SubElement(swc_internal_behavior,'STATIC-MEMORYS')

def StaticMemory_VDP(StaticMemory_shortname, type_tref_adt, Init_val, sw_calibration_access_Enum, sw_impl_policy_Enum):#completed
	a=processor.value_to_str(Init_val)

	variable_data_prototype=ET.SubElement(static_memorys,'VARIABLE-DATA-PROTOTYPE')
	variable_data_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(variable_data_prototype,'SHORT-NAME')
	short_name.text=StaticMemory_shortname
	sw_data_def_props=ET.SubElement(variable_data_prototype,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text=sw_calibration_access_Enum
	sw_impl_policy=ET.SubElement(sw_data_def_props_conditional,'SW-IMPL-POLICY')
	sw_impl_policy.text=sw_impl_policy_Enum
	type_tref=ET.SubElement(variable_data_prototype,'TYPE-TREF')
	type_tref.text=f'/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/{type_tref_adt}'
	type_tref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}

	init_value=ET.SubElement(variable_data_prototype,'INIT-VALUE')
	numerical_value_specification=ET.SubElement(init_value,'NUMERICAL-VALUE-SPECIFICATION')
	short_labe=ET.SubElement(numerical_value_specification,'SHORT-LABEL')
	short_labe.text='Value'
	value=ET.SubElement(numerical_value_specification,'VALUE')
	value.text=a

	#constant reference need to do something for init value


	# init_value2=ET.SubElement(variable_data_prototype,'INIT-VALUE')
	# constant_reference1=ET.SubElement(init_value2,'CONSTANT-REFERENCE')
	# short_label5=ET.SubElement(constant_reference1,'SHORT-LABEL')
	# short_label5.text='ReferenceToConstant'
	# constant_ref1=ET.SubElement(constant_reference1,'CONSTANT-REF')
	# constant_ref1.text='/SharedElements/ConstantSpecifications/ApplicationSwComponentType_StaticMemory'
	# constant_ref1.attrib={'DEST':'CONSTANT-SPECIFICATION'}

def ArTypedPerInstanceMemory():#completed
	global ar_typed_per_instance_memorys
 
	ar_typed_per_instance_memorys=ET.SubElement(swc_internal_behavior,'AR-TYPED-PER-INSTANCE-MEMORYS')

def ArTypedPerInstanceMemory_VDP(ArTypedPerInstanceMemory_shortname, type_tref_adt, Init_val, sw_calibration_access_Enum, sw_impl_policy_Enum):	#completed
	a=processor.value_to_str(Init_val)
	variable_data_prototype=ET.SubElement(ar_typed_per_instance_memorys,'VARIABLE-DATA-PROTOTYPE')
	variable_data_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(variable_data_prototype,'SHORT-NAME')
	short_name.text=ArTypedPerInstanceMemory_shortname
	sw_data_def_props=ET.SubElement(variable_data_prototype,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text=sw_calibration_access_Enum
	sw_impl_policy=ET.SubElement(sw_data_def_props_conditional,'SW-IMPL-POLICY')
	sw_impl_policy.text=sw_impl_policy_Enum
	type_tref=ET.SubElement(variable_data_prototype,'TYPE-TREF')
	type_tref.text=f'/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/{type_tref_adt}'
	type_tref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}

	init_value=ET.SubElement(variable_data_prototype,'INIT-VALUE')
	numerical_value_specification=ET.SubElement(init_value,'NUMERICAL-VALUE-SPECIFICATION')
	short_labe=ET.SubElement(numerical_value_specification,'SHORT-LABEL')
	short_labe.text='Value'
	value=ET.SubElement(numerical_value_specification,'VALUE')
	value.text=a

def ExplicitInterRunnableVariable():#completed
	global explicit_inter_runnable_variables
 
	explicit_inter_runnable_variables=ET.SubElement(swc_internal_behavior,'EXPLICIT-INTER-RUNNABLE-VARIABLES')

def ExplicitInterRunnableVariable_VDP(ExplicitInterRunnableVariable_shortname, type_tref_adt, Init_val, sw_calibration_access_Enum, sw_impl_policy_Enum):#completed
	a=processor.value_to_str(Init_val)
	variable_data_prototype=ET.SubElement(explicit_inter_runnable_variables,'VARIABLE-DATA-PROTOTYPE')
	variable_data_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(variable_data_prototype,'SHORT-NAME')
	short_name.text=ExplicitInterRunnableVariable_shortname
	sw_data_def_props=ET.SubElement(variable_data_prototype,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text=sw_calibration_access_Enum
	sw_impl_policy=ET.SubElement(sw_data_def_props_conditional,'SW-IMPL-POLICY')
	sw_impl_policy.text= sw_impl_policy_Enum
	type_tref=ET.SubElement(variable_data_prototype,'TYPE-TREF')
	type_tref.text=f'/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/{type_tref_adt}'
	type_tref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}
	
	init_value=ET.SubElement(variable_data_prototype,'INIT-VALUE')
	numerical_value_specification=ET.SubElement(init_value,'NUMERICAL-VALUE-SPECIFICATION')
	short_labe=ET.SubElement(numerical_value_specification,'SHORT-LABEL')
	short_labe.text='Value'
	value=ET.SubElement(numerical_value_specification,'VALUE')
	value.text=a

def handle_termination_and_restart(handle_termination_and_restart_Enum):#completed
 
	handle_termination_and_restart=ET.SubElement(swc_internal_behavior,'HANDLE-TERMINATION-AND-RESTART')
	handle_termination_and_restart.text=handle_termination_and_restart_Enum

def ImplicitInterRunnableVariable():#completed
	global implicit_inter_runnable_variables
 
	implicit_inter_runnable_variables=ET.SubElement(swc_internal_behavior,'IMPLICIT-INTER-RUNNABLE-VARIABLES')

def ImplicitInterRunnableVariable_VDP(implicit_inter_runnable_variable_shortname, type_tref_adt, Init_val, sw_calibration_access_Enum, sw_impl_policy_Enum):#completed
	a=processor.value_to_str(Init_val)
	variable_data_prototype=ET.SubElement(implicit_inter_runnable_variables,'VARIABLE-DATA-PROTOTYPE')
	variable_data_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(variable_data_prototype,'SHORT-NAME')
	short_name.text=implicit_inter_runnable_variable_shortname
	sw_data_def_props=ET.SubElement(variable_data_prototype,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text=sw_calibration_access_Enum
	sw_impl_policy=ET.SubElement(sw_data_def_props_conditional,'SW-IMPL-POLICY')
	sw_impl_policy.text= sw_impl_policy_Enum
	type_tref=ET.SubElement(variable_data_prototype,'TYPE-TREF')
	type_tref.text=f'/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/{type_tref_adt}'
	type_tref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}
	
	init_value=ET.SubElement(variable_data_prototype,'INIT-VALUE')
	numerical_value_specification=ET.SubElement(init_value,'NUMERICAL-VALUE-SPECIFICATION')
	short_labe=ET.SubElement(numerical_value_specification,'SHORT-LABEL')
	short_labe.text='Value'
	value=ET.SubElement(numerical_value_specification,'VALUE')
	value.text=a

def PerInstanceParameter():#completed
	global per_instance_parameters
	per_instance_parameters=ET.SubElement(swc_internal_behavior,'PER-INSTANCE-PARAMETERS')

def PerInstanceParameter_PDP(per_instance_parameters_shortname, type_tref_adt, Init_val, sw_calibration_access_Enum, sw_impl_policy_Enum):#completed

	a=processor.value_to_str(Init_val)
	parameter_data_prototype=ET.SubElement(per_instance_parameters,'PARAMETER-DATA-PROTOTYPE')
	parameter_data_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(parameter_data_prototype,'SHORT-NAME')
	short_name.text=per_instance_parameters_shortname
	sw_data_def_props=ET.SubElement(parameter_data_prototype,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text=sw_calibration_access_Enum
	sw_impl_policy=ET.SubElement(sw_data_def_props_conditional,'SW-IMPL-POLICY')
	sw_impl_policy.text=sw_impl_policy_Enum
	type_tref=ET.SubElement(parameter_data_prototype,'TYPE-TREF')
	type_tref.text=f'/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/{type_tref_adt}'
	type_tref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}
	init_value=ET.SubElement(parameter_data_prototype,'INIT-VALUE')
	numerical_value_specification=ET.SubElement(init_value,'NUMERICAL-VALUE-SPECIFICATION')
	short_labe=ET.SubElement(numerical_value_specification,'SHORT-LABEL')
	short_labe.text='Value'
	value=ET.SubElement(numerical_value_specification,'VALUE')
	value.text=a

def PerInstanceParameter():#completed
	global per_instance_parameters
 
	per_instance_parameters=ET.SubElement(swc_internal_behavior,'PER-INSTANCE-PARAMETERS')

def PerInstanceParameter_PDP(per_instance_parameters_shortname, type_tref_adt, Init_val, sw_calibration_access_Enum, sw_impl_policy_Enum):#completed

	a=processor.value_to_str(Init_val)
	parameter_data_prototype=ET.SubElement(per_instance_parameters,'PARAMETER-DATA-PROTOTYPE')
	parameter_data_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(parameter_data_prototype,'SHORT-NAME')
	short_name.text=per_instance_parameters_shortname
	sw_data_def_props=ET.SubElement(parameter_data_prototype,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text=sw_calibration_access_Enum
	sw_impl_policy=ET.SubElement(sw_data_def_props_conditional,'SW-IMPL-POLICY')
	sw_impl_policy.text=sw_impl_policy_Enum
	type_tref=ET.SubElement(parameter_data_prototype,'TYPE-TREF')
	type_tref.text=f'/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/{type_tref_adt}'
	type_tref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}
	init_value=ET.SubElement(parameter_data_prototype,'INIT-VALUE')
	numerical_value_specification=ET.SubElement(init_value,'NUMERICAL-VALUE-SPECIFICATION')
	short_labe=ET.SubElement(numerical_value_specification,'SHORT-LABEL')
	short_labe.text='Value'
	value=ET.SubElement(numerical_value_specification,'VALUE')
	value.text=a

def SharedParameter(): #completed
    
    global shared_parameters
    shared_parameters=ET.SubElement(swc_internal_behavior,'SHARED-PARAMETERS')

def SharedParameter_PDP(SharedParameter_shortname, type_tref_adt, Init_val, sw_calibration_access_Enum, sw_impl_policy_Enum):#completed
	a=processor.value_to_str(Init_val)
	parameter_data_prototype=ET.SubElement(shared_parameters,'PARAMETER-DATA-PROTOTYPE')
	parameter_data_prototype.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(parameter_data_prototype,'SHORT-NAME')
	short_name.text=SharedParameter_shortname
	sw_data_def_props=ET.SubElement(parameter_data_prototype,'SW-DATA-DEF-PROPS')
	sw_data_def_props_variants=ET.SubElement(sw_data_def_props,'SW-DATA-DEF-PROPS-VARIANTS')
	sw_data_def_props_conditional=ET.SubElement(sw_data_def_props_variants,'SW-DATA-DEF-PROPS-CONDITIONAL')
	sw_calibration_access=ET.SubElement(sw_data_def_props_conditional,'SW-CALIBRATION-ACCESS')
	sw_calibration_access.text=sw_calibration_access_Enum
	sw_impl_policy=ET.SubElement(sw_data_def_props_conditional,'SW-IMPL-POLICY')
	sw_impl_policy.text=sw_impl_policy_Enum
	type_tref=ET.SubElement(parameter_data_prototype,'TYPE-TREF')
	type_tref.text=f'/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/{type_tref_adt}'
	type_tref.attrib={'DEST':'IMPLEMENTATION-DATA-TYPE'}
	init_value=ET.SubElement(parameter_data_prototype,'INIT-VALUE')
	numerical_value_specification=ET.SubElement(init_value,'NUMERICAL-VALUE-SPECIFICATION')
	short_labe=ET.SubElement(numerical_value_specification,'SHORT-LABEL')
	short_labe.text='Value'
	value=ET.SubElement(numerical_value_specification,'VALUE')
	value.text=a

def supports_multiple_instantiation(supports_multiple_instantiation_enum):#completed
    supports_multiple_instantiation=ET.SubElement(swc_internal_behavior,'SUPPORTS-MULTIPLE-INSTANTIATION')
    supports_multiple_instantiation.text=supports_multiple_instantiation_enum

########## RTE Events ###########

def RTE_Event():#completed
	global Rte_events
	Rte_events=ET.SubElement(swc_internal_behavior,'EVENTS')

def AsynchronousServerCallReturnsEvent(RTE_Event_name,Rnbl_shortname,currentfolder, currentswc):#completed 

    asynchronous_server_call_returns_event=ET.SubElement(Rte_events,'ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT')
    asynchronous_server_call_returns_event.attrib={'UUID':rng.generate_uuid()}
    short_name=ET.SubElement(asynchronous_server_call_returns_event,'SHORT-NAME')
    short_name.text=RTE_Event_name
    start_on_event_ref=ET.SubElement(asynchronous_server_call_returns_event,'START-ON-EVENT-REF')
    start_on_event_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}'
    start_on_event_ref.attrib={'DEST':'RUNNABLE-ENTITY'}
    event_source_ref=ET.SubElement(asynchronous_server_call_returns_event,'EVENT-SOURCE-REF')
    event_source_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}/{ASCP_short_name}'
    event_source_ref.attrib={'DEST':'ASYNCHRONOUS-SERVER-CALL-RESULT-POINT'}

def BackgroundEvent(RTE_Event_name,Rnbl_shortname,currentfolder, currentswc):#completed

	background_event=ET.SubElement(Rte_events,'BACKGROUND-EVENT')
	background_event.attrib={'UUID':rng.generate_uuid()} #:'878975ea-f390-4f62-a34f-05ca7fd73896'}
	short_name=ET.SubElement(background_event,'SHORT-NAME')
	short_name.text=RTE_Event_name
	start_on_event_ref=ET.SubElement(background_event,'START-ON-EVENT-REF')
	start_on_event_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}'
	start_on_event_ref.attrib={'DEST':'RUNNABLE-ENTITY'}

def DataReceiveErrorEvent(RTE_Event_name,Rnbl_shortname,currentfolder, currentswc, rport, If_name, DE):#remained

	data_receive_error_event=ET.SubElement(Rte_events,'DATA-RECEIVE-ERROR-EVENT')
	data_receive_error_event.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(data_receive_error_event,'SHORT-NAME')
	short_name.text=RTE_Event_name
	start_on_event_ref=ET.SubElement(data_receive_error_event,'START-ON-EVENT-REF')
	start_on_event_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}' #Runnable2'
	start_on_event_ref.attrib={'DEST':'RUNNABLE-ENTITY'}
	data_iref=ET.SubElement(data_receive_error_event,'DATA-IREF')
	context_r_port_ref=ET.SubElement(data_iref,'CONTEXT-R-PORT-REF')
	context_r_port_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{rport}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
	context_r_port_ref.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_data_element_ref=ET.SubElement(data_iref,'TARGET-DATA-ELEMENT-REF')
	target_data_element_ref.text=f'/SharedElements/PortInterfaces/SenderReceiver/{If_name}/{DE}' #'/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
	target_data_element_ref.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DataReceivedEvent(RTE_Event_name,Rnbl_shortname,currentfolder, currentswc, rport, If_name, DE):#remained
 
	data_received_event=ET.SubElement(Rte_events,'DATA-RECEIVED-EVENT')
	data_received_event.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(data_received_event,'SHORT-NAME')
	short_name.text=RTE_Event_name
	start_on_event_ref=ET.SubElement(data_received_event,'START-ON-EVENT-REF')
	start_on_event_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}' #Runnable3'
	start_on_event_ref.attrib={'DEST':'RUNNABLE-ENTITY'}
	data_iref=ET.SubElement(data_received_event,'DATA-IREF')
	context_r_port_ref=ET.SubElement(data_iref,'CONTEXT-R-PORT-REF')
	context_r_port_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{rport}' #/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
	context_r_port_ref.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_data_element_ref=ET.SubElement(data_iref,'TARGET-DATA-ELEMENT-REF')
	target_data_element_ref.text=f'/SharedElements/PortInterfaces/SenderReceiver/{If_name}/{DE}' #'/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
	target_data_element_ref.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DataSendCompletedEvent(RTE_Event_name,Rnbl_shortname,currentfolder, currentswc, pport, DE):#remained
 
	data_send_completed_event=ET.SubElement(Rte_events,'DATA-SEND-COMPLETED-EVENT')
	data_send_completed_event.attrib={'UUID':rng.generate_uuid()} 
	short_name=ET.SubElement(data_send_completed_event,'SHORT-NAME')
	short_name.text=RTE_Event_name
	start_on_event_ref=ET.SubElement(data_send_completed_event,'START-ON-EVENT-REF')
	start_on_event_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable4'
	start_on_event_ref.attrib={'DEST':'RUNNABLE-ENTITY'}
	event_source_ref=ET.SubElement(data_send_completed_event,'EVENT-SOURCE-REF')
	event_source_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}/DSP_{pport}_{DE}' #/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable4/DSP_PPort_SR_DataElement'
	event_source_ref.attrib={'DEST':'VARIABLE-ACCESS'}

def DataWriteCompletedEvent(RTE_Event_name,Rnbl_shortname,currentfolder, currentswc, pport, DE):#remained
 
	data_write_completed_event=ET.SubElement(Rte_events,'DATA-WRITE-COMPLETED-EVENT')
	data_write_completed_event.attrib={'UUID':rng.generate_uuid()} 
	short_name=ET.SubElement(data_write_completed_event,'SHORT-NAME')
	short_name.text=RTE_Event_name
	start_on_event_ref=ET.SubElement(data_write_completed_event,'START-ON-EVENT-REF')
	start_on_event_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable5'
	start_on_event_ref.attrib={'DEST':'RUNNABLE-ENTITY'}
	event_source_ref=ET.SubElement(data_write_completed_event,'EVENT-SOURCE-REF')
	event_source_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}/DWA_{pport}_{DE}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable5/DWA_PPort_SR_DataElement1'
	event_source_ref.attrib={'DEST':'VARIABLE-ACCESS'}

def ExternalTriggerOccurredEvent(RTE_Event_name,Rnbl_shortname,currentfolder, currentswc, rport, If_name, trigger):#remained
 
	external_trigger_occurred_event=ET.SubElement(Rte_events,'EXTERNAL-TRIGGER-OCCURRED-EVENT')
	external_trigger_occurred_event.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(external_trigger_occurred_event,'SHORT-NAME')
	short_name.text=RTE_Event_name
	start_on_event_ref=ET.SubElement(external_trigger_occurred_event,'START-ON-EVENT-REF')
	start_on_event_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable6'
	start_on_event_ref.attrib={'DEST':'RUNNABLE-ENTITY'}
	trigger_iref=ET.SubElement(external_trigger_occurred_event,'TRIGGER-IREF')
	context_r_port_ref=ET.SubElement(trigger_iref,'CONTEXT-R-PORT-REF')
	context_r_port_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{rport}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_trigger'
	context_r_port_ref.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_trigger_ref=ET.SubElement(trigger_iref,'TARGET-TRIGGER-REF')
	target_trigger_ref.text=f'/SharedElements/PortInterfaces/Trigger/{If_name}/{trigger}' #'/SharedElements/PortInterfaces/Trigger/TriggerInterface/Trigger'
	target_trigger_ref.attrib={'DEST':'TRIGGER'}

#fetch
def InitEvent(): #remained
    init_event = ET.SubElement(events, 'INIT-EVENT')
    init_event.attrib = {'UUID':rng.generate_uuid()} # : '6febdb10-eefc-44b9-adad-fdef91bbef72'
    short_name498 = ET.SubElement(init_event, 'SHORT-NAME')
    short_name498.text = 'InitEvent'
    start_on_event_ref8 = ET.SubElement(init_event, 'START-ON-EVENT-REF')
    start_on_event_ref8.text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable7'
    start_on_event_ref8.attrib = {'DEST': 'RUNNABLE-ENTITY'}


def ModeSwitchedAckEvent(RTE_Event_name,Rnbl_shortname,currentfolder, currentswc, pport, modegroup):#remained
 
	mode_switched_ack_event=ET.SubElement(Rte_events,'MODE-SWITCHED-ACK-EVENT')
	mode_switched_ack_event.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(mode_switched_ack_event,'SHORT-NAME')
	short_name.text=RTE_Event_name
	start_on_event_ref=ET.SubElement(mode_switched_ack_event,'START-ON-EVENT-REF')
	start_on_event_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable9'
	start_on_event_ref.attrib={'DEST':'RUNNABLE-ENTITY'}
	event_source_ref=ET.SubElement(mode_switched_ack_event,'EVENT-SOURCE-REF')
	event_source_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}/MSP_{pport}_{modegroup}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable9/MSP_PPort_msi_ModeGroup'
	event_source_ref.attrib={'DEST':'MODE-SWITCH-POINT'}

def OperationInvokedEvent(RTE_Event_name,Rnbl_shortname,currentfolder, currentswc, pport, If_name, operation):#remained
 
	operation_invoked_event=ET.SubElement(Rte_events,'OPERATION-INVOKED-EVENT')
	operation_invoked_event.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(operation_invoked_event,'SHORT-NAME')
	short_name.text=RTE_Event_name
	start_on_event_ref=ET.SubElement(operation_invoked_event,'START-ON-EVENT-REF')
	start_on_event_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable10'
	start_on_event_ref.attrib={'DEST':'RUNNABLE-ENTITY'}
	operation_iref=ET.SubElement(operation_invoked_event,'OPERATION-IREF')
	context_p_port_ref=ET.SubElement(operation_iref,'CONTEXT-P-PORT-REF')
	context_p_port_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{pport}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_CS'
	context_p_port_ref.attrib={'DEST':'P-PORT-PROTOTYPE'}
	target_provided_operation_ref=ET.SubElement(operation_iref,'TARGET-PROVIDED-OPERATION-REF')
	target_provided_operation_ref.text=f'/SharedElements/PortInterfaces/ClientServer/{If_name}/{operation}' #'/SharedElements/PortInterfaces/ClientServer/ClientServerInterface/Operation1'
	target_provided_operation_ref.attrib={'DEST':'CLIENT-SERVER-OPERATION'}

#fetch
def SwcModeManagerErrorEvent():
    swc_mode_manager_error_event = ET.SubElement(events, 'SWC-MODE-MANAGER-ERROR-EVENT')
    swc_mode_manager_error_event.attrib = {'UUID':rng.generate_uuid()} #: '2e3337be-0df8-4dce-a65a-ca8bb234754a'
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

def SwcModeSwitchEvent(RTE_Event_name,Rnbl_shortname,currentfolder, currentswc, rport, If_name, modegroup, mode):#partially completed
	swc_mode_switch_event=ET.SubElement(Rte_events,'SWC-MODE-SWITCH-EVENT')
	swc_mode_switch_event.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(swc_mode_switch_event,'SHORT-NAME')
	short_name.text=RTE_Event_name
	start_on_event_ref=ET.SubElement(swc_mode_switch_event,'START-ON-EVENT-REF')
	start_on_event_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable12'
	start_on_event_ref.attrib={'DEST':'RUNNABLE-ENTITY'}
	activation=ET.SubElement(swc_mode_switch_event,'ACTIVATION')
	activation.text='ON-TRANSITION' #other erason remaining like 'ON-ENTRY' or 'ON-EXIT'
	mode_irefs=ET.SubElement(swc_mode_switch_event,'MODE-IREFS')
	mode_iref1=ET.SubElement(mode_irefs,'MODE-IREF')
	context_port_ref=ET.SubElement(mode_iref1,'CONTEXT-PORT-REF')
	context_port_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{rport}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_msi'
	context_port_ref.attrib={'DEST':'R-PORT-PROTOTYPE'}
	context_mode_declaration_group_prototype_ref=ET.SubElement(mode_iref1,'CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF')
	context_mode_declaration_group_prototype_ref.text= f'/SharedElements/PortInterfaces/ModeSwitch/{If_name}/{modegroup}' #'/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
	context_mode_declaration_group_prototype_ref.attrib={'DEST':'MODE-DECLARATION-GROUP-PROTOTYPE'}
	target_mode_declaration_ref=ET.SubElement(mode_iref1,'TARGET-MODE-DECLARATION-REF')
	target_mode_declaration_ref.text=f'/SharedElements/PortInterfaces/ModeSwitch/{modegroup}/{mode}' #'/SharedElements/PortInterfaces/ModeSwitch/ModeDeclarationGroup/ModeDeclaration2'
	target_mode_declaration_ref.attrib={'DEST':'MODE-DECLARATION'}
	mode_iref2=ET.SubElement(mode_irefs,'MODE-IREF')
	context_port_ref=ET.SubElement(mode_iref2,'CONTEXT-PORT-REF')
	context_port_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{rport}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_msi'
	context_port_ref.attrib={'DEST':'R-PORT-PROTOTYPE'}
	context_mode_declaration_group_prototype_ref=ET.SubElement(mode_iref2,'CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF')
	context_mode_declaration_group_prototype_ref.text=f'/SharedElements/PortInterfaces/ModeSwitch/{If_name}/{modegroup}' #'/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
	context_mode_declaration_group_prototype_ref.attrib={'DEST':'MODE-DECLARATION-GROUP-PROTOTYPE'}
	target_mode_declaration_ref=ET.SubElement(mode_iref2,'TARGET-MODE-DECLARATION-REF')
	target_mode_declaration_ref.text=f'/SharedElements/PortInterfaces/ModeSwitch/{modegroup}/{mode}' #'/SharedElements/PortInterfaces/ModeSwitch/ModeDeclarationGroup/ModeDeclaration'
	target_mode_declaration_ref.attrib={'DEST':'MODE-DECLARATION'}

def TimingEvent(RTE_Event_name,Rnbl_shortname,currentfolder, currentswc, periodictime):#remained
	a=processor.value_to_str(periodictime)
	timing_event=ET.SubElement(Rte_events,'TIMING-EVENT')
	timing_event.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(timing_event,'SHORT-NAME')
	short_name.text=RTE_Event_name
	start_on_event_ref=ET.SubElement(timing_event,'START-ON-EVENT-REF')
	start_on_event_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable13'
	start_on_event_ref.attrib={'DEST':'RUNNABLE-ENTITY'}
	period=ET.SubElement(timing_event,'PERIOD')
	period.text= a

# def TimingEvent1(RTE_Event_name,Rnbl_shortname,currentfolder, currentswc):#remained
 
# 	timing_event=ET.SubElement(Rte_events,'TIMING-EVENT')
# 	timing_event.attrib={'UUID':rng.generate_uuid()}
# 	short_name=ET.SubElement(timing_event,'SHORT-NAME')
# 	short_name.text=RTE_Event_name
# 	start_on_event_ref=ET.SubElement(timing_event,'START-ON-EVENT-REF')
# 	start_on_event_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}' #'/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable15'
# 	start_on_event_ref.attrib={'DEST':'RUNNABLE-ENTITY'}
# 	period=ET.SubElement(timing_event,'PERIOD')
# 	period.text='0.01'

 
########## Runnable ###########

def create_Runnable():#completed
    
	global runnables
	runnables=ET.SubElement(swc_internal_behavior,'RUNNABLES')

def Runnable_ASCRE(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#completed
	global ASCP_short_name

	runnable_entity=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(runnable_entity,'SHORT-NAME')
	short_name.text=Rnbl_shortname
	minimum_start_interval=ET.SubElement(runnable_entity,'MINIMUM-START-INTERVAL')
	minimum_start_interval.text='0'
	# sw_addr_method_ref=ET.SubElement(runnable_entity,'SW-ADDR-METHOD-REF')
	# sw_addr_method_ref.text=f'/SharedElements/SwAddrMethods/{SwAddrMethod}'
	# sw_addr_method_ref.attrib={'DEST':'SW-ADDR-METHOD'}
	asynchronous_server_call_result_points=ET.SubElement(runnable_entity,'ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS')
	asynchronous_server_call_result_point=ET.SubElement(asynchronous_server_call_result_points,'ASYNCHRONOUS-SERVER-CALL-RESULT-POINT')
	asynchronous_server_call_result_point.attrib={'UUID':rng.generate_uuid()}
	ASCP_short_name=ET.SubElement(asynchronous_server_call_result_point,'SHORT-NAME')
	ASCP_short_name.text='AsynchronousServerCallResultPoint'
	asynchronous_server_call_point_ref=ET.SubElement(asynchronous_server_call_result_point,'ASYNCHRONOUS-SERVER-CALL-POINT-REF')
	asynchronous_server_call_point_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{swc_internal_behavior}/{Rnbl_shortname}/ASCP_{rport}_{operation}'
	# currentfolder = ApplSWC, currentswc = ApplicationSwComponentType
	asynchronous_server_call_point_ref.attrib={'DEST':'ASYNCHRONOUS-SERVER-CALL-POINT'}
	can_be_invoked_concurrently1=ET.SubElement(runnable_entity,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently1.text='false'
	server_call_points=ET.SubElement(runnable_entity,'SERVER-CALL-POINTS')
	asynchronous_server_call_point=ET.SubElement(server_call_points,'ASYNCHRONOUS-SERVER-CALL-POINT')
	asynchronous_server_call_point.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(asynchronous_server_call_point,'SHORT-NAME')
	short_name.text=f'ASCP_{rport}_{operation}'
	operation_iref=ET.SubElement(asynchronous_server_call_point,'OPERATION-IREF')
	context_r_port_ref=ET.SubElement(operation_iref,'CONTEXT-R-PORT-REF')
	context_r_port_ref.text=f'/SwComponentTypes/{currentfolder}/{currentswc}/{rport}'
	context_r_port_ref.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_required_operation_ref=ET.SubElement(operation_iref,'TARGET-REQUIRED-OPERATION-REF')
	target_required_operation_ref.text=f'/SharedElements/PortInterfaces/ClientServer/{If_name}/{operation}'
	target_required_operation_ref.attrib={'DEST':'CLIENT-SERVER-OPERATION'}
	timeout=ET.SubElement(asynchronous_server_call_point,'TIMEOUT')
	timeout.text='0'
	symbol=ET.SubElement(runnable_entity,'SYMBOL')
	symbol.text=Rnbl_symbol


def Runnable_BE(Rnbl_shortname,Rnbl_symbol):#completed

	runnable_entity=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity.attrib={'UUID':rng.generate_uuid()} 
	short_name=ET.SubElement(runnable_entity,'SHORT-NAME')
	short_name.text=Rnbl_shortname
	minimum_start_interval=ET.SubElement(runnable_entity,'MINIMUM-START-INTERVAL')
	minimum_start_interval.text='0'
	can_be_invoked_concurrently=ET.SubElement(runnable_entity,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently.text='false'
	symbol=ET.SubElement(runnable_entity,'SYMBOL')
	symbol.text=Rnbl_symbol
 
def Runnable2(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#completed
 
	runnable_entity3=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity3.attrib={'UUID':rng.generate_uuid()} #:'83eca00a-85d5-4f04-9573-3d997cd29b67'}
	short_name164=ET.SubElement(runnable_entity3,'SHORT-NAME')
	short_name164.text=Rnbl_shortname
	minimum_start_interval3=ET.SubElement(runnable_entity3,'MINIMUM-START-INTERVAL')
	minimum_start_interval3.text='0'
	can_be_invoked_concurrently3=ET.SubElement(runnable_entity3,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently3.text='false'
	symbol3=ET.SubElement(runnable_entity3,'SYMBOL')
	symbol3.text=Rnbl_symbol

def Runnable3(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#remained
 
	runnable_entity4=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity4.attrib={'UUID':rng.generate_uuid()} #:'20bfd5e2-a118-4324-97fd-dcd5bf5f0a46'}
	short_name165=ET.SubElement(runnable_entity4,'SHORT-NAME')
	short_name165.text=Rnbl_shortname
	minimum_start_interval4=ET.SubElement(runnable_entity4,'MINIMUM-START-INTERVAL')
	minimum_start_interval4.text='0'
	can_be_invoked_concurrently4=ET.SubElement(runnable_entity4,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently4.text='false'
	symbol4=ET.SubElement(runnable_entity4,'SYMBOL')
	symbol4.text=Rnbl_symbol

def Runnable4(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#remained
 
	runnable_entity5=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity5.attrib={'UUID':rng.generate_uuid()} #:'ae315d13-a18a-4515-b02d-f1b207f85e47'}
	short_name166=ET.SubElement(runnable_entity5,'SHORT-NAME')
	short_name166.text=Rnbl_shortname
	minimum_start_interval5=ET.SubElement(runnable_entity5,'MINIMUM-START-INTERVAL')
	minimum_start_interval5.text='0'
	can_be_invoked_concurrently5=ET.SubElement(runnable_entity5,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently5.text='false'
	data_send_points1=ET.SubElement(runnable_entity5,'DATA-SEND-POINTS')
	variable_access1=ET.SubElement(data_send_points1,'VARIABLE-ACCESS')
	variable_access1.attrib={'UUID':rng.generate_uuid()} #:'2a04aecc-a1b6-494f-838e-29671adb5210'}
	short_name167=ET.SubElement(variable_access1,'SHORT-NAME')
	short_name167.text='DSP_PPort_SR_DataElement'
	accessed_variable1=ET.SubElement(variable_access1,'ACCESSED-VARIABLE')
	autosar_variable_iref1=ET.SubElement(accessed_variable1,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref1=ET.SubElement(autosar_variable_iref1,'PORT-PROTOTYPE-REF')
	port_prototype_ref1.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
	port_prototype_ref1.attrib={'DEST':'P-PORT-PROTOTYPE'}
	target_data_prototype_ref1=ET.SubElement(autosar_variable_iref1,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref1.text='/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
	target_data_prototype_ref1.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}
	symbol5=ET.SubElement(runnable_entity5,'SYMBOL')
	symbol5.text=Rnbl_symbol

def Runnable5(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#remained

	runnable_entity6=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity6.attrib={'UUID':rng.generate_uuid()} #:'3ea0641c-9d79-4f93-8287-e34956b5c134'}
	short_name168=ET.SubElement(runnable_entity6,'SHORT-NAME')
	short_name168.text=Rnbl_shortname
	minimum_start_interval6=ET.SubElement(runnable_entity6,'MINIMUM-START-INTERVAL')
	minimum_start_interval6.text='0'
	can_be_invoked_concurrently6=ET.SubElement(runnable_entity6,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently6.text='false'
	data_write_accesss1=ET.SubElement(runnable_entity6,'DATA-WRITE-ACCESSS')
	variable_access2=ET.SubElement(data_write_accesss1,'VARIABLE-ACCESS')
	variable_access2.attrib={'UUID':rng.generate_uuid()} #:'326a474d-8d28-41bc-bd9e-91de9802f682'}
	short_name169=ET.SubElement(variable_access2,'SHORT-NAME')
	short_name169.text='DWA_PPort_SR_DataElement1'
	accessed_variable2=ET.SubElement(variable_access2,'ACCESSED-VARIABLE')
	autosar_variable_iref2=ET.SubElement(accessed_variable2,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref2=ET.SubElement(autosar_variable_iref2,'PORT-PROTOTYPE-REF')
	port_prototype_ref2.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
	port_prototype_ref2.attrib={'DEST':'P-PORT-PROTOTYPE'}
	target_data_prototype_ref2=ET.SubElement(autosar_variable_iref2,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref2.text='/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
	target_data_prototype_ref2.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}
	symbol6=ET.SubElement(runnable_entity6,'SYMBOL')
	symbol6.text=Rnbl_symbol

def Runnable6(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#remained
 
	runnable_entity7=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity7.attrib={'UUID':rng.generate_uuid()} #:'d7adad0b-22d1-4b37-9691-0677036197aa'}
	short_name170=ET.SubElement(runnable_entity7,'SHORT-NAME')
	short_name170.text=Rnbl_shortname
	minimum_start_interval7=ET.SubElement(runnable_entity7,'MINIMUM-START-INTERVAL')
	minimum_start_interval7.text='0'
	can_be_invoked_concurrently7=ET.SubElement(runnable_entity7,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently7.text='false'
	symbol7=ET.SubElement(runnable_entity7,'SYMBOL')
	symbol7.text=Rnbl_symbol

def Runnable7(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#remained
 
	runnable_entity8=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity8.attrib={'UUID':rng.generate_uuid()} #:'98d30ebd-bbcb-4780-bc4a-27e6fd798a5a'}
	short_name171=ET.SubElement(runnable_entity8,'SHORT-NAME')
	short_name171.text=Rnbl_shortname
	minimum_start_interval8=ET.SubElement(runnable_entity8,'MINIMUM-START-INTERVAL')
	minimum_start_interval8.text='0'
	can_be_invoked_concurrently8=ET.SubElement(runnable_entity8,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently8.text='false'
	symbol8=ET.SubElement(runnable_entity8,'SYMBOL')
	symbol8.text=Rnbl_symbol

def Runnable9(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#remained
 
	runnable_entity9=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity9.attrib={'UUID':rng.generate_uuid()} #:'a6d9d7cb-1d57-45f2-b36a-1e1ab717fb1e'}
	short_name172=ET.SubElement(runnable_entity9,'SHORT-NAME')
	short_name172.text=Rnbl_shortname
	minimum_start_interval9=ET.SubElement(runnable_entity9,'MINIMUM-START-INTERVAL')
	minimum_start_interval9.text='0'
	can_be_invoked_concurrently9=ET.SubElement(runnable_entity9,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently9.text='false'
	mode_switch_points1=ET.SubElement(runnable_entity9,'MODE-SWITCH-POINTS')
	mode_switch_point1=ET.SubElement(mode_switch_points1,'MODE-SWITCH-POINT')
	mode_switch_point1.attrib={'UUID':rng.generate_uuid()} #:'dd700e44-3e29-4b21-901f-c2e36c719f6a'}
	short_name173=ET.SubElement(mode_switch_point1,'SHORT-NAME')
	short_name173.text='MSP_PPort_msi_ModeGroup'
	mode_group_iref1=ET.SubElement(mode_switch_point1,'MODE-GROUP-IREF')
	context_p_port_ref2=ET.SubElement(mode_group_iref1,'CONTEXT-P-PORT-REF')
	context_p_port_ref2.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_msi'
	context_p_port_ref2.attrib={'DEST':'P-PORT-PROTOTYPE'}
	target_mode_group_ref1=ET.SubElement(mode_group_iref1,'TARGET-MODE-GROUP-REF')
	target_mode_group_ref1.text='/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
	target_mode_group_ref1.attrib={'DEST':'MODE-DECLARATION-GROUP-PROTOTYPE'}
	symbol9=ET.SubElement(runnable_entity9,'SYMBOL')
	symbol9.text=Rnbl_symbol

def Runnable10(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#remained

	runnable_entity10=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity10.attrib={'UUID':rng.generate_uuid()} #:'3d515ac9-9c51-4cb8-a6af-ea16d3afd01d'}
	short_name174=ET.SubElement(runnable_entity10,'SHORT-NAME')
	short_name174.text=Rnbl_shortname
	minimum_start_interval10=ET.SubElement(runnable_entity10,'MINIMUM-START-INTERVAL')
	minimum_start_interval10.text='0'
	can_be_invoked_concurrently10=ET.SubElement(runnable_entity10,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently10.text='false'
	symbol10=ET.SubElement(runnable_entity10,'SYMBOL')
	symbol10.text=Rnbl_symbol

def Runnable11(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#remained
 
	runnable_entity11=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity11.attrib={'UUID':rng.generate_uuid()} #:'9bddd887-575d-463b-b09d-d1b63ec1352b'}
	short_name175=ET.SubElement(runnable_entity11,'SHORT-NAME')
	short_name175.text=Rnbl_shortname
	minimum_start_interval11=ET.SubElement(runnable_entity11,'MINIMUM-START-INTERVAL')
	minimum_start_interval11.text='0'
	can_be_invoked_concurrently11=ET.SubElement(runnable_entity11,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently11.text='false'
	symbol11=ET.SubElement(runnable_entity11,'SYMBOL')
	symbol11.text=Rnbl_symbol

def Runnable12(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol): #remained
 
	runnable_entity12=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity12.attrib={'UUID':rng.generate_uuid()} #:'fa96688f-7ffe-4b3b-aa43-c124847e2efd'}
	short_name176=ET.SubElement(runnable_entity12,'SHORT-NAME')
	short_name176.text=Rnbl_shortname
	minimum_start_interval12=ET.SubElement(runnable_entity12,'MINIMUM-START-INTERVAL')
	minimum_start_interval12.text='0'
	can_be_invoked_concurrently12=ET.SubElement(runnable_entity12,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently12.text='false'
	symbol12=ET.SubElement(runnable_entity12,'SYMBOL')
	symbol12.text=Rnbl_symbol


def Runnable13(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#remained
    
	global runnable_entity13
	runnable_entity13=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity13.attrib={'UUID':rng.generate_uuid()} #:'e967670f-46d8-4d91-b4b9-62c85a17843e'}
	short_name177=ET.SubElement(runnable_entity13,'SHORT-NAME')
	short_name177.text='Runnable13'
	minimum_start_interval13=ET.SubElement(runnable_entity13,'MINIMUM-START-INTERVAL')
	minimum_start_interval13.text='0'
	can_be_invoked_concurrently13=ET.SubElement(runnable_entity13,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently13.text='false'
	symbol13=ET.SubElement(runnable_entity13,'SYMBOL')
	symbol13.text=Rnbl_symbol

def Runnable14(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#remained
    
    runnable_entity14=ET.SubElement(runnables,'RUNNABLE-ENTITY')
    runnable_entity14.attrib={'UUID':rng.generate_uuid()} #:'1c2e8cb0-fdf5-45ee-9257-dee6f42d2ad4'}
    short_name188=ET.SubElement(runnable_entity14,'SHORT-NAME')
    short_name188.text=Rnbl_shortname
    minimum_start_interval14=ET.SubElement(runnable_entity14,'MINIMUM-START-INTERVAL')
    minimum_start_interval14.text='0'
    can_be_invoked_concurrently14=ET.SubElement(runnable_entity14,'CAN-BE-INVOKED-CONCURRENTLY')
    can_be_invoked_concurrently14.text='false'
    symbol14=ET.SubElement(runnable_entity14,'SYMBOL')
    symbol14.text=Rnbl_symbol



 
def Runnable15(Rnbl_shortname,currentfolder, currentswc, rport, If_name, operation, Rnbl_symbol):#remained
    
	global runnable_entity15
	runnable_entity15=ET.SubElement(runnables,'RUNNABLE-ENTITY')
	runnable_entity15.attrib={'UUID':rng.generate_uuid()} #:'6debf2b3-9c4c-455e-9cbc-0c7cfaca4d43'}
	short_name189=ET.SubElement(runnable_entity15,'SHORT-NAME')
	short_name189.text=Rnbl_shortname
	minimum_start_interval15=ET.SubElement(runnable_entity15,'MINIMUM-START-INTERVAL')
	minimum_start_interval15.text='0'
	can_be_invoked_concurrently15=ET.SubElement(runnable_entity15,'CAN-BE-INVOKED-CONCURRENTLY')
	can_be_invoked_concurrently15.text='false'
	symbol15=ET.SubElement(runnable_entity15,'SYMBOL')
	symbol15.text=Rnbl_symbol

########## Runnable access ###########

def DRA_RPort_SR_DataElement():#remained
    
    global data_read_accesss1
    data_read_accesss1=ET.SubElement(runnable_entity13,'DATA-READ-ACCESSS')
    variable_access3=ET.SubElement(data_read_accesss1,'VARIABLE-ACCESS')
    variable_access3.attrib={'UUID':rng.generate_uuid()} #:'9bf42611-5276-4ce4-92b5-36c024121479'}
    short_name178=ET.SubElement(variable_access3,'SHORT-NAME')
    short_name178.text='DRA_RPort_SR_DataElement'
    accessed_variable3=ET.SubElement(variable_access3,'ACCESSED-VARIABLE')
    autosar_variable_iref3=ET.SubElement(accessed_variable3,'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref3=ET.SubElement(autosar_variable_iref3,'PORT-PROTOTYPE-REF')
    port_prototype_ref3.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    port_prototype_ref3.attrib={'DEST':'R-PORT-PROTOTYPE'}
    target_data_prototype_ref3=ET.SubElement(autosar_variable_iref3,'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref3.text='/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    target_data_prototype_ref3.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DRA_RPort_SR_DataElement1():#remained
 
	variable_access4=ET.SubElement(data_read_accesss1,'VARIABLE-ACCESS')
	variable_access4.attrib={'UUID':rng.generate_uuid()} #:'9eef2638-b3d9-47c1-9e18-37822b089dd4'}
	short_name179=ET.SubElement(variable_access4,'SHORT-NAME')
	short_name179.text='DRA_RPort_SR_DataElement1'
	accessed_variable4=ET.SubElement(variable_access4,'ACCESSED-VARIABLE')
	autosar_variable_iref4=ET.SubElement(accessed_variable4,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref4=ET.SubElement(autosar_variable_iref4,'PORT-PROTOTYPE-REF')
	port_prototype_ref4.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
	port_prototype_ref4.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_data_prototype_ref4=ET.SubElement(autosar_variable_iref4,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref4.text='/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
	target_data_prototype_ref4.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DRA_RPort_nvd_NvData():#remained
 
	variable_access5=ET.SubElement(data_read_accesss1,'VARIABLE-ACCESS')
	variable_access5.attrib={'UUID':rng.generate_uuid()} #:'26ad84a0-bc71-4cae-92f7-69d3d1bc91ff'}
	short_name180=ET.SubElement(variable_access5,'SHORT-NAME')
	short_name180.text='DRA_RPort_nvd_NvData'
	accessed_variable5=ET.SubElement(variable_access5,'ACCESSED-VARIABLE')
	autosar_variable_iref5=ET.SubElement(accessed_variable5,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref5=ET.SubElement(autosar_variable_iref5,'PORT-PROTOTYPE-REF')
	port_prototype_ref5.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
	port_prototype_ref5.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_data_prototype_ref5=ET.SubElement(autosar_variable_iref5,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref5.text='/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
	target_data_prototype_ref5.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DRA_RPort_nvd_NvData1():#remained
 
	variable_access6=ET.SubElement(data_read_accesss1,'VARIABLE-ACCESS')
	variable_access6.attrib={'UUID':rng.generate_uuid()} #:'067aa426-f94d-4f7c-b471-a3631398a8a6'}
	short_name181=ET.SubElement(variable_access6,'SHORT-NAME')
	short_name181.text='DRA_RPort_nvd_NvData1'
	accessed_variable6=ET.SubElement(variable_access6,'ACCESSED-VARIABLE')
	autosar_variable_iref6=ET.SubElement(accessed_variable6,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref6=ET.SubElement(autosar_variable_iref6,'PORT-PROTOTYPE-REF')
	port_prototype_ref6.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
	port_prototype_ref6.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_data_prototype_ref6=ET.SubElement(autosar_variable_iref6,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref6.text='/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
	target_data_prototype_ref6.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DWA_PPort_SR_DataElement():#remained
    
    global data_write_accesss2
    data_write_accesss2=ET.SubElement(runnable_entity13,'DATA-WRITE-ACCESSS')
    variable_access7=ET.SubElement(data_write_accesss2,'VARIABLE-ACCESS')
    variable_access7.attrib={'UUID':rng.generate_uuid()} #:'a0b4f337-7b3c-4ade-bc28-db75b0882305'}
    short_name182=ET.SubElement(variable_access7,'SHORT-NAME')
    short_name182.text='DWA_PPort_SR_DataElement'
    accessed_variable7=ET.SubElement(variable_access7,'ACCESSED-VARIABLE')
    autosar_variable_iref7=ET.SubElement(accessed_variable7,'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref7=ET.SubElement(autosar_variable_iref7,'PORT-PROTOTYPE-REF')
    port_prototype_ref7.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    port_prototype_ref7.attrib={'DEST':'P-PORT-PROTOTYPE'}
    target_data_prototype_ref7=ET.SubElement(autosar_variable_iref7,'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref7.text='/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    target_data_prototype_ref7.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DWA_PPort_SR_DataElement1():#remained 
 
	variable_access8=ET.SubElement(data_write_accesss2,'VARIABLE-ACCESS')
	variable_access8.attrib={'UUID':rng.generate_uuid()} #:'839b63ac-ec02-4b70-aca8-f974d2ab728c'}
	short_name183=ET.SubElement(variable_access8,'SHORT-NAME')
	short_name183.text='DWA_PPort_SR_DataElement1'
	accessed_variable8=ET.SubElement(variable_access8,'ACCESSED-VARIABLE')
	autosar_variable_iref8=ET.SubElement(accessed_variable8,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref8=ET.SubElement(autosar_variable_iref8,'PORT-PROTOTYPE-REF')
	port_prototype_ref8.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
	port_prototype_ref8.attrib={'DEST':'P-PORT-PROTOTYPE'}
	target_data_prototype_ref8=ET.SubElement(autosar_variable_iref8,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref8.text='/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
	target_data_prototype_ref8.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DWA_PPort_nvd_NvData():#remained 
 
	variable_access9=ET.SubElement(data_write_accesss2,'VARIABLE-ACCESS')
	variable_access9.attrib={'UUID':rng.generate_uuid()} #:'b68d4be0-8b3f-4259-9c8a-2901c17454d7'}
	short_name184=ET.SubElement(variable_access9,'SHORT-NAME')
	short_name184.text='DWA_PPort_nvd_NvData'
	accessed_variable9=ET.SubElement(variable_access9,'ACCESSED-VARIABLE')
	autosar_variable_iref9=ET.SubElement(accessed_variable9,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref9=ET.SubElement(autosar_variable_iref9,'PORT-PROTOTYPE-REF')
	port_prototype_ref9.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
	port_prototype_ref9.attrib={'DEST':'P-PORT-PROTOTYPE'}
	target_data_prototype_ref9=ET.SubElement(autosar_variable_iref9,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref9.text='/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
	target_data_prototype_ref9.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DWA_PPort_nvd_NvData1():#remained
 
	variable_access10=ET.SubElement(data_write_accesss2,'VARIABLE-ACCESS')
	variable_access10.attrib={'UUID':rng.generate_uuid()} #:'3e84de24-a491-4152-b344-8c5e44e9197e'}
	short_name185=ET.SubElement(variable_access10,'SHORT-NAME')
	short_name185.text='DWA_PPort_nvd_NvData1'
	accessed_variable10=ET.SubElement(variable_access10,'ACCESSED-VARIABLE')
	autosar_variable_iref10=ET.SubElement(accessed_variable10,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref10=ET.SubElement(autosar_variable_iref10,'PORT-PROTOTYPE-REF')
	port_prototype_ref10.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
	port_prototype_ref10.attrib={'DEST':'P-PORT-PROTOTYPE'}
	target_data_prototype_ref10=ET.SubElement(autosar_variable_iref10,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref10.text='/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
	target_data_prototype_ref10.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def IRVRA_ExplicitInterRunnableVariable():#remained
    
    global read_local_variables1
    read_local_variables1=ET.SubElement(runnable_entity13,'READ-LOCAL-VARIABLES')
    variable_access11=ET.SubElement(read_local_variables1,'VARIABLE-ACCESS')
    variable_access11.attrib={'UUID':rng.generate_uuid()} #:'c8972fdb-f78a-4e12-9a30-4faf0daa6c23'}
    short_name186=ET.SubElement(variable_access11,'SHORT-NAME')
    short_name186.text='IRVRA_ExplicitInterRunnableVariable'
    accessed_variable11=ET.SubElement(variable_access11,'ACCESSED-VARIABLE')
    local_variable_ref1=ET.SubElement(accessed_variable11,'LOCAL-VARIABLE-REF')
    local_variable_ref1.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ExplicitInterRunnableVariable'
    local_variable_ref1.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def IRVRA_ImplicitInterRunnableVariable():#remained 
 
	variable_access12=ET.SubElement(read_local_variables1,'VARIABLE-ACCESS')
	variable_access12.attrib={'UUID':rng.generate_uuid()} #:'bf16d1d1-6833-4572-8830-6e31aa069454'}
	short_name187=ET.SubElement(variable_access12,'SHORT-NAME')
	short_name187.text='IRVRA_ImplicitInterRunnableVariable'
	accessed_variable12=ET.SubElement(variable_access12,'ACCESSED-VARIABLE')
	local_variable_ref2=ET.SubElement(accessed_variable12,'LOCAL-VARIABLE-REF')
	local_variable_ref2.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ImplicitInterRunnableVariable'
	local_variable_ref2.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DRA_RPort_nvd_NvData_():#remained
     
    global data_read_accesss2
    data_read_accesss2=ET.SubElement(runnable_entity15,'DATA-READ-ACCESSS')
    variable_access13=ET.SubElement(data_read_accesss2,'VARIABLE-ACCESS')
    variable_access13.attrib={'UUID':rng.generate_uuid()} #:'5648b05b-23f8-4729-9fdd-25a617e2d17b'}
    short_name190=ET.SubElement(variable_access13,'SHORT-NAME')
    short_name190.text='DRA_RPort_nvd_NvData'
    accessed_variable13=ET.SubElement(variable_access13,'ACCESSED-VARIABLE')
    autosar_variable_iref11=ET.SubElement(accessed_variable13,'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref11=ET.SubElement(autosar_variable_iref11,'PORT-PROTOTYPE-REF')
    port_prototype_ref11.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    port_prototype_ref11.attrib={'DEST':'R-PORT-PROTOTYPE'}
    target_data_prototype_ref11=ET.SubElement(autosar_variable_iref11,'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref11.text='/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    target_data_prototype_ref11.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DRA_RPort_nvd_NvData1_():#remained
 
	variable_access14=ET.SubElement(data_read_accesss2,'VARIABLE-ACCESS')
	variable_access14.attrib={'UUID':rng.generate_uuid()} #:'b355b0ac-1fa9-43f7-b5ab-240eae2c3694'}
	short_name191=ET.SubElement(variable_access14,'SHORT-NAME')
	short_name191.text='DRA_RPort_nvd_NvData1'
	accessed_variable14=ET.SubElement(variable_access14,'ACCESSED-VARIABLE')
	autosar_variable_iref12=ET.SubElement(accessed_variable14,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref12=ET.SubElement(autosar_variable_iref12,'PORT-PROTOTYPE-REF')
	port_prototype_ref12.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
	port_prototype_ref12.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_data_prototype_ref12=ET.SubElement(autosar_variable_iref12,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref12.text='/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
	target_data_prototype_ref12.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DRP_RPort_SR_DataElement():#remained
    
    global data_receive_point_by_arguments1
    data_receive_point_by_arguments1=ET.SubElement(runnable_entity15,'DATA-RECEIVE-POINT-BY-ARGUMENTS')
    variable_access15=ET.SubElement(data_receive_point_by_arguments1,'VARIABLE-ACCESS')
    variable_access15.attrib={'UUID':rng.generate_uuid()} #:'86796258-06a6-480e-8a39-e01411743a56'}
    short_name192=ET.SubElement(variable_access15,'SHORT-NAME')
    short_name192.text='DRP_RPort_SR_DataElement'
    accessed_variable15=ET.SubElement(variable_access15,'ACCESSED-VARIABLE')
    autosar_variable_iref13=ET.SubElement(accessed_variable15,'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref13=ET.SubElement(autosar_variable_iref13,'PORT-PROTOTYPE-REF')
    port_prototype_ref13.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    port_prototype_ref13.attrib={'DEST':'R-PORT-PROTOTYPE'}
    target_data_prototype_ref13=ET.SubElement(autosar_variable_iref13,'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref13.text='/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    target_data_prototype_ref13.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DRP_RPort_nvd_NvData():#remained 
 
	variable_access16=ET.SubElement(data_receive_point_by_arguments1,'VARIABLE-ACCESS')
	variable_access16.attrib={'UUID':rng.generate_uuid()} #:'88c27605-b9a2-4db7-af10-2a0953c5110b'}
	short_name193=ET.SubElement(variable_access16,'SHORT-NAME')
	short_name193.text='DRP_RPort_nvd_NvData'
	accessed_variable16=ET.SubElement(variable_access16,'ACCESSED-VARIABLE')
	autosar_variable_iref14=ET.SubElement(accessed_variable16,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref14=ET.SubElement(autosar_variable_iref14,'PORT-PROTOTYPE-REF')
	port_prototype_ref14.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
	port_prototype_ref14.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_data_prototype_ref14=ET.SubElement(autosar_variable_iref14,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref14.text='/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
	target_data_prototype_ref14.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DRP_RPort_nvd_NvData1():#remained 

	variable_access17=ET.SubElement(data_receive_point_by_arguments1,'VARIABLE-ACCESS')
	variable_access17.attrib={'UUID':rng.generate_uuid()} #:'b69ad602-c226-42a5-9bbb-acbbc5c16743'}
	short_name194=ET.SubElement(variable_access17,'SHORT-NAME')
	short_name194.text='DRP_RPort_nvd_NvData1'
	accessed_variable17=ET.SubElement(variable_access17,'ACCESSED-VARIABLE')
	autosar_variable_iref15=ET.SubElement(accessed_variable17,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref15=ET.SubElement(autosar_variable_iref15,'PORT-PROTOTYPE-REF')
	port_prototype_ref15.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
	port_prototype_ref15.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_data_prototype_ref15=ET.SubElement(autosar_variable_iref15,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref15.text='/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
	target_data_prototype_ref15.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DRPV_RPort_SR_DataElement1():#remained
    
    global data_receive_point_by_values1
    data_receive_point_by_values1=ET.SubElement(runnable_entity15,'DATA-RECEIVE-POINT-BY-VALUES')
    variable_access18=ET.SubElement(data_receive_point_by_values1,'VARIABLE-ACCESS')
    variable_access18.attrib={'UUID':rng.generate_uuid()} #:'38ed8447-65f1-48a9-b075-fa613c1267d2'}
    short_name195=ET.SubElement(variable_access18,'SHORT-NAME')
    short_name195.text='DRPV_RPort_SR_DataElement1'
    accessed_variable18=ET.SubElement(variable_access18,'ACCESSED-VARIABLE')
    autosar_variable_iref16=ET.SubElement(accessed_variable18,'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref16=ET.SubElement(autosar_variable_iref16,'PORT-PROTOTYPE-REF')
    port_prototype_ref16.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    port_prototype_ref16.attrib={'DEST':'R-PORT-PROTOTYPE'}
    target_data_prototype_ref16=ET.SubElement(autosar_variable_iref16,'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref16.text='/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    target_data_prototype_ref16.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DRPV_RPort_nvd_NvData():#remained
 
	variable_access19=ET.SubElement(data_receive_point_by_values1,'VARIABLE-ACCESS')
	variable_access19.attrib={'UUID':rng.generate_uuid()} #:'d07d7e6b-0d9c-4475-bbb9-2ccfc3e60c33'}
	short_name196=ET.SubElement(variable_access19,'SHORT-NAME')
	short_name196.text='DRPV_RPort_nvd_NvData'
	accessed_variable19=ET.SubElement(variable_access19,'ACCESSED-VARIABLE')
	autosar_variable_iref17=ET.SubElement(accessed_variable19,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref17=ET.SubElement(autosar_variable_iref17,'PORT-PROTOTYPE-REF')
	port_prototype_ref17.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
	port_prototype_ref17.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_data_prototype_ref17=ET.SubElement(autosar_variable_iref17,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref17.text='/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
	target_data_prototype_ref17.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DSP_PPort_SR_DataElement():#remained 
    
    global data_send_points2
    data_send_points2=ET.SubElement(runnable_entity15,'DATA-SEND-POINTS')
    variable_access20=ET.SubElement(data_send_points2,'VARIABLE-ACCESS')
    variable_access20.attrib={'UUID':rng.generate_uuid()} #:'2fc872c8-d598-4d11-8502-1a70e9104bc9'}
    short_name197=ET.SubElement(variable_access20,'SHORT-NAME')
    short_name197.text='DSP_PPort_SR_DataElement'
    accessed_variable20=ET.SubElement(variable_access20,'ACCESSED-VARIABLE')
    autosar_variable_iref18=ET.SubElement(accessed_variable20,'AUTOSAR-VARIABLE-IREF')
    port_prototype_ref18=ET.SubElement(autosar_variable_iref18,'PORT-PROTOTYPE-REF')
    port_prototype_ref18.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    port_prototype_ref18.attrib={'DEST':'P-PORT-PROTOTYPE'}
    target_data_prototype_ref18=ET.SubElement(autosar_variable_iref18,'TARGET-DATA-PROTOTYPE-REF')
    target_data_prototype_ref18.text='/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    target_data_prototype_ref18.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DSP_PPort_SR_DataElement1():#remained
 
	variable_access21=ET.SubElement(data_send_points2,'VARIABLE-ACCESS')
	variable_access21.attrib={'UUID':rng.generate_uuid()} #:'a2f22836-4cd0-4c2e-8040-1abdf8935ac0'}
	short_name198=ET.SubElement(variable_access21,'SHORT-NAME')
	short_name198.text='DSP_PPort_SR_DataElement1'
	accessed_variable21=ET.SubElement(variable_access21,'ACCESSED-VARIABLE')
	autosar_variable_iref19=ET.SubElement(accessed_variable21,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref19=ET.SubElement(autosar_variable_iref19,'PORT-PROTOTYPE-REF')
	port_prototype_ref19.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
	port_prototype_ref19.attrib={'DEST':'P-PORT-PROTOTYPE'}
	target_data_prototype_ref19=ET.SubElement(autosar_variable_iref19,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref19.text='/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
	target_data_prototype_ref19.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DSP_PPort_nvd_NvData():#remained 
 
	variable_access22=ET.SubElement(data_send_points2,'VARIABLE-ACCESS')
	variable_access22.attrib={'UUID':rng.generate_uuid()} #:'c0c41eb1-b5bf-4e30-9569-24d7316b64c8'}
	short_name199=ET.SubElement(variable_access22,'SHORT-NAME')
	short_name199.text='DSP_PPort_nvd_NvData'
	accessed_variable22=ET.SubElement(variable_access22,'ACCESSED-VARIABLE')
	autosar_variable_iref20=ET.SubElement(accessed_variable22,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref20=ET.SubElement(autosar_variable_iref20,'PORT-PROTOTYPE-REF')
	port_prototype_ref20.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
	port_prototype_ref20.attrib={'DEST':'P-PORT-PROTOTYPE'}
	target_data_prototype_ref20=ET.SubElement(autosar_variable_iref20,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref20.text='/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
	target_data_prototype_ref20.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DSP_PPort_nvd_NvData1():#remained
 
	variable_access23=ET.SubElement(data_send_points2,'VARIABLE-ACCESS')
	variable_access23.attrib={'UUID':rng.generate_uuid()} #:'96f66382-5f86-4a47-bd5b-9f95f81fc3c9'}
	short_name200=ET.SubElement(variable_access23,'SHORT-NAME')
	short_name200.text='DSP_PPort_nvd_NvData1'
	accessed_variable23=ET.SubElement(variable_access23,'ACCESSED-VARIABLE')
	autosar_variable_iref21=ET.SubElement(accessed_variable23,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref21=ET.SubElement(autosar_variable_iref21,'PORT-PROTOTYPE-REF')
	port_prototype_ref21.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
	port_prototype_ref21.attrib={'DEST':'P-PORT-PROTOTYPE'}
	target_data_prototype_ref21=ET.SubElement(autosar_variable_iref21,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref21.text='/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
	target_data_prototype_ref21.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def DWA_PPort_SR_DataElement1_():#remained 

	data_write_accesss3=ET.SubElement(runnable_entity15,'DATA-WRITE-ACCESSS')
	variable_access24=ET.SubElement(data_write_accesss3,'VARIABLE-ACCESS')
	variable_access24.attrib={'UUID':rng.generate_uuid()} #:'d40a6e94-d8e5-48e5-8a1a-c7debe02592f'}
	short_name201=ET.SubElement(variable_access24,'SHORT-NAME')
	short_name201.text='DWA_PPort_SR_DataElement1'
	accessed_variable24=ET.SubElement(variable_access24,'ACCESSED-VARIABLE')
	autosar_variable_iref22=ET.SubElement(accessed_variable24,'AUTOSAR-VARIABLE-IREF')
	port_prototype_ref22=ET.SubElement(autosar_variable_iref22,'PORT-PROTOTYPE-REF')
	port_prototype_ref22.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
	port_prototype_ref22.attrib={'DEST':'P-PORT-PROTOTYPE'}
	target_data_prototype_ref22=ET.SubElement(autosar_variable_iref22,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref22.text='/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
	target_data_prototype_ref22.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}

def MSP_PPort_msi_ModeGroup():#remained

	mode_switch_points2=ET.SubElement(runnable_entity15,'MODE-SWITCH-POINTS')
	mode_switch_point2=ET.SubElement(mode_switch_points2,'MODE-SWITCH-POINT')
	mode_switch_point2.attrib={'UUID':rng.generate_uuid()} #:'8f7d9801-a32d-4e5f-85cd-fbcf669d921a'}
	short_name202=ET.SubElement(mode_switch_point2,'SHORT-NAME')
	short_name202.text='MSP_PPort_msi_ModeGroup'
	mode_group_iref2=ET.SubElement(mode_switch_point2,'MODE-GROUP-IREF')
	context_p_port_ref3=ET.SubElement(mode_group_iref2,'CONTEXT-P-PORT-REF')
	context_p_port_ref3.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_msi'
	context_p_port_ref3.attrib={'DEST':'P-PORT-PROTOTYPE'}
	target_mode_group_ref2=ET.SubElement(mode_group_iref2,'TARGET-MODE-GROUP-REF')
	target_mode_group_ref2.text='/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
	target_mode_group_ref2.attrib={'DEST':'MODE-DECLARATION-GROUP-PROTOTYPE'}
 
def ParameterAccess():#remained 
    
    global parameter_accesss1
    parameter_accesss1=ET.SubElement(runnable_entity15,'PARAMETER-ACCESSS')
    parameter_access1=ET.SubElement(parameter_accesss1,'PARAMETER-ACCESS')
    parameter_access1.attrib={'UUID':rng.generate_uuid()} #:'92d672aa-34ea-4fcb-a0a2-ab2431d59c0a'}
    short_name203=ET.SubElement(parameter_access1,'SHORT-NAME')
    short_name203.text='ParameterAccess'
    accessed_parameter1=ET.SubElement(parameter_access1,'ACCESSED-PARAMETER')
    local_parameter_ref1=ET.SubElement(accessed_parameter1,'LOCAL-PARAMETER-REF')
    local_parameter_ref1.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ConstantMemory'
    local_parameter_ref1.attrib={'DEST':'PARAMETER-DATA-PROTOTYPE'}
 
def PICPVA_PerInstanceParameter():#remained 
 
	parameter_access2=ET.SubElement(parameter_accesss1,'PARAMETER-ACCESS')
	parameter_access2.attrib={'UUID':rng.generate_uuid()} #:'391726ca-20e2-4c02-b063-65244a9e523a'}
	short_name204=ET.SubElement(parameter_access2,'SHORT-NAME')
	short_name204.text='PICPVA_PerInstanceParameter'
	accessed_parameter2=ET.SubElement(parameter_access2,'ACCESSED-PARAMETER')
	local_parameter_ref2=ET.SubElement(accessed_parameter2,'LOCAL-PARAMETER-REF')
	local_parameter_ref2.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/PerInstanceParameter'
	local_parameter_ref2.attrib={'DEST':'PARAMETER-DATA-PROTOTYPE'}
 
def CPA_RPort_prm_Parameter():#remained
 
	parameter_access3=ET.SubElement(parameter_accesss1,'PARAMETER-ACCESS')
	parameter_access3.attrib={'UUID':rng.generate_uuid()} #:'19d7aee6-82b8-4233-a787-b84bdb562167'}
	short_name205=ET.SubElement(parameter_access3,'SHORT-NAME')
	short_name205.text='CPA_RPort_prm_Parameter'
	accessed_parameter3=ET.SubElement(parameter_access3,'ACCESSED-PARAMETER')
	autosar_parameter_iref1=ET.SubElement(accessed_parameter3,'AUTOSAR-PARAMETER-IREF')
	port_prototype_ref23=ET.SubElement(autosar_parameter_iref1,'PORT-PROTOTYPE-REF')
	port_prototype_ref23.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_prm'
	port_prototype_ref23.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_data_prototype_ref23=ET.SubElement(autosar_parameter_iref1,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref23.text='/SharedElements/PortInterfaces/Parameter/ParameterInterface/Parameter'
	target_data_prototype_ref23.attrib={'DEST':'PARAMETER-DATA-PROTOTYPE'}
 
def CPA_RPort_prm_Parameter1():#remained
 
	parameter_access4=ET.SubElement(parameter_accesss1,'PARAMETER-ACCESS')
	parameter_access4.attrib={'UUID':rng.generate_uuid()} #:'ab7c5c59-47f3-4fee-a310-f64cb2c00c48'}
	short_name206=ET.SubElement(parameter_access4,'SHORT-NAME')
	short_name206.text='CPA_RPort_prm_Parameter1'
	accessed_parameter4=ET.SubElement(parameter_access4,'ACCESSED-PARAMETER')
	autosar_parameter_iref2=ET.SubElement(accessed_parameter4,'AUTOSAR-PARAMETER-IREF')
	port_prototype_ref24=ET.SubElement(autosar_parameter_iref2,'PORT-PROTOTYPE-REF')
	port_prototype_ref24.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_prm'
	port_prototype_ref24.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_data_prototype_ref24=ET.SubElement(autosar_parameter_iref2,'TARGET-DATA-PROTOTYPE-REF')
	target_data_prototype_ref24.text='/SharedElements/PortInterfaces/Parameter/ParameterInterface/Parameter1'
	target_data_prototype_ref24.attrib={'DEST':'PARAMETER-DATA-PROTOTYPE'}

def SCPVA_SharedParameter():#remained 
 
	parameter_access5=ET.SubElement(parameter_accesss1,'PARAMETER-ACCESS')
	parameter_access5.attrib={'UUID':rng.generate_uuid()} #:'f7d2bfa9-92c5-4627-b238-86aadd05585b'}
	short_name207=ET.SubElement(parameter_access5,'SHORT-NAME')
	short_name207.text='SCPVA_SharedParameter'
	accessed_parameter5=ET.SubElement(parameter_access5,'ACCESSED-PARAMETER')
	local_parameter_ref3=ET.SubElement(accessed_parameter5,'LOCAL-PARAMETER-REF')
	local_parameter_ref3.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/SharedParameter'
	local_parameter_ref3.attrib={'DEST':'PARAMETER-DATA-PROTOTYPE'}
 
def SSCP_RPort_CS_Operation1():#remained 
 
	server_call_points2=ET.SubElement(runnable_entity15,'SERVER-CALL-POINTS')
	synchronous_server_call_point1=ET.SubElement(server_call_points2,'SYNCHRONOUS-SERVER-CALL-POINT')
	synchronous_server_call_point1.attrib={'UUID':rng.generate_uuid()} #:'d6a93f51-be57-4a77-bd8f-e25d3e0ba149'}
	short_name208=ET.SubElement(synchronous_server_call_point1,'SHORT-NAME')
	short_name208.text='SSCP_RPort_CS_Operation1'
	operation_iref3=ET.SubElement(synchronous_server_call_point1,'OPERATION-IREF')
	context_r_port_ref5=ET.SubElement(operation_iref3,'CONTEXT-R-PORT-REF')
	context_r_port_ref5.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_CS'
	context_r_port_ref5.attrib={'DEST':'R-PORT-PROTOTYPE'}
	target_required_operation_ref2=ET.SubElement(operation_iref3,'TARGET-REQUIRED-OPERATION-REF')
	target_required_operation_ref2.text='/SharedElements/PortInterfaces/ClientServer/ClientServerInterface/Operation1'
	target_required_operation_ref2.attrib={'DEST':'CLIENT-SERVER-OPERATION'}
	timeout2=ET.SubElement(synchronous_server_call_point1,'TIMEOUT')
	timeout2.text='0'
 
def IRVWA_ExplicitInterRunnableVariable():#remained
    
    global written_local_variables1
    written_local_variables1=ET.SubElement(runnable_entity15,'WRITTEN-LOCAL-VARIABLES')
    variable_access25=ET.SubElement(written_local_variables1,'VARIABLE-ACCESS')
    variable_access25.attrib={'UUID':rng.generate_uuid()} #:'7e246e9c-b78a-47be-8798-02887c881e6e'}
    short_name209=ET.SubElement(variable_access25,'SHORT-NAME')
    short_name209.text='IRVWA_ExplicitInterRunnableVariable'
    accessed_variable25=ET.SubElement(variable_access25,'ACCESSED-VARIABLE')
    local_variable_ref3=ET.SubElement(accessed_variable25,'LOCAL-VARIABLE-REF')
    local_variable_ref3.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ExplicitInterRunnableVariable'
    local_variable_ref3.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}
 
def IRVWA_ImplicitInterRunnableVariable():#remained
 
	variable_access26=ET.SubElement(written_local_variables1,'VARIABLE-ACCESS')
	variable_access26.attrib={'UUID':rng.generate_uuid()} #:'d976bba9-3132-4e15-ac45-88b85facf508'}
	short_name210=ET.SubElement(variable_access26,'SHORT-NAME')
	short_name210.text='IRVWA_ImplicitInterRunnableVariable'
	accessed_variable26=ET.SubElement(variable_access26,'ACCESSED-VARIABLE')
	local_variable_ref4=ET.SubElement(accessed_variable26,'LOCAL-VARIABLE-REF')
	local_variable_ref4.text='/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ImplicitInterRunnableVariable'
	local_variable_ref4.attrib={'DEST':'VARIABLE-DATA-PROTOTYPE'}



########## SW Component types ########### 

def ApplicationSwComponentType(ApplSWC_folder_elements,ApplSWC_shortname): #completed
    global application_sw_component_type

    application_sw_component_type=ET.SubElement(ApplSWC_folder_elements,'APPLICATION-SW-COMPONENT-TYPE')
    application_sw_component_type.attrib={'UUID':rng.generate_uuid()} #automatically rng to be generated and everytime need to check the uuid in the xml file
    ApplSWC_shortname=ET.SubElement(application_sw_component_type,'SHORT-NAME')
    ApplSWC_shortname.text= ApplSWC_shortname
 
def ComplexDeviceDriverSwComponentType(CddSWC_folder_elements, CddSWC_shortname ): #completed

	complex_device_driver_sw_component_type=ET.SubElement(CddSWC_folder_elements,'COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE')
	complex_device_driver_sw_component_type.attrib={'UUID':rng.generate_uuid()}
	short_name=ET.SubElement(complex_device_driver_sw_component_type,'SHORT-NAME')
	short_name.text=CddSWC_shortname
 
def CompositionSwComponentType():#remained
 
	ar_package25=ET.SubElement(ar_packages5,'AR-PACKAGE')
	ar_package25.attrib={'UUID':rng.generate_uuid()} #:'a9d129de-eda4-4cda-9025-70a56f38fb59'}
	short_name215=ET.SubElement(ar_package25,'SHORT-NAME')
	short_name215.text='CompSWC'
	elements21=ET.SubElement(ar_package25,'ELEMENTS')
	composition_sw_component_type1=ET.SubElement(elements21,'COMPOSITION-SW-COMPONENT-TYPE')
	composition_sw_component_type1.attrib={'UUID':rng.generate_uuid()} #9e886193-6d1b-454f-98b2-d0347db57ace'}
	short_name216=ET.SubElement(composition_sw_component_type1,'SHORT-NAME')
	short_name216.text='CompositionSwComponentType'

def EcuAbstractionSwComponentType():#remained
 
	ar_package26=ET.SubElement(ar_packages5,'AR-PACKAGE')
	ar_package26.attrib={'UUID':rng.generate_uuid()} #28aa9cf2-4118-4878-8504-271a3ed4600b'}
	short_name217=ET.SubElement(ar_package26,'SHORT-NAME')
	short_name217.text='EcuAbSWC'
	elements22=ET.SubElement(ar_package26,'ELEMENTS')
	ecu_abstraction_sw_component_type1=ET.SubElement(elements22,'ECU-ABSTRACTION-SW-COMPONENT-TYPE')
	ecu_abstraction_sw_component_type1.attrib={'UUID':rng.generate_uuid()} #0dc33c67-8b23-4896-b6a3-8a537f1cd166'}
	short_name218=ET.SubElement(ecu_abstraction_sw_component_type1,'SHORT-NAME')
	short_name218.text='EcuAbstractionSwComponentType'

def NvBlockSwComponentType():#remained
 
	ar_package27=ET.SubElement(ar_packages5,'AR-PACKAGE')
	ar_package27.attrib={'UUID':rng.generate_uuid()} #8562405a-26a1-4c3d-861f-eb0745310572'}
	short_name219=ET.SubElement(ar_package27,'SHORT-NAME')
	short_name219.text='NvDataSWC'
	elements23=ET.SubElement(ar_package27,'ELEMENTS')
	nv_block_sw_component_type1=ET.SubElement(elements23,'NV-BLOCK-SW-COMPONENT-TYPE')
	nv_block_sw_component_type1.attrib={'UUID':rng.generate_uuid()} #9a2c1578-3f64-4af0-b953-7b81f28434cf'}
	short_name220=ET.SubElement(nv_block_sw_component_type1,'SHORT-NAME')
	short_name220.text='NvBlockSwComponentType'

def ParameterSwComponentType():#remained 
 
	ar_package28=ET.SubElement(ar_packages5,'AR-PACKAGE')
	ar_package28.attrib={'UUID':rng.generate_uuid()} #0a54c44d-f71e-4ec3-bbf1-410c0b885915'}
	short_name221=ET.SubElement(ar_package28,'SHORT-NAME')
	short_name221.text='PrmSWC'
	elements24=ET.SubElement(ar_package28,'ELEMENTS')
	parameter_sw_component_type1=ET.SubElement(elements24,'PARAMETER-SW-COMPONENT-TYPE')
	parameter_sw_component_type1.attrib={'UUID':rng.generate_uuid()} #c21a6d07-19ae-40ac-affe-f4aa3b5acb25'}
	short_name222=ET.SubElement(parameter_sw_component_type1,'SHORT-NAME')
	short_name222.text='ParameterSwComponentType'

def SensorActuatorSwComponentType():#remained
 
	ar_package29=ET.SubElement(ar_packages5,'AR-PACKAGE')
	ar_package29.attrib={'UUID':rng.generate_uuid()} #f142ef66-4dce-4750-8568-a7e836f462da'}
	short_name223=ET.SubElement(ar_package29,'SHORT-NAME')
	short_name223.text='SnsrActSWC'
	elements25=ET.SubElement(ar_package29,'ELEMENTS')
	sensor_actuator_sw_component_type1=ET.SubElement(elements25,'SENSOR-ACTUATOR-SW-COMPONENT-TYPE')
	sensor_actuator_sw_component_type1.attrib={'UUID':rng.generate_uuid()} #e631e3e3-9a52-4bbe-a762-4311d8f45934'}
	short_name224=ET.SubElement(sensor_actuator_sw_component_type1,'SHORT-NAME')
	short_name224.text='SensorActuatorSwComponentType'

def ServiceProxySwComponentType():#remained
 
	ar_package30=ET.SubElement(ar_packages5,'AR-PACKAGE')
	ar_package30.attrib={'UUID':rng.generate_uuid()} #60bb3f96-0a5c-4e30-bdda-5205f3a1cdb6'}
	short_name225=ET.SubElement(ar_package30,'SHORT-NAME')
	short_name225.text='SrvcPrxySWC'
	elements26=ET.SubElement(ar_package30,'ELEMENTS')
	service_proxy_sw_component_type1=ET.SubElement(elements26,'SERVICE-PROXY-SW-COMPONENT-TYPE')
	service_proxy_sw_component_type1.attrib={'UUID':rng.generate_uuid()} #7e09780f-aad2-4f70-8c22-e5e19f1a82e8'}
	short_name226=ET.SubElement(service_proxy_sw_component_type1,'SHORT-NAME')
	short_name226.text='ServiceProxySwComponentType'

def ServiceSwComponentType():#remained
 
	ar_package31=ET.SubElement(ar_packages5,'AR-PACKAGE')
	ar_package31.attrib={'UUID':rng.generate_uuid()} #2ed6bb1a-c9d6-46c0-ae8b-0743080405b6'}
	short_name227=ET.SubElement(ar_package31,'SHORT-NAME')
	short_name227.text='SrvcSWC'
	elements27=ET.SubElement(ar_package31,'ELEMENTS')
	service_sw_component_type1=ET.SubElement(elements27,'SERVICE-SW-COMPONENT-TYPE')
	service_sw_component_type1.attrib={'UUID':rng.generate_uuid()} #1da8de22-a6ec-4cab-829a-56300097c5ac'}
	short_name228=ET.SubElement(service_sw_component_type1,'SHORT-NAME')
	short_name228.text='ServiceSwComponentType'


########## Systems ########### 

def Systems():#remained 

	ar_package32=ET.SubElement(ar_packages1,'AR-PACKAGE')
	short_name229=ET.SubElement(ar_package32,'SHORT-NAME')
	short_name229.text='Systems'
 
    # Call all functions to build up the XML structure
  
      