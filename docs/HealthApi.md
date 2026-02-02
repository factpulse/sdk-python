# factpulse.HealthApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_info_api_v1_me_get**](HealthApi.md#get_user_info_api_v1_me_get) | **GET** /api/v1/me | Get current user information
[**healthcheck_healthcheck_get**](HealthApi.md#healthcheck_healthcheck_get) | **GET** /healthcheck | Docker healthcheck endpoint
[**root_get**](HealthApi.md#root_get) | **GET** / | Check API status


# **get_user_info_api_v1_me_get**
> object get_user_info_api_v1_me_get()

Get current user information

Returns information about the authenticated user.

This endpoint allows you to:
- Verify that authentication works
- Get connected account details
- Test JWT token validity
- Check your consumption quota

**Requires valid authentication.**

### Example

* Api Key Authentication (APIKeyHeader):
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
    api_instance = factpulse.HealthApi(api_client)

    try:
        # Get current user information
        api_response = api_instance.get_user_info_api_v1_me_get()
        print("The response of HealthApi->get_user_info_api_v1_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->get_user_info_api_v1_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User information |  -  |
**401** | Missing or invalid JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **healthcheck_healthcheck_get**
> object healthcheck_healthcheck_get()

Docker healthcheck endpoint

Healthcheck endpoint for Docker and load balancers.

Useful for:
- Docker healthcheck
- Kubernetes liveness/readiness probes
- Load balancers (Nginx, HAProxy)
- Availability monitoring
- Zero downtime deployment

Returns a 200 code if the API is operational.

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
    api_instance = factpulse.HealthApi(api_client)

    try:
        # Docker healthcheck endpoint
        api_response = api_instance.healthcheck_healthcheck_get()
        print("The response of HealthApi->healthcheck_healthcheck_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->healthcheck_healthcheck_get: %s\n" % e)
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
**200** | API is healthy |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> object root_get()

Check API status

Health check endpoint to verify the API is responding.

Useful for:
- Availability monitoring
- Integration tests
- Load balancers

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
    api_instance = factpulse.HealthApi(api_client)

    try:
        # Check API status
        api_response = api_instance.root_get()
        print("The response of HealthApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->root_get: %s\n" % e)
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
**200** | API is operational |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

