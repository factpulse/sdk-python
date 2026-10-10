# SuperPDPDisconnectResponse

Response after disconnecting SuperPDP for a client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the disconnection completed successfully | 
**deleted** | **bool** | Whether a SuperPDP connection existed and was removed | 

## Example

```python
from factpulse.models.super_pdp_disconnect_response import SuperPDPDisconnectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuperPDPDisconnectResponse from a JSON string
super_pdp_disconnect_response_instance = SuperPDPDisconnectResponse.from_json(json)
# print the JSON string representation of the object
print(SuperPDPDisconnectResponse.to_json())

# convert the object into a dict
super_pdp_disconnect_response_dict = super_pdp_disconnect_response_instance.to_dict()
# create an instance of SuperPDPDisconnectResponse from a dict
super_pdp_disconnect_response_from_dict = SuperPDPDisconnectResponse.from_dict(super_pdp_disconnect_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


