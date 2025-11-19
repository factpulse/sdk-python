# Fournisseur

Informations sur le fournisseur qui émet la facture.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adresse_electronique** | [**AdresseElectronique**](AdresseElectronique.md) |  | 
**id_fournisseur** | **int** |  | 
**code_coordonnees_bancaires_fournisseur** | **int** |  | [optional] 
**id_service_fournisseur** | **int** |  | [optional] 
**nom** | **str** |  | [optional] 
**siren** | **str** |  | [optional] 
**siret** | **str** |  | [optional] 
**numero_tva_intra** | **str** |  | [optional] 
**iban** | **str** |  | [optional] 
**adresse_postale** | [**AdressePostale**](AdressePostale.md) |  | [optional] 

## Example

```python
from factpulse.models.fournisseur import Fournisseur

# TODO update the JSON string below
json = "{}"
# create an instance of Fournisseur from a JSON string
fournisseur_instance = Fournisseur.from_json(json)
# print the JSON string representation of the object
print(Fournisseur.to_json())

# convert the object into a dict
fournisseur_dict = fournisseur_instance.to_dict()
# create an instance of Fournisseur from a dict
fournisseur_from_dict = Fournisseur.from_dict(fournisseur_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


