# AFNORDirectoryLineSearchPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | [**AFNORSearchDirectoryLine**](AFNORSearchDirectoryLine.md) |  | [optional] 
**total_number_of_results** | **int** | The total number of results | [optional] 
**results** | [**List[AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode]**](AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_directory_line_search_post200_response import AFNORDirectoryLineSearchPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORDirectoryLineSearchPost200Response from a JSON string
afnor_directory_line_search_post200_response_instance = AFNORDirectoryLineSearchPost200Response.from_json(json)
# print the JSON string representation of the object
print(AFNORDirectoryLineSearchPost200Response.to_json())

# convert the object into a dict
afnor_directory_line_search_post200_response_dict = afnor_directory_line_search_post200_response_instance.to_dict()
# create an instance of AFNORDirectoryLineSearchPost200Response from a dict
afnor_directory_line_search_post200_response_from_dict = AFNORDirectoryLineSearchPost200Response.from_dict(afnor_directory_line_search_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


