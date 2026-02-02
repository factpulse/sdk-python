# PDPConfigResponse

PDP configuration (secrets masked).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_configured** | **bool** | Whether PDP config exists | 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**mode_sandbox** | **bool** |  | [optional] 
**flow_service_url** | **str** |  | [optional] 
**token_url** | **str** |  | [optional] 
**oauth_client_id** | **str** |  | [optional] 
**encryption_mode** | **str** |  | [optional] 
**secret_status** | [**SecretStatus**](SecretStatus.md) |  | [optional] 
**last_test_at** | **datetime** |  | [optional] 
**last_test_success** | **bool** |  | [optional] 
**last_test_error** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from factpulse.models.pdp_config_response import PDPConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PDPConfigResponse from a JSON string
pdp_config_response_instance = PDPConfigResponse.from_json(json)
# print the JSON string representation of the object
print(PDPConfigResponse.to_json())

# convert the object into a dict
pdp_config_response_dict = pdp_config_response_instance.to_dict()
# create an instance of PDPConfigResponse from a dict
pdp_config_response_from_dict = PDPConfigResponse.from_dict(pdp_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


