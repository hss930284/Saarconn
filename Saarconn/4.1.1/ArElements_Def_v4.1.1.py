import xml.etree.ElementTree as ET
global_elements = {}

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
# Create the root element
root = ET.Element('AUTOSAR', attrib={
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns': "http://autosar.org/schema/r4.0",
    'xsi:schemaLocation': "http://autosar.org/schema/r4.0 AUTOSAR_4-1-1.xsd"
})

global_elements = {
    'root': root
}

def ApplicationArrayDataType_Fixed():
    global_elements['elements12'] = ET.SubElement(global_elements['ar-package27'], 'elements')
    global_elements['application-array-data-type'] = ET.SubElement(global_elements['elements12'], 'application-array-data-type')
    global_elements['application-array-data-type'].attrib = {'UUID': '99540e2c-05ec-4a85-94bb-9a3999ac57fe'}
    global_elements['short-name350'] = ET.SubElement(global_elements['application-array-data-type'], 'short-name')
    global_elements['short-name350'].text = 'ApplicationArrayDataType_Fixed'
    global_elements['category69'] = ET.SubElement(global_elements['application-array-data-type'], 'category')
    global_elements['category69'].text = 'ARRAY'
    global_elements['element'] = ET.SubElement(global_elements['application-array-data-type'], 'element')
    global_elements['element'].attrib = {'UUID': '7391c5fe-50b6-4b88-bc63-ec1975221a4f'}
    global_elements['short-name351'] = ET.SubElement(global_elements['element'], 'short-name')
    global_elements['short-name351'].text = 'Element'
    global_elements['category70'] = ET.SubElement(global_elements['element'], 'category')
    global_elements['category70'].text = 'VALUE'
    global_elements['type-tref'] = ET.SubElement(global_elements['element'], 'type-tref')
    global_elements['type-tref'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['array-size-semantics'] = ET.SubElement(global_elements['element'], 'array-size-semantics')
    global_elements['array-size-semantics'].text = 'FIXED-SIZE'
    global_elements['max-number-of-elements'] = ET.SubElement(global_elements['element'], 'max-number-of-elements')
    global_elements['max-number-of-elements'].text = '15'
    global_elements['application-array-data-type2'] = ET.SubElement(global_elements['elements12'], 'application-array-data-type')
    global_elements['application-array-data-type2'].attrib = {'UUID': 'd5f3c7e9-dd94-4d37-888e-b6e44b01cc5a'}
    global_elements['short-name352'] = ET.SubElement(global_elements['application-array-data-type2'], 'short-name')
    global_elements['short-name352'].text = 'ApplicationArrayDataType_Variable'
    global_elements['category71'] = ET.SubElement(global_elements['application-array-data-type2'], 'category')
    global_elements['category71'].text = 'ARRAY'
    global_elements['element2'] = ET.SubElement(global_elements['application-array-data-type2'], 'element')
    global_elements['element2'].attrib = {'UUID': 'fef3f4b8-d9bd-4cb1-94b8-4403e665c4fa'}
    global_elements['short-name353'] = ET.SubElement(global_elements['element2'], 'short-name')
    global_elements['short-name353'].text = 'Element'
    global_elements['category72'] = ET.SubElement(global_elements['element2'], 'category')
    global_elements['category72'].text = 'VALUE'
    global_elements['type-tref2'] = ET.SubElement(global_elements['element2'], 'type-tref')
    global_elements['type-tref2'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref2'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['array-size-semantics2'] = ET.SubElement(global_elements['element2'], 'array-size-semantics')
    global_elements['array-size-semantics2'].text = 'VARIABLE-SIZE'
    global_elements['max-number-of-elements2'] = ET.SubElement(global_elements['element2'], 'max-number-of-elements')
    global_elements['max-number-of-elements2'].text = '15'


def ApplicationPrimitiveDataType():
    global_elements['ar-package28'] = ET.SubElement(global_elements['ar-packages9'], 'ar-package')
    global_elements['ar-package28'].attrib = {'UUID': 'b142aaa0-2671-41cd-bbc6-78cc30cf22c4'}
    global_elements['short-name354'] = ET.SubElement(global_elements['ar-package28'], 'short-name')
    global_elements['short-name354'].text = 'Primitive'
    global_elements['elements13'] = ET.SubElement(global_elements['ar-package28'], 'elements')
    global_elements['application-primitive-data-type'] = ET.SubElement(global_elements['elements13'], 'application-primitive-data-type')
    global_elements['application-primitive-data-type'].attrib = {'UUID': '18357165-e774-4282-90db-fcb76c7c6727'}
    global_elements['short-name355'] = ET.SubElement(global_elements['application-primitive-data-type'], 'short-name')
    global_elements['short-name355'].text = 'ApplicationPrimitiveDataType'
    global_elements['category73'] = ET.SubElement(global_elements['application-primitive-data-type'], 'category')
    global_elements['category73'].text = 'VALUE'
    global_elements['sw-data-def-props44'] = ET.SubElement(global_elements['application-primitive-data-type'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants44'] = ET.SubElement(global_elements['sw-data-def-props44'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional44'] = ET.SubElement(global_elements['sw-data-def-props-variants44'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access'] = ET.SubElement(global_elements['sw-data-def-props-conditional44'], 'sw-calibration-access')
    global_elements['sw-calibration-access'].text = 'NOT-ACCESSIBLE'
    global_elements['compu-method-ref7'] = ET.SubElement(global_elements['sw-data-def-props-conditional44'], 'compu-method-ref')
    global_elements['compu-method-ref7'].text = '/SharedElements/CompuMethods/CompuMethod'
    global_elements['compu-method-ref7'].attrib = {'DEST': 'COMPU-METHOD'}
    global_elements['data-constr-ref24'] = ET.SubElement(global_elements['sw-data-def-props-conditional44'], 'data-constr-ref')
    global_elements['data-constr-ref24'].text = '/SharedElements/DataConstr/DataConstr'
    global_elements['data-constr-ref24'].attrib = {'DEST': 'DATA-CONSTR'}
    global_elements['invalid-value'] = ET.SubElement(global_elements['sw-data-def-props-conditional44'], 'invalid-value')
    global_elements['application-value-specification'] = ET.SubElement(global_elements['invalid-value'], 'application-value-specification')
    global_elements['category74'] = ET.SubElement(global_elements['application-value-specification'], 'category')
    global_elements['category74'].text = 'VALUE'
    global_elements['sw-value-cont'] = ET.SubElement(global_elements['application-value-specification'], 'sw-value-cont')
    global_elements['sw-values-phys'] = ET.SubElement(global_elements['sw-value-cont'], 'sw-values-phys')
    global_elements['v'] = ET.SubElement(global_elements['sw-values-phys'], 'v')
    global_elements['v'].text = '8'
    global_elements['unit-ref'] = ET.SubElement(global_elements['sw-data-def-props-conditional44'], 'unit-ref')
    global_elements['unit-ref'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref'].attrib = {'DEST': 'UNIT'}
    global_elements['application-primitive-data-type2'] = ET.SubElement(global_elements['elements13'], 'application-primitive-data-type')
    global_elements['application-primitive-data-type2'].attrib = {'UUID': '14c56edb-9cf8-48cc-92d7-4cc1ca683a0f'}
    global_elements['short-name356'] = ET.SubElement(global_elements['application-primitive-data-type2'], 'short-name')
    global_elements['short-name356'].text = 'Bool_ApplicationPrimitiveDataType'
    global_elements['category75'] = ET.SubElement(global_elements['application-primitive-data-type2'], 'category')
    global_elements['category75'].text = 'BOOLEAN'
    global_elements['sw-data-def-props45'] = ET.SubElement(global_elements['application-primitive-data-type2'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants45'] = ET.SubElement(global_elements['sw-data-def-props45'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional45'] = ET.SubElement(global_elements['sw-data-def-props-variants45'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access2'] = ET.SubElement(global_elements['sw-data-def-props-conditional45'], 'sw-calibration-access')
    global_elements['sw-calibration-access2'].text = 'NOT-ACCESSIBLE'
    global_elements['compu-method-ref8'] = ET.SubElement(global_elements['sw-data-def-props-conditional45'], 'compu-method-ref')
    global_elements['compu-method-ref8'].text = '/SharedElements/CompuMethods/CompuMethod'
    global_elements['compu-method-ref8'].attrib = {'DEST': 'COMPU-METHOD'}
    global_elements['data-constr-ref25'] = ET.SubElement(global_elements['sw-data-def-props-conditional45'], 'data-constr-ref')
    global_elements['data-constr-ref25'].text = '/SharedElements/DataConstr/DataConstr'
    global_elements['data-constr-ref25'].attrib = {'DEST': 'DATA-CONSTR'}
    global_elements['unit-ref2'] = ET.SubElement(global_elements['sw-data-def-props-conditional45'], 'unit-ref')
    global_elements['unit-ref2'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref2'].attrib = {'DEST': 'UNIT'}
    global_elements['application-primitive-data-type3'] = ET.SubElement(global_elements['elements13'], 'application-primitive-data-type')
    global_elements['application-primitive-data-type3'].attrib = {'UUID': 'a799e394-8020-4e26-abaf-804ce312d6c0'}
    global_elements['short-name357'] = ET.SubElement(global_elements['application-primitive-data-type3'], 'short-name')
    global_elements['short-name357'].text = 'Copy_ApplicationPrimitiveDataType'
    global_elements['category76'] = ET.SubElement(global_elements['application-primitive-data-type3'], 'category')
    global_elements['category76'].text = 'VALUE'
    global_elements['sw-data-def-props46'] = ET.SubElement(global_elements['application-primitive-data-type3'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants46'] = ET.SubElement(global_elements['sw-data-def-props46'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional46'] = ET.SubElement(global_elements['sw-data-def-props-variants46'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access3'] = ET.SubElement(global_elements['sw-data-def-props-conditional46'], 'sw-calibration-access')
    global_elements['sw-calibration-access3'].text = 'NOT-ACCESSIBLE'
    global_elements['compu-method-ref9'] = ET.SubElement(global_elements['sw-data-def-props-conditional46'], 'compu-method-ref')
    global_elements['compu-method-ref9'].text = '/SharedElements/CompuMethods/CompuMethod'
    global_elements['compu-method-ref9'].attrib = {'DEST': 'COMPU-METHOD'}
    global_elements['data-constr-ref26'] = ET.SubElement(global_elements['sw-data-def-props-conditional46'], 'data-constr-ref')
    global_elements['data-constr-ref26'].text = '/SharedElements/DataConstr/DataConstr'
    global_elements['data-constr-ref26'].attrib = {'DEST': 'DATA-CONSTR'}
    global_elements['unit-ref3'] = ET.SubElement(global_elements['sw-data-def-props-conditional46'], 'unit-ref')
    global_elements['unit-ref3'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref3'].attrib = {'DEST': 'UNIT'}
    global_elements['application-primitive-data-type4'] = ET.SubElement(global_elements['elements13'], 'application-primitive-data-type')
    global_elements['application-primitive-data-type4'].attrib = {'UUID': 'decc899e-e751-4907-998b-8769b6445a38'}
    global_elements['short-name358'] = ET.SubElement(global_elements['application-primitive-data-type4'], 'short-name')
    global_elements['short-name358'].text = 'String_ApplicationPrimitiveDataType'
    global_elements['category77'] = ET.SubElement(global_elements['application-primitive-data-type4'], 'category')
    global_elements['category77'].text = 'STRING'
    global_elements['sw-data-def-props47'] = ET.SubElement(global_elements['application-primitive-data-type4'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants47'] = ET.SubElement(global_elements['sw-data-def-props47'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional47'] = ET.SubElement(global_elements['sw-data-def-props-variants47'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access4'] = ET.SubElement(global_elements['sw-data-def-props-conditional47'], 'sw-calibration-access')
    global_elements['sw-calibration-access4'].text = 'NOT-ACCESSIBLE'
    global_elements['sw-text-props'] = ET.SubElement(global_elements['sw-data-def-props-conditional47'], 'sw-text-props')
    global_elements['array-size-semantics3'] = ET.SubElement(global_elements['sw-text-props'], 'array-size-semantics')
    global_elements['array-size-semantics3'].text = 'VARIABLE-SIZE'
    global_elements['sw-max-text-size'] = ET.SubElement(global_elements['sw-text-props'], 'sw-max-text-size')
    global_elements['sw-max-text-size'].text = '16'
    global_elements['unit-ref4'] = ET.SubElement(global_elements['sw-data-def-props-conditional47'], 'unit-ref')
    global_elements['unit-ref4'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref4'].attrib = {'DEST': 'UNIT'}

def Record():
    global_elements['ar-package29'] = ET.SubElement(global_elements['ar-packages9'], 'ar-package')
    global_elements['ar-package29'].attrib = {'UUID': '65217d8d-3662-4a20-a643-ec9ee94de7a0'}
    global_elements['short-name359'] = ET.SubElement(global_elements['ar-package29'], 'short-name')
    global_elements['short-name359'].text = 'Record'
    global_elements['elements14'] = ET.SubElement(global_elements['ar-package29'], 'elements')
    global_elements['application-record-data-type'] = ET.SubElement(global_elements['elements14'], 'application-record-data-type')
    global_elements['application-record-data-type'].attrib = {'UUID': 'd20b1ec6-9940-43c7-beda-f773a805fab6'}
    global_elements['short-name360'] = ET.SubElement(global_elements['application-record-data-type'], 'short-name')
    global_elements['short-name360'].text = 'ApplicationRecordDataType'
    global_elements['category78'] = ET.SubElement(global_elements['application-record-data-type'], 'category')
    global_elements['category78'].text = 'STRUCTURE'
    global_elements['elements15'] = ET.SubElement(global_elements['application-record-data-type'], 'elements')
    global_elements['application-record-element'] = ET.SubElement(global_elements['elements15'], 'application-record-element')
    global_elements['application-record-element'].attrib = {'UUID': 'bd5079b0-6ac0-4d72-a63a-afd373f2bcc5'}
    global_elements['short-name361'] = ET.SubElement(global_elements['application-record-element'], 'short-name')
    global_elements['short-name361'].text = 'Element'
    global_elements['type-tref3'] = ET.SubElement(global_elements['application-record-element'], 'type-tref')
    global_elements['type-tref3'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref3'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['application-record-element2'] = ET.SubElement(global_elements['elements15'], 'application-record-element')
    global_elements['application-record-element2'].attrib = {'UUID': '12021f0e-9ad1-4df2-bffa-197611387a0a'}
    global_elements['short-name362'] = ET.SubElement(global_elements['application-record-element2'], 'short-name')
    global_elements['short-name362'].text = 'Element1'
    global_elements['type-tref4'] = ET.SubElement(global_elements['application-record-element2'], 'type-tref')
    global_elements['type-tref4'].text = '/SharedElements/ApplicationDataTypes/Array/ApplicationArrayDataType_Fixed'
    global_elements['type-tref4'].attrib = {'DEST': 'APPLICATION-ARRAY-DATA-TYPE'}

def BITFIELD_TEXTTABLE_CompuMethod():
    global_elements['ar-package30'] = ET.SubElement(global_elements['ar-packages8'], 'ar-package')
    global_elements['short-name363'] = ET.SubElement(global_elements['ar-package30'], 'short-name')
    global_elements['short-name363'].text = 'CompuMethods'
    global_elements['elements16'] = ET.SubElement(global_elements['ar-package30'], 'elements')
    global_elements['compu-method7'] = ET.SubElement(global_elements['elements16'], 'compu-method')
    global_elements['compu-method7'].attrib = {'UUID': 'e51fd87b-fe38-48d5-b94a-c11851da3006'}
    global_elements['short-name364'] = ET.SubElement(global_elements['compu-method7'], 'short-name')
    global_elements['short-name364'].text = 'BITFIELD_TEXTTABLE_CompuMethod'
    global_elements['category79'] = ET.SubElement(global_elements['compu-method7'], 'category')
    global_elements['category79'].text = 'BITFIELD_TEXTTABLE'
    global_elements['unit-ref5'] = ET.SubElement(global_elements['compu-method7'], 'unit-ref')
    global_elements['unit-ref5'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref5'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys7'] = ET.SubElement(global_elements['compu-method7'], 'compu-internal-to-phys')
    global_elements['compu-scales7'] = ET.SubElement(global_elements['compu-internal-to-phys7'], 'compu-scales')
    global_elements['compu-scale18'] = ET.SubElement(global_elements['compu-scales7'], 'compu-scale')
    global_elements['mask'] = ET.SubElement(global_elements['compu-scale18'], 'mask')
    global_elements['mask'].text = '0'
    global_elements['lower-limit41'] = ET.SubElement(global_elements['compu-scale18'], 'lower-limit')
    global_elements['lower-limit41'].text = '0'
    global_elements['upper-limit41'] = ET.SubElement(global_elements['compu-scale18'], 'upper-limit')
    global_elements['upper-limit41'].text = '0'
    global_elements['compu-const18'] = ET.SubElement(global_elements['compu-scale18'], 'compu-const')
    global_elements['vt18'] = ET.SubElement(global_elements['compu-const18'], 'vt')
    global_elements['vt18'].text = 'xyz'
    global_elements['compu-scale19'] = ET.SubElement(global_elements['compu-scales7'], 'compu-scale')
    global_elements['mask2'] = ET.SubElement(global_elements['compu-scale19'], 'mask')
    global_elements['mask2'].text = '0'
    global_elements['lower-limit42'] = ET.SubElement(global_elements['compu-scale19'], 'lower-limit')
    global_elements['lower-limit42'].text = '1'
    global_elements['upper-limit42'] = ET.SubElement(global_elements['compu-scale19'], 'upper-limit')
    global_elements['upper-limit42'].text = '1'
    global_elements['compu-const19'] = ET.SubElement(global_elements['compu-scale19'], 'compu-const')
    global_elements['vt19'] = ET.SubElement(global_elements['compu-const19'], 'vt')
    global_elements['vt19'].text = 'xyz1'
    global_elements['compu-scale20'] = ET.SubElement(global_elements['compu-scales7'], 'compu-scale')
    global_elements['mask3'] = ET.SubElement(global_elements['compu-scale20'], 'mask')
    global_elements['mask3'].text = '0'
    global_elements['lower-limit43'] = ET.SubElement(global_elements['compu-scale20'], 'lower-limit')
    global_elements['lower-limit43'].text = '2'
    global_elements['upper-limit43'] = ET.SubElement(global_elements['compu-scale20'], 'upper-limit')
    global_elements['upper-limit43'].text = '2'
    global_elements['compu-const20'] = ET.SubElement(global_elements['compu-scale20'], 'compu-const')
    global_elements['vt20'] = ET.SubElement(global_elements['compu-const20'], 'vt')
    global_elements['vt20'].text = 'xyz2'
    global_elements['compu-scale21'] = ET.SubElement(global_elements['compu-scales7'], 'compu-scale')
    global_elements['mask4'] = ET.SubElement(global_elements['compu-scale21'], 'mask')
    global_elements['mask4'].text = '0'
    global_elements['lower-limit44'] = ET.SubElement(global_elements['compu-scale21'], 'lower-limit')
    global_elements['lower-limit44'].text = '3'
    global_elements['upper-limit44'] = ET.SubElement(global_elements['compu-scale21'], 'upper-limit')
    global_elements['upper-limit44'].text = '3'
    global_elements['compu-const21'] = ET.SubElement(global_elements['compu-scale21'], 'compu-const')
    global_elements['vt21'] = ET.SubElement(global_elements['compu-const21'], 'vt')
    global_elements['vt21'].text = 'xyz3'
    global_elements['compu-scale22'] = ET.SubElement(global_elements['compu-scales7'], 'compu-scale')
    global_elements['mask5'] = ET.SubElement(global_elements['compu-scale22'], 'mask')
    global_elements['mask5'].text = '0'
    global_elements['lower-limit45'] = ET.SubElement(global_elements['compu-scale22'], 'lower-limit')
    global_elements['lower-limit45'].text = '4'
    global_elements['upper-limit45'] = ET.SubElement(global_elements['compu-scale22'], 'upper-limit')
    global_elements['upper-limit45'].text = '4'
    global_elements['compu-const22'] = ET.SubElement(global_elements['compu-scale22'], 'compu-const')
    global_elements['vt22'] = ET.SubElement(global_elements['compu-const22'], 'vt')
    global_elements['vt22'].text = 'xyz4'

def CompuMethod():
    global_elements['compu-method8'].attrib = {'UUID': 'a65ae6b6-3eab-43ff-907b-2c8276c8528b'}
    global_elements['short-name365'] = ET.SubElement(global_elements['compu-method8'], 'short-name')
    global_elements['short-name365'].text = 'CompuMethod'
    global_elements['category80'] = ET.SubElement(global_elements['compu-method8'], 'category')
    global_elements['category80'].text = 'IDENTICAL'
    global_elements['unit-ref6'] = ET.SubElement(global_elements['compu-method8'], 'unit-ref')
    global_elements['unit-ref6'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref6'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-method9'] = ET.SubElement(global_elements['elements16'], 'compu-method')
    global_elements['compu-method9'].attrib = {'UUID': '386978fd-a90f-4003-b63e-f9e35b6d76b8'}
    global_elements['short-name366'] = ET.SubElement(global_elements['compu-method9'], 'short-name')
    global_elements['compu-method8'] = ET.SubElement(global_elements['elements16'], 'compu-method') #short-name366'].text = 'LINEAR_CompuMethod'
    global_elements['short-name366'].text = 'LINEAR_CompuMethod'
    global_elements['category81'] = ET.SubElement(global_elements['compu-method9'], 'category')
    global_elements['category81'].text = 'LINEAR'
    global_elements['unit-ref7'] = ET.SubElement(global_elements['compu-method9'], 'unit-ref')
    global_elements['unit-ref7'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref7'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys8'] = ET.SubElement(global_elements['compu-method9'], 'compu-internal-to-phys')
    global_elements['compu-scales8'] = ET.SubElement(global_elements['compu-internal-to-phys8'], 'compu-scales')
    global_elements['compu-scale23'] = ET.SubElement(global_elements['compu-scales8'], 'compu-scale')
    global_elements['compu-rational-coeffs'] = ET.SubElement(global_elements['compu-scale23'], 'compu-rational-coeffs')
    global_elements['compu-numerator'] = ET.SubElement(global_elements['compu-rational-coeffs'], 'compu-numerator')
    global_elements['v2'] = ET.SubElement(global_elements['compu-numerator'], 'v')
    global_elements['v2'].text = '0'
    global_elements['v3'] = ET.SubElement(global_elements['compu-numerator'], 'v')
    global_elements['v3'].text = '1'
    global_elements['compu-denominator'] = ET.SubElement(global_elements['compu-rational-coeffs'], 'compu-denominator')
    global_elements['v4'] = ET.SubElement(global_elements['compu-denominator'], 'v')
    global_elements['v4'].text = '1'

def RAT_FUNC_CompuMethod():
    global_elements['compu-method10'] = ET.SubElement(global_elements['elements16'], 'compu-method')
    global_elements['compu-method10'].attrib = {'UUID': '74ea35c5-6b05-40a2-b22c-3c1a179a095b'}
    global_elements['short-name367'] = ET.SubElement(global_elements['compu-method10'], 'short-name')
    global_elements['short-name367'].text = 'RAT_FUNC_CompuMethod'
    global_elements['category82'] = ET.SubElement(global_elements['compu-method10'], 'category')
    global_elements['category82'].text = 'RAT_FUNC'
    global_elements['unit-ref8'] = ET.SubElement(global_elements['compu-method10'], 'unit-ref')
    global_elements['unit-ref8'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref8'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys9'] = ET.SubElement(global_elements['compu-method10'], 'compu-internal-to-phys')
    global_elements['compu-scales9'] = ET.SubElement(global_elements['compu-internal-to-phys9'], 'compu-scales')
    global_elements['compu-scale24'] = ET.SubElement(global_elements['compu-scales9'], 'compu-scale')
    global_elements['compu-rational-coeffs2'] = ET.SubElement(global_elements['compu-scale24'], 'compu-rational-coeffs')
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
    global_elements['compu-method11'] = ET.SubElement(global_elements['elements16'], 'compu-method')
    global_elements['compu-method11'].attrib = {'UUID': 'cb57246c-cf48-448f-b8a5-5f319b76ee49'}
    global_elements['short-name368'] = ET.SubElement(global_elements['compu-method11'], 'short-name')
    global_elements['short-name368'].text = 'SCALE_RATIONAL_AND_TEXTTABLE_CompuMethod'
    global_elements['desc8'] = ET.SubElement(global_elements['compu-method11'], 'desc')
    global_elements['l-28'] = ET.SubElement(global_elements['desc8'], 'l-2')
    global_elements['l-28'].text = 'S'
    global_elements['l-28'].attrib = {'L': 'FOR-ALL'}
    global_elements['category83'] = ET.SubElement(global_elements['compu-method11'], 'category')
    global_elements['category83'].text = 'SCALE_RATIONAL_AND_TEXTTABLE'
    global_elements['unit-ref9'] = ET.SubElement(global_elements['compu-method11'], 'unit-ref')
    global_elements['unit-ref9'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref9'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys10'] = ET.SubElement(global_elements['compu-method11'], 'compu-internal-to-phys')
    global_elements['compu-scales10'] = ET.SubElement(global_elements['compu-internal-to-phys10'], 'compu-scales')
    global_elements['compu-scale25'] = ET.SubElement(global_elements['compu-scales10'], 'compu-scale')
    global_elements['lower-limit46'] = ET.SubElement(global_elements['compu-scale25'], 'lower-limit')
    global_elements['lower-limit46'].text = '0'
    global_elements['upper-limit46'] = ET.SubElement(global_elements['compu-scale25'], 'upper-limit')
    global_elements['upper-limit46'].text = '15'
    global_elements['compu-rational-coeffs3'] = ET.SubElement(global_elements['compu-scale25'], 'compu-rational-coeffs')
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
    global_elements['compu-scale26'] = ET.SubElement(global_elements['compu-scales10'], 'compu-scale')
    global_elements['symbol'] = ET.SubElement(global_elements['compu-scale26'], 'symbol')
    global_elements['symbol'].text = 'sdcd'
    global_elements['lower-limit47'] = ET.SubElement(global_elements['compu-scale26'], 'lower-limit')
    global_elements['lower-limit47'].text = '16'
    global_elements['upper-limit47'] = ET.SubElement(global_elements['compu-scale26'], 'upper-limit')
    global_elements['upper-limit47'].text = '16'
    global_elements['compu-const23'] = ET.SubElement(global_elements['compu-scale26'], 'compu-const')
    global_elements['vt23'] = ET.SubElement(global_elements['compu-const23'], 'vt')
    global_elements['vt23'].text = 'sdcd'
    global_elements['compu-scale27'] = ET.SubElement(global_elements['compu-scales10'], 'compu-scale')
    global_elements['symbol2'] = ET.SubElement(global_elements['compu-scale27'], 'symbol')
    global_elements['symbol2'].text = 'sdcd1'
    global_elements['lower-limit48'] = ET.SubElement(global_elements['compu-scale27'], 'lower-limit')
    global_elements['lower-limit48'].text = '17'
    global_elements['upper-limit48'] = ET.SubElement(global_elements['compu-scale27'], 'upper-limit')
    global_elements['upper-limit48'].text = '17'
    global_elements['compu-const24'] = ET.SubElement(global_elements['compu-scale27'], 'compu-const')
    global_elements['vt24'] = ET.SubElement(global_elements['compu-const24'], 'vt')
    global_elements['vt24'].text = 'sdcd1'
    global_elements['compu-default-value'] = ET.SubElement(global_elements['compu-internal-to-phys10'], 'compu-default-value')
    global_elements['v17'] = ET.SubElement(global_elements['compu-default-value'], 'v')
    global_elements['v17'].text = '17'

def Scale_linear_And_texttable_CompuMethod():
    global_elements['compu-method12'] = ET.SubElement(global_elements['elements16'], 'compu-method')
    global_elements['compu-method12'].attrib = {'UUID': '19ee54ef-4447-4987-bcbe-a9d2a743d569'}
    global_elements['short-name369'] = ET.SubElement(global_elements['compu-method12'], 'short-name')
    global_elements['short-name369'].text = 'Scale_linear_And_texttable_CompuMethod'
    global_elements['desc9'] = ET.SubElement(global_elements['compu-method12'], 'desc')
    global_elements['l-29'] = ET.SubElement(global_elements['desc9'], 'l-2')
    global_elements['l-29'].text = 'Scale_linear _And_texttable_CompuMethod'
    global_elements['l-29'].attrib = {'L': 'FOR-ALL'}
    global_elements['category84'] = ET.SubElement(global_elements['compu-method12'], 'category')
    global_elements['category84'].text = 'SCALE_LINEAR_AND_TEXTTABLE'
    global_elements['unit-ref10'] = ET.SubElement(global_elements['compu-method12'], 'unit-ref')
    global_elements['unit-ref10'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref10'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys11'] = ET.SubElement(global_elements['compu-method12'], 'compu-internal-to-phys')
    global_elements['compu-scales11'] = ET.SubElement(global_elements['compu-internal-to-phys11'], 'compu-scales')
    global_elements['compu-scale28'] = ET.SubElement(global_elements['compu-scales11'], 'compu-scale')
    global_elements['lower-limit49'] = ET.SubElement(global_elements['compu-scale28'], 'lower-limit')
    global_elements['lower-limit49'].text = '0'
    global_elements['upper-limit49'] = ET.SubElement(global_elements['compu-scale28'], 'upper-limit')
    global_elements['upper-limit49'].text = '7'
    global_elements['compu-rational-coeffs4'] = ET.SubElement(global_elements['compu-scale28'], 'compu-rational-coeffs')
    global_elements['compu-numerator4'] = ET.SubElement(global_elements['compu-rational-coeffs4'], 'compu-numerator')
    global_elements['v18'] = ET.SubElement(global_elements['compu-numerator4'], 'v')
    global_elements['v18'].text = '0'
    global_elements['v19'] = ET.SubElement(global_elements['compu-numerator4'], 'v')
    global_elements['v19'].text = '1'
    global_elements['compu-denominator4'] = ET.SubElement(global_elements['compu-rational-coeffs4'], 'compu-denominator')
    global_elements['v20'] = ET.SubElement(global_elements['compu-denominator4'], 'v')
    global_elements['v20'].text = '1'
    global_elements['compu-scale29'] = ET.SubElement(global_elements['compu-scales11'], 'compu-scale')
    global_elements['symbol3'] = ET.SubElement(global_elements['compu-scale29'], 'symbol')
    global_elements['symbol3'].text = 'abcd'
    global_elements['lower-limit50'] = ET.SubElement(global_elements['compu-scale29'], 'lower-limit')
    global_elements['lower-limit50'].text = '8'
    global_elements['upper-limit50'] = ET.SubElement(global_elements['compu-scale29'], 'upper-limit')
    global_elements['upper-limit50'].text = '8'
    global_elements['compu-const25'] = ET.SubElement(global_elements['compu-scale29'], 'compu-const')
    global_elements['vt25'] = ET.SubElement(global_elements['compu-const25'], 'vt')
    global_elements['vt25'].text = 'abcd'
    global_elements['compu-scale30'] = ET.SubElement(global_elements['compu-scales11'], 'compu-scale')
    global_elements['symbol4'] = ET.SubElement(global_elements['compu-scale30'], 'symbol')
    global_elements['symbol4'].text = 'abcd1'
    global_elements['lower-limit51'] = ET.SubElement(global_elements['compu-scale30'], 'lower-limit')
    global_elements['lower-limit51'].text = '9'
    global_elements['upper-limit51'] = ET.SubElement(global_elements['compu-scale30'], 'upper-limit')
    global_elements['upper-limit51'].text = '9'
    global_elements['compu-const26'] = ET.SubElement(global_elements['compu-scale30'], 'compu-const')
    global_elements['vt26'] = ET.SubElement(global_elements['compu-const26'], 'vt')
    global_elements['vt26'].text = 'abcd1'
    global_elements['compu-default-value2'] = ET.SubElement(global_elements['compu-internal-to-phys11'], 'compu-default-value')
    global_elements['v21'] = ET.SubElement(global_elements['compu-default-value2'], 'v')
    global_elements['v21'].text = '8'

def TAB_NOINTP_CompuMethod():
    global_elements['compu-method13'] = ET.SubElement(global_elements['elements16'], 'compu-method')
    global_elements['compu-method13'].attrib = {'UUID': 'd4a62613-2238-4523-b274-2677c5a2235a'}
    global_elements['short-name370'] = ET.SubElement(global_elements['compu-method13'], 'short-name')
    global_elements['short-name370'].text = 'TAB_NOINTP_CompuMethod'
    global_elements['desc10'] = ET.SubElement(global_elements['compu-method13'], 'desc')
    global_elements['category85'] = ET.SubElement(global_elements['compu-method13'], 'category')
    global_elements['category85'].text = 'TAB_NOINTP'
    global_elements['unit-ref11'] = ET.SubElement(global_elements['compu-method13'], 'unit-ref')
    global_elements['unit-ref11'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref11'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys12'] = ET.SubElement(global_elements['compu-method13'], 'compu-internal-to-phys')
    global_elements['compu-scales12'] = ET.SubElement(global_elements['compu-internal-to-phys12'], 'compu-scales')
    global_elements['compu-scale31'] = ET.SubElement(global_elements['compu-scales12'], 'compu-scale')
    global_elements['desc11'] = ET.SubElement(global_elements['compu-scale31'], 'desc')
    global_elements['l-210'] = ET.SubElement(global_elements['desc11'], 'l-2')
    global_elements['l-210'].attrib = {'L': 'AA'}
    global_elements['lower-limit52'] = ET.SubElement(global_elements['compu-scale31'], 'lower-limit')
    global_elements['lower-limit52'].text = '0'
    global_elements['upper-limit52'] = ET.SubElement(global_elements['compu-scale31'], 'upper-limit')
    global_elements['upper-limit52'].text = '0'
    global_elements['compu-const27'] = ET.SubElement(global_elements['compu-scale31'], 'compu-const')
    global_elements['v22'] = ET.SubElement(global_elements['compu-const27'], 'v')
    global_elements['v22'].text = '10'
    global_elements['compu-scale32'] = ET.SubElement(global_elements['compu-scales12'], 'compu-scale')
    global_elements['lower-limit53'] = ET.SubElement(global_elements['compu-scale32'], 'lower-limit')
    global_elements['lower-limit53'].text = '1'
    global_elements['upper-limit53'] = ET.SubElement(global_elements['compu-scale32'], 'upper-limit')
    global_elements['upper-limit53'].text = '1'
    global_elements['compu-const28'] = ET.SubElement(global_elements['compu-scale32'], 'compu-const')
    global_elements['v23'] = ET.SubElement(global_elements['compu-const28'], 'v')
    global_elements['v23'].text = '9'
    global_elements['compu-scale33'] = ET.SubElement(global_elements['compu-scales12'], 'compu-scale')
    global_elements['lower-limit54'] = ET.SubElement(global_elements['compu-scale33'], 'lower-limit')
    global_elements['lower-limit54'].text = '2'
    global_elements['upper-limit54'] = ET.SubElement(global_elements['compu-scale33'], 'upper-limit')
    global_elements['upper-limit54'].text = '2'
    global_elements['compu-const29'] = ET.SubElement(global_elements['compu-scale33'], 'compu-const')
    global_elements['v24'] = ET.SubElement(global_elements['compu-const29'], 'v')
    global_elements['v24'].text = '8'
    global_elements['compu-default-value3'] = ET.SubElement(global_elements['compu-internal-to-phys12'], 'compu-default-value')
    global_elements['vf'] = ET.SubElement(global_elements['compu-default-value3'], 'vf')
    global_elements['vf'].text = '0'

def TEXTTABLE_CompuMethod():
    global_elements['compu-method14'] = ET.SubElement(global_elements['elements16'], 'compu-method')
    global_elements['compu-method14'].attrib = {'UUID': '6ef51214-688c-4e48-a115-d80fcf62bffc'}
    global_elements['short-name371'] = ET.SubElement(global_elements['compu-method14'], 'short-name')
    global_elements['short-name371'].text = 'TEXTTABLE_CompuMethod'
    global_elements['category86'] = ET.SubElement(global_elements['compu-method14'], 'category')
    global_elements['category86'].text = 'TEXTTABLE'
    global_elements['unit-ref12'] = ET.SubElement(global_elements['compu-method14'], 'unit-ref')
    global_elements['unit-ref12'].text = '/AUTOSAR/AUTOSAR_PhysicalUnits/Units/NoUnit'
    global_elements['unit-ref12'].attrib = {'DEST': 'UNIT'}
    global_elements['compu-internal-to-phys13'] = ET.SubElement(global_elements['compu-method14'], 'compu-internal-to-phys')
    global_elements['compu-scales13'] = ET.SubElement(global_elements['compu-internal-to-phys13'], 'compu-scales')
    global_elements['compu-scale34'] = ET.SubElement(global_elements['compu-scales13'], 'compu-scale')
    global_elements['symbol5'] = ET.SubElement(global_elements['compu-scale34'], 'symbol')
    global_elements['symbol5'].text = 'text1'
    global_elements['lower-limit55'] = ET.SubElement(global_elements['compu-scale34'], 'lower-limit')
    global_elements['lower-limit55'].text = '0'
    global_elements['upper-limit55'] = ET.SubElement(global_elements['compu-scale34'], 'upper-limit')
    global_elements['upper-limit55'].text = '0'
    global_elements['compu-const30'] = ET.SubElement(global_elements['compu-scale34'], 'compu-const')
    global_elements['vt27'] = ET.SubElement(global_elements['compu-const30'], 'vt')
    global_elements['vt27'].text = 'text1'
    global_elements['compu-scale35'] = ET.SubElement(global_elements['compu-scales13'], 'compu-scale')
    global_elements['symbol6'] = ET.SubElement(global_elements['compu-scale35'], 'symbol')
    global_elements['symbol6'].text = 'text2'
    global_elements['lower-limit56'] = ET.SubElement(global_elements['compu-scale35'], 'lower-limit')
    global_elements['lower-limit56'].text = '1'
    global_elements['upper-limit56'] = ET.SubElement(global_elements['compu-scale35'], 'upper-limit')
    global_elements['upper-limit56'].text = '1'
    global_elements['compu-const31'] = ET.SubElement(global_elements['compu-scale35'], 'compu-const')
    global_elements['vt28'] = ET.SubElement(global_elements['compu-const31'], 'vt')
    global_elements['vt28'].text = 'text2'
    global_elements['compu-scale36'] = ET.SubElement(global_elements['compu-scales13'], 'compu-scale')
    global_elements['symbol7'] = ET.SubElement(global_elements['compu-scale36'], 'symbol')
    global_elements['symbol7'].text = 'text3'
    global_elements['lower-limit57'] = ET.SubElement(global_elements['compu-scale36'], 'lower-limit')
    global_elements['lower-limit57'].text = '2'
    global_elements['upper-limit57'] = ET.SubElement(global_elements['compu-scale36'], 'upper-limit')
    global_elements['upper-limit57'].text = '2'
    global_elements['compu-const32'] = ET.SubElement(global_elements['compu-scale36'], 'compu-const')
    global_elements['vt29'] = ET.SubElement(global_elements['compu-const32'], 'vt')
    global_elements['vt29'].text = 'text3'
    global_elements['compu-scale37'] = ET.SubElement(global_elements['compu-scales13'], 'compu-scale')
    global_elements['symbol8'] = ET.SubElement(global_elements['compu-scale37'], 'symbol')
    global_elements['symbol8'].text = 'text4'
    global_elements['lower-limit58'] = ET.SubElement(global_elements['compu-scale37'], 'lower-limit')
    global_elements['lower-limit58'].text = '3'
    global_elements['upper-limit58'] = ET.SubElement(global_elements['compu-scale37'], 'upper-limit')
    global_elements['upper-limit58'].text = '3'
    global_elements['compu-const33'] = ET.SubElement(global_elements['compu-scale37'], 'compu-const')
    global_elements['vt30'] = ET.SubElement(global_elements['compu-const33'], 'vt')
    global_elements['vt30'].text = 'text4'
    global_elements['compu-default-value4'] = ET.SubElement(global_elements['compu-internal-to-phys13'], 'compu-default-value')
    global_elements['v25'] = ET.SubElement(global_elements['compu-default-value4'], 'v')
    global_elements['v25'].text = '0'

def ConstantSpecifications():
    global_elements['ar-package31'] = ET.SubElement(global_elements['ar-packages8'], 'ar-package')
    global_elements['short-name372'] = ET.SubElement(global_elements['ar-package31'], 'short-name')
    global_elements['short-name372'].text = 'ConstantSpecifications'
    global_elements['elements17'] = ET.SubElement(global_elements['ar-package31'], 'elements')
    global_elements['constant-specification'] = ET.SubElement(global_elements['elements17'], 'constant-specification')
    global_elements['constant-specification'].attrib = {'UUID': '5679b253-a22a-4532-8116-7ce8ac35a562'}
    global_elements['short-name373'] = ET.SubElement(global_elements['constant-specification'], 'short-name')
    global_elements['short-name373'].text = 'ApplicationSwComponentType_ExplicitInterRunnableVariable'
    global_elements['value-spec'] = ET.SubElement(global_elements['constant-specification'], 'value-spec')
    global_elements['numerical-value-specification'] = ET.SubElement(global_elements['value-spec'], 'numerical-value-specification')
    global_elements['short-label2'] = ET.SubElement(global_elements['numerical-value-specification'], 'short-label')
    global_elements['short-label2'].text = 'Value'
    global_elements['value'] = ET.SubElement(global_elements['numerical-value-specification'], 'value')
    global_elements['value'].text = '0'
    global_elements['constant-specification2'] = ET.SubElement(global_elements['elements17'], 'constant-specification')
    global_elements['constant-specification2'].attrib = {'UUID': '82a61fa2-2547-4ce8-a0d4-c583629db923'}
    global_elements['short-name374'] = ET.SubElement(global_elements['constant-specification2'], 'short-name')
    global_elements['short-name374'].text = 'ApplicationSwComponentType_SharedParameter'
    global_elements['value-spec2'] = ET.SubElement(global_elements['constant-specification2'], 'value-spec')
    global_elements['numerical-value-specification2'] = ET.SubElement(global_elements['value-spec2'], 'numerical-value-specification')
    global_elements['short-label3'] = ET.SubElement(global_elements['numerical-value-specification2'], 'short-label')
    global_elements['short-label3'].text = 'Value'
    global_elements['value2'] = ET.SubElement(global_elements['numerical-value-specification2'], 'value')
    global_elements['value2'].text = '5.5'
    global_elements['constant-specification3'] = ET.SubElement(global_elements['elements17'], 'constant-specification')
    global_elements['constant-specification3'].attrib = {'UUID': 'e3a2b67f-9cda-465d-8b6f-f31127e7b3a1'}
    global_elements['short-name375'] = ET.SubElement(global_elements['constant-specification3'], 'short-name')
    global_elements['short-name375'].text = 'ApplicationSwComponentType_StaticMemory'
    global_elements['value-spec3'] = ET.SubElement(global_elements['constant-specification3'], 'value-spec')
    global_elements['numerical-value-specification3'] = ET.SubElement(global_elements['value-spec3'], 'numerical-value-specification')
    global_elements['short-label4'] = ET.SubElement(global_elements['numerical-value-specification3'], 'short-label')
    global_elements['short-label4'].text = 'Value'
    global_elements['value3'] = ET.SubElement(global_elements['numerical-value-specification3'], 'value')
    global_elements['value3'].text = '9'
    global_elements['constant-specification4'] = ET.SubElement(global_elements['elements17'], 'constant-specification')
    global_elements['constant-specification4'].attrib = {'UUID': '3c303401-cc30-49f7-a7cb-0cf2844a3f18'}
    global_elements['short-name376'] = ET.SubElement(global_elements['constant-specification4'], 'short-name')
    global_elements['short-name376'].text = 'ConstantSpecification'


def ConstantTypeMappingSets():
    global_elements['ar-package32'] = ET.SubElement(global_elements['ar-packages8'], 'ar-package')
    global_elements['ar-package32'].attrib = {'UUID': '6fcb326d-7f82-4cd3-9429-fa90f212d1e8'}
    global_elements['short-name377'] = ET.SubElement(global_elements['ar-package32'], 'short-name')
    global_elements['short-name377'].text = 'ConstantTypeMappingSets'
    global_elements['elements18'] = ET.SubElement(global_elements['ar-package32'], 'elements')
    global_elements['constant-specification-mapping-set'] = ET.SubElement(global_elements['elements18'], 'constant-specification-mapping-set')
    global_elements['constant-specification-mapping-set'].attrib = {'UUID': '4f3bdbd1-af02-46e6-a3ba-411118807380'}
    global_elements['short-name378'] = ET.SubElement(global_elements['constant-specification-mapping-set'], 'short-name')
    global_elements['short-name378'].text = 'ConstantSpecificationMappingSet'

def DataConstr():
    global_elements['ar-package33'] = ET.SubElement(global_elements['ar-packages8'], 'ar-package')
    global_elements['ar-package33'].attrib = {'UUID': '5b7c99d1-d4ef-481b-95e4-0d6975de4f3b'}
    global_elements['short-name379'] = ET.SubElement(global_elements['ar-package33'], 'short-name')
    global_elements['short-name379'].text = 'DataConstr'
    global_elements['elements19'] = ET.SubElement(global_elements['ar-package33'], 'elements')
    global_elements['data-constr24'] = ET.SubElement(global_elements['elements19'], 'data-constr')
    global_elements['data-constr24'].attrib = {'UUID': '78b9384e-7f45-4396-b617-a03a03aaf3ce'}
    global_elements['short-name380'] = ET.SubElement(global_elements['data-constr24'], 'short-name')
    global_elements['short-name380'].text = 'DataConstr'
    global_elements['data-constr-rules24'] = ET.SubElement(global_elements['data-constr24'], 'data-constr-rules')
    global_elements['data-constr-rule24'] = ET.SubElement(global_elements['data-constr-rules24'], 'data-constr-rule')
    global_elements['constr-level'] = ET.SubElement(global_elements['data-constr-rule24'], 'constr-level')
    global_elements['constr-level'].text = '0'
    global_elements['phys-constrs'] = ET.SubElement(global_elements['data-constr-rule24'], 'phys-constrs')
    global_elements['lower-limit59'] = ET.SubElement(global_elements['phys-constrs'], 'lower-limit')
    global_elements['lower-limit59'].text = '0'
    global_elements['upper-limit59'] = ET.SubElement(global_elements['phys-constrs'], 'upper-limit')
    global_elements['upper-limit59'].text = '7'

def DataTypemappingSets():
    global_elements['ar-package34'] = ET.SubElement(global_elements['ar-packages8'], 'ar-package')
    global_elements['ar-package34'].attrib = {'UUID': '463cbb86-4f8e-463e-8bb3-dafc528ccbdf'}
    global_elements['short-name381'] = ET.SubElement(global_elements['ar-package34'], 'short-name')
    global_elements['short-name381'].text = 'DataTypemappingSets'
    global_elements['elements20'] = ET.SubElement(global_elements['ar-package34'], 'elements')
    global_elements['data-type-mapping-set'] = ET.SubElement(global_elements['elements20'], 'data-type-mapping-set')
    global_elements['data-type-mapping-set'].attrib = {'UUID': '84bab728-8c47-495c-a5d4-5290c3551358'}
    global_elements['short-name382'] = ET.SubElement(global_elements['data-type-mapping-set'], 'short-name')
    global_elements['short-name382'].text = 'DataTypeMappingSet'
    global_elements['data-type-maps'] = ET.SubElement(global_elements['data-type-mapping-set'], 'data-type-maps')
    global_elements['data-type-map'] = ET.SubElement(global_elements['data-type-maps'], 'data-type-map')
    global_elements['application-data-type-ref'] = ET.SubElement(global_elements['data-type-map'], 'application-data-type-ref')
    global_elements['application-data-type-ref'].text = '/SharedElements/ApplicationDataTypes/Array/ApplicationArrayDataType_Fixed'
    global_elements['application-data-type-ref'].attrib = {'DEST': 'APPLICATION-ARRAY-DATA-TYPE'}
    global_elements['implementation-data-type-ref19'] = ET.SubElement(global_elements['data-type-map'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref19'].text = '/SharedElements/ImplementationDataTypes/ARRAY_ImplementationDataType'
    global_elements['implementation-data-type-ref19'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['data-type-map2'] = ET.SubElement(global_elements['data-type-maps'], 'data-type-map')
    global_elements['application-data-type-ref2'] = ET.SubElement(global_elements['data-type-map2'], 'application-data-type-ref')
    global_elements['application-data-type-ref2'].text = '/SharedElements/ApplicationDataTypes/Record/ApplicationRecordDataType'
    global_elements['application-data-type-ref2'].attrib = {'DEST': 'APPLICATION-RECORD-DATA-TYPE'}
    global_elements['implementation-data-type-ref20'] = ET.SubElement(global_elements['data-type-map2'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref20'].text = '/SharedElements/ImplementationDataTypes/STRUCTURE_ImplementationDataType1'
    global_elements['implementation-data-type-ref20'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['data-type-map3'] = ET.SubElement(global_elements['data-type-maps'], 'data-type-map')
    global_elements['application-data-type-ref3'] = ET.SubElement(global_elements['data-type-map3'], 'application-data-type-ref')
    global_elements['application-data-type-ref3'].text = '/SharedElements/ApplicationDataTypes/Array/ApplicationArrayDataType_Variable'
    global_elements['application-data-type-ref3'].attrib = {'DEST': 'APPLICATION-ARRAY-DATA-TYPE'}
    global_elements['implementation-data-type-ref21'] = ET.SubElement(global_elements['data-type-map3'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref21'].text = '/SharedElements/ImplementationDataTypes/Struct_Array_ImplementationDataType'
    global_elements['implementation-data-type-ref21'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['data-type-map4'] = ET.SubElement(global_elements['data-type-maps'], 'data-type-map')
    global_elements['application-data-type-ref4'] = ET.SubElement(global_elements['data-type-map4'], 'application-data-type-ref')
    global_elements['application-data-type-ref4'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['application-data-type-ref4'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['implementation-data-type-ref22'] = ET.SubElement(global_elements['data-type-map4'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref22'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    global_elements['implementation-data-type-ref22'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def ARRAY_ImplementationDataType():
    global_elements['ar-package35'] = ET.SubElement(global_elements['ar-packages8'], 'ar-package')
    global_elements['short-name383'] = ET.SubElement(global_elements['ar-package35'], 'short-name')
    global_elements['short-name383'].text = 'ImplementationDataTypes'
    global_elements['elements21'] = ET.SubElement(global_elements['ar-package35'], 'elements')
    global_elements['implementation-data-type29'] = ET.SubElement(global_elements['elements21'], 'implementation-data-type')
    global_elements['implementation-data-type29'].attrib = {'UUID': '21f9a013-317d-4a6a-8c1d-cdc72f7df8f5'}
    global_elements['short-name384'] = ET.SubElement(global_elements['implementation-data-type29'], 'short-name')
    global_elements['short-name384'].text = 'ARRAY_ImplementationDataType'
    global_elements['category87'] = ET.SubElement(global_elements['implementation-data-type29'], 'category')
    global_elements['category87'].text = 'ARRAY'
    global_elements['sw-data-def-props48'] = ET.SubElement(global_elements['implementation-data-type29'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants48'] = ET.SubElement(global_elements['sw-data-def-props48'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional48'] = ET.SubElement(global_elements['sw-data-def-props-variants48'], 'sw-data-def-props-conditional')
    global_elements['sub-elements3'] = ET.SubElement(global_elements['implementation-data-type29'], 'sub-elements')
    global_elements['implementation-data-type-element8'] = ET.SubElement(global_elements['sub-elements3'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element8'].attrib = {'UUID': '5512b8b7-a43f-436f-bb18-47a903ad1e17'}
    global_elements['short-name385'] = ET.SubElement(global_elements['implementation-data-type-element8'], 'short-name')
    global_elements['short-name385'].text = 'SubElement'
    global_elements['category88'] = ET.SubElement(global_elements['implementation-data-type-element8'], 'category')
    global_elements['category88'].text = 'TYPE_REFERENCE'
    global_elements['array-size'] = ET.SubElement(global_elements['implementation-data-type-element8'], 'array-size')
    global_elements['array-size'].text = '15'
    global_elements['array-size-semantics4'] = ET.SubElement(global_elements['implementation-data-type-element8'], 'array-size-semantics')
    global_elements['array-size-semantics4'].text = 'FIXED-SIZE'
    global_elements['sw-data-def-props49'] = ET.SubElement(global_elements['implementation-data-type-element8'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants49'] = ET.SubElement(global_elements['sw-data-def-props49'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional49'] = ET.SubElement(global_elements['sw-data-def-props-variants49'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref23'] = ET.SubElement(global_elements['sw-data-def-props-conditional49'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref23'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    global_elements['implementation-data-type-ref23'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def ARRAY_ImplementationDataType1():
    global_elements['implementation-data-type30'] = ET.SubElement(global_elements['elements21'], 'implementation-data-type')
    global_elements['implementation-data-type30'].attrib = {'UUID': 'f01098ff-1c78-439e-9476-11d641870637'}
    global_elements['short-name386'] = ET.SubElement(global_elements['implementation-data-type30'], 'short-name')
    global_elements['short-name386'].text = 'ARRAY_ImplementationDataType1'
    global_elements['category89'] = ET.SubElement(global_elements['implementation-data-type30'], 'category')
    global_elements['category89'].text = 'ARRAY'
    global_elements['sub-elements4'] = ET.SubElement(global_elements['implementation-data-type30'], 'sub-elements')
    global_elements['implementation-data-type-element9'] = ET.SubElement(global_elements['sub-elements4'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element9'].attrib = {'UUID': 'ee36cc86-25eb-4048-8698-d1ec326fda32'}
    global_elements['short-name387'] = ET.SubElement(global_elements['implementation-data-type-element9'], 'short-name')
    global_elements['short-name387'].text = 'SubElement'
    global_elements['category90'] = ET.SubElement(global_elements['implementation-data-type-element9'], 'category')
    global_elements['category90'].text = 'TYPE_REFERENCE'
    global_elements['array-size2'] = ET.SubElement(global_elements['implementation-data-type-element9'], 'array-size')
    global_elements['array-size2'].text = '15'
    global_elements['array-size-semantics5'] = ET.SubElement(global_elements['implementation-data-type-element9'], 'array-size-semantics')
    global_elements['array-size-semantics5'].text = 'VARIABLE-SIZE'
    global_elements['sw-data-def-props50'] = ET.SubElement(global_elements['implementation-data-type-element9'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants50'] = ET.SubElement(global_elements['sw-data-def-props50'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional50'] = ET.SubElement(global_elements['sw-data-def-props-variants50'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref24'] = ET.SubElement(global_elements['sw-data-def-props-conditional50'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref24'].text = '/SharedElements/ImplementationDataTypes/STRUCTURE_ImplementationDataType1'
    global_elements['implementation-data-type-ref24'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def ImplementationDataType():
    global_elements['implementation-data-type31'] = ET.SubElement(global_elements['elements21'], 'implementation-data-type')
    global_elements['implementation-data-type31'].attrib = {'UUID': '77ef0bea-be4b-4dea-b5ea-114e5a3f3d26'}
    global_elements['short-name388'] = ET.SubElement(global_elements['implementation-data-type31'], 'short-name')
    global_elements['short-name388'].text = 'ImplementationDataType'
    global_elements['category91'] = ET.SubElement(global_elements['implementation-data-type31'], 'category')
    global_elements['category91'].text = 'VALUE'
    global_elements['sw-data-def-props51'] = ET.SubElement(global_elements['implementation-data-type31'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants51'] = ET.SubElement(global_elements['sw-data-def-props51'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional51'] = ET.SubElement(global_elements['sw-data-def-props-variants51'], 'sw-data-def-props-conditional')
    global_elements['base-type-ref14'] = ET.SubElement(global_elements['sw-data-def-props-conditional51'], 'base-type-ref')
    global_elements['base-type-ref14'].text = '/AUTOSAR/AUTOSAR_Platform/BaseTypes/uint8'
    global_elements['base-type-ref14'].attrib = {'DEST': 'SW-BASE-TYPE'}


def STRUCTURE_ImplementationDataType1():
    global_elements['implementation-data-type32'] = ET.SubElement(global_elements['elements21'], 'implementation-data-type')
    global_elements['implementation-data-type32'].attrib = {'UUID': '53ec3bfc-5a92-4d42-b31b-8e29e99a2b46'}
    global_elements['short-name389'] = ET.SubElement(global_elements['implementation-data-type32'], 'short-name')
    global_elements['short-name389'].text = 'STRUCTURE_ImplementationDataType1'
    global_elements['category92'] = ET.SubElement(global_elements['implementation-data-type32'], 'category')
    global_elements['category92'].text = 'STRUCTURE'
    global_elements['sub-elements5'] = ET.SubElement(global_elements['implementation-data-type32'], 'sub-elements')
    global_elements['implementation-data-type-element10'] = ET.SubElement(global_elements['sub-elements5'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element10'].attrib = {'UUID': '31f01782-3ce8-4dbe-81d1-0d5fb89bef99'}
    global_elements['short-name390'] = ET.SubElement(global_elements['implementation-data-type-element10'], 'short-name')
    global_elements['short-name390'].text = 'SubElement'
    global_elements['category93'] = ET.SubElement(global_elements['implementation-data-type-element10'], 'category')
    global_elements['category93'].text = 'TYPE_REFERENCE'
    global_elements['sw-data-def-props52'] = ET.SubElement(global_elements['implementation-data-type-element10'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants52'] = ET.SubElement(global_elements['sw-data-def-props52'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional52'] = ET.SubElement(global_elements['sw-data-def-props-variants52'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref25'] = ET.SubElement(global_elements['sw-data-def-props-conditional52'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref25'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    global_elements['implementation-data-type-ref25'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['implementation-data-type-element11'] = ET.SubElement(global_elements['sub-elements5'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element11'].attrib = {'UUID': '83bd06cb-a4ff-4d55-bd3d-1a691b582d46'}
    global_elements['short-name391'] = ET.SubElement(global_elements['implementation-data-type-element11'], 'short-name')
    global_elements['short-name391'].text = 'SubElement1'
    global_elements['category94'] = ET.SubElement(global_elements['implementation-data-type-element11'], 'category')
    global_elements['category94'].text = 'TYPE_REFERENCE'
    global_elements['sw-data-def-props53'] = ET.SubElement(global_elements['implementation-data-type-element11'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants53'] = ET.SubElement(global_elements['sw-data-def-props53'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional53'] = ET.SubElement(global_elements['sw-data-def-props-variants53'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref26'] = ET.SubElement(global_elements['sw-data-def-props-conditional53'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref26'].text = '/SharedElements/ImplementationDataTypes/ARRAY_ImplementationDataType'
    global_elements['implementation-data-type-ref26'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def Struct_Array_ImplementationDataType():
    global_elements['implementation-data-type33'] = ET.SubElement(global_elements['elements21'], 'implementation-data-type')
    global_elements['implementation-data-type33'].attrib = {'UUID': 'ccd15817-26a8-424d-8c87-3f3d70b5ee9d'}
    global_elements['short-name392'] = ET.SubElement(global_elements['implementation-data-type33'], 'short-name')
    global_elements['short-name392'].text = 'Struct_Array_ImplementationDataType'
    global_elements['category95'] = ET.SubElement(global_elements['implementation-data-type33'], 'category')
    global_elements['category95'].text = 'STRUCTURE'
    global_elements['sub-elements6'] = ET.SubElement(global_elements['implementation-data-type33'], 'sub-elements')
    global_elements['implementation-data-type-element12'] = ET.SubElement(global_elements['sub-elements6'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element12'].attrib = {'UUID': '3f61bc0d-d829-4ab0-9e22-7de6a25972e3'}
    global_elements['short-name393'] = ET.SubElement(global_elements['implementation-data-type-element12'], 'short-name')
    global_elements['short-name393'].text = 'SubElement1'
    global_elements['category96'] = ET.SubElement(global_elements['implementation-data-type-element12'], 'category')
    global_elements['category96'].text = 'TYPE_REFERENCE'
    global_elements['sw-data-def-props54'] = ET.SubElement(global_elements['implementation-data-type-element12'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants54'] = ET.SubElement(global_elements['sw-data-def-props54'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional54'] = ET.SubElement(global_elements['sw-data-def-props-variants54'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref27'] = ET.SubElement(global_elements['sw-data-def-props-conditional54'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref27'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['implementation-data-type-ref27'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['implementation-data-type-element13'] = ET.SubElement(global_elements['sub-elements6'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element13'].attrib = {'UUID': 'dc530c9c-3b65-4707-99c3-842e2d2b7788'}
    global_elements['short-name394'] = ET.SubElement(global_elements['implementation-data-type-element13'], 'short-name')
    global_elements['short-name394'].text = 'SubElement'
    global_elements['category97'] = ET.SubElement(global_elements['implementation-data-type-element13'], 'category')
    global_elements['category97'].text = 'ARRAY'
    global_elements['sub-elements7'] = ET.SubElement(global_elements['implementation-data-type-element13'], 'sub-elements')
    global_elements['implementation-data-type-element14'] = ET.SubElement(global_elements['sub-elements7'], 'implementation-data-type-element')
    global_elements['implementation-data-type-element14'].attrib = {'UUID': 'af21d788-9aea-4789-b7d0-8665f2d0c8c7'}
    global_elements['short-name395'] = ET.SubElement(global_elements['implementation-data-type-element14'], 'short-name')
    global_elements['short-name395'].text = 'SubElement'
    global_elements['category98'] = ET.SubElement(global_elements['implementation-data-type-element14'], 'category')
    global_elements['category98'].text = 'TYPE_REFERENCE'
    global_elements['array-size3'] = ET.SubElement(global_elements['implementation-data-type-element14'], 'array-size')
    global_elements['array-size3'].text = '15'
    global_elements['array-size-semantics6'] = ET.SubElement(global_elements['implementation-data-type-element14'], 'array-size-semantics')
    global_elements['array-size-semantics6'].text = 'VARIABLE-SIZE'
    global_elements['sw-data-def-props55'] = ET.SubElement(global_elements['implementation-data-type-element14'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants55'] = ET.SubElement(global_elements['sw-data-def-props55'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional55'] = ET.SubElement(global_elements['sw-data-def-props-variants55'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref28'] = ET.SubElement(global_elements['sw-data-def-props-conditional55'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref28'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint16'
    global_elements['implementation-data-type-ref28'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['sw-data-def-props56'] = ET.SubElement(global_elements['implementation-data-type-element13'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants56'] = ET.SubElement(global_elements['sw-data-def-props56'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional56'] = ET.SubElement(global_elements['sw-data-def-props-variants56'], 'sw-data-def-props-conditional')


def TypeTref_ImplementationDataType():
    global_elements['implementation-data-type34'] = ET.SubElement(global_elements['elements21'], 'implementation-data-type')
    global_elements['implementation-data-type34'].attrib = {'UUID': '79fa9e8f-a805-43da-b4b5-ac42d2a23ff0'}
    global_elements['short-name396'] = ET.SubElement(global_elements['implementation-data-type34'], 'short-name')
    global_elements['short-name396'].text = 'TypeTref_ImplementationDataType'
    global_elements['category99'] = ET.SubElement(global_elements['implementation-data-type34'], 'category')
    global_elements['category99'].text = 'TYPE_REFERENCE'
    global_elements['sw-data-def-props57'] = ET.SubElement(global_elements['implementation-data-type34'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants57'] = ET.SubElement(global_elements['sw-data-def-props57'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional57'] = ET.SubElement(global_elements['sw-data-def-props-variants57'], 'sw-data-def-props-conditional')
    global_elements['implementation-data-type-ref29'] = ET.SubElement(global_elements['sw-data-def-props-conditional57'], 'implementation-data-type-ref')
    global_elements['implementation-data-type-ref29'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float32'
    global_elements['implementation-data-type-ref29'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def ClientServer():
    global_elements['ar-package36'] = ET.SubElement(global_elements['ar-packages8'], 'ar-package')
    global_elements['short-name397'] = ET.SubElement(global_elements['ar-package36'], 'short-name')
    global_elements['short-name397'].text = 'PortInterfaces'
    global_elements['ar-packages10'] = ET.SubElement(global_elements['ar-package36'], 'ar-packages')
    global_elements['ar-package37'] = ET.SubElement(global_elements['ar-packages10'], 'ar-package')
    global_elements['ar-package37'].attrib = {'UUID': 'a0d0a13a-15e8-47a3-8169-5f11ad6c7d3f'}
    global_elements['short-name398'] = ET.SubElement(global_elements['ar-package37'], 'short-name')
    global_elements['short-name398'].text = 'ClientServer'
    global_elements['elements22'] = ET.SubElement(global_elements['ar-package37'], 'elements')
    global_elements['client-server-interface'] = ET.SubElement(global_elements['elements22'], 'client-server-interface')
    global_elements['client-server-interface'].attrib = {'UUID': 'de068aa3-6af8-4bad-a17f-893dbfa6d08d'}
    global_elements['short-name399'] = ET.SubElement(global_elements['client-server-interface'], 'short-name')
    global_elements['short-name399'].text = 'ClientServerInterface'
    global_elements['is-service'] = ET.SubElement(global_elements['client-server-interface'], 'is-service')
    global_elements['is-service'].text = 'false'
    global_elements['operations'] = ET.SubElement(global_elements['client-server-interface'], 'operations')
    global_elements['client-server-operation'] = ET.SubElement(global_elements['operations'], 'client-server-operation')
    global_elements['client-server-operation'].attrib = {'UUID': 'f963f5c2-07f7-439d-be71-e8ffb77736cb'}
    global_elements['short-name400'] = ET.SubElement(global_elements['client-server-operation'], 'short-name')
    global_elements['short-name400'].text = 'Operation'
    global_elements['arguments2'] = ET.SubElement(global_elements['client-server-operation'], 'arguments')
    global_elements['argument-data-prototype'] = ET.SubElement(global_elements['arguments2'], 'argument-data-prototype')
    global_elements['argument-data-prototype'].attrib = {'UUID': '0757643f-ef26-4951-9974-c0ad09b5c8d0'}
    global_elements['short-name401'] = ET.SubElement(global_elements['argument-data-prototype'], 'short-name')
    global_elements['short-name401'].text = 'Argument'
    global_elements['sw-data-def-props58'] = ET.SubElement(global_elements['argument-data-prototype'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants58'] = ET.SubElement(global_elements['sw-data-def-props58'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional58'] = ET.SubElement(global_elements['sw-data-def-props-variants58'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy3'] = ET.SubElement(global_elements['sw-data-def-props-conditional58'], 'sw-impl-policy')
    global_elements['sw-impl-policy3'].text = 'STANDARD'
    global_elements['type-tref5'] = ET.SubElement(global_elements['argument-data-prototype'], 'type-tref')
    global_elements['type-tref5'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref5'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['direction5'] = ET.SubElement(global_elements['argument-data-prototype'], 'direction')
    global_elements['direction5'].text = 'IN'
    global_elements['server-argument-impl-policy'] = ET.SubElement(global_elements['argument-data-prototype'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy'].text = 'USE-ARGUMENT-TYPE'
    global_elements['client-server-operation2'] = ET.SubElement(global_elements['operations'], 'client-server-operation')
    global_elements['client-server-operation2'].attrib = {'UUID': '9d946ffc-e827-4a3b-9217-80ae67bdce09'}
    global_elements['short-name402'] = ET.SubElement(global_elements['client-server-operation2'], 'short-name')
    global_elements['short-name402'].text = 'Operation1'
    global_elements['arguments3'] = ET.SubElement(global_elements['client-server-operation2'], 'arguments')
    global_elements['argument-data-prototype2'] = ET.SubElement(global_elements['arguments3'], 'argument-data-prototype')
    global_elements['argument-data-prototype2'].attrib = {'UUID': 'fbd7c03a-e379-467c-9efb-5818113f5e64'}
    global_elements['short-name403'] = ET.SubElement(global_elements['argument-data-prototype2'], 'short-name')
    global_elements['short-name403'].text = 'Argument'
    global_elements['sw-data-def-props59'] = ET.SubElement(global_elements['argument-data-prototype2'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants59'] = ET.SubElement(global_elements['sw-data-def-props59'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional59'] = ET.SubElement(global_elements['sw-data-def-props-variants59'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy4'] = ET.SubElement(global_elements['sw-data-def-props-conditional59'], 'sw-impl-policy')
    global_elements['sw-impl-policy4'].text = 'STANDARD'
    global_elements['type-tref6'] = ET.SubElement(global_elements['argument-data-prototype2'], 'type-tref')
    global_elements['type-tref6'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref6'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['direction6'] = ET.SubElement(global_elements['argument-data-prototype2'], 'direction')
    global_elements['direction6'].text = 'OUT'
    global_elements['server-argument-impl-policy2'] = ET.SubElement(global_elements['argument-data-prototype2'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy2'].text = 'USE-ARGUMENT-TYPE'

def Copy2_ClientServerInterface():
    global_elements['client-server-interface2'] = ET.SubElement(global_elements['elements22'], 'client-server-interface')
    global_elements['client-server-interface2'].attrib = {'UUID': '68861440-758d-43f6-92a2-fed7438de313'}
    global_elements['short-name404'] = ET.SubElement(global_elements['client-server-interface2'], 'short-name')
    global_elements['short-name404'].text = 'Copy2_ClientServerInterface'
    global_elements['is-service2'] = ET.SubElement(global_elements['client-server-interface2'], 'is-service')
    global_elements['is-service2'].text = 'false'
    global_elements['operations2'] = ET.SubElement(global_elements['client-server-interface2'], 'operations')
    global_elements['client-server-operation3'] = ET.SubElement(global_elements['operations2'], 'client-server-operation')
    global_elements['client-server-operation3'].attrib = {'UUID': 'dd8cf435-bddb-45bb-a59d-cffcdd11cedd'}
    global_elements['short-name405'] = ET.SubElement(global_elements['client-server-operation3'], 'short-name')
    global_elements['short-name405'].text = 'Operation'
    global_elements['arguments4'] = ET.SubElement(global_elements['client-server-operation3'], 'arguments')
    global_elements['argument-data-prototype3'] = ET.SubElement(global_elements['arguments4'], 'argument-data-prototype')
    global_elements['argument-data-prototype3'].attrib = {'UUID': '474b5949-0760-4780-9d06-6d2b549c40e3'}
    global_elements['short-name406'] = ET.SubElement(global_elements['argument-data-prototype3'], 'short-name')
    global_elements['short-name406'].text = 'Argument'
    global_elements['sw-data-def-props60'] = ET.SubElement(global_elements['argument-data-prototype3'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants60'] = ET.SubElement(global_elements['sw-data-def-props60'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional60'] = ET.SubElement(global_elements['sw-data-def-props-variants60'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy5'] = ET.SubElement(global_elements['sw-data-def-props-conditional60'], 'sw-impl-policy')
    global_elements['sw-impl-policy5'].text = 'STANDARD'
    global_elements['type-tref7'] = ET.SubElement(global_elements['argument-data-prototype3'], 'type-tref')
    global_elements['type-tref7'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref7'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['direction7'] = ET.SubElement(global_elements['argument-data-prototype3'], 'direction')
    global_elements['direction7'].text = 'IN'
    global_elements['server-argument-impl-policy3'] = ET.SubElement(global_elements['argument-data-prototype3'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy3'].text = 'USE-ARGUMENT-TYPE'
    global_elements['client-server-operation4'] = ET.SubElement(global_elements['operations2'], 'client-server-operation')
    global_elements['client-server-operation4'].attrib = {'UUID': 'ceba0008-a280-4915-acc8-c4b28afc10c4'}
    global_elements['short-name407'] = ET.SubElement(global_elements['client-server-operation4'], 'short-name')
    global_elements['short-name407'].text = 'Operation1'
    global_elements['arguments5'] = ET.SubElement(global_elements['client-server-operation4'], 'arguments')
    global_elements['argument-data-prototype4'] = ET.SubElement(global_elements['arguments5'], 'argument-data-prototype')
    global_elements['argument-data-prototype4'].attrib = {'UUID': '48e7b87f-8674-441c-bc3e-b6143e20802e'}
    global_elements['short-name408'] = ET.SubElement(global_elements['argument-data-prototype4'], 'short-name')
    global_elements['short-name408'].text = 'Argument'
    global_elements['sw-data-def-props61'] = ET.SubElement(global_elements['argument-data-prototype4'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants61'] = ET.SubElement(global_elements['sw-data-def-props61'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional61'] = ET.SubElement(global_elements['sw-data-def-props-variants61'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy6'] = ET.SubElement(global_elements['sw-data-def-props-conditional61'], 'sw-impl-policy')
    global_elements['sw-impl-policy6'].text = 'STANDARD'
    global_elements['type-tref8'] = ET.SubElement(global_elements['argument-data-prototype4'], 'type-tref')
    global_elements['type-tref8'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref8'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['direction8'] = ET.SubElement(global_elements['argument-data-prototype4'], 'direction')
    global_elements['direction8'].text = 'OUT'
    global_elements['server-argument-impl-policy4'] = ET.SubElement(global_elements['argument-data-prototype4'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy4'].text = 'USE-ARGUMENT-TYPE'

def Copy3_ClientServerInterface():
    global_elements['client-server-interface3'] = ET.SubElement(global_elements['elements22'], 'client-server-interface')
    global_elements['client-server-interface3'].attrib = {'UUID': '9b8ada7b-e7a9-49d6-a945-db726b3bd1f9'}
    global_elements['short-name409'] = ET.SubElement(global_elements['client-server-interface3'], 'short-name')
    global_elements['short-name409'].text = 'Copy3_ClientServerInterface'
    global_elements['is-service3'] = ET.SubElement(global_elements['client-server-interface3'], 'is-service')
    global_elements['is-service3'].text = 'false'
    global_elements['operations3'] = ET.SubElement(global_elements['client-server-interface3'], 'operations')
    global_elements['client-server-operation5'] = ET.SubElement(global_elements['operations3'], 'client-server-operation')
    global_elements['client-server-operation5'].attrib = {'UUID': '8b64e196-a577-4332-a8f2-8e907214f2ac'}
    global_elements['short-name410'] = ET.SubElement(global_elements['client-server-operation5'], 'short-name')
    global_elements['short-name410'].text = 'Operation'
    global_elements['arguments6'] = ET.SubElement(global_elements['client-server-operation5'], 'arguments')
    global_elements['argument-data-prototype5'] = ET.SubElement(global_elements['arguments6'], 'argument-data-prototype')
    global_elements['argument-data-prototype5'].attrib = {'UUID': 'cf106dae-c79b-4cea-a011-2d5ff268ac3e'}
    global_elements['short-name411'] = ET.SubElement(global_elements['argument-data-prototype5'], 'short-name')
    global_elements['short-name411'].text = 'Argument'
    global_elements['sw-data-def-props62'] = ET.SubElement(global_elements['argument-data-prototype5'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants62'] = ET.SubElement(global_elements['sw-data-def-props62'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional62'] = ET.SubElement(global_elements['sw-data-def-props-variants62'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy7'] = ET.SubElement(global_elements['sw-data-def-props-conditional62'], 'sw-impl-policy')
    global_elements['sw-impl-policy7'].text = 'STANDARD'
    global_elements['type-tref9'] = ET.SubElement(global_elements['argument-data-prototype5'], 'type-tref')
    global_elements['type-tref9'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref9'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['direction9'] = ET.SubElement(global_elements['argument-data-prototype5'], 'direction')
    global_elements['direction9'].text = 'IN'
    global_elements['server-argument-impl-policy5'] = ET.SubElement(global_elements['argument-data-prototype5'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy5'].text = 'USE-ARGUMENT-TYPE'
    global_elements['client-server-operation6'] = ET.SubElement(global_elements['operations3'], 'client-server-operation')
    global_elements['client-server-operation6'].attrib = {'UUID': '03f0b7d8-222c-465d-9663-185446b9f092'}
    global_elements['short-name412'] = ET.SubElement(global_elements['client-server-operation6'], 'short-name')
    global_elements['short-name412'].text = 'Operation1'
    global_elements['arguments7'] = ET.SubElement(global_elements['client-server-operation6'], 'arguments')
    global_elements['argument-data-prototype6'] = ET.SubElement(global_elements['arguments7'], 'argument-data-prototype')
    global_elements['argument-data-prototype6'].attrib = {'UUID': '9fe53cee-82db-4c74-887a-137d3260eae6'}
    global_elements['short-name413'] = ET.SubElement(global_elements['argument-data-prototype6'], 'short-name')
    global_elements['short-name413'].text = 'Argument'
    global_elements['sw-data-def-props63'] = ET.SubElement(global_elements['argument-data-prototype6'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants63'] = ET.SubElement(global_elements['sw-data-def-props63'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional63'] = ET.SubElement(global_elements['sw-data-def-props-variants63'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy8'] = ET.SubElement(global_elements['sw-data-def-props-conditional63'], 'sw-impl-policy')
    global_elements['sw-impl-policy8'].text = 'STANDARD'
    global_elements['type-tref10'] = ET.SubElement(global_elements['argument-data-prototype6'], 'type-tref')
    global_elements['type-tref10'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref10'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['direction10'] = ET.SubElement(global_elements['argument-data-prototype6'], 'direction')
    global_elements['direction10'].text = 'OUT'
    global_elements['server-argument-impl-policy6'] = ET.SubElement(global_elements['argument-data-prototype6'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy6'].text = 'USE-ARGUMENT-TYPE'

def Copy4_ClientServerInterface():
    global_elements['client-server-interface4'] = ET.SubElement(global_elements['elements22'], 'client-server-interface')
    global_elements['client-server-interface4'].attrib = {'UUID': 'bc94762b-35e3-49e1-ae8b-70bc63394d9c'}
    global_elements['short-name414'] = ET.SubElement(global_elements['client-server-interface4'], 'short-name')
    global_elements['short-name414'].text = 'Copy4_ClientServerInterface'
    global_elements['is-service4'] = ET.SubElement(global_elements['client-server-interface4'], 'is-service')
    global_elements['is-service4'].text = 'false'
    global_elements['operations4'] = ET.SubElement(global_elements['client-server-interface4'], 'operations')
    global_elements['client-server-operation7'] = ET.SubElement(global_elements['operations4'], 'client-server-operation')
    global_elements['client-server-operation7'].attrib = {'UUID': '4f953ec5-5e57-4a1c-bcf2-9eba8fde4ddd'}
    global_elements['short-name415'] = ET.SubElement(global_elements['client-server-operation7'], 'short-name')
    global_elements['short-name415'].text = 'Operation'
    global_elements['arguments8'] = ET.SubElement(global_elements['client-server-operation7'], 'arguments')
    global_elements['argument-data-prototype7'] = ET.SubElement(global_elements['arguments8'], 'argument-data-prototype')
    global_elements['argument-data-prototype7'].attrib = {'UUID': '573e55c4-304e-48a7-ae98-47c7744d4415'}
    global_elements['short-name416'] = ET.SubElement(global_elements['argument-data-prototype7'], 'short-name')
    global_elements['short-name416'].text = 'Argument'
    global_elements['sw-data-def-props64'] = ET.SubElement(global_elements['argument-data-prototype7'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants64'] = ET.SubElement(global_elements['sw-data-def-props64'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional64'] = ET.SubElement(global_elements['sw-data-def-props-variants64'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy9'] = ET.SubElement(global_elements['sw-data-def-props-conditional64'], 'sw-impl-policy')
    global_elements['sw-impl-policy9'].text = 'STANDARD'
    global_elements['type-tref11'] = ET.SubElement(global_elements['argument-data-prototype7'], 'type-tref')
    global_elements['type-tref11'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref11'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['direction11'] = ET.SubElement(global_elements['argument-data-prototype7'], 'direction')
    global_elements['direction11'].text = 'IN'
    global_elements['server-argument-impl-policy7'] = ET.SubElement(global_elements['argument-data-prototype7'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy7'].text = 'USE-ARGUMENT-TYPE'
    global_elements['client-server-operation8'] = ET.SubElement(global_elements['operations4'], 'client-server-operation')
    global_elements['client-server-operation8'].attrib = {'UUID': '32dd33c4-e167-4858-93d3-bc02d325d12c'}
    global_elements['short-name417'] = ET.SubElement(global_elements['client-server-operation8'], 'short-name')
    global_elements['short-name417'].text = 'Operation1'
    global_elements['arguments9'] = ET.SubElement(global_elements['client-server-operation8'], 'arguments')
    global_elements['argument-data-prototype8'] = ET.SubElement(global_elements['arguments9'], 'argument-data-prototype')
    global_elements['argument-data-prototype8'].attrib = {'UUID': '28cc5664-0a70-4275-b1a3-3cb7a40597db'}
    global_elements['short-name418'] = ET.SubElement(global_elements['argument-data-prototype8'], 'short-name')
    global_elements['short-name418'].text = 'Argument'
    global_elements['sw-data-def-props65'] = ET.SubElement(global_elements['argument-data-prototype8'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants65'] = ET.SubElement(global_elements['sw-data-def-props65'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional65'] = ET.SubElement(global_elements['sw-data-def-props-variants65'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy10'] = ET.SubElement(global_elements['sw-data-def-props-conditional65'], 'sw-impl-policy')
    global_elements['sw-impl-policy10'].text = 'STANDARD'
    global_elements['type-tref12'] = ET.SubElement(global_elements['argument-data-prototype8'], 'type-tref')
    global_elements['type-tref12'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref12'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['direction12'] = ET.SubElement(global_elements['argument-data-prototype8'], 'direction')
    global_elements['direction12'].text = 'OUT'
    global_elements['server-argument-impl-policy8'] = ET.SubElement(global_elements['argument-data-prototype8'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy8'].text = 'USE-ARGUMENT-TYPE'

def Copy_ClientServerInterface():
    global_elements['client-server-interface5'] = ET.SubElement(global_elements['elements22'], 'client-server-interface')
    global_elements['client-server-interface5'].attrib = {'UUID': 'ad797ff8-41de-49b7-a6c3-c2dd864f60dd'}
    global_elements['short-name419'] = ET.SubElement(global_elements['client-server-interface5'], 'short-name')
    global_elements['short-name419'].text = 'Copy_ClientServerInterface'
    global_elements['is-service5'] = ET.SubElement(global_elements['client-server-interface5'], 'is-service')
    global_elements['is-service5'].text = 'false'
    global_elements['operations5'] = ET.SubElement(global_elements['client-server-interface5'], 'operations')
    global_elements['client-server-operation9'] = ET.SubElement(global_elements['operations5'], 'client-server-operation')
    global_elements['client-server-operation9'].attrib = {'UUID': '5d536ac2-edd2-4788-b233-5b0ef32a2022'}
    global_elements['short-name420'] = ET.SubElement(global_elements['client-server-operation9'], 'short-name')
    global_elements['short-name420'].text = 'Operation'
    global_elements['arguments10'] = ET.SubElement(global_elements['client-server-operation9'], 'arguments')
    global_elements['argument-data-prototype9'] = ET.SubElement(global_elements['arguments10'], 'argument-data-prototype')
    global_elements['argument-data-prototype9'].attrib = {'UUID': '174674f0-498e-41bc-9667-2459277f62ea'}
    global_elements['short-name421'] = ET.SubElement(global_elements['argument-data-prototype9'], 'short-name')
    global_elements['short-name421'].text = 'Argument'
    global_elements['sw-data-def-props66'] = ET.SubElement(global_elements['argument-data-prototype9'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants66'] = ET.SubElement(global_elements['sw-data-def-props66'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional66'] = ET.SubElement(global_elements['sw-data-def-props-variants66'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy11'] = ET.SubElement(global_elements['sw-data-def-props-conditional66'], 'sw-impl-policy')
    global_elements['sw-impl-policy11'].text = 'STANDARD'
    global_elements['type-tref13'] = ET.SubElement(global_elements['argument-data-prototype9'], 'type-tref')
    global_elements['type-tref13'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref13'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['direction13'] = ET.SubElement(global_elements['argument-data-prototype9'], 'direction')
    global_elements['direction13'].text = 'IN'
    global_elements['server-argument-impl-policy9'] = ET.SubElement(global_elements['argument-data-prototype9'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy9'].text = 'USE-ARGUMENT-TYPE'

def Operation1():
    global_elements['client-server-operation10'] = ET.SubElement(global_elements['operations5'], 'client-server-operation')
    global_elements['client-server-operation10'].attrib = {'UUID': 'be00c41e-3412-411d-ad74-a6a0feee0ecd'}
    global_elements['short-name422'] = ET.SubElement(global_elements['client-server-operation10'], 'short-name')
    global_elements['short-name422'].text = 'Operation1'
    global_elements['arguments11'] = ET.SubElement(global_elements['client-server-operation10'], 'arguments')
    global_elements['argument-data-prototype10'] = ET.SubElement(global_elements['arguments11'], 'argument-data-prototype')
    global_elements['argument-data-prototype10'].attrib = {'UUID': '8c68ce17-1680-4ec1-951d-9d9c871aca06'}
    global_elements['short-name423'] = ET.SubElement(global_elements['argument-data-prototype10'], 'short-name')
    global_elements['short-name423'].text = 'Argument'
    global_elements['sw-data-def-props67'] = ET.SubElement(global_elements['argument-data-prototype10'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants67'] = ET.SubElement(global_elements['sw-data-def-props67'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional67'] = ET.SubElement(global_elements['sw-data-def-props-variants67'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy12'] = ET.SubElement(global_elements['sw-data-def-props-conditional67'], 'sw-impl-policy')
    global_elements['sw-impl-policy12'].text = 'STANDARD'
    global_elements['type-tref14'] = ET.SubElement(global_elements['argument-data-prototype10'], 'type-tref')
    global_elements['type-tref14'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref14'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['direction14'] = ET.SubElement(global_elements['argument-data-prototype10'], 'direction')
    global_elements['direction14'].text = 'OUT'
    global_elements['server-argument-impl-policy10'] = ET.SubElement(global_elements['argument-data-prototype10'], 'server-argument-impl-policy')
    global_elements['server-argument-impl-policy10'].text = 'USE-ARGUMENT-TYPE'

def ModeSwitch():
    global_elements['ar-package38'] = ET.SubElement(global_elements['ar-packages10'], 'ar-package')
    global_elements['ar-package38'].attrib = {'UUID': '3503a605-12c8-44be-96cf-4ad548d5d58f'}
    global_elements['short-name424'] = ET.SubElement(global_elements['ar-package38'], 'short-name')
    global_elements['short-name424'].text = 'ModeSwitch'
    global_elements['elements23'] = ET.SubElement(global_elements['ar-package38'], 'elements')
    global_elements['mode-declaration-group'] = ET.SubElement(global_elements['elements23'], 'mode-declaration-group')
    global_elements['mode-declaration-group'].attrib = {'UUID': 'd1db93d0-7154-468f-b3bc-872d23a7385f'}
    global_elements['short-name425'] = ET.SubElement(global_elements['mode-declaration-group'], 'short-name')
    global_elements['short-name425'].text = 'Copy_ModeDeclarationGroup'
    global_elements['category100'] = ET.SubElement(global_elements['mode-declaration-group'], 'category')
    global_elements['category100'].text = 'EXPLICIT_ORDER'
    global_elements['initial-mode-ref'] = ET.SubElement(global_elements['mode-declaration-group'], 'initial-mode-ref')
    global_elements['initial-mode-ref'].text = '/SharedElements/PortInterfaces/ModeSwitch/Copy_ModeDeclarationGroup/ModeDeclaration'
    global_elements['initial-mode-ref'].attrib = {'DEST': 'MODE-DECLARATION'}
    global_elements['mode-declarations'] = ET.SubElement(global_elements['mode-declaration-group'], 'mode-declarations')
    global_elements['mode-declaration'] = ET.SubElement(global_elements['mode-declarations'], 'mode-declaration')
    global_elements['mode-declaration'].attrib = {'UUID': '2608f59c-87b0-47b2-8cee-8e9c3ba94cac'}
    global_elements['short-name426'] = ET.SubElement(global_elements['mode-declaration'], 'short-name')
    global_elements['short-name426'].text = 'ModeDeclaration'
    global_elements['value4'] = ET.SubElement(global_elements['mode-declaration'], 'value')
    global_elements['value4'].text = '0'
    global_elements['mode-declaration2'] = ET.SubElement(global_elements['mode-declarations'], 'mode-declaration')
    global_elements['mode-declaration2'].attrib = {'UUID': '7cc2e588-342f-40a3-ad77-b3d49457e996'}
    global_elements['short-name427'] = ET.SubElement(global_elements['mode-declaration2'], 'short-name')
    global_elements['short-name427'].text = 'ModeDeclaration1'
    global_elements['value5'] = ET.SubElement(global_elements['mode-declaration2'], 'value')
    global_elements['value5'].text = '1'
    global_elements['mode-declaration3'] = ET.SubElement(global_elements['mode-declarations'], 'mode-declaration')
    global_elements['mode-declaration3'].attrib = {'UUID': '278335ee-b40e-4f50-9fc3-164297dafbfd'}
    global_elements['short-name428'] = ET.SubElement(global_elements['mode-declaration3'], 'short-name')
    global_elements['short-name428'].text = 'ModeDeclaration2'
    global_elements['value6'] = ET.SubElement(global_elements['mode-declaration3'], 'value')
    global_elements['value6'].text = '2'
    global_elements['on-transition-value'] = ET.SubElement(global_elements['mode-declaration-group'], 'on-transition-value')
    global_elements['on-transition-value'].text = '3'
    global_elements['mode-switch-interface'] = ET.SubElement(global_elements['elements23'], 'mode-switch-interface')
    global_elements['mode-switch-interface'].attrib = {'UUID': '359238c5-e830-44a4-b8a0-362c11b6864f'}
    global_elements['short-name429'] = ET.SubElement(global_elements['mode-switch-interface'], 'short-name')
    global_elements['short-name429'].text = 'Copy_ModeSwitchInterface'
    global_elements['is-service6'] = ET.SubElement(global_elements['mode-switch-interface'], 'is-service')
    global_elements['is-service6'].text = 'false'
    global_elements['mode-group'] = ET.SubElement(global_elements['mode-switch-interface'], 'mode-group')
    global_elements['mode-group'].attrib = {'UUID': '5de6bb25-e952-4b16-ad52-f4692d7da6d9'}
    global_elements['short-name430'] = ET.SubElement(global_elements['mode-group'], 'short-name')
    global_elements['short-name430'].text = 'ModeGroup'
    global_elements['type-tref15'] = ET.SubElement(global_elements['mode-group'], 'type-tref')
    global_elements['type-tref15'].text = '/SharedElements/PortInterfaces/ModeSwitch/Copy_ModeDeclarationGroup'
    global_elements['type-tref15'].attrib = {'DEST': 'MODE-DECLARATION-GROUP'}
    global_elements['mode-declaration-group2'] = ET.SubElement(global_elements['elements23'], 'mode-declaration-group')
    global_elements['mode-declaration-group2'].attrib = {'UUID': 'b9ed1cc5-6caf-43d0-b094-3c763b6cbb9a'}
    global_elements['short-name431'] = ET.SubElement(global_elements['mode-declaration-group2'], 'short-name')
    global_elements['short-name431'].text = 'ModeDeclarationGroup'
    global_elements['category101'] = ET.SubElement(global_elements['mode-declaration-group2'], 'category')
    global_elements['category101'].text = 'ALPHABETIC_ORDER'
    global_elements['initial-mode-ref2'] = ET.SubElement(global_elements['mode-declaration-group2'], 'initial-mode-ref')
    global_elements['initial-mode-ref2'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeDeclarationGroup/ModeDeclaration'
    global_elements['initial-mode-ref2'].attrib = {'DEST': 'MODE-DECLARATION'}
    global_elements['mode-declarations2'] = ET.SubElement(global_elements['mode-declaration-group2'], 'mode-declarations')
    global_elements['mode-declaration4'] = ET.SubElement(global_elements['mode-declarations2'], 'mode-declaration')
    global_elements['mode-declaration4'].attrib = {'UUID': 'c1fb19b0-d635-4deb-a718-37e3d20b8878'}
    global_elements['short-name432'] = ET.SubElement(global_elements['mode-declaration4'], 'short-name')
    global_elements['short-name432'].text = 'ModeDeclaration'
    global_elements['mode-declaration5'] = ET.SubElement(global_elements['mode-declarations2'], 'mode-declaration')
    global_elements['mode-declaration5'].attrib = {'UUID': 'a586eb27-c099-42ab-b553-a0fd227d1fe5'}
    global_elements['short-name433'] = ET.SubElement(global_elements['mode-declaration5'], 'short-name')
    global_elements['short-name433'].text = 'ModeDeclaration1'
    global_elements['mode-declaration6'] = ET.SubElement(global_elements['mode-declarations2'], 'mode-declaration')
    global_elements['mode-declaration6'].attrib = {'UUID': 'a891dd23-e1f6-41f0-b669-b383af7bd17e'}
    global_elements['short-name434'] = ET.SubElement(global_elements['mode-declaration6'], 'short-name')
    global_elements['short-name434'].text = 'ModeDeclaration2'
    global_elements['mode-switch-interface2'] = ET.SubElement(global_elements['elements23'], 'mode-switch-interface')
    global_elements['mode-switch-interface2'].attrib = {'UUID': '949dcf4f-08eb-4d99-8504-1c613d93f5e9'}
    global_elements['short-name435'] = ET.SubElement(global_elements['mode-switch-interface2'], 'short-name')
    global_elements['short-name435'].text = 'ModeSwitchInterface'
    global_elements['is-service7'] = ET.SubElement(global_elements['mode-switch-interface2'], 'is-service')
    global_elements['is-service7'].text = 'false'
    global_elements['mode-group2'] = ET.SubElement(global_elements['mode-switch-interface2'], 'mode-group')
    global_elements['mode-group2'].attrib = {'UUID': '26ede937-ce36-4065-93e5-d8bca12d51cd'}
    global_elements['short-name436'] = ET.SubElement(global_elements['mode-group2'], 'short-name')
    global_elements['short-name436'].text = 'ModeGroup'
    global_elements['type-tref16'] = ET.SubElement(global_elements['mode-group2'], 'type-tref')
    global_elements['type-tref16'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeDeclarationGroup'
    global_elements['type-tref16'].attrib = {'DEST': 'MODE-DECLARATION-GROUP'}


def NvData():
    global_elements['ar-package39'] = ET.SubElement(global_elements['ar-packages10'], 'ar-package')
    global_elements['ar-package39'].attrib = {'UUID': '07677b4a-bc79-4c7b-afa1-581ad642a3dd'}
    global_elements['short-name437'] = ET.SubElement(global_elements['ar-package39'], 'short-name')
    global_elements['short-name437'].text = 'NvData'
    global_elements['elements24'] = ET.SubElement(global_elements['ar-package39'], 'elements')
    global_elements['nv-data-interface'] = ET.SubElement(global_elements['elements24'], 'nv-data-interface')
    global_elements['nv-data-interface'].attrib = {'UUID': '8a4989b3-88e2-4e47-b98f-591e75c76b17'}
    global_elements['short-name438'] = ET.SubElement(global_elements['nv-data-interface'], 'short-name')
    global_elements['short-name438'].text = 'NvDataInterface'
    global_elements['is-service8'] = ET.SubElement(global_elements['nv-data-interface'], 'is-service')
    global_elements['is-service8'].text = 'false'
    global_elements['nv-datas'] = ET.SubElement(global_elements['nv-data-interface'], 'nv-datas')
    global_elements['variable-data-prototype'] = ET.SubElement(global_elements['nv-datas'], 'variable-data-prototype')
    global_elements['variable-data-prototype'].attrib = {'UUID': '8a84bf2f-0e49-4923-bbc2-7a6606812ef4'}
    global_elements['short-name439'] = ET.SubElement(global_elements['variable-data-prototype'], 'short-name')
    global_elements['short-name439'].text = 'NvData'
    global_elements['sw-data-def-props68'] = ET.SubElement(global_elements['variable-data-prototype'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants68'] = ET.SubElement(global_elements['sw-data-def-props68'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional68'] = ET.SubElement(global_elements['sw-data-def-props-variants68'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy13'] = ET.SubElement(global_elements['sw-data-def-props-conditional68'], 'sw-impl-policy')
    global_elements['sw-impl-policy13'].text = 'STANDARD'
    global_elements['type-tref17'] = ET.SubElement(global_elements['variable-data-prototype'], 'type-tref')
    global_elements['type-tref17'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref17'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['variable-data-prototype2'] = ET.SubElement(global_elements['nv-datas'], 'variable-data-prototype')
    global_elements['variable-data-prototype2'].attrib = {'UUID': '4437f330-788c-4fb4-92e5-9545dfdbd9f0'}
    global_elements['short-name440'] = ET.SubElement(global_elements['variable-data-prototype2'], 'short-name')
    global_elements['short-name440'].text = 'NvData1'
    global_elements['sw-data-def-props69'] = ET.SubElement(global_elements['variable-data-prototype2'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants69'] = ET.SubElement(global_elements['sw-data-def-props69'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional69'] = ET.SubElement(global_elements['sw-data-def-props-variants69'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy14'] = ET.SubElement(global_elements['sw-data-def-props-conditional69'], 'sw-impl-policy')
    global_elements['sw-impl-policy14'].text = 'STANDARD'
    global_elements['type-tref18'] = ET.SubElement(global_elements['variable-data-prototype2'], 'type-tref')
    global_elements['type-tref18'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float64'
    global_elements['type-tref18'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Parameter():
    global_elements['ar-package40'] = ET.SubElement(global_elements['ar-packages10'], 'ar-package')
    global_elements['ar-package40'].attrib = {'UUID': '9b48ec34-87aa-4f84-9080-1d3f919ca090'}
    global_elements['short-name441'] = ET.SubElement(global_elements['ar-package40'], 'short-name')
    global_elements['short-name441'].text = 'Parameter'
    global_elements['elements25'] = ET.SubElement(global_elements['ar-package40'], 'elements')
    global_elements['parameter-interface'] = ET.SubElement(global_elements['elements25'], 'parameter-interface')
    global_elements['parameter-interface'].attrib = {'UUID': '618ca0ee-adf8-43c1-b898-33ea5ca916d8'}
    global_elements['short-name442'] = ET.SubElement(global_elements['parameter-interface'], 'short-name')
    global_elements['short-name442'].text = 'ParameterInterface'
    global_elements['is-service9'] = ET.SubElement(global_elements['parameter-interface'], 'is-service')
    global_elements['is-service9'].text = 'false'
    global_elements['parameters'] = ET.SubElement(global_elements['parameter-interface'], 'parameters')
    global_elements['parameter-data-prototype'] = ET.SubElement(global_elements['parameters'], 'parameter-data-prototype')
    global_elements['parameter-data-prototype'].attrib = {'UUID': 'd359a294-51b2-461a-b7fb-0de80cf2598a'}
    global_elements['short-name443'] = ET.SubElement(global_elements['parameter-data-prototype'], 'short-name')
    global_elements['short-name443'].text = 'Parameter'
    global_elements['sw-data-def-props70'] = ET.SubElement(global_elements['parameter-data-prototype'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants70'] = ET.SubElement(global_elements['sw-data-def-props70'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional70'] = ET.SubElement(global_elements['sw-data-def-props-variants70'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access5'] = ET.SubElement(global_elements['sw-data-def-props-conditional70'], 'sw-calibration-access')
    global_elements['sw-calibration-access5'].text = 'READ-WRITE'
    global_elements['sw-impl-policy15'] = ET.SubElement(global_elements['sw-data-def-props-conditional70'], 'sw-impl-policy')
    global_elements['sw-impl-policy15'].text = 'STANDARD'
    global_elements['type-tref19'] = ET.SubElement(global_elements['parameter-data-prototype'], 'type-tref')
    global_elements['type-tref19'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float32'
    global_elements['type-tref19'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['parameter-data-prototype2'] = ET.SubElement(global_elements['parameters'], 'parameter-data-prototype')
    global_elements['parameter-data-prototype2'].attrib = {'UUID': 'a60e4821-63b4-4fa4-9f04-983264b2a55f'}
    global_elements['short-name444'] = ET.SubElement(global_elements['parameter-data-prototype2'], 'short-name')
    global_elements['short-name444'].text = 'Parameter1'
    global_elements['sw-data-def-props71'] = ET.SubElement(global_elements['parameter-data-prototype2'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants71'] = ET.SubElement(global_elements['sw-data-def-props71'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional71'] = ET.SubElement(global_elements['sw-data-def-props-variants71'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access6'] = ET.SubElement(global_elements['sw-data-def-props-conditional71'], 'sw-calibration-access')
    global_elements['sw-calibration-access6'].text = 'READ-WRITE'
    global_elements['sw-impl-policy16'] = ET.SubElement(global_elements['sw-data-def-props-conditional71'], 'sw-impl-policy')
    global_elements['sw-impl-policy16'].text = 'STANDARD'
    global_elements['type-tref20'] = ET.SubElement(global_elements['parameter-data-prototype2'], 'type-tref')
    global_elements['type-tref20'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref20'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}


def SenderReceiver():
    global_elements['ar-package41'] = ET.SubElement(global_elements['ar-packages10'], 'ar-package')
    global_elements['ar-package41'].attrib = {'UUID': '304f7bbd-15e6-4f85-b22f-4b02c9a5631c'}
    global_elements['short-name445'] = ET.SubElement(global_elements['ar-package41'], 'short-name')
    global_elements['short-name445'].text = 'SenderReceiver'
    global_elements['elements26'] = ET.SubElement(global_elements['ar-package41'], 'elements')
    global_elements['sender-receiver-interface'] = ET.SubElement(global_elements['elements26'], 'sender-receiver-interface')
    global_elements['sender-receiver-interface'].attrib = {'UUID': '5301b51c-ab80-4717-880a-f53963ebb47d'}
    global_elements['short-name446'] = ET.SubElement(global_elements['sender-receiver-interface'], 'short-name')
    global_elements['short-name446'].text = 'Copy2_SenderReceiverInterface'
    global_elements['is-service10'] = ET.SubElement(global_elements['sender-receiver-interface'], 'is-service')
    global_elements['is-service10'].text = 'false'
    global_elements['data-elements'] = ET.SubElement(global_elements['sender-receiver-interface'], 'data-elements')
    global_elements['variable-data-prototype3'] = ET.SubElement(global_elements['data-elements'], 'variable-data-prototype')
    global_elements['variable-data-prototype3'].attrib = {'UUID': 'd071c034-64ed-44d0-81f0-a0735e373ce3'}
    global_elements['short-name447'] = ET.SubElement(global_elements['variable-data-prototype3'], 'short-name')
    global_elements['short-name447'].text = 'DataElement'
    global_elements['sw-data-def-props72'] = ET.SubElement(global_elements['variable-data-prototype3'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants72'] = ET.SubElement(global_elements['sw-data-def-props72'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional72'] = ET.SubElement(global_elements['sw-data-def-props-variants72'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access7'] = ET.SubElement(global_elements['sw-data-def-props-conditional72'], 'sw-calibration-access')
    global_elements['sw-calibration-access7'].text = 'READ-WRITE'
    global_elements['sw-impl-policy17'] = ET.SubElement(global_elements['sw-data-def-props-conditional72'], 'sw-impl-policy')
    global_elements['sw-impl-policy17'].text = 'STANDARD'
    global_elements['type-tref21'] = ET.SubElement(global_elements['variable-data-prototype3'], 'type-tref')
    global_elements['type-tref21'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    global_elements['type-tref21'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['variable-data-prototype4'] = ET.SubElement(global_elements['data-elements'], 'variable-data-prototype')
    global_elements['variable-data-prototype4'].attrib = {'UUID': '3afe6629-f986-4006-9ecf-b2902644f64e'}
    global_elements['short-name448'] = ET.SubElement(global_elements['variable-data-prototype4'], 'short-name')
    global_elements['short-name448'].text = 'DataElement1'
    global_elements['sw-data-def-props73'] = ET.SubElement(global_elements['variable-data-prototype4'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants73'] = ET.SubElement(global_elements['sw-data-def-props73'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional73'] = ET.SubElement(global_elements['sw-data-def-props-variants73'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy18'] = ET.SubElement(global_elements['sw-data-def-props-conditional73'], 'sw-impl-policy')
    global_elements['sw-impl-policy18'].text = 'STANDARD'
    global_elements['type-tref22'] = ET.SubElement(global_elements['variable-data-prototype4'], 'type-tref')
    global_elements['type-tref22'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    global_elements['type-tref22'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy3_SenderReceiverInterface():
    global_elements['sender-receiver-interface2'] = ET.SubElement(global_elements['elements26'], 'sender-receiver-interface')
    global_elements['sender-receiver-interface2'].attrib = {'UUID': 'b4591ad1-c21f-4706-8eac-55f6169b8c96'}
    global_elements['short-name449'] = ET.SubElement(global_elements['sender-receiver-interface2'], 'short-name')
    global_elements['short-name449'].text = 'Copy3_SenderReceiverInterface'
    global_elements['is-service11'] = ET.SubElement(global_elements['sender-receiver-interface2'], 'is-service')
    global_elements['is-service11'].text = 'false'
    global_elements['data-elements2'] = ET.SubElement(global_elements['sender-receiver-interface2'], 'data-elements')
    global_elements['variable-data-prototype5'] = ET.SubElement(global_elements['data-elements2'], 'variable-data-prototype')
    global_elements['variable-data-prototype5'].attrib = {'UUID': 'dd322790-2f29-43dc-93a0-10c5addc7871'}
    global_elements['short-name450'] = ET.SubElement(global_elements['variable-data-prototype5'], 'short-name')
    global_elements['short-name450'].text = 'DataElement'
    global_elements['sw-data-def-props74'] = ET.SubElement(global_elements['variable-data-prototype5'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants74'] = ET.SubElement(global_elements['sw-data-def-props74'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional74'] = ET.SubElement(global_elements['sw-data-def-props-variants74'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access8'] = ET.SubElement(global_elements['sw-data-def-props-conditional74'], 'sw-calibration-access')
    global_elements['sw-calibration-access8'].text = 'READ-WRITE'
    global_elements['sw-impl-policy19'] = ET.SubElement(global_elements['sw-data-def-props-conditional74'], 'sw-impl-policy')
    global_elements['sw-impl-policy19'].text = 'STANDARD'
    global_elements['type-tref23'] = ET.SubElement(global_elements['variable-data-prototype5'], 'type-tref')
    global_elements['type-tref23'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    global_elements['type-tref23'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['variable-data-prototype6'] = ET.SubElement(global_elements['data-elements2'], 'variable-data-prototype')
    global_elements['variable-data-prototype6'].attrib = {'UUID': '27292aab-8793-404f-b1d0-3128a4ab29bf'}
    global_elements['short-name451'] = ET.SubElement(global_elements['variable-data-prototype6'], 'short-name')
    global_elements['short-name451'].text = 'DataElement1'
    global_elements['sw-data-def-props75'] = ET.SubElement(global_elements['variable-data-prototype6'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants75'] = ET.SubElement(global_elements['sw-data-def-props75'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional75'] = ET.SubElement(global_elements['sw-data-def-props-variants75'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy20'] = ET.SubElement(global_elements['sw-data-def-props-conditional75'], 'sw-impl-policy')
    global_elements['sw-impl-policy20'].text = 'STANDARD'
    global_elements['type-tref24'] = ET.SubElement(global_elements['variable-data-prototype6'], 'type-tref')
    global_elements['type-tref24'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    global_elements['type-tref24'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy4_SenderReceiverInterface():
    global_elements['sender-receiver-interface3'] = ET.SubElement(global_elements['elements26'], 'sender-receiver-interface')
    global_elements['sender-receiver-interface3'].attrib = {'UUID': 'e5b1f8fc-9e46-4d58-b278-cb3461917783'}
    global_elements['short-name452'] = ET.SubElement(global_elements['sender-receiver-interface3'], 'short-name')
    global_elements['short-name452'].text = 'Copy4_SenderReceiverInterface'
    global_elements['is-service12'] = ET.SubElement(global_elements['sender-receiver-interface3'], 'is-service')
    global_elements['is-service12'].text = 'false'
    global_elements['data-elements3'] = ET.SubElement(global_elements['sender-receiver-interface3'], 'data-elements')
    global_elements['variable-data-prototype7'] = ET.SubElement(global_elements['data-elements3'], 'variable-data-prototype')
    global_elements['variable-data-prototype7'].attrib = {'UUID': '81fa7709-76a3-4e64-8ab6-0302340d9596'}
    global_elements['short-name453'] = ET.SubElement(global_elements['variable-data-prototype7'], 'short-name')
    global_elements['short-name453'].text = 'DataElement'
    global_elements['sw-data-def-props76'] = ET.SubElement(global_elements['variable-data-prototype7'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants76'] = ET.SubElement(global_elements['sw-data-def-props76'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional76'] = ET.SubElement(global_elements['sw-data-def-props-variants76'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access9'] = ET.SubElement(global_elements['sw-data-def-props-conditional76'], 'sw-calibration-access')
    global_elements['sw-calibration-access9'].text = 'READ-WRITE'
    global_elements['sw-impl-policy21'] = ET.SubElement(global_elements['sw-data-def-props-conditional76'], 'sw-impl-policy')
    global_elements['sw-impl-policy21'].text = 'STANDARD'
    global_elements['type-tref25'] = ET.SubElement(global_elements['variable-data-prototype7'], 'type-tref')
    global_elements['type-tref25'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    global_elements['type-tref25'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['variable-data-prototype8'] = ET.SubElement(global_elements['data-elements3'], 'variable-data-prototype')
    global_elements['variable-data-prototype8'].attrib = {'UUID': '4139b239-b260-44f9-a1b9-26592a9702b7'}
    global_elements['short-name454'] = ET.SubElement(global_elements['variable-data-prototype8'], 'short-name')
    global_elements['short-name454'].text = 'DataElement1'
    global_elements['sw-data-def-props77'] = ET.SubElement(global_elements['variable-data-prototype8'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants77'] = ET.SubElement(global_elements['sw-data-def-props77'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional77'] = ET.SubElement(global_elements['sw-data-def-props-variants77'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy22'] = ET.SubElement(global_elements['sw-data-def-props-conditional77'], 'sw-impl-policy')
    global_elements['sw-impl-policy22'].text = 'STANDARD'
    global_elements['type-tref26'] = ET.SubElement(global_elements['variable-data-prototype8'], 'type-tref')
    global_elements['type-tref26'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    global_elements['type-tref26'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy5_SenderReceiverInterface():
    global_elements['sender-receiver-interface4'] = ET.SubElement(global_elements['elements26'], 'sender-receiver-interface')
    global_elements['sender-receiver-interface4'].attrib = {'UUID': '67583438-372e-4f89-aad7-44d221ba987e'}
    global_elements['short-name455'] = ET.SubElement(global_elements['sender-receiver-interface4'], 'short-name')
    global_elements['short-name455'].text = 'Copy5_SenderReceiverInterface'
    global_elements['is-service13'] = ET.SubElement(global_elements['sender-receiver-interface4'], 'is-service')
    global_elements['is-service13'].text = 'false'
    global_elements['data-elements4'] = ET.SubElement(global_elements['sender-receiver-interface4'], 'data-elements')
    global_elements['variable-data-prototype9'] = ET.SubElement(global_elements['data-elements4'], 'variable-data-prototype')
    global_elements['variable-data-prototype9'].attrib = {'UUID': 'b67450ea-eee7-49cd-9e1b-696114cdc06b'}
    global_elements['short-name456'] = ET.SubElement(global_elements['variable-data-prototype9'], 'short-name')
    global_elements['short-name456'].text = 'DataElement'
    global_elements['sw-data-def-props78'] = ET.SubElement(global_elements['variable-data-prototype9'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants78'] = ET.SubElement(global_elements['sw-data-def-props78'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional78'] = ET.SubElement(global_elements['sw-data-def-props-variants78'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access10'] = ET.SubElement(global_elements['sw-data-def-props-conditional78'], 'sw-calibration-access')
    global_elements['sw-calibration-access10'].text = 'READ-WRITE'
    global_elements['sw-impl-policy23'] = ET.SubElement(global_elements['sw-data-def-props-conditional78'], 'sw-impl-policy')
    global_elements['sw-impl-policy23'].text = 'STANDARD'
    global_elements['type-tref27'] = ET.SubElement(global_elements['variable-data-prototype9'], 'type-tref')
    global_elements['type-tref27'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    global_elements['type-tref27'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['variable-data-prototype10'] = ET.SubElement(global_elements['data-elements4'], 'variable-data-prototype')
    global_elements['variable-data-prototype10'].attrib = {'UUID': '6616174f-78ab-48e5-b54f-f0ac623eefa6'}
    global_elements['short-name457'] = ET.SubElement(global_elements['variable-data-prototype10'], 'short-name')
    global_elements['short-name457'].text = 'DataElement1'
    global_elements['sw-data-def-props79'] = ET.SubElement(global_elements['variable-data-prototype10'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants79'] = ET.SubElement(global_elements['sw-data-def-props79'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional79'] = ET.SubElement(global_elements['sw-data-def-props-variants79'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy24'] = ET.SubElement(global_elements['sw-data-def-props-conditional79'], 'sw-impl-policy')
    global_elements['sw-impl-policy24'].text = 'STANDARD'
    global_elements['type-tref28'] = ET.SubElement(global_elements['variable-data-prototype10'], 'type-tref')
    global_elements['type-tref28'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    global_elements['type-tref28'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def Copy_SenderReceiverInterface():
    global_elements['sender-receiver-interface5'] = ET.SubElement(global_elements['elements26'], 'sender-receiver-interface')
    global_elements['sender-receiver-interface5'].attrib = {'UUID': 'c0a51d5f-0a8c-4bdc-a77d-03a338508c6b'}
    global_elements['short-name458'] = ET.SubElement(global_elements['sender-receiver-interface5'], 'short-name')
    global_elements['short-name458'].text = 'Copy_SenderReceiverInterface'
    global_elements['is-service14'] = ET.SubElement(global_elements['sender-receiver-interface5'], 'is-service')
    global_elements['is-service14'].text = 'false'
    global_elements['data-elements5'] = ET.SubElement(global_elements['sender-receiver-interface5'], 'data-elements')
    global_elements['variable-data-prototype11'] = ET.SubElement(global_elements['data-elements5'], 'variable-data-prototype')
    global_elements['variable-data-prototype11'].attrib = {'UUID': 'b7a89eaf-844f-4e6d-b357-dc9976ba211e'}
    global_elements['short-name459'] = ET.SubElement(global_elements['variable-data-prototype11'], 'short-name')
    global_elements['short-name459'].text = 'DataElement'
    global_elements['sw-data-def-props80'] = ET.SubElement(global_elements['variable-data-prototype11'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants80'] = ET.SubElement(global_elements['sw-data-def-props80'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional80'] = ET.SubElement(global_elements['sw-data-def-props-variants80'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access11'] = ET.SubElement(global_elements['sw-data-def-props-conditional80'], 'sw-calibration-access')
    global_elements['sw-calibration-access11'].text = 'READ-WRITE'
    global_elements['sw-impl-policy25'] = ET.SubElement(global_elements['sw-data-def-props-conditional80'], 'sw-impl-policy')
    global_elements['sw-impl-policy25'].text = 'STANDARD'
    global_elements['type-tref29'] = ET.SubElement(global_elements['variable-data-prototype11'], 'type-tref')
    global_elements['type-tref29'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    global_elements['type-tref29'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['variable-data-prototype12'] = ET.SubElement(global_elements['data-elements5'], 'variable-data-prototype')
    global_elements['variable-data-prototype12'].attrib = {'UUID': '373c6d56-b664-4bba-b6bf-37630aed9fef'}
    global_elements['short-name460'] = ET.SubElement(global_elements['variable-data-prototype12'], 'short-name')
    global_elements['short-name460'].text = 'DataElement1'
    global_elements['sw-data-def-props81'] = ET.SubElement(global_elements['variable-data-prototype12'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants81'] = ET.SubElement(global_elements['sw-data-def-props81'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional81'] = ET.SubElement(global_elements['sw-data-def-props-variants81'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy26'] = ET.SubElement(global_elements['sw-data-def-props-conditional81'], 'sw-impl-policy')
    global_elements['sw-impl-policy26'].text = 'STANDARD'
    global_elements['type-tref30'] = ET.SubElement(global_elements['variable-data-prototype12'], 'type-tref')
    global_elements['type-tref30'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint32'
    global_elements['type-tref30'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}

def SenderReceiverInterface():
    global_elements['sender-receiver-interface6'] = ET.SubElement(global_elements['elements26'], 'sender-receiver-interface')
    global_elements['sender-receiver-interface6'].attrib = {'UUID': '5f56a3f5-0f22-429f-a8b9-003d68bbc759'}
    global_elements['short-name461'] = ET.SubElement(global_elements['sender-receiver-interface6'], 'short-name')
    global_elements['short-name461'].text = 'SenderReceiverInterface'
    global_elements['is-service15'] = ET.SubElement(global_elements['sender-receiver-interface6'], 'is-service')
    global_elements['is-service15'].text = 'false'
    global_elements['data-elements6'] = ET.SubElement(global_elements['sender-receiver-interface6'], 'data-elements')
    global_elements['variable-data-prototype13'] = ET.SubElement(global_elements['data-elements6'], 'variable-data-prototype')
    global_elements['variable-data-prototype13'].attrib = {'UUID': 'c448fbc4-20d2-443d-bb7a-87585742cfcf'}
    global_elements['short-name462'] = ET.SubElement(global_elements['variable-data-prototype13'], 'short-name')
    global_elements['short-name462'].text = 'DataElement'
    global_elements['sw-data-def-props82'] = ET.SubElement(global_elements['variable-data-prototype13'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants82'] = ET.SubElement(global_elements['sw-data-def-props82'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional82'] = ET.SubElement(global_elements['sw-data-def-props-variants82'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access12'] = ET.SubElement(global_elements['sw-data-def-props-conditional82'], 'sw-calibration-access')
    global_elements['sw-calibration-access12'].text = 'READ-WRITE'
    global_elements['sw-impl-policy27'] = ET.SubElement(global_elements['sw-data-def-props-conditional82'], 'sw-impl-policy')
    global_elements['sw-impl-policy27'].text = 'STANDARD'
    global_elements['type-tref31'] = ET.SubElement(global_elements['variable-data-prototype13'], 'type-tref')
    global_elements['type-tref31'].text = '/SharedElements/ApplicationDataTypes/Primitive/ApplicationPrimitiveDataType'
    global_elements['type-tref31'].attrib = {'DEST': 'APPLICATION-PRIMITIVE-DATA-TYPE'}
    global_elements['variable-data-prototype14'] = ET.SubElement(global_elements['data-elements6'], 'variable-data-prototype')
    global_elements['variable-data-prototype14'].attrib = {'UUID': '6862a5ea-8794-4906-9f54-50624e9d6044'}
    global_elements['short-name463'] = ET.SubElement(global_elements['variable-data-prototype14'], 'short-name')
    global_elements['short-name463'].text = 'DataElement1'
    global_elements['sw-data-def-props83'] = ET.SubElement(global_elements['variable-data-prototype14'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants83'] = ET.SubElement(global_elements['sw-data-def-props83'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional83'] = ET.SubElement(global_elements['sw-data-def-props-variants83'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy28'] = ET.SubElement(global_elements['sw-data-def-props-conditional83'], 'sw-impl-policy')
    global_elements['sw-impl-policy28'].text = 'STANDARD'
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
    global_elements['ar-package42'] = ET.SubElement(global_elements['ar-packages10'], 'ar-package')
    global_elements['ar-package42'].attrib = {'UUID': '00421379-584f-4dbb-8c9f-d70ad66b8e41'}
    global_elements['short-name464'] = ET.SubElement(global_elements['ar-package42'], 'short-name')
    global_elements['short-name464'].text = 'Trigger'
    global_elements['elements27'] = ET.SubElement(global_elements['ar-package42'], 'elements')
    global_elements['trigger-interface'] = ET.SubElement(global_elements['elements27'], 'trigger-interface')
    global_elements['trigger-interface'].attrib = {'UUID': '97d54491-56c6-49b9-9812-bb5eadaefa82'}
    global_elements['short-name465'] = ET.SubElement(global_elements['trigger-interface'], 'short-name')
    global_elements['short-name465'].text = 'TriggerInterface'
    global_elements['is-service16'] = ET.SubElement(global_elements['trigger-interface'], 'is-service')
    global_elements['is-service16'].text = 'false'
    global_elements['triggers'] = ET.SubElement(global_elements['trigger-interface'], 'triggers')
    global_elements['trigger'] = ET.SubElement(global_elements['triggers'], 'trigger')
    global_elements['trigger'].attrib = {'UUID': '06d545dc-664d-45fb-be23-8a076bded4b5'}
    global_elements['short-name466'] = ET.SubElement(global_elements['trigger'], 'short-name')
    global_elements['short-name466'].text = 'Trigger'
    global_elements['sw-impl-policy29'] = ET.SubElement(global_elements['trigger'], 'sw-impl-policy')
    global_elements['sw-impl-policy29'].text = 'STANDARD'
    global_elements['trigger-period'] = ET.SubElement(global_elements['trigger'], 'trigger-period')
    global_elements['cse-code'] = ET.SubElement(global_elements['trigger-period'], 'cse-code')
    global_elements['cse-code'].text = '6'
    global_elements['cse-code-factor'] = ET.SubElement(global_elements['trigger-period'], 'cse-code-factor')
    global_elements['cse-code-factor'].text = '15'

def SWCImpl():
    global_elements['ar-package43'] = ET.SubElement(global_elements['ar-packages8'], 'ar-package')
    global_elements['ar-package43'].attrib = {'UUID': 'a21c4095-c5dd-41b4-8a15-aa23a460a3e9'}
    global_elements['short-name467'] = ET.SubElement(global_elements['ar-package43'], 'short-name')
    global_elements['short-name467'].text = 'SWCImpl'
    global_elements['elements28'] = ET.SubElement(global_elements['ar-package43'], 'elements')
    global_elements['swc-implementation'] = ET.SubElement(global_elements['elements28'], 'swc-implementation')
    global_elements['swc-implementation'].attrib = {'UUID': 'a8e1b9bd-bc2d-4bba-8d84-7fb588da487b'}
    global_elements['short-name468'] = ET.SubElement(global_elements['swc-implementation'], 'short-name')
    global_elements['short-name468'].text = 'SwcImplementation'
    global_elements['programming-language'] = ET.SubElement(global_elements['swc-implementation'], 'programming-language')
    global_elements['programming-language'].text = 'C'
    global_elements['resource-consumption'] = ET.SubElement(global_elements['swc-implementation'], 'resource-consumption')
    global_elements['resource-consumption'].attrib = {'UUID': '664bf3d9-9efc-49d1-a4fd-9936922aa5f9'}
    global_elements['short-name469'] = ET.SubElement(global_elements['resource-consumption'], 'short-name')
    global_elements['short-name469'].text = 'ResourceConsumption'
    global_elements['sw-version'] = ET.SubElement(global_elements['swc-implementation'], 'sw-version')
    global_elements['sw-version'].text = '1.0.0.0'
    global_elements['behavior-ref'] = ET.SubElement(global_elements['swc-implementation'], 'behavior-ref')
    global_elements['behavior-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl'
    global_elements['behavior-ref'].attrib = {'DEST': 'SWC-INTERNAL-BEHAVIOR'}
    global_elements['ar-package44'] = ET.SubElement(global_elements['ar-packages8'], 'ar-package')
    global_elements['ar-package44'].attrib = {'UUID': 'fc8b946c-31d4-49d6-8e0c-ff6847ede7f5'}
    global_elements['short-name470'] = ET.SubElement(global_elements['ar-package44'], 'short-name')
    global_elements['short-name470'].text = 'SwAddrMethods'
    global_elements['elements29'] = ET.SubElement(global_elements['ar-package44'], 'elements')
    global_elements['sw-addr-method'] = ET.SubElement(global_elements['elements29'], 'sw-addr-method')
    global_elements['sw-addr-method'].attrib = {'UUID': '8a973d95-6644-4157-ab41-c78f7ccbcb2c'}
    global_elements['short-name471'] = ET.SubElement(global_elements['sw-addr-method'], 'short-name')
    global_elements['short-name471'].text = 'Copy2_SwAddrMethod'
    global_elements['memory-allocation-keyword-policy'] = ET.SubElement(global_elements['sw-addr-method'], 'memory-allocation-keyword-policy')
    global_elements['memory-allocation-keyword-policy'].text = 'ADDR-METHOD-SHORT-NAME'
    global_elements['section-type'] = ET.SubElement(global_elements['sw-addr-method'], 'section-type')
    global_elements['section-type'].text = 'CODE'
    global_elements['sw-addr-method2'] = ET.SubElement(global_elements['elements29'], 'sw-addr-method')
    global_elements['sw-addr-method2'].attrib = {'UUID': '73ccfb92-d7eb-4aee-b724-b520ed1a3e84'}
    global_elements['short-name472'] = ET.SubElement(global_elements['sw-addr-method2'], 'short-name')
    global_elements['short-name472'].text = 'Copy_SwAddrMethod'
    global_elements['memory-allocation-keyword-policy2'] = ET.SubElement(global_elements['sw-addr-method2'], 'memory-allocation-keyword-policy')
    global_elements['memory-allocation-keyword-policy2'].text = 'ADDR-METHOD-SHORT-NAME-AND-ALIGNMENT'
    global_elements['section-type2'] = ET.SubElement(global_elements['sw-addr-method2'], 'section-type')
    global_elements['section-type2'].text = 'CALIBRATION-VARIABLES'
    global_elements['sw-addr-method3'] = ET.SubElement(global_elements['elements29'], 'sw-addr-method')
    global_elements['sw-addr-method3'].attrib = {'UUID': '59a8a159-68d8-4804-8d3b-76f1a5d48b3c'}
    global_elements['short-name473'] = ET.SubElement(global_elements['sw-addr-method3'], 'short-name')
    global_elements['short-name473'].text = 'SwAddrMethod'
    global_elements['memory-allocation-keyword-policy3'] = ET.SubElement(global_elements['sw-addr-method3'], 'memory-allocation-keyword-policy')
    global_elements['memory-allocation-keyword-policy3'].text = 'ADDR-METHOD-SHORT-NAME'
    global_elements['section-type3'] = ET.SubElement(global_elements['sw-addr-method3'], 'section-type')
    global_elements['section-type3'].text = 'CALIBRATION-VARIABLES'


def SwComponentTypes():
    global_elements['ar-package45'] = ET.SubElement(global_elements['ar-packages'], 'ar-package')
    global_elements['short-name474'] = ET.SubElement(global_elements['ar-package45'], 'short-name')
    global_elements['short-name474'].text = 'SwComponentTypes'
    global_elements['ar-packages11'] = ET.SubElement(global_elements['ar-package45'], 'ar-packages')
    global_elements['ar-package46'] = ET.SubElement(global_elements['ar-packages11'], 'ar-package')
    global_elements['ar-package46'].attrib = {'UUID': '7e1cfec7-fc85-4615-9df0-46ddc1fdaa09'}
    global_elements['short-name475'] = ET.SubElement(global_elements['ar-package46'], 'short-name')
    global_elements['short-name475'].text = 'ApplSWC'
    global_elements['elements30'] = ET.SubElement(global_elements['ar-package46'], 'elements')
    global_elements['application-sw-component-type'] = ET.SubElement(global_elements['elements30'], 'application-sw-component-type')
    global_elements['application-sw-component-type'].attrib = {'UUID': 'e74b1e65-d39d-460c-8d4d-d95c8a9e12dd'}
    global_elements['short-name476'] = ET.SubElement(global_elements['application-sw-component-type'], 'short-name')
    global_elements['short-name476'].text = 'ApplicationSwComponentType'
    global_elements['ports'] = ET.SubElement(global_elements['application-sw-component-type'], 'ports')
    global_elements['r-port-prototype'] = ET.SubElement(global_elements['ports'], 'r-port-prototype')
    global_elements['r-port-prototype'].attrib = {'UUID': '1ecadefd-df18-4c05-a2d5-803778e62ae1'}
    global_elements['short-name477'] = ET.SubElement(global_elements['r-port-prototype'], 'short-name')
    global_elements['short-name477'].text = 'RPort_SR'
    global_elements['required-interface-tref'] = ET.SubElement(global_elements['r-port-prototype'], 'required-interface-tref')
    global_elements['required-interface-tref'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface'
    global_elements['required-interface-tref'].attrib = {'DEST': 'SENDER-RECEIVER-INTERFACE'}
    global_elements['p-port-prototype'] = ET.SubElement(global_elements['ports'], 'p-port-prototype')
    global_elements['p-port-prototype'].attrib = {'UUID': 'a3e8969f-1dde-4749-af9a-f337b0f053d8'}
    global_elements['short-name478'] = ET.SubElement(global_elements['p-port-prototype'], 'short-name')
    global_elements['short-name478'].text = 'PPort_SR'
    global_elements['provided-interface-tref'] = ET.SubElement(global_elements['p-port-prototype'], 'provided-interface-tref')
    global_elements['provided-interface-tref'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface'
    global_elements['provided-interface-tref'].attrib = {'DEST': 'SENDER-RECEIVER-INTERFACE'}
    global_elements['r-port-prototype2'] = ET.SubElement(global_elements['ports'], 'r-port-prototype')
    global_elements['r-port-prototype2'].attrib = {'UUID': '933a7736-19ea-4662-8301-3fe9991367bc'}
    global_elements['short-name479'] = ET.SubElement(global_elements['r-port-prototype2'], 'short-name')
    global_elements['short-name479'].text = 'RPort_CS'
    global_elements['required-interface-tref2'] = ET.SubElement(global_elements['r-port-prototype2'], 'required-interface-tref')
    global_elements['required-interface-tref2'].text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface'
    global_elements['required-interface-tref2'].attrib = {'DEST': 'CLIENT-SERVER-INTERFACE'}
    global_elements['p-port-prototype2'] = ET.SubElement(global_elements['ports'], 'p-port-prototype')
    global_elements['p-port-prototype2'].attrib = {'UUID': '38b3145f-1dd8-4a0f-943b-2f6b2d0a4221'}
    global_elements['short-name480'] = ET.SubElement(global_elements['p-port-prototype2'], 'short-name')
    global_elements['short-name480'].text = 'PPort_CS'
    global_elements['provided-interface-tref2'] = ET.SubElement(global_elements['p-port-prototype2'], 'provided-interface-tref')
    global_elements['provided-interface-tref2'].text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface'
    global_elements['provided-interface-tref2'].attrib = {'DEST': 'CLIENT-SERVER-INTERFACE'}
    global_elements['r-port-prototype3'] = ET.SubElement(global_elements['ports'], 'r-port-prototype')
    global_elements['r-port-prototype3'].attrib = {'UUID': '08e53a34-e89a-4c1c-a2d4-9536c0e123af'}
    global_elements['short-name481'] = ET.SubElement(global_elements['r-port-prototype3'], 'short-name')
    global_elements['short-name481'].text = 'RPort_msi'
    global_elements['required-interface-tref3'] = ET.SubElement(global_elements['r-port-prototype3'], 'required-interface-tref')
    global_elements['required-interface-tref3'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface'
    global_elements['required-interface-tref3'].attrib = {'DEST': 'MODE-SWITCH-INTERFACE'}
    global_elements['p-port-prototype3'] = ET.SubElement(global_elements['ports'], 'p-port-prototype')
    global_elements['p-port-prototype3'].attrib = {'UUID': '8ed933c7-270b-45cf-8a3e-206782153f61'}
    global_elements['short-name482'] = ET.SubElement(global_elements['p-port-prototype3'], 'short-name')
    global_elements['short-name482'].text = 'PPort_msi'
    global_elements['provided-interface-tref3'] = ET.SubElement(global_elements['p-port-prototype3'], 'provided-interface-tref')
    global_elements['provided-interface-tref3'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface'
    global_elements['provided-interface-tref3'].attrib = {'DEST': 'MODE-SWITCH-INTERFACE'}
    global_elements['r-port-prototype4'] = ET.SubElement(global_elements['ports'], 'r-port-prototype')
    global_elements['r-port-prototype4'].attrib = {'UUID': '52c8bb91-6599-4bdd-a556-e2b22ab9c73b'}
    global_elements['short-name483'] = ET.SubElement(global_elements['r-port-prototype4'], 'short-name')
    global_elements['short-name483'].text = 'RPort_nvd'
    global_elements['required-interface-tref4'] = ET.SubElement(global_elements['r-port-prototype4'], 'required-interface-tref')
    global_elements['required-interface-tref4'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface'
    global_elements['required-interface-tref4'].attrib = {'DEST': 'NV-DATA-INTERFACE'}
    global_elements['p-port-prototype4'] = ET.SubElement(global_elements['ports'], 'p-port-prototype')
    global_elements['p-port-prototype4'].attrib = {'UUID': 'a69f810c-0a9d-4729-9b49-5b4be2f55ffa'}
    global_elements['short-name484'] = ET.SubElement(global_elements['p-port-prototype4'], 'short-name')
    global_elements['short-name484'].text = 'PPort_nvd'
    global_elements['provided-interface-tref4'] = ET.SubElement(global_elements['p-port-prototype4'], 'provided-interface-tref')
    global_elements['provided-interface-tref4'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface'
    global_elements['provided-interface-tref4'].attrib = {'DEST': 'NV-DATA-INTERFACE'}
    global_elements['r-port-prototype5'] = ET.SubElement(global_elements['ports'], 'r-port-prototype')
    global_elements['r-port-prototype5'].attrib = {'UUID': '7bee2832-df48-4712-a0cf-9b2f095db921'}
    global_elements['short-name485'] = ET.SubElement(global_elements['r-port-prototype5'], 'short-name')
    global_elements['short-name485'].text = 'RPort_prm'
    global_elements['required-interface-tref5'] = ET.SubElement(global_elements['r-port-prototype5'], 'required-interface-tref')
    global_elements['required-interface-tref5'].text = '/SharedElements/PortInterfaces/Parameter/ParameterInterface'
    global_elements['required-interface-tref5'].attrib = {'DEST': 'PARAMETER-INTERFACE'}
    global_elements['r-port-prototype6'] = ET.SubElement(global_elements['ports'], 'r-port-prototype')
    global_elements['r-port-prototype6'].attrib = {'UUID': '9194fa9f-f535-4ef4-ad71-379f00251a5f'}
    global_elements['short-name486'] = ET.SubElement(global_elements['r-port-prototype6'], 'short-name')
    global_elements['short-name486'].text = 'RPort_trigger'
    global_elements['required-interface-tref6'] = ET.SubElement(global_elements['r-port-prototype6'], 'required-interface-tref')
    global_elements['required-interface-tref6'].text = '/SharedElements/PortInterfaces/Trigger/TriggerInterface'
    global_elements['required-interface-tref6'].attrib = {'DEST': 'TRIGGER-INTERFACE'}

def IB_Appl():
    global_elements['internal-behaviors'] = ET.SubElement(global_elements['application-sw-component-type'], 'internal-behaviors')
    global_elements['swc-internal-behavior'] = ET.SubElement(global_elements['internal-behaviors'], 'swc-internal-behavior')
    global_elements['swc-internal-behavior'].attrib = {'UUID': 'd0c29733-8863-4bcd-af6a-1579e0a29746'}
    global_elements['short-name487'] = ET.SubElement(global_elements['swc-internal-behavior'], 'short-name')
    global_elements['short-name487'].text = 'IB_Appl'
    global_elements['constant-memorys'] = ET.SubElement(global_elements['swc-internal-behavior'], 'constant-memorys')
    global_elements['parameter-data-prototype3'] = ET.SubElement(global_elements['constant-memorys'], 'parameter-data-prototype')
    global_elements['parameter-data-prototype3'].attrib = {'UUID': '666c53b0-408c-4084-8002-71810ad2bea7'}
    global_elements['short-name488'] = ET.SubElement(global_elements['parameter-data-prototype3'], 'short-name')
    global_elements['short-name488'].text = 'ConstantMemory'
    global_elements['sw-data-def-props84'] = ET.SubElement(global_elements['parameter-data-prototype3'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants84'] = ET.SubElement(global_elements['sw-data-def-props84'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional84'] = ET.SubElement(global_elements['sw-data-def-props-variants84'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access13'] = ET.SubElement(global_elements['sw-data-def-props-conditional84'], 'sw-calibration-access')
    global_elements['sw-calibration-access13'].text = 'READ-WRITE'
    global_elements['sw-impl-policy30'] = ET.SubElement(global_elements['sw-data-def-props-conditional84'], 'sw-impl-policy')
    global_elements['sw-impl-policy30'].text = 'STANDARD'
    global_elements['type-tref33'] = ET.SubElement(global_elements['parameter-data-prototype3'], 'type-tref')
    global_elements['type-tref33'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint64'
    global_elements['type-tref33'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value'] = ET.SubElement(global_elements['parameter-data-prototype3'], 'init-value')
    global_elements['numerical-value-specification4'] = ET.SubElement(global_elements['init-value'], 'numerical-value-specification')
    global_elements['short-label5'] = ET.SubElement(global_elements['numerical-value-specification4'], 'short-label')
    global_elements['short-label5'].text = 'Value'
    global_elements['value7'] = ET.SubElement(global_elements['numerical-value-specification4'], 'value')
    global_elements['value7'].text = '3'


def StaticMemory():
    global_elements['data-type-mapping-refs'] = ET.SubElement(global_elements['swc-internal-behavior'], 'data-type-mapping-refs')
    global_elements['data-type-mapping-ref'] = ET.SubElement(global_elements['data-type-mapping-refs'], 'data-type-mapping-ref')
    global_elements['data-type-mapping-ref'].text = '/SharedElements/DataTypemappingSets/DataTypeMappingSet'
    global_elements['data-type-mapping-ref'].attrib = {'DEST': 'DATA-TYPE-MAPPING-SET'}
    global_elements['static-memorys'] = ET.SubElement(global_elements['swc-internal-behavior'], 'static-memorys')
    global_elements['variable-data-prototype15'] = ET.SubElement(global_elements['static-memorys'], 'variable-data-prototype')
    global_elements['variable-data-prototype15'].attrib = {'UUID': '0a83fe83-959c-49d2-abf1-981ac4641b7d'}
    global_elements['short-name489'] = ET.SubElement(global_elements['variable-data-prototype15'], 'short-name')
    global_elements['short-name489'].text = 'StaticMemory'
    global_elements['sw-data-def-props85'] = ET.SubElement(global_elements['variable-data-prototype15'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants85'] = ET.SubElement(global_elements['sw-data-def-props85'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional85'] = ET.SubElement(global_elements['sw-data-def-props-variants85'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy31'] = ET.SubElement(global_elements['sw-data-def-props-conditional85'], 'sw-impl-policy')
    global_elements['sw-impl-policy31'].text = 'STANDARD'
    global_elements['type-tref34'] = ET.SubElement(global_elements['variable-data-prototype15'], 'type-tref')
    global_elements['type-tref34'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref34'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value2'] = ET.SubElement(global_elements['variable-data-prototype15'], 'init-value')
    global_elements['constant-reference'] = ET.SubElement(global_elements['init-value2'], 'constant-reference')
    global_elements['short-label6'] = ET.SubElement(global_elements['constant-reference'], 'short-label')
    global_elements['short-label6'].text = 'ReferenceToConstant'
    global_elements['constant-ref'] = ET.SubElement(global_elements['constant-reference'], 'constant-ref')
    global_elements['constant-ref'].text = '/SharedElements/ConstantSpecifications/ApplicationSwComponentType_StaticMemory'
    global_elements['constant-ref'].attrib = {'DEST': 'CONSTANT-SPECIFICATION'}

def ArTypedPerInstanceMemory():
    global_elements['ar-typed-per-instance-memorys'] = ET.SubElement(global_elements['swc-internal-behavior'], 'ar-typed-per-instance-memorys')
    global_elements['variable-data-prototype16'] = ET.SubElement(global_elements['ar-typed-per-instance-memorys'], 'variable-data-prototype')
    global_elements['variable-data-prototype16'].attrib = {'UUID': 'c2401b62-709c-4a61-a9d7-5f540d144075'}
    global_elements['short-name490'] = ET.SubElement(global_elements['variable-data-prototype16'], 'short-name')
    global_elements['short-name490'].text = 'ArTypedPerInstanceMemory'
    global_elements['sw-data-def-props86'] = ET.SubElement(global_elements['variable-data-prototype16'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants86'] = ET.SubElement(global_elements['sw-data-def-props86'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional86'] = ET.SubElement(global_elements['sw-data-def-props-variants86'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy32'] = ET.SubElement(global_elements['sw-data-def-props-conditional86'], 'sw-impl-policy')
    global_elements['sw-impl-policy32'].text = 'STANDARD'
    global_elements['type-tref35'] = ET.SubElement(global_elements['variable-data-prototype16'], 'type-tref')
    global_elements['type-tref35'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/sint16'
    global_elements['type-tref35'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value3'] = ET.SubElement(global_elements['variable-data-prototype16'], 'init-value')
    global_elements['numerical-value-specification5'] = ET.SubElement(global_elements['init-value3'], 'numerical-value-specification')
    global_elements['short-label7'] = ET.SubElement(global_elements['numerical-value-specification5'], 'short-label')
    global_elements['short-label7'].text = 'Value'
    global_elements['value8'] = ET.SubElement(global_elements['numerical-value-specification5'], 'value')
    global_elements['value8'].text = '-3'

def AsynchronousServerCallReturnsEvent():
    global_elements['events'] = ET.SubElement(global_elements['swc-internal-behavior'], 'events')
    global_elements['asynchronous-server-call-returns-event'] = ET.SubElement(global_elements['events'], 'asynchronous-server-call-returns-event')
    global_elements['asynchronous-server-call-returns-event'].attrib = {'UUID': '98e66756-7475-4549-94ba-bd68dca85e27'}
    global_elements['short-name491'] = ET.SubElement(global_elements['asynchronous-server-call-returns-event'], 'short-name')
    global_elements['short-name491'].text = 'AsynchronousServerCallReturnsEvent'
    global_elements['start-on-event-ref'] = ET.SubElement(global_elements['asynchronous-server-call-returns-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable'
    global_elements['start-on-event-ref'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['event-source-ref'] = ET.SubElement(global_elements['asynchronous-server-call-returns-event'], 'event-source-ref')
    global_elements['event-source-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable/AsynchronousServerCallResultPoint'
    global_elements['event-source-ref'].attrib = {'DEST': 'ASYNCHRONOUS-SERVER-CALL-RESULT-POINT'}
    global_elements['background-event'] = ET.SubElement(global_elements['events'], 'background-event')
    global_elements['background-event'].attrib = {'UUID': '878975ea-f390-4f62-a34f-05ca7fd73896'}
    global_elements['short-name492'] = ET.SubElement(global_elements['background-event'], 'short-name')
    global_elements['short-name492'].text = 'BackgroundEvent'
    global_elements['start-on-event-ref2'] = ET.SubElement(global_elements['background-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable1'
    global_elements['start-on-event-ref2'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['data-receive-error-event'] = ET.SubElement(global_elements['events'], 'data-receive-error-event')
    global_elements['data-receive-error-event'].attrib = {'UUID': '733de305-2dc6-4ac2-be25-134d242372ad'}
    global_elements['short-name493'] = ET.SubElement(global_elements['data-receive-error-event'], 'short-name')
    global_elements['short-name493'].text = 'DataReceiveErrorEvent'
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
    global_elements['data-received-event'] = ET.SubElement(global_elements['events'], 'data-received-event')
    global_elements['data-received-event'].attrib = {'UUID': '30fc9c83-5302-44fc-a25d-0d77e2b3d112'}
    global_elements['short-name494'] = ET.SubElement(global_elements['data-received-event'], 'short-name')
    global_elements['short-name494'].text = 'DataReceivedEvent'
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
    global_elements['data-send-completed-event'] = ET.SubElement(global_elements['events'], 'data-send-completed-event')
    global_elements['data-send-completed-event'].attrib = {'UUID': 'aefde323-2cf9-4226-aedb-0a1a33876a55'}
    global_elements['short-name495'] = ET.SubElement(global_elements['data-send-completed-event'], 'short-name')
    global_elements['short-name495'].text = 'DataSendCompletedEvent'
    global_elements['start-on-event-ref5'] = ET.SubElement(global_elements['data-send-completed-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref5'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable4'
    global_elements['start-on-event-ref5'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['event-source-ref2'] = ET.SubElement(global_elements['data-send-completed-event'], 'event-source-ref')
    global_elements['event-source-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable4/DSP_PPort_SR_DataElement'
    global_elements['event-source-ref2'].attrib = {'DEST': 'VARIABLE-ACCESS'}
    global_elements['data-write-completed-event'] = ET.SubElement(global_elements['events'], 'data-write-completed-event')
    global_elements['data-write-completed-event'].attrib = {'UUID': '0da70404-5ab6-4651-ad56-e1c3adab06e5'}
    global_elements['short-name496'] = ET.SubElement(global_elements['data-write-completed-event'], 'short-name')
    global_elements['short-name496'].text = 'DataWriteCompletedEvent'
    global_elements['start-on-event-ref6'] = ET.SubElement(global_elements['data-write-completed-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref6'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable5'
    global_elements['start-on-event-ref6'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['event-source-ref3'] = ET.SubElement(global_elements['data-write-completed-event'], 'event-source-ref')
    global_elements['event-source-ref3'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable5/DWA_PPort_SR_DataElement1'
    global_elements['event-source-ref3'].attrib = {'DEST': 'VARIABLE-ACCESS'}
    global_elements['external-trigger-occurred-event'] = ET.SubElement(global_elements['events'], 'external-trigger-occurred-event')
    global_elements['external-trigger-occurred-event'].attrib = {'UUID': '7f122189-5a69-4e28-af84-b5a1e73c9206'}
    global_elements['short-name497'] = ET.SubElement(global_elements['external-trigger-occurred-event'], 'short-name')
    global_elements['short-name497'].text = 'ExternalTriggerOccurredEvent'
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

    global_elements['init-event'] = ET.SubElement(global_elements['events'], 'init-event')
    global_elements['init-event'].attrib = {'UUID': '6febdb10-eefc-44b9-adad-fdef91bbef72'}
    global_elements['short-name498'] = ET.SubElement(global_elements['init-event'], 'short-name')
    global_elements['short-name498'].text = 'InitEvent'
    global_elements['start-on-event-ref8'] = ET.SubElement(global_elements['init-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref8'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable7'
    global_elements['start-on-event-ref8'].attrib = {'DEST': 'RUNNABLE-ENTITY'}

    global_elements['mode-switched-ack-event'] = ET.SubElement(global_elements['events'], 'mode-switched-ack-event')
    global_elements['mode-switched-ack-event'].attrib = {'UUID': '2f5c24be-60cf-4249-bfde-ceabef6d00d4'}
    global_elements['short-name499'] = ET.SubElement(global_elements['mode-switched-ack-event'], 'short-name')
    global_elements['short-name499'].text = 'ModeSwitchedAckEvent'
    global_elements['start-on-event-ref9'] = ET.SubElement(global_elements['mode-switched-ack-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref9'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable9'
    global_elements['start-on-event-ref9'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['event-source-ref4'] = ET.SubElement(global_elements['mode-switched-ack-event'], 'event-source-ref')
    global_elements['event-source-ref4'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable9/MSP_PPort_msi_ModeGroup'
    global_elements['event-source-ref4'].attrib = {'DEST': 'MODE-SWITCH-POINT'}
    global_elements['operation-invoked-event'] = ET.SubElement(global_elements['events'], 'operation-invoked-event')
    global_elements['operation-invoked-event'].attrib = {'UUID': '02646a86-1109-43a4-8e09-cb8878e932a5'}
    global_elements['short-name500'] = ET.SubElement(global_elements['operation-invoked-event'], 'short-name')
    global_elements['short-name500'].text = 'OperationInvokedEvent'
    global_elements['start-on-event-ref10'] = ET.SubElement(global_elements['operation-invoked-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref10'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable10'
    global_elements['start-on-event-ref10'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['operation-iref'] = ET.SubElement(global_elements['operation-invoked-event'], 'operation-iref')
    global_elements['context-p-port-ref'] = ET.SubElement(global_elements['operation-iref'], 'context-p-port-ref')
    global_elements['context-p-port-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_CS'
    global_elements['context-p-port-ref'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-provided-operation-ref'] = ET.SubElement(global_elements['operation-iref'], 'target-provided-operation-ref')
    global_elements['target-provided-operation-ref'].text = '/SharedElements/PortInterfaces/ClientServer/ClientServerInterface/Operation1'
    global_elements['target-provided-operation-ref'].attrib = {'DEST': 'CLIENT-SERVER-OPERATION'}

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
    
    global_elements['swc-mode-switch-event'] = ET.SubElement(global_elements['events'], 'swc-mode-switch-event')
    global_elements['swc-mode-switch-event'].attrib = {'UUID': '5bebf915-dc23-4d8d-ac15-4af9a83cb9f1'}
    global_elements['short-name502'] = ET.SubElement(global_elements['swc-mode-switch-event'], 'short-name')
    global_elements['short-name502'].text = 'SwcModeSwitchEvent'
    global_elements['start-on-event-ref12'] = ET.SubElement(global_elements['swc-mode-switch-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref12'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable12'
    global_elements['start-on-event-ref12'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
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
    global_elements['timing-event'] = ET.SubElement(global_elements['events'], 'timing-event')
    global_elements['timing-event'].attrib = {'UUID': 'a761b6cb-cd31-4a99-b2f8-21c5a132097e'}
    global_elements['short-name503'] = ET.SubElement(global_elements['timing-event'], 'short-name')
    global_elements['short-name503'].text = 'TimingEvent'
    global_elements['start-on-event-ref13'] = ET.SubElement(global_elements['timing-event'], 'start-on-event-ref')
    global_elements['start-on-event-ref13'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable13'
    global_elements['start-on-event-ref13'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['period'] = ET.SubElement(global_elements['timing-event'], 'period')
    global_elements['period'].text = '0.01'
    global_elements['timing-event2'] = ET.SubElement(global_elements['events'], 'timing-event')
    global_elements['timing-event2'].attrib = {'UUID': '0faaa505-7947-4b84-b8ea-4086fa60a54c'}
    global_elements['short-name504'] = ET.SubElement(global_elements['timing-event2'], 'short-name')
    global_elements['short-name504'].text = 'TimingEvent1'
    global_elements['start-on-event-ref14'] = ET.SubElement(global_elements['timing-event2'], 'start-on-event-ref')
    global_elements['start-on-event-ref14'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable15'
    global_elements['start-on-event-ref14'].attrib = {'DEST': 'RUNNABLE-ENTITY'}
    global_elements['period2'] = ET.SubElement(global_elements['timing-event2'], 'period')
    global_elements['period2'].text = '0.01'


def ExplicitInterRunnableVariable():
    global_elements['explicit-inter-runnable-variables'] = ET.SubElement(global_elements['swc-internal-behavior'], 'explicit-inter-runnable-variables')
    global_elements['variable-data-prototype17'] = ET.SubElement(global_elements['explicit-inter-runnable-variables'], 'variable-data-prototype')
    global_elements['variable-data-prototype17'].attrib = {'UUID': '46bf0c15-16f3-428f-92de-ce374a9faf1c'}
    global_elements['short-name505'] = ET.SubElement(global_elements['variable-data-prototype17'], 'short-name')
    global_elements['short-name505'].text = 'ExplicitInterRunnableVariable'
    global_elements['sw-data-def-props87'] = ET.SubElement(global_elements['variable-data-prototype17'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants87'] = ET.SubElement(global_elements['sw-data-def-props87'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional87'] = ET.SubElement(global_elements['sw-data-def-props-variants87'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy33'] = ET.SubElement(global_elements['sw-data-def-props-conditional87'], 'sw-impl-policy')
    global_elements['sw-impl-policy33'].text = 'STANDARD'
    global_elements['type-tref36'] = ET.SubElement(global_elements['variable-data-prototype17'], 'type-tref')
    global_elements['type-tref36'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/boolean'
    global_elements['type-tref36'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value4'] = ET.SubElement(global_elements['variable-data-prototype17'], 'init-value')
    global_elements['constant-reference2'] = ET.SubElement(global_elements['init-value4'], 'constant-reference')
    global_elements['short-label8'] = ET.SubElement(global_elements['constant-reference2'], 'short-label')
    global_elements['short-label8'].text = 'ReferenceToConstant'
    global_elements['constant-ref2'] = ET.SubElement(global_elements['constant-reference2'], 'constant-ref')
    global_elements['constant-ref2'].text = '/SharedElements/ConstantSpecifications/ApplicationSwComponentType_ExplicitInterRunnableVariable'
    global_elements['constant-ref2'].attrib = {'DEST': 'CONSTANT-SPECIFICATION'}

def ImplicitInterRunnableVariable():
    global_elements['handle-termination-and-restart'] = ET.SubElement(global_elements['swc-internal-behavior'], 'handle-termination-and-restart')
    global_elements['handle-termination-and-restart'].text = 'NO-SUPPORT'
    global_elements['implicit-inter-runnable-variables'] = ET.SubElement(global_elements['swc-internal-behavior'], 'implicit-inter-runnable-variables')
    global_elements['variable-data-prototype18'] = ET.SubElement(global_elements['implicit-inter-runnable-variables'], 'variable-data-prototype')
    global_elements['variable-data-prototype18'].attrib = {'UUID': '100df329-69ca-4527-945c-b23a59017964'}
    global_elements['short-name506'] = ET.SubElement(global_elements['variable-data-prototype18'], 'short-name')
    global_elements['short-name506'].text = 'ImplicitInterRunnableVariable'
    global_elements['sw-data-def-props88'] = ET.SubElement(global_elements['variable-data-prototype18'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants88'] = ET.SubElement(global_elements['sw-data-def-props88'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional88'] = ET.SubElement(global_elements['sw-data-def-props-variants88'], 'sw-data-def-props-conditional')
    global_elements['sw-impl-policy34'] = ET.SubElement(global_elements['sw-data-def-props-conditional88'], 'sw-impl-policy')
    global_elements['sw-impl-policy34'].text = 'STANDARD'
    global_elements['type-tref37'] = ET.SubElement(global_elements['variable-data-prototype18'], 'type-tref')
    global_elements['type-tref37'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/sint16'
    global_elements['type-tref37'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value5'] = ET.SubElement(global_elements['variable-data-prototype18'], 'init-value')
    global_elements['numerical-value-specification6'] = ET.SubElement(global_elements['init-value5'], 'numerical-value-specification')
    global_elements['short-label9'] = ET.SubElement(global_elements['numerical-value-specification6'], 'short-label')
    global_elements['short-label9'].text = 'Value'
    global_elements['value9'] = ET.SubElement(global_elements['numerical-value-specification6'], 'value')
    global_elements['value9'].text = '0'

def PerInstanceParameter():
    global_elements['per-instance-parameters'] = ET.SubElement(global_elements['swc-internal-behavior'], 'per-instance-parameters')
    global_elements['parameter-data-prototype4'] = ET.SubElement(global_elements['per-instance-parameters'], 'parameter-data-prototype')
    global_elements['parameter-data-prototype4'].attrib = {'UUID': 'a2509010-a816-4ea4-b0ed-c5ba10c3ca78'}
    global_elements['short-name507'] = ET.SubElement(global_elements['parameter-data-prototype4'], 'short-name')
    global_elements['short-name507'].text = 'PerInstanceParameter'
    global_elements['sw-data-def-props89'] = ET.SubElement(global_elements['parameter-data-prototype4'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants89'] = ET.SubElement(global_elements['sw-data-def-props89'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional89'] = ET.SubElement(global_elements['sw-data-def-props-variants89'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access14'] = ET.SubElement(global_elements['sw-data-def-props-conditional89'], 'sw-calibration-access')
    global_elements['sw-calibration-access14'].text = 'READ-WRITE'
    global_elements['sw-impl-policy35'] = ET.SubElement(global_elements['sw-data-def-props-conditional89'], 'sw-impl-policy')
    global_elements['sw-impl-policy35'].text = 'STANDARD'
    global_elements['type-tref38'] = ET.SubElement(global_elements['parameter-data-prototype4'], 'type-tref')
    global_elements['type-tref38'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/uint8'
    global_elements['type-tref38'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value6'] = ET.SubElement(global_elements['parameter-data-prototype4'], 'init-value')
    global_elements['numerical-value-specification7'] = ET.SubElement(global_elements['init-value6'], 'numerical-value-specification')
    global_elements['short-label10'] = ET.SubElement(global_elements['numerical-value-specification7'], 'short-label')
    global_elements['short-label10'].text = 'Value'
    global_elements['value10'] = ET.SubElement(global_elements['numerical-value-specification7'], 'value')
    global_elements['value10'].text = '5'
def Runnable():
    global_elements['runnables'] = ET.SubElement(global_elements['swc-internal-behavior'], 'runnables')
    global_elements['runnable-entity'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity'].attrib = {'UUID': 'bfb2d01b-9082-4a58-a929-6d7a860a2d9a'}
    global_elements['short-name508'] = ET.SubElement(global_elements['runnable-entity'], 'short-name')
    global_elements['short-name508'].text = 'Runnable'
    global_elements['minimum-start-interval'] = ET.SubElement(global_elements['runnable-entity'], 'minimum-start-interval')
    global_elements['minimum-start-interval'].text = '0'
    global_elements['sw-addr-method-ref'] = ET.SubElement(global_elements['runnable-entity'], 'sw-addr-method-ref')
    global_elements['sw-addr-method-ref'].text = '/SharedElements/SwAddrMethods/Copy2_SwAddrMethod'
    global_elements['sw-addr-method-ref'].attrib = {'DEST': 'SW-ADDR-METHOD'}
    global_elements['asynchronous-server-call-result-points'] = ET.SubElement(global_elements['runnable-entity'], 'asynchronous-server-call-result-points')
    global_elements['asynchronous-server-call-result-point'] = ET.SubElement(global_elements['asynchronous-server-call-result-points'], 'asynchronous-server-call-result-point')
    global_elements['asynchronous-server-call-result-point'].attrib = {'UUID': 'f857d505-3c25-43b2-b929-36e0e40f1177'}
    global_elements['short-name509'] = ET.SubElement(global_elements['asynchronous-server-call-result-point'], 'short-name')
    global_elements['short-name509'].text = 'AsynchronousServerCallResultPoint'
    global_elements['asynchronous-server-call-point-ref'] = ET.SubElement(global_elements['asynchronous-server-call-result-point'], 'asynchronous-server-call-point-ref')
    global_elements['asynchronous-server-call-point-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/Runnable/ASCP_RPort_CS_Operation'
    global_elements['asynchronous-server-call-point-ref'].attrib = {'DEST': 'ASYNCHRONOUS-SERVER-CALL-POINT'}
    global_elements['can-be-invoked-concurrently'] = ET.SubElement(global_elements['runnable-entity'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently'].text = 'false'
    global_elements['server-call-points'] = ET.SubElement(global_elements['runnable-entity'], 'server-call-points')
    global_elements['asynchronous-server-call-point'] = ET.SubElement(global_elements['server-call-points'], 'asynchronous-server-call-point')
    global_elements['asynchronous-server-call-point'].attrib = {'UUID': 'e7aacef3-56e7-4964-b0b6-5569dd4abc09'}
    global_elements['short-name510'] = ET.SubElement(global_elements['asynchronous-server-call-point'], 'short-name')
    global_elements['short-name510'].text = 'ASCP_RPort_CS_Operation'
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
    global_elements['runnable-entity2'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity2'].attrib = {'UUID': '4a40f3ec-f4dd-4ab0-8562-6a5174f2901e'}
    global_elements['short-name511'] = ET.SubElement(global_elements['runnable-entity2'], 'short-name')
    global_elements['short-name511'].text = 'Runnable1'
    global_elements['minimum-start-interval2'] = ET.SubElement(global_elements['runnable-entity2'], 'minimum-start-interval')
    global_elements['minimum-start-interval2'].text = '0'
    global_elements['can-be-invoked-concurrently2'] = ET.SubElement(global_elements['runnable-entity2'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently2'].text = 'false'

def ApplicationSwComponentType_Runnable():
    global_elements['symbol10'] = ET.SubElement(global_elements['runnable-entity2'], 'symbol')
    global_elements['symbol10'].text = 'ApplicationSwComponentType_Runnable1'
    global_elements['runnable-entity3'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity3'].attrib = {'UUID': '83eca00a-85d5-4f04-9573-3d997cd29b67'}
    global_elements['short-name512'] = ET.SubElement(global_elements['runnable-entity3'], 'short-name')
    global_elements['short-name512'].text = 'Runnable2'
    global_elements['minimum-start-interval3'] = ET.SubElement(global_elements['runnable-entity3'], 'minimum-start-interval')
    global_elements['minimum-start-interval3'].text = '0'
    global_elements['can-be-invoked-concurrently3'] = ET.SubElement(global_elements['runnable-entity3'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently3'].text = 'false'
    global_elements['symbol11'] = ET.SubElement(global_elements['runnable-entity3'], 'symbol')
    global_elements['symbol11'].text = 'ApplicationSwComponentType_Runnable2'
    global_elements['runnable-entity4'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity4'].attrib = {'UUID': '20bfd5e2-a118-4324-97fd-dcd5bf5f0a46'}
    global_elements['short-name513'] = ET.SubElement(global_elements['runnable-entity4'], 'short-name')
    global_elements['short-name513'].text = 'Runnable3'
    global_elements['minimum-start-interval4'] = ET.SubElement(global_elements['runnable-entity4'], 'minimum-start-interval')
    global_elements['minimum-start-interval4'].text = '0'
    global_elements['can-be-invoked-concurrently4'] = ET.SubElement(global_elements['runnable-entity4'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently4'].text = 'false'
    global_elements['symbol12'] = ET.SubElement(global_elements['runnable-entity4'], 'symbol')
    global_elements['symbol12'].text = 'ApplicationSwComponentType_Runnable3'
    global_elements['runnable-entity5'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity5'].attrib = {'UUID': 'ae315d13-a18a-4515-b02d-f1b207f85e47'}
    global_elements['short-name514'] = ET.SubElement(global_elements['runnable-entity5'], 'short-name')
    global_elements['short-name514'].text = 'Runnable4'
    global_elements['minimum-start-interval5'] = ET.SubElement(global_elements['runnable-entity5'], 'minimum-start-interval')
    global_elements['minimum-start-interval5'].text = '0'
    global_elements['can-be-invoked-concurrently5'] = ET.SubElement(global_elements['runnable-entity5'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently5'].text = 'false'
    global_elements['data-send-points'] = ET.SubElement(global_elements['runnable-entity5'], 'data-send-points')
    global_elements['variable-access'] = ET.SubElement(global_elements['data-send-points'], 'variable-access')
    global_elements['variable-access'].attrib = {'UUID': '2a04aecc-a1b6-494f-838e-29671adb5210'}
    global_elements['short-name515'] = ET.SubElement(global_elements['variable-access'], 'short-name')
    global_elements['short-name515'].text = 'DSP_PPort_SR_DataElement'
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
    global_elements['runnable-entity6'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity6'].attrib = {'UUID': '3ea0641c-9d79-4f93-8287-e34956b5c134'}
    global_elements['short-name516'] = ET.SubElement(global_elements['runnable-entity6'], 'short-name')
    global_elements['short-name516'].text = 'Runnable5'
    global_elements['minimum-start-interval6'] = ET.SubElement(global_elements['runnable-entity6'], 'minimum-start-interval')
    global_elements['minimum-start-interval6'].text = '0'
    global_elements['can-be-invoked-concurrently6'] = ET.SubElement(global_elements['runnable-entity6'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently6'].text = 'false'
    global_elements['data-write-accesss'] = ET.SubElement(global_elements['runnable-entity6'], 'data-write-accesss')
    global_elements['variable-access2'] = ET.SubElement(global_elements['data-write-accesss'], 'variable-access')
    global_elements['variable-access2'].attrib = {'UUID': '326a474d-8d28-41bc-bd9e-91de9802f682'}
    global_elements['short-name517'] = ET.SubElement(global_elements['variable-access2'], 'short-name')
    global_elements['short-name517'].text = 'DWA_PPort_SR_DataElement1'
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
    global_elements['runnable-entity7'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity7'].attrib = {'UUID': 'd7adad0b-22d1-4b37-9691-0677036197aa'}
    global_elements['short-name518'] = ET.SubElement(global_elements['runnable-entity7'], 'short-name')
    global_elements['short-name518'].text = 'Runnable6'
    global_elements['minimum-start-interval7'] = ET.SubElement(global_elements['runnable-entity7'], 'minimum-start-interval')
    global_elements['minimum-start-interval7'].text = '0'
    global_elements['can-be-invoked-concurrently7'] = ET.SubElement(global_elements['runnable-entity7'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently7'].text = 'false'
    global_elements['symbol15'] = ET.SubElement(global_elements['runnable-entity7'], 'symbol')
    global_elements['symbol15'].text = 'ApplicationSwComponentType_Runnable6'
    global_elements['runnable-entity8'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity8'].attrib = {'UUID': '98d30ebd-bbcb-4780-bc4a-27e6fd798a5a'}
    global_elements['short-name519'] = ET.SubElement(global_elements['runnable-entity8'], 'short-name')
    global_elements['short-name519'].text = 'Runnable7'
    global_elements['minimum-start-interval8'] = ET.SubElement(global_elements['runnable-entity8'], 'minimum-start-interval')
    global_elements['minimum-start-interval8'].text = '0'
    global_elements['can-be-invoked-concurrently8'] = ET.SubElement(global_elements['runnable-entity8'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently8'].text = 'false'
    global_elements['symbol16'] = ET.SubElement(global_elements['runnable-entity8'], 'symbol')
    global_elements['symbol16'].text = 'ApplicationSwComponentType_Runnable7'
    global_elements['runnable-entity9'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity9'].attrib = {'UUID': 'a6d9d7cb-1d57-45f2-b36a-1e1ab717fb1e'}
    global_elements['short-name520'] = ET.SubElement(global_elements['runnable-entity9'], 'short-name')
    global_elements['short-name520'].text = 'Runnable9'
    global_elements['minimum-start-interval9'] = ET.SubElement(global_elements['runnable-entity9'], 'minimum-start-interval')
    global_elements['minimum-start-interval9'].text = '0'
    global_elements['can-be-invoked-concurrently9'] = ET.SubElement(global_elements['runnable-entity9'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently9'].text = 'false'
    global_elements['mode-switch-points'] = ET.SubElement(global_elements['runnable-entity9'], 'mode-switch-points')
    global_elements['mode-switch-point'] = ET.SubElement(global_elements['mode-switch-points'], 'mode-switch-point')
    global_elements['mode-switch-point'].attrib = {'UUID': 'dd700e44-3e29-4b21-901f-c2e36c719f6a'}
    global_elements['short-name521'] = ET.SubElement(global_elements['mode-switch-point'], 'short-name')
    global_elements['short-name521'].text = 'MSP_PPort_msi_ModeGroup'
    global_elements['mode-group-iref2'] = ET.SubElement(global_elements['mode-switch-point'], 'mode-group-iref')
    global_elements['context-p-port-ref3'] = ET.SubElement(global_elements['mode-group-iref2'], 'context-p-port-ref')
    global_elements['context-p-port-ref3'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_msi'
    global_elements['context-p-port-ref3'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-mode-group-ref2'] = ET.SubElement(global_elements['mode-group-iref2'], 'target-mode-group-ref')
    global_elements['target-mode-group-ref2'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
    global_elements['target-mode-group-ref2'].attrib = {'DEST': 'MODE-DECLARATION-GROUP-PROTOTYPE'}
    global_elements['symbol17'] = ET.SubElement(global_elements['runnable-entity9'], 'symbol')
    global_elements['symbol17'].text = 'ApplicationSwComponentType_Runnable9'
    global_elements['runnable-entity10'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity10'].attrib = {'UUID': '3d515ac9-9c51-4cb8-a6af-ea16d3afd01d'}
    global_elements['short-name522'] = ET.SubElement(global_elements['runnable-entity10'], 'short-name')
    global_elements['short-name522'].text = 'Runnable10'
    global_elements['minimum-start-interval10'] = ET.SubElement(global_elements['runnable-entity10'], 'minimum-start-interval')
    global_elements['minimum-start-interval10'].text = '0'
    global_elements['can-be-invoked-concurrently10'] = ET.SubElement(global_elements['runnable-entity10'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently10'].text = 'false'
    global_elements['symbol18'] = ET.SubElement(global_elements['runnable-entity10'], 'symbol')
    global_elements['symbol18'].text = 'ApplicationSwComponentType_Runnable10'
    global_elements['runnable-entity11'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity11'].attrib = {'UUID': '9bddd887-575d-463b-b09d-d1b63ec1352b'}
    global_elements['short-name523'] = ET.SubElement(global_elements['runnable-entity11'], 'short-name')
    global_elements['short-name523'].text = 'Runnable11'
    global_elements['minimum-start-interval11'] = ET.SubElement(global_elements['runnable-entity11'], 'minimum-start-interval')
    global_elements['minimum-start-interval11'].text = '0'
    global_elements['can-be-invoked-concurrently11'] = ET.SubElement(global_elements['runnable-entity11'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently11'].text = 'false'
    global_elements['symbol19'] = ET.SubElement(global_elements['runnable-entity11'], 'symbol')
    global_elements['symbol19'].text = 'ApplicationSwComponentType_Runnable11'
    global_elements['runnable-entity12'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity12'].attrib = {'UUID': 'fa96688f-7ffe-4b3b-aa43-c124847e2efd'}
    global_elements['short-name524'] = ET.SubElement(global_elements['runnable-entity12'], 'short-name')
    global_elements['short-name524'].text = 'Runnable12'
    global_elements['minimum-start-interval12'] = ET.SubElement(global_elements['runnable-entity12'], 'minimum-start-interval')
    global_elements['minimum-start-interval12'].text = '0'
    global_elements['can-be-invoked-concurrently12'] = ET.SubElement(global_elements['runnable-entity12'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently12'].text = 'false'
    global_elements['symbol20'] = ET.SubElement(global_elements['runnable-entity12'], 'symbol')
    global_elements['symbol20'].text = 'ApplicationSwComponentType_Runnable12'
    global_elements['runnable-entity13'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity13'].attrib = {'UUID': 'e967670f-46d8-4d91-b4b9-62c85a17843e'}
    global_elements['short-name525'] = ET.SubElement(global_elements['runnable-entity13'], 'short-name')
    global_elements['short-name525'].text = 'Runnable13'
    global_elements['minimum-start-interval13'] = ET.SubElement(global_elements['runnable-entity13'], 'minimum-start-interval')
    global_elements['minimum-start-interval13'].text = '0'
    global_elements['can-be-invoked-concurrently13'] = ET.SubElement(global_elements['runnable-entity13'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently13'].text = 'false'

def DRA_RPort_SR_DataElement():
    global_elements['data-read-accesss'] = ET.SubElement(global_elements['runnable-entity13'], 'data-read-accesss')
    global_elements['variable-access3'] = ET.SubElement(global_elements['data-read-accesss'], 'variable-access')
    global_elements['variable-access3'].attrib = {'UUID': '9bf42611-5276-4ce4-92b5-36c024121479'}
    global_elements['short-name526'] = ET.SubElement(global_elements['variable-access3'], 'short-name')
    global_elements['short-name526'].text = 'DRA_RPort_SR_DataElement'
    global_elements['accessed-variable3'] = ET.SubElement(global_elements['variable-access3'], 'accessed-variable')
    global_elements['autosar-variable-iref3'] = ET.SubElement(global_elements['accessed-variable3'], 'autosar-variable-iref')
    global_elements['port-prototype-ref3'] = ET.SubElement(global_elements['autosar-variable-iref3'], 'port-prototype-ref')
    global_elements['port-prototype-ref3'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    global_elements['port-prototype-ref3'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref3'] = ET.SubElement(global_elements['autosar-variable-iref3'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref3'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    global_elements['target-data-prototype-ref3'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access4'] = ET.SubElement(global_elements['data-read-accesss'], 'variable-access')
    global_elements['variable-access4'].attrib = {'UUID': '9eef2638-b3d9-47c1-9e18-37822b089dd4'}
    global_elements['short-name527'] = ET.SubElement(global_elements['variable-access4'], 'short-name')
    global_elements['short-name527'].text = 'DRA_RPort_SR_DataElement1'
    global_elements['accessed-variable4'] = ET.SubElement(global_elements['variable-access4'], 'accessed-variable')
    global_elements['autosar-variable-iref4'] = ET.SubElement(global_elements['accessed-variable4'], 'autosar-variable-iref')
    global_elements['port-prototype-ref4'] = ET.SubElement(global_elements['autosar-variable-iref4'], 'port-prototype-ref')
    global_elements['port-prototype-ref4'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    global_elements['port-prototype-ref4'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref4'] = ET.SubElement(global_elements['autosar-variable-iref4'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref4'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    global_elements['target-data-prototype-ref4'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access5'] = ET.SubElement(global_elements['data-read-accesss'], 'variable-access')
    global_elements['variable-access5'].attrib = {'UUID': '26ad84a0-bc71-4cae-92f7-69d3d1bc91ff'}
    global_elements['short-name528'] = ET.SubElement(global_elements['variable-access5'], 'short-name')
    global_elements['short-name528'].text = 'DRA_RPort_nvd_NvData'
    global_elements['accessed-variable5'] = ET.SubElement(global_elements['variable-access5'], 'accessed-variable')
    global_elements['autosar-variable-iref5'] = ET.SubElement(global_elements['accessed-variable5'], 'autosar-variable-iref')
    global_elements['port-prototype-ref5'] = ET.SubElement(global_elements['autosar-variable-iref5'], 'port-prototype-ref')
    global_elements['port-prototype-ref5'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref5'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref5'] = ET.SubElement(global_elements['autosar-variable-iref5'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref5'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    global_elements['target-data-prototype-ref5'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access6'] = ET.SubElement(global_elements['data-read-accesss'], 'variable-access')
    global_elements['variable-access6'].attrib = {'UUID': '067aa426-f94d-4f7c-b471-a3631398a8a6'}
    global_elements['short-name529'] = ET.SubElement(global_elements['variable-access6'], 'short-name')
    global_elements['short-name529'].text = 'DRA_RPort_nvd_NvData1'
    global_elements['accessed-variable6'] = ET.SubElement(global_elements['variable-access6'], 'accessed-variable')
    global_elements['autosar-variable-iref6'] = ET.SubElement(global_elements['accessed-variable6'], 'autosar-variable-iref')
    global_elements['port-prototype-ref6'] = ET.SubElement(global_elements['autosar-variable-iref6'], 'port-prototype-ref')
    global_elements['port-prototype-ref6'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref6'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref6'] = ET.SubElement(global_elements['autosar-variable-iref6'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref6'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    global_elements['target-data-prototype-ref6'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['data-write-accesss2'] = ET.SubElement(global_elements['runnable-entity13'], 'data-write-accesss')
    global_elements['variable-access7'] = ET.SubElement(global_elements['data-write-accesss2'], 'variable-access')
    global_elements['variable-access7'].attrib = {'UUID': 'a0b4f337-7b3c-4ade-bc28-db75b0882305'}
    global_elements['short-name530'] = ET.SubElement(global_elements['variable-access7'], 'short-name')
    global_elements['short-name530'].text = 'DWA_PPort_SR_DataElement'
    global_elements['accessed-variable7'] = ET.SubElement(global_elements['variable-access7'], 'accessed-variable')
    global_elements['autosar-variable-iref7'] = ET.SubElement(global_elements['accessed-variable7'], 'autosar-variable-iref')
    global_elements['port-prototype-ref7'] = ET.SubElement(global_elements['autosar-variable-iref7'], 'port-prototype-ref')
    global_elements['port-prototype-ref7'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    global_elements['port-prototype-ref7'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref7'] = ET.SubElement(global_elements['autosar-variable-iref7'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref7'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    global_elements['target-data-prototype-ref7'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access8'] = ET.SubElement(global_elements['data-write-accesss2'], 'variable-access')
    global_elements['variable-access8'].attrib = {'UUID': '839b63ac-ec02-4b70-aca8-f974d2ab728c'}
    global_elements['short-name531'] = ET.SubElement(global_elements['variable-access8'], 'short-name')
    global_elements['short-name531'].text = 'DWA_PPort_SR_DataElement1'
    global_elements['accessed-variable8'] = ET.SubElement(global_elements['variable-access8'], 'accessed-variable')
    global_elements['autosar-variable-iref8'] = ET.SubElement(global_elements['accessed-variable8'], 'autosar-variable-iref')
    global_elements['port-prototype-ref8'] = ET.SubElement(global_elements['autosar-variable-iref8'], 'port-prototype-ref')
    global_elements['port-prototype-ref8'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    global_elements['port-prototype-ref8'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref8'] = ET.SubElement(global_elements['autosar-variable-iref8'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref8'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    global_elements['target-data-prototype-ref8'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access9'] = ET.SubElement(global_elements['data-write-accesss2'], 'variable-access')
    global_elements['variable-access9'].attrib = {'UUID': 'b68d4be0-8b3f-4259-9c8a-2901c17454d7'}
    global_elements['short-name532'] = ET.SubElement(global_elements['variable-access9'], 'short-name')
    global_elements['short-name532'].text = 'DWA_PPort_nvd_NvData'
    global_elements['accessed-variable9'] = ET.SubElement(global_elements['variable-access9'], 'accessed-variable')
    global_elements['autosar-variable-iref9'] = ET.SubElement(global_elements['accessed-variable9'], 'autosar-variable-iref')
    global_elements['port-prototype-ref9'] = ET.SubElement(global_elements['autosar-variable-iref9'], 'port-prototype-ref')
    global_elements['port-prototype-ref9'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
    global_elements['port-prototype-ref9'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref9'] = ET.SubElement(global_elements['autosar-variable-iref9'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref9'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    global_elements['target-data-prototype-ref9'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access10'] = ET.SubElement(global_elements['data-write-accesss2'], 'variable-access')
    global_elements['variable-access10'].attrib = {'UUID': '3e84de24-a491-4152-b344-8c5e44e9197e'}
    global_elements['short-name533'] = ET.SubElement(global_elements['variable-access10'], 'short-name')
    global_elements['short-name533'].text = 'DWA_PPort_nvd_NvData1'
    global_elements['accessed-variable10'] = ET.SubElement(global_elements['variable-access10'], 'accessed-variable')
    global_elements['autosar-variable-iref10'] = ET.SubElement(global_elements['accessed-variable10'], 'autosar-variable-iref')
    global_elements['port-prototype-ref10'] = ET.SubElement(global_elements['autosar-variable-iref10'], 'port-prototype-ref')
    global_elements['port-prototype-ref10'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
    global_elements['port-prototype-ref10'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref10'] = ET.SubElement(global_elements['autosar-variable-iref10'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref10'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    global_elements['target-data-prototype-ref10'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['read-local-variables'] = ET.SubElement(global_elements['runnable-entity13'], 'read-local-variables')
    global_elements['variable-access11'] = ET.SubElement(global_elements['read-local-variables'], 'variable-access')
    global_elements['variable-access11'].attrib = {'UUID': 'c8972fdb-f78a-4e12-9a30-4faf0daa6c23'}
    global_elements['short-name534'] = ET.SubElement(global_elements['variable-access11'], 'short-name')
    global_elements['short-name534'].text = 'IRVRA_ExplicitInterRunnableVariable'
    global_elements['accessed-variable11'] = ET.SubElement(global_elements['variable-access11'], 'accessed-variable')
    global_elements['local-variable-ref'] = ET.SubElement(global_elements['accessed-variable11'], 'local-variable-ref')
    global_elements['local-variable-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ExplicitInterRunnableVariable'
    global_elements['local-variable-ref'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access12'] = ET.SubElement(global_elements['read-local-variables'], 'variable-access')
    global_elements['variable-access12'].attrib = {'UUID': 'bf16d1d1-6833-4572-8830-6e31aa069454'}
    global_elements['short-name535'] = ET.SubElement(global_elements['variable-access12'], 'short-name')
    global_elements['short-name535'].text = 'IRVRA_ImplicitInterRunnableVariable'
    global_elements['accessed-variable12'] = ET.SubElement(global_elements['variable-access12'], 'accessed-variable')
    global_elements['local-variable-ref2'] = ET.SubElement(global_elements['accessed-variable12'], 'local-variable-ref')
    global_elements['local-variable-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ImplicitInterRunnableVariable'
    global_elements['local-variable-ref2'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['symbol21'] = ET.SubElement(global_elements['runnable-entity13'], 'symbol')
    global_elements['symbol21'].text = 'ApplicationSwComponentType_Runnable13'
    global_elements['runnable-entity14'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity14'].attrib = {'UUID': '1c2e8cb0-fdf5-45ee-9257-dee6f42d2ad4'}
    global_elements['short-name536'] = ET.SubElement(global_elements['runnable-entity14'], 'short-name')
    global_elements['short-name536'].text = 'Runnable14'
    global_elements['minimum-start-interval14'] = ET.SubElement(global_elements['runnable-entity14'], 'minimum-start-interval')
    global_elements['minimum-start-interval14'].text = '0'
    global_elements['can-be-invoked-concurrently14'] = ET.SubElement(global_elements['runnable-entity14'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently14'].text = 'false'
    global_elements['symbol22'] = ET.SubElement(global_elements['runnable-entity14'], 'symbol')
    global_elements['symbol22'].text = 'ApplicationSwComponentType_Runnable14'
    global_elements['runnable-entity15'] = ET.SubElement(global_elements['runnables'], 'runnable-entity')
    global_elements['runnable-entity15'].attrib = {'UUID': '6debf2b3-9c4c-455e-9cbc-0c7cfaca4d43'}
    global_elements['short-name537'] = ET.SubElement(global_elements['runnable-entity15'], 'short-name')
    global_elements['short-name537'].text = 'Runnable15'
    global_elements['minimum-start-interval15'] = ET.SubElement(global_elements['runnable-entity15'], 'minimum-start-interval')
    global_elements['minimum-start-interval15'].text = '0'
    global_elements['can-be-invoked-concurrently15'] = ET.SubElement(global_elements['runnable-entity15'], 'can-be-invoked-concurrently')
    global_elements['can-be-invoked-concurrently15'].text = 'false'
    global_elements['data-read-accesss2'] = ET.SubElement(global_elements['runnable-entity15'], 'data-read-accesss')
    global_elements['variable-access13'] = ET.SubElement(global_elements['data-read-accesss2'], 'variable-access')
    global_elements['variable-access13'].attrib = {'UUID': '5648b05b-23f8-4729-9fdd-25a617e2d17b'}
    global_elements['short-name538'] = ET.SubElement(global_elements['variable-access13'], 'short-name')
    global_elements['short-name538'].text = 'DRA_RPort_nvd_NvData'
    global_elements['accessed-variable13'] = ET.SubElement(global_elements['variable-access13'], 'accessed-variable')
    global_elements['autosar-variable-iref11'] = ET.SubElement(global_elements['accessed-variable13'], 'autosar-variable-iref')
    global_elements['port-prototype-ref11'] = ET.SubElement(global_elements['autosar-variable-iref11'], 'port-prototype-ref')
    global_elements['port-prototype-ref11'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref11'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref11'] = ET.SubElement(global_elements['autosar-variable-iref11'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref11'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    global_elements['target-data-prototype-ref11'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access14'] = ET.SubElement(global_elements['data-read-accesss2'], 'variable-access')
    global_elements['variable-access14'].attrib = {'UUID': 'b355b0ac-1fa9-43f7-b5ab-240eae2c3694'}
    global_elements['short-name539'] = ET.SubElement(global_elements['variable-access14'], 'short-name')
    global_elements['short-name539'].text = 'DRA_RPort_nvd_NvData1'
    global_elements['accessed-variable14'] = ET.SubElement(global_elements['variable-access14'], 'accessed-variable')
    global_elements['autosar-variable-iref12'] = ET.SubElement(global_elements['accessed-variable14'], 'autosar-variable-iref')
    global_elements['port-prototype-ref12'] = ET.SubElement(global_elements['autosar-variable-iref12'], 'port-prototype-ref')
    global_elements['port-prototype-ref12'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref12'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref12'] = ET.SubElement(global_elements['autosar-variable-iref12'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref12'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    global_elements['target-data-prototype-ref12'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['data-receive-point-by-arguments'] = ET.SubElement(global_elements['runnable-entity15'], 'data-receive-point-by-arguments')
    global_elements['variable-access15'] = ET.SubElement(global_elements['data-receive-point-by-arguments'], 'variable-access')
    global_elements['variable-access15'].attrib = {'UUID': '86796258-06a6-480e-8a39-e01411743a56'}
    global_elements['short-name540'] = ET.SubElement(global_elements['variable-access15'], 'short-name')
    global_elements['short-name540'].text = 'DRP_RPort_SR_DataElement'
    global_elements['accessed-variable15'] = ET.SubElement(global_elements['variable-access15'], 'accessed-variable')
    global_elements['autosar-variable-iref13'] = ET.SubElement(global_elements['accessed-variable15'], 'autosar-variable-iref')
    global_elements['port-prototype-ref13'] = ET.SubElement(global_elements['autosar-variable-iref13'], 'port-prototype-ref')
    global_elements['port-prototype-ref13'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    global_elements['port-prototype-ref13'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref13'] = ET.SubElement(global_elements['autosar-variable-iref13'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref13'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    global_elements['target-data-prototype-ref13'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access16'] = ET.SubElement(global_elements['data-receive-point-by-arguments'], 'variable-access')
    global_elements['variable-access16'].attrib = {'UUID': '88c27605-b9a2-4db7-af10-2a0953c5110b'}
    global_elements['short-name541'] = ET.SubElement(global_elements['variable-access16'], 'short-name')
    global_elements['short-name541'].text = 'DRP_RPort_nvd_NvData'
    global_elements['accessed-variable16'] = ET.SubElement(global_elements['variable-access16'], 'accessed-variable')
    global_elements['autosar-variable-iref14'] = ET.SubElement(global_elements['accessed-variable16'], 'autosar-variable-iref')
    global_elements['port-prototype-ref14'] = ET.SubElement(global_elements['autosar-variable-iref14'], 'port-prototype-ref')
    global_elements['port-prototype-ref14'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref14'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref14'] = ET.SubElement(global_elements['autosar-variable-iref14'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref14'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    global_elements['target-data-prototype-ref14'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access17'] = ET.SubElement(global_elements['data-receive-point-by-arguments'], 'variable-access')
    global_elements['variable-access17'].attrib = {'UUID': 'b69ad602-c226-42a5-9bbb-acbbc5c16743'}
    global_elements['short-name542'] = ET.SubElement(global_elements['variable-access17'], 'short-name')
    global_elements['short-name542'].text = 'DRP_RPort_nvd_NvData1'
    global_elements['accessed-variable17'] = ET.SubElement(global_elements['variable-access17'], 'accessed-variable')
    global_elements['autosar-variable-iref15'] = ET.SubElement(global_elements['accessed-variable17'], 'autosar-variable-iref')
    global_elements['port-prototype-ref15'] = ET.SubElement(global_elements['autosar-variable-iref15'], 'port-prototype-ref')
    global_elements['port-prototype-ref15'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref15'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref15'] = ET.SubElement(global_elements['autosar-variable-iref15'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref15'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    global_elements['target-data-prototype-ref15'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['data-receive-point-by-values'] = ET.SubElement(global_elements['runnable-entity15'], 'data-receive-point-by-values')
    global_elements['variable-access18'] = ET.SubElement(global_elements['data-receive-point-by-values'], 'variable-access')
    global_elements['variable-access18'].attrib = {'UUID': '38ed8447-65f1-48a9-b075-fa613c1267d2'}
    global_elements['short-name543'] = ET.SubElement(global_elements['variable-access18'], 'short-name')
    global_elements['short-name543'].text = 'DRPV_RPort_SR_DataElement1'
    global_elements['accessed-variable18'] = ET.SubElement(global_elements['variable-access18'], 'accessed-variable')
    global_elements['autosar-variable-iref16'] = ET.SubElement(global_elements['accessed-variable18'], 'autosar-variable-iref')
    global_elements['port-prototype-ref16'] = ET.SubElement(global_elements['autosar-variable-iref16'], 'port-prototype-ref')
    global_elements['port-prototype-ref16'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_SR'
    global_elements['port-prototype-ref16'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref16'] = ET.SubElement(global_elements['autosar-variable-iref16'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref16'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    global_elements['target-data-prototype-ref16'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access19'] = ET.SubElement(global_elements['data-receive-point-by-values'], 'variable-access')
    global_elements['variable-access19'].attrib = {'UUID': 'd07d7e6b-0d9c-4475-bbb9-2ccfc3e60c33'}
    global_elements['short-name544'] = ET.SubElement(global_elements['variable-access19'], 'short-name')
    global_elements['short-name544'].text = 'DRPV_RPort_nvd_NvData'
    global_elements['accessed-variable19'] = ET.SubElement(global_elements['variable-access19'], 'accessed-variable')
    global_elements['autosar-variable-iref17'] = ET.SubElement(global_elements['accessed-variable19'], 'autosar-variable-iref')
    global_elements['port-prototype-ref17'] = ET.SubElement(global_elements['autosar-variable-iref17'], 'port-prototype-ref')
    global_elements['port-prototype-ref17'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_nvd'
    global_elements['port-prototype-ref17'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref17'] = ET.SubElement(global_elements['autosar-variable-iref17'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref17'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    global_elements['target-data-prototype-ref17'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['data-send-points2'] = ET.SubElement(global_elements['runnable-entity15'], 'data-send-points')
    global_elements['variable-access20'] = ET.SubElement(global_elements['data-send-points2'], 'variable-access')
    global_elements['variable-access20'].attrib = {'UUID': '2fc872c8-d598-4d11-8502-1a70e9104bc9'}
    global_elements['short-name545'] = ET.SubElement(global_elements['variable-access20'], 'short-name')
    global_elements['short-name545'].text = 'DSP_PPort_SR_DataElement'
    global_elements['accessed-variable20'] = ET.SubElement(global_elements['variable-access20'], 'accessed-variable')
    global_elements['autosar-variable-iref18'] = ET.SubElement(global_elements['accessed-variable20'], 'autosar-variable-iref')
    global_elements['port-prototype-ref18'] = ET.SubElement(global_elements['autosar-variable-iref18'], 'port-prototype-ref')
    global_elements['port-prototype-ref18'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    global_elements['port-prototype-ref18'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref18'] = ET.SubElement(global_elements['autosar-variable-iref18'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref18'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement'
    global_elements['target-data-prototype-ref18'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access21'] = ET.SubElement(global_elements['data-send-points2'], 'variable-access')
    global_elements['variable-access21'].attrib = {'UUID': 'a2f22836-4cd0-4c2e-8040-1abdf8935ac0'}
    global_elements['short-name546'] = ET.SubElement(global_elements['variable-access21'], 'short-name')
    global_elements['short-name546'].text = 'DSP_PPort_SR_DataElement1'
    global_elements['accessed-variable21'] = ET.SubElement(global_elements['variable-access21'], 'accessed-variable')
    global_elements['autosar-variable-iref19'] = ET.SubElement(global_elements['accessed-variable21'], 'autosar-variable-iref')
    global_elements['port-prototype-ref19'] = ET.SubElement(global_elements['autosar-variable-iref19'], 'port-prototype-ref')
    global_elements['port-prototype-ref19'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    global_elements['port-prototype-ref19'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref19'] = ET.SubElement(global_elements['autosar-variable-iref19'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref19'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    global_elements['target-data-prototype-ref19'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access22'] = ET.SubElement(global_elements['data-send-points2'], 'variable-access')
    global_elements['variable-access22'].attrib = {'UUID': 'c0c41eb1-b5bf-4e30-9569-24d7316b64c8'}
    global_elements['short-name547'] = ET.SubElement(global_elements['variable-access22'], 'short-name')
    global_elements['short-name547'].text = 'DSP_PPort_nvd_NvData'
    global_elements['accessed-variable22'] = ET.SubElement(global_elements['variable-access22'], 'accessed-variable')
    global_elements['autosar-variable-iref20'] = ET.SubElement(global_elements['accessed-variable22'], 'autosar-variable-iref')
    global_elements['port-prototype-ref20'] = ET.SubElement(global_elements['autosar-variable-iref20'], 'port-prototype-ref')
    global_elements['port-prototype-ref20'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
    global_elements['port-prototype-ref20'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref20'] = ET.SubElement(global_elements['autosar-variable-iref20'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref20'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData'
    global_elements['target-data-prototype-ref20'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access23'] = ET.SubElement(global_elements['data-send-points2'], 'variable-access')
    global_elements['variable-access23'].attrib = {'UUID': '96f66382-5f86-4a47-bd5b-9f95f81fc3c9'}
    global_elements['short-name548'] = ET.SubElement(global_elements['variable-access23'], 'short-name')
    global_elements['short-name548'].text = 'DSP_PPort_nvd_NvData1'
    global_elements['accessed-variable23'] = ET.SubElement(global_elements['variable-access23'], 'accessed-variable')
    global_elements['autosar-variable-iref21'] = ET.SubElement(global_elements['accessed-variable23'], 'autosar-variable-iref')
    global_elements['port-prototype-ref21'] = ET.SubElement(global_elements['autosar-variable-iref21'], 'port-prototype-ref')
    global_elements['port-prototype-ref21'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_nvd'
    global_elements['port-prototype-ref21'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref21'] = ET.SubElement(global_elements['autosar-variable-iref21'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref21'].text = '/SharedElements/PortInterfaces/NvData/NvDataInterface/NvData1'
    global_elements['target-data-prototype-ref21'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['data-write-accesss3'] = ET.SubElement(global_elements['runnable-entity15'], 'data-write-accesss')
    global_elements['variable-access24'] = ET.SubElement(global_elements['data-write-accesss3'], 'variable-access')
    global_elements['variable-access24'].attrib = {'UUID': 'd40a6e94-d8e5-48e5-8a1a-c7debe02592f'}
    global_elements['short-name549'] = ET.SubElement(global_elements['variable-access24'], 'short-name')
    global_elements['short-name549'].text = 'DWA_PPort_SR_DataElement1'
    global_elements['accessed-variable24'] = ET.SubElement(global_elements['variable-access24'], 'accessed-variable')
    global_elements['autosar-variable-iref22'] = ET.SubElement(global_elements['accessed-variable24'], 'autosar-variable-iref')
    global_elements['port-prototype-ref22'] = ET.SubElement(global_elements['autosar-variable-iref22'], 'port-prototype-ref')
    global_elements['port-prototype-ref22'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_SR'
    global_elements['port-prototype-ref22'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref22'] = ET.SubElement(global_elements['autosar-variable-iref22'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref22'].text = '/SharedElements/PortInterfaces/SenderReceiver/SenderReceiverInterface/DataElement1'
    global_elements['target-data-prototype-ref22'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['mode-switch-points2'] = ET.SubElement(global_elements['runnable-entity15'], 'mode-switch-points')
    global_elements['mode-switch-point2'] = ET.SubElement(global_elements['mode-switch-points2'], 'mode-switch-point')
    global_elements['mode-switch-point2'].attrib = {'UUID': '8f7d9801-a32d-4e5f-85cd-fbcf669d921a'}
    global_elements['short-name550'] = ET.SubElement(global_elements['mode-switch-point2'], 'short-name')
    global_elements['short-name550'].text = 'MSP_PPort_msi_ModeGroup'
    global_elements['mode-group-iref3'] = ET.SubElement(global_elements['mode-switch-point2'], 'mode-group-iref')
    global_elements['context-p-port-ref4'] = ET.SubElement(global_elements['mode-group-iref3'], 'context-p-port-ref')
    global_elements['context-p-port-ref4'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/PPort_msi'
    global_elements['context-p-port-ref4'].attrib = {'DEST': 'P-PORT-PROTOTYPE'}
    global_elements['target-mode-group-ref3'] = ET.SubElement(global_elements['mode-group-iref3'], 'target-mode-group-ref')
    global_elements['target-mode-group-ref3'].text = '/SharedElements/PortInterfaces/ModeSwitch/ModeSwitchInterface/ModeGroup'
    global_elements['target-mode-group-ref3'].attrib = {'DEST': 'MODE-DECLARATION-GROUP-PROTOTYPE'}
    global_elements['parameter-accesss'] = ET.SubElement(global_elements['runnable-entity15'], 'parameter-accesss')
    global_elements['parameter-access'] = ET.SubElement(global_elements['parameter-accesss'], 'parameter-access')
    global_elements['parameter-access'].attrib = {'UUID': '92d672aa-34ea-4fcb-a0a2-ab2431d59c0a'}
    global_elements['short-name551'] = ET.SubElement(global_elements['parameter-access'], 'short-name')
    global_elements['short-name551'].text = 'ParameterAccess'
    global_elements['accessed-parameter'] = ET.SubElement(global_elements['parameter-access'], 'accessed-parameter')
    global_elements['local-parameter-ref'] = ET.SubElement(global_elements['accessed-parameter'], 'local-parameter-ref')
    global_elements['local-parameter-ref'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ConstantMemory'
    global_elements['local-parameter-ref'].attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}
    global_elements['parameter-access2'] = ET.SubElement(global_elements['parameter-accesss'], 'parameter-access')
    global_elements['parameter-access2'].attrib = {'UUID': '391726ca-20e2-4c02-b063-65244a9e523a'}
    global_elements['short-name552'] = ET.SubElement(global_elements['parameter-access2'], 'short-name')
    global_elements['short-name552'].text = 'PICPVA_PerInstanceParameter'
    global_elements['accessed-parameter2'] = ET.SubElement(global_elements['parameter-access2'], 'accessed-parameter')
    global_elements['local-parameter-ref2'] = ET.SubElement(global_elements['accessed-parameter2'], 'local-parameter-ref')
    global_elements['local-parameter-ref2'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/PerInstanceParameter'
    global_elements['local-parameter-ref2'].attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}
    global_elements['parameter-access3'] = ET.SubElement(global_elements['parameter-accesss'], 'parameter-access')
    global_elements['parameter-access3'].attrib = {'UUID': '19d7aee6-82b8-4233-a787-b84bdb562167'}
    global_elements['short-name553'] = ET.SubElement(global_elements['parameter-access3'], 'short-name')
    global_elements['short-name553'].text = 'CPA_RPort_prm_Parameter'
    global_elements['accessed-parameter3'] = ET.SubElement(global_elements['parameter-access3'], 'accessed-parameter')
    global_elements['autosar-parameter-iref'] = ET.SubElement(global_elements['accessed-parameter3'], 'autosar-parameter-iref')
    global_elements['port-prototype-ref23'] = ET.SubElement(global_elements['autosar-parameter-iref'], 'port-prototype-ref')
    global_elements['port-prototype-ref23'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_prm'
    global_elements['port-prototype-ref23'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref23'] = ET.SubElement(global_elements['autosar-parameter-iref'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref23'].text = '/SharedElements/PortInterfaces/Parameter/ParameterInterface/Parameter'
    global_elements['target-data-prototype-ref23'].attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}
    global_elements['parameter-access4'] = ET.SubElement(global_elements['parameter-accesss'], 'parameter-access')
    global_elements['parameter-access4'].attrib = {'UUID': 'ab7c5c59-47f3-4fee-a310-f64cb2c00c48'}
    global_elements['short-name554'] = ET.SubElement(global_elements['parameter-access4'], 'short-name')
    global_elements['short-name554'].text = 'CPA_RPort_prm_Parameter1'
    global_elements['accessed-parameter4'] = ET.SubElement(global_elements['parameter-access4'], 'accessed-parameter')
    global_elements['autosar-parameter-iref2'] = ET.SubElement(global_elements['accessed-parameter4'], 'autosar-parameter-iref')
    global_elements['port-prototype-ref24'] = ET.SubElement(global_elements['autosar-parameter-iref2'], 'port-prototype-ref')
    global_elements['port-prototype-ref24'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/RPort_prm'
    global_elements['port-prototype-ref24'].attrib = {'DEST': 'R-PORT-PROTOTYPE'}
    global_elements['target-data-prototype-ref24'] = ET.SubElement(global_elements['autosar-parameter-iref2'], 'target-data-prototype-ref')
    global_elements['target-data-prototype-ref24'].text = '/SharedElements/PortInterfaces/Parameter/ParameterInterface/Parameter1'
    global_elements['target-data-prototype-ref24'].attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}
    global_elements['parameter-access5'] = ET.SubElement(global_elements['parameter-accesss'], 'parameter-access')
    global_elements['parameter-access5'].attrib = {'UUID': 'f7d2bfa9-92c5-4627-b238-86aadd05585b'}
    global_elements['short-name555'] = ET.SubElement(global_elements['parameter-access5'], 'short-name')
    global_elements['short-name555'].text = 'SCPVA_SharedParameter'
    global_elements['accessed-parameter5'] = ET.SubElement(global_elements['parameter-access5'], 'accessed-parameter')
    global_elements['local-parameter-ref3'] = ET.SubElement(global_elements['accessed-parameter5'], 'local-parameter-ref')
    global_elements['local-parameter-ref3'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/SharedParameter'
    global_elements['local-parameter-ref3'].attrib = {'DEST': 'PARAMETER-DATA-PROTOTYPE'}
    global_elements['server-call-points2'] = ET.SubElement(global_elements['runnable-entity15'], 'server-call-points')
    global_elements['synchronous-server-call-point'] = ET.SubElement(global_elements['server-call-points2'], 'synchronous-server-call-point')
    global_elements['synchronous-server-call-point'].attrib = {'UUID': 'd6a93f51-be57-4a77-bd8f-e25d3e0ba149'}
    global_elements['short-name556'] = ET.SubElement(global_elements['synchronous-server-call-point'], 'short-name')
    global_elements['short-name556'].text = 'SSCP_RPort_CS_Operation1'
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
    global_elements['written-local-variables'] = ET.SubElement(global_elements['runnable-entity15'], 'written-local-variables')
    global_elements['variable-access25'] = ET.SubElement(global_elements['written-local-variables'], 'variable-access')
    global_elements['variable-access25'].attrib = {'UUID': '7e246e9c-b78a-47be-8798-02887c881e6e'}
    global_elements['short-name557'] = ET.SubElement(global_elements['variable-access25'], 'short-name')
    global_elements['short-name557'].text = 'IRVWA_ExplicitInterRunnableVariable'
    global_elements['accessed-variable25'] = ET.SubElement(global_elements['variable-access25'], 'accessed-variable')
    global_elements['local-variable-ref3'] = ET.SubElement(global_elements['accessed-variable25'], 'local-variable-ref')
    global_elements['local-variable-ref3'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ExplicitInterRunnableVariable'
    global_elements['local-variable-ref3'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}
    global_elements['variable-access26'] = ET.SubElement(global_elements['written-local-variables'], 'variable-access')
    global_elements['variable-access26'].attrib = {'UUID': 'd976bba9-3132-4e15-ac45-88b85facf508'}
    global_elements['short-name558'] = ET.SubElement(global_elements['variable-access26'], 'short-name')
    global_elements['short-name558'].text = 'IRVWA_ImplicitInterRunnableVariable'
    global_elements['accessed-variable26'] = ET.SubElement(global_elements['variable-access26'], 'accessed-variable')
    global_elements['local-variable-ref4'] = ET.SubElement(global_elements['accessed-variable26'], 'local-variable-ref')
    global_elements['local-variable-ref4'].text = '/SwComponentTypes/ApplSWC/ApplicationSwComponentType/IB_Appl/ImplicitInterRunnableVariable'
    global_elements['local-variable-ref4'].attrib = {'DEST': 'VARIABLE-DATA-PROTOTYPE'}

def SharedParameter():
    global_elements['shared-parameters'] = ET.SubElement(global_elements['swc-internal-behavior'], 'shared-parameters')
    global_elements['parameter-data-prototype5'] = ET.SubElement(global_elements['shared-parameters'], 'parameter-data-prototype')
    global_elements['parameter-data-prototype5'].attrib = {'UUID': 'edf877b4-19ea-4e47-8180-a74099cfff0f'}
    global_elements['short-name559'] = ET.SubElement(global_elements['parameter-data-prototype5'], 'short-name')
    global_elements['short-name559'].text = 'SharedParameter'
    global_elements['sw-data-def-props90'] = ET.SubElement(global_elements['parameter-data-prototype5'], 'sw-data-def-props')
    global_elements['sw-data-def-props-variants90'] = ET.SubElement(global_elements['sw-data-def-props90'], 'sw-data-def-props-variants')
    global_elements['sw-data-def-props-conditional90'] = ET.SubElement(global_elements['sw-data-def-props-variants90'], 'sw-data-def-props-conditional')
    global_elements['sw-calibration-access15'] = ET.SubElement(global_elements['sw-data-def-props-conditional90'], 'sw-calibration-access')
    global_elements['sw-calibration-access15'].text = 'READ-WRITE'
    global_elements['sw-impl-policy36'] = ET.SubElement(global_elements['sw-data-def-props-conditional90'], 'sw-impl-policy')
    global_elements['sw-impl-policy36'].text = 'STANDARD'
    global_elements['type-tref39'] = ET.SubElement(global_elements['parameter-data-prototype5'], 'type-tref')
    global_elements['type-tref39'].text = '/AUTOSAR/AUTOSAR_Platform/ImplementationDataTypes/float32'
    global_elements['type-tref39'].attrib = {'DEST': 'IMPLEMENTATION-DATA-TYPE'}
    global_elements['init-value7'] = ET.SubElement(global_elements['parameter-data-prototype5'], 'init-value')
    global_elements['constant-reference3'] = ET.SubElement(global_elements['init-value7'], 'constant-reference')
    global_elements['short-label11'] = ET.SubElement(global_elements['constant-reference3'], 'short-label')
    global_elements['short-label11'].text = 'ReferenceToConstant'
    global_elements['constant-ref3'] = ET.SubElement(global_elements['constant-reference3'], 'constant-ref')
    global_elements['constant-ref3'].text = '/SharedElements/ConstantSpecifications/ApplicationSwComponentType_SharedParameter'
    global_elements['constant-ref3'].attrib = {'DEST': 'CONSTANT-SPECIFICATION'}
    global_elements['supports-multiple-instantiation'] = ET.SubElement(global_elements['swc-internal-behavior'], 'supports-multiple-instantiation')
    global_elements['supports-multiple-instantiation'].text = 'false'

def ConstantSpecifications2():
    global_elements['ar-packages12'] = ET.SubElement(global_elements['ar-package46'], 'ar-packages')
    global_elements['ar-package47'] = ET.SubElement(global_elements['ar-packages12'], 'ar-package')
    global_elements['ar-package47'].attrib = {'UUID': '0f00b99f-27e3-434f-9d85-398fc7c29067'}
    global_elements['short-name560'] = ET.SubElement(global_elements['ar-package47'], 'short-name')
    global_elements['short-name560'].text = 'ConstantSpecifications'
    global_elements['ar-package48'] = ET.SubElement(global_elements['ar-packages11'], 'ar-package')
    global_elements['ar-package48'].attrib = {'UUID': '7f0b665f-81ab-462f-aeab-1777b0f9dfd8'}
    global_elements['short-name561'] = ET.SubElement(global_elements['ar-package48'], 'short-name')
    global_elements['short-name561'].text = 'CddSWC'
    global_elements['elements31'] = ET.SubElement(global_elements['ar-package48'], 'elements')
    global_elements['complex-device-driver-sw-component-type'] = ET.SubElement(global_elements['elements31'], 'complex-device-driver-sw-component-type')
    global_elements['complex-device-driver-sw-component-type'].attrib = {'UUID': '27755bdf-1bfe-447f-bfdf-54402e4f4db3'}
    global_elements['short-name562'] = ET.SubElement(global_elements['complex-device-driver-sw-component-type'], 'short-name')
    global_elements['short-name562'].text = 'ComplexDeviceDriverSwComponentType'
    global_elements['ar-package49'] = ET.SubElement(global_elements['ar-packages11'], 'ar-package')
    global_elements['ar-package49'].attrib = {'UUID': 'a9d129de-eda4-4cda-9025-70a56f38fb59'}
    global_elements['short-name563'] = ET.SubElement(global_elements['ar-package49'], 'short-name')
    global_elements['short-name563'].text = 'CompSWC'
    global_elements['elements32'] = ET.SubElement(global_elements['ar-package49'], 'elements')
    global_elements['composition-sw-component-type'] = ET.SubElement(global_elements['elements32'], 'composition-sw-component-type')
    global_elements['composition-sw-component-type'].attrib = {'UUID': '9e886193-6d1b-454f-98b2-d0347db57ace'}
    global_elements['short-name564'] = ET.SubElement(global_elements['composition-sw-component-type'], 'short-name')
    global_elements['short-name564'].text = 'CompositionSwComponentType'
    global_elements['ar-package50'] = ET.SubElement(global_elements['ar-packages11'], 'ar-package')
    global_elements['ar-package50'].attrib = {'UUID': '28aa9cf2-4118-4878-8504-271a3ed4600b'}
    global_elements['short-name565'] = ET.SubElement(global_elements['ar-package50'], 'short-name')
    global_elements['short-name565'].text = 'EcuAbSWC'
    global_elements['elements33'] = ET.SubElement(global_elements['ar-package50'], 'elements')
    global_elements['ecu-abstraction-sw-component-type'] = ET.SubElement(global_elements['elements33'], 'ecu-abstraction-sw-component-type')
    global_elements['ecu-abstraction-sw-component-type'].attrib = {'UUID': '0dc33c67-8b23-4896-b6a3-8a537f1cd166'}
    global_elements['short-name566'] = ET.SubElement(global_elements['ecu-abstraction-sw-component-type'], 'short-name')
    global_elements['short-name566'].text = 'EcuAbstractionSwComponentType'
    global_elements['ar-package51'] = ET.SubElement(global_elements['ar-packages11'], 'ar-package')
    global_elements['ar-package51'].attrib = {'UUID': '8562405a-26a1-4c3d-861f-eb0745310572'}
    global_elements['short-name567'] = ET.SubElement(global_elements['ar-package51'], 'short-name')
    global_elements['short-name567'].text = 'NvDataSWC'
    global_elements['elements34'] = ET.SubElement(global_elements['ar-package51'], 'elements')
    global_elements['nv-block-sw-component-type'] = ET.SubElement(global_elements['elements34'], 'nv-block-sw-component-type')
    global_elements['nv-block-sw-component-type'].attrib = {'UUID': '9a2c1578-3f64-4af0-b953-7b81f28434cf'}
    global_elements['short-name568'] = ET.SubElement(global_elements['nv-block-sw-component-type'], 'short-name')
    global_elements['short-name568'].text = 'NvBlockSwComponentType'
    global_elements['ar-package52'] = ET.SubElement(global_elements['ar-packages11'], 'ar-package')
    global_elements['ar-package52'].attrib = {'UUID': '0a54c44d-f71e-4ec3-bbf1-410c0b885915'}
    global_elements['short-name569'] = ET.SubElement(global_elements['ar-package52'], 'short-name')
    global_elements['short-name569'].text = 'PrmSWC'
    global_elements['elements35'] = ET.SubElement(global_elements['ar-package52'], 'elements')
    global_elements['parameter-sw-component-type'] = ET.SubElement(global_elements['elements35'], 'parameter-sw-component-type')
    global_elements['parameter-sw-component-type'].attrib = {'UUID': 'c21a6d07-19ae-40ac-affe-f4aa3b5acb25'}
    global_elements['short-name570'] = ET.SubElement(global_elements['parameter-sw-component-type'], 'short-name')
    global_elements['short-name570'].text = 'ParameterSwComponentType'
    global_elements['ar-package53'] = ET.SubElement(global_elements['ar-packages11'], 'ar-package')
    global_elements['ar-package53'].attrib = {'UUID': 'f142ef66-4dce-4750-8568-a7e836f462da'}
    global_elements['short-name571'] = ET.SubElement(global_elements['ar-package53'], 'short-name')
    global_elements['short-name571'].text = 'SnsrActSWC'
    global_elements['elements36'] = ET.SubElement(global_elements['ar-package53'], 'elements')
    global_elements['sensor-actuator-sw-component-type'] = ET.SubElement(global_elements['elements36'], 'sensor-actuator-sw-component-type')
    global_elements['sensor-actuator-sw-component-type'].attrib = {'UUID': 'e631e3e3-9a52-4bbe-a762-4311d8f45934'}
    global_elements['short-name572'] = ET.SubElement(global_elements['sensor-actuator-sw-component-type'], 'short-name')
    global_elements['short-name572'].text = 'SensorActuatorSwComponentType'
    global_elements['ar-package54'] = ET.SubElement(global_elements['ar-packages11'], 'ar-package')
    global_elements['ar-package54'].attrib = {'UUID': '60bb3f96-0a5c-4e30-bdda-5205f3a1cdb6'}
    global_elements['short-name573'] = ET.SubElement(global_elements['ar-package54'], 'short-name')
    global_elements['short-name573'].text = 'SrvcPrxySWC'
    global_elements['elements37'] = ET.SubElement(global_elements['ar-package54'], 'elements')
    global_elements['service-proxy-sw-component-type'] = ET.SubElement(global_elements['elements37'], 'service-proxy-sw-component-type')
    global_elements['service-proxy-sw-component-type'].attrib = {'UUID': '7e09780f-aad2-4f70-8c22-e5e19f1a82e8'}
    global_elements['short-name574'] = ET.SubElement(global_elements['service-proxy-sw-component-type'], 'short-name')
    global_elements['short-name574'].text = 'ServiceProxySwComponentType'
    global_elements['ar-package55'] = ET.SubElement(global_elements['ar-packages11'], 'ar-package')
    global_elements['ar-package55'].attrib = {'UUID': '2ed6bb1a-c9d6-46c0-ae8b-0743080405b6'}
    global_elements['short-name575'] = ET.SubElement(global_elements['ar-package55'], 'short-name')
    global_elements['short-name575'].text = 'SrvcSWC'
    global_elements['elements38'] = ET.SubElement(global_elements['ar-package55'], 'elements')
    global_elements['service-sw-component-type'] = ET.SubElement(global_elements['elements38'], 'service-sw-component-type')
    global_elements['service-sw-component-type'].attrib = {'UUID': '1da8de22-a6ec-4cab-829a-56300097c5ac'}
    global_elements['short-name576'] = ET.SubElement(global_elements['service-sw-component-type'], 'short-name')
    global_elements['short-name576'].text = 'ServiceSwComponentType'
    global_elements['ar-package56'] = ET.SubElement(global_elements['ar-packages'], 'ar-package')
    global_elements['short-name577'] = ET.SubElement(global_elements['ar-package56'], 'short-name')
    global_elements['short-name577'].text = 'Systems'





    indent(global_elements['root'])
    tree = ET.ElementTree(global_elements['root'])
    tree.write('output.arxml', encoding='utf-8', xml_declaration=True)

    print("ARXML file has been created and saved as 'output.arxml'.")

if __name__ == "__main__":
    # Example function calls
    # Auto-generated script to call all functions
    AUTOSAR_GenDef()
    AUTOSAR_PhysicalUnits()
    I1()
    Illmn1()
    Len1()
    Len1M1TiNeg2()
    Len1M1TiNeg2INeg2()
    Len1M1TiNeg2_1()
    Len1M1TiNeg3INeg1()
    Len1M1TiNeg3TNeg1()
    Len1TiNeg1()
    Len1TiNeg2()
    Len1TiNeg3()
    Len2()
    Len2M1()
    Len2M1TiNeg1()
    Len2M1TiNeg2()
    Len2M1TiNeg2AmntNeg1()
    Len2M1TiNeg2INeg1()
    Len2M1TiNeg2INeg2()
    Len2M1TiNeg2TNeg1()
    Len2M1TiNeg2TNeg1AmntNeg1()
    Len2M1TiNeg2_1()
    Len2M1TiNeg3()
    Len2M1TiNeg3INeg1()
    Len2M1TiNeg3INeg2()
    Len2M1TiNeg3_1()
    Len2M1TiNeg4()
    Len2M1TiNeg4INeg1()
    Len2Ti1()
    Len2TiNeg2()
    Len2TiNeg2TNeg1()
    Len2_1()
    Len3()
    Len3MNeg1()
    Len3TiNeg1()
    Len3TiNeg2()
    LenNeg1()
    LenNeg1M1TiNeg1()
    LenNeg1M1TiNeg2()
    LenNeg1M1TiNeg2_1()
    LenNeg1M1TiNeg3()
    LenNeg2Illmn1()
    LenNeg2MNeg1Ti3I2()
    LenNeg2MNeg1Ti4I2()
    LenNeg3Amnt1()
    LenNeg3M1()
    LenNeg3MNeg1Ti2I2()
    LenNeg3MNeg1Ti3I2()
    LenNeg3Ti1I1()
    LenNeg3Ti1I1_1()
    LenNeg3TiNeg1Amnt1()
    LenNeg4M1TiNeg1()
    M1()
    M1AmntNeg1()
    M1TiNeg1()
    M1TiNeg1_1()
    M1TiNeg2()
    M1TiNeg2INeg1()
    M1TiNeg3TNeg1()
    NoDimension()
    NoDimension_1()
    NoDimension_2()
    NoDimension_5()
    NoDimension_6()
    T1()
    T1I1()
    T1_1()
    Ti1()
    TiNeg1()
    TiNeg1Amnt1()
    TiNeg1I1()
    TiNeg1T1()
    TiNeg1_1()
    TiNeg1_2()
    TiNeg1_3()
    TiNeg2()
    STANDARD()
    Ampr()
    AmprPerSec()
    AmprSec()
    Bar()
    BarPerSec()
    Bel()
    Bit()
    BitPerSec()
    BytPerSec()
    Byte()
    Cd()
    CentiMtr()
    CentiMtrSqd()
    Coulomb()
    Day()
    DeciBel()
    Deg()
    DegCgrd()
    DegPerSec()
    Frd()
    Gr()
    GrPerLtr()
    GrPerMol()
    GrPerSec()
    HectoPa()
    HectoPaPerSec()
    HectoPaPerVolt()
    HectoPaSecPerMtrCubd()
    Henry()
    HenryPerMtr()
    Hr()
    Hz()
    Jou()
    JouPerKelvin()
    JouPerKiloGr()
    JouPerKiloGrPerKelvin()
    JouPerMol()
    JouPerMolPerKelvin()
    Kat()
    KelvinAbslt()
    KelvinPerSec()
    KelvinRel()
    KiloBitPerSec()
    KiloGr()
    KiloGrPerHr()
    KiloGrPerMtrCubd()
    KiloGrPerSec()
    KiloGrSqrMtr()
    KiloHz()
    KiloJou()
    KiloMtr()
    KiloMtrPerHr()
    KiloMtrPerHrPerSec()
    KiloNwt()
    KiloNwtMtrPerSec()
    KiloOhm()
    KiloVolt()
    KiloWatt()
    KiloWattHr()
    KiloWattHrPer100KiloMtr()
    Ltr()
    LtrPer100KiloMtr()
    LtrPerHr()
    LtrPerKiloMtr()
    MegaBitPerSec()
    MegaHz()
    MegaJou()
    MegaOhm()
    MegaPa()
    MegaWatt()
    Micro()
    Milli()
    Mins()
    Mile()
    Mo1()
    Mtr()
    NanoFrd()
    Nwt()
    Ohm()
    Pascal()
    PerMille()
    Perc()
    PicoFrd()
    Rpm()
    Siemens()
    Tesla()
    Tonne()
    Volt()
    Watt()
    Wb()
    Yr()
    AUTOSAR_Platform()
    BaseTypes()
    CompuMethods()
    DataConstrs()
    ImplementationDataTypes()
    BswModuleEntrys()
    Std_MessageResultType()
    DataConstrs2()
    Std_ExtractProtocolHeaderFieldsType()
    Communication()
    EcuInstances()
    ApplicationPrimitiveDataType()
    Record()
    BITFIELD_TEXTTABLE_CompuMethod()
    CompuMethods()
    RAT_FUNC_CompuMethod()
    SCALE_RATIONAL_AND_TEXTTABLE_CompuMethod()
    Scale_linear_And_texttable_CompuMethod()
    TAB_NOINTP_CompuMethod()
    TEXTTABLE_CompuMethod()
    ConstantSpecifications()
    ConstantTypeMappingSets()
    DataConstr()
    DataTypemappingSets()
    ARRAY_ImplementationDataType()
    ARRAY_ImplementationDataType1()
    ImplementationDataType()
    STRUCTURE_ImplementationDataType1()
    Struct_Array_ImplementationDataType()
    TypeTref_ImplementationDataType()
    ClientServer()
    Copy2_ClientServerInterface()
    Copy3_ClientServerInterface()
    Copy4_ClientServerInterface()
    Copy_ClientServerInterface()
    Operation1()
    ModeSwitch()
    NvData()
    Parameter()
    SenderReceiver()
    Copy3_SenderReceiverInterface()
    Copy4_SenderReceiverInterface()
    Copy5_SenderReceiverInterface()
    Copy_SenderReceiverInterface()
    SenderReceiverInterface()
    Trigger()
    SWCImpl()
    SwComponentTypes()
    IB_Appl()
    StaticMemory()
    ArTypedPerInstanceMemory()
    AsynchronousServerCallReturnsEvent()
    ExplicitInterRunnableVariable()
    ImplicitInterRunnableVariable()
    PerInstanceParameter()
    Runnable()
    ApplicationSwComponentType_Runnable()
    DRA_RPort_SR_DataElement()
    SharedParameter()
    ConstantSpecifications2()

