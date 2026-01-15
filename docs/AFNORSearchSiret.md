# AFNORSearchSiret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**AFNORSearchSiretFilters**](AFNORSearchSiretFilters.md) |  | [optional] 
**sorting** | [**List[AFNORSearchSiretSortingInner]**](AFNORSearchSiretSortingInner.md) | Sorting criteria on a field and an order (ascending or descending). | [optional] 
**fields** | [**List[AFNORSiretField]**](AFNORSiretField.md) | Allows you to filter the desired fields in the response. | [optional] 
**include** | **List[str]** |  | [optional] 
**limit** | **int** | Maximum number of results | [optional] 
**ignore** | **int** | Number of results to skip | [optional] 

## Example

```python
from factpulse.models.afnor_search_siret import AFNORSearchSiret

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSiret from a JSON string
afnor_search_siret_instance = AFNORSearchSiret.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSiret.to_json())

# convert the object into a dict
afnor_search_siret_dict = afnor_search_siret_instance.to_dict()
# create an instance of AFNORSearchSiret from a dict
afnor_search_siret_from_dict = AFNORSearchSiret.from_dict(afnor_search_siret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


