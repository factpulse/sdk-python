# AFNORFacilityPayloadIncluded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**siret** | **str** | SIRET Number | [optional] 
**siren** | **str** | SIREN number | [optional] 
**name** | **str** | business name | [optional] 
**facility_type** | [**AFNORFacilityType**](AFNORFacilityType.md) |  | [optional] 
**diffusible** | [**AFNORDiffusionStatus**](AFNORDiffusionStatus.md) |  | [optional] 
**administrative_status** | [**AFNORFacilityAdministrativeStatus**](AFNORFacilityAdministrativeStatus.md) |  | [optional] 
**address** | [**AFNORAddressRead**](AFNORAddressRead.md) |  | [optional] 
**b2g_additional_data** | [**AFNORFacilityPayloadHistoryUleB2gAdditionalData**](AFNORFacilityPayloadHistoryUleB2gAdditionalData.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_facility_payload_included import AFNORFacilityPayloadIncluded

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORFacilityPayloadIncluded from a JSON string
afnor_facility_payload_included_instance = AFNORFacilityPayloadIncluded.from_json(json)
# print the JSON string representation of the object
print(AFNORFacilityPayloadIncluded.to_json())

# convert the object into a dict
afnor_facility_payload_included_dict = afnor_facility_payload_included_instance.to_dict()
# create an instance of AFNORFacilityPayloadIncluded from a dict
afnor_facility_payload_included_from_dict = AFNORFacilityPayloadIncluded.from_dict(afnor_facility_payload_included_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


