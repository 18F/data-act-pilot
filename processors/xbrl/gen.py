# ./gen.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:150b54fdf036d7ac8617514f7fe4f5309a33b903
# Generated 2015-09-09 15:57:00.673218 by PyXB version 1.2.4 using Python 2.7.8.final.0
# Namespace http://www.xbrl.org/int/gl/gen/2006-10-25 [xmlns:gen]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.xbrl.org/int/gl/gen/2006-10-25', create_if_missing=True)
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 6, 1)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.consolidating = STD_ANON._CF_enumeration.addEnumeration(unicode_value='consolidating', tag='consolidating')
STD_ANON.european = STD_ANON._CF_enumeration.addEnumeration(unicode_value='european', tag='european')
STD_ANON.ifrs = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ifrs', tag='ifrs')
STD_ANON.offsetting = STD_ANON._CF_enumeration.addEnumeration(unicode_value='offsetting', tag='offsetting')
STD_ANON.primary = STD_ANON._CF_enumeration.addEnumeration(unicode_value='primary', tag='primary')
STD_ANON.tax = STD_ANON._CF_enumeration.addEnumeration(unicode_value='tax', tag='tax')
STD_ANON.usgaap = STD_ANON._CF_enumeration.addEnumeration(unicode_value='usgaap', tag='usgaap')
STD_ANON.japanese = STD_ANON._CF_enumeration.addEnumeration(unicode_value='japanese', tag='japanese')
STD_ANON.other = STD_ANON._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 21, 1)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.account = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='account', tag='account')
STD_ANON_.bank = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='bank', tag='bank')
STD_ANON_.employee = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='employee', tag='employee')
STD_ANON_.customer = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='customer', tag='customer')
STD_ANON_.job = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='job', tag='job')
STD_ANON_.vendor = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='vendor', tag='vendor')
STD_ANON_.measurable = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='measurable', tag='measurable')
STD_ANON_.statistical = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='statistical', tag='statistical')
STD_ANON_.other = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 36, 1)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.permanent = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='permanent', tag='permanent')
STD_ANON_2.temporary = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='temporary', tag='temporary')
STD_ANON_2.none = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 45, 1)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.individual = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='individual', tag='individual')
STD_ANON_3.organization = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='organization', tag='organization')
STD_ANON_3.other = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 54, 1)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.D = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
STD_ANON_4.C = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
STD_ANON_4.debit = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='debit', tag='debit')
STD_ANON_4.credit = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='credit', tag='credit')
STD_ANON_4.undefined = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='undefined', tag='undefined')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 65, 1)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.check = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='check', tag='check')
STD_ANON_5.debit_memo = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='debit-memo', tag='debit_memo')
STD_ANON_5.credit_memo = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='credit-memo', tag='credit_memo')
STD_ANON_5.finance_charge = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='finance-charge', tag='finance_charge')
STD_ANON_5.invoice = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='invoice', tag='invoice')
STD_ANON_5.order_customer = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='order-customer', tag='order_customer')
STD_ANON_5.order_vendor = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='order-vendor', tag='order_vendor')
STD_ANON_5.payment_other = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='payment-other', tag='payment_other')
STD_ANON_5.reminder = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='reminder', tag='reminder')
STD_ANON_5.tegata = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='tegata', tag='tegata')
STD_ANON_5.voucher = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='voucher', tag='voucher')
STD_ANON_5.shipment = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='shipment', tag='shipment')
STD_ANON_5.receipt = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='receipt', tag='receipt')
STD_ANON_5.manual_adjustment = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='manual-adjustment', tag='manual_adjustment')
STD_ANON_5.other = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 86, 1)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6, enum_prefix=None)
STD_ANON_6.ePos = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='ePos', tag='ePos')
STD_ANON_6.self_billed = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='self-billed', tag='self_billed')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 94, 1)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_7, enum_prefix=None)
STD_ANON_7.account = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='account', tag='account')
STD_ANON_7.balance = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='balance', tag='balance')
STD_ANON_7.entries = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='entries', tag='entries')
STD_ANON_7.journal = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='journal', tag='journal')
STD_ANON_7.ledger = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='ledger', tag='ledger')
STD_ANON_7.assets = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='assets', tag='assets')
STD_ANON_7.trialbalance = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='trialbalance', tag='trialbalance')
STD_ANON_7.taxtables = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='taxtables', tag='taxtables')
STD_ANON_7.other = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 109, 1)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_8, enum_prefix=None)
STD_ANON_8.adjusting = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='adjusting', tag='adjusting')
STD_ANON_8.budget = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='budget', tag='budget')
STD_ANON_8.comparative = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='comparative', tag='comparative')
STD_ANON_8.external_accountant = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='external-accountant', tag='external_accountant')
STD_ANON_8.standard = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='standard', tag='standard')
STD_ANON_8.passed_adjusting = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='passed-adjusting', tag='passed_adjusting')
STD_ANON_8.eliminating = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='eliminating', tag='eliminating')
STD_ANON_8.proposed = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='proposed', tag='proposed')
STD_ANON_8.recurring = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='recurring', tag='recurring')
STD_ANON_8.reclassifying = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='reclassifying', tag='reclassifying')
STD_ANON_8.simulated = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='simulated', tag='simulated')
STD_ANON_8.tax = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='tax', tag='tax')
STD_ANON_8.other = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 128, 1)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_9, enum_prefix=None)
STD_ANON_9.C = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
STD_ANON_9.customer = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='customer', tag='customer')
STD_ANON_9.E = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='E', tag='E')
STD_ANON_9.employee = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='employee', tag='employee')
STD_ANON_9.V = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='V', tag='V')
STD_ANON_9.vendor = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='vendor', tag='vendor')
STD_ANON_9.O = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='O', tag='O')
STD_ANON_9.other = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_9.I = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='I', tag='I')
STD_ANON_9.salesperson_internal = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='salesperson-internal', tag='salesperson_internal')
STD_ANON_9.X = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='X', tag='X')
STD_ANON_9.salesperson_external = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='salesperson-external', tag='salesperson_external')
STD_ANON_9.N = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
STD_ANON_9.contractor = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='contractor', tag='contractor')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 148, 1)
    _Documentation = None
STD_ANON_10._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_10, enum_prefix=None)
STD_ANON_10.asset = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='asset', tag='asset')
STD_ANON_10.liability = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='liability', tag='liability')
STD_ANON_10.equity = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='equity', tag='equity')
STD_ANON_10.income = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='income', tag='income')
STD_ANON_10.gain = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='gain', tag='gain')
STD_ANON_10.expense = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='expense', tag='expense')
STD_ANON_10.loss = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='loss', tag='loss')
STD_ANON_10.contr_to_equity = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='contr-to-equity', tag='contr_to_equity')
STD_ANON_10.distr_from_equity = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='distr-from-equity', tag='distr_from_equity')
STD_ANON_10.comprehensive_income = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='comprehensive-income', tag='comprehensive_income')
STD_ANON_10.other = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 165, 1)
    _Documentation = None
STD_ANON_11._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_11, enum_prefix=None)
STD_ANON_11.deferred = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='deferred', tag='deferred')
STD_ANON_11.posted = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='posted', tag='posted')
STD_ANON_11.proposed = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='proposed', tag='proposed')
STD_ANON_11.simulated = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='simulated', tag='simulated')
STD_ANON_11.tax = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='tax', tag='tax')
STD_ANON_11.unposted = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='unposted', tag='unposted')
STD_ANON_11.cancelled = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='cancelled', tag='cancelled')
STD_ANON_11.other = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 179, 1)
    _Documentation = None
STD_ANON_12._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_12, enum_prefix=None)
STD_ANON_12.standard = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='standard', tag='standard')
STD_ANON_12.balance_brought_forward = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='balance-brought-forward', tag='balance_brought_forward')
STD_ANON_12.other = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 188, 1)
    _Documentation = None
STD_ANON_13._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_13, enum_prefix=None)
STD_ANON_13.supplement = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='supplement', tag='supplement')
STD_ANON_13.supersede = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='supersede', tag='supersede')
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 196, 1)
    _Documentation = None
STD_ANON_14._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_14, enum_prefix=None)
STD_ANON_14.emptyString = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='+', tag='emptyString')
STD_ANON_14.emptyString_ = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='-', tag='emptyString_')
STD_ANON_14.plus = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='plus', tag='plus')
STD_ANON_14.minus = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='minus', tag='minus')
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 206, 1)
    _Documentation = None
STD_ANON_15._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_15, enum_prefix=None)
STD_ANON_15.cd = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='cd', tag='cd')
STD_ANON_15.cr = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='cr', tag='cr')
STD_ANON_15.fa = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='fa', tag='fa')
STD_ANON_15.gi = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='gi', tag='gi')
STD_ANON_15.gj = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='gj', tag='gj')
STD_ANON_15.im = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='im', tag='im')
STD_ANON_15.jc = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='jc', tag='jc')
STD_ANON_15.pj = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='pj', tag='pj')
STD_ANON_15.pl = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='pl', tag='pl')
STD_ANON_15.sj = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='sj', tag='sj')
STD_ANON_15.se = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='se', tag='se')
STD_ANON_15.ud = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='ud', tag='ud')
STD_ANON_15.ot = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='ot', tag='ot')
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 225, 1)
    _Documentation = None
STD_ANON_16._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_16, enum_prefix=None)
STD_ANON_16.beginning_balance = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='beginning_balance', tag='beginning_balance')
STD_ANON_16.ending_balance = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='ending_balance', tag='ending_balance')
STD_ANON_16.period_change = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='period_change', tag='period_change')
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 234, 1)
    _Documentation = None
