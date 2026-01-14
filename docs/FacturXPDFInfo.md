# FacturXPDFInfo

Information about the generated Factur-X PDF.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | PDF size in bytes | 
**profile** | **str** | Factur-X profile used | 
**signed** | **bool** | PDF electronically signed | [optional] [default to False]

## Example

```python
from factpulse.models.factur_xpdf_info import FacturXPDFInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FacturXPDFInfo from a JSON string
factur_xpdf_info_instance = FacturXPDFInfo.from_json(json)
# print the JSON string representation of the object
print(FacturXPDFInfo.to_json())

# convert the object into a dict
factur_xpdf_info_dict = factur_xpdf_info_instance.to_dict()
# create an instance of FacturXPDFInfo from a dict
factur_xpdf_info_from_dict = FacturXPDFInfo.from_dict(factur_xpdf_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


