# Utilisateur

Modèle Pydantic représentant les données de l'utilisateur authentifié.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**username** | **str** |  | 
**email** | **str** |  | 
**is_active** | **bool** |  | 
**is_superuser** | **bool** |  | [optional] [default to False]
**is_staff** | **bool** |  | [optional] [default to False]
**bypass_quota** | **bool** |  | [optional] [default to False]
**team_id** | **int** |  | [optional] 
**has_quota** | **bool** |  | [optional] [default to True]
**quota_info** | [**QuotaInfo**](QuotaInfo.md) |  | [optional] 
**is_trial** | **bool** |  | [optional] [default to False]
**client_uid** | **str** |  | [optional] 

## Example

```python
from factpulse.models.utilisateur import Utilisateur

# TODO update the JSON string below
json = "{}"
# create an instance of Utilisateur from a JSON string
utilisateur_instance = Utilisateur.from_json(json)
# print the JSON string representation of the object
print(Utilisateur.to_json())

# convert the object into a dict
utilisateur_dict = utilisateur_instance.to_dict()
# create an instance of Utilisateur from a dict
utilisateur_from_dict = Utilisateur.from_dict(utilisateur_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


