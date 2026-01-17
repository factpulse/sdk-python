# SubmitCDARResponse

Réponse de soumission CDAR.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | Identifiant du flux AFNOR | 
**status** | **str** | Statut de la soumission | 
**message** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 

## Example

```python
from factpulse.models.submit_cdar_response import SubmitCDARResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitCDARResponse from a JSON string
submit_cdar_response_instance = SubmitCDARResponse.from_json(json)
# print the JSON string representation of the object
print(SubmitCDARResponse.to_json())

# convert the object into a dict
submit_cdar_response_dict = submit_cdar_response_instance.to_dict()
# create an instance of SubmitCDARResponse from a dict
submit_cdar_response_from_dict = SubmitCDARResponse.from_dict(submit_cdar_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


