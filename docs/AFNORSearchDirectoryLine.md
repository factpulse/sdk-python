# AFNORSearchDirectoryLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**AFNORSearchDirectoryLineFilters**](AFNORSearchDirectoryLineFilters.md) |  | [optional] 
**sorting** | [**List[AFNORSearchDirectoryLineSortingInner]**](AFNORSearchDirectoryLineSortingInner.md) | Sorting criteria on a field and an order (ascending or descending). | [optional] 
**fields** | [**List[AFNORDirectoryLineField]**](AFNORDirectoryLineField.md) | Allows you to filter the desired fields in the response. | [optional] 
**limit** | **int** | Maximum number of results | [optional] 
**ignore** | **int** | Number of results to skip | [optional] 

## Example

```python
from factpulse.models.afnor_search_directory_line import AFNORSearchDirectoryLine

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchDirectoryLine from a JSON string
afnor_search_directory_line_instance = AFNORSearchDirectoryLine.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchDirectoryLine.to_json())

# convert the object into a dict
afnor_search_directory_line_dict = afnor_search_directory_line_instance.to_dict()
# create an instance of AFNORSearchDirectoryLine from a dict
afnor_search_directory_line_from_dict = AFNORSearchDirectoryLine.from_dict(afnor_search_directory_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


