# factpulse.SantApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthcheck_healthcheck_get**](SantApi.md#healthcheck_healthcheck_get) | **GET** /healthcheck | Endpoint de healthcheck pour Docker
[**racine_get**](SantApi.md#racine_get) | **GET** / | Vérifier l&#39;état de l&#39;API


# **healthcheck_healthcheck_get**
> object healthcheck_healthcheck_get()

Endpoint de healthcheck pour Docker

Endpoint de healthcheck pour Docker et les load balancers.

Utile pour :
- Docker healthcheck
- Kubernetes liveness/readiness probes
- Load balancers (Nginx, HAProxy)
- Monitoring de disponibilité
- Déploiement zero downtime

Retourne un code 200 si l'API est opérationnelle.

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
    api_instance = factpulse.SantApi(api_client)

    try:
        # Endpoint de healthcheck pour Docker
        api_response = api_instance.healthcheck_healthcheck_get()
        print("The response of SantApi->healthcheck_healthcheck_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SantApi->healthcheck_healthcheck_get: %s\n" % e)
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
**200** | L&#39;API est en bonne santé |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **racine_get**
> object racine_get()

Vérifier l'état de l'API

Endpoint de health check pour vérifier que l'API répond.

Utile pour :
- Monitoring de disponibilité
- Tests d'intégration
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
    api_instance = factpulse.SantApi(api_client)

    try:
        # Vérifier l'état de l'API
        api_response = api_instance.racine_get()
        print("The response of SantApi->racine_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SantApi->racine_get: %s\n" % e)
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
**200** | L&#39;API est opérationnelle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

