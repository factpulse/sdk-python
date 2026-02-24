# factpulse.ReferencesApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vatex_codes_api_v1_references_vatex_codes_get**](ReferencesApi.md#get_vatex_codes_api_v1_references_vatex_codes_get) | **GET** /api/v1/references/vatex-codes | VATEX exemption reason codes


# **get_vatex_codes_api_v1_references_vatex_codes_get**
> VATEXCodesResponse get_vatex_codes_api_v1_references_vatex_codes_get(category=category)

VATEX exemption reason codes

Returns the list of VATEX (VAT exemption reason) codes from the Peppol BIS Billing 3.0 code list. Source: https://docs.peppol.eu/poacc/billing/3.0/codelist/vatex/

### Example


```python
import factpulse
from factpulse.models.vatex_codes_response import VATEXCodesResponse
from factpulse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://factpulse.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "https://factpulse.fr"
)


# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ReferencesApi(api_client)
    category = 'category_example' # str | Filter by VAT category code (E, AE, K, G, O). (optional)

    try:
        # VATEX exemption reason codes
        api_response = api_instance.get_vatex_codes_api_v1_references_vatex_codes_get(category=category)
        print("The response of ReferencesApi->get_vatex_codes_api_v1_references_vatex_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->get_vatex_codes_api_v1_references_vatex_codes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter by VAT category code (E, AE, K, G, O). | [optional] 

### Return type

[**VATEXCodesResponse**](VATEXCodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of VATEX codes with their descriptions and associated VAT categories. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

