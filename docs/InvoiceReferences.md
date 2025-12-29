# InvoiceReferences

Contains various invoice references (currency, type, etc.).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_process_id** | **str** |  | [optional] 
**invoice_currency** | **str** | Invoice currency code (BT-5). ISO 4217. | [optional] [default to 'EUR']
**payment_means** | [**PaymentMeans**](PaymentMeans.md) | Payment means type code (BT-81). | 
**payment_means_text** | **str** |  | [optional] 
**invoice_type** | [**InvoiceTypeCode**](InvoiceTypeCode.md) |  | 
**vat_accounting_code** | [**VATAccountingCode**](VATAccountingCode.md) | VAT accounting code. | 
**buyer_reference** | **str** |  | [optional] 
**contract_reference** | **str** |  | [optional] 
**purchase_order_reference** | **str** |  | [optional] 
**seller_order_reference** | **str** |  | [optional] 
**receiving_advice_reference** | **str** |  | [optional] 
**despatch_advice_reference** | **str** |  | [optional] 
**tender_reference** | **str** |  | [optional] 
**preceding_invoice_reference** | **str** |  | [optional] 
**preceding_invoice_date** | **str** |  | [optional] 
**project_reference** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**vat_exemption_reason** | **str** |  | [optional] 

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


