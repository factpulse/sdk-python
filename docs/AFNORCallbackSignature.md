# AFNORCallbackSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algo** | [**AFNORAlgorithm**](AFNORAlgorithm.md) |  | 
**key** | **bytes** | Base 64 encoded string | 

## Example

```python
from factpulse.models.afnor_callback_signature import AFNORCallbackSignature

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORCallbackSignature from a JSON string
afnor_callback_signature_instance = AFNORCallbackSignature.from_json(json)
# print the JSON string representation of the object
print(AFNORCallbackSignature.to_json())

# convert the object into a dict
afnor_callback_signature_dict = afnor_callback_signature_instance.to_dict()
# create an instance of AFNORCallbackSignature from a dict
afnor_callback_signature_from_dict = AFNORCallbackSignature.from_dict(afnor_callback_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


