# AFNORBasicAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**user_password** | **str** |  | 

## Example

```python
from factpulse.models.afnor_basic_authentication import AFNORBasicAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORBasicAuthentication from a JSON string
afnor_basic_authentication_instance = AFNORBasicAuthentication.from_json(json)
# print the JSON string representation of the object
print(AFNORBasicAuthentication.to_json())

# convert the object into a dict
afnor_basic_authentication_dict = afnor_basic_authentication_instance.to_dict()
# create an instance of AFNORBasicAuthentication from a dict
afnor_basic_authentication_from_dict = AFNORBasicAuthentication.from_dict(afnor_basic_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


