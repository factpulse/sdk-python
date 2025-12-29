# VATLine

Represents a VAT breakdown line by rate (BG-23).  For exemptions (categories E, AE, K, G, O), the fields `exemption_reason` and `vatex_code` are required per EN16931.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxable_amount** | [**TaxableAmount**](TaxableAmount.md) |  | 
**vat_amount** | [**VATAmount**](VATAmount.md) |  | 
**rate** | **str** |  | [optional] 
**manual_rate** | [**ManualRate**](ManualRate.md) |  | [optional] 
**category** | [**VATCategory**](VATCategory.md) |  | [optional] 
**due_date_type_code** | [**VATPointDateCode**](VATPointDateCode.md) |  | [optional] 
**exemption_reason** | **str** |  | [optional] 
**vatex_code** | **str** |  | [optional] 

## Example

```python
from factpulse.models.vat_line import VATLine

# TODO update the JSON string below
json = "{}"
# create an instance of VATLine from a JSON string
vat_line_instance = VATLine.from_json(json)
# print the JSON string representation of the object
print(VATLine.to_json())

# convert the object into a dict
vat_line_dict = vat_line_instance.to_dict()
# create an instance of VATLine from a dict
vat_line_from_dict = VATLine.from_dict(vat_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


