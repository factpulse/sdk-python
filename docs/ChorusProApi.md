# factpulse.ChorusProApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ajouter_fichier_api_v1_chorus_pro_transverses_ajouter_fichier_post**](ChorusProApi.md#ajouter_fichier_api_v1_chorus_pro_transverses_ajouter_fichier_post) | **POST** /api/v1/chorus-pro/transverses/ajouter-fichier | Ajouter une pièce jointe
[**completer_facture_api_v1_chorus_pro_factures_completer_post**](ChorusProApi.md#completer_facture_api_v1_chorus_pro_factures_completer_post) | **POST** /api/v1/chorus-pro/factures/completer | Compléter une facture suspendue (Fournisseur)
[**consulter_facture_api_v1_chorus_pro_factures_consulter_post**](ChorusProApi.md#consulter_facture_api_v1_chorus_pro_factures_consulter_post) | **POST** /api/v1/chorus-pro/factures/consulter | Consulter le statut d&#39;une facture
[**consulter_structure_api_v1_chorus_pro_structures_consulter_post**](ChorusProApi.md#consulter_structure_api_v1_chorus_pro_structures_consulter_post) | **POST** /api/v1/chorus-pro/structures/consulter | Consulter les détails d&#39;une structure
[**lister_services_structure_api_v1_chorus_pro_structures_id_structure_cpp_services_get**](ChorusProApi.md#lister_services_structure_api_v1_chorus_pro_structures_id_structure_cpp_services_get) | **GET** /api/v1/chorus-pro/structures/{id_structure_cpp}/services | Lister les services d&#39;une structure
[**obtenir_id_chorus_pro_depuis_siret_api_v1_chorus_pro_structures_obtenir_id_depuis_siret_post**](ChorusProApi.md#obtenir_id_chorus_pro_depuis_siret_api_v1_chorus_pro_structures_obtenir_id_depuis_siret_post) | **POST** /api/v1/chorus-pro/structures/obtenir-id-depuis-siret | Utilitaire : Obtenir l&#39;ID Chorus Pro depuis un SIRET
[**rechercher_factures_destinataire_api_v1_chorus_pro_factures_rechercher_destinataire_post**](ChorusProApi.md#rechercher_factures_destinataire_api_v1_chorus_pro_factures_rechercher_destinataire_post) | **POST** /api/v1/chorus-pro/factures/rechercher-destinataire | Rechercher factures reçues (Destinataire)
[**rechercher_factures_fournisseur_api_v1_chorus_pro_factures_rechercher_fournisseur_post**](ChorusProApi.md#rechercher_factures_fournisseur_api_v1_chorus_pro_factures_rechercher_fournisseur_post) | **POST** /api/v1/chorus-pro/factures/rechercher-fournisseur | Rechercher factures émises (Fournisseur)
[**rechercher_structures_api_v1_chorus_pro_structures_rechercher_post**](ChorusProApi.md#rechercher_structures_api_v1_chorus_pro_structures_rechercher_post) | **POST** /api/v1/chorus-pro/structures/rechercher | Rechercher des structures Chorus Pro
[**recycler_facture_api_v1_chorus_pro_factures_recycler_post**](ChorusProApi.md#recycler_facture_api_v1_chorus_pro_factures_recycler_post) | **POST** /api/v1/chorus-pro/factures/recycler | Recycler une facture (Fournisseur)
[**soumettre_facture_api_v1_chorus_pro_factures_soumettre_post**](ChorusProApi.md#soumettre_facture_api_v1_chorus_pro_factures_soumettre_post) | **POST** /api/v1/chorus-pro/factures/soumettre | Soumettre une facture à Chorus Pro
[**telecharger_groupe_factures_api_v1_chorus_pro_factures_telecharger_groupe_post**](ChorusProApi.md#telecharger_groupe_factures_api_v1_chorus_pro_factures_telecharger_groupe_post) | **POST** /api/v1/chorus-pro/factures/telecharger-groupe | Télécharger un groupe de factures
[**traiter_facture_recue_api_v1_chorus_pro_factures_traiter_facture_recue_post**](ChorusProApi.md#traiter_facture_recue_api_v1_chorus_pro_factures_traiter_facture_recue_post) | **POST** /api/v1/chorus-pro/factures/traiter-facture-recue | Traiter une facture reçue (Destinataire)
[**valideur_consulter_facture_api_v1_chorus_pro_factures_valideur_consulter_post**](ChorusProApi.md#valideur_consulter_facture_api_v1_chorus_pro_factures_valideur_consulter_post) | **POST** /api/v1/chorus-pro/factures/valideur/consulter | Consulter une facture (Valideur)
[**valideur_rechercher_factures_api_v1_chorus_pro_factures_valideur_rechercher_post**](ChorusProApi.md#valideur_rechercher_factures_api_v1_chorus_pro_factures_valideur_rechercher_post) | **POST** /api/v1/chorus-pro/factures/valideur/rechercher | Rechercher factures à valider (Valideur)
[**valideur_traiter_facture_api_v1_chorus_pro_factures_valideur_traiter_post**](ChorusProApi.md#valideur_traiter_facture_api_v1_chorus_pro_factures_valideur_traiter_post) | **POST** /api/v1/chorus-pro/factures/valideur/traiter | Valider ou refuser une facture (Valideur)


# **ajouter_fichier_api_v1_chorus_pro_transverses_ajouter_fichier_post**
> object ajouter_fichier_api_v1_chorus_pro_transverses_ajouter_fichier_post(body_ajouter_fichier_api_v1_chorus_pro_transverses_ajouter_fichier_post)

Ajouter une pièce jointe

Ajoute une pièce jointe au compte utilisateur courant.

    **Taille max** : 10 Mo par fichier

    **Payload exemple** :
    ```json
    {
      "pieceJointeFichier": "JVBERi0xLjQKJeLjz9MKNSAwIG9iago8P...",
      "pieceJointeNom": "bon_commande.pdf",
      "pieceJointeTypeMime": "application/pdf",
      "pieceJointeExtension": "PDF"
    }
    ```

    **Retour** : L'ID de la pièce jointe (`pieceJointeIdFichier`) à utiliser ensuite dans `/factures/completer`.

    **Extensions acceptées** : PDF, JPG, PNG, ZIP, XML, etc.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_ajouter_fichier_api_v1_chorus_pro_transverses_ajouter_fichier_post import BodyAjouterFichierApiV1ChorusProTransversesAjouterFichierPost
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
    api_instance = factpulse.ChorusProApi(api_client)
    body_ajouter_fichier_api_v1_chorus_pro_transverses_ajouter_fichier_post = factpulse.BodyAjouterFichierApiV1ChorusProTransversesAjouterFichierPost() # BodyAjouterFichierApiV1ChorusProTransversesAjouterFichierPost | 

    try:
        # Ajouter une pièce jointe
        api_response = api_instance.ajouter_fichier_api_v1_chorus_pro_transverses_ajouter_fichier_post(body_ajouter_fichier_api_v1_chorus_pro_transverses_ajouter_fichier_post)
        print("The response of ChorusProApi->ajouter_fichier_api_v1_chorus_pro_transverses_ajouter_fichier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->ajouter_fichier_api_v1_chorus_pro_transverses_ajouter_fichier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_ajouter_fichier_api_v1_chorus_pro_transverses_ajouter_fichier_post** | [**BodyAjouterFichierApiV1ChorusProTransversesAjouterFichierPost**](BodyAjouterFichierApiV1ChorusProTransversesAjouterFichierPost.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **completer_facture_api_v1_chorus_pro_factures_completer_post**
> object completer_facture_api_v1_chorus_pro_factures_completer_post(body_completer_facture_api_v1_chorus_pro_factures_completer_post)

Compléter une facture suspendue (Fournisseur)

Complète une facture au statut SUSPENDUE en ajoutant des pièces jointes ou un commentaire.

    **Statut requis** : SUSPENDUE

    **Actions possibles** :
    - Ajouter des pièces jointes (justificatifs, bons de commande, etc.)
    - Modifier le commentaire

    **Payload exemple** :
    ```json
    {
      "identifiantFactureCPP": 12345,
      "commentaire": "Voici les justificatifs demandés",
      "listePiecesJointes": [
        {
          "pieceJointeIdFichier": 98765,
          "pieceJointeNom": "bon_commande.pdf"
        }
      ]
    }
    ```

    **Note** : Les pièces jointes doivent d'abord être uploadées via `/transverses/ajouter-fichier`.

    **Après complétion** : La facture repasse au statut MISE_A_DISPOSITION.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_completer_facture_api_v1_chorus_pro_factures_completer_post import BodyCompleterFactureApiV1ChorusProFacturesCompleterPost
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
    api_instance = factpulse.ChorusProApi(api_client)
    body_completer_facture_api_v1_chorus_pro_factures_completer_post = factpulse.BodyCompleterFactureApiV1ChorusProFacturesCompleterPost() # BodyCompleterFactureApiV1ChorusProFacturesCompleterPost | 

    try:
        # Compléter une facture suspendue (Fournisseur)
        api_response = api_instance.completer_facture_api_v1_chorus_pro_factures_completer_post(body_completer_facture_api_v1_chorus_pro_factures_completer_post)
        print("The response of ChorusProApi->completer_facture_api_v1_chorus_pro_factures_completer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->completer_facture_api_v1_chorus_pro_factures_completer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_completer_facture_api_v1_chorus_pro_factures_completer_post** | [**BodyCompleterFactureApiV1ChorusProFacturesCompleterPost**](BodyCompleterFactureApiV1ChorusProFacturesCompleterPost.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consulter_facture_api_v1_chorus_pro_factures_consulter_post**
> ConsulterFactureResponse consulter_facture_api_v1_chorus_pro_factures_consulter_post(consulter_facture_request)

Consulter le statut d'une facture

Récupère les informations et le statut actuel d'une facture soumise à Chorus Pro.

    **Retour** :
    - Numéro et date de facture
    - Montant TTC
    - **Statut courant** : SOUMISE, VALIDEE, REJETEE, SUSPENDUE, MANDATEE, MISE_EN_PAIEMENT, etc.
    - Structure destinataire

    **Cas d'usage** :
    - Suivre l'évolution du traitement d'une facture
    - Vérifier si une facture a été validée ou rejetée
    - Obtenir la date de mise en paiement

    **Polling** : Appelez cet endpoint régulièrement pour suivre l'évolution du statut.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.consulter_facture_request import ConsulterFactureRequest
from factpulse.models.consulter_facture_response import ConsulterFactureResponse
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
    api_instance = factpulse.ChorusProApi(api_client)
    consulter_facture_request = factpulse.ConsulterFactureRequest() # ConsulterFactureRequest | 

    try:
        # Consulter le statut d'une facture
        api_response = api_instance.consulter_facture_api_v1_chorus_pro_factures_consulter_post(consulter_facture_request)
        print("The response of ChorusProApi->consulter_facture_api_v1_chorus_pro_factures_consulter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->consulter_facture_api_v1_chorus_pro_factures_consulter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consulter_facture_request** | [**ConsulterFactureRequest**](ConsulterFactureRequest.md)|  | 

### Return type

[**ConsulterFactureResponse**](ConsulterFactureResponse.md)

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

# **consulter_structure_api_v1_chorus_pro_structures_consulter_post**
> ConsulterStructureResponse consulter_structure_api_v1_chorus_pro_structures_consulter_post(consulter_structure_request)

Consulter les détails d'une structure

Récupère les informations détaillées d'une structure Chorus Pro.


    **Retour** :
    - Raison sociale
    - Numéro de TVA intracommunautaire
    - Email de contact
    - **Paramètres obligatoires** : Indique si le code service et/ou numéro d'engagement sont requis pour soumettre une facture

    **Étape typique** : Appelée après `rechercher-structures` pour savoir quels champs sont obligatoires avant de soumettre une facture.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.consulter_structure_request import ConsulterStructureRequest
from factpulse.models.consulter_structure_response import ConsulterStructureResponse
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
    api_instance = factpulse.ChorusProApi(api_client)
    consulter_structure_request = factpulse.ConsulterStructureRequest() # ConsulterStructureRequest | 

    try:
        # Consulter les détails d'une structure
        api_response = api_instance.consulter_structure_api_v1_chorus_pro_structures_consulter_post(consulter_structure_request)
        print("The response of ChorusProApi->consulter_structure_api_v1_chorus_pro_structures_consulter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->consulter_structure_api_v1_chorus_pro_structures_consulter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consulter_structure_request** | [**ConsulterStructureRequest**](ConsulterStructureRequest.md)|  | 

### Return type

[**ConsulterStructureResponse**](ConsulterStructureResponse.md)

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

# **lister_services_structure_api_v1_chorus_pro_structures_id_structure_cpp_services_get**
> RechercherServicesResponse lister_services_structure_api_v1_chorus_pro_structures_id_structure_cpp_services_get(id_structure_cpp, body_lister_services_structure_api_v1_chorus_pro_structures_id_structure_cpp_services_get)

Lister les services d'une structure

Récupère la liste des services actifs d'une structure publique.

    **Cas d'usage** :
    - Lister les services disponibles pour une administration
    - Vérifier qu'un code service existe avant de soumettre une facture

    **Retour** :
    - Liste des services avec leur code, libellé et statut (actif/inactif)

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_lister_services_structure_api_v1_chorus_pro_structures_id_structure_cpp_services_get import BodyListerServicesStructureApiV1ChorusProStructuresIdStructureCppServicesGet
from factpulse.models.rechercher_services_response import RechercherServicesResponse
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
    api_instance = factpulse.ChorusProApi(api_client)
    id_structure_cpp = 56 # int | 
    body_lister_services_structure_api_v1_chorus_pro_structures_id_structure_cpp_services_get = factpulse.BodyListerServicesStructureApiV1ChorusProStructuresIdStructureCppServicesGet() # BodyListerServicesStructureApiV1ChorusProStructuresIdStructureCppServicesGet | 

    try:
        # Lister les services d'une structure
        api_response = api_instance.lister_services_structure_api_v1_chorus_pro_structures_id_structure_cpp_services_get(id_structure_cpp, body_lister_services_structure_api_v1_chorus_pro_structures_id_structure_cpp_services_get)
        print("The response of ChorusProApi->lister_services_structure_api_v1_chorus_pro_structures_id_structure_cpp_services_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->lister_services_structure_api_v1_chorus_pro_structures_id_structure_cpp_services_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_structure_cpp** | **int**|  | 
 **body_lister_services_structure_api_v1_chorus_pro_structures_id_structure_cpp_services_get** | [**BodyListerServicesStructureApiV1ChorusProStructuresIdStructureCppServicesGet**](BodyListerServicesStructureApiV1ChorusProStructuresIdStructureCppServicesGet.md)|  | 

### Return type

[**RechercherServicesResponse**](RechercherServicesResponse.md)

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

# **obtenir_id_chorus_pro_depuis_siret_api_v1_chorus_pro_structures_obtenir_id_depuis_siret_post**
> ObtenirIdChorusProResponse obtenir_id_chorus_pro_depuis_siret_api_v1_chorus_pro_structures_obtenir_id_depuis_siret_post(obtenir_id_chorus_pro_request)

Utilitaire : Obtenir l'ID Chorus Pro depuis un SIRET

**Utilitaire pratique** pour obtenir l'ID Chorus Pro d'une structure à partir de son SIRET.


    Cette fonction wrapper combine :
    1. Recherche de la structure par SIRET
    2. Extraction de l'`id_structure_cpp` si une seule structure est trouvée

    **Retour** :
    - `id_structure_cpp` : ID Chorus Pro (0 si non trouvé ou si plusieurs résultats)
    - `designation_structure` : Nom de la structure (si trouvée)
    - `message` : Message explicatif

    **Cas d'usage** :
    - Raccourci pour obtenir directement l'ID Chorus Pro avant de soumettre une facture
    - Alternative simplifiée à `rechercher-structures` + extraction manuelle de l'ID

    **Note** : Si plusieurs structures correspondent au SIRET (rare), retourne 0 et un message d'erreur.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.obtenir_id_chorus_pro_request import ObtenirIdChorusProRequest
from factpulse.models.obtenir_id_chorus_pro_response import ObtenirIdChorusProResponse
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
    api_instance = factpulse.ChorusProApi(api_client)
    obtenir_id_chorus_pro_request = factpulse.ObtenirIdChorusProRequest() # ObtenirIdChorusProRequest | 

    try:
        # Utilitaire : Obtenir l'ID Chorus Pro depuis un SIRET
        api_response = api_instance.obtenir_id_chorus_pro_depuis_siret_api_v1_chorus_pro_structures_obtenir_id_depuis_siret_post(obtenir_id_chorus_pro_request)
        print("The response of ChorusProApi->obtenir_id_chorus_pro_depuis_siret_api_v1_chorus_pro_structures_obtenir_id_depuis_siret_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->obtenir_id_chorus_pro_depuis_siret_api_v1_chorus_pro_structures_obtenir_id_depuis_siret_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obtenir_id_chorus_pro_request** | [**ObtenirIdChorusProRequest**](ObtenirIdChorusProRequest.md)|  | 

### Return type

[**ObtenirIdChorusProResponse**](ObtenirIdChorusProResponse.md)

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

# **rechercher_factures_destinataire_api_v1_chorus_pro_factures_rechercher_destinataire_post**
> object rechercher_factures_destinataire_api_v1_chorus_pro_factures_rechercher_destinataire_post(body_rechercher_factures_destinataire_api_v1_chorus_pro_factures_rechercher_destinataire_post)

Rechercher factures reçues (Destinataire)

Recherche les factures reçues par le destinataire connecté.

    **Filtres** :
    - Téléchargée / non téléchargée
    - Dates de réception
    - Statut (MISE_A_DISPOSITION, SUSPENDUE, etc.)
    - Fournisseur

    **Indicateur utile** : `factureTelechargeeParDestinataire` permet de savoir si la facture a déjà été téléchargée.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_rechercher_factures_destinataire_api_v1_chorus_pro_factures_rechercher_destinataire_post import BodyRechercherFacturesDestinataireApiV1ChorusProFacturesRechercherDestinatairePost
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
    api_instance = factpulse.ChorusProApi(api_client)
    body_rechercher_factures_destinataire_api_v1_chorus_pro_factures_rechercher_destinataire_post = factpulse.BodyRechercherFacturesDestinataireApiV1ChorusProFacturesRechercherDestinatairePost() # BodyRechercherFacturesDestinataireApiV1ChorusProFacturesRechercherDestinatairePost | 

    try:
        # Rechercher factures reçues (Destinataire)
        api_response = api_instance.rechercher_factures_destinataire_api_v1_chorus_pro_factures_rechercher_destinataire_post(body_rechercher_factures_destinataire_api_v1_chorus_pro_factures_rechercher_destinataire_post)
        print("The response of ChorusProApi->rechercher_factures_destinataire_api_v1_chorus_pro_factures_rechercher_destinataire_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->rechercher_factures_destinataire_api_v1_chorus_pro_factures_rechercher_destinataire_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_rechercher_factures_destinataire_api_v1_chorus_pro_factures_rechercher_destinataire_post** | [**BodyRechercherFacturesDestinataireApiV1ChorusProFacturesRechercherDestinatairePost**](BodyRechercherFacturesDestinataireApiV1ChorusProFacturesRechercherDestinatairePost.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rechercher_factures_fournisseur_api_v1_chorus_pro_factures_rechercher_fournisseur_post**
> object rechercher_factures_fournisseur_api_v1_chorus_pro_factures_rechercher_fournisseur_post(body_rechercher_factures_fournisseur_api_v1_chorus_pro_factures_rechercher_fournisseur_post)

Rechercher factures émises (Fournisseur)

Recherche les factures émises par le fournisseur connecté.

    **Filtres disponibles** :
    - Numéro de facture
    - Dates (début/fin)
    - Statut
    - Structure destinataire
    - Montant

    **Cas d'usage** :
    - Suivi des factures émises
    - Vérification des statuts
    - Export pour comptabilité

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_rechercher_factures_fournisseur_api_v1_chorus_pro_factures_rechercher_fournisseur_post import BodyRechercherFacturesFournisseurApiV1ChorusProFacturesRechercherFournisseurPost
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
    api_instance = factpulse.ChorusProApi(api_client)
    body_rechercher_factures_fournisseur_api_v1_chorus_pro_factures_rechercher_fournisseur_post = factpulse.BodyRechercherFacturesFournisseurApiV1ChorusProFacturesRechercherFournisseurPost() # BodyRechercherFacturesFournisseurApiV1ChorusProFacturesRechercherFournisseurPost | 

    try:
        # Rechercher factures émises (Fournisseur)
        api_response = api_instance.rechercher_factures_fournisseur_api_v1_chorus_pro_factures_rechercher_fournisseur_post(body_rechercher_factures_fournisseur_api_v1_chorus_pro_factures_rechercher_fournisseur_post)
        print("The response of ChorusProApi->rechercher_factures_fournisseur_api_v1_chorus_pro_factures_rechercher_fournisseur_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->rechercher_factures_fournisseur_api_v1_chorus_pro_factures_rechercher_fournisseur_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_rechercher_factures_fournisseur_api_v1_chorus_pro_factures_rechercher_fournisseur_post** | [**BodyRechercherFacturesFournisseurApiV1ChorusProFacturesRechercherFournisseurPost**](BodyRechercherFacturesFournisseurApiV1ChorusProFacturesRechercherFournisseurPost.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rechercher_structures_api_v1_chorus_pro_structures_rechercher_post**
> RechercherStructureResponse rechercher_structures_api_v1_chorus_pro_structures_rechercher_post(rechercher_structure_request)

Rechercher des structures Chorus Pro

Recherche des structures (entreprises, administrations) enregistrées sur Chorus Pro.

    **Cas d'usage** :
    - Trouver l'ID Chorus Pro d'une structure à partir de son SIRET
    - Vérifier si une structure est enregistrée sur Chorus Pro
    - Lister les structures correspondant à des critères

    **Filtres disponibles** :
    - Identifiant (SIRET, SIREN, etc.)
    - Raison sociale
    - Type d'identifiant
    - Structures privées uniquement

    **Étape typique** : Appelée avant `soumettre-facture` pour obtenir l'`id_structure_cpp` du destinataire.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.rechercher_structure_request import RechercherStructureRequest
from factpulse.models.rechercher_structure_response import RechercherStructureResponse
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
    api_instance = factpulse.ChorusProApi(api_client)
    rechercher_structure_request = factpulse.RechercherStructureRequest() # RechercherStructureRequest | 

    try:
        # Rechercher des structures Chorus Pro
        api_response = api_instance.rechercher_structures_api_v1_chorus_pro_structures_rechercher_post(rechercher_structure_request)
        print("The response of ChorusProApi->rechercher_structures_api_v1_chorus_pro_structures_rechercher_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->rechercher_structures_api_v1_chorus_pro_structures_rechercher_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rechercher_structure_request** | [**RechercherStructureRequest**](RechercherStructureRequest.md)|  | 

### Return type

[**RechercherStructureResponse**](RechercherStructureResponse.md)

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

# **recycler_facture_api_v1_chorus_pro_factures_recycler_post**
> object recycler_facture_api_v1_chorus_pro_factures_recycler_post(body_recycler_facture_api_v1_chorus_pro_factures_recycler_post)

Recycler une facture (Fournisseur)

Recycle une facture au statut A_RECYCLER en modifiant les données d'acheminement.

    **Statut requis** : A_RECYCLER

    **Champs modifiables** :
    - Destinataire (`idStructureCPP`)
    - Code service
    - Numéro d'engagement

    **Cas d'usage** :
    - Erreur de destinataire
    - Changement de service facturation
    - Mise à jour du numéro d'engagement

    **Payload exemple** :
    ```json
    {
      "identifiantFactureCPP": 12345,
      "idStructureCPP": 67890,
      "codeService": "SERVICE_01",
      "numeroEngagement": "ENG2024001"
    }
    ```

    **Note** : La facture conserve son numéro et ses montants, seuls les champs d'acheminement changent.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_recycler_facture_api_v1_chorus_pro_factures_recycler_post import BodyRecyclerFactureApiV1ChorusProFacturesRecyclerPost
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
    api_instance = factpulse.ChorusProApi(api_client)
    body_recycler_facture_api_v1_chorus_pro_factures_recycler_post = factpulse.BodyRecyclerFactureApiV1ChorusProFacturesRecyclerPost() # BodyRecyclerFactureApiV1ChorusProFacturesRecyclerPost | 

    try:
        # Recycler une facture (Fournisseur)
        api_response = api_instance.recycler_facture_api_v1_chorus_pro_factures_recycler_post(body_recycler_facture_api_v1_chorus_pro_factures_recycler_post)
        print("The response of ChorusProApi->recycler_facture_api_v1_chorus_pro_factures_recycler_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->recycler_facture_api_v1_chorus_pro_factures_recycler_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_recycler_facture_api_v1_chorus_pro_factures_recycler_post** | [**BodyRecyclerFactureApiV1ChorusProFacturesRecyclerPost**](BodyRecyclerFactureApiV1ChorusProFacturesRecyclerPost.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soumettre_facture_api_v1_chorus_pro_factures_soumettre_post**
> SoumettreFactureResponse soumettre_facture_api_v1_chorus_pro_factures_soumettre_post(soumettre_facture_request)

Soumettre une facture à Chorus Pro

Soumet une facture électronique à une structure publique via Chorus Pro.


    **📋 Workflow complet** :
    1. **Uploader le PDF Factur-X** via `/transverses/ajouter-fichier` → récupérer `pieceJointeId`
    2. **Obtenir l'ID structure** via `/structures/rechercher` ou `/structures/obtenir-id-depuis-siret`
    3. **Vérifier les paramètres obligatoires** via `/structures/consulter`
    4. **Soumettre la facture** avec le `piece_jointe_principale_id` obtenu à l'étape 1

    **Pré-requis** :
    1. Avoir l'`id_structure_cpp` du destinataire (via `/structures/rechercher`)
    2. Connaître les paramètres obligatoires (via `/structures/consulter`) :
       - Code service si `code_service_doit_etre_renseigne=true`
       - Numéro d'engagement si `numero_ej_doit_etre_renseigne=true`
    3. Avoir uploadé le PDF Factur-X (via `/transverses/ajouter-fichier`)

    **Format attendu** :
    - `piece_jointe_principale_id` : ID retourné par `/transverses/ajouter-fichier`
    - Montants : Chaînes de caractères avec 2 décimales (ex: "1250.50")
    - Dates : Format ISO 8601 (YYYY-MM-DD)

    **Retour** :
    - `identifiant_facture_cpp` : ID Chorus Pro de la facture créée
    - `numero_flux_depot` : Numéro de suivi du dépôt

    **Statuts possibles après soumission** :
    - SOUMISE : En attente de validation
    - VALIDEE : Validée par le destinataire
    - REJETEE : Rejetée (erreur de données ou refus métier)
    - SUSPENDUE : En attente d'informations complémentaires

    **Note** : Utilisez `/factures/consulter` pour suivre l'évolution du statut.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.soumettre_facture_request import SoumettreFactureRequest
from factpulse.models.soumettre_facture_response import SoumettreFactureResponse
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
    api_instance = factpulse.ChorusProApi(api_client)
    soumettre_facture_request = factpulse.SoumettreFactureRequest() # SoumettreFactureRequest | 

    try:
        # Soumettre une facture à Chorus Pro
        api_response = api_instance.soumettre_facture_api_v1_chorus_pro_factures_soumettre_post(soumettre_facture_request)
        print("The response of ChorusProApi->soumettre_facture_api_v1_chorus_pro_factures_soumettre_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->soumettre_facture_api_v1_chorus_pro_factures_soumettre_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soumettre_facture_request** | [**SoumettreFactureRequest**](SoumettreFactureRequest.md)|  | 

### Return type

[**SoumettreFactureResponse**](SoumettreFactureResponse.md)

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

# **telecharger_groupe_factures_api_v1_chorus_pro_factures_telecharger_groupe_post**
> object telecharger_groupe_factures_api_v1_chorus_pro_factures_telecharger_groupe_post(body_telecharger_groupe_factures_api_v1_chorus_pro_factures_telecharger_groupe_post)

Télécharger un groupe de factures

Télécharge une ou plusieurs factures (max 10 recommandé) avec leurs pièces jointes.

    **Formats disponibles** :
    - PDF : Fichier PDF uniquement
    - XML : Fichier XML uniquement
    - ZIP : Archive contenant PDF + XML + pièces jointes

    **Taille maximale** : 120 Mo par téléchargement

    **Payload exemple** :
    ```json
    {
      "listeIdentifiantsFactureCPP": [12345, 12346],
      "inclurePiecesJointes": true,
      "formatFichier": "ZIP"
    }
    ```

    **Retour** : Le fichier est encodé en base64 dans le champ `fichierBase64`.

    **Note** : Le flag `factureTelechargeeParDestinataire` est mis à jour automatiquement.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_telecharger_groupe_factures_api_v1_chorus_pro_factures_telecharger_groupe_post import BodyTelechargerGroupeFacturesApiV1ChorusProFacturesTelechargerGroupePost
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
    api_instance = factpulse.ChorusProApi(api_client)
    body_telecharger_groupe_factures_api_v1_chorus_pro_factures_telecharger_groupe_post = factpulse.BodyTelechargerGroupeFacturesApiV1ChorusProFacturesTelechargerGroupePost() # BodyTelechargerGroupeFacturesApiV1ChorusProFacturesTelechargerGroupePost | 

    try:
        # Télécharger un groupe de factures
        api_response = api_instance.telecharger_groupe_factures_api_v1_chorus_pro_factures_telecharger_groupe_post(body_telecharger_groupe_factures_api_v1_chorus_pro_factures_telecharger_groupe_post)
        print("The response of ChorusProApi->telecharger_groupe_factures_api_v1_chorus_pro_factures_telecharger_groupe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->telecharger_groupe_factures_api_v1_chorus_pro_factures_telecharger_groupe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_telecharger_groupe_factures_api_v1_chorus_pro_factures_telecharger_groupe_post** | [**BodyTelechargerGroupeFacturesApiV1ChorusProFacturesTelechargerGroupePost**](BodyTelechargerGroupeFacturesApiV1ChorusProFacturesTelechargerGroupePost.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **traiter_facture_recue_api_v1_chorus_pro_factures_traiter_facture_recue_post**
> object traiter_facture_recue_api_v1_chorus_pro_factures_traiter_facture_recue_post(body_traiter_facture_recue_api_v1_chorus_pro_factures_traiter_facture_recue_post)

Traiter une facture reçue (Destinataire)

Change le statut d'une facture reçue.

    **Statuts possibles** :
    - MISE_A_DISPOSITION : Facture acceptée
    - SUSPENDUE : En attente d'informations complémentaires (motif obligatoire)
    - REJETEE : Facture refusée (motif obligatoire)
    - MANDATEE : Facture mandatée
    - MISE_EN_PAIEMENT : Facture en cours de paiement
    - COMPTABILISEE : Facture comptabilisée
    - MISE_A_DISPOSITION_COMPTABLE : Mise à disposition comptable
    - A_RECYCLER : À recycler
    - COMPLETEE : Complétée
    - SERVICE-FAIT : Service fait
    - PRISE_EN_COMPTE_DESTINATAIRE : Prise en compte
    - TRANSMISE_MOA : Transmise à la MOA

    **Payload exemple** :
    ```json
    {
      "identifiantFactureCPP": 12345,
      "nouveauStatut": "REJETEE",
      "motifRejet": "Facture en double",
      "commentaire": "Facture déjà reçue sous la référence ABC123"
    }
    ```

    **Règles** :
    - Un motif est **obligatoire** pour SUSPENDUE et REJETEE
    - Seuls certains statuts sont autorisés selon le statut actuel de la facture

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_traiter_facture_recue_api_v1_chorus_pro_factures_traiter_facture_recue_post import BodyTraiterFactureRecueApiV1ChorusProFacturesTraiterFactureRecuePost
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
    api_instance = factpulse.ChorusProApi(api_client)
    body_traiter_facture_recue_api_v1_chorus_pro_factures_traiter_facture_recue_post = factpulse.BodyTraiterFactureRecueApiV1ChorusProFacturesTraiterFactureRecuePost() # BodyTraiterFactureRecueApiV1ChorusProFacturesTraiterFactureRecuePost | 

    try:
        # Traiter une facture reçue (Destinataire)
        api_response = api_instance.traiter_facture_recue_api_v1_chorus_pro_factures_traiter_facture_recue_post(body_traiter_facture_recue_api_v1_chorus_pro_factures_traiter_facture_recue_post)
        print("The response of ChorusProApi->traiter_facture_recue_api_v1_chorus_pro_factures_traiter_facture_recue_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->traiter_facture_recue_api_v1_chorus_pro_factures_traiter_facture_recue_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_traiter_facture_recue_api_v1_chorus_pro_factures_traiter_facture_recue_post** | [**BodyTraiterFactureRecueApiV1ChorusProFacturesTraiterFactureRecuePost**](BodyTraiterFactureRecueApiV1ChorusProFacturesTraiterFactureRecuePost.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **valideur_consulter_facture_api_v1_chorus_pro_factures_valideur_consulter_post**
> object valideur_consulter_facture_api_v1_chorus_pro_factures_valideur_consulter_post(body_valideur_consulter_facture_api_v1_chorus_pro_factures_valideur_consulter_post)

Consulter une facture (Valideur)

Consulte facture (valideur).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_valideur_consulter_facture_api_v1_chorus_pro_factures_valideur_consulter_post import BodyValideurConsulterFactureApiV1ChorusProFacturesValideurConsulterPost
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
    api_instance = factpulse.ChorusProApi(api_client)
    body_valideur_consulter_facture_api_v1_chorus_pro_factures_valideur_consulter_post = factpulse.BodyValideurConsulterFactureApiV1ChorusProFacturesValideurConsulterPost() # BodyValideurConsulterFactureApiV1ChorusProFacturesValideurConsulterPost | 

    try:
        # Consulter une facture (Valideur)
        api_response = api_instance.valideur_consulter_facture_api_v1_chorus_pro_factures_valideur_consulter_post(body_valideur_consulter_facture_api_v1_chorus_pro_factures_valideur_consulter_post)
        print("The response of ChorusProApi->valideur_consulter_facture_api_v1_chorus_pro_factures_valideur_consulter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->valideur_consulter_facture_api_v1_chorus_pro_factures_valideur_consulter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_valideur_consulter_facture_api_v1_chorus_pro_factures_valideur_consulter_post** | [**BodyValideurConsulterFactureApiV1ChorusProFacturesValideurConsulterPost**](BodyValideurConsulterFactureApiV1ChorusProFacturesValideurConsulterPost.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **valideur_rechercher_factures_api_v1_chorus_pro_factures_valideur_rechercher_post**
> object valideur_rechercher_factures_api_v1_chorus_pro_factures_valideur_rechercher_post(body_valideur_rechercher_factures_api_v1_chorus_pro_factures_valideur_rechercher_post)

Rechercher factures à valider (Valideur)

Recherche les factures en attente de validation par le valideur connecté.

    **Rôle** : Valideur dans le circuit de validation interne.

    **Filtres** : Dates, structure, service, etc.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_valideur_rechercher_factures_api_v1_chorus_pro_factures_valideur_rechercher_post import BodyValideurRechercherFacturesApiV1ChorusProFacturesValideurRechercherPost
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
    api_instance = factpulse.ChorusProApi(api_client)
    body_valideur_rechercher_factures_api_v1_chorus_pro_factures_valideur_rechercher_post = factpulse.BodyValideurRechercherFacturesApiV1ChorusProFacturesValideurRechercherPost() # BodyValideurRechercherFacturesApiV1ChorusProFacturesValideurRechercherPost | 

    try:
        # Rechercher factures à valider (Valideur)
        api_response = api_instance.valideur_rechercher_factures_api_v1_chorus_pro_factures_valideur_rechercher_post(body_valideur_rechercher_factures_api_v1_chorus_pro_factures_valideur_rechercher_post)
        print("The response of ChorusProApi->valideur_rechercher_factures_api_v1_chorus_pro_factures_valideur_rechercher_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->valideur_rechercher_factures_api_v1_chorus_pro_factures_valideur_rechercher_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_valideur_rechercher_factures_api_v1_chorus_pro_factures_valideur_rechercher_post** | [**BodyValideurRechercherFacturesApiV1ChorusProFacturesValideurRechercherPost**](BodyValideurRechercherFacturesApiV1ChorusProFacturesValideurRechercherPost.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **valideur_traiter_facture_api_v1_chorus_pro_factures_valideur_traiter_post**
> object valideur_traiter_facture_api_v1_chorus_pro_factures_valideur_traiter_post(body_valideur_traiter_facture_api_v1_chorus_pro_factures_valideur_traiter_post)

Valider ou refuser une facture (Valideur)

Valide ou refuse une facture en attente de validation.

    **Actions** :
    - Valider : La facture passe au statut suivant du circuit
    - Refuser : La facture est rejetée (motif obligatoire)

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_valideur_traiter_facture_api_v1_chorus_pro_factures_valideur_traiter_post import BodyValideurTraiterFactureApiV1ChorusProFacturesValideurTraiterPost
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
    api_instance = factpulse.ChorusProApi(api_client)
    body_valideur_traiter_facture_api_v1_chorus_pro_factures_valideur_traiter_post = factpulse.BodyValideurTraiterFactureApiV1ChorusProFacturesValideurTraiterPost() # BodyValideurTraiterFactureApiV1ChorusProFacturesValideurTraiterPost | 

    try:
        # Valider ou refuser une facture (Valideur)
        api_response = api_instance.valideur_traiter_facture_api_v1_chorus_pro_factures_valideur_traiter_post(body_valideur_traiter_facture_api_v1_chorus_pro_factures_valideur_traiter_post)
        print("The response of ChorusProApi->valideur_traiter_facture_api_v1_chorus_pro_factures_valideur_traiter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChorusProApi->valideur_traiter_facture_api_v1_chorus_pro_factures_valideur_traiter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_valideur_traiter_facture_api_v1_chorus_pro_factures_valideur_traiter_post** | [**BodyValideurTraiterFactureApiV1ChorusProFacturesValideurTraiterPost**](BodyValideurTraiterFactureApiV1ChorusProFacturesValideurTraiterPost.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

