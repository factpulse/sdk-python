# DonneesFactureSimplifiees

Données simplifiées de la facture (format minimal pour auto-enrichissement).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero** | **str** | Numéro de facture unique | 
**emetteur** | **Dict[str, object]** | Informations sur l&#39;émetteur (siret, iban, ...) | 
**destinataire** | **Dict[str, object]** | Informations sur le destinataire (siret, ...) | 
**lignes** | **List[Dict[str, object]]** | Lignes de la facture | 
**var_date** | **str** |  | [optional] 
**echeance_jours** | **int** | Échéance en jours (défaut: 30) | [optional] [default to 30]
**commentaire** | **str** |  | [optional] 
**numero_bon_commande** | **str** |  | [optional] 
**numero_marche** | **str** |  | [optional] 

## Example

```python
from factpulse.models.donnees_facture_simplifiees import DonneesFactureSimplifiees

# TODO update the JSON string below
json = "{}"
# create an instance of DonneesFactureSimplifiees from a JSON string
donnees_facture_simplifiees_instance = DonneesFactureSimplifiees.from_json(json)
# print the JSON string representation of the object
print(DonneesFactureSimplifiees.to_json())

# convert the object into a dict
donnees_facture_simplifiees_dict = donnees_facture_simplifiees_instance.to_dict()
# create an instance of DonneesFactureSimplifiees from a dict
donnees_facture_simplifiees_from_dict = DonneesFactureSimplifiees.from_dict(donnees_facture_simplifiees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


