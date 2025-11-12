# ChorusProCredentials

Credentials Chorus Pro pour mode Zero-Trust.  **Mode Zero-Trust** : Les credentials sont passés dans chaque requête et ne sont JAMAIS stockés.  **Sécurité** : - Les credentials ne sont jamais persistés dans la base de données - Ils sont utilisés uniquement pour la durée de la requête - Transmission sécurisée via HTTPS  **Cas d'usage** : - Environnements à haute sécurité (banques, administrations) - Conformité RGPD stricte - Tests avec credentials temporaires - Utilisateurs ne voulant pas stocker leurs credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**piste_client_id** | **str** | Client ID PISTE (portail API gouvernement) | 
**piste_client_secret** | **str** | Client Secret PISTE | 
**chorus_pro_login** | **str** | Login Chorus Pro | 
**chorus_pro_password** | **str** | Mot de passe Chorus Pro | 
**sandbox** | **bool** | Utiliser l&#39;environnement sandbox (true) ou production (false) | [optional] [default to True]

## Example

```python
from factpulse.models.chorus_pro_credentials import ChorusProCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of ChorusProCredentials from a JSON string
chorus_pro_credentials_instance = ChorusProCredentials.from_json(json)
# print the JSON string representation of the object
print(ChorusProCredentials.to_json())

# convert the object into a dict
chorus_pro_credentials_dict = chorus_pro_credentials_instance.to_dict()
# create an instance of ChorusProCredentials from a dict
chorus_pro_credentials_from_dict = ChorusProCredentials.from_dict(chorus_pro_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


