# AFNORDirectoryLinePost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_instance** | **int** | Platform instance identifier in the directory | [optional] 
**addressing_identifier** | **str** | Addressing identifier of the directory line. | [optional] 
**date_from** | **date** | Effective start date of the directory line.. | [optional] 

## Example

```python
from factpulse.models.afnor_directory_line_post201_response import AFNORDirectoryLinePost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORDirectoryLinePost201Response from a JSON string
afnor_directory_line_post201_response_instance = AFNORDirectoryLinePost201Response.from_json(json)
# print the JSON string representation of the object
print(AFNORDirectoryLinePost201Response.to_json())

# convert the object into a dict
afnor_directory_line_post201_response_dict = afnor_directory_line_post201_response_instance.to_dict()
# create an instance of AFNORDirectoryLinePost201Response from a dict
afnor_directory_line_post201_response_from_dict = AFNORDirectoryLinePost201Response.from_dict(afnor_directory_line_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


