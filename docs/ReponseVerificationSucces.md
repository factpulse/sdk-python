# ReponseVerificationSucces

Réponse de vérification réussie avec données unifiées.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**est_conforme** | **bool** | True si aucun écart critique | 
**score_conformite** | **float** | Score de conformité (0-100%) | 
**champs_verifies** | **int** | Nombre de champs vérifiés | [optional] [default to 0]
**champs_conformes** | **int** | Nombre de champs conformes | [optional] [default to 0]
**est_facturx** | **bool** | True si le PDF contient du XML Factur-X | [optional] [default to False]
**profil_facturx** | **str** |  | [optional] 
**champs** | [**List[ChampVerifieSchema]**](ChampVerifieSchema.md) | Liste des champs vérifiés avec valeurs, statuts et coordonnées PDF | [optional] 
**notes_obligatoires** | [**List[NoteObligatoireSchema]**](NoteObligatoireSchema.md) | Notes obligatoires (PMT, PMD, AAB) avec localisation PDF | [optional] 
**dimensions_pages** | [**List[DimensionPageSchema]**](DimensionPageSchema.md) | Dimensions de chaque page du PDF (largeur, hauteur) | [optional] 
**avertissements** | **List[str]** | Avertissements non bloquants | [optional] 

## Example

```python
from factpulse.models.reponse_verification_succes import ReponseVerificationSucces

# TODO update the JSON string below
json = "{}"
# create an instance of ReponseVerificationSucces from a JSON string
reponse_verification_succes_instance = ReponseVerificationSucces.from_json(json)
# print the JSON string representation of the object
print(ReponseVerificationSucces.to_json())

# convert the object into a dict
reponse_verification_succes_dict = reponse_verification_succes_instance.to_dict()
# create an instance of ReponseVerificationSucces from a dict
reponse_verification_succes_from_dict = ReponseVerificationSucces.from_dict(reponse_verification_succes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


