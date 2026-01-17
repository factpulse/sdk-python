# factpulse.CDARCycleDeVieApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_cdar_api_v1_cdar_generate_post**](CDARCycleDeVieApi.md#generate_cdar_api_v1_cdar_generate_post) | **POST** /api/v1/cdar/generate | Générer un message CDAR
[**get_action_codes_api_v1_cdar_action_codes_get**](CDARCycleDeVieApi.md#get_action_codes_api_v1_cdar_action_codes_get) | **GET** /api/v1/cdar/action-codes | Liste des codes action CDAR
[**get_reason_codes_api_v1_cdar_reason_codes_get**](CDARCycleDeVieApi.md#get_reason_codes_api_v1_cdar_reason_codes_get) | **GET** /api/v1/cdar/reason-codes | Liste des codes motif CDAR
[**get_status_codes_api_v1_cdar_status_codes_get**](CDARCycleDeVieApi.md#get_status_codes_api_v1_cdar_status_codes_get) | **GET** /api/v1/cdar/status-codes | Liste des codes statut CDAR
[**submit_cdar_api_v1_cdar_submit_post**](CDARCycleDeVieApi.md#submit_cdar_api_v1_cdar_submit_post) | **POST** /api/v1/cdar/submit | Générer et soumettre un message CDAR
[**submit_cdar_xml_api_v1_cdar_submit_xml_post**](CDARCycleDeVieApi.md#submit_cdar_xml_api_v1_cdar_submit_xml_post) | **POST** /api/v1/cdar/submit-xml | Soumettre un XML CDAR pré-généré
[**validate_cdar_api_v1_cdar_validate_post**](CDARCycleDeVieApi.md#validate_cdar_api_v1_cdar_validate_post) | **POST** /api/v1/cdar/validate | Valider des données CDAR


# **generate_cdar_api_v1_cdar_generate_post**
> GenerateCDARResponse generate_cdar_api_v1_cdar_generate_post(create_cdar_request)

Générer un message CDAR

Génère un message XML CDAR (Cross Domain Acknowledgement and Response)
pour communiquer le statut d'une facture.

**Types de messages:**
- **23** (Traitement): Message de cycle de vie standard
- **305** (Transmission): Message de transmission entre plateformes

**Règles métier:**
- BR-FR-CDV-14: Le statut 212 (ENCAISSEE) requiert un montant encaissé
- BR-FR-CDV-15: Les statuts 206/207/208/210/213/501 requièrent un code motif

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.create_cdar_request import CreateCDARRequest
from factpulse.models.generate_cdar_response import GenerateCDARResponse
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
    api_instance = factpulse.CDARCycleDeVieApi(api_client)
    create_cdar_request = factpulse.CreateCDARRequest() # CreateCDARRequest | 

    try:
        # Générer un message CDAR
        api_response = api_instance.generate_cdar_api_v1_cdar_generate_post(create_cdar_request)
        print("The response of CDARCycleDeVieApi->generate_cdar_api_v1_cdar_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDARCycleDeVieApi->generate_cdar_api_v1_cdar_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cdar_request** | [**CreateCDARRequest**](CreateCDARRequest.md)|  | 

### Return type

[**GenerateCDARResponse**](GenerateCDARResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Requête invalide |  -  |
**422** | Erreur de validation |  -  |
**500** | Erreur serveur |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_codes_api_v1_cdar_action_codes_get**
> ActionCodesResponse get_action_codes_api_v1_cdar_action_codes_get()

Liste des codes action CDAR

Retourne la liste complète des codes action (BR-FR-CDV-CL-10).

Ces codes indiquent l'action demandée sur la facture.

### Example


```python
import factpulse
from factpulse.models.action_codes_response import ActionCodesResponse
from factpulse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://factpulse.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "https://factpulse.fr"
)


# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.CDARCycleDeVieApi(api_client)

    try:
        # Liste des codes action CDAR
        api_response = api_instance.get_action_codes_api_v1_cdar_action_codes_get()
        print("The response of CDARCycleDeVieApi->get_action_codes_api_v1_cdar_action_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDARCycleDeVieApi->get_action_codes_api_v1_cdar_action_codes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ActionCodesResponse**](ActionCodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Requête invalide |  -  |
**422** | Erreur de validation |  -  |
**500** | Erreur serveur |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reason_codes_api_v1_cdar_reason_codes_get**
> ReasonCodesResponse get_reason_codes_api_v1_cdar_reason_codes_get()

Liste des codes motif CDAR

Retourne la liste complète des codes motif de statut (BR-FR-CDV-CL-09).

Ces codes expliquent la raison d'un statut particulier.

### Example


```python
import factpulse
from factpulse.models.reason_codes_response import ReasonCodesResponse
from factpulse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://factpulse.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "https://factpulse.fr"
)


# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.CDARCycleDeVieApi(api_client)

    try:
        # Liste des codes motif CDAR
        api_response = api_instance.get_reason_codes_api_v1_cdar_reason_codes_get()
        print("The response of CDARCycleDeVieApi->get_reason_codes_api_v1_cdar_reason_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDARCycleDeVieApi->get_reason_codes_api_v1_cdar_reason_codes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReasonCodesResponse**](ReasonCodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Requête invalide |  -  |
**422** | Erreur de validation |  -  |
**500** | Erreur serveur |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_codes_api_v1_cdar_status_codes_get**
> StatusCodesResponse get_status_codes_api_v1_cdar_status_codes_get()

Liste des codes statut CDAR

Retourne la liste complète des codes statut de facture (BR-FR-CDV-CL-06).

Ces codes indiquent l'état du cycle de vie d'une facture.

### Example


```python
import factpulse
from factpulse.models.status_codes_response import StatusCodesResponse
from factpulse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://factpulse.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = factpulse.Configuration(
    host = "https://factpulse.fr"
)


# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.CDARCycleDeVieApi(api_client)

    try:
        # Liste des codes statut CDAR
        api_response = api_instance.get_status_codes_api_v1_cdar_status_codes_get()
        print("The response of CDARCycleDeVieApi->get_status_codes_api_v1_cdar_status_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDARCycleDeVieApi->get_status_codes_api_v1_cdar_status_codes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatusCodesResponse**](StatusCodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Requête invalide |  -  |
**422** | Erreur de validation |  -  |
**500** | Erreur serveur |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_cdar_api_v1_cdar_submit_post**
> SubmitCDARResponse submit_cdar_api_v1_cdar_submit_post(user_id, body_submit_cdar_api_v1_cdar_submit_post, jwt_token=jwt_token, client_uid=client_uid)

Générer et soumettre un message CDAR

Génère un message CDAR et le soumet à la plateforme PA/PDP.

Nécessite une authentification AFNOR valide.

**Types de flux (flowType):**
- `CustomerInvoiceLC`: Cycle de vie côté client (acheteur)
- `SupplierInvoiceLC`: Cycle de vie côté fournisseur (vendeur)

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_submit_cdar_api_v1_cdar_submit_post import BodySubmitCdarApiV1CdarSubmitPost
from factpulse.models.submit_cdar_response import SubmitCDARResponse
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
    api_instance = factpulse.CDARCycleDeVieApi(api_client)
    user_id = 56 # int | 
    body_submit_cdar_api_v1_cdar_submit_post = factpulse.BodySubmitCdarApiV1CdarSubmitPost() # BodySubmitCdarApiV1CdarSubmitPost | 
    jwt_token = 'jwt_token_example' # str |  (optional)
    client_uid = 'client_uid_example' # str |  (optional)

    try:
        # Générer et soumettre un message CDAR
        api_response = api_instance.submit_cdar_api_v1_cdar_submit_post(user_id, body_submit_cdar_api_v1_cdar_submit_post, jwt_token=jwt_token, client_uid=client_uid)
        print("The response of CDARCycleDeVieApi->submit_cdar_api_v1_cdar_submit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDARCycleDeVieApi->submit_cdar_api_v1_cdar_submit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **body_submit_cdar_api_v1_cdar_submit_post** | [**BodySubmitCdarApiV1CdarSubmitPost**](BodySubmitCdarApiV1CdarSubmitPost.md)|  | 
 **jwt_token** | **str**|  | [optional] 
 **client_uid** | **str**|  | [optional] 

### Return type

[**SubmitCDARResponse**](SubmitCDARResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Requête invalide |  -  |
**422** | Erreur de validation |  -  |
**500** | Erreur serveur |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_cdar_xml_api_v1_cdar_submit_xml_post**
> SubmitCDARResponse submit_cdar_xml_api_v1_cdar_submit_xml_post(user_id, body_submit_cdar_xml_api_v1_cdar_submit_xml_post, jwt_token=jwt_token, client_uid=client_uid)

Soumettre un XML CDAR pré-généré

Soumet un message XML CDAR pré-généré à la plateforme PA/PDP.

Utile pour soumettre des XML générés par d'autres systèmes.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.body_submit_cdar_xml_api_v1_cdar_submit_xml_post import BodySubmitCdarXmlApiV1CdarSubmitXmlPost
from factpulse.models.submit_cdar_response import SubmitCDARResponse
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
    api_instance = factpulse.CDARCycleDeVieApi(api_client)
    user_id = 56 # int | 
    body_submit_cdar_xml_api_v1_cdar_submit_xml_post = factpulse.BodySubmitCdarXmlApiV1CdarSubmitXmlPost() # BodySubmitCdarXmlApiV1CdarSubmitXmlPost | 
    jwt_token = 'jwt_token_example' # str |  (optional)
    client_uid = 'client_uid_example' # str |  (optional)

    try:
        # Soumettre un XML CDAR pré-généré
        api_response = api_instance.submit_cdar_xml_api_v1_cdar_submit_xml_post(user_id, body_submit_cdar_xml_api_v1_cdar_submit_xml_post, jwt_token=jwt_token, client_uid=client_uid)
        print("The response of CDARCycleDeVieApi->submit_cdar_xml_api_v1_cdar_submit_xml_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDARCycleDeVieApi->submit_cdar_xml_api_v1_cdar_submit_xml_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **body_submit_cdar_xml_api_v1_cdar_submit_xml_post** | [**BodySubmitCdarXmlApiV1CdarSubmitXmlPost**](BodySubmitCdarXmlApiV1CdarSubmitXmlPost.md)|  | 
 **jwt_token** | **str**|  | [optional] 
 **client_uid** | **str**|  | [optional] 

### Return type

[**SubmitCDARResponse**](SubmitCDARResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Requête invalide |  -  |
**422** | Erreur de validation |  -  |
**500** | Erreur serveur |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_cdar_api_v1_cdar_validate_post**
> ValidateCDARResponse validate_cdar_api_v1_cdar_validate_post(validate_cdar_request)

Valider des données CDAR

Valide les données CDAR sans générer le XML.

Vérifie:
- Les formats des champs (SIREN, dates, etc.)
- Les codes enums (statut, motif, action)
- Les règles métier BR-FR-CDV-*

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.validate_cdar_request import ValidateCDARRequest
from factpulse.models.validate_cdar_response import ValidateCDARResponse
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
    api_instance = factpulse.CDARCycleDeVieApi(api_client)
    validate_cdar_request = factpulse.ValidateCDARRequest() # ValidateCDARRequest | 

    try:
        # Valider des données CDAR
        api_response = api_instance.validate_cdar_api_v1_cdar_validate_post(validate_cdar_request)
        print("The response of CDARCycleDeVieApi->validate_cdar_api_v1_cdar_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDARCycleDeVieApi->validate_cdar_api_v1_cdar_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_cdar_request** | [**ValidateCDARRequest**](ValidateCDARRequest.md)|  | 

### Return type

[**ValidateCDARResponse**](ValidateCDARResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Requête invalide |  -  |
**422** | Erreur de validation |  -  |
**500** | Erreur serveur |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

