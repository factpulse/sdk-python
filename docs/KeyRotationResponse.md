# KeyRotationResponse

Response from key rotation operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether rotation was successful | 
**message** | **str** | Result message | 
**rotated_count** | **int** | Number of secrets that were rotated | 
**partial_errors** | **List[str]** |  | [optional] 

## Example

```python
from factpulse.models.key_rotation_response import KeyRotationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KeyRotationResponse from a JSON string
key_rotation_response_instance = KeyRotationResponse.from_json(json)
# print the JSON string representation of the object
print(KeyRotationResponse.to_json())

# convert the object into a dict
key_rotation_response_dict = key_rotation_response_instance.to_dict()
# create an instance of KeyRotationResponse from a dict
key_rotation_response_from_dict = KeyRotationResponse.from_dict(key_rotation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


