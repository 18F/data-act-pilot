# ./ussgl.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:32084f8fa78422cabd7660a367cac6158f034e91
# Generated 2015-09-09 15:57:00.673528 by PyXB version 1.2.4 using Python 2.7.8.final.0
# Namespace http://www.xbrl.org/int/gl/cor/2006-10-25

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
Namespace = pyxb.namespace.NamespaceForURI('http://www.xbrl.org/int/gl/cor/2006-10-25', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gen = _ImportedBinding_gen.Namespace
_Namespace_gen.configureCategories(['typeBinding', 'elementBinding'])

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
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 67, 1)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.B = STD_ANON._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
STD_ANON.E = STD_ANON._CF_enumeration.addEnumeration(unicode_value='E', tag='E')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (_ImportedBinding_xbrli.pure):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 75, 1)
    _Documentation = None
STD_ANON_._InitializeFacetMap()

# Complex type {http://www.xbrl.org/int/gl/cor/2006-10-25}accountingEntriesComplexType with content type ELEMENT_ONLY
class accountingEntriesComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/gl/cor/2006-10-25}accountingEntriesComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'accountingEntriesComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 6, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}fiscalYear uses Python identifier fiscalYear
    __fiscalYear = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fiscalYear'), 'fiscalYear', '__httpwww_xbrl_orgintglcor2006_10_25_accountingEntriesComplexType_httpwww_xbrl_orgintglcor2006_10_25fiscalYear', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 84, 1), )

    
    fiscalYear = property(__fiscalYear.value, __fiscalYear.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}period uses Python identifier period
    __period = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'period'), 'period', '__httpwww_xbrl_orgintglcor2006_10_25_accountingEntriesComplexType_httpwww_xbrl_orgintglcor2006_10_25period', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 85, 1), )

    
    period = property(__period.value, __period.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}USSGLentryHeader uses Python identifier USSGLentryHeader
    __USSGLentryHeader = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'USSGLentryHeader'), 'USSGLentryHeader', '__httpwww_xbrl_orgintglcor2006_10_25_accountingEntriesComplexType_httpwww_xbrl_orgintglcor2006_10_25USSGLentryHeader', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 86, 1), )

    
    USSGLentryHeader = property(__USSGLentryHeader.value, __USSGLentryHeader.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintglcor2006_10_25_accountingEntriesComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 14, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 14, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __fiscalYear.name() : __fiscalYear,
        __period.name() : __period,
        __USSGLentryHeader.name() : __USSGLentryHeader
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'accountingEntriesComplexType', accountingEntriesComplexType)


