# AsyncTaskStatus

Complete description of an async task status.  The `status` field indicates the Celery state of the task. When `status=\"SUCCESS\"`, check `result.status` for the business result (\"SUCCESS\" or \"ERROR\").

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Unique task identifier | 
**status** | [**CeleryStatus**](CeleryStatus.md) | Celery task status (PENDING, STARTED, SUCCESS, FAILURE, RETRY) | 
**result** | **Dict[str, object]** |  | [optional] 

## Example

```python
from factpulse.models.async_task_status import AsyncTaskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncTaskStatus from a JSON string
async_task_status_instance = AsyncTaskStatus.from_json(json)
# print the JSON string representation of the object
print(AsyncTaskStatus.to_json())

# convert the object into a dict
async_task_status_dict = async_task_status_instance.to_dict()
# create an instance of AsyncTaskStatus from a dict
async_task_status_from_dict = AsyncTaskStatus.from_dict(async_task_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


