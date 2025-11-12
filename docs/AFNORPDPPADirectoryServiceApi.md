# factpulse.AFNORPDPPADirectoryServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get**](AFNORPDPPADirectoryServiceApi.md#directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get) | **GET** /api/v1/afnor/directory/v1/healthcheck | Healthcheck Directory Service
[**get_company_proxy_api_v1_afnor_directory_v1_companies_siren_get**](AFNORPDPPADirectoryServiceApi.md#get_company_proxy_api_v1_afnor_directory_v1_companies_siren_get) | **GET** /api/v1/afnor/directory/v1/companies/{siren} | Récupérer une entreprise
[**search_companies_proxy_api_v1_afnor_directory_v1_companies_search_post**](AFNORPDPPADirectoryServiceApi.md#search_companies_proxy_api_v1_afnor_directory_v1_companies_search_post) | **POST** /api/v1/afnor/directory/v1/companies/search | Rechercher des entreprises


# **directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get**
> object directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get()

Healthcheck Directory Service

Vérifier la disponibilité du Directory Service

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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)

    try:
        # Healthcheck Directory Service
        api_response = api_instance.directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get()
        print("The response of AFNORPDPPADirectoryServiceApi->directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get: %s\n" % e)
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
**200** | Service opérationnel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_proxy_api_v1_afnor_directory_v1_companies_siren_get**
> object get_company_proxy_api_v1_afnor_directory_v1_companies_siren_get(siren)

Récupérer une entreprise

Récupérer les informations d'une entreprise par son SIREN

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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    siren = 'siren_example' # str | 

    try:
        # Récupérer une entreprise
        api_response = api_instance.get_company_proxy_api_v1_afnor_directory_v1_companies_siren_get(siren)
        print("The response of AFNORPDPPADirectoryServiceApi->get_company_proxy_api_v1_afnor_directory_v1_companies_siren_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->get_company_proxy_api_v1_afnor_directory_v1_companies_siren_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siren** | **str**|  | 

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
**200** | Informations de l&#39;entreprise |  -  |
**404** | Entreprise non trouvée |  -  |
**401** | Non authentifié |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_companies_proxy_api_v1_afnor_directory_v1_companies_search_post**
> object search_companies_proxy_api_v1_afnor_directory_v1_companies_search_post()

Rechercher des entreprises

Rechercher des entreprises dans l'annuaire AFNOR

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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)

    try:
        # Rechercher des entreprises
        api_response = api_instance.search_companies_proxy_api_v1_afnor_directory_v1_companies_search_post()
        print("The response of AFNORPDPPADirectoryServiceApi->search_companies_proxy_api_v1_afnor_directory_v1_companies_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->search_companies_proxy_api_v1_afnor_directory_v1_companies_search_post: %s\n" % e)
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
**200** | Résultats de recherche |  -  |
**401** | Non authentifié |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

