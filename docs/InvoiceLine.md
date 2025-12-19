# InvoiceLine

Represents a line item in an invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** |  | 
**reference** | **str** |  | [optional] 
**item_name** | **str** |  | 
**quantity** | [**Quantity**](Quantity.md) |  | 
**unit** | [**UnitOfMeasure**](UnitOfMeasure.md) |  | 
**unit_net_price** | [**UnitNetPrice**](UnitNetPrice.md) |  | 
**allowance_amount** | [**InvoiceLineAllowanceAmount**](InvoiceLineAllowanceAmount.md) |  | [optional] 
**line_net_amount** | [**LineNetAmount**](LineNetAmount.md) |  | [optional] 
**vat_rate** | **str** |  | [optional] 
**manual_vat_rate** | [**ManualVatRate**](ManualVatRate.md) |  | [optional] 
**vat_category** | [**VATCategory**](VATCategory.md) |  | [optional] 
**period_start_date** | **str** |  | [optional] 
**period_end_date** | **str** |  | [optional] 
**allowance_reason_code** | [**AllowanceReasonCode**](AllowanceReasonCode.md) |  | [optional] 
**allowance_reason** | **str** |  | [optional] 

## Example

```python
from factpulse.models.invoice_line import InvoiceLine

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLine from a JSON string
invoice_line_instance = InvoiceLine.from_json(json)
# print the JSON string representation of the object
print(InvoiceLine.to_json())

# convert the object into a dict
invoice_line_dict = invoice_line_instance.to_dict()
# create an instance of InvoiceLine from a dict
invoice_line_from_dict = InvoiceLine.from_dict(invoice_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


