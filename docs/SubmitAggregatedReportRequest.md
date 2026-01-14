# SubmitAggregatedReportRequest

Request to submit an aggregated e-reporting to a PA/PDP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateAggregatedReportRequest**](CreateAggregatedReportRequest.md) | Aggregated e-reporting data | 
**tracking_id** | **str** |  | [optional] 
**pdp_flow_service_url** | **str** |  | [optional] 
**pdp_token_url** | **str** |  | [optional] 
**pdp_client_id** | **str** |  | [optional] 
**pdp_client_secret** | **str** |  | [optional] 

## Example

```python
from factpulse.models.submit_aggregated_report_request import SubmitAggregatedReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitAggregatedReportRequest from a JSON string
submit_aggregated_report_request_instance = SubmitAggregatedReportRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitAggregatedReportRequest.to_json())

# convert the object into a dict
submit_aggregated_report_request_dict = submit_aggregated_report_request_instance.to_dict()
# create an instance of SubmitAggregatedReportRequest from a dict
submit_aggregated_report_request_from_dict = SubmitAggregatedReportRequest.from_dict(submit_aggregated_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


