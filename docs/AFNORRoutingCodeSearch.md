# AFNORRoutingCodeSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**AFNORRoutingCodeSearchFilters**](AFNORRoutingCodeSearchFilters.md) |  | [optional] 
**sorting** | [**List[AFNORRoutingCodeSearchSortingInner]**](AFNORRoutingCodeSearchSortingInner.md) | Sorting criteria on a field and an order (ascending or descending). | [optional] 
**fields** | [**List[AFNORRoutingCodeField]**](AFNORRoutingCodeField.md) | Allows you to filter the desired fields in the response. | [optional] 
**include** | **List[str]** |  | [optional] 
**limit** | **int** | Maximum number of results | [optional] 
**ignore** | **int** | Number of results to skip | [optional] 

## Example

```python
from factpulse.models.afnor_routing_code_search import AFNORRoutingCodeSearch

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORRoutingCodeSearch from a JSON string
afnor_routing_code_search_instance = AFNORRoutingCodeSearch.from_json(json)
# print the JSON string representation of the object
print(AFNORRoutingCodeSearch.to_json())

# convert the object into a dict
afnor_routing_code_search_dict = afnor_routing_code_search_instance.to_dict()
# create an instance of AFNORRoutingCodeSearch from a dict
afnor_routing_code_search_from_dict = AFNORRoutingCodeSearch.from_dict(afnor_routing_code_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


