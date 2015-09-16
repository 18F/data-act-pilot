# ./xbrli.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:94009e0b237ef44f2a32beea3614a93f0ad71e56
# Generated 2015-09-09 15:57:00.672908 by PyXB version 1.2.4 using Python 2.7.8.final.0
# Namespace http://www.xbrl.org/2003/instance [xmlns:xbrli]

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
import _link as _ImportedBinding__link
import _xl as _ImportedBinding__xl

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.xbrl.org/2003/instance', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_link = _ImportedBinding__link.Namespace
_Namespace_link.configureCategories(['typeBinding', 'elementBinding'])

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
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 49, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.instant = STD_ANON._CF_enumeration.addEnumeration(unicode_value='instant', tag='instant')
STD_ANON.duration = STD_ANON._CF_enumeration.addEnumeration(unicode_value='duration', tag='duration')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 63, 4)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.debit = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='debit', tag='debit')
STD_ANON_.credit = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='credit', tag='credit')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: {http://www.xbrl.org/2003/instance}monetary
class monetary (pyxb.binding.datatypes.decimal):

    """
      the monetary type serves as the datatype for those financial 
      concepts in a taxonomy which denote units in a currency.
      Instance items with this type must have a unit of measure 
      from the ISO 4217 namespace of currencies.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'monetary')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 77, 2)
    _Documentation = '\n      the monetary type serves as the datatype for those financial \n      concepts in a taxonomy which denote units in a currency.\n      Instance items with this type must have a unit of measure \n      from the ISO 4217 namespace of currencies.\n      '
monetary._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'monetary', monetary)

# Atomic simple type: {http://www.xbrl.org/2003/instance}shares
class shares (pyxb.binding.datatypes.decimal):

    """
      This datatype serves as the datatype for share based 
      financial concepts.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'shares')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 89, 2)
    _Documentation = '\n      This datatype serves as the datatype for share based \n      financial concepts.\n      '
shares._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'shares', shares)

# Atomic simple type: {http://www.xbrl.org/2003/instance}pure
class pure (pyxb.binding.datatypes.decimal):

    """
      This datatype serves as the type for dimensionless numbers 
      such as percentage change, growth rates, and other ratios 
      where the numerator and denominator have the same units.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pure')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 99, 2)
    _Documentation = '\n      This datatype serves as the type for dimensionless numbers \n      such as percentage change, growth rates, and other ratios \n      where the numerator and denominator have the same units.\n      '
pure._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'pure', pure)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 119, 6)
    _Documentation = None
STD_ANON_2._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.decimal, value=pyxb.binding.datatypes.anySimpleType('0'))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_minExclusive)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 124, 6)
    _Documentation = None
STD_ANON_3._CF_maxExclusive = pyxb.binding.facets.CF_maxExclusive(value_datatype=pyxb.binding.datatypes.decimal, value=pyxb.binding.datatypes.anySimpleType('0'))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_maxExclusive)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 142, 6)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.INF = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='INF', tag='INF')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 160, 6)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.INF = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='INF', tag='INF')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 615, 16)
    _Documentation = None
STD_ANON_6._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_minLength)

# Union simple type: {http://www.xbrl.org/2003/instance}dateUnion
# superclasses pyxb.binding.datatypes.anySimpleType
class dateUnion (pyxb.binding.basis.STD_union):

    """
      The union of the date and dateTime simple types.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateUnion')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 629, 2)
    _Documentation = '\n      The union of the date and dateTime simple types.\n      '

    _MemberTypes = ( pyxb.binding.datatypes.date, pyxb.binding.datatypes.dateTime, )
dateUnion._CF_pattern = pyxb.binding.facets.CF_pattern()
dateUnion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dateUnion)
dateUnion._InitializeFacetMap(dateUnion._CF_pattern,
   dateUnion._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'dateUnion', dateUnion)

# Union simple type: {http://www.xbrl.org/2003/instance}nonZeroDecimal
# superclasses pyxb.binding.datatypes.anySimpleType
class nonZeroDecimal (pyxb.binding.basis.STD_union):

    """
      As the name implies this is a decimal value that can not take 
      the value 0 - it is used as the type for the denominator of a 
      fractionItemType.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nonZeroDecimal')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 110, 2)
    _Documentation = '\n      As the name implies this is a decimal value that can not take \n      the value 0 - it is used as the type for the denominator of a \n      fractionItemType.\n      '

    _MemberTypes = ( STD_ANON_2, STD_ANON_3, )
nonZeroDecimal._CF_pattern = pyxb.binding.facets.CF_pattern()
nonZeroDecimal._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nonZeroDecimal)
nonZeroDecimal._InitializeFacetMap(nonZeroDecimal._CF_pattern,
   nonZeroDecimal._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'nonZeroDecimal', nonZeroDecimal)

# Union simple type: {http://www.xbrl.org/2003/instance}precisionType
# superclasses pyxb.binding.datatypes.anySimpleType
class precisionType (pyxb.binding.basis.STD_union):

    """
      This type is used to specify the value of the 
      precision attribute on numeric items.  It consists 
      of the union of nonNegativeInteger and "INF" (used 
      to signify infinite precision or "exact value").
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'precisionType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 132, 2)
    _Documentation = '\n      This type is used to specify the value of the \n      precision attribute on numeric items.  It consists \n      of the union of nonNegativeInteger and "INF" (used \n      to signify infinite precision or "exact value").\n      '

    _MemberTypes = ( pyxb.binding.datatypes.nonNegativeInteger, STD_ANON_4, )
