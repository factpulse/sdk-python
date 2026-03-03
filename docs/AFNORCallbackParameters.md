# AFNORCallbackParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**headers** | [**List[AFNORCallbackHeader]**](AFNORCallbackHeader.md) |  | [optional] 
**authentication** | [**AFNORCallbackAuthentication**](AFNORCallbackAuthentication.md) |  | [optional] 
**signature** | [**AFNORCallbackSignature**](AFNORCallbackSignature.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_callback_parameters import AFNORCallbackParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORCallbackParameters from a JSON string
afnor_callback_parameters_instance = AFNORCallbackParameters.from_json(json)
# print the JSON string representation of the object
print(AFNORCallbackParameters.to_json())

# convert the object into a dict
afnor_callback_parameters_dict = afnor_callback_parameters_instance.to_dict()
# create an instance of AFNORCallbackParameters from a dict
afnor_callback_parameters_from_dict = AFNORCallbackParameters.from_dict(afnor_callback_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


