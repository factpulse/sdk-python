# AFNORSirenInstructions

Instructions regarding the SIREN

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_sales_prospecting_forbidden** | **bool** | Indicates whether the information is forbidden from being used for sales prospecting purposes. | [optional] 

## Example

```python
from factpulse.models.afnor_siren_instructions import AFNORSirenInstructions

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSirenInstructions from a JSON string
afnor_siren_instructions_instance = AFNORSirenInstructions.from_json(json)
# print the JSON string representation of the object
print(AFNORSirenInstructions.to_json())

# convert the object into a dict
afnor_siren_instructions_dict = afnor_siren_instructions_instance.to_dict()
# create an instance of AFNORSirenInstructions from a dict
afnor_siren_instructions_from_dict = AFNORSirenInstructions.from_dict(afnor_siren_instructions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


