# GenerateCertificateResponse

Réponse après génération d'un certificat de test.  Contient le certificat PEM, la clé privée PEM, et optionnellement le PKCS#12.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Statut de l&#39;opération | [optional] [default to 'success']
**certificat_pem** | **str** | Certificat X.509 au format PEM | 
**cle_privee_pem** | **str** | Clé privée RSA au format PEM | 
**pkcs12_base64** | **str** |  | [optional] 
**info** | [**CertificateInfoResponse**](CertificateInfoResponse.md) | Informations sur le certificat généré | 
**avertissement** | **str** | Avertissement sur l&#39;utilisation du certificat | [optional] [default to '⚠️ Ce certificat est AUTO-SIGNÉ et destiné uniquement aux TESTS. Ne PAS utiliser en production. Niveau eIDAS : SES (Simple Electronic Signature)']

## Example

```python
from factpulse.models.generate_certificate_response import GenerateCertificateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateCertificateResponse from a JSON string
generate_certificate_response_instance = GenerateCertificateResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateCertificateResponse.to_json())

# convert the object into a dict
generate_certificate_response_dict = generate_certificate_response_instance.to_dict()
# create an instance of GenerateCertificateResponse from a dict
generate_certificate_response_from_dict = GenerateCertificateResponse.from_dict(generate_certificate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


