# ResultatValidationPDFAPI

Résultat complet de la validation d'un PDF Factur-X.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**est_conforme** | **bool** | True si le PDF est conforme à tous les critères (XML, PDF/A, XMP) | 
**xml_present** | **bool** | True si un XML Factur-X est embarqué dans le PDF | 
**xml_conforme** | **bool** | True si le XML Factur-X est conforme aux règles Schematron | 
**profil_detecte** | **str** |  | [optional] 
**erreurs_xml** | **List[str]** | Liste des erreurs de validation XML | [optional] 
**pdfa_conforme** | **bool** | True si le PDF est conforme PDF/A | 
**version_pdfa** | **str** |  | [optional] 
**methode_validation_pdfa** | **str** | Méthode utilisée pour la validation PDF/A (metadata ou verapdf) | [optional] [default to 'metadata']
**regles_validees** | **int** |  | [optional] 
**regles_echouees** | **int** |  | [optional] 
**erreurs_pdfa** | **List[str]** | Liste des erreurs de conformité PDF/A | [optional] 
**avertissements_pdfa** | **List[str]** | Liste des avertissements PDF/A | [optional] 
**xmp_present** | **bool** | True si des métadonnées XMP sont présentes | 
**xmp_conforme_facturx** | **bool** | True si les métadonnées XMP contiennent des informations Factur-X | 
**profil_xmp** | **str** |  | [optional] 
**version_xmp** | **str** |  | [optional] 
**erreurs_xmp** | **List[str]** | Liste des erreurs de métadonnées XMP | [optional] 
**metadonnees_xmp** | **Dict[str, object]** | Métadonnées XMP extraites du PDF | [optional] 
**est_signe** | **bool** | True si le PDF contient au moins une signature | 
**nombre_signatures** | **int** | Nombre de signatures électroniques trouvées | [optional] [default to 0]
**signatures** | [**List[InformationSignatureAPI]**](InformationSignatureAPI.md) | Liste des signatures trouvées avec leurs informations | [optional] 
**erreurs_signatures** | **List[str]** | Liste des erreurs lors de l&#39;analyse des signatures | [optional] 
**message_resume** | **str** | Message résumant le résultat de la validation | 

## Example

```python
from factpulse.models.resultat_validation_pdfapi import ResultatValidationPDFAPI

# TODO update the JSON string below
json = "{}"
# create an instance of ResultatValidationPDFAPI from a JSON string
resultat_validation_pdfapi_instance = ResultatValidationPDFAPI.from_json(json)
# print the JSON string representation of the object
print(ResultatValidationPDFAPI.to_json())

# convert the object into a dict
resultat_validation_pdfapi_dict = resultat_validation_pdfapi_instance.to_dict()
# create an instance of ResultatValidationPDFAPI from a dict
resultat_validation_pdfapi_from_dict = ResultatValidationPDFAPI.from_dict(resultat_validation_pdfapi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


