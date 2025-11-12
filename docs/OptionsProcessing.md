# OptionsProcessing

Options de traitement pour la génération et la soumission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profil_facturx** | **str** | Profil Factur-X à utiliser | [optional] [default to 'EN16931']
**auto_enrichir** | **bool** | Auto-enrichir les données (APIs Entreprises, Chorus Pro, etc.) | [optional] [default to True]
**valider** | **bool** | Valider le XML Factur-X avec Schematron | [optional] [default to True]
**verifier_parametres_destination** | **bool** | Vérifier les paramètres requis par la destination (ex: code_service pour Chorus) | [optional] [default to True]

## Example

```python
from factpulse.models.options_processing import OptionsProcessing

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsProcessing from a JSON string
options_processing_instance = OptionsProcessing.from_json(json)
# print the JSON string representation of the object
print(OptionsProcessing.to_json())

# convert the object into a dict
options_processing_dict = options_processing_instance.to_dict()
# create an instance of OptionsProcessing from a dict
options_processing_from_dict = OptionsProcessing.from_dict(options_processing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


