# TaskErrorResult

Common error result returned by all task domains.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'ERROR']
**error_code** | **str** |  | 
**error_message** | **str** |  | 
**details** | [**List[AFNORErrorDetail]**](AFNORErrorDetail.md) |  | [optional] 
**traceback** | **str** |  | [optional] 

## Example

```python
from factpulse.models.task_error_result import TaskErrorResult

# TODO update the JSON string below
json = "{}"
# create an instance of TaskErrorResult from a JSON string
task_error_result_instance = TaskErrorResult.from_json(json)
# print the JSON string representation of the object
print(TaskErrorResult.to_json())

# convert the object into a dict
task_error_result_dict = task_error_result_instance.to_dict()
# create an instance of TaskErrorResult from a dict
task_error_result_from_dict = TaskErrorResult.from_dict(task_error_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


