# ValidationSuccessResponse

Response for successful validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message confirming XML compliance. | 

## Example

```python
from factpulse.models.validation_success_response import ValidationSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationSuccessResponse from a JSON string
validation_success_response_instance = ValidationSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(ValidationSuccessResponse.to_json())

# convert the object into a dict
validation_success_response_dict = validation_success_response_instance.to_dict()
# create an instance of ValidationSuccessResponse from a dict
validation_success_response_from_dict = ValidationSuccessResponse.from_dict(validation_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


