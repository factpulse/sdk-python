# ReasonCodeInfo

Information sur un code motif.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code | 
**name** | **str** | Nom Python de l&#39;enum | 
**description** | **str** | Description | 

## Example

```python
from factpulse.models.reason_code_info import ReasonCodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReasonCodeInfo from a JSON string
reason_code_info_instance = ReasonCodeInfo.from_json(json)
# print the JSON string representation of the object
print(ReasonCodeInfo.to_json())

# convert the object into a dict
reason_code_info_dict = reason_code_info_instance.to_dict()
# create an instance of ReasonCodeInfo from a dict
reason_code_info_from_dict = ReasonCodeInfo.from_dict(reason_code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


