# DestinationChorusPro

Configuration spécifique pour la destination Chorus Pro.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'chorus_pro']
**credentials** | [**CredentialsChorusPro**](CredentialsChorusPro.md) |  | [optional] 

## Example

```python
from factpulse.models.destination_chorus_pro import DestinationChorusPro

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationChorusPro from a JSON string
destination_chorus_pro_instance = DestinationChorusPro.from_json(json)
# print the JSON string representation of the object
print(DestinationChorusPro.to_json())

# convert the object into a dict
destination_chorus_pro_dict = destination_chorus_pro_instance.to_dict()
# create an instance of DestinationChorusPro from a dict
destination_chorus_pro_from_dict = DestinationChorusPro.from_dict(destination_chorus_pro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


