# factpulse.AFNORPDPPAFlowServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get**](AFNORPDPPAFlowServiceApi.md#download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get) | **GET** /api/v1/afnor/flow/v1/flows/{flowId} | Download a flow
[**flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get**](AFNORPDPPAFlowServiceApi.md#flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get) | **GET** /api/v1/afnor/flow/v1/healthcheck | Healthcheck Flow Service
[**search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post**](AFNORPDPPAFlowServiceApi.md#search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post) | **POST** /api/v1/afnor/flow/v1/flows/search | Search flows
[**submit_flow_proxy_api_v1_afnor_flow_v1_flows_post**](AFNORPDPPAFlowServiceApi.md#submit_flow_proxy_api_v1_afnor_flow_v1_flows_post) | **POST** /api/v1/afnor/flow/v1/flows | Submit an invoicing flow


# **download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get**
> object download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get(flow_id)

Download a flow

Download the PDF/A-3 file of an invoicing flow (uses JWT client_uid)

### Example


```python
import factpulse
from factpulse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.AFNORPDPPAFlowServiceApi(api_client)
    flow_id = 'flow_id_example' # str | 

    try:
        # Download a flow
        api_response = api_instance.download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get(flow_id)
        print("The response of AFNORPDPPAFlowServiceApi->download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPAFlowServiceApi->download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF/A-3 file |  -  |
**400** | Missing PDP configuration |  -  |
**401** | Not authenticated - Missing or invalid JWT token |  -  |
**404** | Flow not found or invalid client_uid |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get**
> object flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get()

Healthcheck Flow Service

Check Flow Service availability

### Example


```python
import factpulse
from factpulse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "http://localhost"
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
**200** | Service operational |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post**
> object search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post()

Search flows

Search invoicing flows by criteria (uses JWT client_uid)

### Example


```python
import factpulse
from factpulse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.AFNORPDPPAFlowServiceApi(api_client)

    try:
        # Search flows
        api_response = api_instance.search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post()
        print("The response of AFNORPDPPAFlowServiceApi->search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPAFlowServiceApi->search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post: %s\n" % e)
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
**200** | Search results |  -  |
**400** | Missing PDP configuration |  -  |
**401** | Not authenticated - Missing or invalid JWT token |  -  |
**404** | PDP client not found (invalid client_uid) |  -  |
**429** | Too many requests - Rate limit reached (60 searches/minute) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_flow_proxy_api_v1_afnor_flow_v1_flows_post**
> object submit_flow_proxy_api_v1_afnor_flow_v1_flows_post()

Submit an invoicing flow

Submits an electronic invoice to a Partner Dematerialization Platform (PDP) in compliance with the AFNOR XP Z12-013 standard

### Example


```python
import factpulse
from factpulse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.AFNORPDPPAFlowServiceApi(api_client)

    try:
        # Submit an invoicing flow
        api_response = api_instance.submit_flow_proxy_api_v1_afnor_flow_v1_flows_post()
        print("The response of AFNORPDPPAFlowServiceApi->submit_flow_proxy_api_v1_afnor_flow_v1_flows_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPAFlowServiceApi->submit_flow_proxy_api_v1_afnor_flow_v1_flows_post: %s\n" % e)
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
**200** | Successful Response |  -  |
**201** | Flow submitted successfully |  -  |
**400** | Invalid request or missing PDP configuration |  -  |
**401** | Not authenticated - Missing or invalid JWT token |  -  |
**403** | Not authorized - Quota exceeded or insufficient permissions |  -  |
**404** | PDP client not found (invalid client_uid) |  -  |
**429** | Too many requests - Rate limit reached (30 submissions/minute) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

