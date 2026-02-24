# LifecycleResponse

Reponse des cycles de vie, groupes par facture.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoices** | [**List[InvoiceLifecycle]**](InvoiceLifecycle.md) | Cycles de vie par facture | [optional] 
**total_invoices** | **int** | Nombre de factures | 
**cutoff_days** | **int** | Nombre de jours de la fenetre de recherche | 

## Example

```python
from factpulse.models.lifecycle_response import LifecycleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleResponse from a JSON string
lifecycle_response_instance = LifecycleResponse.from_json(json)
# print the JSON string representation of the object
print(LifecycleResponse.to_json())

# convert the object into a dict
lifecycle_response_dict = lifecycle_response_instance.to_dict()
# create an instance of LifecycleResponse from a dict
lifecycle_response_from_dict = LifecycleResponse.from_dict(lifecycle_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


