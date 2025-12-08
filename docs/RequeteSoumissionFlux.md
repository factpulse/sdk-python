# RequeteSoumissionFlux

Requête pour soumettre une facture à une PDP/PA via AFNOR

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nom_flux** | **str** | Nom du flux (ex: &#39;Facture 2025-001&#39;) | 
**syntaxe_flux** | [**SyntaxeFlux**](SyntaxeFlux.md) | Syntaxe du flux (CII pour Factur-X) | [optional] 
**profil_flux** | [**ProfilFlux**](ProfilFlux.md) |  | [optional] 
**tracking_id** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**pdp_credentials** | [**PDPCredentials**](PDPCredentials.md) |  | [optional] 

## Example

```python
from factpulse.models.requete_soumission_flux import RequeteSoumissionFlux

# TODO update the JSON string below
json = "{}"
# create an instance of RequeteSoumissionFlux from a JSON string
requete_soumission_flux_instance = RequeteSoumissionFlux.from_json(json)
# print the JSON string representation of the object
print(RequeteSoumissionFlux.to_json())

# convert the object into a dict
requete_soumission_flux_dict = requete_soumission_flux_instance.to_dict()
# create an instance of RequeteSoumissionFlux from a dict
requete_soumission_flux_from_dict = RequeteSoumissionFlux.from_dict(requete_soumission_flux_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


