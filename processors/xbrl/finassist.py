# ./finassist.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:33f4e30661b717ae7082099f096fec7033ac6a83
# Generated 2015-09-09 15:57:00.674134 by PyXB version 1.2.4 using Python 2.7.8.final.0
# Namespace http://www.xbrl.org/int/finassist/2006-10-25

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
import award as _ImportedBinding_award

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.xbrl.org/int/finassist/2006-10-25', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_award = _ImportedBinding_award.Namespace
_Namespace_award.configureCategories(['typeBinding', 'elementBinding'])
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


# Complex type {http://www.xbrl.org/int/finassist/2006-10-25}awardComplexType with content type ELEMENT_ONLY
class awardComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/finassist/2006-10-25}awardComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'awardComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 7, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/award/2006-10-25}awardDescription uses Python identifier awardDescription
    __awardDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'awardDescription'), 'awardDescription', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintaward2006_10_25awardDescription', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 78, 1), )

    
    awardDescription = property(__awardDescription.value, __awardDescription.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}parentAwardID uses Python identifier parentAwardID
    __parentAwardID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'parentAwardID'), 'parentAwardID', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintaward2006_10_25parentAwardID', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 79, 1), )

    
    parentAwardID = property(__parentAwardID.value, __parentAwardID.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}recordType uses Python identifier recordType
    __recordType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'recordType'), 'recordType', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintaward2006_10_25recordType', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 82, 1), )

    
    recordType = property(__recordType.value, __recordType.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}typeOfAction uses Python identifier typeOfAction
    __typeOfAction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'typeOfAction'), 'typeOfAction', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintaward2006_10_25typeOfAction', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 83, 1), )

    
    typeOfAction = property(__typeOfAction.value, __typeOfAction.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}typeOfTransactionCode uses Python identifier typeOfTransactionCode
    __typeOfTransactionCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'typeOfTransactionCode'), 'typeOfTransactionCode', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintaward2006_10_25typeOfTransactionCode', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 84, 1), )

    
    typeOfTransactionCode = property(__typeOfTransactionCode.value, __typeOfTransactionCode.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}modificationAmendmentNumber uses Python identifier modificationAmendmentNumber
    __modificationAmendmentNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'modificationAmendmentNumber'), 'modificationAmendmentNumber', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintaward2006_10_25modificationAmendmentNumber', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 85, 1), )

    
    modificationAmendmentNumber = property(__modificationAmendmentNumber.value, __modificationAmendmentNumber.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}primaryPlaceOfPerformance uses Python identifier primaryPlaceOfPerformance
    __primaryPlaceOfPerformance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'primaryPlaceOfPerformance'), 'primaryPlaceOfPerformance', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintaward2006_10_25primaryPlaceOfPerformance', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 91, 1), )

    
    primaryPlaceOfPerformance = property(__primaryPlaceOfPerformance.value, __primaryPlaceOfPerformance.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}awardingAgency uses Python identifier awardingAgency
    __awardingAgency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'awardingAgency'), 'awardingAgency', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintaward2006_10_25awardingAgency', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 92, 1), )

    
    awardingAgency = property(__awardingAgency.value, __awardingAgency.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}fundingAgency uses Python identifier fundingAgency
    __fundingAgency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'fundingAgency'), 'fundingAgency', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintaward2006_10_25fundingAgency', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 93, 1), )

    
    fundingAgency = property(__fundingAgency.value, __fundingAgency.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}awardingSubTierAgency uses Python identifier awardingSubTierAgency
    __awardingSubTierAgency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'awardingSubTierAgency'), 'awardingSubTierAgency', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintaward2006_10_25awardingSubTierAgency', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 94, 1), )

    
    awardingSubTierAgency = property(__awardingSubTierAgency.value, __awardingSubTierAgency.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}fundingSubTierAgency uses Python identifier fundingSubTierAgency
    __fundingSubTierAgency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'fundingSubTierAgency'), 'fundingSubTierAgency', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintaward2006_10_25fundingSubTierAgency', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 95, 1), )

    
    fundingSubTierAgency = property(__fundingSubTierAgency.value, __fundingSubTierAgency.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}highlyCompensatedOfficer uses Python identifier highlyCompensatedOfficer
    __highlyCompensatedOfficer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'highlyCompensatedOfficer'), 'highlyCompensatedOfficer', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintaward2006_10_25highlyCompensatedOfficer', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 100, 1), )

    
    highlyCompensatedOfficer = property(__highlyCompensatedOfficer.value, __highlyCompensatedOfficer.set, None, None)

    
    # Element {http://www.xbrl.org/int/finassist/2006-10-25}awardeeInformation uses Python identifier awardeeInformation
    __awardeeInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'awardeeInformation'), 'awardeeInformation', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintfinassist2006_10_25awardeeInformation', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 89, 1), )

    
    awardeeInformation = property(__awardeeInformation.value, __awardeeInformation.set, None, None)

    
    # Element {http://www.xbrl.org/int/finassist/2006-10-25}catalogOfFederalDomesticAssistanceProgram uses Python identifier catalogOfFederalDomesticAssistanceProgram
    __catalogOfFederalDomesticAssistanceProgram = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceProgram'), 'catalogOfFederalDomesticAssistanceProgram', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintfinassist2006_10_25catalogOfFederalDomesticAssistanceProgram', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 90, 1), )

    
    catalogOfFederalDomesticAssistanceProgram = property(__catalogOfFederalDomesticAssistanceProgram.value, __catalogOfFederalDomesticAssistanceProgram.set, None, None)

    
    # Element {http://www.xbrl.org/int/finassist/2006-10-25}awardAmounts uses Python identifier awardAmounts
    __awardAmounts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'awardAmounts'), 'awardAmounts', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintfinassist2006_10_25awardAmounts', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 93, 1), )

    
    awardAmounts = property(__awardAmounts.value, __awardAmounts.set, None, None)

    
    # Element {http://www.xbrl.org/int/finassist/2006-10-25}periodOfPerformance uses Python identifier periodOfPerformance
    __periodOfPerformance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'periodOfPerformance'), 'periodOfPerformance', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintfinassist2006_10_25periodOfPerformance', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 94, 1), )

    
    periodOfPerformance = property(__periodOfPerformance.value, __periodOfPerformance.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}awardID uses Python identifier awardID
    __awardID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gen, 'awardID'), 'awardID', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_httpwww_xbrl_orgintglgen2006_10_25awardID', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 899, 1), )

    
    awardID = property(__awardID.value, __awardID.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintfinassist2006_10_25_awardComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 30, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 30, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __awardDescription.name() : __awardDescription,
        __parentAwardID.name() : __parentAwardID,
        __recordType.name() : __recordType,
        __typeOfAction.name() : __typeOfAction,
        __typeOfTransactionCode.name() : __typeOfTransactionCode,
        __modificationAmendmentNumber.name() : __modificationAmendmentNumber,
        __primaryPlaceOfPerformance.name() : __primaryPlaceOfPerformance,
        __awardingAgency.name() : __awardingAgency,
        __fundingAgency.name() : __fundingAgency,
        __awardingSubTierAgency.name() : __awardingSubTierAgency,
        __fundingSubTierAgency.name() : __fundingSubTierAgency,
        __highlyCompensatedOfficer.name() : __highlyCompensatedOfficer,
        __awardeeInformation.name() : __awardeeInformation,
        __catalogOfFederalDomesticAssistanceProgram.name() : __catalogOfFederalDomesticAssistanceProgram,
        __awardAmounts.name() : __awardAmounts,
        __periodOfPerformance.name() : __periodOfPerformance,
        __awardID.name() : __awardID
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'awardComplexType', awardComplexType)


