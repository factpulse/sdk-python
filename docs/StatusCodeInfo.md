# StatusCodeInfo

Information sur un code statut.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code numérique | 
**name** | **str** | Nom Python de l&#39;enum | 
**description** | **str** | Description | 

## Example

```python
from factpulse.models.status_code_info import StatusCodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCodeInfo from a JSON string
status_code_info_instance = StatusCodeInfo.from_json(json)
# print the JSON string representation of the object
print(StatusCodeInfo.to_json())

# convert the object into a dict
status_code_info_dict = status_code_info_instance.to_dict()
# create an instance of StatusCodeInfo from a dict
status_code_info_from_dict = StatusCodeInfo.from_dict(status_code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


