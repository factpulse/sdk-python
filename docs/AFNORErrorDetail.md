# AFNORErrorDetail

Error detail in AFNOR format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | 
**item** | **str** |  | 
**reason** | **str** |  | 
**source** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from factpulse.models.afnor_error_detail import AFNORErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORErrorDetail from a JSON string
afnor_error_detail_instance = AFNORErrorDetail.from_json(json)
# print the JSON string representation of the object
print(AFNORErrorDetail.to_json())

# convert the object into a dict
afnor_error_detail_dict = afnor_error_detail_instance.to_dict()
# create an instance of AFNORErrorDetail from a dict
afnor_error_detail_from_dict = AFNORErrorDetail.from_dict(afnor_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


