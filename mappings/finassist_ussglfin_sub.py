#!/usr/bin/env python

#
# Generated  by generateDS.py.
#
# Command line options:
#   ('-o', 'finassist_ussglfin.py')
#   ('-s', 'finassist_ussglfin_sub.py')
#   ('-f', '')
#   ('--no-dates', '')
#   ('--no-versions', '')
#   ('--member-specs', 'list')
#
# Command line arguments:
#   ../schema/xbrl/plt/case-finassist-ussglfin/da-palette-finassist-ussglfin-2015-06-29.xsd
#
# Command line:
#   /Users/rebeccasweger/Dev/.virtualenvs/intercessor/lib/python2.7/site-packages/generateDS-2.17a0/generateDS.py -o "finassist_ussglfin.py" -s "finassist_ussglfin_sub.py" -f --no-dates --no-versions --member-specs="list" ../schema/xbrl/plt/case-finassist-ussglfin/da-palette-finassist-ussglfin-2015-06-29.xsd
#
# Current working directory (os.getcwd()):
#   mappings
#

import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class accountingEntriesComplexTypeSub(supermod.accountingEntriesComplexType):
    def __init__(self, id=None, fiscalYear=None, period=None, USSGLentryHeader=None):
        super(accountingEntriesComplexTypeSub, self).__init__(id, fiscalYear, period, USSGLentryHeader, )
supermod.accountingEntriesComplexType.subclass = accountingEntriesComplexTypeSub
# end class accountingEntriesComplexTypeSub


class USSGLentryHeaderComplexTypeSub(supermod.USSGLentryHeaderComplexType):
    def __init__(self, id=None, treasuryAccountSymbol=None, entryDetail=None, obligatedAmount=None, unobligatedAmount=None, budgetAuthorityAppropriated=None, otherBudgetaryResources=None, outlays=None, appropriationAccount=None):
        super(USSGLentryHeaderComplexTypeSub, self).__init__(id, treasuryAccountSymbol, entryDetail, obligatedAmount, unobligatedAmount, budgetAuthorityAppropriated, otherBudgetaryResources, outlays, appropriationAccount, )
supermod.USSGLentryHeaderComplexType.subclass = USSGLentryHeaderComplexTypeSub
# end class USSGLentryHeaderComplexTypeSub


class entryDetailComplexTypeSub(supermod.entryDetailComplexType):
    def __init__(self, id=None, account=None, amount=None, debitCreditCode=None, beginningEndIndicator=None, programActivity=None):
        super(entryDetailComplexTypeSub, self).__init__(id, account, amount, debitCreditCode, beginningEndIndicator, programActivity, )
supermod.entryDetailComplexType.subclass = entryDetailComplexTypeSub
# end class entryDetailComplexTypeSub


class accountComplexTypeSub(supermod.accountComplexType):
    def __init__(self, id=None, accountNumber=None, objectClass=None, awardID=None, accountDescription=None):
        super(accountComplexTypeSub, self).__init__(id, accountNumber, objectClass, awardID, accountDescription, )
supermod.accountComplexType.subclass = accountComplexTypeSub
# end class accountComplexTypeSub


