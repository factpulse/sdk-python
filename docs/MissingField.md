# MissingField

Champ manquant requis pour la conformite.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Nom du champ | 
**bt_code** | **str** | Code Business Term (BT-XX) | 
**description** | **str** | Description du champ | 
**required_for** | **List[str]** | Profils necessitant ce champ | 
**suggested_value** | **str** |  | [optional] 
**confidence** | **float** |  | [optional] 

## Example

```python
from factpulse.models.missing_field import MissingField

# TODO update the JSON string below
json = "{}"
# create an instance of MissingField from a JSON string
missing_field_instance = MissingField.from_json(json)
# print the JSON string representation of the object
print(MissingField.to_json())

# convert the object into a dict
missing_field_dict = missing_field_instance.to_dict()
# create an instance of MissingField from a dict
missing_field_from_dict = MissingField.from_dict(missing_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


