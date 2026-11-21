# SuperPDPVatRegimeResponse

VAT regime of the client's company at SuperPDP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vat_regime** | **str** |  | [optional] 
**has_vat_on_debits** | **bool** | Whether VAT on debits is opted for | [optional] [default to False]

## Example

```python
from factpulse.models.super_pdp_vat_regime_response import SuperPDPVatRegimeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuperPDPVatRegimeResponse from a JSON string
super_pdp_vat_regime_response_instance = SuperPDPVatRegimeResponse.from_json(json)
# print the JSON string representation of the object
print(SuperPDPVatRegimeResponse.to_json())

# convert the object into a dict
super_pdp_vat_regime_response_dict = super_pdp_vat_regime_response_instance.to_dict()
# create an instance of SuperPDPVatRegimeResponse from a dict
super_pdp_vat_regime_response_from_dict = SuperPDPVatRegimeResponse.from_dict(super_pdp_vat_regime_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


