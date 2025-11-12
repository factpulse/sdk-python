# factpulse.ProcessingEndpointsUnifisApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**soumettre_facture_complete_api_v1_traitement_factures_soumettre_complete_post**](ProcessingEndpointsUnifisApi.md#soumettre_facture_complete_api_v1_traitement_factures_soumettre_complete_post) | **POST** /api/v1/traitement/factures/soumettre-complete | Soumettre une facture complète (génération + signature + soumission)
[**soumettre_facture_complete_async_api_v1_traitement_factures_soumettre_complete_async_post**](ProcessingEndpointsUnifisApi.md#soumettre_facture_complete_async_api_v1_traitement_factures_soumettre_complete_async_post) | **POST** /api/v1/traitement/factures/soumettre-complete-async | Soumettre une facture complète (asynchrone avec Celery)


# **soumettre_facture_complete_api_v1_traitement_factures_soumettre_complete_post**
> SoumettreFactureCompleteResponse soumettre_facture_complete_api_v1_traitement_factures_soumettre_complete_post(soumettre_facture_complete_request)

Soumettre une facture complète (génération + signature + soumission)

Endpoint unifié pour soumettre une facture complète vers différentes destinations.

    **Workflow automatisé :**
    1. **Auto-enrichissement** (optionnel) : récupère les données via APIs publiques et Chorus Pro/AFNOR
    2. **Génération PDF Factur-X** : crée un PDF/A-3 avec XML embarqué
    3. **Signature électronique** (optionnelle) : signe le PDF avec un certificat
    4. **Soumission** : envoie vers la destination choisie (Chorus Pro ou AFNOR PDP)

    **Destinations supportées :**
    - **Chorus Pro** : plateforme B2G française (factures vers secteur public)
    - **AFNOR PDP** : Plateformes de Dématérialisation Partenaires

    **Credentials de destination - 2 modes disponibles :**

    **Mode 1 - Récupération via JWT (recommandé) :**
    - Les credentials sont récupérés automatiquement via le `client_uid` du JWT
    - Ne pas fournir le champ `credentials` dans `destination`
    - Architecture 0-trust : aucun secret dans le payload
    - Exemple : `"destination": {"type": "chorus_pro"}`

    **Mode 2 - Credentials dans le payload :**
    - Fournir les credentials directement dans le payload
    - Utile pour tests ou intégrations tierces
    - Exemple : `"destination": {"type": "chorus_pro", "credentials": {...}}`


    **Signature électronique (optionnelle) - 2 modes disponibles :**

    **Mode 1 - Certificat stocké (recommandé) :**
    - Le certificat est récupéré automatiquement via le `client_uid` du JWT
    - Aucune clé à fournir dans le payload
    - Signature PAdES-B-LT avec horodatage (conforme eIDAS)
    - Exemple : `"signature": {"raison": "Conformité Factur-X"}`

    **Mode 2 - Clés dans le payload (pour tests) :**
    - Fournir `key_pem` et `cert_pem` directement
    - Format PEM accepté : brut ou base64
    - Utile pour tests ou cas spéciaux sans certificat stocké
    - Exemple : `"signature": {"key_pem": "-----BEGIN...", "cert_pem": "-----BEGIN..."}`

    Si `key_pem` et `cert_pem` sont fournis → Mode 2
    Sinon → Mode 1 (certificat récupéré via `client_uid`)

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.soumettre_facture_complete_request import SoumettreFactureCompleteRequest
from factpulse.models.soumettre_facture_complete_response import SoumettreFactureCompleteResponse
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
    api_instance = factpulse.ProcessingEndpointsUnifisApi(api_client)
    soumettre_facture_complete_request = factpulse.SoumettreFactureCompleteRequest() # SoumettreFactureCompleteRequest | 

    try:
        # Soumettre une facture complète (génération + signature + soumission)
        api_response = api_instance.soumettre_facture_complete_api_v1_traitement_factures_soumettre_complete_post(soumettre_facture_complete_request)
        print("The response of ProcessingEndpointsUnifisApi->soumettre_facture_complete_api_v1_traitement_factures_soumettre_complete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingEndpointsUnifisApi->soumettre_facture_complete_api_v1_traitement_factures_soumettre_complete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soumettre_facture_complete_request** | [**SoumettreFactureCompleteRequest**](SoumettreFactureCompleteRequest.md)|  | 

### Return type

[**SoumettreFactureCompleteResponse**](SoumettreFactureCompleteResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soumettre_facture_complete_async_api_v1_traitement_factures_soumettre_complete_async_post**
> ReponseTache soumettre_facture_complete_async_api_v1_traitement_factures_soumettre_complete_async_post(soumettre_facture_complete_request)

Soumettre une facture complète (asynchrone avec Celery)

Version asynchrone de l'endpoint `/factures/soumettre-complete` utilisant Celery pour le traitement en arrière-plan.

    **Workflow automatisé (identique à la version synchrone) :**
    1. **Auto-enrichissement** (optionnel) : récupère les données via APIs publiques et Chorus Pro/AFNOR
    2. **Génération PDF Factur-X** : crée un PDF/A-3 avec XML embarqué
    3. **Signature électronique** (optionnelle) : signe le PDF avec un certificat
    4. **Soumission** : envoie vers la destination choisie (Chorus Pro ou AFNOR PDP)

    **Destinations supportées :**
    - **Chorus Pro** : plateforme B2G française (factures vers secteur public)
    - **AFNOR PDP** : Plateformes de Dématérialisation Partenaires

    **Différences avec la version synchrone :**
    - ✅ **Non-bloquant** : Retourne immédiatement un `id_tache` (HTTP 202 Accepted)
    - ✅ **Traitement en arrière-plan** : La facture est traitée par un worker Celery
    - ✅ **Suivi d'avancement** : Utilisez `/taches/{id_tache}/statut` pour suivre le statut
    - ✅ **Idéal pour gros volumes** : Permet de traiter de nombreuses factures en parallèle

    **Comment utiliser :**
    1. **Soumission** : Appelez cet endpoint avec vos données de facture
    2. **Retour immédiat** : Vous recevez un `id_tache` (ex: "abc123-def456")
    3. **Suivi** : Appelez `/taches/{id_tache}/statut` pour vérifier l'avancement
    4. **Résultat** : Quand `statut = "SUCCESS"`, le champ `resultat` contient la réponse complète

    **Credentials et signature** : Mêmes modes que la version synchrone (JWT ou payload).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.reponse_tache import ReponseTache
from factpulse.models.soumettre_facture_complete_request import SoumettreFactureCompleteRequest
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
    api_instance = factpulse.ProcessingEndpointsUnifisApi(api_client)
    soumettre_facture_complete_request = factpulse.SoumettreFactureCompleteRequest() # SoumettreFactureCompleteRequest | 

    try:
        # Soumettre une facture complète (asynchrone avec Celery)
        api_response = api_instance.soumettre_facture_complete_async_api_v1_traitement_factures_soumettre_complete_async_post(soumettre_facture_complete_request)
        print("The response of ProcessingEndpointsUnifisApi->soumettre_facture_complete_async_api_v1_traitement_factures_soumettre_complete_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingEndpointsUnifisApi->soumettre_facture_complete_async_api_v1_traitement_factures_soumettre_complete_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soumettre_facture_complete_request** | [**SoumettreFactureCompleteRequest**](SoumettreFactureCompleteRequest.md)|  | 

### Return type

[**ReponseTache**](ReponseTache.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

