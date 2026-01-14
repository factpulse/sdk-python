# factpulse.AFNORPDPPAFlowServiceApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get**](AFNORPDPPAFlowServiceApi.md#download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get) | **GET** /api/v1/afnor/flow/v1/flows/{flowId} | Download a flow
[**flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get**](AFNORPDPPAFlowServiceApi.md#flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get) | **GET** /api/v1/afnor/flow/v1/healthcheck | Healthcheck Flow Service
[**search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post**](AFNORPDPPAFlowServiceApi.md#search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post) | **POST** /api/v1/afnor/flow/v1/flows/search | Search flows
[**submit_flow_proxy_api_v1_afnor_flow_v1_flows_post**](AFNORPDPPAFlowServiceApi.md#submit_flow_proxy_api_v1_afnor_flow_v1_flows_post) | **POST** /api/v1/afnor/flow/v1/flows | Submit an invoicing flow


# **download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get**
> AFNORFlow download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get(flow_id, doc_type=doc_type)

Download a flow

Download a file related to a given flow (AFNOR XP Z12-013 compliant):
- Metadata [Default]: provides the flow metadata as JSON
- Original: the document initially sent by the emitter
- Converted: the document optionally converted by the system
- ReadableView: the document optionally generated as readable file

### Example


```python
import factpulse
from factpulse.models.afnor_flow import AFNORFlow
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
    api_instance = factpulse.AFNORPDPPAFlowServiceApi(api_client)
    flow_id = 'flow_id_example' # str | AFNOR flow identifier (UUID)
    doc_type = factpulse.DocType() # DocType | Type of file to download: Metadata (default, JSON), Original, Converted, or ReadableView (optional)

    try:
        # Download a flow
        api_response = api_instance.download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get(flow_id, doc_type=doc_type)
        print("The response of AFNORPDPPAFlowServiceApi->download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPAFlowServiceApi->download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**| AFNOR flow identifier (UUID) | 
 **doc_type** | [**DocType**](.md)| Type of file to download: Metadata (default, JSON), Original, Converted, or ReadableView | [optional] 

### Return type

[**AFNORFlow**](AFNORFlow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Flow file or metadata returned |  -  |
**400** | Bad request - Invalid input parameters |  -  |
**401** | Authentication error - Missing or invalid token |  -  |
**403** | Forbidden - Insufficient permissions |  -  |
**404** | Resource not found |  -  |
**429** | Too many requests - Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable - PDP temporarily unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get**
> object flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get()

Healthcheck Flow Service

Check Flow Service availability (AFNOR XP Z12-013 compliant)

### Example


```python
import factpulse
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
    api_instance = factpulse.AFNORPDPPAFlowServiceApi(api_client)

    try:
        # Healthcheck Flow Service
        api_response = api_instance.flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get()
        print("The response of AFNORPDPPAFlowServiceApi->flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPAFlowServiceApi->flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Service is operational |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable - PDP temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post**
> AFNORSearchFlowContent search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post(afnor_search_flow_params)

Search flows

Search invoicing flows by criteria (AFNOR XP Z12-013 compliant)

### Example


```python
import factpulse
from factpulse.models.afnor_search_flow_content import AFNORSearchFlowContent
from factpulse.models.afnor_search_flow_params import AFNORSearchFlowParams
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
    api_instance = factpulse.AFNORPDPPAFlowServiceApi(api_client)
    afnor_search_flow_params = factpulse.AFNORSearchFlowParams() # AFNORSearchFlowParams | 

    try:
        # Search flows
        api_response = api_instance.search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post(afnor_search_flow_params)
        print("The response of AFNORPDPPAFlowServiceApi->search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPAFlowServiceApi->search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **afnor_search_flow_params** | [**AFNORSearchFlowParams**](AFNORSearchFlowParams.md)|  | 

### Return type

[**AFNORSearchFlowContent**](AFNORSearchFlowContent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Search results returned |  -  |
**400** | Bad request - Invalid input parameters |  -  |
**401** | Authentication error - Missing or invalid token |  -  |
**403** | Forbidden - Insufficient permissions |  -  |
**429** | Too many requests - Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable - PDP temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_flow_proxy_api_v1_afnor_flow_v1_flows_post**
> object submit_flow_proxy_api_v1_afnor_flow_v1_flows_post(flow_info, file)

Submit an invoicing flow

Submits an electronic invoice to a Partner Dematerialization Platform (PDP) in compliance with the AFNOR XP Z12-013 standard

### Example


```python
import factpulse
from factpulse.models.afnor_flow_info import AFNORFlowInfo
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
    api_instance = factpulse.AFNORPDPPAFlowServiceApi(api_client)
    flow_info = factpulse.AFNORFlowInfo() # AFNORFlowInfo | 
    file = None # bytearray | Flow file (PDF/A-3 with embedded XML or XML)

    try:
        # Submit an invoicing flow
        api_response = api_instance.submit_flow_proxy_api_v1_afnor_flow_v1_flows_post(flow_info, file)
        print("The response of AFNORPDPPAFlowServiceApi->submit_flow_proxy_api_v1_afnor_flow_v1_flows_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPAFlowServiceApi->submit_flow_proxy_api_v1_afnor_flow_v1_flows_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_info** | [**AFNORFlowInfo**](AFNORFlowInfo.md)|  | 
 **file** | **bytearray**| Flow file (PDF/A-3 with embedded XML or XML) | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**202** | OK - Flow has been uploaded and accepted for processing |  -  |
**400** | Bad request - Invalid input parameters |  -  |
**401** | Authentication error - Missing or invalid token |  -  |
**403** | Forbidden - Insufficient permissions |  -  |
**404** | Resource not found |  -  |
**413** | Payload too large - File exceeds maximum size |  -  |
**422** | Unprocessable entity - Business rule validation failed |  -  |
**429** | Too many requests - Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable - PDP temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

