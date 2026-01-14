# FilesInfo

Fichiers generes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facturx_pdf** | [**FileInfo**](FileInfo.md) |  | [optional] 
**xml** | [**FileInfo**](FileInfo.md) |  | [optional] 

## Example

```python
from factpulse.models.files_info import FilesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FilesInfo from a JSON string
files_info_instance = FilesInfo.from_json(json)
# print the JSON string representation of the object
print(FilesInfo.to_json())

# convert the object into a dict
files_info_dict = files_info_instance.to_dict()
# create an instance of FilesInfo from a dict
files_info_from_dict = FilesInfo.from_dict(files_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


