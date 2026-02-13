# VerificationTypedTaskStatusResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'ERROR']
**verification_result** | [**VerificationSuccessResponse**](VerificationSuccessResponse.md) |  | 
**error_code** | **str** |  | 
**error_message** | **str** |  | 
**details** | [**List[AFNORErrorDetail]**](AFNORErrorDetail.md) |  | [optional] 
**traceback** | **str** |  | [optional] 

## Example

```python
from factpulse.models.verification_typed_task_status_result import VerificationTypedTaskStatusResult

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationTypedTaskStatusResult from a JSON string
verification_typed_task_status_result_instance = VerificationTypedTaskStatusResult.from_json(json)
# print the JSON string representation of the object
print(VerificationTypedTaskStatusResult.to_json())

# convert the object into a dict
verification_typed_task_status_result_dict = verification_typed_task_status_result_instance.to_dict()
# create an instance of VerificationTypedTaskStatusResult from a dict
verification_typed_task_status_result_from_dict = VerificationTypedTaskStatusResult.from_dict(verification_typed_task_status_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


