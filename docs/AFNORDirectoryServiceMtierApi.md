# factpulse.AFNORDirectoryServiceMtierApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_siren_metier_api_v1_afnor_directory_siren_siren_get**](AFNORDirectoryServiceMtierApi.md#get_siren_metier_api_v1_afnor_directory_siren_siren_get) | **GET** /api/v1/afnor/directory/siren/{siren} | Récupérer une entreprise par SIREN (multi-tenant)
[**get_siret_metier_api_v1_afnor_directory_siret_siret_get**](AFNORDirectoryServiceMtierApi.md#get_siret_metier_api_v1_afnor_directory_siret_siret_get) | **GET** /api/v1/afnor/directory/siret/{siret} | Récupérer un établissement par SIRET (multi-tenant)
[**search_siren_metier_api_v1_afnor_directory_siren_search_post**](AFNORDirectoryServiceMtierApi.md#search_siren_metier_api_v1_afnor_directory_siren_search_post) | **POST** /api/v1/afnor/directory/siren/search | Rechercher des entreprises (multi-tenant)
[**search_siret_metier_api_v1_afnor_directory_siret_search_post**](AFNORDirectoryServiceMtierApi.md#search_siret_metier_api_v1_afnor_directory_siret_search_post) | **POST** /api/v1/afnor/directory/siret/search | Rechercher des établissements (multi-tenant)


# **get_siren_metier_api_v1_afnor_directory_siren_siren_get**
> object get_siren_metier_api_v1_afnor_directory_siren_siren_get(siren, pdp_credentials=pdp_credentials)

Récupérer une entreprise par SIREN (multi-tenant)

Récupère les informations d'une entreprise dans le Directory Service AFNOR. Les credentials PDP sont récupérés automatiquement via le client_uid du JWT, ou peuvent être fournis directement dans le body (zero-storage).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.pdp_credentials import PDPCredentials
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
    api_instance = factpulse.AFNORDirectoryServiceMtierApi(api_client)
    siren = 'siren_example' # str | 
    pdp_credentials = factpulse.PDPCredentials() # PDPCredentials |  (optional)

    try:
        # Récupérer une entreprise par SIREN (multi-tenant)
        api_response = api_instance.get_siren_metier_api_v1_afnor_directory_siren_siren_get(siren, pdp_credentials=pdp_credentials)
        print("The response of AFNORDirectoryServiceMtierApi->get_siren_metier_api_v1_afnor_directory_siren_siren_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORDirectoryServiceMtierApi->get_siren_metier_api_v1_afnor_directory_siren_siren_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siren** | **str**|  | 
 **pdp_credentials** | [**PDPCredentials**](PDPCredentials.md)|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entreprise trouvée |  -  |
**404** | Entreprise non trouvée |  -  |
**400** | Aucune config PDP fournie |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_siret_metier_api_v1_afnor_directory_siret_siret_get**
> object get_siret_metier_api_v1_afnor_directory_siret_siret_get(siret, pdp_credentials=pdp_credentials)

Récupérer un établissement par SIRET (multi-tenant)

Récupère les informations d'un établissement dans le Directory Service AFNOR. Les credentials PDP sont récupérés automatiquement via le client_uid du JWT, ou peuvent être fournis directement dans le body (zero-storage).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.pdp_credentials import PDPCredentials
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
    api_instance = factpulse.AFNORDirectoryServiceMtierApi(api_client)
    siret = 'siret_example' # str | 
    pdp_credentials = factpulse.PDPCredentials() # PDPCredentials |  (optional)

    try:
        # Récupérer un établissement par SIRET (multi-tenant)
        api_response = api_instance.get_siret_metier_api_v1_afnor_directory_siret_siret_get(siret, pdp_credentials=pdp_credentials)
        print("The response of AFNORDirectoryServiceMtierApi->get_siret_metier_api_v1_afnor_directory_siret_siret_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORDirectoryServiceMtierApi->get_siret_metier_api_v1_afnor_directory_siret_siret_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siret** | **str**|  | 
 **pdp_credentials** | [**PDPCredentials**](PDPCredentials.md)|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Établissement trouvé |  -  |
**404** | Établissement non trouvé |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_siren_metier_api_v1_afnor_directory_siren_search_post**
> object search_siren_metier_api_v1_afnor_directory_siren_search_post(body_search_siren_metier_api_v1_afnor_directory_siren_search_post)

Rechercher des entreprises (multi-tenant)

Recherche multi-critères d'entreprises dans le Directory Service AFNOR. Les credentials PDP sont récupérés automatiquement via le client_uid du JWT, ou peuvent être fournis directement dans le body (zero-storage).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_search_siren_metier_api_v1_afnor_directory_siren_search_post import BodySearchSirenMetierApiV1AfnorDirectorySirenSearchPost
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
    api_instance = factpulse.AFNORDirectoryServiceMtierApi(api_client)
    body_search_siren_metier_api_v1_afnor_directory_siren_search_post = factpulse.BodySearchSirenMetierApiV1AfnorDirectorySirenSearchPost() # BodySearchSirenMetierApiV1AfnorDirectorySirenSearchPost | 

    try:
        # Rechercher des entreprises (multi-tenant)
        api_response = api_instance.search_siren_metier_api_v1_afnor_directory_siren_search_post(body_search_siren_metier_api_v1_afnor_directory_siren_search_post)
        print("The response of AFNORDirectoryServiceMtierApi->search_siren_metier_api_v1_afnor_directory_siren_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORDirectoryServiceMtierApi->search_siren_metier_api_v1_afnor_directory_siren_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_search_siren_metier_api_v1_afnor_directory_siren_search_post** | [**BodySearchSirenMetierApiV1AfnorDirectorySirenSearchPost**](BodySearchSirenMetierApiV1AfnorDirectorySirenSearchPost.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Résultats de recherche |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_siret_metier_api_v1_afnor_directory_siret_search_post**
> object search_siret_metier_api_v1_afnor_directory_siret_search_post(body_search_siret_metier_api_v1_afnor_directory_siret_search_post)

Rechercher des établissements (multi-tenant)

Recherche multi-critères d'établissements dans le Directory Service AFNOR. Les credentials PDP sont récupérés automatiquement via le client_uid du JWT, ou peuvent être fournis directement dans le body (zero-storage).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_search_siret_metier_api_v1_afnor_directory_siret_search_post import BodySearchSiretMetierApiV1AfnorDirectorySiretSearchPost
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
    api_instance = factpulse.AFNORDirectoryServiceMtierApi(api_client)
    body_search_siret_metier_api_v1_afnor_directory_siret_search_post = factpulse.BodySearchSiretMetierApiV1AfnorDirectorySiretSearchPost() # BodySearchSiretMetierApiV1AfnorDirectorySiretSearchPost | 

    try:
        # Rechercher des établissements (multi-tenant)
        api_response = api_instance.search_siret_metier_api_v1_afnor_directory_siret_search_post(body_search_siret_metier_api_v1_afnor_directory_siret_search_post)
        print("The response of AFNORDirectoryServiceMtierApi->search_siret_metier_api_v1_afnor_directory_siret_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORDirectoryServiceMtierApi->search_siret_metier_api_v1_afnor_directory_siret_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_search_siret_metier_api_v1_afnor_directory_siret_search_post** | [**BodySearchSiretMetierApiV1AfnorDirectorySiretSearchPost**](BodySearchSiretMetierApiV1AfnorDirectorySiretSearchPost.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Résultats de recherche |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

