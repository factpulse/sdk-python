# AFNORSirenSearchPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | [**AFNORSearchSiren**](AFNORSearchSiren.md) |  | [optional] 
**total_number_of_results** | **int** | The total number of results | [optional] 
**results** | [**List[AFNORLegalUnitPayloadHistory]**](AFNORLegalUnitPayloadHistory.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_siren_search_post200_response import AFNORSirenSearchPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSirenSearchPost200Response from a JSON string
afnor_siren_search_post200_response_instance = AFNORSirenSearchPost200Response.from_json(json)
# print the JSON string representation of the object
print(AFNORSirenSearchPost200Response.to_json())

# convert the object into a dict
afnor_siren_search_post200_response_dict = afnor_siren_search_post200_response_instance.to_dict()
# create an instance of AFNORSirenSearchPost200Response from a dict
afnor_siren_search_post200_response_from_dict = AFNORSirenSearchPost200Response.from_dict(afnor_siren_search_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


