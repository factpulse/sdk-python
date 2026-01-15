# AFNORSearchSiretFiltersLocality


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORContainsOperator**](AFNORContainsOperator.md) |  | [optional] 
**value** | **str** | Municipality of the recipient structure having defined the directory line(s). | [optional] 

## Example

```python
from factpulse.models.afnor_search_siret_filters_locality import AFNORSearchSiretFiltersLocality

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSiretFiltersLocality from a JSON string
afnor_search_siret_filters_locality_instance = AFNORSearchSiretFiltersLocality.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSiretFiltersLocality.to_json())

# convert the object into a dict
afnor_search_siret_filters_locality_dict = afnor_search_siret_filters_locality_instance.to_dict()
# create an instance of AFNORSearchSiretFiltersLocality from a dict
afnor_search_siret_filters_locality_from_dict = AFNORSearchSiretFiltersLocality.from_dict(afnor_search_siret_filters_locality_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


