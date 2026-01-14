# AFNORCreateDirectoryLineBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**AFNORCreateDirectoryLineBodyPeriod**](AFNORCreateDirectoryLineBodyPeriod.md) |  | [optional] 
**addressing_information** | [**AFNORCreateDirectoryLineBodyAddressingInformation**](AFNORCreateDirectoryLineBodyAddressingInformation.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_create_directory_line_body import AFNORCreateDirectoryLineBody

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORCreateDirectoryLineBody from a JSON string
afnor_create_directory_line_body_instance = AFNORCreateDirectoryLineBody.from_json(json)
# print the JSON string representation of the object
print(AFNORCreateDirectoryLineBody.to_json())

# convert the object into a dict
afnor_create_directory_line_body_dict = afnor_create_directory_line_body_instance.to_dict()
# create an instance of AFNORCreateDirectoryLineBody from a dict
afnor_create_directory_line_body_from_dict = AFNORCreateDirectoryLineBody.from_dict(afnor_create_directory_line_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


