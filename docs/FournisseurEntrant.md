# FournisseurEntrant

Fournisseur extrait d'une facture entrante.  Contrairement au modèle Fournisseur de models.py, ce modèle n'a pas de champ id_fournisseur car cette information n'est pas disponible dans les XML Factur-X/CII/UBL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nom** | **str** | Raison sociale du fournisseur (BT-27) | 
**siren** | **str** |  | [optional] 
**siret** | **str** |  | [optional] 
**numero_tva_intra** | **str** |  | [optional] 
**adresse_postale** | [**AdressePostale**](AdressePostale.md) |  | [optional] 
**adresse_electronique** | [**AdresseElectronique**](AdresseElectronique.md) |  | [optional] 
**email** | **str** |  | [optional] 
**telephone** | **str** |  | [optional] 

## Example

```python
from factpulse.models.fournisseur_entrant import FournisseurEntrant

# TODO update the JSON string below
json = "{}"
# create an instance of FournisseurEntrant from a JSON string
fournisseur_entrant_instance = FournisseurEntrant.from_json(json)
# print the JSON string representation of the object
print(FournisseurEntrant.to_json())

# convert the object into a dict
fournisseur_entrant_dict = fournisseur_entrant_instance.to_dict()
# create an instance of FournisseurEntrant from a dict
fournisseur_entrant_from_dict = FournisseurEntrant.from_dict(fournisseur_entrant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


