# GenerationTaskStatusResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'ERROR']
**content_b64** | **str** |  | [optional] 
**xml_content** | **str** |  | [optional] 
**filename** | **str** |  | 
**error_code** | **str** |  | 
**error_message** | **str** |  | 
**details** | [**List[AFNORErrorDetail]**](AFNORErrorDetail.md) |  | [optional] 
**traceback** | **str** |  | [optional] 

## Example

```python
from factpulse.models.generation_task_status_result import GenerationTaskStatusResult

# TODO update the JSON string below
json = "{}"
# create an instance of GenerationTaskStatusResult from a JSON string
generation_task_status_result_instance = GenerationTaskStatusResult.from_json(json)
# print the JSON string representation of the object
print(GenerationTaskStatusResult.to_json())

# convert the object into a dict
generation_task_status_result_dict = generation_task_status_result_instance.to_dict()
# create an instance of GenerationTaskStatusResult from a dict
generation_task_status_result_from_dict = GenerationTaskStatusResult.from_dict(generation_task_status_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


