# VatRate

VAT rate applicable to this allowance/charge (BT-96/103).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.vat_rate import VatRate

# TODO update the JSON string below
json = "{}"
# create an instance of VatRate from a JSON string
vat_rate_instance = VatRate.from_json(json)
# print the JSON string representation of the object
print(VatRate.to_json())

# convert the object into a dict
vat_rate_dict = vat_rate_instance.to_dict()
# create an instance of VatRate from a dict
vat_rate_from_dict = VatRate.from_dict(vat_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


