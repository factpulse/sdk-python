# GenerateCDARResponse

Réponse de génération de message CDAR.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | 
**xml** | **str** | XML CDAR généré | 
**xml_size** | **int** | Taille du XML en octets | 
**sha256** | **str** | Hash SHA256 du XML | 
**message** | **str** | Message de succès | 

## Example

```python
from factpulse.models.generate_cdar_response import GenerateCDARResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateCDARResponse from a JSON string
generate_cdar_response_instance = GenerateCDARResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateCDARResponse.to_json())

# convert the object into a dict
generate_cdar_response_dict = generate_cdar_response_instance.to_dict()
# create an instance of GenerateCDARResponse from a dict
generate_cdar_response_from_dict = GenerateCDARResponse.from_dict(generate_cdar_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


