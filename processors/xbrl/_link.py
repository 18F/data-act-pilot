# ./_link.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a6b2d22bd943719888030ebbfd9cbd2329dbe639
# Generated 2015-09-09 15:57:00.672578 by PyXB version 1.2.4 using Python 2.7.8.final.0
# Namespace http://www.xbrl.org/2003/linkbase [xmlns:link]

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
import _xl as _ImportedBinding__xl
import _xlink as _ImportedBinding__xlink

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.xbrl.org/2003/linkbase', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xl = _ImportedBinding__xl.Namespace
_Namespace_xl.configureCategories(['typeBinding', 'elementBinding'])
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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 97, 12)
    _Documentation = None
STD_ANON._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 475, 8)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.any = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='any', tag='any')
STD_ANON_.undirected = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='undirected', tag='undirected')
STD_ANON_.none = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
      Definition of the linkbase element.  Used to 
      contain a set of zero or more extended link elements.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 330, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/linkbase}documentation uses Python identifier documentation
    __documentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentation'), 'documentation', '__httpwww_xbrl_org2003linkbase_CTD_ANON_httpwww_xbrl_org2003linkbasedocumentation', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2), )

    
    documentation = property(__documentation.value, __documentation.set, None, '\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}roleRef uses Python identifier roleRef
    __roleRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'roleRef'), 'roleRef', '__httpwww_xbrl_org2003linkbase_CTD_ANON_httpwww_xbrl_org2003linkbaseroleRef', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 378, 2), )

    
    roleRef = property(__roleRef.value, __roleRef.set, None, '\n      Definition of the roleRef element - used \n      to link to resolve xlink:role attribute values to \n      the roleType element declaration.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}arcroleRef uses Python identifier arcroleRef
    __arcroleRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'arcroleRef'), 'arcroleRef', '__httpwww_xbrl_org2003linkbase_CTD_ANON_httpwww_xbrl_org2003linkbasearcroleRef', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 401, 2), )

    
    arcroleRef = property(__arcroleRef.value, __arcroleRef.set, None, '\n      Definition of the roleRef element - used \n      to link to resolve xlink:arcrole attribute values to \n      the arcroleType element declaration.\n      ')

    
    # Element {http://www.xbrl.org/2003/XLink}extended uses Python identifier extended
    __extended = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_xl, 'extended'), 'extended', '__httpwww_xbrl_org2003linkbase_CTD_ANON_httpwww_xbrl_org2003XLinkextended', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 216, 2), )

    
    extended = property(__extended.value, __extended.set, None, '\n      Abstract extended link element at head of extended link substitution group.\n      ')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003linkbase_CTD_ANON_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 337, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 337, 6)
    
    id = property(__id.value, __id.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        __documentation.name() : __documentation,
        __roleRef.name() : __roleRef,
        __arcroleRef.name() : __arcroleRef,
        __extended.name() : __extended
    })
    _AttributeMap.update({
        __id.name() : __id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
      The roleType element definition - used to define custom
      role values in XBRL extended links.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 450, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/linkbase}definition uses Python identifier definition
    __definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'definition'), 'definition', '__httpwww_xbrl_org2003linkbase_CTD_ANON__httpwww_xbrl_org2003linkbasedefinition', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 424, 2), )

    
    definition = property(__definition.value, __definition.set, None, '\n      The element to use for human-readable definition \n      of custom roles and arc roles.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}usedOn uses Python identifier usedOn
    __usedOn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usedOn'), 'usedOn', '__httpwww_xbrl_org2003linkbase_CTD_ANON__httpwww_xbrl_org2003linkbaseusedOn', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 433, 2), )

    
    usedOn = property(__usedOn.value, __usedOn.set, None, '\n      Definition of the usedOn element - used\n      to identify what elements may use a \n      taxonomy defined role or arc role value.\n      ')

    
    # Attribute roleURI uses Python identifier roleURI
    __roleURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'roleURI'), 'roleURI', '__httpwww_xbrl_org2003linkbase_CTD_ANON__roleURI', _ImportedBinding__xl.nonEmptyURI, required=True)
    __roleURI._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 455, 6)
    __roleURI._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 455, 6)
    
    roleURI = property(__roleURI.value, __roleURI.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003linkbase_CTD_ANON__id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 456, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 456, 6)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __definition.name() : __definition,
        __usedOn.name() : __usedOn
    })
    _AttributeMap.update({
        __roleURI.name() : __roleURI,
        __id.name() : __id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
      The  arcroleType element definition - used to define custom
      arc role values in XBRL extended links.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 467, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/2003/linkbase}definition uses Python identifier definition
    __definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'definition'), 'definition', '__httpwww_xbrl_org2003linkbase_CTD_ANON_2_httpwww_xbrl_org2003linkbasedefinition', False, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 424, 2), )

    
    definition = property(__definition.value, __definition.set, None, '\n      The element to use for human-readable definition \n      of custom roles and arc roles.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}usedOn uses Python identifier usedOn
    __usedOn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usedOn'), 'usedOn', '__httpwww_xbrl_org2003linkbase_CTD_ANON_2_httpwww_xbrl_org2003linkbaseusedOn', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 433, 2), )

    
    usedOn = property(__usedOn.value, __usedOn.set, None, '\n      Definition of the usedOn element - used\n      to identify what elements may use a \n      taxonomy defined role or arc role value.\n      ')

    
    # Attribute arcroleURI uses Python identifier arcroleURI
    __arcroleURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arcroleURI'), 'arcroleURI', '__httpwww_xbrl_org2003linkbase_CTD_ANON_2_arcroleURI', _ImportedBinding__xl.nonEmptyURI, required=True)
    __arcroleURI._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 472, 6)
    __arcroleURI._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 472, 6)
    
    arcroleURI = property(__arcroleURI.value, __arcroleURI.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_org2003linkbase_CTD_ANON_2_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 473, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 473, 6)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute cyclesAllowed uses Python identifier cyclesAllowed
    __cyclesAllowed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cyclesAllowed'), 'cyclesAllowed', '__httpwww_xbrl_org2003linkbase_CTD_ANON_2_cyclesAllowed', STD_ANON_, required=True)
    __cyclesAllowed._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 474, 6)
    __cyclesAllowed._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 474, 6)
    
    cyclesAllowed = property(__cyclesAllowed.value, __cyclesAllowed.set, None, None)

    _ElementMap.update({
        __definition.name() : __definition,
        __usedOn.name() : __usedOn
    })
    _AttributeMap.update({
        __arcroleURI.name() : __arcroleURI,
        __id.name() : __id,
        __cyclesAllowed.name() : __cyclesAllowed
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (_ImportedBinding__xl.arcType):
    """
        Extension of the extended link arc type for presentation arcs.
        Adds a preferredLabel attribute that documents the role attribute
        value of preferred labels (as they occur in label extended links).
        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 86, 4)
    _ElementMap = _ImportedBinding__xl.arcType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.arcType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.arcType
    
    # Element title ({http://www.xbrl.org/2003/XLink}title) inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute arcrole inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute title_ inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute show inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute actuate inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute from_ inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute to inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute order inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute use inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute priority inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute preferredLabel uses Python identifier preferredLabel
    __preferredLabel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'preferredLabel'), 'preferredLabel', '__httpwww_xbrl_org2003linkbase_CTD_ANON_3_preferredLabel', STD_ANON)
    __preferredLabel._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 96, 10)
    __preferredLabel._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 96, 10)
    
    preferredLabel = property(__preferredLabel.value, __preferredLabel.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/XLink'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __preferredLabel.name() : __preferredLabel
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (_ImportedBinding__xl.arcType):
    """
        Extension of the extended link arc type for calculation arcs.
        Adds a weight attribute to track weights on contributions to 
        summations.
        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 109, 4)
    _ElementMap = _ImportedBinding__xl.arcType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.arcType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.arcType
    
    # Element title ({http://www.xbrl.org/2003/XLink}title) inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute arcrole inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute title_ inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute show inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute actuate inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute from_ inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute to inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute order inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute use inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute priority inherited from {http://www.xbrl.org/2003/XLink}arcType
    
    # Attribute weight uses Python identifier weight
    __weight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'weight'), 'weight', '__httpwww_xbrl_org2003linkbase_CTD_ANON_4_weight', pyxb.binding.datatypes.decimal, required=True)
    __weight._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 119, 10)
    __weight._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 119, 10)
    
    weight = property(__weight.value, __weight.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.xbrl.org/2003/XLink'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __weight.name() : __weight
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_5 (_ImportedBinding__xl.resourceType):
    """
      Definition of the label  resource element.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 139, 4)
    _ElementMap = _ImportedBinding__xl.resourceType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.resourceType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.resourceType
    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}resourceType
    
    # Attribute role inherited from {http://www.xbrl.org/2003/XLink}resourceType
    
    # Attribute title inherited from {http://www.xbrl.org/2003/XLink}resourceType
    
    # Attribute label inherited from {http://www.xbrl.org/2003/XLink}resourceType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/XLink}resourceType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_6 (_ImportedBinding__xl.resourceType):
    """
      Definition of the reference  resource element.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 165, 4)
    _ElementMap = _ImportedBinding__xl.resourceType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.resourceType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.resourceType
    
    # Element {http://www.xbrl.org/2003/linkbase}part uses Python identifier part
    __part = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'part'), 'part', '__httpwww_xbrl_org2003linkbase_CTD_ANON_6_httpwww_xbrl_org2003linkbasepart', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 151, 2), )

    
    part = property(__part.value, __part.set, None, '\n      Definition of the reference  part element - for use in reference  resources.\n      ')

    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}resourceType
    
    # Attribute role inherited from {http://www.xbrl.org/2003/XLink}resourceType
    
    # Attribute title inherited from {http://www.xbrl.org/2003/XLink}resourceType
    
    # Attribute label inherited from {http://www.xbrl.org/2003/XLink}resourceType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/XLink}resourceType
    _ElementMap.update({
        __part.name() : __part
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_7 (_ImportedBinding__xl.resourceType):
    """
      Definition of the reference  resource element
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 182, 4)
    _ElementMap = _ImportedBinding__xl.resourceType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.resourceType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.resourceType
    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}resourceType
    
    # Attribute role inherited from {http://www.xbrl.org/2003/XLink}resourceType
    
    # Attribute title inherited from {http://www.xbrl.org/2003/XLink}resourceType
    
    # Attribute label inherited from {http://www.xbrl.org/2003/XLink}resourceType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/XLink}resourceType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (_ImportedBinding__xl.extendedType):
    """
      presentation extended link element definition.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 200, 4)
    _ElementMap = _ImportedBinding__xl.extendedType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.extendedType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.extendedType
    
    # Element title ({http://www.xbrl.org/2003/XLink}title) inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Element {http://www.xbrl.org/2003/linkbase}documentation uses Python identifier documentation_
    __documentation_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentation'), 'documentation_', '__httpwww_xbrl_org2003linkbase_CTD_ANON_8_httpwww_xbrl_org2003linkbasedocumentation', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2), )

    
    documentation_ = property(__documentation_.value, __documentation_.set, None, '\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}loc uses Python identifier loc
    __loc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'loc'), 'loc', '__httpwww_xbrl_org2003linkbase_CTD_ANON_8_httpwww_xbrl_org2003linkbaseloc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2), )

    
    loc = property(__loc.value, __loc.set, None, '\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}presentationArc uses Python identifier presentationArc
    __presentationArc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'presentationArc'), 'presentationArc', '__httpwww_xbrl_org2003linkbase_CTD_ANON_8_httpwww_xbrl_org2003linkbasepresentationArc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 85, 2), )

    
    presentationArc = property(__presentationArc.value, __presentationArc.set, None, None)

    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute role inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute title_ inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/XLink}extendedType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        __documentation_.name() : __documentation_,
        __loc.name() : __loc,
        __presentationArc.name() : __presentationArc
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (_ImportedBinding__xl.extendedType):
    """
      definition extended link element definition
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 221, 4)
    _ElementMap = _ImportedBinding__xl.extendedType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.extendedType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.extendedType
    
    # Element title ({http://www.xbrl.org/2003/XLink}title) inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Element {http://www.xbrl.org/2003/linkbase}documentation uses Python identifier documentation_
    __documentation_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentation'), 'documentation_', '__httpwww_xbrl_org2003linkbase_CTD_ANON_9_httpwww_xbrl_org2003linkbasedocumentation', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2), )

    
    documentation_ = property(__documentation_.value, __documentation_.set, None, '\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}loc uses Python identifier loc
    __loc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'loc'), 'loc', '__httpwww_xbrl_org2003linkbase_CTD_ANON_9_httpwww_xbrl_org2003linkbaseloc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2), )

    
    loc = property(__loc.value, __loc.set, None, '\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}definitionArc uses Python identifier definitionArc
    __definitionArc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'definitionArc'), 'definitionArc', '__httpwww_xbrl_org2003linkbase_CTD_ANON_9_httpwww_xbrl_org2003linkbasedefinitionArc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 77, 2), )

    
    definitionArc = property(__definitionArc.value, __definitionArc.set, None, '\n      Concrete arc for use in definition extended links.\n      ')

    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute role inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute title_ inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/XLink}extendedType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        __documentation_.name() : __documentation_,
        __loc.name() : __loc,
        __definitionArc.name() : __definitionArc
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (_ImportedBinding__xl.extendedType):
    """
      calculation  extended link element definition
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 242, 4)
    _ElementMap = _ImportedBinding__xl.extendedType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.extendedType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.extendedType
    
    # Element title ({http://www.xbrl.org/2003/XLink}title) inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Element {http://www.xbrl.org/2003/linkbase}documentation uses Python identifier documentation_
    __documentation_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentation'), 'documentation_', '__httpwww_xbrl_org2003linkbase_CTD_ANON_10_httpwww_xbrl_org2003linkbasedocumentation', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2), )

    
    documentation_ = property(__documentation_.value, __documentation_.set, None, '\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}loc uses Python identifier loc
    __loc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'loc'), 'loc', '__httpwww_xbrl_org2003linkbase_CTD_ANON_10_httpwww_xbrl_org2003linkbaseloc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2), )

    
    loc = property(__loc.value, __loc.set, None, '\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}calculationArc uses Python identifier calculationArc
    __calculationArc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'calculationArc'), 'calculationArc', '__httpwww_xbrl_org2003linkbase_CTD_ANON_10_httpwww_xbrl_org2003linkbasecalculationArc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 108, 2), )

    
    calculationArc = property(__calculationArc.value, __calculationArc.set, None, None)

    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute role inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute title_ inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/XLink}extendedType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        __documentation_.name() : __documentation_,
        __loc.name() : __loc,
        __calculationArc.name() : __calculationArc
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (_ImportedBinding__xl.extendedType):
    """
      label extended link element definition
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 263, 4)
    _ElementMap = _ImportedBinding__xl.extendedType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.extendedType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.extendedType
    
    # Element title ({http://www.xbrl.org/2003/XLink}title) inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Element {http://www.xbrl.org/2003/linkbase}documentation uses Python identifier documentation_
    __documentation_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentation'), 'documentation_', '__httpwww_xbrl_org2003linkbase_CTD_ANON_11_httpwww_xbrl_org2003linkbasedocumentation', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2), )

    
    documentation_ = property(__documentation_.value, __documentation_.set, None, '\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}loc uses Python identifier loc
    __loc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'loc'), 'loc', '__httpwww_xbrl_org2003linkbase_CTD_ANON_11_httpwww_xbrl_org2003linkbaseloc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2), )

    
    loc = property(__loc.value, __loc.set, None, '\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}labelArc uses Python identifier labelArc
    __labelArc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'labelArc'), 'labelArc', '__httpwww_xbrl_org2003linkbase_CTD_ANON_11_httpwww_xbrl_org2003linkbaselabelArc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 61, 2), )

    
    labelArc = property(__labelArc.value, __labelArc.set, None, '\n      Concrete arc for use in label extended links.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'label'), 'label', '__httpwww_xbrl_org2003linkbase_CTD_ANON_11_httpwww_xbrl_org2003linkbaselabel', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 133, 2), )

    
    label = property(__label.value, __label.set, None, '\n      Definition of the label  resource element.\n      ')

    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute role inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute title_ inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/XLink}extendedType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        __documentation_.name() : __documentation_,
        __loc.name() : __loc,
        __labelArc.name() : __labelArc,
        __label.name() : __label
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (_ImportedBinding__xl.extendedType):
    """
      reference extended link element definition
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 285, 4)
    _ElementMap = _ImportedBinding__xl.extendedType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.extendedType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.extendedType
    
    # Element title ({http://www.xbrl.org/2003/XLink}title) inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Element {http://www.xbrl.org/2003/linkbase}documentation uses Python identifier documentation_
    __documentation_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentation'), 'documentation_', '__httpwww_xbrl_org2003linkbase_CTD_ANON_12_httpwww_xbrl_org2003linkbasedocumentation', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2), )

    
    documentation_ = property(__documentation_.value, __documentation_.set, None, '\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}loc uses Python identifier loc
    __loc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'loc'), 'loc', '__httpwww_xbrl_org2003linkbase_CTD_ANON_12_httpwww_xbrl_org2003linkbaseloc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2), )

    
    loc = property(__loc.value, __loc.set, None, '\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}referenceArc uses Python identifier referenceArc
    __referenceArc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'referenceArc'), 'referenceArc', '__httpwww_xbrl_org2003linkbase_CTD_ANON_12_httpwww_xbrl_org2003linkbasereferenceArc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 69, 2), )

    
    referenceArc = property(__referenceArc.value, __referenceArc.set, None, '\n      Concrete arc for use in reference extended links.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}reference uses Python identifier reference
    __reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reference'), 'reference', '__httpwww_xbrl_org2003linkbase_CTD_ANON_12_httpwww_xbrl_org2003linkbasereference', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 159, 2), )

    
    reference = property(__reference.value, __reference.set, None, '\n      Definition of the reference  resource element.\n      ')

    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute role inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute title_ inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/XLink}extendedType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        __documentation_.name() : __documentation_,
        __loc.name() : __loc,
        __referenceArc.name() : __referenceArc,
        __reference.name() : __reference
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (_ImportedBinding__xl.extendedType):
    """
      footnote extended link element definition
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 307, 4)
    _ElementMap = _ImportedBinding__xl.extendedType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.extendedType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.extendedType
    
    # Element title ({http://www.xbrl.org/2003/XLink}title) inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Element {http://www.xbrl.org/2003/linkbase}documentation uses Python identifier documentation_
    __documentation_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentation'), 'documentation_', '__httpwww_xbrl_org2003linkbase_CTD_ANON_13_httpwww_xbrl_org2003linkbasedocumentation', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2), )

    
    documentation_ = property(__documentation_.value, __documentation_.set, None, '\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}loc uses Python identifier loc
    __loc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'loc'), 'loc', '__httpwww_xbrl_org2003linkbase_CTD_ANON_13_httpwww_xbrl_org2003linkbaseloc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2), )

    
    loc = property(__loc.value, __loc.set, None, '\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}footnoteArc uses Python identifier footnoteArc
    __footnoteArc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'footnoteArc'), 'footnoteArc', '__httpwww_xbrl_org2003linkbase_CTD_ANON_13_httpwww_xbrl_org2003linkbasefootnoteArc', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 125, 2), )

    
    footnoteArc = property(__footnoteArc.value, __footnoteArc.set, None, '\n      Concrete arc for use in footnote extended links.\n      ')

    
    # Element {http://www.xbrl.org/2003/linkbase}footnote uses Python identifier footnote
    __footnote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'footnote'), 'footnote', '__httpwww_xbrl_org2003linkbase_CTD_ANON_13_httpwww_xbrl_org2003linkbasefootnote', True, pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 176, 2), )

    
    footnote = property(__footnote.value, __footnote.set, None, '\n      Definition of the reference  resource element\n      ')

    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute role inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute title_ inherited from {http://www.xbrl.org/2003/XLink}extendedType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/XLink}extendedType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        __documentation_.name() : __documentation_,
        __loc.name() : __loc,
        __footnoteArc.name() : __footnoteArc,
        __footnote.name() : __footnote
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_14 (_ImportedBinding__xl.simpleType):
    """
      Definition of the linkbaseRef element - used 
      to link to XBRL taxonomy extended links from 
      taxonomy schema documents and from XBRL
      instances.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 351, 4)
    _ElementMap = _ImportedBinding__xl.simpleType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.simpleType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.simpleType
    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute role inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute arcrole is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_xbrl_org2003XLink_simpleType_httpwww_w3_org1999xlinkarcrole', _ImportedBinding__xlink.STD_ANON_2, required=True)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 65, 2)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 354, 10)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute title inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute show inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute actuate inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute href inherited from {http://www.xbrl.org/2003/XLink}simpleType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __arcrole.name() : __arcrole
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_15 (_ImportedBinding__xl.simpleType):
    """
      Definition of the roleRef element - used 
      to link to resolve xlink:role attribute values to 
      the roleType element declaration.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 386, 4)
    _ElementMap = _ImportedBinding__xl.simpleType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.simpleType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.simpleType
    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute role inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute arcrole inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute title inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute show inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute actuate inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute href inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute roleURI uses Python identifier roleURI
    __roleURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'roleURI'), 'roleURI', '__httpwww_xbrl_org2003linkbase_CTD_ANON_15_roleURI', _ImportedBinding__xl.nonEmptyURI, required=True)
    __roleURI._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 389, 10)
    __roleURI._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 389, 10)
    
    roleURI = property(__roleURI.value, __roleURI.set, None, '\n                This attribute contains the role name.\n              ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __roleURI.name() : __roleURI
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_16 (_ImportedBinding__xl.simpleType):
    """
      Definition of the roleRef element - used 
      to link to resolve xlink:arcrole attribute values to 
      the arcroleType element declaration.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 409, 4)
    _ElementMap = _ImportedBinding__xl.simpleType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__xl.simpleType._AttributeMap.copy()
    # Base type is _ImportedBinding__xl.simpleType
    
    # Attribute type inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute role inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute arcrole inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute title inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute show inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute actuate inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute href inherited from {http://www.xbrl.org/2003/XLink}simpleType
    
    # Attribute arcroleURI uses Python identifier arcroleURI
    __arcroleURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arcroleURI'), 'arcroleURI', '__httpwww_xbrl_org2003linkbase_CTD_ANON_16_arcroleURI', _ImportedBinding__xl.nonEmptyURI, required=True)
    __arcroleURI._DeclarationLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 412, 10)
    __arcroleURI._UseLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 412, 10)
    
    arcroleURI = property(__arcroleURI.value, __arcroleURI.set, None, '\n                This attribute contains the arc role name.\n              ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/XML/1998/namespace']))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __arcroleURI.name() : __arcroleURI
    })



part = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'part'), pyxb.binding.datatypes.anySimpleType, abstract=pyxb.binding.datatypes.boolean(1), documentation='\n      Definition of the reference  part element - for use in reference  resources.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 151, 2))
Namespace.addCategoryObject('elementBinding', part.name().localName(), part)

definition = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definition'), pyxb.binding.datatypes.string, documentation='\n      The element to use for human-readable definition \n      of custom roles and arc roles.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 424, 2))
Namespace.addCategoryObject('elementBinding', definition.name().localName(), definition)

usedOn = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usedOn'), pyxb.binding.datatypes.QName, documentation='\n      Definition of the usedOn element - used\n      to identify what elements may use a \n      taxonomy defined role or arc role value.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 433, 2))
Namespace.addCategoryObject('elementBinding', usedOn.name().localName(), usedOn)

documentation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentation'), _ImportedBinding__xl.documentationType, documentation='\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2))
Namespace.addCategoryObject('elementBinding', documentation.name().localName(), documentation)

linkbase = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'linkbase'), CTD_ANON, documentation='\n      Definition of the linkbase element.  Used to \n      contain a set of zero or more extended link elements.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 323, 2))
Namespace.addCategoryObject('elementBinding', linkbase.name().localName(), linkbase)

loc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'loc'), _ImportedBinding__xl.locatorType, documentation='\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2))
Namespace.addCategoryObject('elementBinding', loc.name().localName(), loc)

