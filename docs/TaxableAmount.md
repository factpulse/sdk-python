# TaxableAmount

VAT category taxable amount (BT-116). Can be negative for correction invoices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.taxable_amount import TaxableAmount

# TODO update the JSON string below
json = "{}"
# create an instance of TaxableAmount from a JSON string
taxable_amount_instance = TaxableAmount.from_json(json)
# print the JSON string representation of the object
print(TaxableAmount.to_json())

# convert the object into a dict
taxable_amount_dict = taxable_amount_instance.to_dict()
# create an instance of TaxableAmount from a dict
taxable_amount_from_dict = TaxableAmount.from_dict(taxable_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


