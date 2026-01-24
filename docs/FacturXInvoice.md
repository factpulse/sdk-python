# FacturXInvoice

Data model for an invoice to be converted to Factur-X.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** |  | 
**payment_due_date** | **str** |  | 
**invoice_date** | **str** |  | [optional] 
**submission_mode** | [**SubmissionMode**](SubmissionMode.md) |  | [optional] 
**recipient** | [**Recipient**](Recipient.md) |  | 
**supplier** | [**Supplier**](Supplier.md) |  | 
**invoicing_framework** | [**InvoicingFramework**](InvoicingFramework.md) |  | 
**references** | [**InvoiceReferences**](InvoiceReferences.md) |  | 
**totals** | [**InvoiceTotals**](InvoiceTotals.md) |  | 
**invoice_lines** | [**List[InvoiceLine]**](InvoiceLine.md) |  | [optional] 
**vat_lines** | [**List[VATLine]**](VATLine.md) |  | [optional] 
**notes** | [**List[InvoiceNote]**](InvoiceNote.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**current_user_id** | **int** |  | [optional] 
**supplementary_attachments** | [**List[SupplementaryAttachment]**](SupplementaryAttachment.md) |  | [optional] 
**payee** | [**Payee**](Payee.md) |  | [optional] 
**delivery_party** | [**DeliveryParty**](DeliveryParty.md) |  | [optional] 
**tax_representative** | [**TaxRepresentative**](TaxRepresentative.md) |  | [optional] 
**delivery_date** | **str** |  | [optional] 
**billing_period_start** | **str** |  | [optional] 
**billing_period_end** | **str** |  | [optional] 
**payment_reference** | **str** |  | [optional] 
**creditor_reference_id** | **str** |  | [optional] 
**direct_debit_mandate_id** | **str** |  | [optional] 
**debtor_iban** | **str** |  | [optional] 
**payment_terms** | **str** |  | [optional] 
**allowances_charges** | [**List[AllowanceCharge]**](AllowanceCharge.md) |  | [optional] 
**additional_documents** | [**List[AdditionalDocument]**](AdditionalDocument.md) |  | [optional] 
**buyer_accounting_reference** | **str** |  | [optional] 
**payment_card** | [**PaymentCard**](PaymentCard.md) |  | [optional] 

## Example

```python
from factpulse.models.factur_x_invoice import FacturXInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of FacturXInvoice from a JSON string
factur_x_invoice_instance = FacturXInvoice.from_json(json)
# print the JSON string representation of the object
print(FacturXInvoice.to_json())

# convert the object into a dict
factur_x_invoice_dict = factur_x_invoice_instance.to_dict()
# create an instance of FacturXInvoice from a dict
factur_x_invoice_from_dict = FacturXInvoice.from_dict(factur_x_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


