# PDPConfigUpdateRequest

PDP configuration update request.  For encryption_mode='double', the X-Encryption-Key header must also be provided containing a base64-encoded AES-256 key (32 bytes).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | Whether config is active | [optional] [default to True]
**mode_sandbox** | **bool** | Sandbox mode | [optional] [default to False]
**flow_service_url** | **str** | PDP Flow Service URL | 
**token_url** | **str** | PDP OAuth token URL | 
**oauth_client_id** | **str** | OAuth Client ID | 
**client_secret** | **str** | OAuth Client Secret (sent but never returned) | 
**encryption_mode** | **str** |  | [optional] 

## Example

```python
from factpulse.models.pdp_config_update_request import PDPConfigUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PDPConfigUpdateRequest from a JSON string
pdp_config_update_request_instance = PDPConfigUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PDPConfigUpdateRequest.to_json())

# convert the object into a dict
pdp_config_update_request_dict = pdp_config_update_request_instance.to_dict()
# create an instance of PDPConfigUpdateRequest from a dict
pdp_config_update_request_from_dict = PDPConfigUpdateRequest.from_dict(pdp_config_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


