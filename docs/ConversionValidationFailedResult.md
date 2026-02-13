# ConversionValidationFailedResult

Conversion extracted data failed Schematron validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'VALIDATION_FAILED']
**conversion_id** | **str** |  | 
**message** | **str** |  | 
**extracted_data** | **Dict[str, object]** |  | 
**extraction** | [**ConversionExtractionInfo**](ConversionExtractionInfo.md) |  | [optional] 
**validation_errors** | **List[Dict[str, object]]** |  | [optional] 
**profile** | **str** |  | 
**processing_time_ms** | **int** |  | 
**correction_attempted** | **bool** |  | [optional] [default to False]

## Example

```python
from factpulse.models.conversion_validation_failed_result import ConversionValidationFailedResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionValidationFailedResult from a JSON string
conversion_validation_failed_result_instance = ConversionValidationFailedResult.from_json(json)
# print the JSON string representation of the object
print(ConversionValidationFailedResult.to_json())

# convert the object into a dict
conversion_validation_failed_result_dict = conversion_validation_failed_result_instance.to_dict()
# create an instance of ConversionValidationFailedResult from a dict
conversion_validation_failed_result_from_dict = ConversionValidationFailedResult.from_dict(conversion_validation_failed_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