# Complex type {http://www.xbrl.org/int/finassist/2006-10-25}catalogOfFederalDomesticAssistanceProgramComplexType with content type ELEMENT_ONLY
class catalogOfFederalDomesticAssistanceProgramComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/finassist/2006-10-25}catalogOfFederalDomesticAssistanceProgramComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceProgramComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 34, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/finassist/2006-10-25}catalogOfFederalDomesticAssistanceTitle uses Python identifier catalogOfFederalDomesticAssistanceTitle
    __catalogOfFederalDomesticAssistanceTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceTitle'), 'catalogOfFederalDomesticAssistanceTitle', '__httpwww_xbrl_orgintfinassist2006_10_25_catalogOfFederalDomesticAssistanceProgramComplexType_httpwww_xbrl_orgintfinassist2006_10_25catalogOfFederalDomesticAssistanceTitle', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 91, 1), )

    
    catalogOfFederalDomesticAssistanceTitle = property(__catalogOfFederalDomesticAssistanceTitle.value, __catalogOfFederalDomesticAssistanceTitle.set, None, None)

    
    # Element {http://www.xbrl.org/int/finassist/2006-10-25}catalogOfFederalDomesticAssistanceNumber uses Python identifier catalogOfFederalDomesticAssistanceNumber
    __catalogOfFederalDomesticAssistanceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceNumber'), 'catalogOfFederalDomesticAssistanceNumber', '__httpwww_xbrl_orgintfinassist2006_10_25_catalogOfFederalDomesticAssistanceProgramComplexType_httpwww_xbrl_orgintfinassist2006_10_25catalogOfFederalDomesticAssistanceNumber', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 92, 1), )

    
    catalogOfFederalDomesticAssistanceNumber = property(__catalogOfFederalDomesticAssistanceNumber.value, __catalogOfFederalDomesticAssistanceNumber.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintfinassist2006_10_25_catalogOfFederalDomesticAssistanceProgramComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 41, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 41, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __catalogOfFederalDomesticAssistanceTitle.name() : __catalogOfFederalDomesticAssistanceTitle,
        __catalogOfFederalDomesticAssistanceNumber.name() : __catalogOfFederalDomesticAssistanceNumber
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'catalogOfFederalDomesticAssistanceProgramComplexType', catalogOfFederalDomesticAssistanceProgramComplexType)


