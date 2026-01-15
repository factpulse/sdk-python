# AFNORSearchSirenFiltersBusinessName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORContainsOperator**](AFNORContainsOperator.md) |  | [optional] 
**value** | **str** | Business name | [optional] 

## Example

```python
from factpulse.models.afnor_search_siren_filters_business_name import AFNORSearchSirenFiltersBusinessName

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSirenFiltersBusinessName from a JSON string
afnor_search_siren_filters_business_name_instance = AFNORSearchSirenFiltersBusinessName.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSirenFiltersBusinessName.to_json())

# convert the object into a dict
afnor_search_siren_filters_business_name_dict = afnor_search_siren_filters_business_name_instance.to_dict()
# create an instance of AFNORSearchSirenFiltersBusinessName from a dict
afnor_search_siren_filters_business_name_from_dict = AFNORSearchSirenFiltersBusinessName.from_dict(afnor_search_siren_filters_business_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