STD_ANON_17._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_17, enum_prefix=None)
STD_ANON_17.bookkeeper = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='bookkeeper', tag='bookkeeper')
STD_ANON_17.controller = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='controller', tag='controller')
STD_ANON_17.direct = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='direct', tag='direct')
STD_ANON_17.fax = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='fax', tag='fax')
STD_ANON_17.investor_relations = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='investor-relations', tag='investor_relations')
STD_ANON_17.main = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='main', tag='main')
STD_ANON_17.switchboard = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='switchboard', tag='switchboard')
STD_ANON_17.other = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 250, 1)
    _Documentation = None
STD_ANON_18._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_18, enum_prefix=None)
STD_ANON_18.A = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
STD_ANON_18.F = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
STD_ANON_18.X = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='X', tag='X')
STD_ANON_18.null = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='null', tag='null')
STD_ANON_18.emptyString = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='', tag='emptyString')
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_19 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 339, 1)
    _Documentation = None
STD_ANON_19._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_19, enum_prefix=None)
STD_ANON_19.Alabama_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Alabama 1st', tag='Alabama_1st')
STD_ANON_19.Alabama_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Alabama 2nd', tag='Alabama_2nd')
STD_ANON_19.Alabama_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Alabama 3rd', tag='Alabama_3rd')
STD_ANON_19.Alabama_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Alabama 4th', tag='Alabama_4th')
STD_ANON_19.Alabama_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Alabama 5th', tag='Alabama_5th')
STD_ANON_19.Alabama_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Alabama 6th', tag='Alabama_6th')
STD_ANON_19.Alabama_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Alabama 7th', tag='Alabama_7th')
STD_ANON_19.Alaska_at_large = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Alaska at large', tag='Alaska_at_large')
STD_ANON_19.Arizona_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Arizona 1st', tag='Arizona_1st')
STD_ANON_19.Arizona_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Arizona 2nd', tag='Arizona_2nd')
STD_ANON_19.Arizona_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Arizona 3rd', tag='Arizona_3rd')
STD_ANON_19.Arizona_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Arizona 4th', tag='Arizona_4th')
STD_ANON_19.Arizona_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Arizona 5th', tag='Arizona_5th')
STD_ANON_19.Arizona_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Arizona 6th', tag='Arizona_6th')
STD_ANON_19.Arizona_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Arizona 7th', tag='Arizona_7th')
STD_ANON_19.Arizona_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Arizona 8th', tag='Arizona_8th')
STD_ANON_19.Arkansas_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Arkansas 1st', tag='Arkansas_1st')
STD_ANON_19.Arkansas_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Arkansas 2nd', tag='Arkansas_2nd')
STD_ANON_19.Arkansas_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Arkansas 3rd', tag='Arkansas_3rd')
STD_ANON_19.Arkansas_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Arkansas 4th', tag='Arkansas_4th')
STD_ANON_19.California_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 10th', tag='California_10th')
STD_ANON_19.California_11th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 11th', tag='California_11th')
STD_ANON_19.California_12th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 12th', tag='California_12th')
STD_ANON_19.California_13th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 13th', tag='California_13th')
STD_ANON_19.California_14th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 14th', tag='California_14th')
STD_ANON_19.California_15th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 15th', tag='California_15th')
STD_ANON_19.California_16th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 16th', tag='California_16th')
STD_ANON_19.California_17th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 17th', tag='California_17th')
STD_ANON_19.California_18th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 18th', tag='California_18th')
STD_ANON_19.California_19th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 19th', tag='California_19th')
STD_ANON_19.California_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 1st', tag='California_1st')
STD_ANON_19.California_20th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 20th', tag='California_20th')
STD_ANON_19.California_21st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 21st', tag='California_21st')
STD_ANON_19.California_22nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 22nd', tag='California_22nd')
STD_ANON_19.California_23rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 23rd', tag='California_23rd')
STD_ANON_19.California_24th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 24th', tag='California_24th')
STD_ANON_19.California_25th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 25th', tag='California_25th')
STD_ANON_19.California_26th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 26th', tag='California_26th')
STD_ANON_19.California_27th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 27th', tag='California_27th')
STD_ANON_19.California_28th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 28th', tag='California_28th')
STD_ANON_19.California_29th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 29th', tag='California_29th')
STD_ANON_19.California_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 2nd', tag='California_2nd')
STD_ANON_19.California_30th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 30th', tag='California_30th')
STD_ANON_19.California_31st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 31st', tag='California_31st')
STD_ANON_19.California_32nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 32nd', tag='California_32nd')
STD_ANON_19.California_33rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 33rd', tag='California_33rd')
STD_ANON_19.California_34th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 34th', tag='California_34th')
STD_ANON_19.California_35th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 35th', tag='California_35th')
STD_ANON_19.California_36th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 36th', tag='California_36th')
STD_ANON_19.California_37th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 37th', tag='California_37th')
STD_ANON_19.California_38th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 38th', tag='California_38th')
STD_ANON_19.California_39th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 39th', tag='California_39th')
STD_ANON_19.California_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 3rd', tag='California_3rd')
STD_ANON_19.California_40th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 40th', tag='California_40th')
STD_ANON_19.California_41st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 41st', tag='California_41st')
STD_ANON_19.California_42nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 42nd', tag='California_42nd')
STD_ANON_19.California_43rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 43rd', tag='California_43rd')
STD_ANON_19.California_44th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 44th', tag='California_44th')
STD_ANON_19.California_45th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 45th', tag='California_45th')
STD_ANON_19.California_46th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 46th', tag='California_46th')
STD_ANON_19.California_47th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 47th', tag='California_47th')
STD_ANON_19.California_48th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 48th', tag='California_48th')
STD_ANON_19.California_49th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 49th', tag='California_49th')
STD_ANON_19.California_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 4th', tag='California_4th')
STD_ANON_19.California_50th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 50th', tag='California_50th')
STD_ANON_19.California_51st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 51st', tag='California_51st')
STD_ANON_19.California_52nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 52nd', tag='California_52nd')
STD_ANON_19.California_53rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 53rd', tag='California_53rd')
STD_ANON_19.California_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 5th', tag='California_5th')
STD_ANON_19.California_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 6th', tag='California_6th')
STD_ANON_19.California_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 7th', tag='California_7th')
STD_ANON_19.California_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 8th', tag='California_8th')
STD_ANON_19.California_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='California 9th', tag='California_9th')
STD_ANON_19.Colorado_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Colorado 1st', tag='Colorado_1st')
STD_ANON_19.Colorado_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Colorado 2nd', tag='Colorado_2nd')
STD_ANON_19.Colorado_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Colorado 3rd', tag='Colorado_3rd')
STD_ANON_19.Colorado_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Colorado 4th', tag='Colorado_4th')
STD_ANON_19.Colorado_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Colorado 5th', tag='Colorado_5th')
STD_ANON_19.Colorado_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Colorado 6th', tag='Colorado_6th')
STD_ANON_19.Colorado_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Colorado 7th', tag='Colorado_7th')
STD_ANON_19.Connecticut_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Connecticut 1st', tag='Connecticut_1st')
STD_ANON_19.Connecticut_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Connecticut 2nd', tag='Connecticut_2nd')
STD_ANON_19.Connecticut_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Connecticut 3rd', tag='Connecticut_3rd')
STD_ANON_19.Connecticut_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Connecticut 4th', tag='Connecticut_4th')
STD_ANON_19.Connecticut_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Connecticut 5th', tag='Connecticut_5th')
STD_ANON_19.Delaware_at_large = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Delaware at large', tag='Delaware_at_large')
STD_ANON_19.District_of_Columbia_at_large = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='District of Columbia at large', tag='District_of_Columbia_at_large')
STD_ANON_19.Florida_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 10th', tag='Florida_10th')
STD_ANON_19.Florida_11th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 11th', tag='Florida_11th')
STD_ANON_19.Florida_12th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 12th', tag='Florida_12th')
STD_ANON_19.Florida_13th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 13th', tag='Florida_13th')
STD_ANON_19.Florida_14th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 14th', tag='Florida_14th')
STD_ANON_19.Florida_15th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 15th', tag='Florida_15th')
STD_ANON_19.Florida_16th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 16th', tag='Florida_16th')
STD_ANON_19.Florida_17th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 17th', tag='Florida_17th')
STD_ANON_19.Florida_18th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 18th', tag='Florida_18th')
STD_ANON_19.Florida_19th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 19th', tag='Florida_19th')
STD_ANON_19.Florida_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 1st', tag='Florida_1st')
STD_ANON_19.Florida_20th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 20th', tag='Florida_20th')
STD_ANON_19.Florida_21st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 21st', tag='Florida_21st')
STD_ANON_19.Florida_22nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 22nd', tag='Florida_22nd')
STD_ANON_19.Florida_23rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 23rd', tag='Florida_23rd')
STD_ANON_19.Florida_24th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 24th', tag='Florida_24th')
STD_ANON_19.Florida_25th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 25th', tag='Florida_25th')
STD_ANON_19.Florida_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 2nd', tag='Florida_2nd')
STD_ANON_19.Florida_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 3rd', tag='Florida_3rd')
STD_ANON_19.Florida_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 4th', tag='Florida_4th')
STD_ANON_19.Florida_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 5th', tag='Florida_5th')
STD_ANON_19.Florida_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 6th', tag='Florida_6th')
STD_ANON_19.Florida_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 7th', tag='Florida_7th')
STD_ANON_19.Florida_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 8th', tag='Florida_8th')
STD_ANON_19.Florida_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Florida 9th', tag='Florida_9th')
STD_ANON_19.Georgia_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 10th', tag='Georgia_10th')
STD_ANON_19.Georgia_11th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 11th', tag='Georgia_11th')
STD_ANON_19.Georgia_12th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 12th', tag='Georgia_12th')
STD_ANON_19.Georgia_13th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 13th', tag='Georgia_13th')
STD_ANON_19.Georgia_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 1st', tag='Georgia_1st')
STD_ANON_19.Georgia_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 2nd', tag='Georgia_2nd')
STD_ANON_19.Georgia_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 3rd', tag='Georgia_3rd')
STD_ANON_19.Georgia_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 4th', tag='Georgia_4th')
STD_ANON_19.Georgia_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 5th', tag='Georgia_5th')
STD_ANON_19.Georgia_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 6th', tag='Georgia_6th')
STD_ANON_19.Georgia_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 7th', tag='Georgia_7th')
STD_ANON_19.Georgia_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 8th', tag='Georgia_8th')
STD_ANON_19.Georgia_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Georgia 9th', tag='Georgia_9th')
STD_ANON_19.Hawaii_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Hawaii 1st', tag='Hawaii_1st')
STD_ANON_19.Hawaii_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Hawaii 2nd', tag='Hawaii_2nd')
STD_ANON_19.Idaho_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Idaho 1st', tag='Idaho_1st')
STD_ANON_19.Idaho_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Idaho 2nd', tag='Idaho_2nd')
STD_ANON_19.Illinois_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 10th', tag='Illinois_10th')
STD_ANON_19.Illinois_11th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 11th', tag='Illinois_11th')
STD_ANON_19.Illinois_12th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 12th', tag='Illinois_12th')
STD_ANON_19.Illinois_13th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 13th', tag='Illinois_13th')
STD_ANON_19.Illinois_14th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 14th', tag='Illinois_14th')
STD_ANON_19.Illinois_15th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 15th', tag='Illinois_15th')
STD_ANON_19.Illinois_16th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 16th', tag='Illinois_16th')
STD_ANON_19.Illinois_17th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 17th', tag='Illinois_17th')
STD_ANON_19.Illinois_18th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 18th', tag='Illinois_18th')
STD_ANON_19.Illinois_19th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 19th', tag='Illinois_19th')
STD_ANON_19.Illinois_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 1st', tag='Illinois_1st')
STD_ANON_19.Illinois_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 2nd', tag='Illinois_2nd')
STD_ANON_19.Illinois_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 3rd', tag='Illinois_3rd')
STD_ANON_19.Illinois_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 4th', tag='Illinois_4th')
STD_ANON_19.Illinois_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 5th', tag='Illinois_5th')
STD_ANON_19.Illinois_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 6th', tag='Illinois_6th')
STD_ANON_19.Illinois_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 7th', tag='Illinois_7th')
STD_ANON_19.Illinois_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 8th', tag='Illinois_8th')
STD_ANON_19.Illinois_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Illinois 9th', tag='Illinois_9th')
STD_ANON_19.Indiana_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Indiana 1st', tag='Indiana_1st')
STD_ANON_19.Indiana_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Indiana 2nd', tag='Indiana_2nd')
STD_ANON_19.Indiana_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Indiana 3rd', tag='Indiana_3rd')
STD_ANON_19.Indiana_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Indiana 4th', tag='Indiana_4th')
STD_ANON_19.Indiana_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Indiana 5th', tag='Indiana_5th')
STD_ANON_19.Indiana_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Indiana 6th', tag='Indiana_6th')
STD_ANON_19.Indiana_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Indiana 7th', tag='Indiana_7th')
STD_ANON_19.Indiana_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Indiana 8th', tag='Indiana_8th')
STD_ANON_19.Indiana_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Indiana 9th', tag='Indiana_9th')
STD_ANON_19.Iowa_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Iowa 1st', tag='Iowa_1st')
STD_ANON_19.Iowa_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Iowa 2nd', tag='Iowa_2nd')
STD_ANON_19.Iowa_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Iowa 3rd', tag='Iowa_3rd')
STD_ANON_19.Iowa_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Iowa 4th', tag='Iowa_4th')
STD_ANON_19.Iowa_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Iowa 5th', tag='Iowa_5th')
STD_ANON_19.Kansas_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Kansas 1st', tag='Kansas_1st')
STD_ANON_19.Kansas_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Kansas 2nd', tag='Kansas_2nd')
STD_ANON_19.Kansas_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Kansas 3rd', tag='Kansas_3rd')
STD_ANON_19.Kansas_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Kansas 4th', tag='Kansas_4th')
STD_ANON_19.Kentucky_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Kentucky 1st', tag='Kentucky_1st')
STD_ANON_19.Kentucky_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Kentucky 2nd', tag='Kentucky_2nd')
STD_ANON_19.Kentucky_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Kentucky 3rd', tag='Kentucky_3rd')
STD_ANON_19.Kentucky_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Kentucky 4th', tag='Kentucky_4th')
STD_ANON_19.Kentucky_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Kentucky 5th', tag='Kentucky_5th')
STD_ANON_19.Kentucky_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Kentucky 6th', tag='Kentucky_6th')
STD_ANON_19.Louisiana_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Louisiana 1st', tag='Louisiana_1st')
STD_ANON_19.Louisiana_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Louisiana 2nd', tag='Louisiana_2nd')
STD_ANON_19.Louisiana_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Louisiana 3rd', tag='Louisiana_3rd')
STD_ANON_19.Louisiana_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Louisiana 4th', tag='Louisiana_4th')
STD_ANON_19.Louisiana_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Louisiana 5th', tag='Louisiana_5th')
STD_ANON_19.Louisiana_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Louisiana 6th', tag='Louisiana_6th')
STD_ANON_19.Louisiana_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Louisiana 7th', tag='Louisiana_7th')
STD_ANON_19.Maine_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Maine 1st', tag='Maine_1st')
STD_ANON_19.Maine_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Maine 2nd', tag='Maine_2nd')
STD_ANON_19.Maryland_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Maryland 1st', tag='Maryland_1st')
STD_ANON_19.Maryland_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Maryland 2nd', tag='Maryland_2nd')
STD_ANON_19.Maryland_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Maryland 3rd', tag='Maryland_3rd')
STD_ANON_19.Maryland_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Maryland 4th', tag='Maryland_4th')
STD_ANON_19.Maryland_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Maryland 5th', tag='Maryland_5th')
STD_ANON_19.Maryland_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Maryland 6th', tag='Maryland_6th')
STD_ANON_19.Maryland_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Maryland 7th', tag='Maryland_7th')
STD_ANON_19.Maryland_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Maryland 8th', tag='Maryland_8th')
STD_ANON_19.Massachusetts_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Massachusetts 10th', tag='Massachusetts_10th')
STD_ANON_19.Massachusetts_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Massachusetts 1st', tag='Massachusetts_1st')
STD_ANON_19.Massachusetts_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Massachusetts 2nd', tag='Massachusetts_2nd')
STD_ANON_19.Massachusetts_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Massachusetts 3rd', tag='Massachusetts_3rd')
STD_ANON_19.Massachusetts_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Massachusetts 4th', tag='Massachusetts_4th')
STD_ANON_19.Massachusetts_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Massachusetts 5th', tag='Massachusetts_5th')
STD_ANON_19.Massachusetts_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Massachusetts 6th', tag='Massachusetts_6th')
STD_ANON_19.Massachusetts_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Massachusetts 7th', tag='Massachusetts_7th')
STD_ANON_19.Massachusetts_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Massachusetts 8th', tag='Massachusetts_8th')
STD_ANON_19.Massachusetts_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Massachusetts 9th', tag='Massachusetts_9th')
STD_ANON_19.Michigan_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 10th', tag='Michigan_10th')
STD_ANON_19.Michigan_11th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 11th', tag='Michigan_11th')
STD_ANON_19.Michigan_12th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 12th', tag='Michigan_12th')
STD_ANON_19.Michigan_13th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 13th', tag='Michigan_13th')
STD_ANON_19.Michigan_14th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 14th', tag='Michigan_14th')
STD_ANON_19.Michigan_15th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 15th', tag='Michigan_15th')
STD_ANON_19.Michigan_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 1st', tag='Michigan_1st')
STD_ANON_19.Michigan_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 2nd', tag='Michigan_2nd')
STD_ANON_19.Michigan_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 3rd', tag='Michigan_3rd')
STD_ANON_19.Michigan_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 4th', tag='Michigan_4th')
STD_ANON_19.Michigan_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 5th', tag='Michigan_5th')
STD_ANON_19.Michigan_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 6th', tag='Michigan_6th')
STD_ANON_19.Michigan_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 7th', tag='Michigan_7th')
STD_ANON_19.Michigan_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 8th', tag='Michigan_8th')
STD_ANON_19.Michigan_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Michigan 9th', tag='Michigan_9th')
STD_ANON_19.Minnesota_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Minnesota 1st', tag='Minnesota_1st')
STD_ANON_19.Minnesota_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Minnesota 2nd', tag='Minnesota_2nd')
STD_ANON_19.Minnesota_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Minnesota 3rd', tag='Minnesota_3rd')
STD_ANON_19.Minnesota_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Minnesota 4th', tag='Minnesota_4th')
STD_ANON_19.Minnesota_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Minnesota 5th', tag='Minnesota_5th')
STD_ANON_19.Minnesota_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Minnesota 6th', tag='Minnesota_6th')
STD_ANON_19.Minnesota_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Minnesota 7th', tag='Minnesota_7th')
STD_ANON_19.Minnesota_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Minnesota 8th', tag='Minnesota_8th')
STD_ANON_19.Mississippi_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Mississippi 1st', tag='Mississippi_1st')
STD_ANON_19.Mississippi_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Mississippi 2nd', tag='Mississippi_2nd')
STD_ANON_19.Mississippi_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Mississippi 3rd', tag='Mississippi_3rd')
STD_ANON_19.Mississippi_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Mississippi 4th', tag='Mississippi_4th')
STD_ANON_19.Missouri_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Missouri 1st', tag='Missouri_1st')
STD_ANON_19.Missouri_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Missouri 2nd', tag='Missouri_2nd')
STD_ANON_19.Missouri_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Missouri 3rd', tag='Missouri_3rd')
STD_ANON_19.Missouri_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Missouri 4th', tag='Missouri_4th')
STD_ANON_19.Missouri_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Missouri 5th', tag='Missouri_5th')
STD_ANON_19.Missouri_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Missouri 6th', tag='Missouri_6th')
STD_ANON_19.Missouri_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Missouri 7th', tag='Missouri_7th')
STD_ANON_19.Missouri_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Missouri 8th', tag='Missouri_8th')
STD_ANON_19.Missouri_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Missouri 9th', tag='Missouri_9th')
STD_ANON_19.Montana_at_large = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Montana at large', tag='Montana_at_large')
STD_ANON_19.Nebraska_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Nebraska 1st', tag='Nebraska_1st')
STD_ANON_19.Nebraska_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Nebraska 2nd', tag='Nebraska_2nd')
STD_ANON_19.Nebraska_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Nebraska 3rd', tag='Nebraska_3rd')
STD_ANON_19.Nevada_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Nevada 1st', tag='Nevada_1st')
STD_ANON_19.Nevada_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Nevada 2nd', tag='Nevada_2nd')
STD_ANON_19.Nevada_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Nevada 3rd', tag='Nevada_3rd')
STD_ANON_19.New_Hampshire_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Hampshire 1st', tag='New_Hampshire_1st')
STD_ANON_19.New_Hampshire_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Hampshire 2nd', tag='New_Hampshire_2nd')
STD_ANON_19.New_Jersey_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 10th', tag='New_Jersey_10th')
STD_ANON_19.New_Jersey_11th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 11th', tag='New_Jersey_11th')
STD_ANON_19.New_Jersey_12th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 12th', tag='New_Jersey_12th')
STD_ANON_19.New_Jersey_13th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 13th', tag='New_Jersey_13th')
STD_ANON_19.New_Jersey_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 1st', tag='New_Jersey_1st')
STD_ANON_19.New_Jersey_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 2nd', tag='New_Jersey_2nd')
STD_ANON_19.New_Jersey_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 3rd', tag='New_Jersey_3rd')
STD_ANON_19.New_Jersey_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 4th', tag='New_Jersey_4th')
STD_ANON_19.New_Jersey_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 5th', tag='New_Jersey_5th')
STD_ANON_19.New_Jersey_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 6th', tag='New_Jersey_6th')
STD_ANON_19.New_Jersey_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 7th', tag='New_Jersey_7th')
STD_ANON_19.New_Jersey_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 8th', tag='New_Jersey_8th')
STD_ANON_19.New_Jersey_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Jersey 9th', tag='New_Jersey_9th')
STD_ANON_19.New_Mexico_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Mexico 1st', tag='New_Mexico_1st')
STD_ANON_19.New_Mexico_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Mexico 2nd', tag='New_Mexico_2nd')
STD_ANON_19.New_Mexico_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New Mexico 3rd', tag='New_Mexico_3rd')
STD_ANON_19.New_York_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 10th', tag='New_York_10th')
STD_ANON_19.New_York_11th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 11th', tag='New_York_11th')
STD_ANON_19.New_York_12th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 12th', tag='New_York_12th')
STD_ANON_19.New_York_13th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 13th', tag='New_York_13th')
STD_ANON_19.New_York_14th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 14th', tag='New_York_14th')
STD_ANON_19.New_York_15th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 15th', tag='New_York_15th')
STD_ANON_19.New_York_16th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 16th', tag='New_York_16th')
STD_ANON_19.New_York_17th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 17th', tag='New_York_17th')
STD_ANON_19.New_York_18th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 18th', tag='New_York_18th')
STD_ANON_19.New_York_19th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 19th', tag='New_York_19th')
STD_ANON_19.New_York_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 1st', tag='New_York_1st')
STD_ANON_19.New_York_20th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 20th', tag='New_York_20th')
STD_ANON_19.New_York_21st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 21st', tag='New_York_21st')
STD_ANON_19.New_York_22nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 22nd', tag='New_York_22nd')
STD_ANON_19.New_York_23rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 23rd', tag='New_York_23rd')
STD_ANON_19.New_York_24th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 24th', tag='New_York_24th')
STD_ANON_19.New_York_25th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 25th', tag='New_York_25th')
STD_ANON_19.New_York_26th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 26th', tag='New_York_26th')
STD_ANON_19.New_York_27th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 27th', tag='New_York_27th')
STD_ANON_19.New_York_28th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 28th', tag='New_York_28th')
STD_ANON_19.New_York_29th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 29th', tag='New_York_29th')
STD_ANON_19.New_York_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 2nd', tag='New_York_2nd')
STD_ANON_19.New_York_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 3rd', tag='New_York_3rd')
STD_ANON_19.New_York_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 4th', tag='New_York_4th')
STD_ANON_19.New_York_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 5th', tag='New_York_5th')
STD_ANON_19.New_York_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 6th', tag='New_York_6th')
STD_ANON_19.New_York_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 7th', tag='New_York_7th')
STD_ANON_19.New_York_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 8th', tag='New_York_8th')
STD_ANON_19.New_York_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='New York 9th', tag='New_York_9th')
STD_ANON_19.North_Carolina_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 10th', tag='North_Carolina_10th')
STD_ANON_19.North_Carolina_11th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 11th', tag='North_Carolina_11th')
STD_ANON_19.North_Carolina_12th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 12th', tag='North_Carolina_12th')
STD_ANON_19.North_Carolina_13th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 13th', tag='North_Carolina_13th')
STD_ANON_19.North_Carolina_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 1st', tag='North_Carolina_1st')
STD_ANON_19.North_Carolina_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 2nd', tag='North_Carolina_2nd')
STD_ANON_19.North_Carolina_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 3rd', tag='North_Carolina_3rd')
STD_ANON_19.North_Carolina_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 4th', tag='North_Carolina_4th')
STD_ANON_19.North_Carolina_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 5th', tag='North_Carolina_5th')
STD_ANON_19.North_Carolina_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 6th', tag='North_Carolina_6th')
STD_ANON_19.North_Carolina_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 7th', tag='North_Carolina_7th')
STD_ANON_19.North_Carolina_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 8th', tag='North_Carolina_8th')
STD_ANON_19.North_Carolina_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Carolina 9th', tag='North_Carolina_9th')
STD_ANON_19.North_Dakota_at_large = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='North Dakota at large', tag='North_Dakota_at_large')
STD_ANON_19.Ohio_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 10th', tag='Ohio_10th')
STD_ANON_19.Ohio_11th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 11th', tag='Ohio_11th')
STD_ANON_19.Ohio_12th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 12th', tag='Ohio_12th')
STD_ANON_19.Ohio_13th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 13th', tag='Ohio_13th')
STD_ANON_19.Ohio_14th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 14th', tag='Ohio_14th')
STD_ANON_19.Ohio_15th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 15th', tag='Ohio_15th')
STD_ANON_19.Ohio_16th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 16th', tag='Ohio_16th')
STD_ANON_19.Ohio_17th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 17th', tag='Ohio_17th')
STD_ANON_19.Ohio_18th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 18th', tag='Ohio_18th')
STD_ANON_19.Ohio_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 1st', tag='Ohio_1st')
STD_ANON_19.Ohio_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 2nd', tag='Ohio_2nd')
STD_ANON_19.Ohio_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 3rd', tag='Ohio_3rd')
STD_ANON_19.Ohio_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 4th', tag='Ohio_4th')
STD_ANON_19.Ohio_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 5th', tag='Ohio_5th')
STD_ANON_19.Ohio_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 6th', tag='Ohio_6th')
STD_ANON_19.Ohio_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 7th', tag='Ohio_7th')
STD_ANON_19.Ohio_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 8th', tag='Ohio_8th')
STD_ANON_19.Ohio_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Ohio 9th', tag='Ohio_9th')
STD_ANON_19.Oklahoma_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Oklahoma 1st', tag='Oklahoma_1st')
STD_ANON_19.Oklahoma_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Oklahoma 2nd', tag='Oklahoma_2nd')
STD_ANON_19.Oklahoma_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Oklahoma 3rd', tag='Oklahoma_3rd')
STD_ANON_19.Oklahoma_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Oklahoma 4th', tag='Oklahoma_4th')
STD_ANON_19.Oklahoma_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Oklahoma 5th', tag='Oklahoma_5th')
STD_ANON_19.Oregon_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Oregon 1st', tag='Oregon_1st')
STD_ANON_19.Oregon_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Oregon 2nd', tag='Oregon_2nd')
STD_ANON_19.Oregon_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Oregon 3rd', tag='Oregon_3rd')
STD_ANON_19.Oregon_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Oregon 4th', tag='Oregon_4th')
STD_ANON_19.Oregon_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Oregon 5th', tag='Oregon_5th')
STD_ANON_19.Pennsylvania_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 10th', tag='Pennsylvania_10th')
STD_ANON_19.Pennsylvania_11th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 11th', tag='Pennsylvania_11th')
STD_ANON_19.Pennsylvania_12th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 12th', tag='Pennsylvania_12th')
STD_ANON_19.Pennsylvania_13th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 13th', tag='Pennsylvania_13th')
STD_ANON_19.Pennsylvania_14th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 14th', tag='Pennsylvania_14th')
STD_ANON_19.Pennsylvania_15th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 15th', tag='Pennsylvania_15th')
STD_ANON_19.Pennsylvania_16th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 16th', tag='Pennsylvania_16th')
STD_ANON_19.Pennsylvania_17th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 17th', tag='Pennsylvania_17th')
STD_ANON_19.Pennsylvania_18th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 18th', tag='Pennsylvania_18th')
STD_ANON_19.Pennsylvania_19th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 19th', tag='Pennsylvania_19th')
STD_ANON_19.Pennsylvania_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 1st', tag='Pennsylvania_1st')
STD_ANON_19.Pennsylvania_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 2nd', tag='Pennsylvania_2nd')
STD_ANON_19.Pennsylvania_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 3rd', tag='Pennsylvania_3rd')
STD_ANON_19.Pennsylvania_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 4th', tag='Pennsylvania_4th')
STD_ANON_19.Pennsylvania_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 5th', tag='Pennsylvania_5th')
STD_ANON_19.Pennsylvania_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 6th', tag='Pennsylvania_6th')
STD_ANON_19.Pennsylvania_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 7th', tag='Pennsylvania_7th')
STD_ANON_19.Pennsylvania_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 8th', tag='Pennsylvania_8th')
STD_ANON_19.Pennsylvania_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Pennsylvania 9th', tag='Pennsylvania_9th')
STD_ANON_19.Rhode_Island_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Rhode Island 1st', tag='Rhode_Island_1st')
STD_ANON_19.Rhode_Island_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Rhode Island 2nd', tag='Rhode_Island_2nd')
STD_ANON_19.South_Carolina_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='South Carolina 1st', tag='South_Carolina_1st')
STD_ANON_19.South_Carolina_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='South Carolina 2nd', tag='South_Carolina_2nd')
STD_ANON_19.South_Carolina_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='South Carolina 3rd', tag='South_Carolina_3rd')
STD_ANON_19.South_Carolina_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='South Carolina 4th', tag='South_Carolina_4th')
STD_ANON_19.South_Carolina_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='South Carolina 5th', tag='South_Carolina_5th')
STD_ANON_19.South_Carolina_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='South Carolina 6th', tag='South_Carolina_6th')
STD_ANON_19.South_Dakota_at_large = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='South Dakota at large', tag='South_Dakota_at_large')
STD_ANON_19.Tennessee_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Tennessee 1st', tag='Tennessee_1st')
STD_ANON_19.Tennessee_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Tennessee 2nd', tag='Tennessee_2nd')
STD_ANON_19.Tennessee_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Tennessee 3rd', tag='Tennessee_3rd')
STD_ANON_19.Tennessee_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Tennessee 4th', tag='Tennessee_4th')
STD_ANON_19.Tennessee_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Tennessee 5th', tag='Tennessee_5th')
STD_ANON_19.Tennessee_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Tennessee 6th', tag='Tennessee_6th')
STD_ANON_19.Tennessee_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Tennessee 7th', tag='Tennessee_7th')
STD_ANON_19.Tennessee_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Tennessee 8th', tag='Tennessee_8th')
STD_ANON_19.Tennessee_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Tennessee 9th', tag='Tennessee_9th')
STD_ANON_19.Texas_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 10th', tag='Texas_10th')
STD_ANON_19.Texas_11th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 11th', tag='Texas_11th')
STD_ANON_19.Texas_12th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 12th', tag='Texas_12th')
STD_ANON_19.Texas_13th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 13th', tag='Texas_13th')
STD_ANON_19.Texas_14th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 14th', tag='Texas_14th')
STD_ANON_19.Texas_15th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 15th', tag='Texas_15th')
STD_ANON_19.Texas_16th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 16th', tag='Texas_16th')
STD_ANON_19.Texas_17th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 17th', tag='Texas_17th')
STD_ANON_19.Texas_18th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 18th', tag='Texas_18th')
STD_ANON_19.Texas_19th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 19th', tag='Texas_19th')
STD_ANON_19.Texas_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 1st', tag='Texas_1st')
STD_ANON_19.Texas_20th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 20th', tag='Texas_20th')
STD_ANON_19.Texas_21st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 21st', tag='Texas_21st')
STD_ANON_19.Texas_22nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 22nd', tag='Texas_22nd')
STD_ANON_19.Texas_23rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 23rd', tag='Texas_23rd')
STD_ANON_19.Texas_24th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 24th', tag='Texas_24th')
STD_ANON_19.Texas_25th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 25th', tag='Texas_25th')
STD_ANON_19.Texas_26th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 26th', tag='Texas_26th')
STD_ANON_19.Texas_27th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 27th', tag='Texas_27th')
STD_ANON_19.Texas_28th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 28th', tag='Texas_28th')
STD_ANON_19.Texas_29th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 29th', tag='Texas_29th')
STD_ANON_19.Texas_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 2nd', tag='Texas_2nd')
STD_ANON_19.Texas_30th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 30th', tag='Texas_30th')
STD_ANON_19.Texas_31st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 31st', tag='Texas_31st')
STD_ANON_19.Texas_32nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 32nd', tag='Texas_32nd')
STD_ANON_19.Texas_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 3rd', tag='Texas_3rd')
STD_ANON_19.Texas_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 4th', tag='Texas_4th')
STD_ANON_19.Texas_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 5th', tag='Texas_5th')
STD_ANON_19.Texas_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 6th', tag='Texas_6th')
STD_ANON_19.Texas_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 7th', tag='Texas_7th')
STD_ANON_19.Texas_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 8th', tag='Texas_8th')
STD_ANON_19.Texas_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Texas 9th', tag='Texas_9th')
STD_ANON_19.Utah_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Utah 1st', tag='Utah_1st')
STD_ANON_19.Utah_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Utah 2nd', tag='Utah_2nd')
STD_ANON_19.Utah_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Utah 3rd', tag='Utah_3rd')
STD_ANON_19.Vermont_at_large = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Vermont at large', tag='Vermont_at_large')
STD_ANON_19.Virginia_10th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Virginia 10th', tag='Virginia_10th')
STD_ANON_19.Virginia_11th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Virginia 11th', tag='Virginia_11th')
STD_ANON_19.Virginia_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Virginia 1st', tag='Virginia_1st')
STD_ANON_19.Virginia_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Virginia 2nd', tag='Virginia_2nd')
STD_ANON_19.Virginia_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Virginia 3rd', tag='Virginia_3rd')
STD_ANON_19.Virginia_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Virginia 4th', tag='Virginia_4th')
STD_ANON_19.Virginia_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Virginia 5th', tag='Virginia_5th')
STD_ANON_19.Virginia_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Virginia 6th', tag='Virginia_6th')
STD_ANON_19.Virginia_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Virginia 7th', tag='Virginia_7th')
STD_ANON_19.Virginia_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Virginia 8th', tag='Virginia_8th')
STD_ANON_19.Virginia_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Virginia 9th', tag='Virginia_9th')
STD_ANON_19.Washington_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Washington 1st', tag='Washington_1st')
STD_ANON_19.Washington_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Washington 2nd', tag='Washington_2nd')
STD_ANON_19.Washington_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Washington 3rd', tag='Washington_3rd')
STD_ANON_19.Washington_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Washington 4th', tag='Washington_4th')
STD_ANON_19.Washington_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Washington 5th', tag='Washington_5th')
STD_ANON_19.Washington_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Washington 6th', tag='Washington_6th')
STD_ANON_19.Washington_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Washington 7th', tag='Washington_7th')
STD_ANON_19.Washington_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Washington 8th', tag='Washington_8th')
STD_ANON_19.Washington_9th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Washington 9th', tag='Washington_9th')
STD_ANON_19.West_Virginia_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='West Virginia 1st', tag='West_Virginia_1st')
STD_ANON_19.West_Virginia_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='West Virginia 2nd', tag='West_Virginia_2nd')
STD_ANON_19.West_Virginia_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='West Virginia 3rd', tag='West_Virginia_3rd')
STD_ANON_19.Wisconsin_1st = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Wisconsin 1st', tag='Wisconsin_1st')
STD_ANON_19.Wisconsin_2nd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Wisconsin 2nd', tag='Wisconsin_2nd')
STD_ANON_19.Wisconsin_3rd = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Wisconsin 3rd', tag='Wisconsin_3rd')
STD_ANON_19.Wisconsin_4th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Wisconsin 4th', tag='Wisconsin_4th')
STD_ANON_19.Wisconsin_5th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Wisconsin 5th', tag='Wisconsin_5th')
STD_ANON_19.Wisconsin_6th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Wisconsin 6th', tag='Wisconsin_6th')
STD_ANON_19.Wisconsin_7th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Wisconsin 7th', tag='Wisconsin_7th')
STD_ANON_19.Wisconsin_8th = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Wisconsin 8th', tag='Wisconsin_8th')
STD_ANON_19.Wyoming_at_large = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Wyoming at large', tag='Wyoming_at_large')
STD_ANON_19.undefined = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='undefined', tag='undefined')
STD_ANON_19._InitializeFacetMap(STD_ANON_19._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_20 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 782, 1)
    _Documentation = None