# Complex type {http://www.xbrl.org/int/finassist/2006-10-25}awardAmountsComplexType with content type ELEMENT_ONLY
class awardAmountsComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/finassist/2006-10-25}awardAmountsComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'awardAmountsComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 45, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/award/2006-10-25}federalFundingAmount uses Python identifier federalFundingAmount
    __federalFundingAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'federalFundingAmount'), 'federalFundingAmount', '__httpwww_xbrl_orgintfinassist2006_10_25_awardAmountsComplexType_httpwww_xbrl_orgintaward2006_10_25federalFundingAmount', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 105, 1), )

    
    federalFundingAmount = property(__federalFundingAmount.value, __federalFundingAmount.set, None, None)

    
    # Element {http://www.xbrl.org/int/finassist/2006-10-25}totalFundingAmount uses Python identifier totalFundingAmount
    __totalFundingAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'totalFundingAmount'), 'totalFundingAmount', '__httpwww_xbrl_orgintfinassist2006_10_25_awardAmountsComplexType_httpwww_xbrl_orgintfinassist2006_10_25totalFundingAmount', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 95, 1), )

    
    totalFundingAmount = property(__totalFundingAmount.value, __totalFundingAmount.set, None, None)

    
    # Element {http://www.xbrl.org/int/finassist/2006-10-25}nonFederalFundingAmount uses Python identifier nonFederalFundingAmount
    __nonFederalFundingAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nonFederalFundingAmount'), 'nonFederalFundingAmount', '__httpwww_xbrl_orgintfinassist2006_10_25_awardAmountsComplexType_httpwww_xbrl_orgintfinassist2006_10_25nonFederalFundingAmount', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 96, 1), )

    
    nonFederalFundingAmount = property(__nonFederalFundingAmount.value, __nonFederalFundingAmount.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintfinassist2006_10_25_awardAmountsComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 53, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 53, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __federalFundingAmount.name() : __federalFundingAmount,
        __totalFundingAmount.name() : __totalFundingAmount,
        __nonFederalFundingAmount.name() : __nonFederalFundingAmount
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'awardAmountsComplexType', awardAmountsComplexType)


