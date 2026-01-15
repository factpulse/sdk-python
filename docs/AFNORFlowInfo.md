# AFNORFlowInfo

Signaling of the flow: - The tracking id is an external identifier and is used to track the flow by the sender - The sha256 is the fingerprint of the attached file:   - if provided in the request: it should be checked once received   - if not provided in the request: it should be computed and returned in the response 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_id** | **str** | Unique identifier supporting UUID but not only, for flexibility purpose | [optional] 
**name** | **str** | Name of the file | [optional] 
**processing_rule** | [**AFNORProcessingRule**](AFNORProcessingRule.md) |  | [optional] 
**flow_syntax** | [**AFNORFlowSyntax**](AFNORFlowSyntax.md) |  | 
**flow_profile** | [**AFNORFlowProfile**](AFNORFlowProfile.md) |  | [optional] 
**sha256** | **str** |  | [optional] 

## Example

```python
from factpulse.models.afnor_flow_info import AFNORFlowInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORFlowInfo from a JSON string
afnor_flow_info_instance = AFNORFlowInfo.from_json(json)
# print the JSON string representation of the object
print(AFNORFlowInfo.to_json())

# convert the object into a dict
afnor_flow_info_dict = afnor_flow_info_instance.to_dict()
# create an instance of AFNORFlowInfo from a dict
afnor_flow_info_from_dict = AFNORFlowInfo.from_dict(afnor_flow_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


