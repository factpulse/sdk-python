# StatusCodesResponse

Liste des codes statut disponibles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codes** | [**List[StatusCodeInfo]**](StatusCodeInfo.md) | Liste des codes statut | 
**count** | **int** | Nombre de codes | 
**source** | **str** | Règle source | [optional] [default to 'BR-FR-CDV-CL-06']

## Example

```python
from factpulse.models.status_codes_response import StatusCodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCodesResponse from a JSON string
status_codes_response_instance = StatusCodesResponse.from_json(json)
# print the JSON string representation of the object
print(StatusCodesResponse.to_json())

# convert the object into a dict
status_codes_response_dict = status_codes_response_instance.to_dict()
# create an instance of StatusCodesResponse from a dict
status_codes_response_from_dict = StatusCodesResponse.from_dict(status_codes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