labelArc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'labelArc'), _ImportedBinding__xl.arcType, documentation='\n      Concrete arc for use in label extended links.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 61, 2))
Namespace.addCategoryObject('elementBinding', labelArc.name().localName(), labelArc)

referenceArc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'referenceArc'), _ImportedBinding__xl.arcType, documentation='\n      Concrete arc for use in reference extended links.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 69, 2))
Namespace.addCategoryObject('elementBinding', referenceArc.name().localName(), referenceArc)

definitionArc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definitionArc'), _ImportedBinding__xl.arcType, documentation='\n      Concrete arc for use in definition extended links.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 77, 2))
Namespace.addCategoryObject('elementBinding', definitionArc.name().localName(), definitionArc)

footnoteArc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'footnoteArc'), _ImportedBinding__xl.arcType, documentation='\n      Concrete arc for use in footnote extended links.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 125, 2))
Namespace.addCategoryObject('elementBinding', footnoteArc.name().localName(), footnoteArc)

schemaRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'schemaRef'), _ImportedBinding__xl.simpleType, documentation='\n      Definition of the schemaRef element - used \n      to link to XBRL taxonomy schemas from \n      XBRL instances.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 368, 2))
Namespace.addCategoryObject('elementBinding', schemaRef.name().localName(), schemaRef)

