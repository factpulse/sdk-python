# factpulse.SignatureLectroniqueApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generer_certificat_test_api_v1_traitement_generer_certificat_test_post**](SignatureLectroniqueApi.md#generer_certificat_test_api_v1_traitement_generer_certificat_test_post) | **POST** /api/v1/traitement/generer-certificat-test | Générer un certificat X.509 auto-signé de test
[**signer_pdf_api_v1_traitement_signer_pdf_post**](SignatureLectroniqueApi.md#signer_pdf_api_v1_traitement_signer_pdf_post) | **POST** /api/v1/traitement/signer-pdf | Signer un PDF avec le certificat du client (PAdES-B-LT)
[**signer_pdf_async_api_v1_traitement_signer_pdf_async_post**](SignatureLectroniqueApi.md#signer_pdf_async_api_v1_traitement_signer_pdf_async_post) | **POST** /api/v1/traitement/signer-pdf-async | Signer un PDF de manière asynchrone (Celery)
[**valider_signature_pdf_endpoint_api_v1_traitement_valider_signature_pdf_post**](SignatureLectroniqueApi.md#valider_signature_pdf_endpoint_api_v1_traitement_valider_signature_pdf_post) | **POST** /api/v1/traitement/valider-signature-pdf | Valider les signatures électroniques d&#39;un PDF


# **generer_certificat_test_api_v1_traitement_generer_certificat_test_post**
> GenerateCertificateResponse generer_certificat_test_api_v1_traitement_generer_certificat_test_post(generate_certificate_request)

Générer un certificat X.509 auto-signé de test

Génère un certificat X.509 auto-signé pour les tests de signature électronique PDF.

    **⚠️ ATTENTION : Certificat de TEST uniquement !**

    Ce certificat est :
    - ✅ Adapté pour tests et développement
    - ✅ Compatible signature PDF (PAdES)
    - ✅ Conforme eIDAS niveau **SES** (Simple Electronic Signature)
    - ❌ **JAMAIS utilisable en production**
    - ❌ **Non reconnu** par les navigateurs et lecteurs PDF
    - ❌ **Aucune valeur juridique**

    ## Niveaux eIDAS

    - **SES** (Simple) : Certificat auto-signé ← Généré par cet endpoint
    - **AdES** (Advanced) : Certificat CA commerciale (Let's Encrypt, etc.)
    - **QES** (Qualified) : Certificat qualifié PSCO (CertEurope, Universign, etc.)

    ## Utilisation

    Une fois généré, le certificat peut être :

    1. **Enregistré dans Django** (recommandé) :
       - Django Admin > Certificats de signature
       - Upload `certificat_pem` et `cle_privee_pem`

    2. **Utilisé directement** :
       - Signer un PDF avec `/signer-pdf`
       - Le certificat sera automatiquement utilisé

    ## Exemple d'appel

    ```bash
    curl -X POST "https://www.factpulse.fr/api/facturation/generer-certificat-test" \
      -H "Authorization: Bearer eyJ0eXAi..." \
      -H "Content-Type: application/json" \
      -d '{
        "cn": "Test Client XYZ",
        "organisation": "Client XYZ SARL",
        "email": "contact@xyz.fr",
        "duree_jours": 365
      }'
    ```

    ## Cas d'usage

    - Tests de signature PDF en développement
    - POC de signature électronique
    - Formation et démos
    - Tests d'intégration automatisés

    ## Conformité technique

    Certificat généré avec :
    - Clé RSA 2048 ou 4096 bits
    - Algorithme SHA-256
    - Extensions Key Usage : `digitalSignature`, `contentCommitment` (non-repudiation)
    - Extensions Extended Key Usage : `codeSigning`, `emailProtection`
    - Validité : 1 jour à 10 ans (configurable)
    - Format : PEM (certificat et clé)
    - Optionnel : PKCS#12 (.p12)

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.generate_certificate_request import GenerateCertificateRequest
from factpulse.models.generate_certificate_response import GenerateCertificateResponse
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
    api_instance = factpulse.SignatureLectroniqueApi(api_client)
    generate_certificate_request = factpulse.GenerateCertificateRequest() # GenerateCertificateRequest | 

    try:
        # Générer un certificat X.509 auto-signé de test
        api_response = api_instance.generer_certificat_test_api_v1_traitement_generer_certificat_test_post(generate_certificate_request)
        print("The response of SignatureLectroniqueApi->generer_certificat_test_api_v1_traitement_generer_certificat_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignatureLectroniqueApi->generer_certificat_test_api_v1_traitement_generer_certificat_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_certificate_request** | [**GenerateCertificateRequest**](GenerateCertificateRequest.md)|  | 

### Return type

[**GenerateCertificateResponse**](GenerateCertificateResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificat généré avec succès |  -  |
**400** | Requête invalide (paramètres incorrects) |  -  |
**500** | Erreur serveur lors de la génération |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signer_pdf_api_v1_traitement_signer_pdf_post**
> object signer_pdf_api_v1_traitement_signer_pdf_post(fichier_pdf, raison=raison, localisation=localisation, contact=contact, field_name=field_name, use_pades_lt=use_pades_lt, use_timestamp=use_timestamp)

Signer un PDF avec le certificat du client (PAdES-B-LT)

Signe un PDF uploadé avec le certificat électronique configuré pour le client (via client_uid du JWT).

    **Standards supportés** : PAdES-B-B, PAdES-B-T (horodatage), PAdES-B-LT (archivage long terme).

    **Niveaux eIDAS** : SES (auto-signé), AdES (CA commerciale), QES (PSCO - hors scope).

    **⚠️ Disclaimer légal** : Les signatures générées sont des cachets électroniques au sens
    du règlement eIDAS. Le niveau de validité juridique dépend du certificat utilisé (SES/AdES/QES).
    FactPulse ne fournit pas de certificats qualifiés QES - vous devez obtenir un certificat auprès
    d'un PSCO (Prestataire de Services de Confiance qualifié) pour une validité juridique maximale.

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
    api_instance = factpulse.SignatureLectroniqueApi(api_client)
    fichier_pdf = None # bytearray | Fichier PDF à signer (sera traité puis retourné signé en base64)
    raison = 'raison_example' # str |  (optional)
    localisation = 'localisation_example' # str |  (optional)
    contact = 'contact_example' # str |  (optional)
    field_name = 'FactPulseSignature' # str | Nom du champ de signature PDF (optional) (default to 'FactPulseSignature')
    use_pades_lt = False # bool | Activer PAdES-B-LT (archivage long terme avec données de validation embarquées). NÉCESSITE un certificat avec accès OCSP/CRL. (optional) (default to False)
    use_timestamp = True # bool | Activer l'horodatage RFC 3161 avec FreeTSA (PAdES-B-T) (optional) (default to True)

    try:
        # Signer un PDF avec le certificat du client (PAdES-B-LT)
        api_response = api_instance.signer_pdf_api_v1_traitement_signer_pdf_post(fichier_pdf, raison=raison, localisation=localisation, contact=contact, field_name=field_name, use_pades_lt=use_pades_lt, use_timestamp=use_timestamp)
        print("The response of SignatureLectroniqueApi->signer_pdf_api_v1_traitement_signer_pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignatureLectroniqueApi->signer_pdf_api_v1_traitement_signer_pdf_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fichier_pdf** | **bytearray**| Fichier PDF à signer (sera traité puis retourné signé en base64) | 
 **raison** | **str**|  | [optional] 
 **localisation** | **str**|  | [optional] 
 **contact** | **str**|  | [optional] 
 **field_name** | **str**| Nom du champ de signature PDF | [optional] [default to &#39;FactPulseSignature&#39;]
 **use_pades_lt** | **bool**| Activer PAdES-B-LT (archivage long terme avec données de validation embarquées). NÉCESSITE un certificat avec accès OCSP/CRL. | [optional] [default to False]
 **use_timestamp** | **bool**| Activer l&#39;horodatage RFC 3161 avec FreeTSA (PAdES-B-T) | [optional] [default to True]

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
**200** | PDF signé avec succès |  -  |
**400** | Certificat invalide ou expiré |  -  |
**404** | Aucun certificat configuré pour ce client |  -  |
**401** | Non authentifié - Token JWT manquant ou invalide |  -  |
**503** | Service Django inaccessible |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signer_pdf_async_api_v1_traitement_signer_pdf_async_post**
> object signer_pdf_async_api_v1_traitement_signer_pdf_async_post(fichier_pdf, raison=raison, localisation=localisation, contact=contact, field_name=field_name, use_pades_lt=use_pades_lt, use_timestamp=use_timestamp)

Signer un PDF de manière asynchrone (Celery)

Signe un PDF uploadé de manière asynchrone via une tâche Celery.

    **Différence avec /signer-pdf** :
    - `/signer-pdf` : Signature synchrone (blocage jusqu'à la fin)
    - `/signer-pdf-async` : Signature asynchrone (retourne immédiatement un task_id)

    **Avantages de l'async** :
    - Pas de timeout pour les gros fichiers
    - Pas de blocage du worker FastAPI
    - Possibilité de suivre la progression via le task_id
    - Idéal pour les traitements par lot

    **Standards supportés** : PAdES-B-B, PAdES-B-T (horodatage), PAdES-B-LT (archivage long terme).

    **⚠️ Disclaimer légal** : Identique à /signer-pdf (voir documentation de cet endpoint).

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
    api_instance = factpulse.SignatureLectroniqueApi(api_client)
    fichier_pdf = None # bytearray | Fichier PDF à signer (traité de manière asynchrone)
    raison = 'raison_example' # str |  (optional)
    localisation = 'localisation_example' # str |  (optional)
    contact = 'contact_example' # str |  (optional)
    field_name = 'FactPulseSignature' # str | Nom du champ de signature PDF (optional) (default to 'FactPulseSignature')
    use_pades_lt = False # bool | Activer PAdES-B-LT (archivage long terme avec données de validation embarquées). NÉCESSITE un certificat avec accès OCSP/CRL. (optional) (default to False)
    use_timestamp = True # bool | Activer l'horodatage RFC 3161 avec FreeTSA (PAdES-B-T) (optional) (default to True)

    try:
        # Signer un PDF de manière asynchrone (Celery)
        api_response = api_instance.signer_pdf_async_api_v1_traitement_signer_pdf_async_post(fichier_pdf, raison=raison, localisation=localisation, contact=contact, field_name=field_name, use_pades_lt=use_pades_lt, use_timestamp=use_timestamp)
        print("The response of SignatureLectroniqueApi->signer_pdf_async_api_v1_traitement_signer_pdf_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignatureLectroniqueApi->signer_pdf_async_api_v1_traitement_signer_pdf_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fichier_pdf** | **bytearray**| Fichier PDF à signer (traité de manière asynchrone) | 
 **raison** | **str**|  | [optional] 
 **localisation** | **str**|  | [optional] 
 **contact** | **str**|  | [optional] 
 **field_name** | **str**| Nom du champ de signature PDF | [optional] [default to &#39;FactPulseSignature&#39;]
 **use_pades_lt** | **bool**| Activer PAdES-B-LT (archivage long terme avec données de validation embarquées). NÉCESSITE un certificat avec accès OCSP/CRL. | [optional] [default to False]
 **use_timestamp** | **bool**| Activer l&#39;horodatage RFC 3161 avec FreeTSA (PAdES-B-T) | [optional] [default to True]

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
**202** | Tâche de signature créée avec succès |  -  |
**400** | Paramètres invalides |  -  |
**401** | Non authentifié - Token JWT manquant ou invalide |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **valider_signature_pdf_endpoint_api_v1_traitement_valider_signature_pdf_post**
> object valider_signature_pdf_endpoint_api_v1_traitement_valider_signature_pdf_post(fichier_pdf)

Valider les signatures électroniques d'un PDF

Valide les signatures électroniques présentes dans un PDF uploadé.

    **Vérifications effectuées** :
    - Présence de signatures
    - Intégrité du document (non modifié depuis signature)
    - Validité des certificats
    - Chaîne de confiance (si disponible)
    - Présence d'horodatage (PAdES-B-T)
    - Données de validation (PAdES-B-LT)

    **Standards supportés** : PAdES-B-B, PAdES-B-T, PAdES-B-LT, ISO 32000-2.

    **⚠️ Note** : Cette validation est technique (intégrité cryptographique). La validité juridique
    dépend du niveau eIDAS du certificat (SES/AdES/QES) et du contexte d'utilisation.

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
    api_instance = factpulse.SignatureLectroniqueApi(api_client)
    fichier_pdf = None # bytearray | Fichier PDF à valider (sera analysé pour détecter et valider les signatures)

    try:
        # Valider les signatures électroniques d'un PDF
        api_response = api_instance.valider_signature_pdf_endpoint_api_v1_traitement_valider_signature_pdf_post(fichier_pdf)
        print("The response of SignatureLectroniqueApi->valider_signature_pdf_endpoint_api_v1_traitement_valider_signature_pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignatureLectroniqueApi->valider_signature_pdf_endpoint_api_v1_traitement_valider_signature_pdf_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fichier_pdf** | **bytearray**| Fichier PDF à valider (sera analysé pour détecter et valider les signatures) | 

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
**200** | Validation réussie |  -  |
**400** | Fichier invalide ou non lisible |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

