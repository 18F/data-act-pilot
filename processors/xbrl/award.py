# ./award.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:894d7c559aa410f812c4820facd187ce53d922fd
# Generated 2015-09-09 15:57:00.673839 by PyXB version 1.2.4 using Python 2.7.8.final.0
# Namespace http://www.xbrl.org/int/award/2006-10-25 [xmlns:award]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:11b44d4a-5746-11e5-a0a3-3c15c2ca4b96')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import xbrli as _ImportedBinding_xbrli
import gen as _ImportedBinding_gen

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.xbrl.org/int/award/2006-10-25', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 6, 1)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.n00 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='00', tag='n00')
STD_ANON.n01 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='01', tag='n01')
STD_ANON.n02 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='02', tag='n02')
STD_ANON.n03 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='03', tag='n03')
STD_ANON.n04 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='04', tag='n04')
STD_ANON.n05 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='05', tag='n05')
STD_ANON.n06 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='06', tag='n06')
STD_ANON.n11 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='11', tag='n11')
STD_ANON.n12 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='12', tag='n12')
STD_ANON.n20 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='20', tag='n20')
STD_ANON.n21 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='21', tag='n21')
STD_ANON.n22 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='22', tag='n22')
STD_ANON.n23 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='23', tag='n23')
STD_ANON.n25 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='25', tag='n25')
STD_ANON.undefined = STD_ANON._CF_enumeration.addEnumeration(unicode_value='undefined', tag='undefined')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 27, 1)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.n1 = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
STD_ANON_.n2 = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
STD_ANON_.undefined = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='undefined', tag='undefined')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 36, 1)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.B = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
STD_ANON_2.C = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
STD_ANON_2.D = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
STD_ANON_2.undefined = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='undefined', tag='undefined')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 46, 1)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.n02 = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='02', tag='n02')
STD_ANON_3.n03 = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='03', tag='n03')
STD_ANON_3.n04 = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='04', tag='n04')
STD_ANON_3.n05 = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='05', tag='n05')
STD_ANON_3.n06 = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='06', tag='n06')
STD_ANON_3.n07 = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='07', tag='n07')
STD_ANON_3.n08 = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='08', tag='n08')
STD_ANON_3.n09 = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='09', tag='n09')
STD_ANON_3.n10 = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='10', tag='n10')
STD_ANON_3.n11 = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='11', tag='n11')
STD_ANON_3.undefined = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='undefined', tag='undefined')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Complex type {http://www.xbrl.org/int/award/2006-10-25}highlyCompensatedOfficerComplexType with content type ELEMENT_ONLY
class highlyCompensatedOfficerComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/award/2006-10-25}highlyCompensatedOfficerComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 63, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/award/2006-10-25}highlyCompensatedOfficerFirstName uses Python identifier highlyCompensatedOfficerFirstName
    __highlyCompensatedOfficerFirstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerFirstName'), 'highlyCompensatedOfficerFirstName', '__httpwww_xbrl_orgintaward2006_10_25_highlyCompensatedOfficerComplexType_httpwww_xbrl_orgintaward2006_10_25highlyCompensatedOfficerFirstName', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 101, 1), )

    
    highlyCompensatedOfficerFirstName = property(__highlyCompensatedOfficerFirstName.value, __highlyCompensatedOfficerFirstName.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}highlyCompensatedOfficerMiddleInitial uses Python identifier highlyCompensatedOfficerMiddleInitial
    __highlyCompensatedOfficerMiddleInitial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerMiddleInitial'), 'highlyCompensatedOfficerMiddleInitial', '__httpwww_xbrl_orgintaward2006_10_25_highlyCompensatedOfficerComplexType_httpwww_xbrl_orgintaward2006_10_25highlyCompensatedOfficerMiddleInitial', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 102, 1), )

    
    highlyCompensatedOfficerMiddleInitial = property(__highlyCompensatedOfficerMiddleInitial.value, __highlyCompensatedOfficerMiddleInitial.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}highlyCompensatedOfficerLastName uses Python identifier highlyCompensatedOfficerLastName
    __highlyCompensatedOfficerLastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerLastName'), 'highlyCompensatedOfficerLastName', '__httpwww_xbrl_orgintaward2006_10_25_highlyCompensatedOfficerComplexType_httpwww_xbrl_orgintaward2006_10_25highlyCompensatedOfficerLastName', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 103, 1), )

    
    highlyCompensatedOfficerLastName = property(__highlyCompensatedOfficerLastName.value, __highlyCompensatedOfficerLastName.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}highlyCompensatedOfficerCompensation uses Python identifier highlyCompensatedOfficerCompensation
    __highlyCompensatedOfficerCompensation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerCompensation'), 'highlyCompensatedOfficerCompensation', '__httpwww_xbrl_orgintaward2006_10_25_highlyCompensatedOfficerComplexType_httpwww_xbrl_orgintaward2006_10_25highlyCompensatedOfficerCompensation', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 104, 1), )

    
    highlyCompensatedOfficerCompensation = property(__highlyCompensatedOfficerCompensation.value, __highlyCompensatedOfficerCompensation.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintaward2006_10_25_highlyCompensatedOfficerComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 72, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 72, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __highlyCompensatedOfficerFirstName.name() : __highlyCompensatedOfficerFirstName,
        __highlyCompensatedOfficerMiddleInitial.name() : __highlyCompensatedOfficerMiddleInitial,
        __highlyCompensatedOfficerLastName.name() : __highlyCompensatedOfficerLastName,
        __highlyCompensatedOfficerCompensation.name() : __highlyCompensatedOfficerCompensation
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'highlyCompensatedOfficerComplexType', highlyCompensatedOfficerComplexType)