roleType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'roleType'), CTD_ANON_, documentation='\n      The roleType element definition - used to define custom\n      role values in XBRL extended links.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 443, 2))
Namespace.addCategoryObject('elementBinding', roleType.name().localName(), roleType)

arcroleType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'arcroleType'), CTD_ANON_2, documentation='\n      The  arcroleType element definition - used to define custom\n      arc role values in XBRL extended links.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 460, 2))
Namespace.addCategoryObject('elementBinding', arcroleType.name().localName(), arcroleType)

presentationArc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'presentationArc'), CTD_ANON_3, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 85, 2))
Namespace.addCategoryObject('elementBinding', presentationArc.name().localName(), presentationArc)

calculationArc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'calculationArc'), CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 108, 2))
Namespace.addCategoryObject('elementBinding', calculationArc.name().localName(), calculationArc)

label = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'label'), CTD_ANON_5, documentation='\n      Definition of the label  resource element.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 133, 2))
Namespace.addCategoryObject('elementBinding', label.name().localName(), label)

reference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reference'), CTD_ANON_6, documentation='\n      Definition of the reference  resource element.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 159, 2))
Namespace.addCategoryObject('elementBinding', reference.name().localName(), reference)

footnote = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'footnote'), CTD_ANON_7, documentation='\n      Definition of the reference  resource element\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 176, 2))
Namespace.addCategoryObject('elementBinding', footnote.name().localName(), footnote)

