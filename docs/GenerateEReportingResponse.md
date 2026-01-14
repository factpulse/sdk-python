# GenerateEReportingResponse

Response after generating e-reporting XML.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** | Report identifier | 
**flow_type** | **str** | Flux type | 
**xml** | **str** | Generated XML content | 
**xml_size** | **int** | XML size in bytes | 
**message** | **str** | Status message | 

## Example

```python
from factpulse.models.generate_e_reporting_response import GenerateEReportingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateEReportingResponse from a JSON string
generate_e_reporting_response_instance = GenerateEReportingResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateEReportingResponse.to_json())

# convert the object into a dict
generate_e_reporting_response_dict = generate_e_reporting_response_instance.to_dict()
# create an instance of GenerateEReportingResponse from a dict
generate_e_reporting_response_from_dict = GenerateEReportingResponse.from_dict(generate_e_reporting_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


