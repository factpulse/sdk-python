# PDFValidationResultAPI

Complete result of a Factur-X PDF validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_compliant** | **bool** | True if PDF complies with all criteria (XML, PDF/A, XMP) | 
**xml_present** | **bool** | True if a Factur-X XML is embedded in the PDF | 
**xml_compliant** | **bool** | True if Factur-X XML complies with Schematron rules | 
**detected_profile** | **str** |  | [optional] 
**xml_errors** | **List[str]** | List of XML validation errors | [optional] 
**pdfa_compliant** | **bool** | True if PDF is PDF/A compliant | 
**pdfa_version** | **str** |  | [optional] 
**pdfa_validation_method** | **str** | Method used for PDF/A validation (metadata or verapdf) | [optional] [default to 'metadata']
**validated_rules** | **int** |  | [optional] 
**failed_rules** | **int** |  | [optional] 
**pdfa_errors** | **List[str]** | List of PDF/A compliance errors | [optional] 
**pdfa_warnings** | **List[str]** | List of PDF/A warnings | [optional] 
**xmp_present** | **bool** | True if XMP metadata is present | 
**xmp_facturx_compliant** | **bool** | True if XMP metadata contains Factur-X information | 
**xmp_profile** | **str** |  | [optional] 
**xmp_version** | **str** |  | [optional] 
**xmp_errors** | **List[str]** | List of XMP metadata errors | [optional] 
**xmp_metadata** | **Dict[str, object]** | XMP metadata extracted from PDF | [optional] 
**is_signed** | **bool** | True if PDF contains at least one signature | 
**signature_count** | **int** | Number of electronic signatures found | [optional] [default to 0]
**signatures** | [**List[SignatureInfoAPI]**](SignatureInfoAPI.md) | List of found signatures with their information | [optional] 
**signature_errors** | **List[str]** | List of errors during signature analysis | [optional] 
**summary_message** | **str** | Message summarizing the validation result | 

## Example

```python
from factpulse.models.pdf_validation_result_api import PDFValidationResultAPI

# TODO update the JSON string below
json = "{}"
# create an instance of PDFValidationResultAPI from a JSON string
pdf_validation_result_api_instance = PDFValidationResultAPI.from_json(json)
# print the JSON string representation of the object
print(PDFValidationResultAPI.to_json())

# convert the object into a dict
pdf_validation_result_api_dict = pdf_validation_result_api_instance.to_dict()
# create an instance of PDFValidationResultAPI from a dict
pdf_validation_result_api_from_dict = PDFValidationResultAPI.from_dict(pdf_validation_result_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