precisionType._CF_pattern = pyxb.binding.facets.CF_pattern()
precisionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=precisionType)
precisionType.INF = 'INF'                         # originally STD_ANON_4.INF
precisionType._InitializeFacetMap(precisionType._CF_pattern,
   precisionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'precisionType', precisionType)

# Union simple type: {http://www.xbrl.org/2003/instance}decimalsType
# superclasses pyxb.binding.datatypes.anySimpleType
class decimalsType (pyxb.binding.basis.STD_union):

    """
      This type is used to specify the value of the decimals attribute 
      on numeric items.  It consists of the union of integer and "INF" 
      (used to signify that a number is expressed to an infinite number 
      of decimal places or "exact value").
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'decimalsType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 150, 2)
    _Documentation = '\n      This type is used to specify the value of the decimals attribute \n      on numeric items.  It consists of the union of integer and "INF" \n      (used to signify that a number is expressed to an infinite number \n      of decimal places or "exact value").\n      '

    _MemberTypes = ( pyxb.binding.datatypes.integer, STD_ANON_5, )
decimalsType._CF_pattern = pyxb.binding.facets.CF_pattern()
decimalsType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=decimalsType)
decimalsType.INF = 'INF'                          # originally STD_ANON_5.INF
decimalsType._InitializeFacetMap(decimalsType._CF_pattern,
   decimalsType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'decimalsType', decimalsType)

# Complex type {http://www.xbrl.org/2003/instance}fractionItemType with content type ELEMENT_ONLY
class fractionItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}fractionItemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fractionItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 294, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/instance}numerator uses Python identifier numerator
    __numerator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'numerator'), 'numerator', '__httpwww_xbrl_org2003instance_fractionItemType_httpwww_xbrl_org2003instancenumerator', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 292, 2), )

    
    numerator = property(__numerator.value, __numerator.set, None, None)

    
    # Element {http://www.xbrl.org/2003/instance}denominator uses Python identifier denominator
    __denominator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'denominator'), 'denominator', '__httpwww_xbrl_org2003instance_fractionItemType_httpwww_xbrl_org2003instancedenominator', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 293, 2), )

    
    denominator = property(__denominator.value, __denominator.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_fractionItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_fractionItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_fractionItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        __numerator.name() : __numerator,
        __denominator.name() : __denominator
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef
    })
Namespace.addCategoryObject('typeBinding', 'fractionItemType', fractionItemType)


# Complex type {http://www.xbrl.org/2003/instance}stringItemType with content type SIMPLE
class stringItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}stringItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stringItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 420, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_stringItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_stringItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'stringItemType', stringItemType)


# Complex type {http://www.xbrl.org/2003/instance}booleanItemType with content type SIMPLE
class booleanItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}booleanItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.boolean
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'booleanItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 428, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.boolean
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_booleanItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_booleanItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'booleanItemType', booleanItemType)


# Complex type {http://www.xbrl.org/2003/instance}hexBinaryItemType with content type SIMPLE
class hexBinaryItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}hexBinaryItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.hexBinary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'hexBinaryItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 436, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.hexBinary
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_hexBinaryItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_hexBinaryItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'hexBinaryItemType', hexBinaryItemType)


# Complex type {http://www.xbrl.org/2003/instance}base64BinaryItemType with content type SIMPLE
class base64BinaryItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}base64BinaryItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'base64BinaryItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 444, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.base64Binary
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_base64BinaryItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_base64BinaryItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'base64BinaryItemType', base64BinaryItemType)


# Complex type {http://www.xbrl.org/2003/instance}anyURIItemType with content type SIMPLE
class anyURIItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}anyURIItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'anyURIItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 452, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_anyURIItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_anyURIItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'anyURIItemType', anyURIItemType)


# Complex type {http://www.xbrl.org/2003/instance}QNameItemType with content type SIMPLE
class QNameItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}QNameItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.QName
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QNameItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 460, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.QName
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_QNameItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_QNameItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'QNameItemType', QNameItemType)


# Complex type {http://www.xbrl.org/2003/instance}durationItemType with content type SIMPLE
class durationItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}durationItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.duration
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'durationItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 468, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.duration
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_durationItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_durationItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'durationItemType', durationItemType)


# Complex type {http://www.xbrl.org/2003/instance}timeItemType with content type SIMPLE
class timeItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}timeItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.time
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 484, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.time
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_timeItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_timeItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'timeItemType', timeItemType)


# Complex type {http://www.xbrl.org/2003/instance}dateItemType with content type SIMPLE
class dateItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}dateItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.date
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 492, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.date
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_dateItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_dateItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'dateItemType', dateItemType)


# Complex type {http://www.xbrl.org/2003/instance}gYearMonthItemType with content type SIMPLE
class gYearMonthItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}gYearMonthItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.gYearMonth
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gYearMonthItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 500, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.gYearMonth
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_gYearMonthItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_gYearMonthItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'gYearMonthItemType', gYearMonthItemType)


# Complex type {http://www.xbrl.org/2003/instance}gYearItemType with content type SIMPLE
class gYearItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}gYearItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.gYear
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gYearItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 508, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.gYear
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_gYearItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_gYearItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'gYearItemType', gYearItemType)


# Complex type {http://www.xbrl.org/2003/instance}gMonthDayItemType with content type SIMPLE
class gMonthDayItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}gMonthDayItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.gMonthDay
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gMonthDayItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 516, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.gMonthDay
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_gMonthDayItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_gMonthDayItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'gMonthDayItemType', gMonthDayItemType)


# Complex type {http://www.xbrl.org/2003/instance}gDayItemType with content type SIMPLE
class gDayItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}gDayItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.gDay
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gDayItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 524, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.gDay
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_gDayItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_gDayItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'gDayItemType', gDayItemType)


# Complex type {http://www.xbrl.org/2003/instance}gMonthItemType with content type SIMPLE
class gMonthItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}gMonthItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.gMonth
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gMonthItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 532, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.gMonth
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_gMonthItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_gMonthItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'gMonthItemType', gMonthItemType)


# Complex type {http://www.xbrl.org/2003/instance}normalizedStringItemType with content type SIMPLE
class normalizedStringItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}normalizedStringItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'normalizedStringItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 547, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.normalizedString
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_normalizedStringItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_normalizedStringItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'normalizedStringItemType', normalizedStringItemType)


# Complex type {http://www.xbrl.org/2003/instance}tokenItemType with content type SIMPLE
class tokenItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}tokenItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.token
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tokenItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 555, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.token
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_tokenItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_tokenItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'tokenItemType', tokenItemType)


# Complex type {http://www.xbrl.org/2003/instance}languageItemType with content type SIMPLE
class languageItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}languageItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.language
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'languageItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 563, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.language
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_languageItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_languageItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'languageItemType', languageItemType)


# Complex type {http://www.xbrl.org/2003/instance}NameItemType with content type SIMPLE
class NameItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}NameItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.Name
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 571, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.Name
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_NameItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_NameItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'NameItemType', NameItemType)


# Complex type {http://www.xbrl.org/2003/instance}NCNameItemType with content type SIMPLE
class NCNameItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}NCNameItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.NCName
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NCNameItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 579, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.NCName
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_NCNameItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_NCNameItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'NCNameItemType', NCNameItemType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 594, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type {http://www.xbrl.org/2003/instance}contextEntityType with content type ELEMENT_ONLY
class contextEntityType (pyxb.binding.basis.complexTypeDefinition):
    """
      The type for the entity element, used to describe the reporting entity.
      Note that the scheme attribute is required and cannot be empty.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'contextEntityType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 602, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/instance}segment uses Python identifier segment
    __segment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'segment'), 'segment', '__httpwww_xbrl_org2003instance_contextEntityType_httpwww_xbrl_org2003instancesegment', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 593, 2), )

    
    segment = property(__segment.value, __segment.set, None, None)

    
    # Element {http://www.xbrl.org/2003/instance}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'identifier'), 'identifier', '__httpwww_xbrl_org2003instance_contextEntityType_httpwww_xbrl_org2003instanceidentifier', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 610, 6), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    _ElementMap.update({
        __segment.name() : __segment,
        __identifier.name() : __identifier
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'contextEntityType', contextEntityType)


