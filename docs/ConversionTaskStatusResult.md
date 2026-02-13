# ConversionTaskStatusResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'ERROR']
**conversion_id** | **str** |  | 
**document_type_code** | **int** |  | 
**profile** | **str** |  | 
**extraction** | [**ConversionExtractionInfo**](ConversionExtractionInfo.md) |  | 
**processing_time_ms** | **int** |  | 
**pdf_regenerated** | **bool** |  | [optional] [default to False]
**pdf_regenerated_reason** | **str** |  | [optional] 
**content_b64** | **str** |  | [optional] 
**xml_content** | **str** |  | [optional] 
**message** | **str** |  | 
**missing_fields** | **List[str]** |  | 
**extracted_data** | **Dict[str, object]** |  | 
**confidence_score** | **float** |  | 
**validation_errors** | **List[Dict[str, object]]** |  | [optional] 
**correction_attempted** | **bool** |  | [optional] [default to False]
**error_code** | **str** |  | 
**error_message** | **str** |  | 
**details** | [**List[AFNORErrorDetail]**](AFNORErrorDetail.md) |  | [optional] 
**traceback** | **str** |  | [optional] 

## Example

```python
from factpulse.models.conversion_task_status_result import ConversionTaskStatusResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionTaskStatusResult from a JSON string
conversion_task_status_result_instance = ConversionTaskStatusResult.from_json(json)
# print the JSON string representation of the object
print(ConversionTaskStatusResult.to_json())

# convert the object into a dict
conversion_task_status_result_dict = conversion_task_status_result_instance.to_dict()
# create an instance of ConversionTaskStatusResult from a dict
conversion_task_status_result_from_dict = ConversionTaskStatusResult.from_dict(conversion_task_status_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


