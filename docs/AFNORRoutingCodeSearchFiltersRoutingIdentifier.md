# AFNORRoutingCodeSearchFiltersRoutingIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORContainsOperator**](AFNORContainsOperator.md) |  | [optional] 
**value** | **str** | Routing identifier for a routing code. | [optional] 

## Example

```python
from factpulse.models.afnor_routing_code_search_filters_routing_identifier import AFNORRoutingCodeSearchFiltersRoutingIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORRoutingCodeSearchFiltersRoutingIdentifier from a JSON string
afnor_routing_code_search_filters_routing_identifier_instance = AFNORRoutingCodeSearchFiltersRoutingIdentifier.from_json(json)
# print the JSON string representation of the object
print(AFNORRoutingCodeSearchFiltersRoutingIdentifier.to_json())

# convert the object into a dict
afnor_routing_code_search_filters_routing_identifier_dict = afnor_routing_code_search_filters_routing_identifier_instance.to_dict()
# create an instance of AFNORRoutingCodeSearchFiltersRoutingIdentifier from a dict
afnor_routing_code_search_filters_routing_identifier_from_dict = AFNORRoutingCodeSearchFiltersRoutingIdentifier.from_dict(afnor_routing_code_search_filters_routing_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


