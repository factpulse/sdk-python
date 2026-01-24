# factpulse.AFNORPDPPAApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_flux_entrant_api_v1_afnor_incoming_flows_flow_id_get**](AFNORPDPPAApi.md#get_flux_entrant_api_v1_afnor_incoming_flows_flow_id_get) | **GET** /api/v1/afnor/incoming-flows/{flow_id} | Retrieve and extract an incoming invoice
[**oauth_token_proxy_api_v1_afnor_oauth_token_post**](AFNORPDPPAApi.md#oauth_token_proxy_api_v1_afnor_oauth_token_post) | **POST** /api/v1/afnor/oauth/token | Test PDP OAuth2 credentials


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
    api_instance = factpulse.AFNORPDPPAApi(api_client)
    flow_id = 'flow_id_example' # str | AFNOR flow ID (UUID format)
    include_document = False # bool | Include base64-encoded document in response (optional) (default to False)

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
 **flow_id** | **str**| AFNOR flow ID (UUID format) | 
 **include_document** | **bool**| Include base64-encoded document in response | [optional] [default to False]

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

Test PDP OAuth2 credentials

OAuth2 proxy to validate PDP credentials. Use this endpoint to verify that OAuth credentials (client_id, client_secret) are valid before saving a PDP configuration. This endpoint is public (no authentication required).

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
    api_instance = factpulse.AFNORPDPPAApi(api_client)

    try:
        # Test PDP OAuth2 credentials
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
**200** | OAuth2 token acquired successfully - credentials are valid |  -  |
**401** | Invalid credentials - client_id or client_secret is wrong |  -  |
**503** | PDP OAuth server unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

