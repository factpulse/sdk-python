# ChorusProDestination

Specific configuration for Chorus Pro destination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'chorus_pro']
**credentials** | [**FactureElectroniqueRestApiSchemasProcessingChorusProCredentials**](FactureElectroniqueRestApiSchemasProcessingChorusProCredentials.md) |  | [optional] 

## Example

```python
from factpulse.models.chorus_pro_destination import ChorusProDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ChorusProDestination from a JSON string
chorus_pro_destination_instance = ChorusProDestination.from_json(json)
# print the JSON string representation of the object
print(ChorusProDestination.to_json())

# convert the object into a dict
chorus_pro_destination_dict = chorus_pro_destination_instance.to_dict()
# create an instance of ChorusProDestination from a dict
chorus_pro_destination_from_dict = ChorusProDestination.from_dict(chorus_pro_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


