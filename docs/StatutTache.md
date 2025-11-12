# StatutTache

Description complète du statut d'une tâche asynchrone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_tache** | **str** |  | 
**statut** | **str** |  | 
**resultat** | [**AnyOf**](AnyOf.md) |  | [optional] 

## Example

```python
from factpulse.models.statut_tache import StatutTache

# TODO update the JSON string below
json = "{}"
# create an instance of StatutTache from a JSON string
statut_tache_instance = StatutTache.from_json(json)
# print the JSON string representation of the object
print(StatutTache.to_json())

# convert the object into a dict
statut_tache_dict = statut_tache_instance.to_dict()
# create an instance of StatutTache from a dict
statut_tache_from_dict = StatutTache.from_dict(statut_tache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


