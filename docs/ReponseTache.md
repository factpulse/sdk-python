# ReponseTache

Réponse immédiate après la soumission d'une tâche asynchrone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_tache** | **str** |  | 

## Example

```python
from factpulse.models.reponse_tache import ReponseTache

# TODO update the JSON string below
json = "{}"
# create an instance of ReponseTache from a JSON string
reponse_tache_instance = ReponseTache.from_json(json)
# print the JSON string representation of the object
print(ReponseTache.to_json())

# convert the object into a dict
reponse_tache_dict = reponse_tache_instance.to_dict()
# create an instance of ReponseTache from a dict
reponse_tache_from_dict = ReponseTache.from_dict(reponse_tache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


