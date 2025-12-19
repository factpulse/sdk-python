# VATAmount

VAT amount for this line. (Accepte number, string ou integer)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.vat_amount import VATAmount

# TODO update the JSON string below
json = "{}"
# create an instance of VATAmount from a JSON string
vat_amount_instance = VATAmount.from_json(json)
# print the JSON string representation of the object
print(VATAmount.to_json())

# convert the object into a dict
vat_amount_dict = vat_amount_instance.to_dict()
# create an instance of VATAmount from a dict
vat_amount_from_dict = VATAmount.from_dict(vat_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


