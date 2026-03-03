# AFNORCallbackHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_name** | **str** |  | 
**header_value** | **str** |  | 

## Example

```python
from factpulse.models.afnor_callback_header import AFNORCallbackHeader

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORCallbackHeader from a JSON string
afnor_callback_header_instance = AFNORCallbackHeader.from_json(json)
# print the JSON string representation of the object
print(AFNORCallbackHeader.to_json())

# convert the object into a dict
afnor_callback_header_dict = afnor_callback_header_instance.to_dict()
# create an instance of AFNORCallbackHeader from a dict
afnor_callback_header_from_dict = AFNORCallbackHeader.from_dict(afnor_callback_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


