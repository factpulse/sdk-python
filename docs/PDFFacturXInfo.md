# PDFFacturXInfo

Informations sur le PDF Factur-X généré.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taille** | **int** | Taille du PDF en octets | 
**profil** | **str** | Profil Factur-X utilisé | 
**signe** | **bool** | PDF signé électroniquement | [optional] [default to False]

## Example

```python
from factpulse.models.pdf_factur_x_info import PDFFacturXInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PDFFacturXInfo from a JSON string
pdf_factur_x_info_instance = PDFFacturXInfo.from_json(json)
# print the JSON string representation of the object
print(PDFFacturXInfo.to_json())

# convert the object into a dict
pdf_factur_x_info_dict = pdf_factur_x_info_instance.to_dict()
# create an instance of PDFFacturXInfo from a dict
pdf_factur_x_info_from_dict = PDFFacturXInfo.from_dict(pdf_factur_x_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


