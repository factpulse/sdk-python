# TaxRepresentative

Seller tax representative (BG-11).  The tax representative is required when the seller is not established in the country where VAT is due.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tax representative name (BT-62). | 
**vat_number** | **str** | Tax representative VAT identifier (BT-63). | 
**postal_address** | [**PostalAddress**](PostalAddress.md) | Tax representative postal address (BG-12). | 

## Example

```python
from factpulse.models.tax_representative import TaxRepresentative

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRepresentative from a JSON string
tax_representative_instance = TaxRepresentative.from_json(json)
# print the JSON string representation of the object
print(TaxRepresentative.to_json())

# convert the object into a dict
tax_representative_dict = tax_representative_instance.to_dict()
# create an instance of TaxRepresentative from a dict
tax_representative_from_dict = TaxRepresentative.from_dict(tax_representative_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


