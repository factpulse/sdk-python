# TaskStatus

Complete description of an async task status.  The `status` field indicates the Celery state of the task. When `status=\"SUCCESS\"`, check `result.status` for the business result (\"SUCCESS\" or \"ERROR\").

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Unique task identifier | 
**status** | [**CeleryStatus**](CeleryStatus.md) | Celery task status (PENDING, STARTED, SUCCESS, FAILURE, RETRY) | 
**result** | **Dict[str, object]** |  | [optional] 

## Example

```python
from factpulse.models.task_status import TaskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatus from a JSON string
task_status_instance = TaskStatus.from_json(json)
# print the JSON string representation of the object
print(TaskStatus.to_json())

# convert the object into a dict
task_status_dict = task_status_instance.to_dict()
# create an instance of TaskStatus from a dict
task_status_from_dict = TaskStatus.from_dict(task_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


