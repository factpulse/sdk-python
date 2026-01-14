# AFNORCreateDirectoryLineBodyPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **date** | Effective start date of the directory line.. | 
**date_to** | **date** | Effective end date of the directory line. | [optional] 

## Example

```python
from factpulse.models.afnor_create_directory_line_body_period import AFNORCreateDirectoryLineBodyPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORCreateDirectoryLineBodyPeriod from a JSON string
afnor_create_directory_line_body_period_instance = AFNORCreateDirectoryLineBodyPeriod.from_json(json)
# print the JSON string representation of the object
print(AFNORCreateDirectoryLineBodyPeriod.to_json())

# convert the object into a dict
afnor_create_directory_line_body_period_dict = afnor_create_directory_line_body_period_instance.to_dict()
# create an instance of AFNORCreateDirectoryLineBodyPeriod from a dict
afnor_create_directory_line_body_period_from_dict = AFNORCreateDirectoryLineBodyPeriod.from_dict(afnor_create_directory_line_body_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


