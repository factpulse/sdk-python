# AFNORLegalUnitPayloadHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**siren** | **str** | SIREN number | [optional] 
**business_name** | **str** | Business name | [optional] 
**entity_type** | [**AFNOREntityType**](AFNOREntityType.md) |  | [optional] 
**administrative_status** | [**AFNORLegalUnitAdministrativeStatus**](AFNORLegalUnitAdministrativeStatus.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_legal_unit_payload_history import AFNORLegalUnitPayloadHistory

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORLegalUnitPayloadHistory from a JSON string
afnor_legal_unit_payload_history_instance = AFNORLegalUnitPayloadHistory.from_json(json)
# print the JSON string representation of the object
print(AFNORLegalUnitPayloadHistory.to_json())

# convert the object into a dict
afnor_legal_unit_payload_history_dict = afnor_legal_unit_payload_history_instance.to_dict()
# create an instance of AFNORLegalUnitPayloadHistory from a dict
afnor_legal_unit_payload_history_from_dict = AFNORLegalUnitPayloadHistory.from_dict(afnor_legal_unit_payload_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


