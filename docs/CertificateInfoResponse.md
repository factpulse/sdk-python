# CertificateInfoResponse

Informations sur un certificat généré.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cn** | **str** | Common Name | 
**organisation** | **str** | Organisation | 
**pays** | **str** | Code pays | 
**ville** | **str** | Ville | 
**province** | **str** | Province | 
**email** | **str** |  | [optional] 
**sujet** | **str** | Sujet complet (RFC4514) | 
**emetteur** | **str** | Émetteur (auto-signé &#x3D; même que sujet) | 
**numero_serie** | **int** | Numéro de série du certificat | 
**valide_du** | **str** | Date de début de validité (ISO 8601) | 
**valide_au** | **str** | Date de fin de validité (ISO 8601) | 
**algorithme** | **str** | Algorithme de signature | 

## Example

```python
from factpulse.models.certificate_info_response import CertificateInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateInfoResponse from a JSON string
certificate_info_response_instance = CertificateInfoResponse.from_json(json)
# print the JSON string representation of the object
print(CertificateInfoResponse.to_json())

# convert the object into a dict
certificate_info_response_dict = certificate_info_response_instance.to_dict()
# create an instance of CertificateInfoResponse from a dict
certificate_info_response_from_dict = CertificateInfoResponse.from_dict(certificate_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