# Complex type {http://www.xbrl.org/int/award/2006-10-25}businessTypeItemType with content type SIMPLE
class businessTypeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/award/2006-10-25}businessTypeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'businessTypeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 6, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'businessTypeItemType', businessTypeItemType)


# Complex type {http://www.xbrl.org/int/award/2006-10-25}recordTypeItemType with content type SIMPLE
class recordTypeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/award/2006-10-25}recordTypeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'recordTypeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 27, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'recordTypeItemType', recordTypeItemType)


# Complex type {http://www.xbrl.org/int/award/2006-10-25}typeOfActionItemType with content type SIMPLE
class typeOfActionItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/award/2006-10-25}typeOfActionItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_2
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeOfActionItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 36, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'typeOfActionItemType', typeOfActionItemType)


# Complex type {http://www.xbrl.org/int/award/2006-10-25}typeOfTransactionCodeItemType with content type SIMPLE
class typeOfTransactionCodeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/award/2006-10-25}typeOfTransactionCodeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_3
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeOfTransactionCodeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 46, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'typeOfTransactionCodeItemType', typeOfTransactionCodeItemType)


awardDescription = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardDescription'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 78, 1))
Namespace.addCategoryObject('elementBinding', awardDescription.name().localName(), awardDescription)

parentAwardID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parentAwardID'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 79, 1))
Namespace.addCategoryObject('elementBinding', parentAwardID.name().localName(), parentAwardID)

awardeeLegalBusinessName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardeeLegalBusinessName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 80, 1))
Namespace.addCategoryObject('elementBinding', awardeeLegalBusinessName.name().localName(), awardeeLegalBusinessName)

modificationAmendmentNumber = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'modificationAmendmentNumber'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 85, 1))
Namespace.addCategoryObject('elementBinding', modificationAmendmentNumber.name().localName(), modificationAmendmentNumber)

awardeeUniqueIdentifierSupplemental = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardeeUniqueIdentifierSupplemental'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 88, 1))
Namespace.addCategoryObject('elementBinding', awardeeUniqueIdentifierSupplemental.name().localName(), awardeeUniqueIdentifierSupplemental)

ultimateParentLegalBusinessName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ultimateParentLegalBusinessName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 89, 1))
Namespace.addCategoryObject('elementBinding', ultimateParentLegalBusinessName.name().localName(), ultimateParentLegalBusinessName)

awardeeAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardeeAddress'), _ImportedBinding_gen.addressComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 90, 1))
Namespace.addCategoryObject('elementBinding', awardeeAddress.name().localName(), awardeeAddress)

