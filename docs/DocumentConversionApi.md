# factpulse.DocumentConversionApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_document_async_api_v1_convert_async_post**](DocumentConversionApi.md#convert_document_async_api_v1_convert_async_post) | **POST** /api/v1/convert/async | Convertir un document en Factur-X (mode asynchrone)
[**download_file_api_v1_convert_conversion_id_download_filename_get**](DocumentConversionApi.md#download_file_api_v1_convert_conversion_id_download_filename_get) | **GET** /api/v1/convert/{conversion_id}/download/{filename} | Télécharger un fichier généré
[**get_conversion_status_api_v1_convert_conversion_id_status_get**](DocumentConversionApi.md#get_conversion_status_api_v1_convert_conversion_id_status_get) | **GET** /api/v1/convert/{conversion_id}/status | Vérifier le statut d&#39;une conversion
[**resume_conversion_api_v1_convert_conversion_id_resume_post**](DocumentConversionApi.md#resume_conversion_api_v1_convert_conversion_id_resume_post) | **POST** /api/v1/convert/{conversion_id}/resume | Reprendre une conversion avec corrections


# **convert_document_async_api_v1_convert_async_post**
> object convert_document_async_api_v1_convert_async_post(file, output=output, callback_url=callback_url, webhook_mode=webhook_mode)

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

# Defining the host is optional and defaults to https://factpulse.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "https://factpulse.fr"
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
    webhook_mode = 'inline' # str | Mode de livraison du contenu: 'inline' (base64 dans webhook) ou 'download_url' (URL temporaire 1h) (optional) (default to 'inline')

    try:
        # Convertir un document en Factur-X (mode asynchrone)
        api_response = api_instance.convert_document_async_api_v1_convert_async_post(file, output=output, callback_url=callback_url, webhook_mode=webhook_mode)
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
 **webhook_mode** | **str**| Mode de livraison du contenu: &#39;inline&#39; (base64 dans webhook) ou &#39;download_url&#39; (URL temporaire 1h) | [optional] [default to &#39;inline&#39;]

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
**401** | Authentication required - Invalid or missing JWT token |  -  |

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

# Defining the host is optional and defaults to https://factpulse.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "https://factpulse.fr"
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
    conversion_id = 'conversion_id_example' # str | Conversion ID returned by POST /convert (UUID format)
    filename = 'filename_example' # str | File to download: 'facturx.pdf' or 'facturx.xml'

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
 **conversion_id** | **str**| Conversion ID returned by POST /convert (UUID format) | 
 **filename** | **str**| File to download: &#39;facturx.pdf&#39; or &#39;facturx.xml&#39; | 

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
**401** | Authentication required - Invalid or missing JWT token |  -  |

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

# Defining the host is optional and defaults to https://factpulse.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "https://factpulse.fr"
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
    conversion_id = 'conversion_id_example' # str | Conversion ID returned by POST /convert (UUID format)

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
 **conversion_id** | **str**| Conversion ID returned by POST /convert (UUID format) | 

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
**401** | Authentication required - Invalid or missing JWT token |  -  |

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
from factpulse.models.convert_success_response import ConvertSuccessResponse
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

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.DocumentConversionApi(api_client)
    conversion_id = 'conversion_id_example' # str | Conversion ID returned by POST /convert (UUID format)
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
 **conversion_id** | **str**| Conversion ID returned by POST /convert (UUID format) | 
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
**200** | Successful Response |  -  |
**404** | Conversion non trouvée ou expirée |  -  |
**422** | Validation toujours en échec |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

