# GetChorusProIdRequest

Get Chorus Pro ID from SIRET.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ChorusProCredentials**](ChorusProCredentials.md) |  | [optional] 
**siret** | **str** | Structure SIRET (14 digits) | 
**identifier_type** | **str** | Identifier type (SIRET, SIREN, UE_HORS_FRANCE, etc.) | [optional] [default to 'SIRET']

## Example

```python
from factpulse.models.get_chorus_pro_id_request import GetChorusProIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetChorusProIdRequest from a JSON string
get_chorus_pro_id_request_instance = GetChorusProIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetChorusProIdRequest.to_json())

# convert the object into a dict
get_chorus_pro_id_request_dict = get_chorus_pro_id_request_instance.to_dict()
# create an instance of GetChorusProIdRequest from a dict
get_chorus_pro_id_request_from_dict = GetChorusProIdRequest.from_dict(get_chorus_pro_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


