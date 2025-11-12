# RequeteRechercheFlux

Requête pour rechercher des flux soumis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_maj_apres** | **datetime** |  | [optional] 
**date_maj_avant** | **datetime** |  | [optional] 
**type_flux** | [**List[TypeFlux]**](TypeFlux.md) |  | [optional] 
**direction_flux** | [**List[DirectionFlux]**](DirectionFlux.md) |  | [optional] 
**tracking_id** | **str** |  | [optional] 
**flow_id** | **str** |  | [optional] 
**statut_acquittement** | [**StatutAcquittement**](StatutAcquittement.md) |  | [optional] 
**offset** | **int** | Décalage pour la pagination | [optional] [default to 0]
**limit** | **int** | Nombre maximum de résultats (max 100) | [optional] [default to 25]

## Example

```python
from factpulse.models.requete_recherche_flux import RequeteRechercheFlux

# TODO update the JSON string below
json = "{}"
# create an instance of RequeteRechercheFlux from a JSON string
requete_recherche_flux_instance = RequeteRechercheFlux.from_json(json)
# print the JSON string representation of the object
print(RequeteRechercheFlux.to_json())

# convert the object into a dict
requete_recherche_flux_dict = requete_recherche_flux_instance.to_dict()
# create an instance of RequeteRechercheFlux from a dict
requete_recherche_flux_from_dict = RequeteRechercheFlux.from_dict(requete_recherche_flux_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