presentationLink = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'presentationLink'), CTD_ANON_8, documentation='\n      presentation extended link element definition.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 194, 2))
Namespace.addCategoryObject('elementBinding', presentationLink.name().localName(), presentationLink)

definitionLink = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definitionLink'), CTD_ANON_9, documentation='\n      definition extended link element definition\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 215, 2))
Namespace.addCategoryObject('elementBinding', definitionLink.name().localName(), definitionLink)

calculationLink = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'calculationLink'), CTD_ANON_10, documentation='\n      calculation  extended link element definition\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 236, 2))
Namespace.addCategoryObject('elementBinding', calculationLink.name().localName(), calculationLink)

labelLink = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'labelLink'), CTD_ANON_11, documentation='\n      label extended link element definition\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 257, 2))
Namespace.addCategoryObject('elementBinding', labelLink.name().localName(), labelLink)

referenceLink = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'referenceLink'), CTD_ANON_12, documentation='\n      reference extended link element definition\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 279, 2))
Namespace.addCategoryObject('elementBinding', referenceLink.name().localName(), referenceLink)

footnoteLink = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'footnoteLink'), CTD_ANON_13, documentation='\n      footnote extended link element definition\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 301, 2))
Namespace.addCategoryObject('elementBinding', footnoteLink.name().localName(), footnoteLink)

linkbaseRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'linkbaseRef'), CTD_ANON_14, documentation='\n      Definition of the linkbaseRef element - used \n      to link to XBRL taxonomy extended links from \n      taxonomy schema documents and from XBRL\n      instances.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 342, 2))
Namespace.addCategoryObject('elementBinding', linkbaseRef.name().localName(), linkbaseRef)

roleRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'roleRef'), CTD_ANON_15, documentation='\n      Definition of the roleRef element - used \n      to link to resolve xlink:role attribute values to \n      the roleType element declaration.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 378, 2))
Namespace.addCategoryObject('elementBinding', roleRef.name().localName(), roleRef)

arcroleRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'arcroleRef'), CTD_ANON_16, documentation='\n      Definition of the roleRef element - used \n      to link to resolve xlink:arcrole attribute values to \n      the arcroleType element declaration.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 401, 2))
Namespace.addCategoryObject('elementBinding', arcroleRef.name().localName(), arcroleRef)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentation'), _ImportedBinding__xl.documentationType, scope=CTD_ANON, documentation='\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'roleRef'), CTD_ANON_15, scope=CTD_ANON, documentation='\n      Definition of the roleRef element - used \n      to link to resolve xlink:role attribute values to \n      the roleType element declaration.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 378, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'arcroleRef'), CTD_ANON_16, scope=CTD_ANON, documentation='\n      Definition of the roleRef element - used \n      to link to resolve xlink:arcrole attribute values to \n      the arcroleType element declaration.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 401, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_xl, 'extended'), _ImportedBinding__xl.extendedType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON, documentation='\n      Abstract extended link element at head of extended link substitution group.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 216, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 331, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentation')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 332, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'roleRef')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 333, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'arcroleRef')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 334, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xl, 'extended')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 335, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definition'), pyxb.binding.datatypes.string, scope=CTD_ANON_, documentation='\n      The element to use for human-readable definition \n      of custom roles and arc roles.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 424, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usedOn'), pyxb.binding.datatypes.QName, scope=CTD_ANON_, documentation='\n      Definition of the usedOn element - used\n      to identify what elements may use a \n      taxonomy defined role or arc role value.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 433, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 452, 8))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'definition')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 452, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usedOn')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 453, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definition'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, documentation='\n      The element to use for human-readable definition \n      of custom roles and arc roles.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 424, 2)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usedOn'), pyxb.binding.datatypes.QName, scope=CTD_ANON_2, documentation='\n      Definition of the usedOn element - used\n      to identify what elements may use a \n      taxonomy defined role or arc role value.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 433, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 469, 8))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'definition')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 469, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usedOn')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 470, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 145, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xl, 'title')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 145, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 145, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xl, 'title')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xl-2003-12-31.xsd', 145, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 143, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=set(['http://www.w3.org/1999/xhtml'])), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 143, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'part'), pyxb.binding.datatypes.anySimpleType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_6, documentation='\n      Definition of the reference  part element - for use in reference  resources.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 151, 2)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 169, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'part')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 169, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 186, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=set(['http://www.w3.org/1999/xhtml'])), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 186, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentation'), _ImportedBinding__xl.documentationType, scope=CTD_ANON_8, documentation='\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'loc'), _ImportedBinding__xl.locatorType, scope=CTD_ANON_8, documentation='\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'presentationArc'), CTD_ANON_3, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 85, 2)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 203, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xl, 'title')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 204, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentation')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 205, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'loc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 206, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'presentationArc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 207, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentation'), _ImportedBinding__xl.documentationType, scope=CTD_ANON_9, documentation='\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'loc'), _ImportedBinding__xl.locatorType, scope=CTD_ANON_9, documentation='\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definitionArc'), _ImportedBinding__xl.arcType, scope=CTD_ANON_9, documentation='\n      Concrete arc for use in definition extended links.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 77, 2)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 224, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xl, 'title')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 225, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentation')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 226, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'loc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 227, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'definitionArc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 228, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentation'), _ImportedBinding__xl.documentationType, scope=CTD_ANON_10, documentation='\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'loc'), _ImportedBinding__xl.locatorType, scope=CTD_ANON_10, documentation='\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'calculationArc'), CTD_ANON_4, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 108, 2)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 245, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xl, 'title')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 246, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentation')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 247, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'loc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 248, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'calculationArc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 249, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_10()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentation'), _ImportedBinding__xl.documentationType, scope=CTD_ANON_11, documentation='\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'loc'), _ImportedBinding__xl.locatorType, scope=CTD_ANON_11, documentation='\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'labelArc'), _ImportedBinding__xl.arcType, scope=CTD_ANON_11, documentation='\n      Concrete arc for use in label extended links.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 61, 2)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'label'), CTD_ANON_5, scope=CTD_ANON_11, documentation='\n      Definition of the label  resource element.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 133, 2)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 266, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xl, 'title')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 267, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentation')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 268, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'loc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 269, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'labelArc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 270, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'label')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 271, 12))
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
CTD_ANON_11._Automaton = _BuildAutomaton_11()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentation'), _ImportedBinding__xl.documentationType, scope=CTD_ANON_12, documentation='\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'loc'), _ImportedBinding__xl.locatorType, scope=CTD_ANON_12, documentation='\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'referenceArc'), _ImportedBinding__xl.arcType, scope=CTD_ANON_12, documentation='\n      Concrete arc for use in reference extended links.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 69, 2)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reference'), CTD_ANON_6, scope=CTD_ANON_12, documentation='\n      Definition of the reference  resource element.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 159, 2)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 288, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xl, 'title')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 289, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentation')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 290, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'loc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 291, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referenceArc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 292, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reference')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 293, 12))
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
CTD_ANON_12._Automaton = _BuildAutomaton_12()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentation'), _ImportedBinding__xl.documentationType, scope=CTD_ANON_13, documentation='\n      Concrete element to use for documentation of \n      extended links and linkbases.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 41, 2)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'loc'), _ImportedBinding__xl.locatorType, scope=CTD_ANON_13, documentation='\n      Concrete locator element.  The loc element is the \n      XLink locator element for all extended links in XBRL.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 52, 2)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'footnoteArc'), _ImportedBinding__xl.arcType, scope=CTD_ANON_13, documentation='\n      Concrete arc for use in footnote extended links.\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 125, 2)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'footnote'), CTD_ANON_7, scope=CTD_ANON_13, documentation='\n      Definition of the reference  resource element\n      ', location=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 176, 2)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 310, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xl, 'title')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 311, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentation')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 312, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'loc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 313, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'footnoteArc')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 314, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'footnote')), pyxb.utils.utility.Location('http://www.xbrl.org/2003/xbrl-linkbase-2003-12-31.xsd', 315, 12))
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
CTD_ANON_13._Automaton = _BuildAutomaton_13()


