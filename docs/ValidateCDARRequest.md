# ValidateCDARRequest

Requête de validation CDAR.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | [optional] 
**sender_siren** | **str** |  | [optional] 
**sender_role** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**invoice_issue_date** | **date** |  | [optional] 
**status** | **str** |  | [optional] 
**reason_code** | **str** |  | [optional] 
**encaisse_amount** | [**Encaisseamount1**](Encaisseamount1.md) |  | [optional] 

## Example

```python
from factpulse.models.validate_cdar_request import ValidateCDARRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateCDARRequest from a JSON string
validate_cdar_request_instance = ValidateCDARRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateCDARRequest.to_json())

# convert the object into a dict
validate_cdar_request_dict = validate_cdar_request_instance.to_dict()
# create an instance of ValidateCDARRequest from a dict
validate_cdar_request_from_dict = ValidateCDARRequest.from_dict(validate_cdar_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


