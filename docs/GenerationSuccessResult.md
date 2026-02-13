# GenerationSuccessResult

Successful result from task_generate_invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'SUCCESS']
**content_b64** | **str** |  | [optional] 
**xml_content** | **str** |  | [optional] 
**filename** | **str** |  | 

## Example

```python
from factpulse.models.generation_success_result import GenerationSuccessResult

# TODO update the JSON string below
json = "{}"
# create an instance of GenerationSuccessResult from a JSON string
generation_success_result_instance = GenerationSuccessResult.from_json(json)
# print the JSON string representation of the object
print(GenerationSuccessResult.to_json())

# convert the object into a dict
generation_success_result_dict = generation_success_result_instance.to_dict()
# create an instance of GenerationSuccessResult from a dict
generation_success_result_from_dict = GenerationSuccessResult.from_dict(generation_success_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


