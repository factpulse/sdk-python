# Beneficiaire

Informations sur le bénéficiaire du paiement (BG-10 / PayeeTradeParty).  Le bénéficiaire est la partie qui reçoit le paiement. Ce bloc est utilisé uniquement si le bénéficiaire est différent du vendeur (fournisseur).  **Cas d'usage principal** : Affacturage (factoring) Quand une facture est affacturée, le factor (société d'affacturage) devient le bénéficiaire du paiement à la place du fournisseur.  **Business Terms (EN16931)** : - BT-59 : Nom du bénéficiaire (obligatoire) - BT-60 : Identifiant du bénéficiaire (SIRET avec schemeID 0009) - BT-61 : Identifiant légal du bénéficiaire (SIREN avec schemeID 0002)  **Référence** : docs/guide_affacturage.md

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nom** | **str** | Nom du bénéficiaire (BT-59). Obligatoire. | 
**siret** | **str** |  | [optional] 
**siren** | **str** |  | [optional] 
**adresse_electronique** | [**AdresseElectronique**](AdresseElectronique.md) |  | [optional] 
**iban** | **str** |  | [optional] 
**bic** | **str** |  | [optional] 

## Example

```python
from factpulse.models.beneficiaire import Beneficiaire

# TODO update the JSON string below
json = "{}"
# create an instance of Beneficiaire from a JSON string
beneficiaire_instance = Beneficiaire.from_json(json)
# print the JSON string representation of the object
print(Beneficiaire.to_json())

# convert the object into a dict
beneficiaire_dict = beneficiaire_instance.to_dict()
# create an instance of Beneficiaire from a dict
beneficiaire_from_dict = Beneficiaire.from_dict(beneficiaire_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


