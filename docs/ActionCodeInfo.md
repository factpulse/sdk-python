# ActionCodeInfo

Information sur un code action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code | 
**name** | **str** | Nom Python de l&#39;enum | 
**description** | **str** | Description | 

## Example

```python
from factpulse.models.action_code_info import ActionCodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ActionCodeInfo from a JSON string
action_code_info_instance = ActionCodeInfo.from_json(json)
# print the JSON string representation of the object
print(ActionCodeInfo.to_json())

# convert the object into a dict
action_code_info_dict = action_code_info_instance.to_dict()
# create an instance of ActionCodeInfo from a dict
action_code_info_from_dict = ActionCodeInfo.from_dict(action_code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


