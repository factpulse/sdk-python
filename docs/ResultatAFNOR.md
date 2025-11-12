# ResultatAFNOR

Résultat de la soumission à AFNOR PDP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | Identifiant du flux soumis | 
**tracking_id** | **str** |  | [optional] 
**sha256** | **str** | Hash SHA-256 du fichier soumis | 
**flow_syntax** | **str** | Syntaxe du flux | 
**flow_profile** | **str** |  | [optional] 

## Example

```python
from factpulse.models.resultat_afnor import ResultatAFNOR

# TODO update the JSON string below
json = "{}"
# create an instance of ResultatAFNOR from a JSON string
resultat_afnor_instance = ResultatAFNOR.from_json(json)
# print the JSON string representation of the object
print(ResultatAFNOR.to_json())

# convert the object into a dict
resultat_afnor_dict = resultat_afnor_instance.to_dict()
# create an instance of ResultatAFNOR from a dict
resultat_afnor_from_dict = ResultatAFNOR.from_dict(resultat_afnor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


