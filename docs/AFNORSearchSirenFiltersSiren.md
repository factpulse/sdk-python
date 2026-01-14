# AFNORSearchSirenFiltersSiren


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORContainsOperator**](AFNORContainsOperator.md) |  | [optional] 
**value** | **str** | SIREN number to search for. | [optional] 

## Example

```python
from factpulse.models.afnor_search_siren_filters_siren import AFNORSearchSirenFiltersSiren

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSirenFiltersSiren from a JSON string
afnor_search_siren_filters_siren_instance = AFNORSearchSirenFiltersSiren.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSirenFiltersSiren.to_json())

# convert the object into a dict
afnor_search_siren_filters_siren_dict = afnor_search_siren_filters_siren_instance.to_dict()
# create an instance of AFNORSearchSirenFiltersSiren from a dict
afnor_search_siren_filters_siren_from_dict = AFNORSearchSirenFiltersSiren.from_dict(afnor_search_siren_filters_siren_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


