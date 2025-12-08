# factpulse.VrificationPDFXMLApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get**](VrificationPDFXMLApi.md#obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get) | **GET** /api/v1/verification/verifier-async/{id_tache}/statut | Obtenir le statut d&#39;une vérification asynchrone
[**obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get_0**](VrificationPDFXMLApi.md#obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get_0) | **GET** /api/v1/verification/verifier-async/{id_tache}/statut | Obtenir le statut d&#39;une vérification asynchrone
[**verifier_pdf_async_api_v1_verification_verifier_async_post**](VrificationPDFXMLApi.md#verifier_pdf_async_api_v1_verification_verifier_async_post) | **POST** /api/v1/verification/verifier-async | Vérifier la conformité PDF/XML Factur-X (asynchrone)
[**verifier_pdf_async_api_v1_verification_verifier_async_post_0**](VrificationPDFXMLApi.md#verifier_pdf_async_api_v1_verification_verifier_async_post_0) | **POST** /api/v1/verification/verifier-async | Vérifier la conformité PDF/XML Factur-X (asynchrone)
[**verifier_pdf_sync_api_v1_verification_verifier_post**](VrificationPDFXMLApi.md#verifier_pdf_sync_api_v1_verification_verifier_post) | **POST** /api/v1/verification/verifier | Vérifier la conformité PDF/XML Factur-X (synchrone)
[**verifier_pdf_sync_api_v1_verification_verifier_post_0**](VrificationPDFXMLApi.md#verifier_pdf_sync_api_v1_verification_verifier_post_0) | **POST** /api/v1/verification/verifier | Vérifier la conformité PDF/XML Factur-X (synchrone)


# **obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get**
> StatutTache obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get(id_tache)

Obtenir le statut d'une vérification asynchrone

Récupère le statut et le résultat d'une tâche de vérification asynchrone.

**Statuts possibles:**
- `PENDING`: Tâche en attente dans la file
- `STARTED`: Tâche en cours d'exécution
- `SUCCESS`: Tâche terminée avec succès (voir `resultat`)
- `FAILURE`: Erreur système (exception non gérée)

**Note:** Le champ `resultat.statut` peut être "SUCCES" ou "ERREUR"
indépendamment du statut Celery (qui sera toujours SUCCESS si la tâche s'est exécutée).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.statut_tache import StatutTache
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
    api_instance = factpulse.VrificationPDFXMLApi(api_client)
    id_tache = 'id_tache_example' # str | 

    try:
        # Obtenir le statut d'une vérification asynchrone
        api_response = api_instance.obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get(id_tache)
        print("The response of VrificationPDFXMLApi->obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VrificationPDFXMLApi->obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_tache** | **str**|  | 

### Return type

[**StatutTache**](StatutTache.md)

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

# **obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get_0**
> StatutTache obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get_0(id_tache)

Obtenir le statut d'une vérification asynchrone

Récupère le statut et le résultat d'une tâche de vérification asynchrone.

**Statuts possibles:**
- `PENDING`: Tâche en attente dans la file
- `STARTED`: Tâche en cours d'exécution
- `SUCCESS`: Tâche terminée avec succès (voir `resultat`)
- `FAILURE`: Erreur système (exception non gérée)

**Note:** Le champ `resultat.statut` peut être "SUCCES" ou "ERREUR"
indépendamment du statut Celery (qui sera toujours SUCCESS si la tâche s'est exécutée).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.statut_tache import StatutTache
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
    api_instance = factpulse.VrificationPDFXMLApi(api_client)
    id_tache = 'id_tache_example' # str | 

    try:
        # Obtenir le statut d'une vérification asynchrone
        api_response = api_instance.obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get_0(id_tache)
        print("The response of VrificationPDFXMLApi->obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VrificationPDFXMLApi->obtenir_statut_verification_api_v1_verification_verifier_async_id_tache_statut_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_tache** | **str**|  | 

### Return type

[**StatutTache**](StatutTache.md)

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

# **verifier_pdf_async_api_v1_verification_verifier_async_post**
> ReponseTache verifier_pdf_async_api_v1_verification_verifier_async_post(fichier_pdf, forcer_ocr=forcer_ocr)

Vérifier la conformité PDF/XML Factur-X (asynchrone)

Vérifie la conformité PDF/XML Factur-X de manière asynchrone.

**IMPORTANT**: Seuls les PDF Factur-X (avec XML embarqué) sont acceptés.
Les PDF sans XML Factur-X retourneront une erreur `NOT_FACTURX` dans le résultat.

Cette version utilise une tâche Celery et peut faire appel au service OCR
si le PDF est une image ou si `forcer_ocr=true`.

**Retourne immédiatement** un ID de tâche. Utilisez `/verifier-async/{id_tache}/statut`
pour récupérer le résultat.

**Principe de vérification (Factur-X 1.08):**
- Principe n°2: Le XML ne peut contenir que des infos présentes dans le PDF
- Principe n°4: Toute info XML doit être présente et conforme dans le PDF

**Champs vérifiés:**
- Identification: BT-1 (n° facture), BT-2 (date), BT-3 (type), BT-5 (devise), BT-23 (cadre)
- Vendeur: BT-27 (nom), BT-29 (SIRET), BT-30 (SIREN), BT-31 (TVA)
- Acheteur: BT-44 (nom), BT-46 (SIRET), BT-47 (SIREN), BT-48 (TVA)
- Montants: BT-109 (HT), BT-110 (TVA), BT-112 (TTC), BT-115 (à payer)
- Ventilation TVA: BT-116, BT-117, BT-118, BT-119
- Lignes de facture: BT-153, BT-129, BT-146, BT-131
- Notes obligatoires: PMT, PMD, AAB
- Règle BR-FR-09: cohérence SIRET/SIREN

**Avantages par rapport à la version synchrone:**
- Support OCR pour les PDF images (via service DocTR)
- Timeout plus long pour les gros documents
- Ne bloque pas le serveur

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.reponse_tache import ReponseTache
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
    api_instance = factpulse.VrificationPDFXMLApi(api_client)
    fichier_pdf = None # bytearray | Fichier PDF Factur-X à vérifier
    forcer_ocr = False # bool | Forcer l'utilisation de l'OCR même si le PDF contient du texte natif (optional) (default to False)

    try:
        # Vérifier la conformité PDF/XML Factur-X (asynchrone)
        api_response = api_instance.verifier_pdf_async_api_v1_verification_verifier_async_post(fichier_pdf, forcer_ocr=forcer_ocr)
        print("The response of VrificationPDFXMLApi->verifier_pdf_async_api_v1_verification_verifier_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VrificationPDFXMLApi->verifier_pdf_async_api_v1_verification_verifier_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fichier_pdf** | **bytearray**| Fichier PDF Factur-X à vérifier | 
 **forcer_ocr** | **bool**| Forcer l&#39;utilisation de l&#39;OCR même si le PDF contient du texte natif | [optional] [default to False]

### Return type

[**ReponseTache**](ReponseTache.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verifier_pdf_async_api_v1_verification_verifier_async_post_0**
> ReponseTache verifier_pdf_async_api_v1_verification_verifier_async_post_0(fichier_pdf, forcer_ocr=forcer_ocr)

Vérifier la conformité PDF/XML Factur-X (asynchrone)

Vérifie la conformité PDF/XML Factur-X de manière asynchrone.

**IMPORTANT**: Seuls les PDF Factur-X (avec XML embarqué) sont acceptés.
Les PDF sans XML Factur-X retourneront une erreur `NOT_FACTURX` dans le résultat.

Cette version utilise une tâche Celery et peut faire appel au service OCR
si le PDF est une image ou si `forcer_ocr=true`.

**Retourne immédiatement** un ID de tâche. Utilisez `/verifier-async/{id_tache}/statut`
pour récupérer le résultat.

**Principe de vérification (Factur-X 1.08):**
- Principe n°2: Le XML ne peut contenir que des infos présentes dans le PDF
- Principe n°4: Toute info XML doit être présente et conforme dans le PDF

**Champs vérifiés:**
- Identification: BT-1 (n° facture), BT-2 (date), BT-3 (type), BT-5 (devise), BT-23 (cadre)
- Vendeur: BT-27 (nom), BT-29 (SIRET), BT-30 (SIREN), BT-31 (TVA)
- Acheteur: BT-44 (nom), BT-46 (SIRET), BT-47 (SIREN), BT-48 (TVA)
- Montants: BT-109 (HT), BT-110 (TVA), BT-112 (TTC), BT-115 (à payer)
- Ventilation TVA: BT-116, BT-117, BT-118, BT-119
- Lignes de facture: BT-153, BT-129, BT-146, BT-131
- Notes obligatoires: PMT, PMD, AAB
- Règle BR-FR-09: cohérence SIRET/SIREN

**Avantages par rapport à la version synchrone:**
- Support OCR pour les PDF images (via service DocTR)
- Timeout plus long pour les gros documents
- Ne bloque pas le serveur

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.reponse_tache import ReponseTache
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
    api_instance = factpulse.VrificationPDFXMLApi(api_client)
    fichier_pdf = None # bytearray | Fichier PDF Factur-X à vérifier
    forcer_ocr = False # bool | Forcer l'utilisation de l'OCR même si le PDF contient du texte natif (optional) (default to False)

    try:
        # Vérifier la conformité PDF/XML Factur-X (asynchrone)
        api_response = api_instance.verifier_pdf_async_api_v1_verification_verifier_async_post_0(fichier_pdf, forcer_ocr=forcer_ocr)
        print("The response of VrificationPDFXMLApi->verifier_pdf_async_api_v1_verification_verifier_async_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VrificationPDFXMLApi->verifier_pdf_async_api_v1_verification_verifier_async_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fichier_pdf** | **bytearray**| Fichier PDF Factur-X à vérifier | 
 **forcer_ocr** | **bool**| Forcer l&#39;utilisation de l&#39;OCR même si le PDF contient du texte natif | [optional] [default to False]

### Return type

[**ReponseTache**](ReponseTache.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verifier_pdf_sync_api_v1_verification_verifier_post**
> ReponseVerificationSucces verifier_pdf_sync_api_v1_verification_verifier_post(fichier_pdf)

Vérifier la conformité PDF/XML Factur-X (synchrone)

Vérifie la conformité entre le PDF et son XML Factur-X embarqué.

**IMPORTANT**: Seuls les PDF Factur-X (avec XML embarqué) sont acceptés.
Les PDF sans XML Factur-X seront rejetés avec une erreur 400.

Cette version synchrone utilise uniquement l'extraction PDF native (pdfplumber).
Pour les PDF images nécessitant de l'OCR, utilisez l'endpoint `/verifier-async`.

**Principe de vérification (Factur-X 1.08):**
- Principe n°2: Le XML ne peut contenir que des infos présentes dans le PDF
- Principe n°4: Toute info XML doit être présente et conforme dans le PDF

**Champs vérifiés:**
- Identification: BT-1 (n° facture), BT-2 (date), BT-3 (type), BT-5 (devise), BT-23 (cadre)
- Vendeur: BT-27 (nom), BT-29 (SIRET), BT-30 (SIREN), BT-31 (TVA)
- Acheteur: BT-44 (nom), BT-46 (SIRET), BT-47 (SIREN), BT-48 (TVA)
- Montants: BT-109 (HT), BT-110 (TVA), BT-112 (TTC), BT-115 (à payer)
- Ventilation TVA: BT-116, BT-117, BT-118, BT-119
- Lignes de facture: BT-153, BT-129, BT-146, BT-131
- Notes obligatoires: PMT, PMD, AAB
- Règle BR-FR-09: cohérence SIRET/SIREN

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.reponse_verification_succes import ReponseVerificationSucces
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
    api_instance = factpulse.VrificationPDFXMLApi(api_client)
    fichier_pdf = None # bytearray | Fichier PDF Factur-X à vérifier

    try:
        # Vérifier la conformité PDF/XML Factur-X (synchrone)
        api_response = api_instance.verifier_pdf_sync_api_v1_verification_verifier_post(fichier_pdf)
        print("The response of VrificationPDFXMLApi->verifier_pdf_sync_api_v1_verification_verifier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VrificationPDFXMLApi->verifier_pdf_sync_api_v1_verification_verifier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fichier_pdf** | **bytearray**| Fichier PDF Factur-X à vérifier | 

### Return type

[**ReponseVerificationSucces**](ReponseVerificationSucces.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vérification réussie |  -  |
**400** | Erreur de vérification (PDF non Factur-X, invalide, etc.) |  -  |
**413** | PDF trop volumineux ou trop de pages |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verifier_pdf_sync_api_v1_verification_verifier_post_0**
> ReponseVerificationSucces verifier_pdf_sync_api_v1_verification_verifier_post_0(fichier_pdf)

Vérifier la conformité PDF/XML Factur-X (synchrone)

Vérifie la conformité entre le PDF et son XML Factur-X embarqué.

**IMPORTANT**: Seuls les PDF Factur-X (avec XML embarqué) sont acceptés.
Les PDF sans XML Factur-X seront rejetés avec une erreur 400.

Cette version synchrone utilise uniquement l'extraction PDF native (pdfplumber).
Pour les PDF images nécessitant de l'OCR, utilisez l'endpoint `/verifier-async`.

**Principe de vérification (Factur-X 1.08):**
- Principe n°2: Le XML ne peut contenir que des infos présentes dans le PDF
- Principe n°4: Toute info XML doit être présente et conforme dans le PDF

**Champs vérifiés:**
- Identification: BT-1 (n° facture), BT-2 (date), BT-3 (type), BT-5 (devise), BT-23 (cadre)
- Vendeur: BT-27 (nom), BT-29 (SIRET), BT-30 (SIREN), BT-31 (TVA)
- Acheteur: BT-44 (nom), BT-46 (SIRET), BT-47 (SIREN), BT-48 (TVA)
- Montants: BT-109 (HT), BT-110 (TVA), BT-112 (TTC), BT-115 (à payer)
- Ventilation TVA: BT-116, BT-117, BT-118, BT-119
- Lignes de facture: BT-153, BT-129, BT-146, BT-131
- Notes obligatoires: PMT, PMD, AAB
- Règle BR-FR-09: cohérence SIRET/SIREN

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.reponse_verification_succes import ReponseVerificationSucces
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
    api_instance = factpulse.VrificationPDFXMLApi(api_client)
    fichier_pdf = None # bytearray | Fichier PDF Factur-X à vérifier

    try:
        # Vérifier la conformité PDF/XML Factur-X (synchrone)
        api_response = api_instance.verifier_pdf_sync_api_v1_verification_verifier_post_0(fichier_pdf)
        print("The response of VrificationPDFXMLApi->verifier_pdf_sync_api_v1_verification_verifier_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VrificationPDFXMLApi->verifier_pdf_sync_api_v1_verification_verifier_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fichier_pdf** | **bytearray**| Fichier PDF Factur-X à vérifier | 

### Return type

[**ReponseVerificationSucces**](ReponseVerificationSucces.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vérification réussie |  -  |
**400** | Erreur de vérification (PDF non Factur-X, invalide, etc.) |  -  |
**413** | PDF trop volumineux ou trop de pages |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

