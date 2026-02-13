# ConversionPendingInputResult

Conversion needs user input (missing fields).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'PENDING_INPUT']
**conversion_id** | **str** |  | 
**message** | **str** |  | 
**missing_fields** | **List[str]** |  | 
**extracted_data** | **Dict[str, object]** |  | 
**confidence_score** | **float** |  | 
**processing_time_ms** | **int** |  | 

## Example

```python
from factpulse.models.conversion_pending_input_result import ConversionPendingInputResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionPendingInputResult from a JSON string
conversion_pending_input_result_instance = ConversionPendingInputResult.from_json(json)
# print the JSON string representation of the object
print(ConversionPendingInputResult.to_json())

# convert the object into a dict
conversion_pending_input_result_dict = conversion_pending_input_result_instance.to_dict()
# create an instance of ConversionPendingInputResult from a dict
conversion_pending_input_result_from_dict = ConversionPendingInputResult.from_dict(conversion_pending_input_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