# Complex type {http://www.xbrl.org/2003/instance}contextPeriodType with content type ELEMENT_ONLY
class contextPeriodType (pyxb.binding.basis.complexTypeDefinition):
    """
      The type for the period element, used to describe the reporting date info.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'contextPeriodType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 638, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/instance}startDate uses Python identifier startDate
    __startDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startDate'), 'startDate', '__httpwww_xbrl_org2003instance_contextPeriodType_httpwww_xbrl_org2003instancestartDate', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 646, 8), )

    
    startDate = property(__startDate.value, __startDate.set, None, None)

    
    # Element {http://www.xbrl.org/2003/instance}endDate uses Python identifier endDate
    __endDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endDate'), 'endDate', '__httpwww_xbrl_org2003instance_contextPeriodType_httpwww_xbrl_org2003instanceendDate', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 647, 8), )

    
    endDate = property(__endDate.value, __endDate.set, None, None)

    
    # Element {http://www.xbrl.org/2003/instance}instant uses Python identifier instant
    __instant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'instant'), 'instant', '__httpwww_xbrl_org2003instance_contextPeriodType_httpwww_xbrl_org2003instanceinstant', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 649, 6), )

    
    instant = property(__instant.value, __instant.set, None, None)

    
    # Element {http://www.xbrl.org/2003/instance}forever uses Python identifier forever
    __forever = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'forever'), 'forever', '__httpwww_xbrl_org2003instance_contextPeriodType_httpwww_xbrl_org2003instanceforever', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 650, 6), )

    
    forever = property(__forever.value, __forever.set, None, None)

    _ElementMap.update({
        __startDate.name() : __startDate,
        __endDate.name() : __endDate,
        __instant.name() : __instant,
        __forever.name() : __forever
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'contextPeriodType', contextPeriodType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 651, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type {http://www.xbrl.org/2003/instance}contextScenarioType with content type ELEMENT_ONLY
class contextScenarioType (pyxb.binding.basis.complexTypeDefinition):
    """
      Used for the scenario under which fact have been reported.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'contextScenarioType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 656, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'contextScenarioType', contextScenarioType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
      Used for an island of context to which facts can be related.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 674, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/instance}entity uses Python identifier entity
    __entity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entity'), 'entity', '__httpwww_xbrl_org2003instance_CTD_ANON_2_httpwww_xbrl_org2003instanceentity', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 676, 8), )

    
    entity = property(__entity.value, __entity.set, None, None)

    
    # Element {http://www.xbrl.org/2003/instance}period uses Python identifier period
    __period = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'period'), 'period', '__httpwww_xbrl_org2003instance_CTD_ANON_2_httpwww_xbrl_org2003instanceperiod', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 677, 8), )

    
    period = property(__period.value, __period.set, None, None)

    
    # Element {http://www.xbrl.org/2003/instance}scenario uses Python identifier scenario
    __scenario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scenario'), 'scenario', '__httpwww_xbrl_org2003instance_CTD_ANON_2_httpwww_xbrl_org2003instancescenario', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 678, 8), )

    
    scenario = property(__scenario.value, __scenario.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_CTD_ANON_2_id', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 680, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 680, 6)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __entity.name() : __entity,
        __period.name() : __period,
        __scenario.name() : __scenario
    })
    _AttributeMap.update({
        __id.name() : __id
    })



