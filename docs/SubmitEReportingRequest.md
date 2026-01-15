# SubmitEReportingRequest

Request to submit e-reporting to a PA/PDP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateEReportingRequest**](CreateEReportingRequest.md) | E-Reporting data to submit | 
**tracking_id** | **str** |  | [optional] 
**pdp_flow_service_url** | **str** |  | [optional] 
**pdp_token_url** | **str** |  | [optional] 
**pdp_client_id** | **str** |  | [optional] 
**pdp_client_secret** | **str** |  | [optional] 

## Example

```python
from factpulse.models.submit_e_reporting_request import SubmitEReportingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitEReportingRequest from a JSON string
submit_e_reporting_request_instance = SubmitEReportingRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitEReportingRequest.to_json())

# convert the object into a dict
submit_e_reporting_request_dict = submit_e_reporting_request_instance.to_dict()
# create an instance of SubmitEReportingRequest from a dict
submit_e_reporting_request_from_dict = SubmitEReportingRequest.from_dict(submit_e_reporting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


