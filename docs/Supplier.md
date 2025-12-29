# Supplier

Information about the supplier / seller (BG-4).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**electronic_address** | [**ElectronicAddress**](ElectronicAddress.md) |  | 
**supplier_id** | **int** |  | 
**private_id** | **str** |  | [optional] 
**supplier_bank_account_code** | **int** |  | [optional] 
**supplier_service_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**trading_business_name** | **str** |  | [optional] 
**legal_description** | **str** |  | [optional] 
**siren** | **str** |  | [optional] 
**siret** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**iban** | **str** |  | [optional] 
**bic** | **str** |  | [optional] 
**bank_account_name** | **str** |  | [optional] 
**proprietary_id** | **str** |  | [optional] 
**postal_address** | [**PostalAddress**](PostalAddress.md) |  | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**global_ids** | [**List[ElectronicAddress]**](ElectronicAddress.md) |  | [optional] 

## Example

```python
from factpulse.models.supplier import Supplier

# TODO update the JSON string below
json = "{}"
# create an instance of Supplier from a JSON string
supplier_instance = Supplier.from_json(json)
# print the JSON string representation of the object
print(Supplier.to_json())

# convert the object into a dict
supplier_dict = supplier_instance.to_dict()
# create an instance of Supplier from a dict
supplier_from_dict = Supplier.from_dict(supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


