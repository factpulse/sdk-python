# ValidationTaskStatus

Typed task status for Factur-X validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**status** | [**CeleryStatus**](CeleryStatus.md) |  | 
**result** | [**ValidationTaskStatusResult**](ValidationTaskStatusResult.md) |  | [optional] 

## Example

```python
from factpulse.models.validation_task_status import ValidationTaskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationTaskStatus from a JSON string
validation_task_status_instance = ValidationTaskStatus.from_json(json)
# print the JSON string representation of the object
print(ValidationTaskStatus.to_json())

# convert the object into a dict
validation_task_status_dict = validation_task_status_instance.to_dict()
# create an instance of ValidationTaskStatus from a dict
validation_task_status_from_dict = ValidationTaskStatus.from_dict(validation_task_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


