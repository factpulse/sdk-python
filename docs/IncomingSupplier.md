# IncomingSupplier

Supplier extracted from an incoming invoice.  Unlike the Supplier model in models.py, this model does not have a supplier_id field as this information is not available in Factur-X/CII/UBL XML files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Supplier business name (BT-27) | 
**siren** | **str** |  | [optional] 
**siret** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**postal_address** | [**PostalAddress**](PostalAddress.md) |  | [optional] 
**electronic_address** | [**ElectronicAddress**](ElectronicAddress.md) |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from factpulse.models.incoming_supplier import IncomingSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingSupplier from a JSON string
incoming_supplier_instance = IncomingSupplier.from_json(json)
# print the JSON string representation of the object
print(IncomingSupplier.to_json())

# convert the object into a dict
incoming_supplier_dict = incoming_supplier_instance.to_dict()
# create an instance of IncomingSupplier from a dict
incoming_supplier_from_dict = IncomingSupplier.from_dict(incoming_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