STD_ANON_20._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_20, enum_prefix=None)
STD_ANON_20.AL = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='AL', tag='AL')
STD_ANON_20.AK = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='AK', tag='AK')
STD_ANON_20.AZ = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='AZ', tag='AZ')
STD_ANON_20.AR = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='AR', tag='AR')
STD_ANON_20.CA = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='CA', tag='CA')
STD_ANON_20.CO = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='CO', tag='CO')
STD_ANON_20.CT = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='CT', tag='CT')
STD_ANON_20.DE = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='DE', tag='DE')
STD_ANON_20.FL = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='FL', tag='FL')
STD_ANON_20.GA = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='GA', tag='GA')
STD_ANON_20.HI = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='HI', tag='HI')
STD_ANON_20.ID = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='ID', tag='ID')
STD_ANON_20.IL = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='IL', tag='IL')
STD_ANON_20.IN = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='IN', tag='IN')
STD_ANON_20.IA = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='IA', tag='IA')
STD_ANON_20.KS = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='KS', tag='KS')
STD_ANON_20.KY = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='KY', tag='KY')
STD_ANON_20.LA = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='LA', tag='LA')
STD_ANON_20.ME = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='ME', tag='ME')
STD_ANON_20.MD = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='MD', tag='MD')
STD_ANON_20.MA = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='MA', tag='MA')
STD_ANON_20.MI = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='MI', tag='MI')
STD_ANON_20.MN = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='MN', tag='MN')
STD_ANON_20.MS = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='MS', tag='MS')
STD_ANON_20.MO = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='MO', tag='MO')
STD_ANON_20.MT = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='MT', tag='MT')
STD_ANON_20.NE = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='NE', tag='NE')
STD_ANON_20.NV = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='NV', tag='NV')
STD_ANON_20.NH = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='NH', tag='NH')
STD_ANON_20.NJ = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='NJ', tag='NJ')
STD_ANON_20.NM = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='NM', tag='NM')
STD_ANON_20.NY = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='NY', tag='NY')
STD_ANON_20.NC = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='NC', tag='NC')
STD_ANON_20.ND = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='ND', tag='ND')
STD_ANON_20.OH = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='OH', tag='OH')
STD_ANON_20.OK = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='OK', tag='OK')
STD_ANON_20.OR = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='OR', tag='OR')
STD_ANON_20.PA = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='PA', tag='PA')
STD_ANON_20.RI = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='RI', tag='RI')
STD_ANON_20.SC = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='SC', tag='SC')
STD_ANON_20.SD = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='SD', tag='SD')
STD_ANON_20.TN = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='TN', tag='TN')
STD_ANON_20.TX = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='TX', tag='TX')
STD_ANON_20.UT = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='UT', tag='UT')
STD_ANON_20.VT = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='VT', tag='VT')
STD_ANON_20.VA = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='VA', tag='VA')
STD_ANON_20.WA = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='WA', tag='WA')
STD_ANON_20.WV = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='WV', tag='WV')
STD_ANON_20.WI = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='WI', tag='WI')
STD_ANON_20.WY = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='WY', tag='WY')
STD_ANON_20.AS = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='AS', tag='AS')
STD_ANON_20.DC = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='DC', tag='DC')
STD_ANON_20.FM = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='FM', tag='FM')
STD_ANON_20.GU = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='GU', tag='GU')
STD_ANON_20.MH = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='MH', tag='MH')
STD_ANON_20.MP = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='MP', tag='MP')
STD_ANON_20.PW = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='PW', tag='PW')
STD_ANON_20.PR = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='PR', tag='PR')
STD_ANON_20.VI = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='VI', tag='VI')
STD_ANON_20.AE = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='AE', tag='AE')
STD_ANON_20.AA = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='AA', tag='AA')
STD_ANON_20.AP = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='AP', tag='AP')
STD_ANON_20.undefined = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='undefined', tag='undefined')
STD_ANON_20._InitializeFacetMap(STD_ANON_20._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_21 (_ImportedBinding_xbrli.monetary):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 334, 1)
    _Documentation = None