documentation._setSubstitutionGroup(_ImportedBinding__xl.documentation)

loc._setSubstitutionGroup(_ImportedBinding__xl.locator)

labelArc._setSubstitutionGroup(_ImportedBinding__xl.arc)

referenceArc._setSubstitutionGroup(_ImportedBinding__xl.arc)

definitionArc._setSubstitutionGroup(_ImportedBinding__xl.arc)

footnoteArc._setSubstitutionGroup(_ImportedBinding__xl.arc)

schemaRef._setSubstitutionGroup(_ImportedBinding__xl.simple)

presentationArc._setSubstitutionGroup(_ImportedBinding__xl.arc)

calculationArc._setSubstitutionGroup(_ImportedBinding__xl.arc)

label._setSubstitutionGroup(_ImportedBinding__xl.resource)

reference._setSubstitutionGroup(_ImportedBinding__xl.resource)

footnote._setSubstitutionGroup(_ImportedBinding__xl.resource)

presentationLink._setSubstitutionGroup(_ImportedBinding__xl.extended)

definitionLink._setSubstitutionGroup(_ImportedBinding__xl.extended)

calculationLink._setSubstitutionGroup(_ImportedBinding__xl.extended)

labelLink._setSubstitutionGroup(_ImportedBinding__xl.extended)

referenceLink._setSubstitutionGroup(_ImportedBinding__xl.extended)

footnoteLink._setSubstitutionGroup(_ImportedBinding__xl.extended)

linkbaseRef._setSubstitutionGroup(_ImportedBinding__xl.simple)

roleRef._setSubstitutionGroup(_ImportedBinding__xl.simple)

arcroleRef._setSubstitutionGroup(_ImportedBinding__xl.simple)
