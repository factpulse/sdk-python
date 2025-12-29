# factpulse.DocumentConversionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_document_api_v1_convert_post**](DocumentConversionApi.md#convert_document_api_v1_convert_post) | **POST** /api/v1/convert | Convertir un document en Factur-X
[**convert_document_async_api_v1_convert_async_post**](DocumentConversionApi.md#convert_document_async_api_v1_convert_async_post) | **POST** /api/v1/convert/async | Convertir un document en Factur-X (mode asynchrone)
[**download_file_api_v1_convert_conversion_id_download_filename_get**](DocumentConversionApi.md#download_file_api_v1_convert_conversion_id_download_filename_get) | **GET** /api/v1/convert/{conversion_id}/download/{filename} | Télécharger un fichier généré
[**get_conversion_status_api_v1_convert_conversion_id_status_get**](DocumentConversionApi.md#get_conversion_status_api_v1_convert_conversion_id_status_get) | **GET** /api/v1/convert/{conversion_id}/status | Vérifier le statut d&#39;une conversion
[**resume_conversion_api_v1_convert_conversion_id_resume_post**](DocumentConversionApi.md#resume_conversion_api_v1_convert_conversion_id_resume_post) | **POST** /api/v1/convert/{conversion_id}/resume | Reprendre une conversion avec corrections


# **convert_document_api_v1_convert_post**
> ConvertSuccessResponse convert_document_api_v1_convert_post(file, output=output, callback_url=callback_url)

Convertir un document en Factur-X

Convertit un document (PDF, DOCX, XLSX, image) en Factur-X conforme.

## Workflow

1. **Upload** : Le document est envoyé en multipart/form-data
2. **Extraction OCR + Classification** : Mistral OCR extrait les données et classifie le document en un seul appel
3. **Enrichissement** : Les données sont enrichies via SIRENE (SIRET → raison sociale)
4. **Validation** : Les règles Schematron sont appliquées
5. **Génération** : Le Factur-X PDF/A-3 est généré

## Réponses possibles

- **200** : Conversion réussie, fichiers disponibles
- **202** : Données manquantes, complétion requise
- **422** : Validation échouée, corrections nécessaires
- **400** : Fichier invalide
- **429** : Quota dépassé

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
    api_instance = factpulse.DocumentConversionApi(api_client)
    file = None # bytearray | Document à convertir (PDF, DOCX, XLSX, JPG, PNG)
    output = 'pdf' # str | Format de sortie: pdf, xml, both (optional) (default to 'pdf')
    callback_url = 'callback_url_example' # str |  (optional)

    try:
        # Convertir un document en Factur-X
        api_response = api_instance.convert_document_api_v1_convert_post(file, output=output, callback_url=callback_url)
        print("The response of DocumentConversionApi->convert_document_api_v1_convert_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentConversionApi->convert_document_api_v1_convert_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| Document à convertir (PDF, DOCX, XLSX, JPG, PNG) | 
 **output** | **str**| Format de sortie: pdf, xml, both | [optional] [default to &#39;pdf&#39;]
 **callback_url** | **str**|  | [optional] 

### Return type

[**ConvertSuccessResponse**](ConvertSuccessResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversion réussie |  -  |
**202** | Données manquantes |  -  |
**422** | Validation échouée |  -  |
**400** | Fichier invalide |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_document_async_api_v1_convert_async_post**
> object convert_document_async_api_v1_convert_async_post(file, output=output, callback_url=callback_url)

Convertir un document en Factur-X (mode asynchrone)

Lance une conversion asynchrone via Celery.

## Workflow

1. **Upload** : Le document est envoyé en multipart/form-data
2. **Task Celery** : La tâche est mise en file d'attente
3. **Callback** : Notification par webhook à la fin

## Réponses possibles

- **202** : Tâche acceptée, en cours de traitement
- **400** : Fichier invalide

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
    api_instance = factpulse.DocumentConversionApi(api_client)
    file = None # bytearray | Document à convertir (PDF, DOCX, XLSX, JPG, PNG)
    output = 'pdf' # str | Format de sortie: pdf, xml, both (optional) (default to 'pdf')
    callback_url = 'callback_url_example' # str |  (optional)

    try:
        # Convertir un document en Factur-X (mode asynchrone)
        api_response = api_instance.convert_document_async_api_v1_convert_async_post(file, output=output, callback_url=callback_url)
        print("The response of DocumentConversionApi->convert_document_async_api_v1_convert_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentConversionApi->convert_document_async_api_v1_convert_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| Document à convertir (PDF, DOCX, XLSX, JPG, PNG) | 
 **output** | **str**| Format de sortie: pdf, xml, both | [optional] [default to &#39;pdf&#39;]
 **callback_url** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**202** | Tâche acceptée |  -  |
**400** | Fichier invalide |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_api_v1_convert_conversion_id_download_filename_get**
> object download_file_api_v1_convert_conversion_id_download_filename_get(conversion_id, filename)

Télécharger un fichier généré

Télécharge le fichier Factur-X PDF ou XML généré.

## Fichiers disponibles

- `facturx.pdf` : PDF/A-3 avec XML embarqué
- `facturx.xml` : XML CII seul (Cross Industry Invoice)

Les fichiers sont disponibles pendant 24 heures après génération.

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
    api_instance = factpulse.DocumentConversionApi(api_client)
    conversion_id = 'conversion_id_example' # str | 
    filename = 'filename_example' # str | 

    try:
        # Télécharger un fichier généré
        api_response = api_instance.download_file_api_v1_convert_conversion_id_download_filename_get(conversion_id, filename)
        print("The response of DocumentConversionApi->download_file_api_v1_convert_conversion_id_download_filename_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentConversionApi->download_file_api_v1_convert_conversion_id_download_filename_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversion_id** | **str**|  | 
 **filename** | **str**|  | 

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
**200** | Fichier téléchargé |  -  |
**404** | Fichier non trouvé ou expiré |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversion_status_api_v1_convert_conversion_id_status_get**
> Dict[str, object] get_conversion_status_api_v1_convert_conversion_id_status_get(conversion_id)

Vérifier le statut d'une conversion

Retourne le statut actuel d'une conversion asynchrone.

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
    api_instance = factpulse.DocumentConversionApi(api_client)
    conversion_id = 'conversion_id_example' # str | 

    try:
        # Vérifier le statut d'une conversion
        api_response = api_instance.get_conversion_status_api_v1_convert_conversion_id_status_get(conversion_id)
        print("The response of DocumentConversionApi->get_conversion_status_api_v1_convert_conversion_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentConversionApi->get_conversion_status_api_v1_convert_conversion_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversion_id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_conversion_api_v1_convert_conversion_id_resume_post**
> ConvertSuccessResponse resume_conversion_api_v1_convert_conversion_id_resume_post(conversion_id, convert_resume_request)

Reprendre une conversion avec corrections

Reprend une conversion après complétion des données manquantes ou correction des erreurs.

L'extraction OCR est conservée, les données sont mises à jour avec les corrections,
puis une nouvelle validation Schematron est effectuée.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.convert_resume_request import ConvertResumeRequest
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
    api_instance = factpulse.DocumentConversionApi(api_client)
    conversion_id = 'conversion_id_example' # str | 
    convert_resume_request = factpulse.ConvertResumeRequest() # ConvertResumeRequest | 

    try:
        # Reprendre une conversion avec corrections
        api_response = api_instance.resume_conversion_api_v1_convert_conversion_id_resume_post(conversion_id, convert_resume_request)
        print("The response of DocumentConversionApi->resume_conversion_api_v1_convert_conversion_id_resume_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentConversionApi->resume_conversion_api_v1_convert_conversion_id_resume_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversion_id** | **str**|  | 
 **convert_resume_request** | [**ConvertResumeRequest**](ConvertResumeRequest.md)|  | 

### Return type

[**ConvertSuccessResponse**](ConvertSuccessResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversion réussie |  -  |
**404** | Conversion non trouvée ou expirée |  -  |
**422** | Validation toujours en échec |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

