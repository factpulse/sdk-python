# InvoiceTotalsPrepayment

Sum of amounts already paid (BT-113). Can be negative for correction invoices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.invoice_totals_prepayment import InvoiceTotalsPrepayment

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceTotalsPrepayment from a JSON string
invoice_totals_prepayment_instance = InvoiceTotalsPrepayment.from_json(json)
# print the JSON string representation of the object
print(InvoiceTotalsPrepayment.to_json())

# convert the object into a dict
invoice_totals_prepayment_dict = invoice_totals_prepayment_instance.to_dict()
# create an instance of InvoiceTotalsPrepayment from a dict
invoice_totals_prepayment_from_dict = InvoiceTotalsPrepayment.from_dict(invoice_totals_prepayment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


