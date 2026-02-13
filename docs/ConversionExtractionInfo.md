# ConversionExtractionInfo

OCR extraction metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence_score** | **float** |  | 
**ocr_provider** | **str** |  | [optional] [default to 'mistral_ocr']

## Example

```python
from factpulse.models.conversion_extraction_info import ConversionExtractionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionExtractionInfo from a JSON string
conversion_extraction_info_instance = ConversionExtractionInfo.from_json(json)
# print the JSON string representation of the object
print(ConversionExtractionInfo.to_json())

# convert the object into a dict
conversion_extraction_info_dict = conversion_extraction_info_instance.to_dict()
# create an instance of ConversionExtractionInfo from a dict
conversion_extraction_info_from_dict = ConversionExtractionInfo.from_dict(conversion_extraction_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


