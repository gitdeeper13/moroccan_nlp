# Data Protection Impact Assessment (DPIA)

**Project:** moroccan_nlp
**Domain:** computer_science
**Stage:** EXPERIMENTAL
**Date:** 2026-07-02T09:03:33.772659

## Summary

- **Total PII Found:** 2659
- **Total Risks:** 3
- **Total Recommendations:** 4
- **Overall Risk Level:** HIGH
- **Compliance Status:** PARTIALLY_COMPLIANT

## PII Findings

- **name** (Severity: MEDIUM)
  - Value: `Younes Samih`
  - Source: references

- **name** (Severity: MEDIUM)
  - Value: `Wolfgang Maier`
  - Source: references

- **name** (Severity: MEDIUM)
  - Value: `An Arabic`
  - Source: references

- **name** (Severity: MEDIUM)
  - Value: `Moroccan Darija Code`
  - Source: references

- **name** (Severity: MEDIUM)
  - Value: `Switched Corpus`
  - Source: references

- **name** (Severity: MEDIUM)
  - Value: `Elabbas Benmamoun`
  - Source: references

- **name** (Severity: MEDIUM)
  - Value: `Licensing of Negative Polarity`
  - Source: references

- **name** (Severity: MEDIUM)
  - Value: `Items in Moroccan Arabic`
  - Source: references

- **name** (Severity: MEDIUM)
  - Value: `Ann Bies`
  - Source: references

- **name** (Severity: MEDIUM)
  - Value: `Denise DiPersio`
  - Source: references

## Risks

- **PII_EXPOSURE** (Severity: HIGH)
  - Found 2659 PII instances

- **HIGH_RISK_DATA** (Severity: HIGH)
  - Found high-risk data categories: bank

- **ANONYMIZATION** (Severity: HIGH)
  - PII found without evidence of anonymization

## Recommendations

- **Anonymize or pseudonymize PII** (Priority: HIGH)
  - Found 2659 PII instances of types: postal_code, credit_card, name
  - Action: Use anonymization_agent to remove or pseudonymize PII before publication

- **Implement additional safeguards for high-risk data** (Priority: CRITICAL)
  - High-risk data categories detected: bank
  - Action: Implement encryption, access control, and logging for high-risk data

- **Conduct formal Data Protection Impact Assessment** (Priority: HIGH)
  - Formal DPIA required due to PII processing and high-risk data
  - Action: Complete the DPIA report and submit to data protection officer

- **Update privacy documentation** (Priority: MEDIUM)
  - Privacy notice and data processing records need updating
  - Action: Update README and documentation with privacy information