# Complex type {http://www.xbrl.org/int/gl/cor/2006-10-25}USSGLentryHeaderComplexType with content type ELEMENT_ONLY
class USSGLentryHeaderComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/gl/cor/2006-10-25}USSGLentryHeaderComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'USSGLentryHeaderComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 18, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}obligatedAmount uses Python identifier obligatedAmount
    __obligatedAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'obligatedAmount'), 'obligatedAmount', '__httpwww_xbrl_orgintglcor2006_10_25_USSGLentryHeaderComplexType_httpwww_xbrl_orgintglcor2006_10_25obligatedAmount', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 87, 1), )

    
    obligatedAmount = property(__obligatedAmount.value, __obligatedAmount.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}unobligatedAmount uses Python identifier unobligatedAmount
    __unobligatedAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unobligatedAmount'), 'unobligatedAmount', '__httpwww_xbrl_orgintglcor2006_10_25_USSGLentryHeaderComplexType_httpwww_xbrl_orgintglcor2006_10_25unobligatedAmount', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 88, 1), )

    
    unobligatedAmount = property(__unobligatedAmount.value, __unobligatedAmount.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}budgetAuthorityAppropriated uses Python identifier budgetAuthorityAppropriated
    __budgetAuthorityAppropriated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'budgetAuthorityAppropriated'), 'budgetAuthorityAppropriated', '__httpwww_xbrl_orgintglcor2006_10_25_USSGLentryHeaderComplexType_httpwww_xbrl_orgintglcor2006_10_25budgetAuthorityAppropriated', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 89, 1), )

    
    budgetAuthorityAppropriated = property(__budgetAuthorityAppropriated.value, __budgetAuthorityAppropriated.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}otherBudgetaryResources uses Python identifier otherBudgetaryResources
    __otherBudgetaryResources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'otherBudgetaryResources'), 'otherBudgetaryResources', '__httpwww_xbrl_orgintglcor2006_10_25_USSGLentryHeaderComplexType_httpwww_xbrl_orgintglcor2006_10_25otherBudgetaryResources', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 90, 1), )

    
    otherBudgetaryResources = property(__otherBudgetaryResources.value, __otherBudgetaryResources.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}outlays uses Python identifier outlays
    __outlays = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outlays'), 'outlays', '__httpwww_xbrl_orgintglcor2006_10_25_USSGLentryHeaderComplexType_httpwww_xbrl_orgintglcor2006_10_25outlays', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 91, 1), )

    
    outlays = property(__outlays.value, __outlays.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}appropriationAccount uses Python identifier appropriationAccount
    __appropriationAccount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'appropriationAccount'), 'appropriationAccount', '__httpwww_xbrl_orgintglcor2006_10_25_USSGLentryHeaderComplexType_httpwww_xbrl_orgintglcor2006_10_25appropriationAccount', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 92, 1), )

    
    appropriationAccount = property(__appropriationAccount.value, __appropriationAccount.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}entryDetail uses Python identifier entryDetail
    __entryDetail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entryDetail'), 'entryDetail', '__httpwww_xbrl_orgintglcor2006_10_25_USSGLentryHeaderComplexType_httpwww_xbrl_orgintglcor2006_10_25entryDetail', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 93, 1), )

    
    entryDetail = property(__entryDetail.value, __entryDetail.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}treasuryAccountSymbol uses Python identifier treasuryAccountSymbol
    __treasuryAccountSymbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gen, 'treasuryAccountSymbol'), 'treasuryAccountSymbol', '__httpwww_xbrl_orgintglcor2006_10_25_USSGLentryHeaderComplexType_httpwww_xbrl_orgintglgen2006_10_25treasuryAccountSymbol', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 865, 1), )

    
    treasuryAccountSymbol = property(__treasuryAccountSymbol.value, __treasuryAccountSymbol.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintglcor2006_10_25_USSGLentryHeaderComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 31, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 31, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __obligatedAmount.name() : __obligatedAmount,
        __unobligatedAmount.name() : __unobligatedAmount,
        __budgetAuthorityAppropriated.name() : __budgetAuthorityAppropriated,
        __otherBudgetaryResources.name() : __otherBudgetaryResources,
        __outlays.name() : __outlays,
        __appropriationAccount.name() : __appropriationAccount,
        __entryDetail.name() : __entryDetail,
        __treasuryAccountSymbol.name() : __treasuryAccountSymbol
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'USSGLentryHeaderComplexType', USSGLentryHeaderComplexType)


# Complex type {http://www.xbrl.org/int/gl/cor/2006-10-25}entryDetailComplexType with content type ELEMENT_ONLY
class entryDetailComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/gl/cor/2006-10-25}entryDetailComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entryDetailComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 35, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'amount'), 'amount', '__httpwww_xbrl_orgintglcor2006_10_25_entryDetailComplexType_httpwww_xbrl_orgintglcor2006_10_25amount', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 94, 1), )

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}beginningEndIndicator uses Python identifier beginningEndIndicator
    __beginningEndIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beginningEndIndicator'), 'beginningEndIndicator', '__httpwww_xbrl_orgintglcor2006_10_25_entryDetailComplexType_httpwww_xbrl_orgintglcor2006_10_25beginningEndIndicator', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 95, 1), )

    
    beginningEndIndicator = property(__beginningEndIndicator.value, __beginningEndIndicator.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}programActivity uses Python identifier programActivity
    __programActivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'programActivity'), 'programActivity', '__httpwww_xbrl_orgintglcor2006_10_25_entryDetailComplexType_httpwww_xbrl_orgintglcor2006_10_25programActivity', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 96, 1), )

    
    programActivity = property(__programActivity.value, __programActivity.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}account uses Python identifier account
    __account = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'account'), 'account', '__httpwww_xbrl_orgintglcor2006_10_25_entryDetailComplexType_httpwww_xbrl_orgintglcor2006_10_25account', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 97, 1), )

    
    account = property(__account.value, __account.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}debitCreditCode uses Python identifier debitCreditCode
    __debitCreditCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'debitCreditCode'), 'debitCreditCode', '__httpwww_xbrl_orgintglcor2006_10_25_entryDetailComplexType_httpwww_xbrl_orgintglcor2006_10_25debitCreditCode', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 102, 1), )

    
    debitCreditCode = property(__debitCreditCode.value, __debitCreditCode.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintglcor2006_10_25_entryDetailComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 45, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 45, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __amount.name() : __amount,
        __beginningEndIndicator.name() : __beginningEndIndicator,
        __programActivity.name() : __programActivity,
        __account.name() : __account,
        __debitCreditCode.name() : __debitCreditCode
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'entryDetailComplexType', entryDetailComplexType)


