# factpulse.AFNORPDPPAApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_token_proxy_api_v1_afnor_oauth_token_post**](AFNORPDPPAApi.md#oauth_token_proxy_api_v1_afnor_oauth_token_post) | **POST** /api/v1/afnor/oauth/token | Endpoint OAuth2 pour authentification AFNOR


# **oauth_token_proxy_api_v1_afnor_oauth_token_post**
> object oauth_token_proxy_api_v1_afnor_oauth_token_post()

Endpoint OAuth2 pour authentification AFNOR

Endpoint proxy OAuth2 pour obtenir un token d'accès AFNOR. Fait proxy vers le mock AFNOR (sandbox) ou la vraie PDP selon MOCK_AFNOR_BASE_URL. Cet endpoint est public (pas d'auth Django requise) car il est appelé par le SDK AFNOR.

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
        # Endpoint OAuth2 pour authentification AFNOR
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
**200** | Token OAuth2 acquis avec succès |  -  |
**401** | Credentials invalides |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

