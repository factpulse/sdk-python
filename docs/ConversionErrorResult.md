# ConversionErrorResult

Error result specific to conversion tasks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'ERROR']
**conversion_id** | **str** |  | [optional] 
**error_code** | **str** |  | 
**error_message** | **str** |  | 
**details** | [**List[AFNORErrorDetail]**](AFNORErrorDetail.md) |  | [optional] 
**traceback** | **str** |  | [optional] 
**processing_time_ms** | **int** |  | [optional] 

## Example

```python
from factpulse.models.conversion_error_result import ConversionErrorResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionErrorResult from a JSON string
conversion_error_result_instance = ConversionErrorResult.from_json(json)
# print the JSON string representation of the object
print(ConversionErrorResult.to_json())

# convert the object into a dict
conversion_error_result_dict = conversion_error_result_instance.to_dict()
# create an instance of ConversionErrorResult from a dict
conversion_error_result_from_dict = ConversionErrorResult.from_dict(conversion_error_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