# Complex type {http://www.xbrl.org/int/gl/cor/2006-10-25}accountComplexType with content type ELEMENT_ONLY
class accountComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/gl/cor/2006-10-25}accountComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'accountComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 49, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}accountNumber uses Python identifier accountNumber
    __accountNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accountNumber'), 'accountNumber', '__httpwww_xbrl_orgintglcor2006_10_25_accountComplexType_httpwww_xbrl_orgintglcor2006_10_25accountNumber', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 98, 1), )

    
    accountNumber = property(__accountNumber.value, __accountNumber.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}objectClass uses Python identifier objectClass
    __objectClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectClass'), 'objectClass', '__httpwww_xbrl_orgintglcor2006_10_25_accountComplexType_httpwww_xbrl_orgintglcor2006_10_25objectClass', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 99, 1), )

    
    objectClass = property(__objectClass.value, __objectClass.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/cor/2006-10-25}accountDescription uses Python identifier accountDescription
    __accountDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accountDescription'), 'accountDescription', '__httpwww_xbrl_orgintglcor2006_10_25_accountComplexType_httpwww_xbrl_orgintglcor2006_10_25accountDescription', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 100, 1), )

    
    accountDescription = property(__accountDescription.value, __accountDescription.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}awardID uses Python identifier awardID
    __awardID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gen, 'awardID'), 'awardID', '__httpwww_xbrl_orgintglcor2006_10_25_accountComplexType_httpwww_xbrl_orgintglgen2006_10_25awardID', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 899, 1), )

    
    awardID = property(__awardID.value, __awardID.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintglcor2006_10_25_accountComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 58, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 58, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accountNumber.name() : __accountNumber,
        __objectClass.name() : __objectClass,
        __accountDescription.name() : __accountDescription,
        __awardID.name() : __awardID
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'accountComplexType', accountComplexType)


# Complex type {http://www.xbrl.org/int/gl/cor/2006-10-25}beginningEndIndicatorItemType with content type SIMPLE
class beginningEndIndicatorItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/cor/2006-10-25}beginningEndIndicatorItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'beginningEndIndicatorItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 67, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'beginningEndIndicatorItemType', beginningEndIndicatorItemType)


