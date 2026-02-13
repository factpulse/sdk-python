# VerificationSuccessTaskResult

Successful result from task_verify_pdf.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'SUCCESS']
**verification_result** | [**VerificationSuccessResponse**](VerificationSuccessResponse.md) |  | 

## Example

```python
from factpulse.models.verification_success_task_result import VerificationSuccessTaskResult

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationSuccessTaskResult from a JSON string
verification_success_task_result_instance = VerificationSuccessTaskResult.from_json(json)
# print the JSON string representation of the object
print(VerificationSuccessTaskResult.to_json())

# convert the object into a dict
verification_success_task_result_dict = verification_success_task_result_instance.to_dict()
# create an instance of VerificationSuccessTaskResult from a dict
verification_success_task_result_from_dict = VerificationSuccessTaskResult.from_dict(verification_success_task_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


