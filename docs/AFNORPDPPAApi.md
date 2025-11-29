# factpulse.AFNORPDPPAApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_afnor_credentials_api_v1_afnor_credentials_get**](AFNORPDPPAApi.md#get_afnor_credentials_api_v1_afnor_credentials_get) | **GET** /api/v1/afnor/credentials | Récupérer les credentials AFNOR stockés
[**get_flux_entrant_api_v1_afnor_flux_entrants_flow_id_get**](AFNORPDPPAApi.md#get_flux_entrant_api_v1_afnor_flux_entrants_flow_id_get) | **GET** /api/v1/afnor/flux-entrants/{flow_id} | Récupérer et extraire une facture entrante
[**oauth_token_proxy_api_v1_afnor_oauth_token_post**](AFNORPDPPAApi.md#oauth_token_proxy_api_v1_afnor_oauth_token_post) | **POST** /api/v1/afnor/oauth/token | Endpoint OAuth2 pour authentification AFNOR


# **get_afnor_credentials_api_v1_afnor_credentials_get**
> object get_afnor_credentials_api_v1_afnor_credentials_get()

Récupérer les credentials AFNOR stockés

Récupère les credentials AFNOR/PDP stockés pour le client_uid du JWT. Cet endpoint est utilisé par le SDK en mode 'stored' pour récupérer les credentials avant de faire l'OAuth AFNOR lui-même.

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
        # Récupérer les credentials AFNOR stockés
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
**200** | Credentials AFNOR récupérés avec succès |  -  |
**400** | Aucun client_uid dans le JWT |  -  |
**401** | Non authentifié - Token JWT manquant ou invalide |  -  |
**404** | Client non trouvé ou pas de credentials AFNOR configurés |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flux_entrant_api_v1_afnor_flux_entrants_flow_id_get**
> FactureEntrante get_flux_entrant_api_v1_afnor_flux_entrants_flow_id_get(flow_id, include_document=include_document)

Récupérer et extraire une facture entrante

Télécharge un flux entrant depuis la PDP AFNOR et extrait les métadonnées de la facture vers un format JSON unifié. Supporte les formats Factur-X, CII et UBL.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.facture_entrante import FactureEntrante
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
        # Récupérer et extraire une facture entrante
        api_response = api_instance.get_flux_entrant_api_v1_afnor_flux_entrants_flow_id_get(flow_id, include_document=include_document)
        print("The response of AFNORPDPPAApi->get_flux_entrant_api_v1_afnor_flux_entrants_flow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPAApi->get_flux_entrant_api_v1_afnor_flux_entrants_flow_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **include_document** | **bool**|  | [optional] [default to False]

### Return type

[**FactureEntrante**](FactureEntrante.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Facture extraite avec succès |  -  |
**400** | Format de facture non supporté ou invalide |  -  |
**401** | Non authentifié |  -  |
**404** | Flux non trouvé |  -  |
**503** | Service PDP indisponible |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

