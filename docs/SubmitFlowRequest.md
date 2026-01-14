# SubmitFlowRequest

Request to submit an invoice to a PDP/PA via AFNOR.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_name** | **str** | Flow name (e.g., &#39;Invoice 2025-001&#39;) | 
**flow_syntax** | [**FlowSyntax**](FlowSyntax.md) | Flow syntax (CII for Factur-X) | [optional] 
**flow_profile** | [**FlowProfile**](FlowProfile.md) |  | [optional] 
**tracking_id** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**pdp_credentials** | [**PDPCredentials**](PDPCredentials.md) |  | [optional] 

## Example

```python
from factpulse.models.submit_flow_request import SubmitFlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitFlowRequest from a JSON string
submit_flow_request_instance = SubmitFlowRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitFlowRequest.to_json())

# convert the object into a dict
submit_flow_request_dict = submit_flow_request_instance.to_dict()
# create an instance of SubmitFlowRequest from a dict
submit_flow_request_from_dict = SubmitFlowRequest.from_dict(submit_flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


