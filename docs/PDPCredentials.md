# PDPCredentials

Credentials PDP pour la stratégie zero-storage (Strategy B).  Permet de fournir directement les credentials PDP dans la requête au lieu de les stocker dans Django.  Utile pour : - Tests ponctuels sans persister les credentials - Intégrations temporaires - Environnements de développement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_service_url** | **str** | URL de base du Flow Service AFNOR | 
**token_url** | **str** | URL du serveur OAuth2 | 
**client_id** | **str** | Client ID OAuth2 | 
**client_secret** | **str** | Client Secret OAuth2 (sensible) | 

## Example

```python
from factpulse.models.pdp_credentials import PDPCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of PDPCredentials from a JSON string
pdp_credentials_instance = PDPCredentials.from_json(json)
# print the JSON string representation of the object
print(PDPCredentials.to_json())

# convert the object into a dict
pdp_credentials_dict = pdp_credentials_instance.to_dict()
# create an instance of PDPCredentials from a dict
pdp_credentials_from_dict = PDPCredentials.from_dict(pdp_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


