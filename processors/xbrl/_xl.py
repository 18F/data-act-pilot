# ./_xl.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ad12a45a799f18105282934aafc838c6d701716c
# Generated 2015-09-09 15:57:00.672255 by PyXB version 1.2.4 using Python 2.7.8.final.0
# Namespace http://www.xbrl.org/2003/XLink [xmlns:xl]

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
import _xlink as _ImportedBinding__xlink

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.xbrl.org/2003/XLink', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xlink = _ImportedBinding__xlink.Namespace
_Namespace_xlink.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://www.xbrl.org/2003/XLink}nonEmptyURI
class nonEmptyURI (pyxb.binding.datatypes.anyURI):

    """
      A URI type with a minimum length of 1 character.
      Used on role and arcrole and href elements.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nonEmptyURI')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 30, 2)
    _Documentation = '\n      A URI type with a minimum length of 1 character.\n      Used on role and arcrole and href elements.\n      '
nonEmptyURI._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
nonEmptyURI._InitializeFacetMap(nonEmptyURI._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'nonEmptyURI', nonEmptyURI)

# Atomic simple type: {http://www.xbrl.org/2003/XLink}useEnum
class useEnum (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """
      Enumerated values for the use attribute on extended link arcs.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'useEnum')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 123, 2)
    _Documentation = '\n      Enumerated values for the use attribute on extended link arcs.\n      '
useEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=useEnum, enum_prefix=None)
useEnum.optional = useEnum._CF_enumeration.addEnumeration(unicode_value='optional', tag='optional')
useEnum.prohibited = useEnum._CF_enumeration.addEnumeration(unicode_value='prohibited', tag='prohibited')
useEnum._InitializeFacetMap(useEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'useEnum', useEnum)

# Complex type {http://www.xbrl.org/2003/XLink}documentationType with content type SIMPLE
class documentationType (pyxb.binding.basis.complexTypeDefinition):
    """
      Element type to use for documentation of 
      extended links and linkbases.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'documentationType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 43, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/XLink'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'documentationType', documentationType)


# Complex type {http://www.xbrl.org/2003/XLink}titleType with content type EMPTY
class titleType (pyxb.binding.basis.complexTypeDefinition):
    """
      Type for the abstract title element - 
      used as a title element template.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'titleType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 72, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_xbrl_org2003XLink_titleType_httpwww_w3_org1999xlinktype', _ImportedBinding__xlink.STD_ANON, fixed=True, unicode_default='title', required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 34, 2)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 81, 5)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'titleType', titleType)


