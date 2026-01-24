# ReportIssuer

Report issuer/declarant information (TT-12 to TT-16).  The issuer is the French company declaring the transactions. The role_code determines whether the company is: - SE (Seller): B2Bi case - French company sells to foreign buyer - BY (Buyer): Bi2B case - French company buys from foreign seller  Source: Annexe 6 v1.9, bloc Issuer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**siren** | **str** | SIREN or SIRET of the declarant (French company) | 
**name** | **str** |  | [optional] 
**vat_id** | **str** |  | [optional] 
**role_code** | [**IssuerRoleCode**](IssuerRoleCode.md) | Role of the declarant (TT-15). SE&#x3D;Seller (B2Bi: French seller to foreign buyer). BY&#x3D;Buyer (Bi2B: French buyer from foreign seller). | [optional] 

## Example

```python
from factpulse.models.report_issuer import ReportIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of ReportIssuer from a JSON string
report_issuer_instance = ReportIssuer.from_json(json)
# print the JSON string representation of the object
print(ReportIssuer.to_json())

# convert the object into a dict
report_issuer_dict = report_issuer_instance.to_dict()
# create an instance of ReportIssuer from a dict
report_issuer_from_dict = ReportIssuer.from_dict(report_issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


