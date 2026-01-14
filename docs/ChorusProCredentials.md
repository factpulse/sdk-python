# ChorusProCredentials

Chorus Pro credentials for Zero-Trust mode.  **Zero-Trust Mode**: Credentials are passed in each request and are NEVER stored.  **Security**: - Credentials are never persisted in the database - They are used only for the duration of the request - Secure transmission via HTTPS  **Use cases**: - High-security environments (banks, administrations) - Strict GDPR compliance - Tests with temporary credentials - Users who don't want to store their credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**piste_client_id** | **str** | PISTE Client ID (government API portal) | 
**piste_client_secret** | **str** | PISTE Client Secret | 
**chorus_pro_login** | **str** | Chorus Pro login | 
**chorus_pro_password** | **str** | Chorus Pro password | 
**sandbox** | **bool** | Use sandbox environment (true) or production (false) | [optional] [default to True]

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


