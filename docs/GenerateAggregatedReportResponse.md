# GenerateAggregatedReportResponse

Response after generating an aggregated e-reporting XML.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** | Report identifier | 
**transmission_type** | **str** | Transmission type (IN or RE) | 
**flow_type** | **str** | AFNOR FlowType determined from content | 
**xml** | **str** | Generated XML content | 
**xml_size** | **int** | XML size in bytes | 
**content_summary** | **Dict[str, object]** | Summary of content (counts by flux type) | 
**message** | **str** | Status message | 

## Example

```python
from factpulse.models.generate_aggregated_report_response import GenerateAggregatedReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAggregatedReportResponse from a JSON string
generate_aggregated_report_response_instance = GenerateAggregatedReportResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateAggregatedReportResponse.to_json())

# convert the object into a dict
generate_aggregated_report_response_dict = generate_aggregated_report_response_instance.to_dict()
# create an instance of GenerateAggregatedReportResponse from a dict
generate_aggregated_report_response_from_dict = GenerateAggregatedReportResponse.from_dict(generate_aggregated_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