STD_ANON_21._InitializeFacetMap()

# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}TreasuryAccountSymbolComplexType with content type ELEMENT_ONLY
class TreasuryAccountSymbolComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}TreasuryAccountSymbolComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TreasuryAccountSymbolComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 261, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}allocationTransferAgencyIdentifier uses Python identifier allocationTransferAgencyIdentifier
    __allocationTransferAgencyIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'allocationTransferAgencyIdentifier'), 'allocationTransferAgencyIdentifier', '__httpwww_xbrl_orgintglgen2006_10_25_TreasuryAccountSymbolComplexType_httpwww_xbrl_orgintglgen2006_10_25allocationTransferAgencyIdentifier', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 867, 1), )

    
    allocationTransferAgencyIdentifier = property(__allocationTransferAgencyIdentifier.value, __allocationTransferAgencyIdentifier.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}mainAccountNumber uses Python identifier mainAccountNumber
    __mainAccountNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mainAccountNumber'), 'mainAccountNumber', '__httpwww_xbrl_orgintglgen2006_10_25_TreasuryAccountSymbolComplexType_httpwww_xbrl_orgintglgen2006_10_25mainAccountNumber', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 868, 1), )

    
    mainAccountNumber = property(__mainAccountNumber.value, __mainAccountNumber.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}subAccountSymbol uses Python identifier subAccountSymbol
    __subAccountSymbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subAccountSymbol'), 'subAccountSymbol', '__httpwww_xbrl_orgintglgen2006_10_25_TreasuryAccountSymbolComplexType_httpwww_xbrl_orgintglgen2006_10_25subAccountSymbol', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 869, 1), )

    
    subAccountSymbol = property(__subAccountSymbol.value, __subAccountSymbol.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}beginningPeriodOfAvailability uses Python identifier beginningPeriodOfAvailability
    __beginningPeriodOfAvailability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beginningPeriodOfAvailability'), 'beginningPeriodOfAvailability', '__httpwww_xbrl_orgintglgen2006_10_25_TreasuryAccountSymbolComplexType_httpwww_xbrl_orgintglgen2006_10_25beginningPeriodOfAvailability', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 870, 1), )

    
    beginningPeriodOfAvailability = property(__beginningPeriodOfAvailability.value, __beginningPeriodOfAvailability.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}endingPeriodOfAvailability uses Python identifier endingPeriodOfAvailability
    __endingPeriodOfAvailability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endingPeriodOfAvailability'), 'endingPeriodOfAvailability', '__httpwww_xbrl_orgintglgen2006_10_25_TreasuryAccountSymbolComplexType_httpwww_xbrl_orgintglgen2006_10_25endingPeriodOfAvailability', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 871, 1), )

    
    endingPeriodOfAvailability = property(__endingPeriodOfAvailability.value, __endingPeriodOfAvailability.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}availabilityTypeCode uses Python identifier availabilityTypeCode
    __availabilityTypeCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'availabilityTypeCode'), 'availabilityTypeCode', '__httpwww_xbrl_orgintglgen2006_10_25_TreasuryAccountSymbolComplexType_httpwww_xbrl_orgintglgen2006_10_25availabilityTypeCode', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 872, 1), )

    
    availabilityTypeCode = property(__availabilityTypeCode.value, __availabilityTypeCode.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}agency uses Python identifier agency
    __agency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agency'), 'agency', '__httpwww_xbrl_orgintglgen2006_10_25_TreasuryAccountSymbolComplexType_httpwww_xbrl_orgintglgen2006_10_25agency', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 890, 1), )

    
    agency = property(__agency.value, __agency.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintglgen2006_10_25_TreasuryAccountSymbolComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 276, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 276, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __allocationTransferAgencyIdentifier.name() : __allocationTransferAgencyIdentifier,
        __mainAccountNumber.name() : __mainAccountNumber,
        __subAccountSymbol.name() : __subAccountSymbol,
        __beginningPeriodOfAvailability.name() : __beginningPeriodOfAvailability,
        __endingPeriodOfAvailability.name() : __endingPeriodOfAvailability,
        __availabilityTypeCode.name() : __availabilityTypeCode,
        __agency.name() : __agency
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'TreasuryAccountSymbolComplexType', TreasuryAccountSymbolComplexType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}addressComplexType with content type ELEMENT_ONLY
class addressComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}addressComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'addressComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 280, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}streetAddress uses Python identifier streetAddress
    __streetAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddress'), 'streetAddress', '__httpwww_xbrl_orgintglgen2006_10_25_addressComplexType_httpwww_xbrl_orgintglgen2006_10_25streetAddress', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 877, 1), )

    
    streetAddress = property(__streetAddress.value, __streetAddress.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httpwww_xbrl_orgintglgen2006_10_25_addressComplexType_httpwww_xbrl_orgintglgen2006_10_25city', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 880, 1), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}county uses Python identifier county
    __county = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'county'), 'county', '__httpwww_xbrl_orgintglgen2006_10_25_addressComplexType_httpwww_xbrl_orgintglgen2006_10_25county', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 881, 1), )

    
    county = property(__county.value, __county.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'state'), 'state', '__httpwww_xbrl_orgintglgen2006_10_25_addressComplexType_httpwww_xbrl_orgintglgen2006_10_25state', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 882, 1), )

    
    state = property(__state.value, __state.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}zipCodePlus4 uses Python identifier zipCodePlus4
    __zipCodePlus4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'zipCodePlus4'), 'zipCodePlus4', '__httpwww_xbrl_orgintglgen2006_10_25_addressComplexType_httpwww_xbrl_orgintglgen2006_10_25zipCodePlus4', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 883, 1), )

    
    zipCodePlus4 = property(__zipCodePlus4.value, __zipCodePlus4.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), 'postalCode', '__httpwww_xbrl_orgintglgen2006_10_25_addressComplexType_httpwww_xbrl_orgintglgen2006_10_25postalCode', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 884, 1), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}countryName uses Python identifier countryName
    __countryName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countryName'), 'countryName', '__httpwww_xbrl_orgintglgen2006_10_25_addressComplexType_httpwww_xbrl_orgintglgen2006_10_25countryName', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 885, 1), )

    
    countryName = property(__countryName.value, __countryName.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), 'countryCode', '__httpwww_xbrl_orgintglgen2006_10_25_addressComplexType_httpwww_xbrl_orgintglgen2006_10_25countryCode', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 886, 1), )

    
    countryCode = property(__countryCode.value, __countryCode.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}congressionalDistrict uses Python identifier congressionalDistrict
    __congressionalDistrict = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'congressionalDistrict'), 'congressionalDistrict', '__httpwww_xbrl_orgintglgen2006_10_25_addressComplexType_httpwww_xbrl_orgintglgen2006_10_25congressionalDistrict', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 887, 1), )

    
    congressionalDistrict = property(__congressionalDistrict.value, __congressionalDistrict.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintglgen2006_10_25_addressComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 297, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 297, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __streetAddress.name() : __streetAddress,
        __city.name() : __city,
        __county.name() : __county,
        __state.name() : __state,
        __zipCodePlus4.name() : __zipCodePlus4,
        __postalCode.name() : __postalCode,
        __countryName.name() : __countryName,
        __countryCode.name() : __countryCode,
        __congressionalDistrict.name() : __congressionalDistrict
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'addressComplexType', addressComplexType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}streetAddressComplexType with content type ELEMENT_ONLY
class streetAddressComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}streetAddressComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'streetAddressComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 301, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}streetAddressLine uses Python identifier streetAddressLine
    __streetAddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddressLine'), 'streetAddressLine', '__httpwww_xbrl_orgintglgen2006_10_25_streetAddressComplexType_httpwww_xbrl_orgintglgen2006_10_25streetAddressLine', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 878, 1), )

    
    streetAddressLine = property(__streetAddressLine.value, __streetAddressLine.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintglgen2006_10_25_streetAddressComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 307, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 307, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __streetAddressLine.name() : __streetAddressLine
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'streetAddressComplexType', streetAddressComplexType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}agencyComplexType with content type ELEMENT_ONLY
class agencyComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}agencyComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'agencyComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 311, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}agencyIdentifier uses Python identifier agencyIdentifier
    __agencyIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agencyIdentifier'), 'agencyIdentifier', '__httpwww_xbrl_orgintglgen2006_10_25_agencyComplexType_httpwww_xbrl_orgintglgen2006_10_25agencyIdentifier', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 891, 1), )

    
    agencyIdentifier = property(__agencyIdentifier.value, __agencyIdentifier.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}agencyName uses Python identifier agencyName
    __agencyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agencyName'), 'agencyName', '__httpwww_xbrl_orgintglgen2006_10_25_agencyComplexType_httpwww_xbrl_orgintglgen2006_10_25agencyName', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 892, 1), )

    
    agencyName = property(__agencyName.value, __agencyName.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}agencyOffice uses Python identifier agencyOffice
    __agencyOffice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agencyOffice'), 'agencyOffice', '__httpwww_xbrl_orgintglgen2006_10_25_agencyComplexType_httpwww_xbrl_orgintglgen2006_10_25agencyOffice', True, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 895, 1), )

    
    agencyOffice = property(__agencyOffice.value, __agencyOffice.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintglgen2006_10_25_agencyComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 319, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 319, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __agencyIdentifier.name() : __agencyIdentifier,
        __agencyName.name() : __agencyName,
        __agencyOffice.name() : __agencyOffice
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'agencyComplexType', agencyComplexType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}agencyOfficeComplexType with content type ELEMENT_ONLY
class agencyOfficeComplexType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}agencyOfficeComplexType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'agencyOfficeComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 323, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}officeIdentifier uses Python identifier officeIdentifier
    __officeIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'officeIdentifier'), 'officeIdentifier', '__httpwww_xbrl_orgintglgen2006_10_25_agencyOfficeComplexType_httpwww_xbrl_orgintglgen2006_10_25officeIdentifier', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 896, 1), )

    
    officeIdentifier = property(__officeIdentifier.value, __officeIdentifier.set, None, None)

    
    # Element {http://www.xbrl.org/int/gl/gen/2006-10-25}officeName uses Python identifier officeName
    __officeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'officeName'), 'officeName', '__httpwww_xbrl_orgintglgen2006_10_25_agencyOfficeComplexType_httpwww_xbrl_orgintglgen2006_10_25officeName', False, pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 897, 1), )

    
    officeName = property(__officeName.value, __officeName.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xbrl_orgintglgen2006_10_25_agencyOfficeComplexType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 330, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 330, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __officeIdentifier.name() : __officeIdentifier,
        __officeName.name() : __officeName
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'agencyOfficeComplexType', agencyOfficeComplexType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}accountPurposeCodeItemType with content type SIMPLE
class accountPurposeCodeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}accountPurposeCodeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'accountPurposeCodeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 6, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'accountPurposeCodeItemType', accountPurposeCodeItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}accountTypeItemType with content type SIMPLE
class accountTypeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}accountTypeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'accountTypeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 21, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'accountTypeItemType', accountTypeItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}bookTaxDifferenceItemType with content type SIMPLE
class bookTaxDifferenceItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}bookTaxDifferenceItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_2
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'bookTaxDifferenceItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 36, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'bookTaxDifferenceItemType', bookTaxDifferenceItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}identifierOrganizationTypeItemType with content type SIMPLE
class identifierOrganizationTypeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}identifierOrganizationTypeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_3
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'identifierOrganizationTypeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 45, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'identifierOrganizationTypeItemType', identifierOrganizationTypeItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}debitCreditCodeItemType with content type SIMPLE
class debitCreditCodeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}debitCreditCodeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_4
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'debitCreditCodeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 54, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'debitCreditCodeItemType', debitCreditCodeItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}documentTypeItemType with content type SIMPLE
class documentTypeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}documentTypeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_5
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'documentTypeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 65, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'documentTypeItemType', documentTypeItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}invoiceTypeItemType with content type SIMPLE
class invoiceTypeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}invoiceTypeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_6
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'invoiceTypeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 86, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'invoiceTypeItemType', invoiceTypeItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}entriesTypeItemType with content type SIMPLE
class entriesTypeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}entriesTypeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_7
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entriesTypeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 94, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'entriesTypeItemType', entriesTypeItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}entryTypeItemType with content type SIMPLE
class entryTypeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}entryTypeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_8
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entryTypeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 109, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'entryTypeItemType', entryTypeItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}identifierTypeItemType with content type SIMPLE
class identifierTypeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}identifierTypeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_9
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'identifierTypeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 128, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'identifierTypeItemType', identifierTypeItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}mainAccountTypeItemType with content type SIMPLE
class mainAccountTypeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}mainAccountTypeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_10
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mainAccountTypeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 148, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mainAccountTypeItemType', mainAccountTypeItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}postingStatusItemType with content type SIMPLE
class postingStatusItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}postingStatusItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_11
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'postingStatusItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 165, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'postingStatusItemType', postingStatusItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}qualifierEntryItemType with content type SIMPLE
class qualifierEntryItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}qualifierEntryItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_12
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'qualifierEntryItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 179, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'qualifierEntryItemType', qualifierEntryItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}revisesUniqueIDActionItemType with content type SIMPLE
class revisesUniqueIDActionItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}revisesUniqueIDActionItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_13
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'revisesUniqueIDActionItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 188, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'revisesUniqueIDActionItemType', revisesUniqueIDActionItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}signOfAmountItemType with content type SIMPLE
class signOfAmountItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}signOfAmountItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_14
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'signOfAmountItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 196, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'signOfAmountItemType', signOfAmountItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}sourceJournalIDItemType with content type SIMPLE
class sourceJournalIDItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}sourceJournalIDItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_15
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sourceJournalIDItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 206, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'sourceJournalIDItemType', sourceJournalIDItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}xbrlIncludeItemType with content type SIMPLE
class xbrlIncludeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}xbrlIncludeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_16
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'xbrlIncludeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 225, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'xbrlIncludeItemType', xbrlIncludeItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}phoneNumberDescriptionItemType with content type SIMPLE
class phoneNumberDescriptionItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}phoneNumberDescriptionItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_17
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phoneNumberDescriptionItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 234, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'phoneNumberDescriptionItemType', phoneNumberDescriptionItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}availableTypeCodeItemType with content type SIMPLE
class availableTypeCodeItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}availableTypeCodeItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_18
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'availableTypeCodeItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 250, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'availableTypeCodeItemType', availableTypeCodeItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}congressionalDistrictItemType with content type SIMPLE
class congressionalDistrictItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}congressionalDistrictItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_19
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'congressionalDistrictItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 339, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'congressionalDistrictItemType', congressionalDistrictItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}stateItemType with content type SIMPLE
class stateItemType (_ImportedBinding_xbrli.tokenItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}stateItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_20
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stateItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 782, 1)
    _ElementMap = _ImportedBinding_xbrli.tokenItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.tokenItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.tokenItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}tokenItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'stateItemType', stateItemType)


# Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}amountItemType with content type SIMPLE
class amountItemType (_ImportedBinding_xbrli.monetaryItemType):
    """Complex type {http://www.xbrl.org/int/gl/gen/2006-10-25}amountItemType with content type SIMPLE"""
    _TypeDefinition = STD_ANON_21
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'amountItemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 334, 1)
    _ElementMap = _ImportedBinding_xbrli.monetaryItemType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_xbrli.monetaryItemType._AttributeMap.copy()
    # Base type is _ImportedBinding_xbrli.monetaryItemType
    
    # Attribute id inherited from {http://www.xbrl.org/2003/instance}monetaryItemType
    
    # Attribute contextRef inherited from {http://www.xbrl.org/2003/instance}monetaryItemType
    
    # Attribute unitRef inherited from {http://www.xbrl.org/2003/instance}monetaryItemType
    
    # Attribute precision inherited from {http://www.xbrl.org/2003/instance}monetaryItemType
    
    # Attribute decimals inherited from {http://www.xbrl.org/2003/instance}monetaryItemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'amountItemType', amountItemType)


treasuryAccountSymbol = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'treasuryAccountSymbol'), TreasuryAccountSymbolComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 865, 1))
Namespace.addCategoryObject('elementBinding', treasuryAccountSymbol.name().localName(), treasuryAccountSymbol)

