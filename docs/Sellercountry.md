# Sellercountry

Seller country code (ISO 3166-1 alpha-2). See CountryCode enum for valid values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.sellercountry import Sellercountry

# TODO update the JSON string below
json = "{}"
# create an instance of Sellercountry from a JSON string
sellercountry_instance = Sellercountry.from_json(json)
# print the JSON string representation of the object
print(Sellercountry.to_json())

# convert the object into a dict
sellercountry_dict = sellercountry_instance.to_dict()
# create an instance of Sellercountry from a dict
sellercountry_from_dict = Sellercountry.from_dict(sellercountry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


