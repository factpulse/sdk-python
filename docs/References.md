# References

Contient les références diverses de la facture (devise, type, etc.).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devise_facture** | **str** |  | [optional] [default to 'EUR']
**mode_paiement** | [**ModePaiement**](ModePaiement.md) |  | 
**type_facture** | [**TypeFacture**](TypeFacture.md) |  | 
**type_tva** | [**TypeTVA**](TypeTVA.md) |  | 
**numero_marche** | **str** |  | [optional] 
**motif_exoneration_tva** | **str** |  | [optional] 
**numero_bon_commande** | **str** |  | [optional] 
**numero_facture_origine** | **str** |  | [optional] 

## Example

```python
from factpulse.models.references import References

# TODO update the JSON string below
json = "{}"
# create an instance of References from a JSON string
references_instance = References.from_json(json)
# print the JSON string representation of the object
print(References.to_json())

# convert the object into a dict
references_dict = references_instance.to_dict()
# create an instance of References from a dict
references_from_dict = References.from_dict(references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