class decimalItemTypeSub(supermod.decimalItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(decimalItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.decimalItemType.subclass = decimalItemTypeSub
# end class decimalItemTypeSub


class floatItemTypeSub(supermod.floatItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(floatItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.floatItemType.subclass = floatItemTypeSub
# end class floatItemTypeSub


class doubleItemTypeSub(supermod.doubleItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(doubleItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.doubleItemType.subclass = doubleItemTypeSub
# end class doubleItemTypeSub


class monetaryItemTypeSub(supermod.monetaryItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None, extensiontype_=None):
        super(monetaryItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, extensiontype_, )
supermod.monetaryItemType.subclass = monetaryItemTypeSub
# end class monetaryItemTypeSub


class sharesItemTypeSub(supermod.sharesItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(sharesItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.sharesItemType.subclass = sharesItemTypeSub
# end class sharesItemTypeSub


class pureItemTypeSub(supermod.pureItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None, extensiontype_=None):
        super(pureItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, extensiontype_, )
supermod.pureItemType.subclass = pureItemTypeSub
# end class pureItemTypeSub


class fractionItemTypeSub(supermod.fractionItemType):
    def __init__(self, unitRef=None, id=None, contextRef=None, numerator=None, denominator=None):
        super(fractionItemTypeSub, self).__init__(unitRef, id, contextRef, numerator, denominator, )
supermod.fractionItemType.subclass = fractionItemTypeSub
# end class fractionItemTypeSub


class integerItemTypeSub(supermod.integerItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(integerItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.integerItemType.subclass = integerItemTypeSub
# end class integerItemTypeSub


class nonPositiveIntegerItemTypeSub(supermod.nonPositiveIntegerItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(nonPositiveIntegerItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.nonPositiveIntegerItemType.subclass = nonPositiveIntegerItemTypeSub
# end class nonPositiveIntegerItemTypeSub


class negativeIntegerItemTypeSub(supermod.negativeIntegerItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(negativeIntegerItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.negativeIntegerItemType.subclass = negativeIntegerItemTypeSub
# end class negativeIntegerItemTypeSub


class longItemTypeSub(supermod.longItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(longItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.longItemType.subclass = longItemTypeSub
# end class longItemTypeSub


class intItemTypeSub(supermod.intItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(intItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.intItemType.subclass = intItemTypeSub
# end class intItemTypeSub


class shortItemTypeSub(supermod.shortItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(shortItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.shortItemType.subclass = shortItemTypeSub
# end class shortItemTypeSub


class byteItemTypeSub(supermod.byteItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(byteItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.byteItemType.subclass = byteItemTypeSub
# end class byteItemTypeSub


class nonNegativeIntegerItemTypeSub(supermod.nonNegativeIntegerItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(nonNegativeIntegerItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.nonNegativeIntegerItemType.subclass = nonNegativeIntegerItemTypeSub
# end class nonNegativeIntegerItemTypeSub


class unsignedLongItemTypeSub(supermod.unsignedLongItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(unsignedLongItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.unsignedLongItemType.subclass = unsignedLongItemTypeSub
# end class unsignedLongItemTypeSub


class unsignedIntItemTypeSub(supermod.unsignedIntItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(unsignedIntItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.unsignedIntItemType.subclass = unsignedIntItemTypeSub
# end class unsignedIntItemTypeSub


class unsignedShortItemTypeSub(supermod.unsignedShortItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(unsignedShortItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.unsignedShortItemType.subclass = unsignedShortItemTypeSub
# end class unsignedShortItemTypeSub


class unsignedByteItemTypeSub(supermod.unsignedByteItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(unsignedByteItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.unsignedByteItemType.subclass = unsignedByteItemTypeSub
# end class unsignedByteItemTypeSub


class positiveIntegerItemTypeSub(supermod.positiveIntegerItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(positiveIntegerItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.positiveIntegerItemType.subclass = positiveIntegerItemTypeSub
# end class positiveIntegerItemTypeSub


class stringItemTypeSub(supermod.stringItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(stringItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.stringItemType.subclass = stringItemTypeSub
# end class stringItemTypeSub


class booleanItemTypeSub(supermod.booleanItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(booleanItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.booleanItemType.subclass = booleanItemTypeSub
# end class booleanItemTypeSub


class hexBinaryItemTypeSub(supermod.hexBinaryItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(hexBinaryItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.hexBinaryItemType.subclass = hexBinaryItemTypeSub
# end class hexBinaryItemTypeSub


class base64BinaryItemTypeSub(supermod.base64BinaryItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(base64BinaryItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.base64BinaryItemType.subclass = base64BinaryItemTypeSub
# end class base64BinaryItemTypeSub


class anyURIItemTypeSub(supermod.anyURIItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(anyURIItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.anyURIItemType.subclass = anyURIItemTypeSub
# end class anyURIItemTypeSub


class QNameItemTypeSub(supermod.QNameItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(QNameItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.QNameItemType.subclass = QNameItemTypeSub
# end class QNameItemTypeSub


class durationItemTypeSub(supermod.durationItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(durationItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.durationItemType.subclass = durationItemTypeSub
# end class durationItemTypeSub


class dateTimeItemTypeSub(supermod.dateTimeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(dateTimeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.dateTimeItemType.subclass = dateTimeItemTypeSub
# end class dateTimeItemTypeSub


class timeItemTypeSub(supermod.timeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(timeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.timeItemType.subclass = timeItemTypeSub
# end class timeItemTypeSub


class dateItemTypeSub(supermod.dateItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(dateItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.dateItemType.subclass = dateItemTypeSub
# end class dateItemTypeSub


class gYearMonthItemTypeSub(supermod.gYearMonthItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(gYearMonthItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.gYearMonthItemType.subclass = gYearMonthItemTypeSub
# end class gYearMonthItemTypeSub


class gYearItemTypeSub(supermod.gYearItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(gYearItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.gYearItemType.subclass = gYearItemTypeSub
# end class gYearItemTypeSub


class gMonthDayItemTypeSub(supermod.gMonthDayItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(gMonthDayItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.gMonthDayItemType.subclass = gMonthDayItemTypeSub
# end class gMonthDayItemTypeSub


class gDayItemTypeSub(supermod.gDayItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(gDayItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.gDayItemType.subclass = gDayItemTypeSub
# end class gDayItemTypeSub


class gMonthItemTypeSub(supermod.gMonthItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(gMonthItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.gMonthItemType.subclass = gMonthItemTypeSub
# end class gMonthItemTypeSub


class normalizedStringItemTypeSub(supermod.normalizedStringItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(normalizedStringItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.normalizedStringItemType.subclass = normalizedStringItemTypeSub
# end class normalizedStringItemTypeSub


class tokenItemTypeSub(supermod.tokenItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None, extensiontype_=None):
        super(tokenItemTypeSub, self).__init__(id, contextRef, valueOf_, extensiontype_, )
supermod.tokenItemType.subclass = tokenItemTypeSub
# end class tokenItemTypeSub


class languageItemTypeSub(supermod.languageItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(languageItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.languageItemType.subclass = languageItemTypeSub
# end class languageItemTypeSub


class NameItemTypeSub(supermod.NameItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(NameItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.NameItemType.subclass = NameItemTypeSub
# end class NameItemTypeSub


class NCNameItemTypeSub(supermod.NCNameItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(NCNameItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.NCNameItemType.subclass = NCNameItemTypeSub
# end class NCNameItemTypeSub


class segmentSub(supermod.segment):
    def __init__(self, anytypeobjs_=None):
        super(segmentSub, self).__init__(anytypeobjs_, )
supermod.segment.subclass = segmentSub
# end class segmentSub


class contextEntityTypeSub(supermod.contextEntityType):
    def __init__(self, identifier=None, segment=None):
        super(contextEntityTypeSub, self).__init__(identifier, segment, )
supermod.contextEntityType.subclass = contextEntityTypeSub
# end class contextEntityTypeSub


class identifierSub(supermod.identifier):
    def __init__(self, scheme=None, valueOf_=None):
        super(identifierSub, self).__init__(scheme, valueOf_, )
supermod.identifier.subclass = identifierSub
# end class identifierSub


class contextPeriodTypeSub(supermod.contextPeriodType):
    def __init__(self, startDate=None, endDate=None, instant=None, forever=None):
        super(contextPeriodTypeSub, self).__init__(startDate, endDate, instant, forever, )
supermod.contextPeriodType.subclass = contextPeriodTypeSub
# end class contextPeriodTypeSub


class contextScenarioTypeSub(supermod.contextScenarioType):
    def __init__(self, anytypeobjs_=None):
        super(contextScenarioTypeSub, self).__init__(anytypeobjs_, )
supermod.contextScenarioType.subclass = contextScenarioTypeSub
# end class contextScenarioTypeSub


class contextSub(supermod.context):
    def __init__(self, id=None, entity=None, period=None, scenario=None):
        super(contextSub, self).__init__(id, entity, period, scenario, )
supermod.context.subclass = contextSub
# end class contextSub


class measuresTypeSub(supermod.measuresType):
    def __init__(self, measure=None):
        super(measuresTypeSub, self).__init__(measure, )
supermod.measuresType.subclass = measuresTypeSub
# end class measuresTypeSub


class divideSub(supermod.divide):
    def __init__(self, unitNumerator=None, unitDenominator=None):
        super(divideSub, self).__init__(unitNumerator, unitDenominator, )
supermod.divide.subclass = divideSub
# end class divideSub


class unitSub(supermod.unit):
    def __init__(self, id=None, measure=None, divide=None):
        super(unitSub, self).__init__(id, measure, divide, )
supermod.unit.subclass = unitSub
# end class unitSub


class xbrlSub(supermod.xbrl):
    def __init__(self, id=None, schemaRef=None, linkbaseRef=None, roleRef=None, arcroleRef=None, item=None, tuple=None, context=None, unit=None, footnoteLink=None):
        super(xbrlSub, self).__init__(id, schemaRef, linkbaseRef, roleRef, arcroleRef, item, tuple, context, unit, footnoteLink, )
supermod.xbrl.subclass = xbrlSub
# end class xbrlSub


class presentationLinkSub(supermod.presentationLink):
    def __init__(self, title=None, documentation=None, loc=None, presentationArc=None):
        super(presentationLinkSub, self).__init__(title, documentation, loc, presentationArc, )
supermod.presentationLink.subclass = presentationLinkSub
# end class presentationLinkSub


class definitionLinkSub(supermod.definitionLink):
    def __init__(self, title=None, documentation=None, loc=None, definitionArc=None):
        super(definitionLinkSub, self).__init__(title, documentation, loc, definitionArc, )
supermod.definitionLink.subclass = definitionLinkSub
# end class definitionLinkSub


class calculationLinkSub(supermod.calculationLink):
    def __init__(self, title=None, documentation=None, loc=None, calculationArc=None):
        super(calculationLinkSub, self).__init__(title, documentation, loc, calculationArc, )
supermod.calculationLink.subclass = calculationLinkSub
# end class calculationLinkSub


class labelLinkSub(supermod.labelLink):
    def __init__(self, title=None, documentation=None, loc=None, labelArc=None, label=None):
        super(labelLinkSub, self).__init__(title, documentation, loc, labelArc, label, )
supermod.labelLink.subclass = labelLinkSub
# end class labelLinkSub


class referenceLinkSub(supermod.referenceLink):
    def __init__(self, title=None, documentation=None, loc=None, referenceArc=None, reference=None):
        super(referenceLinkSub, self).__init__(title, documentation, loc, referenceArc, reference, )
supermod.referenceLink.subclass = referenceLinkSub
# end class referenceLinkSub


class footnoteLinkSub(supermod.footnoteLink):
    def __init__(self, title=None, documentation=None, loc=None, footnoteArc=None, footnote=None):
        super(footnoteLinkSub, self).__init__(title, documentation, loc, footnoteArc, footnote, )
supermod.footnoteLink.subclass = footnoteLinkSub
# end class footnoteLinkSub


class linkbaseSub(supermod.linkbase):
    def __init__(self, id=None, documentation=None, roleRef=None, arcroleRef=None, extended=None):
        super(linkbaseSub, self).__init__(id, documentation, roleRef, arcroleRef, extended, )
supermod.linkbase.subclass = linkbaseSub
# end class linkbaseSub


class linkbaseRefSub(supermod.linkbaseRef):
    def __init__(self, arcrole=None):
        super(linkbaseRefSub, self).__init__(arcrole, )
supermod.linkbaseRef.subclass = linkbaseRefSub
# end class linkbaseRefSub


class roleTypeSub(supermod.roleType):
    def __init__(self, roleURI=None, id=None, definition=None, usedOn=None):
        super(roleTypeSub, self).__init__(roleURI, id, definition, usedOn, )
supermod.roleType.subclass = roleTypeSub
# end class roleTypeSub


class arcroleTypeSub(supermod.arcroleType):
    def __init__(self, arcroleURI=None, id=None, cyclesAllowed=None, definition=None, usedOn=None):
        super(arcroleTypeSub, self).__init__(arcroleURI, id, cyclesAllowed, definition, usedOn, )
supermod.arcroleType.subclass = arcroleTypeSub
# end class arcroleTypeSub


class documentationTypeSub(supermod.documentationType):
    def __init__(self, valueOf_=None):
        super(documentationTypeSub, self).__init__(valueOf_, )
supermod.documentationType.subclass = documentationTypeSub
# end class documentationTypeSub


class titleTypeSub(supermod.titleType):
    def __init__(self, type_=None):
        super(titleTypeSub, self).__init__(type_, )
supermod.titleType.subclass = titleTypeSub
# end class titleTypeSub


class locatorTypeSub(supermod.locatorType):
    def __init__(self, title_attr=None, label=None, href=None, role=None, type_=None, title=None):
        super(locatorTypeSub, self).__init__(title_attr, label, href, role, type_, title, )
supermod.locatorType.subclass = locatorTypeSub
# end class locatorTypeSub


class arcTypeSub(supermod.arcType):
    def __init__(self, use=None, from_=None, title_attr=None, show=None, arcrole=None, actuate=None, priority=None, to=None, type_=None, order=None, title=None, extensiontype_=None):
        super(arcTypeSub, self).__init__(use, from_, title_attr, show, arcrole, actuate, priority, to, type_, order, title, extensiontype_, )
supermod.arcType.subclass = arcTypeSub
# end class arcTypeSub


class resourceTypeSub(supermod.resourceType):
    def __init__(self, role=None, title=None, type_=None, id=None, label=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None):
        super(resourceTypeSub, self).__init__(role, title, type_, id, label, valueOf_, mixedclass_, content_, extensiontype_, )
supermod.resourceType.subclass = resourceTypeSub
# end class resourceTypeSub


class extendedTypeSub(supermod.extendedType):
    def __init__(self, role=None, type_=None, id=None, title_attr=None, title=None, documentation=None, locator=None, arc=None, resource=None):
        super(extendedTypeSub, self).__init__(role, type_, id, title_attr, title, documentation, locator, arc, resource, )
supermod.extendedType.subclass = extendedTypeSub
# end class extendedTypeSub


class simpleTypeSub(supermod.simpleType):
    def __init__(self, show=None, title=None, actuate=None, href=None, role=None, arcrole=None, type_=None, extensiontype_=None):
        super(simpleTypeSub, self).__init__(show, title, actuate, href, role, arcrole, type_, extensiontype_, )
supermod.simpleType.subclass = simpleTypeSub
# end class simpleTypeSub


class accountPurposeCodeItemTypeSub(supermod.accountPurposeCodeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(accountPurposeCodeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.accountPurposeCodeItemType.subclass = accountPurposeCodeItemTypeSub
# end class accountPurposeCodeItemTypeSub


class accountTypeItemTypeSub(supermod.accountTypeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(accountTypeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.accountTypeItemType.subclass = accountTypeItemTypeSub
# end class accountTypeItemTypeSub


class bookTaxDifferenceItemTypeSub(supermod.bookTaxDifferenceItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(bookTaxDifferenceItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.bookTaxDifferenceItemType.subclass = bookTaxDifferenceItemTypeSub
# end class bookTaxDifferenceItemTypeSub


class identifierOrganizationTypeItemTypeSub(supermod.identifierOrganizationTypeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(identifierOrganizationTypeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.identifierOrganizationTypeItemType.subclass = identifierOrganizationTypeItemTypeSub
# end class identifierOrganizationTypeItemTypeSub


class debitCreditCodeItemTypeSub(supermod.debitCreditCodeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(debitCreditCodeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.debitCreditCodeItemType.subclass = debitCreditCodeItemTypeSub
# end class debitCreditCodeItemTypeSub


class documentTypeItemTypeSub(supermod.documentTypeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(documentTypeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.documentTypeItemType.subclass = documentTypeItemTypeSub
# end class documentTypeItemTypeSub


class invoiceTypeItemTypeSub(supermod.invoiceTypeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(invoiceTypeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.invoiceTypeItemType.subclass = invoiceTypeItemTypeSub
# end class invoiceTypeItemTypeSub


class entriesTypeItemTypeSub(supermod.entriesTypeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(entriesTypeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.entriesTypeItemType.subclass = entriesTypeItemTypeSub
# end class entriesTypeItemTypeSub


class entryTypeItemTypeSub(supermod.entryTypeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(entryTypeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.entryTypeItemType.subclass = entryTypeItemTypeSub
# end class entryTypeItemTypeSub


class identifierTypeItemTypeSub(supermod.identifierTypeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(identifierTypeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.identifierTypeItemType.subclass = identifierTypeItemTypeSub
# end class identifierTypeItemTypeSub


class mainAccountTypeItemTypeSub(supermod.mainAccountTypeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(mainAccountTypeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.mainAccountTypeItemType.subclass = mainAccountTypeItemTypeSub
# end class mainAccountTypeItemTypeSub


class postingStatusItemTypeSub(supermod.postingStatusItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(postingStatusItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.postingStatusItemType.subclass = postingStatusItemTypeSub
# end class postingStatusItemTypeSub


class qualifierEntryItemTypeSub(supermod.qualifierEntryItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(qualifierEntryItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.qualifierEntryItemType.subclass = qualifierEntryItemTypeSub
# end class qualifierEntryItemTypeSub


class revisesUniqueIDActionItemTypeSub(supermod.revisesUniqueIDActionItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(revisesUniqueIDActionItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.revisesUniqueIDActionItemType.subclass = revisesUniqueIDActionItemTypeSub
# end class revisesUniqueIDActionItemTypeSub


class signOfAmountItemTypeSub(supermod.signOfAmountItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(signOfAmountItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.signOfAmountItemType.subclass = signOfAmountItemTypeSub
# end class signOfAmountItemTypeSub


class sourceJournalIDItemTypeSub(supermod.sourceJournalIDItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(sourceJournalIDItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.sourceJournalIDItemType.subclass = sourceJournalIDItemTypeSub
# end class sourceJournalIDItemTypeSub


class xbrlIncludeItemTypeSub(supermod.xbrlIncludeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(xbrlIncludeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.xbrlIncludeItemType.subclass = xbrlIncludeItemTypeSub
# end class xbrlIncludeItemTypeSub


class phoneNumberDescriptionItemTypeSub(supermod.phoneNumberDescriptionItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(phoneNumberDescriptionItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.phoneNumberDescriptionItemType.subclass = phoneNumberDescriptionItemTypeSub
# end class phoneNumberDescriptionItemTypeSub


class availableTypeCodeItemTypeSub(supermod.availableTypeCodeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(availableTypeCodeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.availableTypeCodeItemType.subclass = availableTypeCodeItemTypeSub
# end class availableTypeCodeItemTypeSub


class TreasuryAccountSymbolComplexTypeSub(supermod.TreasuryAccountSymbolComplexType):
    def __init__(self, id=None, agency=None, allocationTransferAgencyIdentifier=None, mainAccountNumber=None, subAccountSymbol=None, beginningPeriodOfAvailability=None, endingPeriodOfAvailability=None, availabilityTypeCode=None):
        super(TreasuryAccountSymbolComplexTypeSub, self).__init__(id, agency, allocationTransferAgencyIdentifier, mainAccountNumber, subAccountSymbol, beginningPeriodOfAvailability, endingPeriodOfAvailability, availabilityTypeCode, )
supermod.TreasuryAccountSymbolComplexType.subclass = TreasuryAccountSymbolComplexTypeSub
# end class TreasuryAccountSymbolComplexTypeSub


class addressComplexTypeSub(supermod.addressComplexType):
    def __init__(self, id=None, streetAddress=None, city=None, county=None, state=None, postalCode=None, zipCodePlus4=None, countryName=None, countryCode=None, congressionalDistrict=None):
        super(addressComplexTypeSub, self).__init__(id, streetAddress, city, county, state, postalCode, zipCodePlus4, countryName, countryCode, congressionalDistrict, )
supermod.addressComplexType.subclass = addressComplexTypeSub
# end class addressComplexTypeSub


class streetAddressComplexTypeSub(supermod.streetAddressComplexType):
    def __init__(self, id=None, streetAddressLine=None):
        super(streetAddressComplexTypeSub, self).__init__(id, streetAddressLine, )
supermod.streetAddressComplexType.subclass = streetAddressComplexTypeSub
# end class streetAddressComplexTypeSub


class agencyComplexTypeSub(supermod.agencyComplexType):
    def __init__(self, id=None, agencyIdentifier=None, agencyName=None, agencyOffice=None):
        super(agencyComplexTypeSub, self).__init__(id, agencyIdentifier, agencyName, agencyOffice, )
supermod.agencyComplexType.subclass = agencyComplexTypeSub
# end class agencyComplexTypeSub


class agencyOfficeComplexTypeSub(supermod.agencyOfficeComplexType):
    def __init__(self, id=None, officeIdentifier=None, officeName=None):
        super(agencyOfficeComplexTypeSub, self).__init__(id, officeIdentifier, officeName, )
supermod.agencyOfficeComplexType.subclass = agencyOfficeComplexTypeSub
# end class agencyOfficeComplexTypeSub


class amountItemTypeSub(supermod.amountItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(amountItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.amountItemType.subclass = amountItemTypeSub
# end class amountItemTypeSub


class congressionalDistrictItemTypeSub(supermod.congressionalDistrictItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(congressionalDistrictItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.congressionalDistrictItemType.subclass = congressionalDistrictItemTypeSub
# end class congressionalDistrictItemTypeSub


class stateItemTypeSub(supermod.stateItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(stateItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.stateItemType.subclass = stateItemTypeSub
# end class stateItemTypeSub


class awardComplexTypeSub(supermod.awardComplexType):
    def __init__(self, id=None, awardDescription=None, awardID=None, parentAwardID=None, modificationAmendmentNumber=None, recordType=None, typeOfAction=None, typeOfTransactionCode=None, awardeeInformation=None, primaryPlaceOfPerformance=None, periodOfPerformance=None, awardingAgency=None, fundingAgency=None, awardingSubTierAgency=None, fundingSubTierAgency=None, highlyCompensatedOfficer=None, catalogOfFederalDomesticAssistanceProgram=None, awardAmounts=None):
        super(awardComplexTypeSub, self).__init__(id, awardDescription, awardID, parentAwardID, modificationAmendmentNumber, recordType, typeOfAction, typeOfTransactionCode, awardeeInformation, primaryPlaceOfPerformance, periodOfPerformance, awardingAgency, fundingAgency, awardingSubTierAgency, fundingSubTierAgency, highlyCompensatedOfficer, catalogOfFederalDomesticAssistanceProgram, awardAmounts, )
supermod.awardComplexType.subclass = awardComplexTypeSub
# end class awardComplexTypeSub


class catalogOfFederalDomesticAssistanceProgramComplexTypeSub(supermod.catalogOfFederalDomesticAssistanceProgramComplexType):
    def __init__(self, id=None, catalogOfFederalDomesticAssistanceTitle=None, catalogOfFederalDomesticAssistanceNumber=None):
        super(catalogOfFederalDomesticAssistanceProgramComplexTypeSub, self).__init__(id, catalogOfFederalDomesticAssistanceTitle, catalogOfFederalDomesticAssistanceNumber, )
supermod.catalogOfFederalDomesticAssistanceProgramComplexType.subclass = catalogOfFederalDomesticAssistanceProgramComplexTypeSub
# end class catalogOfFederalDomesticAssistanceProgramComplexTypeSub


class awardAmountsComplexTypeSub(supermod.awardAmountsComplexType):
    def __init__(self, id=None, federalFundingAmount=None, totalFundingAmount=None, nonFederalFundingAmount=None):
        super(awardAmountsComplexTypeSub, self).__init__(id, federalFundingAmount, totalFundingAmount, nonFederalFundingAmount, )
supermod.awardAmountsComplexType.subclass = awardAmountsComplexTypeSub
# end class awardAmountsComplexTypeSub


class awardeeInformationComplexTypeSub(supermod.awardeeInformationComplexType):
    def __init__(self, id=None, businessType=None, awardeeLegalBusinessName=None, ultimateParentUniqueIdentifier=None, awardeeUniqueIdentifier=None, awardeeUniqueIdentifierSupplemental=None, ultimateParentLegalBusinessName=None, awardeeAddress=None):
        super(awardeeInformationComplexTypeSub, self).__init__(id, businessType, awardeeLegalBusinessName, ultimateParentUniqueIdentifier, awardeeUniqueIdentifier, awardeeUniqueIdentifierSupplemental, ultimateParentLegalBusinessName, awardeeAddress, )
supermod.awardeeInformationComplexType.subclass = awardeeInformationComplexTypeSub
# end class awardeeInformationComplexTypeSub


class periodOfPerformanceComplexTypeSub(supermod.periodOfPerformanceComplexType):
    def __init__(self, id=None, periodOfPerformanceActionDate=None, periodOfPerformanceStartDate=None, periodOfPerformanceCurrentEndDate=None, periodOfPerformancePotentialEndDate=None):
        super(periodOfPerformanceComplexTypeSub, self).__init__(id, periodOfPerformanceActionDate, periodOfPerformanceStartDate, periodOfPerformanceCurrentEndDate, periodOfPerformancePotentialEndDate, )
supermod.periodOfPerformanceComplexType.subclass = periodOfPerformanceComplexTypeSub
# end class periodOfPerformanceComplexTypeSub


class businessTypeItemTypeSub(supermod.businessTypeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(businessTypeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.businessTypeItemType.subclass = businessTypeItemTypeSub
# end class businessTypeItemTypeSub


class recordTypeItemTypeSub(supermod.recordTypeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(recordTypeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.recordTypeItemType.subclass = recordTypeItemTypeSub
# end class recordTypeItemTypeSub


class typeOfActionItemTypeSub(supermod.typeOfActionItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(typeOfActionItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.typeOfActionItemType.subclass = typeOfActionItemTypeSub
# end class typeOfActionItemTypeSub


class typeOfTransactionCodeItemTypeSub(supermod.typeOfTransactionCodeItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(typeOfTransactionCodeItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.typeOfTransactionCodeItemType.subclass = typeOfTransactionCodeItemTypeSub
# end class typeOfTransactionCodeItemTypeSub


class highlyCompensatedOfficerComplexTypeSub(supermod.highlyCompensatedOfficerComplexType):
    def __init__(self, id=None, highlyCompensatedOfficerFirstName=None, highlyCompensatedOfficerMiddleInitial=None, highlyCompensatedOfficerLastName=None, highlyCompensatedOfficerCompensation=None):
        super(highlyCompensatedOfficerComplexTypeSub, self).__init__(id, highlyCompensatedOfficerFirstName, highlyCompensatedOfficerMiddleInitial, highlyCompensatedOfficerLastName, highlyCompensatedOfficerCompensation, )
supermod.highlyCompensatedOfficerComplexType.subclass = highlyCompensatedOfficerComplexTypeSub
# end class highlyCompensatedOfficerComplexTypeSub


class arcroleRefSub(supermod.arcroleRef):
    def __init__(self, show=None, title=None, actuate=None, href=None, role=None, arcrole=None, type_=None, arcroleURI=None):
        super(arcroleRefSub, self).__init__(show, title, actuate, href, role, arcrole, type_, arcroleURI, )
supermod.arcroleRef.subclass = arcroleRefSub
# end class arcroleRefSub


class roleRefSub(supermod.roleRef):
    def __init__(self, show=None, title=None, actuate=None, href=None, role=None, arcrole=None, type_=None, roleURI=None):
        super(roleRefSub, self).__init__(show, title, actuate, href, role, arcrole, type_, roleURI, )
supermod.roleRef.subclass = roleRefSub
# end class roleRefSub


class footnoteSub(supermod.footnote):
    def __init__(self, role=None, title=None, type_=None, id=None, label=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(footnoteSub, self).__init__(role, title, type_, id, label, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.footnote.subclass = footnoteSub
# end class footnoteSub


class referenceSub(supermod.reference):
    def __init__(self, role=None, title=None, type_=None, id=None, label=None, part=None, valueOf_=None, mixedclass_=None, content_=None):
        super(referenceSub, self).__init__(role, title, type_, id, label, part, valueOf_, mixedclass_, content_, )
supermod.reference.subclass = referenceSub
# end class referenceSub


class labelSub(supermod.label):
    def __init__(self, role=None, title=None, type_=None, id=None, label=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(labelSub, self).__init__(role, title, type_, id, label, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.label.subclass = labelSub
# end class labelSub


class calculationArcSub(supermod.calculationArc):
    def __init__(self, use=None, from_=None, title_attr=None, show=None, arcrole=None, actuate=None, priority=None, to=None, type_=None, order=None, title=None, weight=None):
        super(calculationArcSub, self).__init__(use, from_, title_attr, show, arcrole, actuate, priority, to, type_, order, title, weight, )
supermod.calculationArc.subclass = calculationArcSub
# end class calculationArcSub


class presentationArcSub(supermod.presentationArc):
    def __init__(self, use=None, from_=None, title_attr=None, show=None, arcrole=None, actuate=None, priority=None, to=None, type_=None, order=None, title=None, preferredLabel=None):
        super(presentationArcSub, self).__init__(use, from_, title_attr, show, arcrole, actuate, priority, to, type_, order, title, preferredLabel, )
supermod.presentationArc.subclass = presentationArcSub
# end class presentationArcSub


class fiscalYearItemTypeSub(supermod.fiscalYearItemType):
    def __init__(self, unitRef=None, decimals=None, id=None, contextRef=None, precision=None, valueOf_=None):
        super(fiscalYearItemTypeSub, self).__init__(unitRef, decimals, id, contextRef, precision, valueOf_, )
supermod.fiscalYearItemType.subclass = fiscalYearItemTypeSub
# end class fiscalYearItemTypeSub


class beginningEndIndicatorItemTypeSub(supermod.beginningEndIndicatorItemType):
    def __init__(self, id=None, contextRef=None, valueOf_=None):
        super(beginningEndIndicatorItemTypeSub, self).__init__(id, contextRef, valueOf_, )
supermod.beginningEndIndicatorItemType.subclass = beginningEndIndicatorItemTypeSub
# end class beginningEndIndicatorItemTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'accountingEntriesComplexType'
        rootClass = supermod.accountingEntriesComplexType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:gl-plt="http://www.xbrl.org/int/gl/plt/2006-10-25"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'accountingEntriesComplexType'
        rootClass = supermod.accountingEntriesComplexType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'accountingEntriesComplexType'
        rootClass = supermod.accountingEntriesComplexType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:gl-plt="http://www.xbrl.org/int/gl/plt/2006-10-25"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'accountingEntriesComplexType'
        rootClass = supermod.accountingEntriesComplexType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
