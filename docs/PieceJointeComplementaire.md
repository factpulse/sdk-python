# PieceJointeComplementaire

Représente une pièce jointe complémentaire.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**designation** | **str** |  | 
**id** | **int** |  | 
**id_liaison** | **int** |  | 
**numero_ligne_facture** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from factpulse.models.piece_jointe_complementaire import PieceJointeComplementaire

# TODO update the JSON string below
json = "{}"
# create an instance of PieceJointeComplementaire from a JSON string
piece_jointe_complementaire_instance = PieceJointeComplementaire.from_json(json)
# print the JSON string representation of the object
print(PieceJointeComplementaire.to_json())

# convert the object into a dict
piece_jointe_complementaire_dict = piece_jointe_complementaire_instance.to_dict()
# create an instance of PieceJointeComplementaire from a dict
piece_jointe_complementaire_from_dict = PieceJointeComplementaire.from_dict(piece_jointe_complementaire_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


