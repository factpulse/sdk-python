# InvoiceLineAllowanceAmount

Allowance amount before tax. (Accepte number, string ou integer)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.invoice_line_allowance_amount import InvoiceLineAllowanceAmount

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineAllowanceAmount from a JSON string
invoice_line_allowance_amount_instance = InvoiceLineAllowanceAmount.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineAllowanceAmount.to_json())

# convert the object into a dict
invoice_line_allowance_amount_dict = invoice_line_allowance_amount_instance.to_dict()
# create an instance of InvoiceLineAllowanceAmount from a dict
invoice_line_allowance_amount_from_dict = InvoiceLineAllowanceAmount.from_dict(invoice_line_allowance_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