# Complex type {http://www.xbrl.org/int/finassist/2006-10-25}awardeeInformationComplexType with content type ELEMENT_ONLY
class awardeeInformationComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/finassist/2006-10-25}awardeeInformationComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'awardeeInformationComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 57, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/award/2006-10-25}awardeeLegalBusinessName uses Python identifier awardeeLegalBusinessName
    __awardeeLegalBusinessName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'awardeeLegalBusinessName'), 'awardeeLegalBusinessName', '__httpwww_xbrl_orgintfinassist2006_10_25_awardeeInformationComplexType_httpwww_xbrl_orgintaward2006_10_25awardeeLegalBusinessName', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 80, 1), )

    
    awardeeLegalBusinessName = property(__awardeeLegalBusinessName.value, __awardeeLegalBusinessName.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}businessType uses Python identifier businessType
    __businessType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'businessType'), 'businessType', '__httpwww_xbrl_orgintfinassist2006_10_25_awardeeInformationComplexType_httpwww_xbrl_orgintaward2006_10_25businessType', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 81, 1), )

    
    businessType = property(__businessType.value, __businessType.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}ultimateParentUniqueIdentifier uses Python identifier ultimateParentUniqueIdentifier
    __ultimateParentUniqueIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'ultimateParentUniqueIdentifier'), 'ultimateParentUniqueIdentifier', '__httpwww_xbrl_orgintfinassist2006_10_25_awardeeInformationComplexType_httpwww_xbrl_orgintaward2006_10_25ultimateParentUniqueIdentifier', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 86, 1), )

    
    ultimateParentUniqueIdentifier = property(__ultimateParentUniqueIdentifier.value, __ultimateParentUniqueIdentifier.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}awardeeUniqueIdentifier uses Python identifier awardeeUniqueIdentifier
    __awardeeUniqueIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'awardeeUniqueIdentifier'), 'awardeeUniqueIdentifier', '__httpwww_xbrl_orgintfinassist2006_10_25_awardeeInformationComplexType_httpwww_xbrl_orgintaward2006_10_25awardeeUniqueIdentifier', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 87, 1), )

    
    awardeeUniqueIdentifier = property(__awardeeUniqueIdentifier.value, __awardeeUniqueIdentifier.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}awardeeUniqueIdentifierSupplemental uses Python identifier awardeeUniqueIdentifierSupplemental
    __awardeeUniqueIdentifierSupplemental = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'awardeeUniqueIdentifierSupplemental'), 'awardeeUniqueIdentifierSupplemental', '__httpwww_xbrl_orgintfinassist2006_10_25_awardeeInformationComplexType_httpwww_xbrl_orgintaward2006_10_25awardeeUniqueIdentifierSupplemental', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 88, 1), )

    
    awardeeUniqueIdentifierSupplemental = property(__awardeeUniqueIdentifierSupplemental.value, __awardeeUniqueIdentifierSupplemental.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}ultimateParentLegalBusinessName uses Python identifier ultimateParentLegalBusinessName
    __ultimateParentLegalBusinessName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'ultimateParentLegalBusinessName'), 'ultimateParentLegalBusinessName', '__httpwww_xbrl_orgintfinassist2006_10_25_awardeeInformationComplexType_httpwww_xbrl_orgintaward2006_10_25ultimateParentLegalBusinessName', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 89, 1), )

    
    ultimateParentLegalBusinessName = property(__ultimateParentLegalBusinessName.value, __ultimateParentLegalBusinessName.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}awardeeAddress uses Python identifier awardeeAddress
    __awardeeAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'awardeeAddress'), 'awardeeAddress', '__httpwww_xbrl_orgintfinassist2006_10_25_awardeeInformationComplexType_httpwww_xbrl_orgintaward2006_10_25awardeeAddress', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 90, 1), )

    
    awardeeAddress = property(__awardeeAddress.value, __awardeeAddress.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintfinassist2006_10_25_awardeeInformationComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 69, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 69, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __awardeeLegalBusinessName.name() : __awardeeLegalBusinessName,
        __businessType.name() : __businessType,
        __ultimateParentUniqueIdentifier.name() : __ultimateParentUniqueIdentifier,
        __awardeeUniqueIdentifier.name() : __awardeeUniqueIdentifier,
        __awardeeUniqueIdentifierSupplemental.name() : __awardeeUniqueIdentifierSupplemental,
        __ultimateParentLegalBusinessName.name() : __ultimateParentLegalBusinessName,
        __awardeeAddress.name() : __awardeeAddress
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'awardeeInformationComplexType', awardeeInformationComplexType)


