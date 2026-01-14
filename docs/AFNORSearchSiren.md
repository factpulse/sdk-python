# AFNORSearchSiren


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**AFNORSearchSirenFilters**](AFNORSearchSirenFilters.md) |  | [optional] 
**sorting** | [**List[AFNORSearchSirenSortingInner]**](AFNORSearchSirenSortingInner.md) | Sorting criteria on a field and an order (ascending or descending). | [optional] 
**fields** | [**List[AFNORSirenField]**](AFNORSirenField.md) | Allows you to filter the desired fields in the response. | [optional] 
**limit** | **int** | Maximum number of results | [optional] 
**ignore** | **int** | Number of results to skip | [optional] 

## Example

```python
from factpulse.models.afnor_search_siren import AFNORSearchSiren

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSiren from a JSON string
afnor_search_siren_instance = AFNORSearchSiren.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSiren.to_json())

# convert the object into a dict
afnor_search_siren_dict = afnor_search_siren_instance.to_dict()
# create an instance of AFNORSearchSiren from a dict
afnor_search_siren_from_dict = AFNORSearchSiren.from_dict(afnor_search_siren_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


