# SignatureInfo

Informations sur la signature électronique.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signe** | **bool** | Le PDF a été signé | 
**cn** | **str** |  | [optional] 
**expiration** | **str** |  | [optional] 

## Example

```python
from factpulse.models.signature_info import SignatureInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureInfo from a JSON string
signature_info_instance = SignatureInfo.from_json(json)
# print the JSON string representation of the object
print(SignatureInfo.to_json())

# convert the object into a dict
signature_info_dict = signature_info_instance.to_dict()
# create an instance of SignatureInfo from a dict
signature_info_from_dict = SignatureInfo.from_dict(signature_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


