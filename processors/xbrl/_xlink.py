# ./_xlink.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b43cd366527ddb6a0e58594876e07421e0148f30
# Generated 2015-09-09 15:57:00.671941 by PyXB version 1.2.4 using Python 2.7.8.final.0
# Namespace http://www.w3.org/1999/xlink [xmlns:xlink]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/1999/xlink', create_if_missing=True)
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
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    Enumeration of values for the type attribute
	    """

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 35, 4)
    _Documentation = '\n\t    Enumeration of values for the type attribute\n\t    '
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.simple = STD_ANON._CF_enumeration.addEnumeration(unicode_value='simple', tag='simple')
STD_ANON.extended = STD_ANON._CF_enumeration.addEnumeration(unicode_value='extended', tag='extended')
STD_ANON.locator = STD_ANON._CF_enumeration.addEnumeration(unicode_value='locator', tag='locator')
STD_ANON.arc = STD_ANON._CF_enumeration.addEnumeration(unicode_value='arc', tag='arc')
STD_ANON.resource = STD_ANON._CF_enumeration.addEnumeration(unicode_value='resource', tag='resource')
STD_ANON.title = STD_ANON._CF_enumeration.addEnumeration(unicode_value='title', tag='title')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.anyURI):

    """
	      A URI with a minimum length of 1 character.
	      """

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 53, 4)
    _Documentation = '\n\t      A URI with a minimum length of 1 character.\n\t      '
STD_ANON_._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.anyURI):

    """
	      A URI with a minimum length of 1 character.
	      """

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 66, 6)
    _Documentation = '\n\t      A URI with a minimum length of 1 character.\n\t      '
STD_ANON_2._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	      Enumeration of values for the show attribute
	      """

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 81, 4)
    _Documentation = '\n\t      Enumeration of values for the show attribute\n\t      '
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.new = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='new', tag='new')
STD_ANON_3.replace = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='replace', tag='replace')
STD_ANON_3.embed = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='embed', tag='embed')
STD_ANON_3.other = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_3.none = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
      Enumeration of values for the actuate attribute
      """

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xbrl.org/2003/xlink-2003-12-31.xsd', 98, 4)
    _Documentation = '\n      Enumeration of values for the actuate attribute\n      '
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.onLoad = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='onLoad', tag='onLoad')
STD_ANON_4.onRequest = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='onRequest', tag='onRequest')
STD_ANON_4.other = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_4.none = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)
