# GenerationTaskStatus

Typed task status for invoice generation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**status** | [**CeleryStatus**](CeleryStatus.md) |  | 
**result** | [**GenerationTaskStatusResult**](GenerationTaskStatusResult.md) |  | [optional] 

## Example

```python
from factpulse.models.generation_task_status import GenerationTaskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GenerationTaskStatus from a JSON string
generation_task_status_instance = GenerationTaskStatus.from_json(json)
# print the JSON string representation of the object
print(GenerationTaskStatus.to_json())

# convert the object into a dict
generation_task_status_dict = generation_task_status_instance.to_dict()
# create an instance of GenerationTaskStatus from a dict
generation_task_status_from_dict = GenerationTaskStatus.from_dict(generation_task_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


