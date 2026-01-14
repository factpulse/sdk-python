# AFNORLegalUnitPayloadIncludedNoSiren


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_name** | **str** | Business name | [optional] 
**entity_type** | [**AFNOREntityType**](AFNOREntityType.md) |  | [optional] 
**administrative_status** | [**AFNORLegalUnitAdministrativeStatus**](AFNORLegalUnitAdministrativeStatus.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_legal_unit_payload_included_no_siren import AFNORLegalUnitPayloadIncludedNoSiren

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORLegalUnitPayloadIncludedNoSiren from a JSON string
afnor_legal_unit_payload_included_no_siren_instance = AFNORLegalUnitPayloadIncludedNoSiren.from_json(json)
# print the JSON string representation of the object
print(AFNORLegalUnitPayloadIncludedNoSiren.to_json())

# convert the object into a dict
afnor_legal_unit_payload_included_no_siren_dict = afnor_legal_unit_payload_included_no_siren_instance.to_dict()
# create an instance of AFNORLegalUnitPayloadIncludedNoSiren from a dict
afnor_legal_unit_payload_included_no_siren_from_dict = AFNORLegalUnitPayloadIncludedNoSiren.from_dict(afnor_legal_unit_payload_included_no_siren_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


