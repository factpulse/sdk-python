# AFNORCallbackAuthentication

The authentication mode required for the callback call

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** |  | 
**user_id** | **str** |  | 
**user_password** | **str** |  | 
**token_url** | **str** |  | 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 

## Example

```python
from factpulse.models.afnor_callback_authentication import AFNORCallbackAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORCallbackAuthentication from a JSON string
afnor_callback_authentication_instance = AFNORCallbackAuthentication.from_json(json)
# print the JSON string representation of the object
print(AFNORCallbackAuthentication.to_json())

# convert the object into a dict
afnor_callback_authentication_dict = afnor_callback_authentication_instance.to_dict()
# create an instance of AFNORCallbackAuthentication from a dict
afnor_callback_authentication_from_dict = AFNORCallbackAuthentication.from_dict(afnor_callback_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


