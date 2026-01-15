# SubmitEReportingResponse

Response after submitting e-reporting to PA/PDP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | Flow identifier from PA/PDP | 
**report_id** | **str** | Report identifier | 
**tracking_id** | **str** |  | [optional] 
**flow_type** | **str** | Flux type | 
**sha256** | **str** | SHA256 hash of submitted XML | 
**afnor_flow_type** | **str** |  | [optional] 
**afnor_response** | **Dict[str, object]** |  | [optional] 
**message** | **str** | Status message | 

## Example

```python
from factpulse.models.submit_e_reporting_response import SubmitEReportingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitEReportingResponse from a JSON string
submit_e_reporting_response_instance = SubmitEReportingResponse.from_json(json)
# print the JSON string representation of the object
print(SubmitEReportingResponse.to_json())

# convert the object into a dict
submit_e_reporting_response_dict = submit_e_reporting_response_instance.to_dict()
# create an instance of SubmitEReportingResponse from a dict
submit_e_reporting_response_from_dict = SubmitEReportingResponse.from_dict(submit_e_reporting_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


