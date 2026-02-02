# KeyRotationRequest

Request to rotate the client encryption key.  This operation re-encrypts all secrets from the old key to the new key. Both keys must be base64-encoded AES-256 keys (32 bytes each).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_key** | **str** | Current encryption key (base64-encoded AES-256) | 
**new_key** | **str** | New encryption key (base64-encoded AES-256) | 

## Example

```python
from factpulse.models.key_rotation_request import KeyRotationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KeyRotationRequest from a JSON string
key_rotation_request_instance = KeyRotationRequest.from_json(json)
# print the JSON string representation of the object
print(KeyRotationRequest.to_json())

# convert the object into a dict
key_rotation_request_dict = key_rotation_request_instance.to_dict()
# create an instance of KeyRotationRequest from a dict
key_rotation_request_from_dict = KeyRotationRequest.from_dict(key_rotation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


