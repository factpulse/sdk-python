# CertificateInfoResponse

Information about a generated certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cn** | **str** | Common Name | 
**organization** | **str** | Organization | 
**country** | **str** | Country code | 
**city** | **str** | City | 
**state** | **str** | State/Province | 
**email** | **str** |  | [optional] 
**subject** | **str** | Full subject (RFC4514) | 
**issuer** | **str** | Issuer (self-signed &#x3D; same as subject) | 
**serial_number** | **int** | Certificate serial number | 
**valid_from** | **str** | Validity start date (ISO 8601) | 
**valid_to** | **str** | Validity end date (ISO 8601) | 
**algorithm** | **str** | Signature algorithm | 

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


