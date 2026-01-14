# AFNORAddressRead

Wrapper for postal addresses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | Corresponds to the address of the recipient structure having defined the directory line(s). | [optional] 
**address_line2** | **str** | Corresponds to the address of the recipient structure having defined the directory line(s). | [optional] 
**address_line3** | **str** | Corresponds to the address of the recipient structure having defined the directory line(s). | [optional] 
**postal_code** | **str** | Service postal code | [optional] 
**country_subdivision** | **str** | Subdivision of the country | [optional] 
**locality** | **str** | Municipality of the recipient structure having defined the directory line(s). | [optional] 
**country_code** | **str** | Corresponds to the country of the recipient structure. | [optional] 
**country_name** | **str** | Corresponds to the country of the recipient structure having defined the directory line(s). | [optional] 

## Example

```python
from factpulse.models.afnor_address_read import AFNORAddressRead

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORAddressRead from a JSON string
afnor_address_read_instance = AFNORAddressRead.from_json(json)
# print the JSON string representation of the object
print(AFNORAddressRead.to_json())

# convert the object into a dict
afnor_address_read_dict = afnor_address_read_instance.to_dict()
# create an instance of AFNORAddressRead from a dict
afnor_address_read_from_dict = AFNORAddressRead.from_dict(afnor_address_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


