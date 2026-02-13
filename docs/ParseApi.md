# factpulse.ParseApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parse_facturx_async_api_v1_processing_parse_facturx_async_post**](ParseApi.md#parse_facturx_async_api_v1_processing_parse_facturx_async_post) | **POST** /api/v1/processing/parse-facturx/async | Parse Factur-X XML or PDF (async)
[**parse_facturx_sync_api_v1_processing_parse_facturx_post**](ParseApi.md#parse_facturx_sync_api_v1_processing_parse_facturx_post) | **POST** /api/v1/processing/parse-facturx | Parse CII, UBL or Factur-X PDF (sync)


# **parse_facturx_async_api_v1_processing_parse_facturx_async_post**
> TaskResponse parse_facturx_async_api_v1_processing_parse_facturx_async_post(file, callback_url=callback_url)

Parse Factur-X XML or PDF (async)

Parse a Factur-X file asynchronously using a Celery task.

**Use case:** For large files or when you want non-blocking processing.

**Workflow:**
1. Submit file with this endpoint -> receive `task_id`
2. Poll `/tasks/{task_id}/status` for result
3. Result contains `invoice` and `detected_profile`

**Optional:** Provide `callback_url` to receive a webhook when parsing completes.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.task_response import TaskResponse
from factpulse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://factpulse.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "https://factpulse.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ParseApi(api_client)
    file = None # bytearray | Factur-X PDF or XML file to parse
    callback_url = 'callback_url_example' # str |  (optional)

    try:
        # Parse Factur-X XML or PDF (async)
        api_response = api_instance.parse_facturx_async_api_v1_processing_parse_facturx_async_post(file, callback_url=callback_url)
        print("The response of ParseApi->parse_facturx_async_api_v1_processing_parse_facturx_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParseApi->parse_facturx_async_api_v1_processing_parse_facturx_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| Factur-X PDF or XML file to parse | 
 **callback_url** | **str**|  | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Task created |  -  |
**422** | Validation Error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_facturx_sync_api_v1_processing_parse_facturx_post**
> ParseFacturXResponse parse_facturx_sync_api_v1_processing_parse_facturx_post(file)

Parse CII, UBL or Factur-X PDF (sync)

Parse a CII XML, UBL XML, or Factur-X PDF and extract the invoice data as a FacturXInvoice model.

**Use cases:**
- Extract invoice data from received invoices (any format)
- Round-trip: parse an existing invoice, modify it, and regenerate in another format
- Convert between CII and UBL via the FacturXInvoice pivot model

**Supported formats:**
- Factur-X PDF (PDF/A-3 with embedded CII XML)
- CII XML (UN/CEFACT Cross-Industry Invoice)
- UBL 2.1 XML (OASIS Invoice or CreditNote)

**Returns:**
- `invoice`: Complete FacturXInvoice data (can be used with /generate-invoice)
- `detected_profile`: Factur-X profile (MINIMUM, BASIC, EN16931, EXTENDED)

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.parse_factur_x_response import ParseFacturXResponse
from factpulse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://factpulse.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "https://factpulse.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ParseApi(api_client)
    file = None # bytearray | Factur-X PDF or XML file to parse

    try:
        # Parse CII, UBL or Factur-X PDF (sync)
        api_response = api_instance.parse_facturx_sync_api_v1_processing_parse_facturx_post(file)
        print("The response of ParseApi->parse_facturx_sync_api_v1_processing_parse_facturx_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParseApi->parse_facturx_sync_api_v1_processing_parse_facturx_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| Factur-X PDF or XML file to parse | 

### Return type

[**ParseFacturXResponse**](ParseFacturXResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoice successfully parsed |  -  |
**400** | Invalid file format or parsing error |  -  |
**422** | Validation Error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