# Complex type {http://www.xbrl.org/2003/instance}measuresType with content type ELEMENT_ONLY
class measuresType (pyxb.binding.basis.complexTypeDefinition):
    """
      A collection of sibling measure elements
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'measuresType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 692, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/instance}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwww_xbrl_org2003instance_measuresType_httpwww_xbrl_org2003instancemeasure', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 690, 2), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'measuresType', measuresType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
      Element used to represent division in units
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 709, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/instance}unitNumerator uses Python identifier unitNumerator
    __unitNumerator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unitNumerator'), 'unitNumerator', '__httpwww_xbrl_org2003instance_CTD_ANON_3_httpwww_xbrl_org2003instanceunitNumerator', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 711, 8), )

    
    unitNumerator = property(__unitNumerator.value, __unitNumerator.set, None, None)

    
    # Element {http://www.xbrl.org/2003/instance}unitDenominator uses Python identifier unitDenominator
    __unitDenominator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unitDenominator'), 'unitDenominator', '__httpwww_xbrl_org2003instance_CTD_ANON_3_httpwww_xbrl_org2003instanceunitDenominator', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 712, 8), )

    
    unitDenominator = property(__unitDenominator.value, __unitDenominator.set, None, None)

    _ElementMap.update({
        __unitNumerator.name() : __unitNumerator,
        __unitDenominator.name() : __unitDenominator
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """
      Element used to represent units information about numeric items
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 723, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/instance}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwww_xbrl_org2003instance_CTD_ANON_4_httpwww_xbrl_org2003instancemeasure', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 690, 2), )

    
    measure = property(__measure.value, __measure.set, None, None)

    
    # Element {http://www.xbrl.org/2003/instance}divide uses Python identifier divide
    __divide = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'divide'), 'divide', '__httpwww_xbrl_org2003instance_CTD_ANON_4_httpwww_xbrl_org2003instancedivide', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 703, 2), )

    
    divide = property(__divide.value, __divide.set, None, '\n      Element used to represent division in units\n      ')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_CTD_ANON_4_id', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 728, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 728, 6)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __measure.name() : __measure,
        __divide.name() : __divide
    })
    _AttributeMap.update({
        __id.name() : __id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """
      XBRL instance root element.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 760, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/instance}context uses Python identifier context
    __context = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'context'), 'context', '__httpwww_xbrl_org2003instance_CTD_ANON_5_httpwww_xbrl_org2003instancecontext', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 668, 2), )

    
    context = property(__context.value, __context.set, None, '\n      Used for an island of context to which facts can be related.\n      ')

    
    # Element {http://www.xbrl.org/2003/instance}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwww_xbrl_org2003instance_CTD_ANON_5_httpwww_xbrl_org2003instanceunit', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 717, 2), )

    
    unit = property(__unit.value, __unit.set, None, '\n      Element used to represent units information about numeric items\n      ')

    
    # Element {http://www.xbrl.org/2003/instance}item uses Python identifier item
    __item = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'item'), 'item', '__httpwww_xbrl_org2003instance_CTD_ANON_5_httpwww_xbrl_org2003instanceitem', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 738, 2), )

    
    item = property(__item.value, __item.set, None, '\n      Abstract item element used as head of item substitution group\n      ')

    
    # Element {http://www.xbrl.org/2003/instance}tuple uses Python identifier tuple
    __tuple = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tuple'), 'tuple', '__httpwww_xbrl_org2003instance_CTD_ANON_5_httpwww_xbrl_org2003instancetuple', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 746, 2), )

    
    tuple = property(__tuple.value, __tuple.set, None, '\n      Abstract tuple element used as head of tuple substitution group\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}footnoteLink uses Python identifier footnoteLink
    __footnoteLink = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_link, 'footnoteLink'), 'footnoteLink', '__httpwww_xbrl_org2003instance_CTD_ANON_5_httpwww_xbrl_org2003linkbasefootnoteLink', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 301, 2), )

    
    footnoteLink = property(__footnoteLink.value, __footnoteLink.set, None, '\n      footnote extended link element definition\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}linkbaseRef uses Python identifier linkbaseRef
    __linkbaseRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_link, 'linkbaseRef'), 'linkbaseRef', '__httpwww_xbrl_org2003instance_CTD_ANON_5_httpwww_xbrl_org2003linkbaselinkbaseRef', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 342, 2), )

    
    linkbaseRef = property(__linkbaseRef.value, __linkbaseRef.set, None, '\n      Definition of the linkbaseRef element - used \n      to link to XBRL taxonomy extended links from \n      taxonomy schema documents and from XBRL\n      instances.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}schemaRef uses Python identifier schemaRef
    __schemaRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_link, 'schemaRef'), 'schemaRef', '__httpwww_xbrl_org2003instance_CTD_ANON_5_httpwww_xbrl_org2003linkbaseschemaRef', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 368, 2), )

    
    schemaRef = property(__schemaRef.value, __schemaRef.set, None, '\n      Definition of the schemaRef element - used \n      to link to XBRL taxonomy schemas from \n      XBRL instances.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}roleRef uses Python identifier roleRef
    __roleRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_link, 'roleRef'), 'roleRef', '__httpwww_xbrl_org2003instance_CTD_ANON_5_httpwww_xbrl_org2003linkbaseroleRef', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 378, 2), )

    
    roleRef = property(__roleRef.value, __roleRef.set, None, '\n      Definition of the roleRef element - used \n      to link to resolve xlink:role attribute values to \n      the roleType element declaration.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}arcroleRef uses Python identifier arcroleRef
    __arcroleRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_link, 'arcroleRef'), 'arcroleRef', '__httpwww_xbrl_org2003instance_CTD_ANON_5_httpwww_xbrl_org2003linkbasearcroleRef', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 401, 2), )

    
    arcroleRef = property(__arcroleRef.value, __arcroleRef.set, None, '\n      Definition of the roleRef element - used \n      to link to resolve xlink:arcrole attribute values to \n      the arcroleType element declaration.\n      ')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_CTD_ANON_5_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 774, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 774, 6)
    
    id = property(__id.value, __id.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        __context.name() : __context,
        __unit.name() : __unit,
        __item.name() : __item,
        __tuple.name() : __tuple,
        __footnoteLink.name() : __footnoteLink,
        __linkbaseRef.name() : __linkbaseRef,
        __schemaRef.name() : __schemaRef,
        __roleRef.name() : __roleRef,
        __arcroleRef.name() : __arcroleRef
    })
    _AttributeMap.update({
        __id.name() : __id
    })



# Complex type {http://www.xbrl.org/2003/instance}dateTimeItemType with content type SIMPLE
class dateTimeItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}dateTimeItemType with content type SIMPLE"""
    _TypeDefinition = dateUnion
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateTimeItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 476, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is dateUnion
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_dateTimeItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_dateTimeItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef
    })
