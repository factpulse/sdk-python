# AllowanceCharge

Document-level or line-level allowance/charge.  Represents BG-20 (Document level allowances), BG-21 (Document level charges), BG-27 (Invoice line allowances), or BG-28 (Invoice line charges).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_charge** | **bool** | True for charge, False for allowance (ChargeIndicator). | 
**amount** | [**Amount1**](Amount1.md) |  | 
**base_amount** | [**BaseAmount**](BaseAmount.md) |  | [optional] 
**percentage** | [**Percentage**](Percentage.md) |  | [optional] 
**reason** | **str** |  | [optional] 
**reason_code** | [**AllowanceChargeReasonCode**](AllowanceChargeReasonCode.md) |  | [optional] 
**vat_category** | [**VATCategory**](VATCategory.md) |  | [optional] 
**vat_rate** | [**VatRate**](VatRate.md) |  | [optional] 

## Example

```python
from factpulse.models.allowance_charge import AllowanceCharge

# TODO update the JSON string below
json = "{}"
# create an instance of AllowanceCharge from a JSON string
allowance_charge_instance = AllowanceCharge.from_json(json)
# print the JSON string representation of the object
print(AllowanceCharge.to_json())

# convert the object into a dict
allowance_charge_dict = allowance_charge_instance.to_dict()
# create an instance of AllowanceCharge from a dict
allowance_charge_from_dict = AllowanceCharge.from_dict(allowance_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


