# factpulse.AFNORPDPPADirectoryServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_post**](AFNORPDPPADirectoryServiceApi.md#create_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_post) | **POST** /api/v1/afnor/directory/v1/directory-line | Creating a directory line
[**create_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_post**](AFNORPDPPADirectoryServiceApi.md#create_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_post) | **POST** /api/v1/afnor/directory/v1/routing-code | Create a routing code
[**delete_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_delete**](AFNORPDPPADirectoryServiceApi.md#delete_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_delete) | **DELETE** /api/v1/afnor/directory/v1/directory-line/id-instance:{id_instance} | Delete a directory line
[**directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get**](AFNORPDPPADirectoryServiceApi.md#directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get) | **GET** /api/v1/afnor/directory/v1/healthcheck | Healthcheck Directory Service
[**get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get**](AFNORPDPPADirectoryServiceApi.md#get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get) | **GET** /api/v1/afnor/directory/v1/directory-line/code:{addressing_identifier} | Get a directory line
[**get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get**](AFNORPDPPADirectoryServiceApi.md#get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get) | **GET** /api/v1/afnor/directory/v1/directory-line/id-instance:{id_instance} | Get a directory line
[**get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get**](AFNORPDPPADirectoryServiceApi.md#get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get) | **GET** /api/v1/afnor/directory/v1/routing-code/id-instance:{id_instance} | Get a routing code by instance-id
[**get_routing_code_by_siret_and_code_proxy_api_v1_afnor_directory_v1_routing_code_siret_siret_code_routing_identifier_get**](AFNORPDPPADirectoryServiceApi.md#get_routing_code_by_siret_and_code_proxy_api_v1_afnor_directory_v1_routing_code_siret_siret_code_routing_identifier_get) | **GET** /api/v1/afnor/directory/v1/routing-code/siret:{siret}/code:{routing_identifier} | Get a routing code by SIRET and routing identifier
[**get_siren_by_code_insee_proxy_api_v1_afnor_directory_v1_siren_code_insee_siren_get**](AFNORPDPPADirectoryServiceApi.md#get_siren_by_code_insee_proxy_api_v1_afnor_directory_v1_siren_code_insee_siren_get) | **GET** /api/v1/afnor/directory/v1/siren/code-insee:{siren} | Consult a siren (legal unit) by SIREN number
[**get_siren_by_id_instance_proxy_api_v1_afnor_directory_v1_siren_id_instance_id_instance_get**](AFNORPDPPADirectoryServiceApi.md#get_siren_by_id_instance_proxy_api_v1_afnor_directory_v1_siren_id_instance_id_instance_get) | **GET** /api/v1/afnor/directory/v1/siren/id-instance:{id_instance} | Gets a siren (legal unit) by instance ID
[**get_siret_by_code_insee_proxy_api_v1_afnor_directory_v1_siret_code_insee_siret_get**](AFNORPDPPADirectoryServiceApi.md#get_siret_by_code_insee_proxy_api_v1_afnor_directory_v1_siret_code_insee_siret_get) | **GET** /api/v1/afnor/directory/v1/siret/code-insee:{siret} | Gets a siret (facility) by SIRET number
[**get_siret_by_id_instance_proxy_api_v1_afnor_directory_v1_siret_id_instance_id_instance_get**](AFNORPDPPADirectoryServiceApi.md#get_siret_by_id_instance_proxy_api_v1_afnor_directory_v1_siret_id_instance_id_instance_get) | **GET** /api/v1/afnor/directory/v1/siret/id-instance:{id_instance} | Gets a siret (facility) by id-instance
[**patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch**](AFNORPDPPADirectoryServiceApi.md#patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch) | **PATCH** /api/v1/afnor/directory/v1/directory-line/id-instance:{id_instance} | Partially updates a directory line
[**patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch**](AFNORPDPPADirectoryServiceApi.md#patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch) | **PATCH** /api/v1/afnor/directory/v1/routing-code/id-instance:{id_instance} | Partially update a private routing code
[**put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put**](AFNORPDPPADirectoryServiceApi.md#put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put) | **PUT** /api/v1/afnor/directory/v1/routing-code/id-instance:{id_instance} | Completely update a private routing code
[**search_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_search_post**](AFNORPDPPADirectoryServiceApi.md#search_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_search_post) | **POST** /api/v1/afnor/directory/v1/directory-line/search | Search for a directory line
[**search_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_search_post**](AFNORPDPPADirectoryServiceApi.md#search_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_search_post) | **POST** /api/v1/afnor/directory/v1/routing-code/search | Search for a routing code
[**search_siren_proxy_api_v1_afnor_directory_v1_siren_search_post**](AFNORPDPPADirectoryServiceApi.md#search_siren_proxy_api_v1_afnor_directory_v1_siren_search_post) | **POST** /api/v1/afnor/directory/v1/siren/search | SIREN search (or legal unit)
[**search_siret_proxy_api_v1_afnor_directory_v1_siret_search_post**](AFNORPDPPADirectoryServiceApi.md#search_siret_proxy_api_v1_afnor_directory_v1_siret_search_post) | **POST** /api/v1/afnor/directory/v1/siret/search | Search for a SIRET (facility)


# **create_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_post**
> object create_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_post()

Creating a directory line

Créer une ligne dans l'annuaire

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
        # Creating a directory line
        api_response = api_instance.create_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_post()
        print("The response of AFNORPDPPADirectoryServiceApi->create_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->create_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_post: %s\n" % e)
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
**201** | Ligne d&#39;annuaire créée avec succès |  -  |
**400** | Requête invalide |  -  |
**401** | Non authentifié |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_post**
> object create_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_post()

Create a routing code

Créer un code de routage dans l'annuaire

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
        # Create a routing code
        api_response = api_instance.create_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_post()
        print("The response of AFNORPDPPADirectoryServiceApi->create_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->create_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_post: %s\n" % e)
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
**201** | Code de routage créé avec succès |  -  |
**400** | Requête invalide |  -  |
**401** | Non authentifié |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_delete**
> object delete_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_delete(id_instance)

Delete a directory line

Supprimer une ligne d'annuaire

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
    id_instance = 'id_instance_example' # str | 

    try:
        # Delete a directory line
        api_response = api_instance.delete_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_delete(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->delete_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->delete_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**|  | 

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
**204** | Ligne d&#39;annuaire supprimée |  -  |
**404** | Ligne d&#39;annuaire non trouvée |  -  |
**401** | Non authentifié |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get**
> object get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get(addressing_identifier)

Get a directory line

Obtenir une ligne d'annuaire identifiée par un identifiant d'adressage

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
    addressing_identifier = 'addressing_identifier_example' # str | 

    try:
        # Get a directory line
        api_response = api_instance.get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get(addressing_identifier)
        print("The response of AFNORPDPPADirectoryServiceApi->get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addressing_identifier** | **str**|  | 

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
**200** | Détails de la ligne d&#39;annuaire |  -  |
**404** | Ligne d&#39;annuaire non trouvée |  -  |
**401** | Non authentifié |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get**
> object get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get(id_instance)

Get a directory line

Obtenir une ligne d'annuaire identifiée par son idInstance

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
    id_instance = 'id_instance_example' # str | 

    try:
        # Get a directory line
        api_response = api_instance.get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**|  | 

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
**200** | Détails de la ligne d&#39;annuaire |  -  |
**404** | Ligne d&#39;annuaire non trouvée |  -  |
**401** | Non authentifié |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get**
> object get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get(id_instance)

Get a routing code by instance-id

Obtenir un code de routage identifié par son idInstance

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
    id_instance = 'id_instance_example' # str | 

    try:
        # Get a routing code by instance-id
        api_response = api_instance.get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**|  | 

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
**200** | Détails du code de routage |  -  |
**404** | Code de routage non trouvé |  -  |
**401** | Non authentifié |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routing_code_by_siret_and_code_proxy_api_v1_afnor_directory_v1_routing_code_siret_siret_code_routing_identifier_get**
> object get_routing_code_by_siret_and_code_proxy_api_v1_afnor_directory_v1_routing_code_siret_siret_code_routing_identifier_get(siret, routing_identifier)

Get a routing code by SIRET and routing identifier

Consulter un code de routage identifié par SIRET et identifiant de routage

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
    siret = 'siret_example' # str | 
    routing_identifier = 'routing_identifier_example' # str | 

    try:
        # Get a routing code by SIRET and routing identifier
        api_response = api_instance.get_routing_code_by_siret_and_code_proxy_api_v1_afnor_directory_v1_routing_code_siret_siret_code_routing_identifier_get(siret, routing_identifier)
        print("The response of AFNORPDPPADirectoryServiceApi->get_routing_code_by_siret_and_code_proxy_api_v1_afnor_directory_v1_routing_code_siret_siret_code_routing_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->get_routing_code_by_siret_and_code_proxy_api_v1_afnor_directory_v1_routing_code_siret_siret_code_routing_identifier_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siret** | **str**|  | 
 **routing_identifier** | **str**|  | 

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
**200** | Détails du code de routage |  -  |
**404** | Code de routage non trouvé |  -  |
**401** | Non authentifié |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_siren_by_code_insee_proxy_api_v1_afnor_directory_v1_siren_code_insee_siren_get**
> object get_siren_by_code_insee_proxy_api_v1_afnor_directory_v1_siren_code_insee_siren_get(siren)

Consult a siren (legal unit) by SIREN number

Retourne les détails d'une entreprise (unité légale) identifiée par son numéro SIREN

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
        # Consult a siren (legal unit) by SIREN number
        api_response = api_instance.get_siren_by_code_insee_proxy_api_v1_afnor_directory_v1_siren_code_insee_siren_get(siren)
        print("The response of AFNORPDPPADirectoryServiceApi->get_siren_by_code_insee_proxy_api_v1_afnor_directory_v1_siren_code_insee_siren_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->get_siren_by_code_insee_proxy_api_v1_afnor_directory_v1_siren_code_insee_siren_get: %s\n" % e)
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

# **get_siren_by_id_instance_proxy_api_v1_afnor_directory_v1_siren_id_instance_id_instance_get**
> object get_siren_by_id_instance_proxy_api_v1_afnor_directory_v1_siren_id_instance_id_instance_get(id_instance)

Gets a siren (legal unit) by instance ID

Obtenir une entreprise (unité légale) identifiée par son idInstance

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
    id_instance = 'id_instance_example' # str | 

    try:
        # Gets a siren (legal unit) by instance ID
        api_response = api_instance.get_siren_by_id_instance_proxy_api_v1_afnor_directory_v1_siren_id_instance_id_instance_get(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->get_siren_by_id_instance_proxy_api_v1_afnor_directory_v1_siren_id_instance_id_instance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->get_siren_by_id_instance_proxy_api_v1_afnor_directory_v1_siren_id_instance_id_instance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**|  | 

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

# **get_siret_by_code_insee_proxy_api_v1_afnor_directory_v1_siret_code_insee_siret_get**
> object get_siret_by_code_insee_proxy_api_v1_afnor_directory_v1_siret_code_insee_siret_get(siret)

Gets a siret (facility) by SIRET number

Obtenir un établissement identifié par son numéro SIRET

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
    siret = 'siret_example' # str | 

    try:
        # Gets a siret (facility) by SIRET number
        api_response = api_instance.get_siret_by_code_insee_proxy_api_v1_afnor_directory_v1_siret_code_insee_siret_get(siret)
        print("The response of AFNORPDPPADirectoryServiceApi->get_siret_by_code_insee_proxy_api_v1_afnor_directory_v1_siret_code_insee_siret_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->get_siret_by_code_insee_proxy_api_v1_afnor_directory_v1_siret_code_insee_siret_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siret** | **str**|  | 

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
**200** | Informations de l&#39;établissement |  -  |
**404** | Établissement non trouvé |  -  |
**401** | Non authentifié |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_siret_by_id_instance_proxy_api_v1_afnor_directory_v1_siret_id_instance_id_instance_get**
> object get_siret_by_id_instance_proxy_api_v1_afnor_directory_v1_siret_id_instance_id_instance_get(id_instance)

Gets a siret (facility) by id-instance

Obtenir un établissement identifié par son idInstance

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
    id_instance = 'id_instance_example' # str | 

    try:
        # Gets a siret (facility) by id-instance
        api_response = api_instance.get_siret_by_id_instance_proxy_api_v1_afnor_directory_v1_siret_id_instance_id_instance_get(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->get_siret_by_id_instance_proxy_api_v1_afnor_directory_v1_siret_id_instance_id_instance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->get_siret_by_id_instance_proxy_api_v1_afnor_directory_v1_siret_id_instance_id_instance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**|  | 

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
**200** | Informations de l&#39;établissement |  -  |
**404** | Établissement non trouvé |  -  |
**401** | Non authentifié |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch**
> object patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch(id_instance)

Partially updates a directory line

Mettre à jour partiellement une ligne d'annuaire

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
    id_instance = 'id_instance_example' # str | 

    try:
        # Partially updates a directory line
        api_response = api_instance.patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**|  | 

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
**200** | Ligne d&#39;annuaire mise à jour |  -  |
**404** | Ligne d&#39;annuaire non trouvée |  -  |
**401** | Non authentifié |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch**
> object patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch(id_instance)

Partially update a private routing code

Mettre à jour partiellement un code de routage privé

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
    id_instance = 'id_instance_example' # str | 

    try:
        # Partially update a private routing code
        api_response = api_instance.patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**|  | 

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
**200** | Code de routage mis à jour |  -  |
**404** | Code de routage non trouvé |  -  |
**401** | Non authentifié |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put**
> object put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put(id_instance)

Completely update a private routing code

Mettre à jour complètement un code de routage privé

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
    id_instance = 'id_instance_example' # str | 

    try:
        # Completely update a private routing code
        api_response = api_instance.put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**|  | 

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
**200** | Code de routage mis à jour |  -  |
**404** | Code de routage non trouvé |  -  |
**401** | Non authentifié |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_search_post**
> object search_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_search_post()

Search for a directory line

Rechercher des lignes d'annuaire selon des critères

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
        # Search for a directory line
        api_response = api_instance.search_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_search_post()
        print("The response of AFNORPDPPADirectoryServiceApi->search_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->search_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_search_post: %s\n" % e)
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

# **search_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_search_post**
> object search_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_search_post()

Search for a routing code

Rechercher des codes de routage selon des critères

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
        # Search for a routing code
        api_response = api_instance.search_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_search_post()
        print("The response of AFNORPDPPADirectoryServiceApi->search_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->search_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_search_post: %s\n" % e)
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

# **search_siren_proxy_api_v1_afnor_directory_v1_siren_search_post**
> object search_siren_proxy_api_v1_afnor_directory_v1_siren_search_post()

SIREN search (or legal unit)

Recherche multi-critères d'entreprises (unités légales)

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
        # SIREN search (or legal unit)
        api_response = api_instance.search_siren_proxy_api_v1_afnor_directory_v1_siren_search_post()
        print("The response of AFNORPDPPADirectoryServiceApi->search_siren_proxy_api_v1_afnor_directory_v1_siren_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->search_siren_proxy_api_v1_afnor_directory_v1_siren_search_post: %s\n" % e)
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
**200** | Retourne une ou plusieurs entreprises |  -  |
**401** | Non authentifié |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_siret_proxy_api_v1_afnor_directory_v1_siret_search_post**
> object search_siret_proxy_api_v1_afnor_directory_v1_siret_search_post()

Search for a SIRET (facility)

Recherche multi-critères d'établissements

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
        # Search for a SIRET (facility)
        api_response = api_instance.search_siret_proxy_api_v1_afnor_directory_v1_siret_search_post()
        print("The response of AFNORPDPPADirectoryServiceApi->search_siret_proxy_api_v1_afnor_directory_v1_siret_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->search_siret_proxy_api_v1_afnor_directory_v1_siret_search_post: %s\n" % e)
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
**200** | Retourne un ou plusieurs établissements |  -  |
**401** | Non authentifié |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

