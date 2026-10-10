# PostalAddressInput

Represents a postal address (BG-5, BG-8, BG-12, BG-15).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_code** | **str** |  | [optional] 
**line_one** | **str** |  | [optional] 
**line_two** | **str** |  | [optional] 
**line_three** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**country_subdivision** | **str** |  | [optional] 

## Example

```python
from factpulse.models.postal_address_input import PostalAddressInput

# TODO update the JSON string below
json = "{}"
# create an instance of PostalAddressInput from a JSON string
postal_address_input_instance = PostalAddressInput.from_json(json)
# print the JSON string representation of the object
print(PostalAddressInput.to_json())

# convert the object into a dict
postal_address_input_dict = postal_address_input_instance.to_dict()
# create an instance of PostalAddressInput from a dict
postal_address_input_from_dict = PostalAddressInput.from_dict(postal_address_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