# Complex type {http://www.xbrl.org/int/finassist/2006-10-25}periodOfPerformanceComplexType with content type ELEMENT_ONLY
class periodOfPerformanceComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/finassist/2006-10-25}periodOfPerformanceComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'periodOfPerformanceComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 73, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/award/2006-10-25}periodOfPerformanceActionDate uses Python identifier periodOfPerformanceActionDate
    __periodOfPerformanceActionDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'periodOfPerformanceActionDate'), 'periodOfPerformanceActionDate', '__httpwww_xbrl_orgintfinassist2006_10_25_periodOfPerformanceComplexType_httpwww_xbrl_orgintaward2006_10_25periodOfPerformanceActionDate', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 96, 1), )

    
    periodOfPerformanceActionDate = property(__periodOfPerformanceActionDate.value, __periodOfPerformanceActionDate.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}periodOfPerformanceStartDate uses Python identifier periodOfPerformanceStartDate
    __periodOfPerformanceStartDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'periodOfPerformanceStartDate'), 'periodOfPerformanceStartDate', '__httpwww_xbrl_orgintfinassist2006_10_25_periodOfPerformanceComplexType_httpwww_xbrl_orgintaward2006_10_25periodOfPerformanceStartDate', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 97, 1), )

    
    periodOfPerformanceStartDate = property(__periodOfPerformanceStartDate.value, __periodOfPerformanceStartDate.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}periodOfPerformanceCurrentEndDate uses Python identifier periodOfPerformanceCurrentEndDate
    __periodOfPerformanceCurrentEndDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'periodOfPerformanceCurrentEndDate'), 'periodOfPerformanceCurrentEndDate', '__httpwww_xbrl_orgintfinassist2006_10_25_periodOfPerformanceComplexType_httpwww_xbrl_orgintaward2006_10_25periodOfPerformanceCurrentEndDate', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 98, 1), )

    
    periodOfPerformanceCurrentEndDate = property(__periodOfPerformanceCurrentEndDate.value, __periodOfPerformanceCurrentEndDate.set, None, None)

    
    # Element {http://www.xbrl.org/int/award/2006-10-25}periodOfPerformancePotentialEndDate uses Python identifier periodOfPerformancePotentialEndDate
    __periodOfPerformancePotentialEndDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_award, 'periodOfPerformancePotentialEndDate'), 'periodOfPerformancePotentialEndDate', '__httpwww_xbrl_orgintfinassist2006_10_25_periodOfPerformanceComplexType_httpwww_xbrl_orgintaward2006_10_25periodOfPerformancePotentialEndDate', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 99, 1), )

    
    periodOfPerformancePotentialEndDate = property(__periodOfPerformancePotentialEndDate.value, __periodOfPerformancePotentialEndDate.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintfinassist2006_10_25_periodOfPerformanceComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 82, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 82, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __periodOfPerformanceActionDate.name() : __periodOfPerformanceActionDate,
        __periodOfPerformanceStartDate.name() : __periodOfPerformanceStartDate,
        __periodOfPerformanceCurrentEndDate.name() : __periodOfPerformanceCurrentEndDate,
        __periodOfPerformancePotentialEndDate.name() : __periodOfPerformancePotentialEndDate
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'periodOfPerformanceComplexType', periodOfPerformanceComplexType)


award = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'award'), awardComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 88, 1))
Namespace.addCategoryObject('elementBinding', award.name().localName(), award)

awardeeInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardeeInformation'), awardeeInformationComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 89, 1))
Namespace.addCategoryObject('elementBinding', awardeeInformation.name().localName(), awardeeInformation)

