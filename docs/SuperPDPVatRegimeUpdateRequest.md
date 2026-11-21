# SuperPDPVatRegimeUpdateRequest

VAT regime to set on the client's company at SuperPDP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vat_regime** | **str** | monthly (réel normal mensuel), quarterly (réel normal trimestriel), simplified (régime simplifié), vat_exemption (franchise en base) | 
**has_vat_on_debits** | **bool** |  | [optional] 

## Example

```python
from factpulse.models.super_pdp_vat_regime_update_request import SuperPDPVatRegimeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SuperPDPVatRegimeUpdateRequest from a JSON string
super_pdp_vat_regime_update_request_instance = SuperPDPVatRegimeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SuperPDPVatRegimeUpdateRequest.to_json())

# convert the object into a dict
super_pdp_vat_regime_update_request_dict = super_pdp_vat_regime_update_request_instance.to_dict()
# create an instance of SuperPDPVatRegimeUpdateRequest from a dict
super_pdp_vat_regime_update_request_from_dict = SuperPDPVatRegimeUpdateRequest.from_dict(super_pdp_vat_regime_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


