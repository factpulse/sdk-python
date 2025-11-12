# CredentialsChorusPro

Credentials Chorus Pro optionnels.  **MODE 1 - Récupération via JWT (recommandé) :** Ne pas fournir ce champ `credentials` dans le payload. Les credentials seront récupérés automatiquement via client_uid du JWT (0-trust).  **MODE 2 - Credentials dans le payload :** Fournir tous les champs requis ci-dessous. Utile pour tests ou intégrations tierces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**piste_client_id** | **str** |  | [optional] 
**piste_client_secret** | **str** |  | [optional] 
**chorus_login** | **str** |  | [optional] 
**chorus_password** | **str** |  | [optional] 
**mode_sandbox** | **bool** | [MODE 2] Utiliser le mode sandbox (défaut: True) | [optional] [default to True]

## Example

```python
from factpulse.models.credentials_chorus_pro import CredentialsChorusPro

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsChorusPro from a JSON string
credentials_chorus_pro_instance = CredentialsChorusPro.from_json(json)
# print the JSON string representation of the object
print(CredentialsChorusPro.to_json())

# convert the object into a dict
credentials_chorus_pro_dict = credentials_chorus_pro_instance.to_dict()
# create an instance of CredentialsChorusPro from a dict
credentials_chorus_pro_from_dict = CredentialsChorusPro.from_dict(credentials_chorus_pro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


