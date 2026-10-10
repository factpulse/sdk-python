# ElectronicAddressInput

Represents an electronic invoicing address, composed of an identifier and its scheme (SchemeID) in accordance with EN16931. Example: { \"identifier\": \"123456789\", \"scheme_id\": \"0225\" }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Electronic address identifier (e.g., SIREN, SIRET, routing code) | 
**scheme_id** | [**SchemeID**](SchemeID.md) | Identification scheme (EAS code) | [optional] 

## Example

```python
from factpulse.models.electronic_address_input import ElectronicAddressInput

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicAddressInput from a JSON string
electronic_address_input_instance = ElectronicAddressInput.from_json(json)
# print the JSON string representation of the object
print(ElectronicAddressInput.to_json())

# convert the object into a dict
electronic_address_input_dict = electronic_address_input_instance.to_dict()
# create an instance of ElectronicAddressInput from a dict
electronic_address_input_from_dict = ElectronicAddressInput.from_dict(electronic_address_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


