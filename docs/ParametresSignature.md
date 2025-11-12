# ParametresSignature

Paramètres optionnels pour signer le PDF généré.  **MODE 1 - Certificat stocké (recommandé) :** Ne fournissez que les métadonnées (raison, localisation, etc.). Le certificat sera récupéré automatiquement via client_uid du JWT. Signature PAdES-B-LT conforme eIDAS.  **MODE 2 - Clés dans le payload (tests/cas spéciaux) :** Fournissez key_pem + cert_pem directement dans le payload. Format PEM accepté : brut (\"-----BEGIN...\") ou base64.  **Règle de sélection :** - Si key_pem ET cert_pem fournis → Mode 2 (clés payload) - Sinon → Mode 1 (certificat stocké récupéré via client_uid)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_pem** | **str** |  | [optional] 
**cert_pem** | **str** |  | [optional] 
**key_passphrase** | **str** |  | [optional] 
**raison** | **str** |  | [optional] 
**localisation** | **str** |  | [optional] 
**contact** | **str** |  | [optional] 
**field_name** | **str** | Nom du champ de signature PDF | [optional] [default to 'FactPulseSignature']
**use_pades_lt** | **bool** | Activer PAdES-B-LT (archivage long terme). NÉCESSITE certificat avec accès OCSP/CRL | [optional] [default to False]
**use_timestamp** | **bool** | Activer l&#39;horodatage RFC 3161 avec FreeTSA (PAdES-B-T) | [optional] [default to True]

## Example

```python
from factpulse.models.parametres_signature import ParametresSignature

# TODO update the JSON string below
json = "{}"
# create an instance of ParametresSignature from a JSON string
parametres_signature_instance = ParametresSignature.from_json(json)
# print the JSON string representation of the object
print(ParametresSignature.to_json())

# convert the object into a dict
parametres_signature_dict = parametres_signature_instance.to_dict()
# create an instance of ParametresSignature from a dict
parametres_signature_from_dict = ParametresSignature.from_dict(parametres_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


