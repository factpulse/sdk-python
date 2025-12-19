# AFNORResult

Result of submission to AFNOR PDP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | Submitted flow identifier | 
**tracking_id** | **str** |  | [optional] 
**sha256** | **str** | SHA-256 hash of submitted file | 
**flow_syntax** | **str** | Flow syntax | 
**flow_profile** | **str** |  | [optional] 

## Example

```python
from factpulse.models.afnor_result import AFNORResult

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORResult from a JSON string
afnor_result_instance = AFNORResult.from_json(json)
# print the JSON string representation of the object
print(AFNORResult.to_json())

# convert the object into a dict
afnor_result_dict = afnor_result_instance.to_dict()
# create an instance of AFNORResult from a dict
afnor_result_from_dict = AFNORResult.from_dict(afnor_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


