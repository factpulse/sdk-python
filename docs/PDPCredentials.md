# PDPCredentials

PDP credentials for zero-storage strategy (Strategy B).  Allows providing PDP credentials directly in the request instead of storing them in Django.  Useful for: - Ad-hoc tests without persisting credentials - Temporary integrations - Development environments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_service_url** | **str** | Base URL of the AFNOR Flow Service | 
**directory_service_url** | **str** |  | [optional] 
**token_url** | **str** | OAuth2 server URL | 
**client_id** | **str** | OAuth2 Client ID | 
**client_secret** | **str** | OAuth2 Client Secret (sensitive) | 

## Example

```python
from factpulse.models.pdp_credentials import PDPCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of PDPCredentials from a JSON string
pdp_credentials_instance = PDPCredentials.from_json(json)
# print the JSON string representation of the object
print(PDPCredentials.to_json())

# convert the object into a dict
pdp_credentials_dict = pdp_credentials_instance.to_dict()
# create an instance of PDPCredentials from a dict
pdp_credentials_from_dict = PDPCredentials.from_dict(pdp_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


