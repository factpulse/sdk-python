# AFNORAddressPut

Wrapper for postal addresses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ligne_adresse1** | **str** | Corresponds to the address of the recipient structure having defined the directory line(s). | 
**ligne_adresse2** | **str** | Corresponds to the address of the recipient structure having defined the directory line(s). | 
**ligne_adresse3** | **str** | Corresponds to the address of the recipient structure having defined the directory line(s). | 
**postal_code** | **str** | Service postal code | 
**country_subdivision** | **str** | Subdivision of the country | 
**locality** | **str** | Corresponds to the municipality of the recipient structure having defined the directory line(s). | 
**code_pays** | **str** | Corresponds to the country code of the recipient structure | 

## Example

```python
from factpulse.models.afnor_address_put import AFNORAddressPut

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORAddressPut from a JSON string
afnor_address_put_instance = AFNORAddressPut.from_json(json)
# print the JSON string representation of the object
print(AFNORAddressPut.to_json())

# convert the object into a dict
afnor_address_put_dict = afnor_address_put_instance.to_dict()
# create an instance of AFNORAddressPut from a dict
afnor_address_put_from_dict = AFNORAddressPut.from_dict(afnor_address_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


