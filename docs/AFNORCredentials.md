# AFNORCredentials

Optional AFNOR PDP credentials.  **MODE 1 - JWT retrieval (recommended):** Do not provide this `credentials` field in the payload. PDP credentials will be automatically retrieved via client_uid from JWT (0-trust).  **MODE 2 - Credentials in payload (zero-storage):** Provide all required fields below. Useful for tests or third-party integrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**flow_service_url** | **str** |  | [optional] 

## Example

```python
from factpulse.models.afnor_credentials import AFNORCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORCredentials from a JSON string
afnor_credentials_instance = AFNORCredentials.from_json(json)
# print the JSON string representation of the object
print(AFNORCredentials.to_json())

# convert the object into a dict
afnor_credentials_dict = afnor_credentials_instance.to_dict()
# create an instance of AFNORCredentials from a dict
afnor_credentials_from_dict = AFNORCredentials.from_dict(afnor_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