beginningPeriodOfAvailability = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beginningPeriodOfAvailability'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 870, 1))
Namespace.addCategoryObject('elementBinding', beginningPeriodOfAvailability.name().localName(), beginningPeriodOfAvailability)

endingPeriodOfAvailability = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endingPeriodOfAvailability'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 871, 1))
Namespace.addCategoryObject('elementBinding', endingPeriodOfAvailability.name().localName(), endingPeriodOfAvailability)

address = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'address'), addressComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 875, 1))
Namespace.addCategoryObject('elementBinding', address.name().localName(), address)

streetAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress'), streetAddressComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 877, 1))
Namespace.addCategoryObject('elementBinding', streetAddress.name().localName(), streetAddress)

streetAddressLine = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddressLine'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 878, 1))
Namespace.addCategoryObject('elementBinding', streetAddressLine.name().localName(), streetAddressLine)

city = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 880, 1))
Namespace.addCategoryObject('elementBinding', city.name().localName(), city)

county = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'county'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 881, 1))
Namespace.addCategoryObject('elementBinding', county.name().localName(), county)

zipCodePlus4 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'zipCodePlus4'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 883, 1))
Namespace.addCategoryObject('elementBinding', zipCodePlus4.name().localName(), zipCodePlus4)

postalCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 884, 1))
Namespace.addCategoryObject('elementBinding', postalCode.name().localName(), postalCode)

