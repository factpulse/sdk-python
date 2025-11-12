# GenerateCertificateRequest

Requête pour générer un certificat X.509 auto-signé de test.  ⚠️ ATTENTION : Ce certificat est destiné uniquement aux TESTS. NE PAS utiliser en production ! Niveau eIDAS : SES (Simple Electronic Signature)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cn** | **str** | Common Name (CN) - Nom du certificat | [optional] [default to 'Test Signature FactPulse']
**organisation** | **str** | Organisation (O) | [optional] [default to 'FactPulse Test']
**pays** | **str** | Code pays ISO 2 lettres (C) | [optional] [default to 'FR']
**ville** | **str** | Ville (L) | [optional] [default to 'Paris']
**province** | **str** | Province/État (ST) | [optional] [default to 'Ile-de-France']
**email** | **str** |  | [optional] 
**duree_jours** | **int** | Durée de validité en jours | [optional] [default to 365]
**taille_cle** | **int** | Taille de la clé RSA en bits | [optional] [default to 2048]
**passphrase_cle** | **str** |  | [optional] 
**generer_p12** | **bool** | Générer aussi un fichier PKCS#12 (.p12) | [optional] [default to False]
**passphrase_p12** | **str** | Passphrase pour le fichier PKCS#12 | [optional] [default to 'changeme']

## Example

```python
from factpulse.models.generate_certificate_request import GenerateCertificateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateCertificateRequest from a JSON string
generate_certificate_request_instance = GenerateCertificateRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateCertificateRequest.to_json())

# convert the object into a dict
generate_certificate_request_dict = generate_certificate_request_instance.to_dict()
# create an instance of GenerateCertificateRequest from a dict
generate_certificate_request_from_dict = GenerateCertificateRequest.from_dict(generate_certificate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


