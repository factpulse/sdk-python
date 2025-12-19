# factpulse.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthcheck_healthcheck_get**](HealthApi.md#healthcheck_healthcheck_get) | **GET** /healthcheck | Docker healthcheck endpoint
[**root_get**](HealthApi.md#root_get) | **GET** / | Check API status


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

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "http://localhost"
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

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "http://localhost"
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

