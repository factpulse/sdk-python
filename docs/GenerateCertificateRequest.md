# GenerateCertificateRequest

Request to generate a self-signed X.509 test certificate.  WARNING: This certificate is intended for TESTING only. DO NOT use in production! eIDAS level: SES (Simple Electronic Signature)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cn** | **str** | Common Name (CN) - Certificate name | [optional] [default to 'Test Signature FactPulse']
**organization** | **str** | Organization (O) | [optional] [default to 'FactPulse Test']
**country** | **str** | ISO 2-letter country code (C) | [optional] [default to 'FR']
**city** | **str** | City (L) | [optional] [default to 'Paris']
**state** | **str** | State/Province (ST) | [optional] [default to 'Ile-de-France']
**email** | **str** |  | [optional] 
**validity_days** | **int** | Validity duration in days | [optional] [default to 365]
**key_size** | **int** | RSA key size in bits | [optional] [default to 2048]
**key_passphrase** | **str** |  | [optional] 
**generate_p12** | **bool** | Also generate a PKCS#12 (.p12) file | [optional] [default to False]
**p12_passphrase** | **str** | Passphrase for PKCS#12 file | [optional] [default to 'changeme']

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


