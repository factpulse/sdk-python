# ManualVatRate

Line VAT rate percentage (BT-152). (Accepte number, string ou integer)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.manual_vat_rate import ManualVatRate

# TODO update the JSON string below
json = "{}"
# create an instance of ManualVatRate from a JSON string
manual_vat_rate_instance = ManualVatRate.from_json(json)
# print the JSON string representation of the object
print(ManualVatRate.to_json())

# convert the object into a dict
manual_vat_rate_dict = manual_vat_rate_instance.to_dict()
# create an instance of ManualVatRate from a dict
manual_vat_rate_from_dict = ManualVatRate.from_dict(manual_vat_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


