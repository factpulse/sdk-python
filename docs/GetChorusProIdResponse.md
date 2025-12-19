# GetChorusProIdResponse

Found Chorus Pro ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**structure_id** | **int** | Chorus Pro ID (0 if not found) | 
**structure_identifier** | **str** | Searched SIRET/SIREN | 
**structure_name** | **str** |  | [optional] 
**message** | **str** | Return message | 

## Example

```python
from factpulse.models.get_chorus_pro_id_response import GetChorusProIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChorusProIdResponse from a JSON string
get_chorus_pro_id_response_instance = GetChorusProIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetChorusProIdResponse.to_json())

# convert the object into a dict
get_chorus_pro_id_response_dict = get_chorus_pro_id_response_instance.to_dict()
# create an instance of GetChorusProIdResponse from a dict
get_chorus_pro_id_response_from_dict = GetChorusProIdResponse.from_dict(get_chorus_pro_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


