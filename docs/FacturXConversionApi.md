# factpulse.FacturXConversionApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_document_async_api_v1_convert_async_post**](FacturXConversionApi.md#convert_document_async_api_v1_convert_async_post) | **POST** /api/v1/convert/async | Convert a document to Factur-X (async mode)
[**download_file_api_v1_convert_conversion_id_download_filename_get**](FacturXConversionApi.md#download_file_api_v1_convert_conversion_id_download_filename_get) | **GET** /api/v1/convert/{conversion_id}/download/{filename} | Download a generated file
[**get_conversion_status_api_v1_convert_conversion_id_status_get**](FacturXConversionApi.md#get_conversion_status_api_v1_convert_conversion_id_status_get) | **GET** /api/v1/convert/{conversion_id}/status | Check conversion status
[**resume_conversion_api_v1_convert_conversion_id_resume_post**](FacturXConversionApi.md#resume_conversion_api_v1_convert_conversion_id_resume_post) | **POST** /api/v1/convert/{conversion_id}/resume | Resume a conversion with corrections


# **convert_document_async_api_v1_convert_async_post**
> object convert_document_async_api_v1_convert_async_post(file, output=output, callback_url=callback_url, webhook_mode=webhook_mode)

Convert a document to Factur-X (async mode)

Launch an asynchronous conversion via Celery.

## Workflow

1. **Upload**: Document is sent as multipart/form-data
2. **Celery Task**: Task is queued for processing
3. **Callback**: Webhook notification on completion

## Possible responses

- **202**: Task accepted, processing
- **400**: Invalid file

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
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

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.FacturXConversionApi(api_client)
    file = None # bytearray | Document to convert (PDF, DOCX, XLSX, JPG, PNG)
    output = 'pdf' # str | Output format: pdf, xml, both (optional) (default to 'pdf')
    callback_url = 'callback_url_example' # str |  (optional)
    webhook_mode = 'inline' # str | Content delivery mode: 'inline' (base64 in webhook) or 'download_url' (temporary URL, 1h TTL) (optional) (default to 'inline')

    try:
        # Convert a document to Factur-X (async mode)
        api_response = api_instance.convert_document_async_api_v1_convert_async_post(file, output=output, callback_url=callback_url, webhook_mode=webhook_mode)
        print("The response of FacturXConversionApi->convert_document_async_api_v1_convert_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacturXConversionApi->convert_document_async_api_v1_convert_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| Document to convert (PDF, DOCX, XLSX, JPG, PNG) | 
 **output** | **str**| Output format: pdf, xml, both | [optional] [default to &#39;pdf&#39;]
 **callback_url** | **str**|  | [optional] 
 **webhook_mode** | **str**| Content delivery mode: &#39;inline&#39; (base64 in webhook) or &#39;download_url&#39; (temporary URL, 1h TTL) | [optional] [default to &#39;inline&#39;]

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**202** | Task accepted |  -  |
**400** | Invalid file |  -  |
**422** | Validation Error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_api_v1_convert_conversion_id_download_filename_get**
> object download_file_api_v1_convert_conversion_id_download_filename_get(conversion_id, filename)

Download a generated file

Download the generated Factur-X PDF or XML file.

## Available files

- `facturx.pdf`: PDF/A-3 with embedded XML
- `facturx.xml`: XML CII only (Cross Industry Invoice)

Files are available for 24 hours after generation.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
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

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.FacturXConversionApi(api_client)
    conversion_id = 'conversion_id_example' # str | Conversion ID returned by POST /convert (UUID format)
    filename = 'filename_example' # str | File to download: 'facturx.pdf' or 'facturx.xml'

    try:
        # Download a generated file
        api_response = api_instance.download_file_api_v1_convert_conversion_id_download_filename_get(conversion_id, filename)
        print("The response of FacturXConversionApi->download_file_api_v1_convert_conversion_id_download_filename_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacturXConversionApi->download_file_api_v1_convert_conversion_id_download_filename_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversion_id** | **str**| Conversion ID returned by POST /convert (UUID format) | 
 **filename** | **str**| File to download: &#39;facturx.pdf&#39; or &#39;facturx.xml&#39; | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File downloaded |  -  |
**404** | File not found or expired |  -  |
**422** | Validation Error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversion_status_api_v1_convert_conversion_id_status_get**
> Dict[str, object] get_conversion_status_api_v1_convert_conversion_id_status_get(conversion_id)

Check conversion status

Returns the current status of an asynchronous conversion.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
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

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.FacturXConversionApi(api_client)
    conversion_id = 'conversion_id_example' # str | Conversion ID returned by POST /convert (UUID format)

    try:
        # Check conversion status
        api_response = api_instance.get_conversion_status_api_v1_convert_conversion_id_status_get(conversion_id)
        print("The response of FacturXConversionApi->get_conversion_status_api_v1_convert_conversion_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacturXConversionApi->get_conversion_status_api_v1_convert_conversion_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversion_id** | **str**| Conversion ID returned by POST /convert (UUID format) | 

### Return type

**Dict[str, object]**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_conversion_api_v1_convert_conversion_id_resume_post**
> ConvertSuccessResponse resume_conversion_api_v1_convert_conversion_id_resume_post(conversion_id, convert_resume_request)

Resume a conversion with corrections

Resume a conversion after completing missing data or correcting errors.

The OCR extraction is preserved, data is updated with corrections,
then a new Schematron validation is performed.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.convert_resume_request import ConvertResumeRequest
from factpulse.models.convert_success_response import ConvertSuccessResponse
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

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.FacturXConversionApi(api_client)
    conversion_id = 'conversion_id_example' # str | Conversion ID returned by POST /convert (UUID format)
    convert_resume_request = factpulse.ConvertResumeRequest() # ConvertResumeRequest | 

    try:
        # Resume a conversion with corrections
        api_response = api_instance.resume_conversion_api_v1_convert_conversion_id_resume_post(conversion_id, convert_resume_request)
        print("The response of FacturXConversionApi->resume_conversion_api_v1_convert_conversion_id_resume_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacturXConversionApi->resume_conversion_api_v1_convert_conversion_id_resume_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversion_id** | **str**| Conversion ID returned by POST /convert (UUID format) | 
 **convert_resume_request** | [**ConvertResumeRequest**](ConvertResumeRequest.md)|  | 

### Return type

[**ConvertSuccessResponse**](ConvertSuccessResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Conversion not found or expired |  -  |
**422** | Validation still failing |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