# Complex type {http://www.xbrl.org/int/gl/cor/2006-10-25}fiscalYearItemType with content type SIMPLE
class fiscalYearItemType (_ImportedBinding_xbrli.pureItemType):
    """Complex type {http://www.xbrl.org/int/gl/cor/2006-10-25}fiscalYearItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fiscalYearItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 75, 1)
    _ElementMap = _ImportedBinding_xbrli.pureItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.pureItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.pureItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}pureItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}pureItemType
    
    # Attribute unitRef inherited from {http://www.xbrl.org/2003/instance}pureItemType
    
    # Attribute precision inherited from {http://www.xbrl.org/2003/instance}pureItemType
    
    # Attribute decimals inherited from {http://www.xbrl.org/2003/instance}pureItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'fiscalYearItemType', fiscalYearItemType)


accountingEntries = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accountingEntries'), accountingEntriesComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 83, 1))
Namespace.addCategoryObject('elementBinding', accountingEntries.name().localName(), accountingEntries)

fiscalYear = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fiscalYear'), _ImportedBinding_xbrli.stringItemType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 84, 1))
Namespace.addCategoryObject('elementBinding', fiscalYear.name().localName(), fiscalYear)

period = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'period'), _ImportedBinding_xbrli.stringItemType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 85, 1))
Namespace.addCategoryObject('elementBinding', period.name().localName(), period)

USSGLentryHeader = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'USSGLentryHeader'), USSGLentryHeaderComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 86, 1))
Namespace.addCategoryObject('elementBinding', USSGLentryHeader.name().localName(), USSGLentryHeader)

appropriationAccount = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'appropriationAccount'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 92, 1))
Namespace.addCategoryObject('elementBinding', appropriationAccount.name().localName(), appropriationAccount)

entryDetail = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entryDetail'), entryDetailComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 93, 1))
Namespace.addCategoryObject('elementBinding', entryDetail.name().localName(), entryDetail)

programActivity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'programActivity'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 96, 1))
Namespace.addCategoryObject('elementBinding', programActivity.name().localName(), programActivity)

account = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'account'), accountComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 97, 1))
Namespace.addCategoryObject('elementBinding', account.name().localName(), account)

accountNumber = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accountNumber'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 98, 1))
Namespace.addCategoryObject('elementBinding', accountNumber.name().localName(), accountNumber)

objectClass = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectClass'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 99, 1))
Namespace.addCategoryObject('elementBinding', objectClass.name().localName(), objectClass)

accountDescription = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accountDescription'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 100, 1))
Namespace.addCategoryObject('elementBinding', accountDescription.name().localName(), accountDescription)

beginningEndIndicator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beginningEndIndicator'), beginningEndIndicatorItemType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 95, 1))
Namespace.addCategoryObject('elementBinding', beginningEndIndicator.name().localName(), beginningEndIndicator)

debitCreditCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'debitCreditCode'), _ImportedBinding_gen.debitCreditCodeItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 102, 1))
Namespace.addCategoryObject('elementBinding', debitCreditCode.name().localName(), debitCreditCode)

obligatedAmount = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'obligatedAmount'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 87, 1))
Namespace.addCategoryObject('elementBinding', obligatedAmount.name().localName(), obligatedAmount)

unobligatedAmount = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unobligatedAmount'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 88, 1))
Namespace.addCategoryObject('elementBinding', unobligatedAmount.name().localName(), unobligatedAmount)

budgetAuthorityAppropriated = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'budgetAuthorityAppropriated'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 89, 1))
Namespace.addCategoryObject('elementBinding', budgetAuthorityAppropriated.name().localName(), budgetAuthorityAppropriated)

otherBudgetaryResources = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'otherBudgetaryResources'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 90, 1))
Namespace.addCategoryObject('elementBinding', otherBudgetaryResources.name().localName(), otherBudgetaryResources)

outlays = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outlays'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 91, 1))
Namespace.addCategoryObject('elementBinding', outlays.name().localName(), outlays)

amount = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amount'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 94, 1))
Namespace.addCategoryObject('elementBinding', amount.name().localName(), amount)



accountingEntriesComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fiscalYear'), _ImportedBinding_xbrli.stringItemType, scope=accountingEntriesComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 84, 1)))

accountingEntriesComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'period'), _ImportedBinding_xbrli.stringItemType, scope=accountingEntriesComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 85, 1)))

accountingEntriesComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'USSGLentryHeader'), USSGLentryHeaderComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=accountingEntriesComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 86, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 10, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 11, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 12, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(accountingEntriesComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fiscalYear')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 10, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(accountingEntriesComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'period')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 11, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(accountingEntriesComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'USSGLentryHeader')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 12, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
accountingEntriesComplexType._Automaton = _BuildAutomaton()




USSGLentryHeaderComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'obligatedAmount'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=USSGLentryHeaderComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 87, 1)))

USSGLentryHeaderComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unobligatedAmount'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=USSGLentryHeaderComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 88, 1)))

USSGLentryHeaderComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'budgetAuthorityAppropriated'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=USSGLentryHeaderComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 89, 1)))

USSGLentryHeaderComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'otherBudgetaryResources'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=USSGLentryHeaderComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 90, 1)))

USSGLentryHeaderComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outlays'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=USSGLentryHeaderComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 91, 1)))

USSGLentryHeaderComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'appropriationAccount'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=USSGLentryHeaderComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 92, 1)))

USSGLentryHeaderComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entryDetail'), entryDetailComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=USSGLentryHeaderComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 93, 1)))

USSGLentryHeaderComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gen, 'treasuryAccountSymbol'), _ImportedBinding_gen.TreasuryAccountSymbolComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=USSGLentryHeaderComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 865, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(USSGLentryHeaderComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gen, 'treasuryAccountSymbol')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 22, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(USSGLentryHeaderComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entryDetail')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 23, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(USSGLentryHeaderComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'obligatedAmount')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 24, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(USSGLentryHeaderComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unobligatedAmount')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 25, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(USSGLentryHeaderComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'budgetAuthorityAppropriated')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 26, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(USSGLentryHeaderComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'otherBudgetaryResources')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 27, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(USSGLentryHeaderComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outlays')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 28, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(USSGLentryHeaderComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'appropriationAccount')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 29, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
USSGLentryHeaderComplexType._Automaton = _BuildAutomaton_()




entryDetailComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amount'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=entryDetailComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 94, 1)))

entryDetailComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beginningEndIndicator'), beginningEndIndicatorItemType, scope=entryDetailComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 95, 1)))

entryDetailComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'programActivity'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=entryDetailComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 96, 1)))

entryDetailComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'account'), accountComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=entryDetailComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 97, 1)))

entryDetailComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'debitCreditCode'), _ImportedBinding_gen.debitCreditCodeItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=entryDetailComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 102, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(entryDetailComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'account')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 39, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(entryDetailComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amount')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 40, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(entryDetailComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'debitCreditCode')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 41, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(entryDetailComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beginningEndIndicator')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 42, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entryDetailComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'programActivity')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 43, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
entryDetailComplexType._Automaton = _BuildAutomaton_2()




accountComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accountNumber'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=accountComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 98, 1)))

accountComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectClass'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=accountComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 99, 1)))

accountComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accountDescription'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=accountComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 100, 1)))

accountComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gen, 'awardID'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=accountComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 899, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(accountComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accountNumber')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 53, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(accountComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectClass')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 54, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(accountComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gen, 'awardID')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 55, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(accountComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accountDescription')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/ussglfin/da-ussglfin-content-2015-06-29.xsd', 56, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
accountComplexType._Automaton = _BuildAutomaton_3()


accountingEntries._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

fiscalYear._setSubstitutionGroup(_ImportedBinding_xbrli.item)

period._setSubstitutionGroup(_ImportedBinding_xbrli.item)

USSGLentryHeader._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

appropriationAccount._setSubstitutionGroup(_ImportedBinding_xbrli.item)

entryDetail._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

programActivity._setSubstitutionGroup(_ImportedBinding_xbrli.item)

account._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

accountNumber._setSubstitutionGroup(_ImportedBinding_xbrli.item)

objectClass._setSubstitutionGroup(_ImportedBinding_xbrli.item)

accountDescription._setSubstitutionGroup(_ImportedBinding_xbrli.item)

beginningEndIndicator._setSubstitutionGroup(_ImportedBinding_xbrli.item)

debitCreditCode._setSubstitutionGroup(_ImportedBinding_xbrli.item)

obligatedAmount._setSubstitutionGroup(_ImportedBinding_xbrli.item)

unobligatedAmount._setSubstitutionGroup(_ImportedBinding_xbrli.item)

budgetAuthorityAppropriated._setSubstitutionGroup(_ImportedBinding_xbrli.item)

otherBudgetaryResources._setSubstitutionGroup(_ImportedBinding_xbrli.item)

outlays._setSubstitutionGroup(_ImportedBinding_xbrli.item)

amount._setSubstitutionGroup(_ImportedBinding_xbrli.item)
