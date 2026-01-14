# AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressing_identifier** | **str** | Addressing identifier of the directory line. | [optional] 
**siren** | **str** | SIREN number | [optional] 
**siret** | **str** | SIRET Number | [optional] 
**addressing_suffix** | **str** | suffix of the directory line which defines an address mesh not attached to a facility | [optional] 
**routing_code** | [**AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCodeRoutingCode**](AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCodeRoutingCode.md) |  | [optional] 
**platform** | [**AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCodePlatform**](AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCodePlatform.md) |  | [optional] 
**legal_unit** | [**AFNORLegalUnitPayloadIncludedNoSiren**](AFNORLegalUnitPayloadIncludedNoSiren.md) |  | [optional] 
**facility** | [**AFNORFacilityPayloadIncluded**](AFNORFacilityPayloadIncluded.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_directory_line_payload_history_legal_unit_facility_routing_code import AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode from a JSON string
afnor_directory_line_payload_history_legal_unit_facility_routing_code_instance = AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode.from_json(json)
# print the JSON string representation of the object
print(AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode.to_json())

# convert the object into a dict
afnor_directory_line_payload_history_legal_unit_facility_routing_code_dict = afnor_directory_line_payload_history_legal_unit_facility_routing_code_instance.to_dict()
# create an instance of AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode from a dict
afnor_directory_line_payload_history_legal_unit_facility_routing_code_from_dict = AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode.from_dict(afnor_directory_line_payload_history_legal_unit_facility_routing_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


