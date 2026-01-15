# AFNORAddressPatch

Wrapper for postal addresses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ligne_adresse1** | **str** | Corresponds to the address of the recipient structure having defined the directory line(s). | [optional] 
**ligne_adresse2** | **str** | Corresponds to the address of the recipient structure having defined the directory line(s). | [optional] 
**ligne_adresse3** | **str** | Corresponds to the address of the recipient structure having defined the directory line(s). | [optional] 
**postal_code** | **str** | Service postal code | [optional] 
**country_subdivision** | **str** | Subdivision of the country | [optional] 
**locality** | **str** | Corresponds to the municipality of the recipient structure having defined the directory line(s). | [optional] 
**code_pays** | **str** | Corresponds to the country code of the recipient structure | [optional] 

## Example

```python
from factpulse.models.afnor_address_patch import AFNORAddressPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORAddressPatch from a JSON string
afnor_address_patch_instance = AFNORAddressPatch.from_json(json)
# print the JSON string representation of the object
print(AFNORAddressPatch.to_json())

# convert the object into a dict
afnor_address_patch_dict = afnor_address_patch_instance.to_dict()
# create an instance of AFNORAddressPatch from a dict
afnor_address_patch_from_dict = AFNORAddressPatch.from_dict(afnor_address_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


