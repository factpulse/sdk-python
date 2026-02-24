# InvoiceLifecycle

Cycle de vie d'une facture specifique.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seller_id** | **str** |  | [optional] 
**invoice_id** | **str** | Reference de la facture (IssuerAssignedID du CDAR) | 
**events** | [**List[LifecycleEvent]**](LifecycleEvent.md) | Evenements de cycle de vie tries chronologiquement | [optional] 
**total_events** | **int** | Nombre total d&#39;evenements | 

## Example

```python
from factpulse.models.invoice_lifecycle import InvoiceLifecycle

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLifecycle from a JSON string
invoice_lifecycle_instance = InvoiceLifecycle.from_json(json)
# print the JSON string representation of the object
print(InvoiceLifecycle.to_json())

# convert the object into a dict
invoice_lifecycle_dict = invoice_lifecycle_instance.to_dict()
# create an instance of InvoiceLifecycle from a dict
invoice_lifecycle_from_dict = InvoiceLifecycle.from_dict(invoice_lifecycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


