# Invoicedata

Invoice data, in either of the two accepted formats (detected automatically, same rule as /generate-invoice): 1. **Simplified format**: `number` + `lines`, with auto-enrichment. Any field of the complete model may be added on top. 2. **Complete format**: full `FacturXInvoice` structure, recognised by the presence of `invoiceLines`. No auto-enrichment of totals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Unique invoice number | 
**supplier** | [**Supplier**](Supplier.md) |  | 
**recipient** | [**Recipient**](Recipient.md) |  | 
**lines** | **List[Dict[str, object]]** | Invoice lines | 
**var_date** | **str** |  | [optional] 
**due_days** | **int** | Due date in days (default: 30) | [optional] [default to 30]
**comment** | **str** |  | [optional] 
**purchase_order_reference** | **str** |  | [optional] 
**contract_reference** | **str** |  | [optional] 
**invoice_type** | [**FactureElectroniqueModelsInvoiceTypeCode**](FactureElectroniqueModelsInvoiceTypeCode.md) | Document type (UNTDID 1001). Default: 380 (Invoice). | [optional] 
**preceding_invoice_reference** | **str** |  | [optional] 
**operation_nature** | [**OperationNature**](OperationNature.md) |  | [optional] 
**invoicing_framework** | [**InvoicingFrameworkCode**](InvoicingFrameworkCode.md) |  | [optional] 
**invoice_number** | **str** |  | 
**payment_due_date** | **str** |  | 
**invoice_date** | **str** |  | [optional] 
**submission_mode** | [**SubmissionMode**](SubmissionMode.md) |  | [optional] 
**invoicing_framework** | [**InvoicingFramework**](InvoicingFramework.md) |  | [optional] 
**references** | [**InvoiceReferences**](InvoiceReferences.md) |  | 
**totals** | [**InvoiceTotals**](InvoiceTotals.md) |  | 
**invoice_lines** | [**List[InvoiceLine]**](InvoiceLine.md) |  | [optional] 
**vat_lines** | [**List[VATLine]**](VATLine.md) |  | [optional] 
**notes** | [**List[InvoiceNote]**](InvoiceNote.md) |  | [optional] 
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
from factpulse.models.invoicedata import Invoicedata

# TODO update the JSON string below
json = "{}"
# create an instance of Invoicedata from a JSON string
invoicedata_instance = Invoicedata.from_json(json)
# print the JSON string representation of the object
print(Invoicedata.to_json())

# convert the object into a dict
invoicedata_dict = invoicedata_instance.to_dict()
# create an instance of Invoicedata from a dict
invoicedata_from_dict = Invoicedata.from_dict(invoicedata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


