# TotalVATAmount

Invoice total VAT amount (BT-110). Can be negative for correction invoices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.total_vat_amount import TotalVATAmount

# TODO update the JSON string below
json = "{}"
# create an instance of TotalVATAmount from a JSON string
total_vat_amount_instance = TotalVATAmount.from_json(json)
# print the JSON string representation of the object
print(TotalVATAmount.to_json())

# convert the object into a dict
total_vat_amount_dict = total_vat_amount_instance.to_dict()
# create an instance of TotalVATAmount from a dict
total_vat_amount_from_dict = TotalVATAmount.from_dict(total_vat_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


