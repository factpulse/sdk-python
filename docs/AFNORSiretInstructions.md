# AFNORSiretInstructions

Instructions regarding the SIRET

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_sales_prospecting_forbidden** | **bool** | Indicates whether the information is forbidden from being used for sales prospecting purposes. | [optional] 

## Example

```python
from factpulse.models.afnor_siret_instructions import AFNORSiretInstructions

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSiretInstructions from a JSON string
afnor_siret_instructions_instance = AFNORSiretInstructions.from_json(json)
# print the JSON string representation of the object
print(AFNORSiretInstructions.to_json())

# convert the object into a dict
afnor_siret_instructions_dict = afnor_siret_instructions_instance.to_dict()
# create an instance of AFNORSiretInstructions from a dict
afnor_siret_instructions_from_dict = AFNORSiretInstructions.from_dict(afnor_siret_instructions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


