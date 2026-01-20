# ClientActivateResponse

Client activation/deactivation response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **UUID** | Unique client identifier | 
**is_active** | **bool** | New status | 
**message** | **str** | Confirmation message | 

## Example

```python
from factpulse.models.client_activate_response import ClientActivateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientActivateResponse from a JSON string
client_activate_response_instance = ClientActivateResponse.from_json(json)
# print the JSON string representation of the object
print(ClientActivateResponse.to_json())

# convert the object into a dict
client_activate_response_dict = client_activate_response_instance.to_dict()
# create an instance of ClientActivateResponse from a dict
client_activate_response_from_dict = ClientActivateResponse.from_dict(client_activate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


