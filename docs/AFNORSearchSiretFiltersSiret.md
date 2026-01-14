# AFNORSearchSiretFiltersSiret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORContainsOperator**](AFNORContainsOperator.md) |  | [optional] 
**value** | **str** | SIRET number to search for. | [optional] 

## Example

```python
from factpulse.models.afnor_search_siret_filters_siret import AFNORSearchSiretFiltersSiret

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSiretFiltersSiret from a JSON string
afnor_search_siret_filters_siret_instance = AFNORSearchSiretFiltersSiret.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSiretFiltersSiret.to_json())

# convert the object into a dict
afnor_search_siret_filters_siret_dict = afnor_search_siret_filters_siret_instance.to_dict()
# create an instance of AFNORSearchSiretFiltersSiret from a dict
afnor_search_siret_filters_siret_from_dict = AFNORSearchSiretFiltersSiret.from_dict(afnor_search_siret_filters_siret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


