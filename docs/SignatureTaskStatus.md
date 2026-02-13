# SignatureTaskStatus

Typed task status for PDF signing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**status** | [**CeleryStatus**](CeleryStatus.md) |  | 
**result** | [**SignatureTaskStatusResult**](SignatureTaskStatusResult.md) |  | [optional] 

## Example

```python
from factpulse.models.signature_task_status import SignatureTaskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureTaskStatus from a JSON string
signature_task_status_instance = SignatureTaskStatus.from_json(json)
# print the JSON string representation of the object
print(SignatureTaskStatus.to_json())

# convert the object into a dict
signature_task_status_dict = signature_task_status_instance.to_dict()
# create an instance of SignatureTaskStatus from a dict
signature_task_status_from_dict = SignatureTaskStatus.from_dict(signature_task_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


