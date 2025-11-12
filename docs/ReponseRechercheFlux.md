# ReponseRechercheFlux

Réponse d'une recherche de flux

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Nombre total de résultats | 
**offset** | **int** | Décalage appliqué | 
**limit** | **int** | Limite de résultats | 
**resultats** | [**List[FluxResume]**](FluxResume.md) | Liste des flux trouvés | 

## Example

```python
from factpulse.models.reponse_recherche_flux import ReponseRechercheFlux

# TODO update the JSON string below
json = "{}"
# create an instance of ReponseRechercheFlux from a JSON string
reponse_recherche_flux_instance = ReponseRechercheFlux.from_json(json)
# print the JSON string representation of the object
print(ReponseRechercheFlux.to_json())

# convert the object into a dict
reponse_recherche_flux_dict = reponse_recherche_flux_instance.to_dict()
# create an instance of ReponseRechercheFlux from a dict
reponse_recherche_flux_from_dict = ReponseRechercheFlux.from_dict(reponse_recherche_flux_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


