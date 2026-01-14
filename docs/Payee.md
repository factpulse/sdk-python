# Payee

Information about the payment beneficiary (BG-10 / PayeeTradeParty).  The payee is the party receiving payment. This block is used only if the payee is different from the seller (supplier).  **Main use case**: Factoring When an invoice is factored, the factor (factoring company) becomes the payment beneficiary instead of the supplier.  **Business Terms (EN16931)**: - BT-59: Payee name (mandatory) - BT-60: Payee identifier (SIRET with schemeID 0009) - BT-61: Payee legal identifier (SIREN with schemeID 0002)  **Reference**: docs/guide_affacturage.md

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nom** | **str** | Payee name (BT-59). Mandatory. | 
**payee_id** | **str** |  | [optional] 
**siret** | **str** |  | [optional] 
**siren** | **str** |  | [optional] 
**electronic_address** | [**ElectronicAddress**](ElectronicAddress.md) |  | [optional] 
**iban** | **str** |  | [optional] 
**bic** | **str** |  | [optional] 
**global_ids** | [**List[ElectronicAddress]**](ElectronicAddress.md) |  | [optional] 

## Example

```python
from factpulse.models.payee import Payee

# TODO update the JSON string below
json = "{}"
# create an instance of Payee from a JSON string
payee_instance = Payee.from_json(json)
# print the JSON string representation of the object
print(Payee.to_json())

# convert the object into a dict
payee_dict = payee_instance.to_dict()
# create an instance of Payee from a dict
payee_from_dict = Payee.from_dict(payee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


