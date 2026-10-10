# SuperPDPStatusResponse

SuperPDP connection status for a client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | **bool** | Whether this client has connected its SuperPDP account | 
**connected_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**mode_sandbox** | **bool** |  | [optional] 
**last_error** | **str** | Last token refresh error, if any | [optional] [default to '']

## Example

```python
from factpulse.models.super_pdp_status_response import SuperPDPStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuperPDPStatusResponse from a JSON string
super_pdp_status_response_instance = SuperPDPStatusResponse.from_json(json)
# print the JSON string representation of the object
print(SuperPDPStatusResponse.to_json())

# convert the object into a dict
super_pdp_status_response_dict = super_pdp_status_response_instance.to_dict()
# create an instance of SuperPDPStatusResponse from a dict
super_pdp_status_response_from_dict = SuperPDPStatusResponse.from_dict(super_pdp_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


