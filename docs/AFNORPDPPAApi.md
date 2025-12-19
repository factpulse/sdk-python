# factpulse.AFNORPDPPAApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_afnor_credentials_api_v1_afnor_credentials_get**](AFNORPDPPAApi.md#get_afnor_credentials_api_v1_afnor_credentials_get) | **GET** /api/v1/afnor/credentials | Retrieve stored AFNOR credentials
[**get_flux_entrant_api_v1_afnor_incoming_flows_flow_id_get**](AFNORPDPPAApi.md#get_flux_entrant_api_v1_afnor_incoming_flows_flow_id_get) | **GET** /api/v1/afnor/incoming-flows/{flow_id} | Retrieve and extract an incoming invoice
[**oauth_token_proxy_api_v1_afnor_oauth_token_post**](AFNORPDPPAApi.md#oauth_token_proxy_api_v1_afnor_oauth_token_post) | **POST** /api/v1/afnor/oauth/token | OAuth2 endpoint for AFNOR authentication


# **get_afnor_credentials_api_v1_afnor_credentials_get**
> object get_afnor_credentials_api_v1_afnor_credentials_get()

Retrieve stored AFNOR credentials

Retrieves stored AFNOR/PDP credentials for the JWT's client_uid. This endpoint is used by the SDK in 'stored' mode to retrieve credentials before performing AFNOR OAuth itself.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "http://localhost"
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
    api_instance = factpulse.AFNORPDPPAApi(api_client)

    try:
        # Retrieve stored AFNOR credentials
        api_response = api_instance.get_afnor_credentials_api_v1_afnor_credentials_get()
        print("The response of AFNORPDPPAApi->get_afnor_credentials_api_v1_afnor_credentials_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPAApi->get_afnor_credentials_api_v1_afnor_credentials_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | AFNOR credentials retrieved successfully |  -  |
**400** | No client_uid in JWT |  -  |
**401** | Not authenticated - Missing or invalid JWT token |  -  |
**404** | Client not found or no AFNOR credentials configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flux_entrant_api_v1_afnor_incoming_flows_flow_id_get**
> IncomingInvoice get_flux_entrant_api_v1_afnor_incoming_flows_flow_id_get(flow_id, include_document=include_document)

Retrieve and extract an incoming invoice

Downloads an incoming flow from the AFNOR PDP and extracts invoice metadata into a unified JSON format. Supports Factur-X, CII, and UBL formats.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.incoming_invoice import IncomingInvoice
from factpulse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "http://localhost"
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
    api_instance = factpulse.AFNORPDPPAApi(api_client)
    flow_id = 'flow_id_example' # str | 
    include_document = False # bool |  (optional) (default to False)

    try:
        # Retrieve and extract an incoming invoice
        api_response = api_instance.get_flux_entrant_api_v1_afnor_incoming_flows_flow_id_get(flow_id, include_document=include_document)
        print("The response of AFNORPDPPAApi->get_flux_entrant_api_v1_afnor_incoming_flows_flow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPAApi->get_flux_entrant_api_v1_afnor_incoming_flows_flow_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **include_document** | **bool**|  | [optional] [default to False]

### Return type

[**IncomingInvoice**](IncomingInvoice.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoice extracted successfully |  -  |
**400** | Unsupported or invalid invoice format |  -  |
**401** | Not authenticated |  -  |
**404** | Flow not found |  -  |
**503** | PDP service unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_token_proxy_api_v1_afnor_oauth_token_post**
> object oauth_token_proxy_api_v1_afnor_oauth_token_post()

OAuth2 endpoint for AFNOR authentication

OAuth2 proxy endpoint to obtain an AFNOR access token. Proxies to AFNOR mock (sandbox) or real PDP depending on MOCK_AFNOR_BASE_URL. This endpoint is public (no Django auth required) as it is called by the AFNOR SDK.

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
    api_instance = factpulse.AFNORPDPPAApi(api_client)

    try:
        # OAuth2 endpoint for AFNOR authentication
        api_response = api_instance.oauth_token_proxy_api_v1_afnor_oauth_token_post()
        print("The response of AFNORPDPPAApi->oauth_token_proxy_api_v1_afnor_oauth_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPAApi->oauth_token_proxy_api_v1_afnor_oauth_token_post: %s\n" % e)
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
**200** | OAuth2 token acquired successfully |  -  |
**401** | Invalid credentials |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

