# SecretStatus

Secret status (never exposes the secret itself).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Secret status: &#39;active&#39;, &#39;missing&#39;, etc. | 
**message** | **str** | Descriptive status message | 
**encryption_mode** | **str** |  | [optional] 
**requires_client_key** | **bool** |  | [optional] 

## Example

```python
from factpulse.models.secret_status import SecretStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SecretStatus from a JSON string
secret_status_instance = SecretStatus.from_json(json)
# print the JSON string representation of the object
print(SecretStatus.to_json())

# convert the object into a dict
secret_status_dict = secret_status_instance.to_dict()
# create an instance of SecretStatus from a dict
secret_status_from_dict = SecretStatus.from_dict(secret_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


