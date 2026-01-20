# ClientCreateRequest

Client creation request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Client name | 
**description** | **str** |  | [optional] 
**siret** | **str** |  | [optional] 

## Example

```python
from factpulse.models.client_create_request import ClientCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCreateRequest from a JSON string
client_create_request_instance = ClientCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ClientCreateRequest.to_json())

# convert the object into a dict
client_create_request_dict = client_create_request_instance.to_dict()
# create an instance of ClientCreateRequest from a dict
client_create_request_from_dict = ClientCreateRequest.from_dict(client_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


