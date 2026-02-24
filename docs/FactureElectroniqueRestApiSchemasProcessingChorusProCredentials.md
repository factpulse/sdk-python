# FactureElectroniqueRestApiSchemasProcessingChorusProCredentials

Optional Chorus Pro credentials.  **MODE 1 - JWT retrieval (recommended):** Do not provide this `credentials` field in the payload. Credentials will be automatically retrieved via client_uid from JWT (0-trust).  **MODE 2 - Credentials in payload:** Provide all required fields below. Useful for tests or third-party integrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**piste_client_id** | **str** |  | [optional] 
**piste_client_secret** | **str** |  | [optional] 
**chorus_login** | **str** |  | [optional] 
**chorus_password** | **str** |  | [optional] 
**sandbox_mode** | **bool** | [MODE 2] Use sandbox mode (default: True) | [optional] [default to True]

## Example

```python
from factpulse.models.facture_electronique_rest_api_schemas_processing_chorus_pro_credentials import FactureElectroniqueRestApiSchemasProcessingChorusProCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of FactureElectroniqueRestApiSchemasProcessingChorusProCredentials from a JSON string
facture_electronique_rest_api_schemas_processing_chorus_pro_credentials_instance = FactureElectroniqueRestApiSchemasProcessingChorusProCredentials.from_json(json)
# print the JSON string representation of the object
print(FactureElectroniqueRestApiSchemasProcessingChorusProCredentials.to_json())

# convert the object into a dict
facture_electronique_rest_api_schemas_processing_chorus_pro_credentials_dict = facture_electronique_rest_api_schemas_processing_chorus_pro_credentials_instance.to_dict()
# create an instance of FactureElectroniqueRestApiSchemasProcessingChorusProCredentials from a dict
facture_electronique_rest_api_schemas_processing_chorus_pro_credentials_from_dict = FactureElectroniqueRestApiSchemasProcessingChorusProCredentials.from_dict(facture_electronique_rest_api_schemas_processing_chorus_pro_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


