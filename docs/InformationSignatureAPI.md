# InformationSignatureAPI

Informations sur une signature électronique dans un PDF.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nom_champ** | **str** | Nom du champ de signature dans le PDF | 
**signataire** | **str** |  | [optional] 
**date_signature** | **str** |  | [optional] 
**raison** | **str** |  | [optional] 
**localisation** | **str** |  | [optional] 
**est_valide** | **bool** |  | [optional] 

## Example

```python
from factpulse.models.information_signature_api import InformationSignatureAPI

# TODO update the JSON string below
json = "{}"
# create an instance of InformationSignatureAPI from a JSON string
information_signature_api_instance = InformationSignatureAPI.from_json(json)
# print the JSON string representation of the object
print(InformationSignatureAPI.to_json())

# convert the object into a dict
information_signature_api_dict = information_signature_api_instance.to_dict()
# create an instance of InformationSignatureAPI from a dict
information_signature_api_from_dict = InformationSignatureAPI.from_dict(information_signature_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


