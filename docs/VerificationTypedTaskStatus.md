# VerificationTypedTaskStatus

Typed task status for PDF/XML verification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**status** | [**CeleryStatus**](CeleryStatus.md) |  | 
**result** | [**VerificationTypedTaskStatusResult**](VerificationTypedTaskStatusResult.md) |  | [optional] 

## Example

```python
from factpulse.models.verification_typed_task_status import VerificationTypedTaskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationTypedTaskStatus from a JSON string
verification_typed_task_status_instance = VerificationTypedTaskStatus.from_json(json)
# print the JSON string representation of the object
print(VerificationTypedTaskStatus.to_json())

# convert the object into a dict
verification_typed_task_status_dict = verification_typed_task_status_instance.to_dict()
# create an instance of VerificationTypedTaskStatus from a dict
verification_typed_task_status_from_dict = VerificationTypedTaskStatus.from_dict(verification_typed_task_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