countryName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 885, 1))
Namespace.addCategoryObject('elementBinding', countryName.name().localName(), countryName)

countryCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 886, 1))
Namespace.addCategoryObject('elementBinding', countryCode.name().localName(), countryCode)

agency = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agency'), agencyComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 890, 1))
Namespace.addCategoryObject('elementBinding', agency.name().localName(), agency)

agencyName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agencyName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 892, 1))
Namespace.addCategoryObject('elementBinding', agencyName.name().localName(), agencyName)

agencyOffice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agencyOffice'), agencyOfficeComplexType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 895, 1))
Namespace.addCategoryObject('elementBinding', agencyOffice.name().localName(), agencyOffice)

officeName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'officeName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 897, 1))
Namespace.addCategoryObject('elementBinding', officeName.name().localName(), officeName)

awardID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardID'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 899, 1))
Namespace.addCategoryObject('elementBinding', awardID.name().localName(), awardID)

availabilityTypeCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'availabilityTypeCode'), availableTypeCodeItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 872, 1))
Namespace.addCategoryObject('elementBinding', availabilityTypeCode.name().localName(), availabilityTypeCode)

state = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'state'), stateItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 882, 1))
Namespace.addCategoryObject('elementBinding', state.name().localName(), state)

congressionalDistrict = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'congressionalDistrict'), congressionalDistrictItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 887, 1))
Namespace.addCategoryObject('elementBinding', congressionalDistrict.name().localName(), congressionalDistrict)

allocationTransferAgencyIdentifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'allocationTransferAgencyIdentifier'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 867, 1))
Namespace.addCategoryObject('elementBinding', allocationTransferAgencyIdentifier.name().localName(), allocationTransferAgencyIdentifier)

mainAccountNumber = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mainAccountNumber'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 868, 1))
Namespace.addCategoryObject('elementBinding', mainAccountNumber.name().localName(), mainAccountNumber)

subAccountSymbol = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subAccountSymbol'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 869, 1))
Namespace.addCategoryObject('elementBinding', subAccountSymbol.name().localName(), subAccountSymbol)

agencyIdentifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agencyIdentifier'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 891, 1))
Namespace.addCategoryObject('elementBinding', agencyIdentifier.name().localName(), agencyIdentifier)

officeIdentifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'officeIdentifier'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 896, 1))
Namespace.addCategoryObject('elementBinding', officeIdentifier.name().localName(), officeIdentifier)



TreasuryAccountSymbolComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'allocationTransferAgencyIdentifier'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=TreasuryAccountSymbolComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 867, 1)))

TreasuryAccountSymbolComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mainAccountNumber'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=TreasuryAccountSymbolComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 868, 1)))

TreasuryAccountSymbolComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subAccountSymbol'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=TreasuryAccountSymbolComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 869, 1)))

TreasuryAccountSymbolComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beginningPeriodOfAvailability'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=TreasuryAccountSymbolComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 870, 1)))

TreasuryAccountSymbolComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endingPeriodOfAvailability'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=TreasuryAccountSymbolComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 871, 1)))

TreasuryAccountSymbolComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'availabilityTypeCode'), availableTypeCodeItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=TreasuryAccountSymbolComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 872, 1)))

TreasuryAccountSymbolComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agency'), agencyComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=TreasuryAccountSymbolComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 890, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 266, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 267, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 268, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 269, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 270, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 271, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 272, 5))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TreasuryAccountSymbolComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agency')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 266, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TreasuryAccountSymbolComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'allocationTransferAgencyIdentifier')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 267, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TreasuryAccountSymbolComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mainAccountNumber')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 268, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TreasuryAccountSymbolComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subAccountSymbol')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 269, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TreasuryAccountSymbolComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beginningPeriodOfAvailability')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 270, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TreasuryAccountSymbolComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endingPeriodOfAvailability')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 271, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TreasuryAccountSymbolComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'availabilityTypeCode')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 272, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TreasuryAccountSymbolComplexType._Automaton = _BuildAutomaton()




addressComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress'), streetAddressComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=addressComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 877, 1)))

addressComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=addressComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 880, 1)))

addressComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'county'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=addressComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 881, 1)))

addressComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'state'), stateItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=addressComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 882, 1)))

addressComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'zipCodePlus4'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=addressComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 883, 1)))

addressComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=addressComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 884, 1)))

addressComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=addressComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 885, 1)))

addressComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=addressComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 886, 1)))

addressComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'congressionalDistrict'), congressionalDistrictItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=addressComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 887, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 284, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 288, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 289, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 290, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 291, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 292, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 293, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 294, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 295, 5))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(addressComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddress')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 284, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(addressComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 288, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(addressComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'county')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 289, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(addressComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'state')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 290, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(addressComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postalCode')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 291, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(addressComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'zipCodePlus4')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 292, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(addressComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countryName')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 293, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(addressComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countryCode')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 294, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(addressComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'congressionalDistrict')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 295, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
addressComplexType._Automaton = _BuildAutomaton_()




streetAddressComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddressLine'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=streetAddressComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 878, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 305, 5))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(streetAddressComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddressLine')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 305, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
streetAddressComplexType._Automaton = _BuildAutomaton_2()




agencyComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agencyIdentifier'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=agencyComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 891, 1)))

agencyComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agencyName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=agencyComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 892, 1)))

agencyComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agencyOffice'), agencyOfficeComplexType, nillable=pyxb.binding.datatypes.boolean(1), scope=agencyComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 895, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 315, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 316, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 317, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(agencyComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agencyIdentifier')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 315, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(agencyComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agencyName')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 316, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(agencyComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agencyOffice')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 317, 5))
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
agencyComplexType._Automaton = _BuildAutomaton_3()




agencyOfficeComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'officeIdentifier'), _ImportedBinding_xbrli.integerItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=agencyOfficeComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 896, 1)))

agencyOfficeComplexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'officeName'), _ImportedBinding_xbrli.stringItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=agencyOfficeComplexType, location=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 897, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 327, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 328, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(agencyOfficeComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'officeIdentifier')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 327, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(agencyOfficeComplexType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'officeName')), pyxb.utils.utility.Location('/Users/micahsaul/Projects/data_act/intercessor/schema/xbrl/gen/da-gen-2015-06-29.xsd', 328, 5))
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
agencyOfficeComplexType._Automaton = _BuildAutomaton_4()


treasuryAccountSymbol._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

beginningPeriodOfAvailability._setSubstitutionGroup(_ImportedBinding_xbrli.item)

endingPeriodOfAvailability._setSubstitutionGroup(_ImportedBinding_xbrli.item)

address._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

streetAddress._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

streetAddressLine._setSubstitutionGroup(_ImportedBinding_xbrli.item)

city._setSubstitutionGroup(_ImportedBinding_xbrli.item)

county._setSubstitutionGroup(_ImportedBinding_xbrli.item)

zipCodePlus4._setSubstitutionGroup(_ImportedBinding_xbrli.item)

postalCode._setSubstitutionGroup(_ImportedBinding_xbrli.item)

countryName._setSubstitutionGroup(_ImportedBinding_xbrli.item)

countryCode._setSubstitutionGroup(_ImportedBinding_xbrli.item)

agency._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

agencyName._setSubstitutionGroup(_ImportedBinding_xbrli.item)

agencyOffice._setSubstitutionGroup(_ImportedBinding_xbrli.tuple)

officeName._setSubstitutionGroup(_ImportedBinding_xbrli.item)

awardID._setSubstitutionGroup(_ImportedBinding_xbrli.item)

availabilityTypeCode._setSubstitutionGroup(_ImportedBinding_xbrli.item)

state._setSubstitutionGroup(_ImportedBinding_xbrli.item)

congressionalDistrict._setSubstitutionGroup(_ImportedBinding_xbrli.item)

allocationTransferAgencyIdentifier._setSubstitutionGroup(_ImportedBinding_xbrli.item)

mainAccountNumber._setSubstitutionGroup(_ImportedBinding_xbrli.item)

subAccountSymbol._setSubstitutionGroup(_ImportedBinding_xbrli.item)

agencyIdentifier._setSubstitutionGroup(_ImportedBinding_xbrli.item)

officeIdentifier._setSubstitutionGroup(_ImportedBinding_xbrli.item)
