# CredentialsAFNOR

Credentials AFNOR PDP optionnels.  **MODE 1 - Récupération via JWT (recommandé) :** Ne pas fournir ce champ `credentials` dans le payload. Les credentials PDP seront récupérées automatiquement via client_uid du JWT (0-trust).  **MODE 2 - Credentials dans le payload (zero-storage) :** Fournir tous les champs requis ci-dessous. Utile pour tests ou intégrations tierces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**flow_service_url** | **str** |  | [optional] 

## Example

```python
from factpulse.models.credentials_afnor import CredentialsAFNOR

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsAFNOR from a JSON string
credentials_afnor_instance = CredentialsAFNOR.from_json(json)
# print the JSON string representation of the object
print(CredentialsAFNOR.to_json())

# convert the object into a dict
credentials_afnor_dict = credentials_afnor_instance.to_dict()
# create an instance of CredentialsAFNOR from a dict
credentials_afnor_from_dict = CredentialsAFNOR.from_dict(credentials_afnor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


