# GenerateCertificateResponse

Response after generating a test certificate.  Contains certificate PEM, private key PEM, and optionally PKCS#12.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Operation status | [optional] [default to 'success']
**certificate_pem** | **str** | X.509 certificate in PEM format | 
**private_key_pem** | **str** | RSA private key in PEM format | 
**pkcs12_base64** | **str** |  | [optional] 
**info** | [**CertificateInfoResponse**](CertificateInfoResponse.md) | Generated certificate information | 
**warning** | **str** | Warning about certificate usage | [optional] [default to 'WARNING: This certificate is SELF-SIGNED and intended for TESTING only. DO NOT use in production. eIDAS level: SES (Simple Electronic Signature)']

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


