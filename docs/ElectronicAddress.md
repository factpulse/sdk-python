# ElectronicAddress

Represents an electronic invoicing address, composed of an identifier and its scheme (SchemeID) in accordance with EN16931. Example: { \"identifier\": \"123456789\", \"scheme_id\": \"0225\" }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**scheme_id** | [**SchemeID**](SchemeID.md) |  | [optional] 

## Example

```python
from factpulse.models.electronic_address import ElectronicAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicAddress from a JSON string
electronic_address_instance = ElectronicAddress.from_json(json)
# print the JSON string representation of the object
print(ElectronicAddress.to_json())

# convert the object into a dict
electronic_address_dict = electronic_address_instance.to_dict()
# create an instance of ElectronicAddress from a dict
electronic_address_from_dict = ElectronicAddress.from_dict(electronic_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


