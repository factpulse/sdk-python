# Destinataire

Informations sur le destinataire de la facture (le client).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adresse_electronique** | [**AdresseElectronique**](AdresseElectronique.md) |  | 
**code_service_executant** | **str** |  | [optional] 
**nom** | **str** |  | [optional] 
**siren** | **str** |  | [optional] 
**siret** | **str** |  | [optional] 
**adresse_postale** | [**AdressePostale**](AdressePostale.md) |  | [optional] 

## Example

```python
from factpulse.models.destinataire import Destinataire

# TODO update the JSON string below
json = "{}"
# create an instance of Destinataire from a JSON string
destinataire_instance = Destinataire.from_json(json)
# print the JSON string representation of the object
print(Destinataire.to_json())

# convert the object into a dict
destinataire_dict = destinataire_instance.to_dict()
# create an instance of Destinataire from a dict
destinataire_from_dict = Destinataire.from_dict(destinataire_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


