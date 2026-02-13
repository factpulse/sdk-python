# ParseFacturXResponse

Response from the /parse-facturx endpoint.  Contains the parsed invoice data, plus metadata about the detected format and profile.  **Response schema depends on source format:** - **CII / Factur-X**: ``invoice`` contains a ``FacturXInvoice`` dict — round-trip compatible   with ``/generate-invoice``. - **UBL**: ``invoice`` contains an ``IncomingInvoice`` dict (simplified extraction with   supplier, amounts, dates). Not directly compatible with ``/generate-invoice``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Parsing status | 
**invoice** | **Dict[str, object]** | Parsed invoice data. For CII/Factur-X: FacturXInvoice format (round-trip with /generate-invoice). For UBL: IncomingInvoice format (summary extraction). | 
**detected_format** | **str** |  | [optional] 
**detected_profile** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from factpulse.models.parse_factur_x_response import ParseFacturXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ParseFacturXResponse from a JSON string
parse_factur_x_response_instance = ParseFacturXResponse.from_json(json)
# print the JSON string representation of the object
print(ParseFacturXResponse.to_json())

# convert the object into a dict
parse_factur_x_response_dict = parse_factur_x_response_instance.to_dict()
# create an instance of ParseFacturXResponse from a dict
parse_factur_x_response_from_dict = ParseFacturXResponse.from_dict(parse_factur_x_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


