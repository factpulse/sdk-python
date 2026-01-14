# AFNORCreateRoutingCodeBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_nature** | [**AFNORFacilityNature**](AFNORFacilityNature.md) |  | 
**routing_identifier** | **str** | Routing identifier od a routing code. | 
**siret** | **str** | SIRET Number | 
**routing_identifier_type** | **str** | Routing Identifier type. | [optional] 
**routing_code_name** | **str** | Name of the directory line routing code. This attribute is only returned if the directory line is defined at the SIREN / SIRET / Routing code mesh. | 
**manages_legal_commitment_code** | **bool** | Indicates whether the public structure requires a legal commitment number. This attribute is only returned if the directory line is defined for a public structure at the SIREN / SIRET or SIREN / SIRET / Routing code level. | [optional] 
**administrative_status** | [**AFNORRoutingCodeAdministrativeStatus**](AFNORRoutingCodeAdministrativeStatus.md) |  | 
**address** | [**AFNORAddressEdit**](AFNORAddressEdit.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_create_routing_code_body import AFNORCreateRoutingCodeBody

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORCreateRoutingCodeBody from a JSON string
afnor_create_routing_code_body_instance = AFNORCreateRoutingCodeBody.from_json(json)
# print the JSON string representation of the object
print(AFNORCreateRoutingCodeBody.to_json())

# convert the object into a dict
afnor_create_routing_code_body_dict = afnor_create_routing_code_body_instance.to_dict()
# create an instance of AFNORCreateRoutingCodeBody from a dict
afnor_create_routing_code_body_from_dict = AFNORCreateRoutingCodeBody.from_dict(afnor_create_routing_code_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


