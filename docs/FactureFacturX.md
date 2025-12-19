# FactureFacturX

Data model for an invoice to be converted to Factur-X.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** |  | 
**payment_due_date** | **str** |  | 
**invoice_date** | **str** |  | [optional] 
**submission_mode** | [**SubmissionMode**](SubmissionMode.md) |  | 
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

## Example

```python
from factpulse.models.facture_factur_x import FactureFacturX

# TODO update the JSON string below
json = "{}"
# create an instance of FactureFacturX from a JSON string
facture_factur_x_instance = FactureFacturX.from_json(json)
# print the JSON string representation of the object
print(FactureFacturX.to_json())

# convert the object into a dict
facture_factur_x_dict = facture_factur_x_instance.to_dict()
# create an instance of FactureFacturX from a dict
facture_factur_x_from_dict = FactureFacturX.from_dict(facture_factur_x_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


