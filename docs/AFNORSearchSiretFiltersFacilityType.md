# AFNORSearchSiretFiltersFacilityType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORContainsOperator**](AFNORContainsOperator.md) |  | [optional] 
**value** | [**AFNORFacilityType**](AFNORFacilityType.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_search_siret_filters_facility_type import AFNORSearchSiretFiltersFacilityType

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSiretFiltersFacilityType from a JSON string
afnor_search_siret_filters_facility_type_instance = AFNORSearchSiretFiltersFacilityType.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSiretFiltersFacilityType.to_json())

# convert the object into a dict
afnor_search_siret_filters_facility_type_dict = afnor_search_siret_filters_facility_type_instance.to_dict()
# create an instance of AFNORSearchSiretFiltersFacilityType from a dict
afnor_search_siret_filters_facility_type_from_dict = AFNORSearchSiretFiltersFacilityType.from_dict(afnor_search_siret_filters_facility_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


