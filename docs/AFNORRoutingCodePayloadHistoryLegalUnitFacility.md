# AFNORRoutingCodePayloadHistoryLegalUnitFacility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_identifier** | **str** | Routing identifier od a routing code. | [optional] 
**siret** | **str** | SIRET Number | [optional] 
**routing_identifier_type** | **str** | Routing Identifier type. | [optional] 
**routing_code_name** | **str** | Name of the directory line routing code. This attribute is only returned if the directory line is defined at the SIREN / SIRET / Routing code mesh. | [optional] 
**manages_legal_commitment_code** | **bool** | Indicates whether the public structure requires a legal commitment number. This attribute is only returned if the directory line is defined for a public structure at the SIREN / SIRET or SIREN / SIRET / Routing code level. | [optional] 
**administrative_status** | [**AFNORRoutingCodeAdministrativeStatus**](AFNORRoutingCodeAdministrativeStatus.md) |  | [optional] 
**address** | [**AFNORAddressRead**](AFNORAddressRead.md) |  | [optional] 
**legal_unit** | [**AFNORLegalUnitPayloadIncluded**](AFNORLegalUnitPayloadIncluded.md) |  | [optional] 
**facility** | [**AFNORFacilityPayloadIncluded**](AFNORFacilityPayloadIncluded.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_routing_code_payload_history_legal_unit_facility import AFNORRoutingCodePayloadHistoryLegalUnitFacility

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORRoutingCodePayloadHistoryLegalUnitFacility from a JSON string
afnor_routing_code_payload_history_legal_unit_facility_instance = AFNORRoutingCodePayloadHistoryLegalUnitFacility.from_json(json)
# print the JSON string representation of the object
print(AFNORRoutingCodePayloadHistoryLegalUnitFacility.to_json())

# convert the object into a dict
afnor_routing_code_payload_history_legal_unit_facility_dict = afnor_routing_code_payload_history_legal_unit_facility_instance.to_dict()
# create an instance of AFNORRoutingCodePayloadHistoryLegalUnitFacility from a dict
afnor_routing_code_payload_history_legal_unit_facility_from_dict = AFNORRoutingCodePayloadHistoryLegalUnitFacility.from_dict(afnor_routing_code_payload_history_legal_unit_facility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


