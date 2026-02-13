# ConversionSuccessTaskResult

Successful result from task_convert_document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'SUCCESS']
**conversion_id** | **str** |  | 
**document_type_code** | **int** |  | 
**profile** | **str** |  | 
**extraction** | [**ConversionExtractionInfo**](ConversionExtractionInfo.md) |  | 
**processing_time_ms** | **int** |  | 
**pdf_regenerated** | **bool** |  | [optional] [default to False]
**pdf_regenerated_reason** | **str** |  | [optional] 
**content_b64** | **str** |  | [optional] 
**xml_content** | **str** |  | [optional] 

## Example

```python
from factpulse.models.conversion_success_task_result import ConversionSuccessTaskResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionSuccessTaskResult from a JSON string
conversion_success_task_result_instance = ConversionSuccessTaskResult.from_json(json)
# print the JSON string representation of the object
print(ConversionSuccessTaskResult.to_json())

# convert the object into a dict
conversion_success_task_result_dict = conversion_success_task_result_instance.to_dict()
# create an instance of ConversionSuccessTaskResult from a dict
conversion_success_task_result_from_dict = ConversionSuccessTaskResult.from_dict(conversion_success_task_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


