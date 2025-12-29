# ProcessingOptions

Processing options for generation and submission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facturx_profile** | [**FacturXProfile**](FacturXProfile.md) | Factur-X profile to use | [optional] 
**auto_enrich** | **bool** | Auto-enrich data (Company APIs, Chorus Pro, etc.) | [optional] [default to True]
**validate_xml** | **bool** | Validate Factur-X XML with Schematron | [optional] [default to True]
**verify_destination_parameters** | **bool** | Verify required parameters for destination (e.g., service_code for Chorus) | [optional] [default to True]

## Example

```python
from factpulse.models.processing_options import ProcessingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingOptions from a JSON string
processing_options_instance = ProcessingOptions.from_json(json)
# print the JSON string representation of the object
print(ProcessingOptions.to_json())

# convert the object into a dict
processing_options_dict = processing_options_instance.to_dict()
# create an instance of ProcessingOptions from a dict
processing_options_from_dict = ProcessingOptions.from_dict(processing_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