Namespace.addCategoryObject('typeBinding', 'dateTimeItemType', dateTimeItemType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.token
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 611, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.token
    
    # Attribute scheme uses Python identifier scheme
    __scheme = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scheme'), 'scheme', '__httpwww_xbrl_org2003instance_CTD_ANON_6_scheme', STD_ANON_6, required=True)
    __scheme._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 614, 14)
    __scheme._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 614, 14)
    
    scheme = property(__scheme.value, __scheme.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __scheme.name() : __scheme
    })



# Complex type {http://www.xbrl.org/2003/instance}decimalItemType with content type SIMPLE
class decimalItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}decimalItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'decimalItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 235, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_decimalItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_decimalItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_decimalItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_decimalItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_decimalItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'decimalItemType', decimalItemType)


# Complex type {http://www.xbrl.org/2003/instance}floatItemType with content type SIMPLE
class floatItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}floatItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.float
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'floatItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 243, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.float
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_floatItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_floatItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_floatItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_floatItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_floatItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'floatItemType', floatItemType)


# Complex type {http://www.xbrl.org/2003/instance}doubleItemType with content type SIMPLE
class doubleItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}doubleItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'doubleItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 251, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_doubleItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_doubleItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_doubleItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_doubleItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_doubleItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'doubleItemType', doubleItemType)


