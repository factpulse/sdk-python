# AFNORSiretSearchPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | [**AFNORSearchSiret**](AFNORSearchSiret.md) |  | [optional] 
**total_number_of_results** | **int** | The total number of results | [optional] 
**results** | [**List[AFNORFacilityPayloadHistory]**](AFNORFacilityPayloadHistory.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_siret_search_post200_response import AFNORSiretSearchPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSiretSearchPost200Response from a JSON string
afnor_siret_search_post200_response_instance = AFNORSiretSearchPost200Response.from_json(json)
# print the JSON string representation of the object
print(AFNORSiretSearchPost200Response.to_json())

# convert the object into a dict
afnor_siret_search_post200_response_dict = afnor_siret_search_post200_response_instance.to_dict()
# create an instance of AFNORSiretSearchPost200Response from a dict
afnor_siret_search_post200_response_from_dict = AFNORSiretSearchPost200Response.from_dict(afnor_siret_search_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


