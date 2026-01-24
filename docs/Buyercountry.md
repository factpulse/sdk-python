# Buyercountry

Buyer country code (ISO 3166-1 alpha-2). FR for Bi2B, other for B2Bi.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.buyercountry import Buyercountry

# TODO update the JSON string below
json = "{}"
# create an instance of Buyercountry from a JSON string
buyercountry_instance = Buyercountry.from_json(json)
# print the JSON string representation of the object
print(Buyercountry.to_json())

# convert the object into a dict
buyercountry_dict = buyercountry_instance.to_dict()
# create an instance of Buyercountry from a dict
buyercountry_from_dict = Buyercountry.from_dict(buyercountry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