catalogOfFederalDomesticAssistanceProgram = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceProgram'), catalogOfFederalDomesticAssistanceProgramComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 90, 1))
Namespace.addCategoryObject('elementBinding', catalogOfFederalDomesticAssistanceProgram.name().localName(), catalogOfFederalDomesticAssistanceProgram)

catalogOfFederalDomesticAssistanceTitle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceTitle'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 91, 1))
Namespace.addCategoryObject('elementBinding', catalogOfFederalDomesticAssistanceTitle.name().localName(), catalogOfFederalDomesticAssistanceTitle)

catalogOfFederalDomesticAssistanceNumber = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceNumber'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 92, 1))
Namespace.addCategoryObject('elementBinding', catalogOfFederalDomesticAssistanceNumber.name().localName(), catalogOfFederalDomesticAssistanceNumber)

awardAmounts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardAmounts'), awardAmountsComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 93, 1))
Namespace.addCategoryObject('elementBinding', awardAmounts.name().localName(), awardAmounts)

periodOfPerformance = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'periodOfPerformance'), periodOfPerformanceComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 94, 1))
Namespace.addCategoryObject('elementBinding', periodOfPerformance.name().localName(), periodOfPerformance)

totalFundingAmount = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totalFundingAmount'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 95, 1))
Namespace.addCategoryObject('elementBinding', totalFundingAmount.name().localName(), totalFundingAmount)

nonFederalFundingAmount = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nonFederalFundingAmount'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 96, 1))
Namespace.addCategoryObject('elementBinding', nonFederalFundingAmount.name().localName(), nonFederalFundingAmount)



awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'awardDescription'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 78, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'parentAwardID'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 79, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'recordType'), _ImportedBinding_award.recordTypeItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 82, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'typeOfAction'), _ImportedBinding_award.typeOfActionItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 83, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'typeOfTransactionCode'), _ImportedBinding_award.typeOfTransactionCodeItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 84, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'modificationAmendmentNumber'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 85, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'primaryPlaceOfPerformance'), _ImportedBinding_gen.addressComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 91, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'awardingAgency'), _ImportedBinding_gen.agencyComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 92, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'fundingAgency'), _ImportedBinding_gen.agencyComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 93, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'awardingSubTierAgency'), _ImportedBinding_gen.agencyComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 94, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'fundingSubTierAgency'), _ImportedBinding_gen.agencyComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 95, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'highlyCompensatedOfficer'), _ImportedBinding_award.highlyCompensatedOfficerComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 100, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardeeInformation'), awardeeInformationComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 89, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceProgram'), catalogOfFederalDomesticAssistanceProgramComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 90, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardAmounts'), awardAmountsComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 93, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'periodOfPerformance'), periodOfPerformanceComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 94, 1)))

awardComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gen, 'awardID'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 899, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 19, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 20, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 21, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 22, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 23, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 24, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=5, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 25, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 26, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 27, 5))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'awardDescription')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 11, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gen, 'awardID')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 12, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'parentAwardID')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 13, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'modificationAmendmentNumber')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 14, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'recordType')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 15, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'typeOfAction')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 16, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'typeOfTransactionCode')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 17, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'awardeeInformation')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 18, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'primaryPlaceOfPerformance')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 19, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'periodOfPerformance')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 20, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'awardingAgency')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 21, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'fundingAgency')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 22, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'awardingSubTierAgency')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 23, 5))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'fundingSubTierAgency')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 24, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'highlyCompensatedOfficer')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 25, 5))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceProgram')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 26, 5))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(awardComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'awardAmounts')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 27, 5))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
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
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
awardComplexType._Automaton = _BuildAutomaton()




catalogOfFederalDomesticAssistanceProgramComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceTitle'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=catalogOfFederalDomesticAssistanceProgramComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 91, 1)))

catalogOfFederalDomesticAssistanceProgramComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceNumber'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=catalogOfFederalDomesticAssistanceProgramComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 92, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 38, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 39, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(catalogOfFederalDomesticAssistanceProgramComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceTitle')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 38, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(catalogOfFederalDomesticAssistanceProgramComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'catalogOfFederalDomesticAssistanceNumber')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 39, 5))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
catalogOfFederalDomesticAssistanceProgramComplexType._Automaton = _BuildAutomaton_()




awardAmountsComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'federalFundingAmount'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardAmountsComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 105, 1)))

awardAmountsComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totalFundingAmount'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardAmountsComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 95, 1)))

awardAmountsComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nonFederalFundingAmount'), _ImportedBinding_gen.amountItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardAmountsComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 96, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 49, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 50, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 51, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(awardAmountsComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'federalFundingAmount')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 49, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(awardAmountsComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'totalFundingAmount')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 50, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(awardAmountsComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nonFederalFundingAmount')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 51, 5))
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
awardAmountsComplexType._Automaton = _BuildAutomaton_2()




awardeeInformationComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'awardeeLegalBusinessName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardeeInformationComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 80, 1)))

awardeeInformationComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'businessType'), _ImportedBinding_award.businessTypeItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardeeInformationComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 81, 1)))

awardeeInformationComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'ultimateParentUniqueIdentifier'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardeeInformationComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 86, 1)))

awardeeInformationComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'awardeeUniqueIdentifier'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardeeInformationComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 87, 1)))

awardeeInformationComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'awardeeUniqueIdentifierSupplemental'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardeeInformationComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 88, 1)))

awardeeInformationComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'ultimateParentLegalBusinessName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardeeInformationComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 89, 1)))

awardeeInformationComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'awardeeAddress'), _ImportedBinding_gen.addressComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=awardeeInformationComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 90, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardeeInformationComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'businessType')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 61, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardeeInformationComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'awardeeLegalBusinessName')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 62, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardeeInformationComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'ultimateParentUniqueIdentifier')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 63, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardeeInformationComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'awardeeUniqueIdentifier')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 64, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardeeInformationComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'awardeeUniqueIdentifierSupplemental')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 65, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(awardeeInformationComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'ultimateParentLegalBusinessName')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 66, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(awardeeInformationComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'awardeeAddress')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 67, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
awardeeInformationComplexType._Automaton = _BuildAutomaton_3()




periodOfPerformanceComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'periodOfPerformanceActionDate'), _ImportedBinding_xbrli.dateItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=periodOfPerformanceComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 96, 1)))

periodOfPerformanceComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'periodOfPerformanceStartDate'), _ImportedBinding_xbrli.dateItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=periodOfPerformanceComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 97, 1)))

periodOfPerformanceComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'periodOfPerformanceCurrentEndDate'), _ImportedBinding_xbrli.dateItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=periodOfPerformanceComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 98, 1)))

periodOfPerformanceComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_award, 'periodOfPerformancePotentialEndDate'), _ImportedBinding_xbrli.dateItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=periodOfPerformanceComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/award/da-award-content-2015-06-29.xsd', 99, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 77, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 78, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 79, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 80, 5))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(periodOfPerformanceComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'periodOfPerformanceActionDate')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 77, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(periodOfPerformanceComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'periodOfPerformanceStartDate')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 78, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(periodOfPerformanceComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'periodOfPerformanceCurrentEndDate')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 79, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(periodOfPerformanceComplexType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_award, 'periodOfPerformancePotentialEndDate')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/finassist/da-finassist-content-2015-06-29.xsd', 80, 5))
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
periodOfPerformanceComplexType._Automaton = _BuildAutomaton_4()


award._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

awardeeInformation._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

catalogOfFederalDomesticAssistanceProgram._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

catalogOfFederalDomesticAssistanceTitle._setSubstitutionGroup(_ImportedBinding_xbrli.item)

catalogOfFederalDomesticAssistanceNumber._setSubstitutionGroup(_ImportedBinding_xbrli.item)

awardAmounts._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

periodOfPerformance._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

totalFundingAmount._setSubstitutionGroup(_ImportedBinding_xbrli.item)

nonFederalFundingAmount._setSubstitutionGroup(_ImportedBinding_xbrli.item)
