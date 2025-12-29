# ConvertResumeRequest

Requete de reprise de conversion avec corrections.  Le champ `overrides` accepte n'importe quel sous-ensemble de FacturXInvoice. Seuls les champs fournis seront mis a jour (merge profond).  Exemple:     {         \"overrides\": {             \"supplier\": {                 \"name\": \"Ma Société\",                 \"siret\": \"12345678901234\"             },             \"totals\": {                 \"total_net_amount\": 1000.00             }         }     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overrides** | **Dict[str, object]** | Sous-ensemble de FacturXInvoice a mettre a jour (merge profond) | [optional] 

## Example

```python
from factpulse.models.convert_resume_request import ConvertResumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertResumeRequest from a JSON string
convert_resume_request_instance = ConvertResumeRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertResumeRequest.to_json())

# convert the object into a dict
convert_resume_request_dict = convert_resume_request_instance.to_dict()
# create an instance of ConvertResumeRequest from a dict
convert_resume_request_from_dict = ConvertResumeRequest.from_dict(convert_resume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


