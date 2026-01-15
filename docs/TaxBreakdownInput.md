# TaxBreakdownInput

VAT breakdown for a transaction or invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | [**Rate1**](Rate1.md) |  | 
**taxable_amount** | [**Taxableamount**](Taxableamount.md) |  | 
**tax_amount** | [**Taxamount2**](Taxamount2.md) |  | 

## Example

```python
from factpulse.models.tax_breakdown_input import TaxBreakdownInput

# TODO update the JSON string below
json = "{}"
# create an instance of TaxBreakdownInput from a JSON string
tax_breakdown_input_instance = TaxBreakdownInput.from_json(json)
# print the JSON string representation of the object
print(TaxBreakdownInput.to_json())

# convert the object into a dict
tax_breakdown_input_dict = tax_breakdown_input_instance.to_dict()
# create an instance of TaxBreakdownInput from a dict
tax_breakdown_input_from_dict = TaxBreakdownInput.from_dict(tax_breakdown_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