primaryPlaceOfPerformance = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'primaryPlaceOfPerformance'), _ImportedBinding_gen.addressComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 91, 1))
Namespace.addCategoryObject('elementBinding', primaryPlaceOfPerformance.name().localName(), primaryPlaceOfPerformance)

awardingAgency = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardingAgency'), _ImportedBinding_gen.agencyComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 92, 1))
Namespace.addCategoryObject('elementBinding', awardingAgency.name().localName(), awardingAgency)

fundingAgency = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fundingAgency'), _ImportedBinding_gen.agencyComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 93, 1))
Namespace.addCategoryObject('elementBinding', fundingAgency.name().localName(), fundingAgency)

awardingSubTierAgency = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardingSubTierAgency'), _ImportedBinding_gen.agencyComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 94, 1))
Namespace.addCategoryObject('elementBinding', awardingSubTierAgency.name().localName(), awardingSubTierAgency)

fundingSubTierAgency = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fundingSubTierAgency'), _ImportedBinding_gen.agencyComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 95, 1))
Namespace.addCategoryObject('elementBinding', fundingSubTierAgency.name().localName(), fundingSubTierAgency)

periodOfPerformanceActionDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'periodOfPerformanceActionDate'), _ImportedBinding_xbrli.dateItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 96, 1))
Namespace.addCategoryObject('elementBinding', periodOfPerformanceActionDate.name().localName(), periodOfPerformanceActionDate)

periodOfPerformanceStartDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'periodOfPerformanceStartDate'), _ImportedBinding_xbrli.dateItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 97, 1))
Namespace.addCategoryObject('elementBinding', periodOfPerformanceStartDate.name().localName(), periodOfPerformanceStartDate)

periodOfPerformanceCurrentEndDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'periodOfPerformanceCurrentEndDate'), _ImportedBinding_xbrli.dateItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 98, 1))
Namespace.addCategoryObject('elementBinding', periodOfPerformanceCurrentEndDate.name().localName(), periodOfPerformanceCurrentEndDate)

periodOfPerformancePotentialEndDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'periodOfPerformancePotentialEndDate'), _ImportedBinding_xbrli.dateItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 99, 1))
Namespace.addCategoryObject('elementBinding', periodOfPerformancePotentialEndDate.name().localName(), periodOfPerformancePotentialEndDate)

highlyCompensatedOfficer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficer'), highlyCompensatedOfficerComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 100, 1))
Namespace.addCategoryObject('elementBinding', highlyCompensatedOfficer.name().localName(), highlyCompensatedOfficer)

highlyCompensatedOfficerFirstName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerFirstName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 101, 1))
Namespace.addCategoryObject('elementBinding', highlyCompensatedOfficerFirstName.name().localName(), highlyCompensatedOfficerFirstName)

highlyCompensatedOfficerMiddleInitial = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerMiddleInitial'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 102, 1))
Namespace.addCategoryObject('elementBinding', highlyCompensatedOfficerMiddleInitial.name().localName(), highlyCompensatedOfficerMiddleInitial)

highlyCompensatedOfficerLastName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerLastName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 103, 1))
Namespace.addCategoryObject('elementBinding', highlyCompensatedOfficerLastName.name().localName(), highlyCompensatedOfficerLastName)

businessType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'businessType'), businessTypeItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 81, 1))
Namespace.addCategoryObject('elementBinding', businessType.name().localName(), businessType)

recordType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordType'), recordTypeItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 82, 1))
Namespace.addCategoryObject('elementBinding', recordType.name().localName(), recordType)

typeOfAction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'typeOfAction'), typeOfActionItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 83, 1))
Namespace.addCategoryObject('elementBinding', typeOfAction.name().localName(), typeOfAction)

typeOfTransactionCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'typeOfTransactionCode'), typeOfTransactionCodeItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 84, 1))
Namespace.addCategoryObject('elementBinding', typeOfTransactionCode.name().localName(), typeOfTransactionCode)

ultimateParentUniqueIdentifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ultimateParentUniqueIdentifier'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 86, 1))
Namespace.addCategoryObject('elementBinding', ultimateParentUniqueIdentifier.name().localName(), ultimateParentUniqueIdentifier)

awardeeUniqueIdentifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardeeUniqueIdentifier'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 87, 1))
Namespace.addCategoryObject('elementBinding', awardeeUniqueIdentifier.name().localName(), awardeeUniqueIdentifier)

highlyCompensatedOfficerCompensation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerCompensation'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 104, 1))
Namespace.addCategoryObject('elementBinding', highlyCompensatedOfficerCompensation.name().localName(), highlyCompensatedOfficerCompensation)

federalFundingAmount = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'federalFundingAmount'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 105, 1))
Namespace.addCategoryObject('elementBinding', federalFundingAmount.name().localName(), federalFundingAmount)



highlyCompensatedOfficerComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerFirstName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=highlyCompensatedOfficerComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 101, 1)))

highlyCompensatedOfficerComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerMiddleInitial'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=highlyCompensatedOfficerComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 102, 1)))

highlyCompensatedOfficerComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerLastName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=highlyCompensatedOfficerComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 103, 1)))

highlyCompensatedOfficerComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerCompensation'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=highlyCompensatedOfficerComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 104, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 67, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 68, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 69, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 70, 5))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(highlyCompensatedOfficerComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerFirstName')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 67, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(highlyCompensatedOfficerComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerMiddleInitial')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 68, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(highlyCompensatedOfficerComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerLastName')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 69, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(highlyCompensatedOfficerComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'highlyCompensatedOfficerCompensation')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 70, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
highlyCompensatedOfficerComplexType._Automaton = _BuildAutomaton()


awardDescription._setSubstitutionGroup(_ImportedBinding_xbrli.item)

parentAwardID._setSubstitutionGroup(_ImportedBinding_xbrli.item)

awardeeLegalBusinessName._setSubstitutionGroup(_ImportedBinding_xbrli.item)

modificationAmendmentNumber._setSubstitutionGroup(_ImportedBinding_xbrli.item)

awardeeUniqueIdentifierSupplemental._setSubstitutionGroup(_ImportedBinding_xbrli.item)

ultimateParentLegalBusinessName._setSubstitutionGroup(_ImportedBinding_xbrli.item)

awardeeAddress._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

primaryPlaceOfPerformance._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

awardingAgency._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

fundingAgency._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

awardingSubTierAgency._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

fundingSubTierAgency._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

periodOfPerformanceActionDate._setSubstitutionGroup(_ImportedBinding_xbrli.item)

periodOfPerformanceStartDate._setSubstitutionGroup(_ImportedBinding_xbrli.item)

periodOfPerformanceCurrentEndDate._setSubstitutionGroup(_ImportedBinding_xbrli.item)

periodOfPerformancePotentialEndDate._setSubstitutionGroup(_ImportedBinding_xbrli.item)

highlyCompensatedOfficer._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

highlyCompensatedOfficerFirstName._setSubstitutionGroup(_ImportedBinding_xbrli.item)

highlyCompensatedOfficerMiddleInitial._setSubstitutionGroup(_ImportedBinding_xbrli.item)

highlyCompensatedOfficerLastName._setSubstitutionGroup(_ImportedBinding_xbrli.item)

businessType._setSubstitutionGroup(_ImportedBinding_xbrli.item)

recordType._setSubstitutionGroup(_ImportedBinding_xbrli.item)

typeOfAction._setSubstitutionGroup(_ImportedBinding_xbrli.item)

typeOfTransactionCode._setSubstitutionGroup(_ImportedBinding_xbrli.item)

ultimateParentUniqueIdentifier._setSubstitutionGroup(_ImportedBinding_xbrli.item)

awardeeUniqueIdentifier._setSubstitutionGroup(_ImportedBinding_xbrli.item)

highlyCompensatedOfficerCompensation._setSubstitutionGroup(_ImportedBinding_xbrli.item)

federalFundingAmount._setSubstitutionGroup(_ImportedBinding_xbrli.item)
