# AFNORFlowInfoExtension

Extension to build the FlowInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha256** | **bytes** | The sha256 is the fingerprint of the attached file: - if provided in the request: it should be checked once received - if not provided in the request: it may be computed and returned in the response  | [optional] 

## Example

```python
from factpulse.models.afnor_flow_info_extension import AFNORFlowInfoExtension

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORFlowInfoExtension from a JSON string
afnor_flow_info_extension_instance = AFNORFlowInfoExtension.from_json(json)
# print the JSON string representation of the object
print(AFNORFlowInfoExtension.to_json())

# convert the object into a dict
afnor_flow_info_extension_dict = afnor_flow_info_extension_instance.to_dict()
# create an instance of AFNORFlowInfoExtension from a dict
afnor_flow_info_extension_from_dict = AFNORFlowInfoExtension.from_dict(afnor_flow_info_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


