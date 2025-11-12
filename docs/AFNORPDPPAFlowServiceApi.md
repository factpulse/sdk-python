# factpulse.AFNORPDPPAFlowServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get**](AFNORPDPPAFlowServiceApi.md#download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get) | **GET** /api/v1/afnor/flow/v1/flows/{flowId} | Télécharger un flux
[**flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get**](AFNORPDPPAFlowServiceApi.md#flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get) | **GET** /api/v1/afnor/flow/v1/healthcheck | Healthcheck Flow Service
[**search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post**](AFNORPDPPAFlowServiceApi.md#search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post) | **POST** /api/v1/afnor/flow/v1/flows/search | Rechercher des flux
[**submit_flow_proxy_api_v1_afnor_flow_v1_flows_post**](AFNORPDPPAFlowServiceApi.md#submit_flow_proxy_api_v1_afnor_flow_v1_flows_post) | **POST** /api/v1/afnor/flow/v1/flows | Soumettre un flux de facturation


# **download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get**
> object download_flow_proxy_api_v1_afnor_flow_v1_flows_flow_id_get(flow_id)

Télécharger un flux

Télécharger le fichier PDF/A-3 d'un flux de facturation (utilise le client_uid du JWT)

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
        # Télécharger un flux
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
**200** | Fichier PDF/A-3 |  -  |
**400** | Configuration PDP manquante |  -  |
**401** | Non authentifié - Token JWT manquant ou invalide |  -  |
**404** | Flux non trouvé ou client_uid invalide |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get**
> object flow_healthcheck_proxy_api_v1_afnor_flow_v1_healthcheck_get()

Healthcheck Flow Service

Vérifier la disponibilité du Flow Service

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
**200** | Service opérationnel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post**
> object search_flows_proxy_api_v1_afnor_flow_v1_flows_search_post()

Rechercher des flux

Rechercher des flux de facturation selon des critères (utilise le client_uid du JWT)

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
        # Rechercher des flux
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
**200** | Résultats de recherche |  -  |
**400** | Configuration PDP manquante |  -  |
**401** | Non authentifié - Token JWT manquant ou invalide |  -  |
**404** | Client PDP non trouvé (client_uid invalide) |  -  |
**429** | Trop de requêtes - Rate limit atteint (60 recherches/minute) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_flow_proxy_api_v1_afnor_flow_v1_flows_post**
> object submit_flow_proxy_api_v1_afnor_flow_v1_flows_post()

Soumettre un flux de facturation

Soumet une facture électronique à une Plateforme de Dématérialisation Partenaire (PDP) conformément à la norme AFNOR XP Z12-013

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
        # Soumettre un flux de facturation
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
**201** | Flux soumis avec succès |  -  |
**400** | Requête invalide ou configuration PDP manquante |  -  |
**401** | Non authentifié - Token JWT manquant ou invalide |  -  |
**403** | Non autorisé - Quota dépassé ou permissions insuffisantes |  -  |
**404** | Client PDP non trouvé (client_uid invalide) |  -  |
**429** | Trop de requêtes - Rate limit atteint (30 soumissions/minute) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

