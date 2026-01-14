# AFNORCreateDirectoryLineBodyAddressingInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**siren** | **str** | SIREN number | 
**siret** | **str** | SIRET Number | [optional] 
**routing_identifier** | **str** | Routing identifier od a routing code. | [optional] 
**addressing_suffix** | **str** | suffix of the directory line which defines an address mesh not attached to a facility | [optional] 

## Example

```python
from factpulse.models.afnor_create_directory_line_body_addressing_information import AFNORCreateDirectoryLineBodyAddressingInformation

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORCreateDirectoryLineBodyAddressingInformation from a JSON string
afnor_create_directory_line_body_addressing_information_instance = AFNORCreateDirectoryLineBodyAddressingInformation.from_json(json)
# print the JSON string representation of the object
print(AFNORCreateDirectoryLineBodyAddressingInformation.to_json())

# convert the object into a dict
afnor_create_directory_line_body_addressing_information_dict = afnor_create_directory_line_body_addressing_information_instance.to_dict()
# create an instance of AFNORCreateDirectoryLineBodyAddressingInformation from a dict
afnor_create_directory_line_body_addressing_information_from_dict = AFNORCreateDirectoryLineBodyAddressingInformation.from_dict(afnor_create_directory_line_body_addressing_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