# Complex type {http://www.xbrl.org/2003/instance}monetaryItemType with content type SIMPLE
class monetaryItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}monetaryItemType with content type SIMPLE"""
    _TypeDefinition = monetary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'monetaryItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 268, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is monetary
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_monetaryItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_monetaryItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_monetaryItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_monetaryItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_monetaryItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'monetaryItemType', monetaryItemType)


# Complex type {http://www.xbrl.org/2003/instance}sharesItemType with content type SIMPLE
class sharesItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}sharesItemType with content type SIMPLE"""
    _TypeDefinition = shares
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sharesItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 276, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is shares
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_sharesItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_sharesItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_sharesItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_sharesItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_sharesItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'sharesItemType', sharesItemType)


# Complex type {http://www.xbrl.org/2003/instance}pureItemType with content type SIMPLE
class pureItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}pureItemType with content type SIMPLE"""
    _TypeDefinition = pure
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pureItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 284, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pure
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_pureItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_pureItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_pureItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_pureItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_pureItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'pureItemType', pureItemType)


# Complex type {http://www.xbrl.org/2003/instance}integerItemType with content type SIMPLE
class integerItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}integerItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.integer
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'integerItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 309, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.integer
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_integerItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_integerItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_integerItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_integerItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_integerItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'integerItemType', integerItemType)


# Complex type {http://www.xbrl.org/2003/instance}nonPositiveIntegerItemType with content type SIMPLE
class nonPositiveIntegerItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}nonPositiveIntegerItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.nonPositiveInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nonPositiveIntegerItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 317, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.nonPositiveInteger
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_nonPositiveIntegerItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_nonPositiveIntegerItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_nonPositiveIntegerItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_nonPositiveIntegerItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_nonPositiveIntegerItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'nonPositiveIntegerItemType', nonPositiveIntegerItemType)


# Complex type {http://www.xbrl.org/2003/instance}negativeIntegerItemType with content type SIMPLE
class negativeIntegerItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}negativeIntegerItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.negativeInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'negativeIntegerItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 325, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.negativeInteger
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_negativeIntegerItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_negativeIntegerItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_negativeIntegerItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_negativeIntegerItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_negativeIntegerItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'negativeIntegerItemType', negativeIntegerItemType)


# Complex type {http://www.xbrl.org/2003/instance}longItemType with content type SIMPLE
class longItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}longItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.long
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'longItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 333, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.long
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_longItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_longItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_longItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_longItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_longItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'longItemType', longItemType)


# Complex type {http://www.xbrl.org/2003/instance}intItemType with content type SIMPLE
class intItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}intItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.int
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'intItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 341, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.int
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_intItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_intItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_intItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_intItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_intItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'intItemType', intItemType)


# Complex type {http://www.xbrl.org/2003/instance}shortItemType with content type SIMPLE
class shortItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}shortItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.short
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'shortItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 349, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.short
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_shortItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_shortItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_shortItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_shortItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_shortItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'shortItemType', shortItemType)


# Complex type {http://www.xbrl.org/2003/instance}byteItemType with content type SIMPLE
class byteItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}byteItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.byte
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'byteItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 357, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.byte
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_byteItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_byteItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_byteItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_byteItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_byteItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'byteItemType', byteItemType)


# Complex type {http://www.xbrl.org/2003/instance}nonNegativeIntegerItemType with content type SIMPLE
class nonNegativeIntegerItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}nonNegativeIntegerItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.nonNegativeInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nonNegativeIntegerItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 365, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.nonNegativeInteger
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_nonNegativeIntegerItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_nonNegativeIntegerItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_nonNegativeIntegerItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_nonNegativeIntegerItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_nonNegativeIntegerItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'nonNegativeIntegerItemType', nonNegativeIntegerItemType)


# Complex type {http://www.xbrl.org/2003/instance}unsignedLongItemType with content type SIMPLE
class unsignedLongItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}unsignedLongItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.unsignedLong
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unsignedLongItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 373, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.unsignedLong
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_unsignedLongItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_unsignedLongItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_unsignedLongItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_unsignedLongItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_unsignedLongItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'unsignedLongItemType', unsignedLongItemType)


# Complex type {http://www.xbrl.org/2003/instance}unsignedIntItemType with content type SIMPLE
class unsignedIntItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}unsignedIntItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.unsignedInt
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unsignedIntItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 381, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.unsignedInt
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_unsignedIntItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_unsignedIntItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_unsignedIntItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_unsignedIntItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_unsignedIntItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'unsignedIntItemType', unsignedIntItemType)


# Complex type {http://www.xbrl.org/2003/instance}unsignedShortItemType with content type SIMPLE
class unsignedShortItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}unsignedShortItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.unsignedShort
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unsignedShortItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 389, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.unsignedShort
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_unsignedShortItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_unsignedShortItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_unsignedShortItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_unsignedShortItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_unsignedShortItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'unsignedShortItemType', unsignedShortItemType)


# Complex type {http://www.xbrl.org/2003/instance}unsignedByteItemType with content type SIMPLE
class unsignedByteItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}unsignedByteItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.unsignedByte
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unsignedByteItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 397, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.unsignedByte
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_unsignedByteItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_unsignedByteItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_unsignedByteItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_unsignedByteItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_unsignedByteItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'unsignedByteItemType', unsignedByteItemType)


# Complex type {http://www.xbrl.org/2003/instance}positiveIntegerItemType with content type SIMPLE
class positiveIntegerItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/2003/instance}positiveIntegerItemType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.positiveInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'positiveIntegerItemType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 405, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.positiveInteger
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003instance_positiveIntegerItemType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 174, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute contextRef uses Python identifier contextRef
    __contextRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contextRef'), 'contextRef', '__httpwww_xbrl_org2003instance_positiveIntegerItemType_contextRef', pyxb.binding.datatypes.IDREF, required=True)
    __contextRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    __contextRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 194, 4)
    
    contextRef = property(__contextRef.value, __contextRef.set, None, None)

    
    # Attribute unitRef uses Python identifier unitRef
    __unitRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitRef'), 'unitRef', '__httpwww_xbrl_org2003instance_positiveIntegerItemType_unitRef', pyxb.binding.datatypes.IDREF, required=True)
    __unitRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    __unitRef._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 204, 4)
    
    unitRef = property(__unitRef.value, __unitRef.set, None, None)

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__httpwww_xbrl_org2003instance_positiveIntegerItemType_precision', precisionType)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    __precision._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 214, 4)
    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Attribute decimals uses Python identifier decimals
    __decimals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimals'), 'decimals', '__httpwww_xbrl_org2003instance_positiveIntegerItemType_decimals', decimalsType)
    __decimals._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    __decimals._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 215, 4)
    
    decimals = property(__decimals.value, __decimals.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __contextRef.name() : __contextRef,
        __unitRef.name() : __unitRef,
        __precision.name() : __precision,
        __decimals.name() : __decimals
    })
Namespace.addCategoryObject('typeBinding', 'positiveIntegerItemType', positiveIntegerItemType)


numerator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'numerator'), pyxb.binding.datatypes.decimal, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 292, 2))
Namespace.addCategoryObject('elementBinding', numerator.name().localName(), numerator)

measure = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), pyxb.binding.datatypes.QName, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 690, 2))
Namespace.addCategoryObject('elementBinding', measure.name().localName(), measure)

item = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'item'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), documentation='\n      Abstract item element used as head of item substitution group\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 738, 2))
Namespace.addCategoryObject('elementBinding', item.name().localName(), item)

tuple = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tuple'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), documentation='\n      Abstract tuple element used as head of tuple substitution group\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 746, 2))
Namespace.addCategoryObject('elementBinding', tuple.name().localName(), tuple)

segment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'segment'), CTD_ANON, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 593, 2))
Namespace.addCategoryObject('elementBinding', segment.name().localName(), segment)

context = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'context'), CTD_ANON_2, documentation='\n      Used for an island of context to which facts can be related.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 668, 2))
Namespace.addCategoryObject('elementBinding', context.name().localName(), context)

divide = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'divide'), CTD_ANON_3, documentation='\n      Element used to represent division in units\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 703, 2))
Namespace.addCategoryObject('elementBinding', divide.name().localName(), divide)

unit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), CTD_ANON_4, documentation='\n      Element used to represent units information about numeric items\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 717, 2))
Namespace.addCategoryObject('elementBinding', unit.name().localName(), unit)

xbrl = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xbrl'), CTD_ANON_5, documentation='\n      XBRL instance root element.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 754, 2))
Namespace.addCategoryObject('elementBinding', xbrl.name().localName(), xbrl)

denominator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'denominator'), nonZeroDecimal, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 293, 2))
Namespace.addCategoryObject('elementBinding', denominator.name().localName(), denominator)



fractionItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'numerator'), pyxb.binding.datatypes.decimal, scope=fractionItemType, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 292, 2)))

fractionItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'denominator'), nonZeroDecimal, scope=fractionItemType, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 293, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fractionItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'numerator')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 296, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fractionItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'denominator')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 297, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
fractionItemType._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 596, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




contextEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'segment'), CTD_ANON, scope=contextEntityType, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 593, 2)))

contextEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifier'), CTD_ANON_6, scope=contextEntityType, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 610, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 625, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(contextEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'identifier')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 610, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(contextEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'segment')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 625, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
contextEntityType._Automaton = _BuildAutomaton_2()




contextPeriodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startDate'), dateUnion, scope=contextPeriodType, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 646, 8)))

contextPeriodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endDate'), dateUnion, scope=contextPeriodType, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 647, 8)))

contextPeriodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'instant'), dateUnion, scope=contextPeriodType, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 649, 6)))

contextPeriodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'forever'), CTD_ANON_, scope=contextPeriodType, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 650, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(contextPeriodType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startDate')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 646, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(contextPeriodType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endDate')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 647, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(contextPeriodType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instant')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 649, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(contextPeriodType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'forever')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 650, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
contextPeriodType._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/instance')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 663, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
contextScenarioType._Automaton = _BuildAutomaton_4()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entity'), contextEntityType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 676, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'period'), contextPeriodType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 677, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scenario'), contextScenarioType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 678, 8)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 678, 8))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entity')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 676, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'period')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 677, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scenario')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 678, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_5()




measuresType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), pyxb.binding.datatypes.QName, scope=measuresType, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 690, 2)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(measuresType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 699, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
measuresType._Automaton = _BuildAutomaton_6()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unitNumerator'), measuresType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 711, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unitDenominator'), measuresType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 712, 8)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unitNumerator')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 711, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unitDenominator')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 712, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_7()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), pyxb.binding.datatypes.QName, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 690, 2)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'divide'), CTD_ANON_3, scope=CTD_ANON_4, documentation='\n      Element used to represent division in units\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 703, 2)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 725, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'divide')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 726, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_8()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'context'), CTD_ANON_2, scope=CTD_ANON_5, documentation='\n      Used for an island of context to which facts can be related.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 668, 2)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), CTD_ANON_4, scope=CTD_ANON_5, documentation='\n      Element used to represent units information about numeric items\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 717, 2)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'item'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_5, documentation='\n      Abstract item element used as head of item substitution group\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 738, 2)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tuple'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_5, documentation='\n      Abstract tuple element used as head of tuple substitution group\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 746, 2)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_link, 'footnoteLink'), _ImportedBinding__link.CTD_ANON_13, scope=CTD_ANON_5, documentation='\n      footnote extended link element definition\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 301, 2)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_link, 'linkbaseRef'), _ImportedBinding__link.CTD_ANON_14, scope=CTD_ANON_5, documentation='\n      Definition of the linkbaseRef element - used \n      to link to XBRL taxonomy extended links from \n      taxonomy schema documents and from XBRL\n      instances.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 342, 2)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_link, 'schemaRef'), _ImportedBinding__xl.simpleType, scope=CTD_ANON_5, documentation='\n      Definition of the schemaRef element - used \n      to link to XBRL taxonomy schemas from \n      XBRL instances.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 368, 2)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_link, 'roleRef'), _ImportedBinding__link.CTD_ANON_15, scope=CTD_ANON_5, documentation='\n      Definition of the roleRef element - used \n      to link to resolve xlink:role attribute values to \n      the roleType element declaration.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 378, 2)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_link, 'arcroleRef'), _ImportedBinding__link.CTD_ANON_16, scope=CTD_ANON_5, documentation='\n      Definition of the roleRef element - used \n      to link to resolve xlink:arcrole attribute values to \n      the arcroleType element declaration.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 401, 2)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 763, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 764, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 765, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 766, 8))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_link, 'schemaRef')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 762, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_link, 'linkbaseRef')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 763, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_link, 'roleRef')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 764, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_link, 'arcroleRef')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 765, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'item')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 767, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tuple')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 768, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'context')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 769, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 770, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_link, 'footnoteLink')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd', 771, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_9()

