# InvoiceReferences

Contains various invoice references (currency, type, etc.).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_currency** | **str** |  | [optional] [default to 'EUR']
**payment_means** | [**PaymentMeans**](PaymentMeans.md) |  | 
**invoice_type** | [**InvoiceTypeCode**](InvoiceTypeCode.md) |  | 
**vat_accounting_code** | [**VATAccountingCode**](VATAccountingCode.md) |  | 
**contract_reference** | **str** |  | [optional] 
**vat_exemption_reason** | **str** |  | [optional] 
**purchase_order_reference** | **str** |  | [optional] 
**preceding_invoice_reference** | **str** |  | [optional] 

## Example

```python
from factpulse.models.invoice_references import InvoiceReferences

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReferences from a JSON string
invoice_references_instance = InvoiceReferences.from_json(json)
# print the JSON string representation of the object
print(InvoiceReferences.to_json())

# convert the object into a dict
invoice_references_dict = invoice_references_instance.to_dict()
# create an instance of InvoiceReferences from a dict
invoice_references_from_dict = InvoiceReferences.from_dict(invoice_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


