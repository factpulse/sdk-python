# InvoiceTotals

Contains all invoice total amounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_net_amount** | [**TotalNetAmount**](TotalNetAmount.md) |  | 
**vat_amount** | [**TotalVATAmount**](TotalVATAmount.md) |  | 
**total_gross_amount** | [**TotalGrossAmount**](TotalGrossAmount.md) |  | 
**amount_due** | [**AmountDue**](AmountDue.md) |  | 
**prepayment** | [**InvoiceTotalsPrepayment**](InvoiceTotalsPrepayment.md) |  | [optional] 
**global_allowance_amount** | [**GlobalAllowanceAmount**](GlobalAllowanceAmount.md) |  | [optional] 
**global_allowance_reason** | **str** |  | [optional] 

## Example

```python
from factpulse.models.invoice_totals import InvoiceTotals

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceTotals from a JSON string
invoice_totals_instance = InvoiceTotals.from_json(json)
# print the JSON string representation of the object
print(InvoiceTotals.to_json())

# convert the object into a dict
invoice_totals_dict = invoice_totals_instance.to_dict()
# create an instance of InvoiceTotals from a dict
invoice_totals_from_dict = InvoiceTotals.from_dict(invoice_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


