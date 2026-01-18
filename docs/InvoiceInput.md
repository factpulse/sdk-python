# InvoiceInput

Invoice for B2B international reporting (flux 10.1).  Used for unitary declaration of international B2B invoices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Invoice identifier | 
**issue_date** | **date** | Invoice issue date | 
**type_code** | [**InvoiceTypeCode**](InvoiceTypeCode.md) | Invoice type code | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**due_date** | **date** |  | [optional] 
**seller_siren** | **str** | Seller SIREN/SIRET | 
**seller_vat_id** | **str** |  | [optional] 
**seller_country** | [**Sellercountry**](Sellercountry.md) |  | [optional] 
**buyer_id** | **str** |  | [optional] 
**buyer_vat_id** | **str** |  | [optional] 
**buyer_country** | [**Buyercountry**](Buyercountry.md) |  | 
**tax_exclusive_amount** | [**Taxexclusiveamount1**](Taxexclusiveamount1.md) |  | 
**tax_amount** | [**Taxamount1**](Taxamount1.md) |  | 
**tax_breakdown** | [**List[TaxBreakdownInput]**](TaxBreakdownInput.md) | VAT breakdown | 
**referenced_invoice_id** | **str** |  | [optional] 
**referenced_invoice_date** | **date** |  | [optional] 

## Example

```python
from factpulse.models.invoice_input import InvoiceInput

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceInput from a JSON string
invoice_input_instance = InvoiceInput.from_json(json)
# print the JSON string representation of the object
print(InvoiceInput.to_json())

# convert the object into a dict
invoice_input_dict = invoice_input_instance.to_dict()
# create an instance of InvoiceInput from a dict
invoice_input_from_dict = InvoiceInput.from_dict(invoice_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


