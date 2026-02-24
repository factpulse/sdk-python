# VATEXCodeInfo

Single VATEX code entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | VATEX code (e.g. VATEX-EU-IC) | 
**name** | **str** | Short name (e.g. &#39;Intra-Community supply&#39;) | 
**description** | **str** | Detailed description / remark | 
**category** | **str** | Associated VAT category code (E, AE, K, G, O) | 

## Example

```python
from factpulse.models.vatex_code_info import VATEXCodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VATEXCodeInfo from a JSON string
vatex_code_info_instance = VATEXCodeInfo.from_json(json)
# print the JSON string representation of the object
print(VATEXCodeInfo.to_json())

# convert the object into a dict
vatex_code_info_dict = vatex_code_info_instance.to_dict()
# create an instance of VATEXCodeInfo from a dict
vatex_code_info_from_dict = VATEXCodeInfo.from_dict(vatex_code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