# Complex type {http://www.xbrl.org/2003/XLink}locatorType with content type ELEMENT_ONLY
class locatorType (pyxb.binding.basis.complexTypeDefinition):
    """
      Generic locator type.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locatorType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 95, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/XLink}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__httpwww_xbrl_org2003XLink_locatorType_httpwww_xbrl_org2003XLinktitle', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 85, 2), )

    
    title = property(__title.value, __title.set, None, '\n      Generic title element for use in extended link documentation.\n      Used on extended links, arcs, locators.\n      See http://www.w3.org/TR/xlink/#title-element for details.\n      ')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_xbrl_org2003XLink_locatorType_httpwww_w3_org1999xlinktype', _ImportedBinding__xlink.STD_ANON, fixed=True, unicode_default='locator', required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 34, 2)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 106, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_xbrl_org2003XLink_locatorType_httpwww_w3_org1999xlinkrole', _ImportedBinding__xlink.STD_ANON_)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 52, 2)
    __role._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 109, 8)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title_
    __title_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title_', '__httpwww_xbrl_org2003XLink_locatorType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title_._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 78, 2)
    __title_._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 110, 8)
    
    title_ = property(__title_.value, __title_.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'label'), 'label', '__httpwww_xbrl_org2003XLink_locatorType_httpwww_w3_org1999xlinklabel', pyxb.binding.datatypes.NCName, required=True)
    __label._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 113, 2)
    __label._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 108, 8)
    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_xbrl_org2003XLink_locatorType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 119, 2)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 107, 8)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        __title.name() : __title
    })
    _AttributeMap.update({
        __type.name() : __type,
        __role.name() : __role,
        __title_.name() : __title_,
        __label.name() : __label,
        __href.name() : __href
    })
Namespace.addCategoryObject('typeBinding', 'locatorType', locatorType)


# Complex type {http://www.xbrl.org/2003/XLink}arcType with content type ELEMENT_ONLY
class arcType (pyxb.binding.basis.complexTypeDefinition):
    """
      basic extended link arc type - extended where necessary for specific arcs
      Extends the generic arc type by adding use, priority and order attributes.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'arcType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 135, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/XLink}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__httpwww_xbrl_org2003XLink_arcType_httpwww_xbrl_org2003XLinktitle', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 85, 2), )

    
    title = property(__title.value, __title.set, None, '\n      Generic title element for use in extended link documentation.\n      Used on extended links, arcs, locators.\n      See http://www.w3.org/TR/xlink/#title-element for details.\n      ')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_xbrl_org2003XLink_arcType_httpwww_w3_org1999xlinktype', _ImportedBinding__xlink.STD_ANON, fixed=True, unicode_default='arc', required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 34, 2)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 147, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_xbrl_org2003XLink_arcType_httpwww_w3_org1999xlinkarcrole', _ImportedBinding__xlink.STD_ANON_2, required=True)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 65, 2)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 150, 8)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title_
    __title_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title_', '__httpwww_xbrl_org2003XLink_arcType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title_._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 78, 2)
    __title_._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 151, 8)
    
    title_ = property(__title_.value, __title_.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_xbrl_org2003XLink_arcType_httpwww_w3_org1999xlinkshow', _ImportedBinding__xlink.STD_ANON_3)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 80, 2)
    __show._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 152, 8)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_xbrl_org2003XLink_arcType_httpwww_w3_org1999xlinkactuate', _ImportedBinding__xlink.STD_ANON_4)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 97, 2)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 153, 8)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'from'), 'from_', '__httpwww_xbrl_org2003XLink_arcType_httpwww_w3_org1999xlinkfrom', pyxb.binding.datatypes.NCName, required=True)
    __from._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 115, 2)
    __from._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 148, 8)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'to'), 'to', '__httpwww_xbrl_org2003XLink_arcType_httpwww_w3_org1999xlinkto', pyxb.binding.datatypes.NCName, required=True)
    __to._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 117, 2)
    __to._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 149, 8)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute order uses Python identifier order
    __order = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'order'), 'order', '__httpwww_xbrl_org2003XLink_arcType_order', pyxb.binding.datatypes.decimal)
    __order._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 154, 8)
    __order._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 154, 8)
    
    order = property(__order.value, __order.set, None, None)

    
    # Attribute use uses Python identifier use
    __use = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'use'), 'use', '__httpwww_xbrl_org2003XLink_arcType_use', useEnum)
    __use._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 155, 8)
    __use._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 155, 8)
    
    use = property(__use.value, __use.set, None, None)

    
    # Attribute priority uses Python identifier priority
    __priority = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'priority'), 'priority', '__httpwww_xbrl_org2003XLink_arcType_priority', pyxb.binding.datatypes.integer)
    __priority._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 156, 8)
    __priority._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 156, 8)
    
    priority = property(__priority.value, __priority.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/XLink'))
    _ElementMap.update({
        __title.name() : __title
    })
    _AttributeMap.update({
        __type.name() : __type,
        __arcrole.name() : __arcrole,
        __title_.name() : __title_,
        __show.name() : __show,
        __actuate.name() : __actuate,
        __from.name() : __from,
        __to.name() : __to,
        __order.name() : __order,
        __use.name() : __use,
        __priority.name() : __priority
    })
Namespace.addCategoryObject('typeBinding', 'arcType', arcType)


# Complex type {http://www.xbrl.org/2003/XLink}resourceType with content type MIXED
class resourceType (pyxb.binding.basis.complexTypeDefinition):
    """
      Generic type for the resource type element
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'resourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 169, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_xbrl_org2003XLink_resourceType_httpwww_w3_org1999xlinktype', _ImportedBinding__xlink.STD_ANON, fixed=True, unicode_default='resource', required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 34, 2)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 177, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_xbrl_org2003XLink_resourceType_httpwww_w3_org1999xlinkrole', _ImportedBinding__xlink.STD_ANON_)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 52, 2)
    __role._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 179, 8)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_xbrl_org2003XLink_resourceType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 78, 2)
    __title._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 180, 8)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'label'), 'label', '__httpwww_xbrl_org2003XLink_resourceType_httpwww_w3_org1999xlinklabel', pyxb.binding.datatypes.NCName, required=True)
    __label._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 113, 2)
    __label._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 178, 8)
    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003XLink_resourceType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 181, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 181, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __role.name() : __role,
        __title.name() : __title,
        __label.name() : __label,
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'resourceType', resourceType)


# Complex type {http://www.xbrl.org/2003/XLink}extendedType with content type ELEMENT_ONLY
class extendedType (pyxb.binding.basis.complexTypeDefinition):
    """
      Generic extended link type
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extendedType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 193, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/XLink}documentation uses Python identifier documentation
    __documentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentation'), 'documentation', '__httpwww_xbrl_org2003XLink_extendedType_httpwww_xbrl_org2003XLinkdocumentation', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 57, 2), )

    
    documentation = property(__documentation.value, __documentation.set, None, '\n      Abstract element to use for documentation of \n      extended links and linkbases.\n      ')

    
    # Element {http://www.xbrl.org/2003/XLink}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__httpwww_xbrl_org2003XLink_extendedType_httpwww_xbrl_org2003XLinktitle', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 85, 2), )

    
    title = property(__title.value, __title.set, None, '\n      Generic title element for use in extended link documentation.\n      Used on extended links, arcs, locators.\n      See http://www.w3.org/TR/xlink/#title-element for details.\n      ')

    
    # Element {http://www.xbrl.org/2003/XLink}locator uses Python identifier locator
    __locator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'locator'), 'locator', '__httpwww_xbrl_org2003XLink_extendedType_httpwww_xbrl_org2003XLinklocator', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 114, 2), )

    
    locator = property(__locator.value, __locator.set, None, '\n      Abstract locator element to be used as head of locator substitution group\n      for all extended link locators in XBRL.\n      ')

    
    # Element {http://www.xbrl.org/2003/XLink}arc uses Python identifier arc
    __arc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'arc'), 'arc', '__httpwww_xbrl_org2003XLink_extendedType_httpwww_xbrl_org2003XLinkarc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 161, 2), )

    
    arc = property(__arc.value, __arc.set, None, '\n      Abstract element to use as head of arc element substitution group.\n      ')

    
    # Element {http://www.xbrl.org/2003/XLink}resource uses Python identifier resource
    __resource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resource'), 'resource', '__httpwww_xbrl_org2003XLink_extendedType_httpwww_xbrl_org2003XLinkresource', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 185, 2), )

    
    resource = property(__resource.value, __resource.set, None, '\n      Abstract element to use as head of resource element substitution group.\n      ')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_xbrl_org2003XLink_extendedType_httpwww_w3_org1999xlinktype', _ImportedBinding__xlink.STD_ANON, fixed=True, unicode_default='extended', required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 34, 2)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 208, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_xbrl_org2003XLink_extendedType_httpwww_w3_org1999xlinkrole', _ImportedBinding__xlink.STD_ANON_, required=True)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 52, 2)
    __role._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 209, 8)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title_
    __title_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title_', '__httpwww_xbrl_org2003XLink_extendedType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title_._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 78, 2)
    __title_._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 210, 8)
    
    title_ = property(__title_.value, __title_.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003XLink_extendedType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 211, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 211, 8)
    
    id = property(__id.value, __id.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        __documentation.name() : __documentation,
        __title.name() : __title,
        __locator.name() : __locator,
        __arc.name() : __arc,
        __resource.name() : __resource
    })
    _AttributeMap.update({
        __type.name() : __type,
        __role.name() : __role,
        __title_.name() : __title_,
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'extendedType', extendedType)


# Complex type {http://www.xbrl.org/2003/XLink}simpleType with content type EMPTY
class simpleType (pyxb.binding.basis.complexTypeDefinition):
    """
      Type for the simple links defined in XBRL
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'simpleType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 224, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_xbrl_org2003XLink_simpleType_httpwww_w3_org1999xlinktype', _ImportedBinding__xlink.STD_ANON, fixed=True, unicode_default='simple', required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 34, 2)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 232, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_xbrl_org2003XLink_simpleType_httpwww_w3_org1999xlinkrole', _ImportedBinding__xlink.STD_ANON_)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 52, 2)
    __role._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 235, 8)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_xbrl_org2003XLink_simpleType_httpwww_w3_org1999xlinkarcrole', _ImportedBinding__xlink.STD_ANON_2)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 65, 2)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 234, 8)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_xbrl_org2003XLink_simpleType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 78, 2)
    __title._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 236, 8)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_xbrl_org2003XLink_simpleType_httpwww_w3_org1999xlinkshow', _ImportedBinding__xlink.STD_ANON_3)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 80, 2)
    __show._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 237, 8)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_xbrl_org2003XLink_simpleType_httpwww_w3_org1999xlinkactuate', _ImportedBinding__xlink.STD_ANON_4)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 97, 2)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 238, 8)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_xbrl_org2003XLink_simpleType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 119, 2)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 233, 8)
    
    href = property(__href.value, __href.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate,
        __href.name() : __href
    })
Namespace.addCategoryObject('typeBinding', 'simpleType', simpleType)


documentation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentation'), documentationType, abstract=pyxb.binding.datatypes.boolean(1), documentation='\n      Abstract element to use for documentation of \n      extended links and linkbases.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 57, 2))
Namespace.addCategoryObject('elementBinding', documentation.name().localName(), documentation)

title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), titleType, abstract=pyxb.binding.datatypes.boolean(1), documentation='\n      Generic title element for use in extended link documentation.\n      Used on extended links, arcs, locators.\n      See http://www.w3.org/TR/xlink/#title-element for details.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 85, 2))
Namespace.addCategoryObject('elementBinding', title.name().localName(), title)

locator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'locator'), locatorType, abstract=pyxb.binding.datatypes.boolean(1), documentation='\n      Abstract locator element to be used as head of locator substitution group\n      for all extended link locators in XBRL.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 114, 2))
Namespace.addCategoryObject('elementBinding', locator.name().localName(), locator)

arc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'arc'), arcType, abstract=pyxb.binding.datatypes.boolean(1), documentation='\n      Abstract element to use as head of arc element substitution group.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 161, 2))
Namespace.addCategoryObject('elementBinding', arc.name().localName(), arc)

resource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resource'), resourceType, abstract=pyxb.binding.datatypes.boolean(1), documentation='\n      Abstract element to use as head of resource element substitution group.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 185, 2))
Namespace.addCategoryObject('elementBinding', resource.name().localName(), resource)

extended = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extended'), extendedType, abstract=pyxb.binding.datatypes.boolean(1), documentation='\n      Abstract extended link element at head of extended link substitution group.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 216, 2))
Namespace.addCategoryObject('elementBinding', extended.name().localName(), extended)

simple = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'simple'), simpleType, abstract=pyxb.binding.datatypes.boolean(1), documentation='\n      The abstract element at the head of the simple link substitution group.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 243, 2))
Namespace.addCategoryObject('elementBinding', simple.name().localName(), simple)



locatorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), titleType, abstract=pyxb.binding.datatypes.boolean(1), scope=locatorType, documentation='\n      Generic title element for use in extended link documentation.\n      Used on extended links, arcs, locators.\n      See http://www.w3.org/TR/xlink/#title-element for details.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 85, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 104, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(locatorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 104, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
locatorType._Automaton = _BuildAutomaton()




arcType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), titleType, abstract=pyxb.binding.datatypes.boolean(1), scope=arcType, documentation='\n      Generic title element for use in extended link documentation.\n      Used on extended links, arcs, locators.\n      See http://www.w3.org/TR/xlink/#title-element for details.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 85, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 145, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(arcType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 145, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
arcType._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
resourceType._Automaton = _BuildAutomaton_2()




extendedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentation'), documentationType, abstract=pyxb.binding.datatypes.boolean(1), scope=extendedType, documentation='\n      Abstract element to use for documentation of \n      extended links and linkbases.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 57, 2)))

extendedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), titleType, abstract=pyxb.binding.datatypes.boolean(1), scope=extendedType, documentation='\n      Generic title element for use in extended link documentation.\n      Used on extended links, arcs, locators.\n      See http://www.w3.org/TR/xlink/#title-element for details.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 85, 2)))

extendedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'locator'), locatorType, abstract=pyxb.binding.datatypes.boolean(1), scope=extendedType, documentation='\n      Abstract locator element to be used as head of locator substitution group\n      for all extended link locators in XBRL.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 114, 2)))

extendedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'arc'), arcType, abstract=pyxb.binding.datatypes.boolean(1), scope=extendedType, documentation='\n      Abstract element to use as head of arc element substitution group.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 161, 2)))

extendedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resource'), resourceType, abstract=pyxb.binding.datatypes.boolean(1), scope=extendedType, documentation='\n      Abstract element to use as head of resource element substitution group.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 185, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 201, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(extendedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 202, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(extendedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentation')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 203, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(extendedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locator')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 204, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(extendedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'arc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 205, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(extendedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resource')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 206, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
extendedType._Automaton = _BuildAutomaton_3()

