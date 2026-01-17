# ReasonCodesResponse

Liste des codes motif disponibles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codes** | [**List[ReasonCodeInfo]**](ReasonCodeInfo.md) | Liste des codes motif | 
**count** | **int** | Nombre de codes | 
**source** | **str** | Règle source | [optional] [default to 'BR-FR-CDV-CL-09']

## Example

```python
from factpulse.models.reason_codes_response import ReasonCodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReasonCodesResponse from a JSON string
reason_codes_response_instance = ReasonCodesResponse.from_json(json)
# print the JSON string representation of the object
print(ReasonCodesResponse.to_json())

# convert the object into a dict
reason_codes_response_dict = reason_codes_response_instance.to_dict()
# create an instance of ReasonCodesResponse from a dict
reason_codes_response_from_dict = ReasonCodesResponse.from_dict(reason_codes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


