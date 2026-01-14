# SignatureParameters

Optional parameters to sign the generated PDF.  **MODE 1 - Stored certificate (recommended):** Only provide metadata (reason, location, etc.). The certificate will be automatically retrieved via client_uid from JWT. eIDAS compliant PAdES-B-LT signature.  **MODE 2 - Keys in payload (tests/special cases):** Provide key_pem + cert_pem directly in the payload. Accepted PEM format: raw (\"-----BEGIN...\") or base64.  **Selection rule:** - If key_pem AND cert_pem provided → Mode 2 (payload keys) - Otherwise → Mode 1 (stored certificate retrieved via client_uid)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_pem** | **str** |  | [optional] 
**cert_pem** | **str** |  | [optional] 
**key_passphrase** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**contact** | **str** |  | [optional] 
**field_name** | **str** | PDF signature field name | [optional] [default to 'FactPulseSignature']
**use_pades_lt** | **bool** | Enable PAdES-B-LT (long-term archival). REQUIRES certificate with OCSP/CRL access | [optional] [default to False]
**use_timestamp** | **bool** | Enable RFC 3161 timestamping with FreeTSA (PAdES-B-T) | [optional] [default to True]

## Example

```python
from factpulse.models.signature_parameters import SignatureParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureParameters from a JSON string
signature_parameters_instance = SignatureParameters.from_json(json)
# print the JSON string representation of the object
print(SignatureParameters.to_json())

# convert the object into a dict
signature_parameters_dict = signature_parameters_instance.to_dict()
# create an instance of SignatureParameters from a dict
signature_parameters_from_dict = SignatureParameters.from_dict(signature_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


