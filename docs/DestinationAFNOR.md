# DestinationAFNOR

Configuration spécifique pour la destination AFNOR PDP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'afnor']
**credentials** | [**CredentialsAFNOR**](CredentialsAFNOR.md) |  | [optional] 
**flow_syntax** | **str** | Syntaxe du flux à envoyer | [optional] [default to 'Factur-X']
**tracking_id** | **str** |  | [optional] 

## Example

```python
from factpulse.models.destination_afnor import DestinationAFNOR

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationAFNOR from a JSON string
destination_afnor_instance = DestinationAFNOR.from_json(json)
# print the JSON string representation of the object
print(DestinationAFNOR.to_json())

# convert the object into a dict
destination_afnor_dict = destination_afnor_instance.to_dict()
# create an instance of DestinationAFNOR from a dict
destination_afnor_from_dict = DestinationAFNOR.from_dict(destination_afnor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


