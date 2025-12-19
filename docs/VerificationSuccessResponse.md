# VerificationSuccessResponse

Successful verification response with unified data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_compliant** | **bool** | True if no critical discrepancy | 
**compliance_score** | **float** | Compliance score (0-100%) | 
**verified_fields_count** | **int** | Number of verified fields | [optional] [default to 0]
**compliant_fields_count** | **int** | Number of compliant fields | [optional] [default to 0]
**is_facturx** | **bool** | True if PDF contains Factur-X XML | [optional] [default to False]
**facturx_profile** | **str** |  | [optional] 
**fields** | [**List[VerifiedFieldSchema]**](VerifiedFieldSchema.md) | List of verified fields with values, statuses and PDF coordinates | [optional] 
**mandatory_notes** | [**List[MandatoryNoteSchema]**](MandatoryNoteSchema.md) | Mandatory notes (PMT, PMD, AAB) with PDF location | [optional] 
**page_dimensions** | [**List[PageDimensionsSchema]**](PageDimensionsSchema.md) | Dimensions of each PDF page (width, height) | [optional] 
**warnings** | **List[str]** | Non-blocking warnings | [optional] 

## Example

```python
from factpulse.models.verification_success_response import VerificationSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationSuccessResponse from a JSON string
verification_success_response_instance = VerificationSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(VerificationSuccessResponse.to_json())

# convert the object into a dict
verification_success_response_dict = verification_success_response_instance.to_dict()
# create an instance of VerificationSuccessResponse from a dict
verification_success_response_from_dict = VerificationSuccessResponse.from_dict(verification_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


