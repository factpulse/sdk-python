# ActionCodesResponse

Liste des codes action disponibles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codes** | [**List[ActionCodeInfo]**](ActionCodeInfo.md) | Liste des codes action | 
**count** | **int** | Nombre de codes | 
**source** | **str** | Règle source | [optional] [default to 'BR-FR-CDV-CL-10']

## Example

```python
from factpulse.models.action_codes_response import ActionCodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionCodesResponse from a JSON string
action_codes_response_instance = ActionCodesResponse.from_json(json)
# print the JSON string representation of the object
print(ActionCodesResponse.to_json())

# convert the object into a dict
action_codes_response_dict = action_codes_response_instance.to_dict()
# create an instance of ActionCodesResponse from a dict
action_codes_response_from_dict = ActionCodesResponse.from_dict(action_codes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


