# ClientUpdateRequest

Partial client update request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**siret** | **str** |  | [optional] 

## Example

```python
from factpulse.models.client_update_request import ClientUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUpdateRequest from a JSON string
client_update_request_instance = ClientUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ClientUpdateRequest.to_json())

# convert the object into a dict
client_update_request_dict = client_update_request_instance.to_dict()
# create an instance of ClientUpdateRequest from a dict
client_update_request_from_dict = ClientUpdateRequest.from_dict(client_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


