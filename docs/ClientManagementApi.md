# factpulse.ClientManagementApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_client_api_v1_clients_uid_activer_post**](ClientManagementApi.md#activate_client_api_v1_clients_uid_activer_post) | **POST** /api/v1/clients/{uid}/activer | Activate a client
[**create_client_api_v1_clients_post**](ClientManagementApi.md#create_client_api_v1_clients_post) | **POST** /api/v1/clients | Create a client
[**deactivate_client_api_v1_clients_uid_desactiver_post**](ClientManagementApi.md#deactivate_client_api_v1_clients_uid_desactiver_post) | **POST** /api/v1/clients/{uid}/desactiver | Deactivate a client
[**delete_webhook_secret_api_v1_clients_uid_webhook_secret_delete**](ClientManagementApi.md#delete_webhook_secret_api_v1_clients_uid_webhook_secret_delete) | **DELETE** /api/v1/clients/{uid}/webhook-secret | Delete webhook secret
[**generate_webhook_secret_api_v1_clients_uid_webhook_secret_generate_post**](ClientManagementApi.md#generate_webhook_secret_api_v1_clients_uid_webhook_secret_generate_post) | **POST** /api/v1/clients/{uid}/webhook-secret/generate | Generate webhook secret
[**get_client_api_v1_clients_uid_get**](ClientManagementApi.md#get_client_api_v1_clients_uid_get) | **GET** /api/v1/clients/{uid} | Get client details
[**get_pdp_config_api_v1_clients_uid_pdp_config_get**](ClientManagementApi.md#get_pdp_config_api_v1_clients_uid_pdp_config_get) | **GET** /api/v1/clients/{uid}/pdp-config | Get client PDP configuration
[**get_webhook_secret_status_api_v1_clients_uid_webhook_secret_status_get**](ClientManagementApi.md#get_webhook_secret_status_api_v1_clients_uid_webhook_secret_status_get) | **GET** /api/v1/clients/{uid}/webhook-secret/status | Get webhook secret status
[**list_clients_api_v1_clients_get**](ClientManagementApi.md#list_clients_api_v1_clients_get) | **GET** /api/v1/clients | List clients
[**rotate_encryption_key_api_v1_clients_uid_rotate_encryption_key_post**](ClientManagementApi.md#rotate_encryption_key_api_v1_clients_uid_rotate_encryption_key_post) | **POST** /api/v1/clients/{uid}/rotate-encryption-key | Rotate client encryption key
[**update_client_api_v1_clients_uid_patch**](ClientManagementApi.md#update_client_api_v1_clients_uid_patch) | **PATCH** /api/v1/clients/{uid} | Update a client
[**update_pdp_config_api_v1_clients_uid_pdp_config_put**](ClientManagementApi.md#update_pdp_config_api_v1_clients_uid_pdp_config_put) | **PUT** /api/v1/clients/{uid}/pdp-config | Configure client PDP


# **activate_client_api_v1_clients_uid_activer_post**
> ClientActivateResponse activate_client_api_v1_clients_uid_activer_post(uid)

Activate a client

Activate a deactivated client.

**Scope**: Client level (JWT with client_uid that must match {uid})

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.client_activate_response import ClientActivateResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ClientManagementApi(api_client)
    uid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Activate a client
        api_response = api_instance.activate_client_api_v1_clients_uid_activer_post(uid)
        print("The response of ClientManagementApi->activate_client_api_v1_clients_uid_activer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->activate_client_api_v1_clients_uid_activer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **UUID**|  | 

### Return type

[**ClientActivateResponse**](ClientActivateResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid JWT token |  -  |
**403** | Access denied |  -  |
**404** | Client not found |  -  |
**500** | Server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_api_v1_clients_post**
> ClientDetail create_client_api_v1_clients_post(client_create_request)

Create a client

Create a new client for the account.

**Scope**: Account level (JWT without client_uid)

**Fields**:
- `name`: Client name (required)
- `description`: Optional description
- `siret`: Optional SIRET (14 digits)

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.client_create_request import ClientCreateRequest
from factpulse.models.client_detail import ClientDetail
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ClientManagementApi(api_client)
    client_create_request = factpulse.ClientCreateRequest() # ClientCreateRequest | 

    try:
        # Create a client
        api_response = api_instance.create_client_api_v1_clients_post(client_create_request)
        print("The response of ClientManagementApi->create_client_api_v1_clients_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->create_client_api_v1_clients_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_create_request** | [**ClientCreateRequest**](ClientCreateRequest.md)|  | 

### Return type

[**ClientDetail**](ClientDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid JWT token |  -  |
**403** | Access denied |  -  |
**404** | Client not found |  -  |
**500** | Server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_client_api_v1_clients_uid_desactiver_post**
> ClientActivateResponse deactivate_client_api_v1_clients_uid_desactiver_post(uid)

Deactivate a client

Deactivate an active client.

**Scope**: Client level (JWT with client_uid that must match {uid})

**Note**: A deactivated client cannot be used for API calls
(AFNOR, Chorus Pro, etc.).

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.client_activate_response import ClientActivateResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ClientManagementApi(api_client)
    uid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Deactivate a client
        api_response = api_instance.deactivate_client_api_v1_clients_uid_desactiver_post(uid)
        print("The response of ClientManagementApi->deactivate_client_api_v1_clients_uid_desactiver_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->deactivate_client_api_v1_clients_uid_desactiver_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **UUID**|  | 

### Return type

[**ClientActivateResponse**](ClientActivateResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid JWT token |  -  |
**403** | Access denied |  -  |
**404** | Client not found |  -  |
**500** | Server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_secret_api_v1_clients_uid_webhook_secret_delete**
> WebhookSecretDeleteResponse delete_webhook_secret_api_v1_clients_uid_webhook_secret_delete(uid)

Delete webhook secret

Delete the webhook secret for a client.

**Scope**: Client level (JWT with client_uid that must match {uid})

**After deletion**: Webhooks for this client will use the global server key
for HMAC signature instead of a client-specific key.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.webhook_secret_delete_response import WebhookSecretDeleteResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ClientManagementApi(api_client)
    uid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete webhook secret
        api_response = api_instance.delete_webhook_secret_api_v1_clients_uid_webhook_secret_delete(uid)
        print("The response of ClientManagementApi->delete_webhook_secret_api_v1_clients_uid_webhook_secret_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->delete_webhook_secret_api_v1_clients_uid_webhook_secret_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **UUID**|  | 

### Return type

[**WebhookSecretDeleteResponse**](WebhookSecretDeleteResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid JWT token |  -  |
**403** | Access denied |  -  |
**404** | Client not found |  -  |
**500** | Server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_webhook_secret_api_v1_clients_uid_webhook_secret_generate_post**
> WebhookSecretGenerateResponse generate_webhook_secret_api_v1_clients_uid_webhook_secret_generate_post(uid)

Generate webhook secret

Generate or regenerate the webhook secret for a client.

**Scope**: Client level (JWT with client_uid that must match {uid})

**Important**: Save the returned secret immediately - it will never be shown again.
The secret is used to sign webhooks sent by the server (HMAC-SHA256).

**If a secret already exists**: It will be replaced by the new one.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.webhook_secret_generate_response import WebhookSecretGenerateResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ClientManagementApi(api_client)
    uid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Generate webhook secret
        api_response = api_instance.generate_webhook_secret_api_v1_clients_uid_webhook_secret_generate_post(uid)
        print("The response of ClientManagementApi->generate_webhook_secret_api_v1_clients_uid_webhook_secret_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->generate_webhook_secret_api_v1_clients_uid_webhook_secret_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **UUID**|  | 

### Return type

[**WebhookSecretGenerateResponse**](WebhookSecretGenerateResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid JWT token |  -  |
**403** | Access denied |  -  |
**404** | Client not found |  -  |
**500** | Server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_api_v1_clients_uid_get**
> ClientDetail get_client_api_v1_clients_uid_get(uid)

Get client details

Get details of a client.

**Scope**: Client level (JWT with client_uid that must match {uid})

**Security**: If the JWT contains a client_uid, it must match the {uid}
in the URL, otherwise a 403 error is returned.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.client_detail import ClientDetail
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ClientManagementApi(api_client)
    uid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get client details
        api_response = api_instance.get_client_api_v1_clients_uid_get(uid)
        print("The response of ClientManagementApi->get_client_api_v1_clients_uid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->get_client_api_v1_clients_uid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **UUID**|  | 

### Return type

[**ClientDetail**](ClientDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid JWT token |  -  |
**403** | Access denied |  -  |
**404** | Client not found |  -  |
**500** | Server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdp_config_api_v1_clients_uid_pdp_config_get**
> PDPConfigResponse get_pdp_config_api_v1_clients_uid_pdp_config_get(uid)

Get client PDP configuration

Get the PDP (PA/PDP) configuration for a client.

**Scope**: Client level (JWT with client_uid that must match {uid})

**Security**: The client secret is never returned. Only a status
(`secretStatus`) indicates whether a secret is configured.

**Response**:
- If configured: all config details (URLs, client_id, secret status)
- If not configured: `isConfigured: false` with a message

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.pdp_config_response import PDPConfigResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ClientManagementApi(api_client)
    uid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get client PDP configuration
        api_response = api_instance.get_pdp_config_api_v1_clients_uid_pdp_config_get(uid)
        print("The response of ClientManagementApi->get_pdp_config_api_v1_clients_uid_pdp_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->get_pdp_config_api_v1_clients_uid_pdp_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **UUID**|  | 

### Return type

[**PDPConfigResponse**](PDPConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid JWT token |  -  |
**403** | Access denied |  -  |
**404** | Client not found |  -  |
**500** | Server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_secret_status_api_v1_clients_uid_webhook_secret_status_get**
> WebhookSecretStatusResponse get_webhook_secret_status_api_v1_clients_uid_webhook_secret_status_get(uid)

Get webhook secret status

Check if a webhook secret is configured for a client.

**Scope**: Client level (JWT with client_uid that must match {uid})

**Response**:
- `hasSecret`: Whether a webhook secret is configured
- `createdAt`: When the secret was created (if exists)

**Note**: The secret value is never returned, only its status.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.webhook_secret_status_response import WebhookSecretStatusResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ClientManagementApi(api_client)
    uid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get webhook secret status
        api_response = api_instance.get_webhook_secret_status_api_v1_clients_uid_webhook_secret_status_get(uid)
        print("The response of ClientManagementApi->get_webhook_secret_status_api_v1_clients_uid_webhook_secret_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->get_webhook_secret_status_api_v1_clients_uid_webhook_secret_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **UUID**|  | 

### Return type

[**WebhookSecretStatusResponse**](WebhookSecretStatusResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid JWT token |  -  |
**403** | Access denied |  -  |
**404** | Client not found |  -  |
**500** | Server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clients_api_v1_clients_get**
> ClientListResponse list_clients_api_v1_clients_get(page=page, page_size=page_size)

List clients

Paginated list of clients for the account.

**Scope**: Account level (JWT without client_uid)

**Pagination**:
- `page`: Page number (default: 1)
- `pageSize`: Page size (default: 20, max: 100)

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.client_list_response import ClientListResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ClientManagementApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Page size (optional) (default to 20)

    try:
        # List clients
        api_response = api_instance.list_clients_api_v1_clients_get(page=page, page_size=page_size)
        print("The response of ClientManagementApi->list_clients_api_v1_clients_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->list_clients_api_v1_clients_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Page size | [optional] [default to 20]

### Return type

[**ClientListResponse**](ClientListResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid JWT token |  -  |
**403** | Access denied |  -  |
**404** | Client not found |  -  |
**500** | Server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_encryption_key_api_v1_clients_uid_rotate_encryption_key_post**
> KeyRotationResponse rotate_encryption_key_api_v1_clients_uid_rotate_encryption_key_post(uid, key_rotation_request)

Rotate client encryption key

Rotate the client encryption key for all secrets in double encryption mode.

**Scope**: Client level (JWT with client_uid that must match {uid})

**What this does**:
1. Decrypts all secrets (PDP, Chorus Pro) using the old key
2. Re-encrypts them using the new key
3. Saves to database

**Important notes**:
- Both keys must be base64-encoded AES-256 keys (32 bytes each)
- The old key becomes invalid immediately after rotation
- Only secrets encrypted with `encryptionMode: "double"` are affected
- If the client has no double-encrypted secrets, returns 404

**Security**:
- The old key must be valid (decryption is verified)
- If decryption fails, rotation is aborted (atomic operation)
- Neither key is logged or stored by the server

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.key_rotation_request import KeyRotationRequest
from factpulse.models.key_rotation_response import KeyRotationResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ClientManagementApi(api_client)
    uid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    key_rotation_request = factpulse.KeyRotationRequest() # KeyRotationRequest | 

    try:
        # Rotate client encryption key
        api_response = api_instance.rotate_encryption_key_api_v1_clients_uid_rotate_encryption_key_post(uid, key_rotation_request)
        print("The response of ClientManagementApi->rotate_encryption_key_api_v1_clients_uid_rotate_encryption_key_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->rotate_encryption_key_api_v1_clients_uid_rotate_encryption_key_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **UUID**|  | 
 **key_rotation_request** | [**KeyRotationRequest**](KeyRotationRequest.md)|  | 

### Return type

[**KeyRotationResponse**](KeyRotationResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid JWT token |  -  |
**403** | Access denied |  -  |
**404** | Client not found |  -  |
**500** | Server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_api_v1_clients_uid_patch**
> ClientDetail update_client_api_v1_clients_uid_patch(uid, client_update_request)

Update a client

Update client information (partial update).

**Scope**: Client level (JWT with client_uid that must match {uid})

**Updatable fields**:
- `name`: Client name
- `description`: Description
- `siret`: SIRET (14 digits)

Only provided fields are updated.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.client_detail import ClientDetail
from factpulse.models.client_update_request import ClientUpdateRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ClientManagementApi(api_client)
    uid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    client_update_request = factpulse.ClientUpdateRequest() # ClientUpdateRequest | 

    try:
        # Update a client
        api_response = api_instance.update_client_api_v1_clients_uid_patch(uid, client_update_request)
        print("The response of ClientManagementApi->update_client_api_v1_clients_uid_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->update_client_api_v1_clients_uid_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **UUID**|  | 
 **client_update_request** | [**ClientUpdateRequest**](ClientUpdateRequest.md)|  | 

### Return type

[**ClientDetail**](ClientDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid JWT token |  -  |
**403** | Access denied |  -  |
**404** | Client not found |  -  |
**500** | Server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pdp_config_api_v1_clients_uid_pdp_config_put**
> PDPConfigResponse update_pdp_config_api_v1_clients_uid_pdp_config_put(uid, pdp_config_update_request, x_encryption_key=x_encryption_key)

Configure client PDP

Configure or update the PDP (PA/PDP) configuration for a client.

**Scope**: Client level (JWT with client_uid that must match {uid})

**Required fields**:
- `flowServiceUrl`: PDP Flow Service URL
- `tokenUrl`: PDP OAuth token URL
- `oauthClientId`: OAuth Client ID
- `clientSecret`: OAuth Client Secret (sent but NEVER returned)

**Optional fields**:
- `isActive`: Enable/disable the config (default: true)
- `modeSandbox`: Sandbox mode (default: false)
- `encryptionMode`: Encryption mode (default: "fernet")
  - "fernet": Server-side encryption only
  - "double": Client AES-256-GCM + Server Fernet (requires X-Encryption-Key header)

**Double Encryption Mode**:
When `encryptionMode` is set to "double", you MUST also provide the
`X-Encryption-Key` header containing a base64-encoded AES-256 key (32 bytes).
This key is used to encrypt the `clientSecret` on the client side before
the server encrypts it again with Fernet. The server cannot decrypt the
secret without the client key.

**Security**: The `clientSecret` is stored encrypted on Django side
and is never returned in API responses.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.pdp_config_response import PDPConfigResponse
from factpulse.models.pdp_config_update_request import PDPConfigUpdateRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = factpulse.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with factpulse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = factpulse.ClientManagementApi(api_client)
    uid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    pdp_config_update_request = factpulse.PDPConfigUpdateRequest() # PDPConfigUpdateRequest | 
    x_encryption_key = 'x_encryption_key_example' # str | Client encryption key for double encryption mode. Must be a base64-encoded AES-256 key (32 bytes). Required only when accessing resources encrypted with encryption_mode='double'. (optional)

    try:
        # Configure client PDP
        api_response = api_instance.update_pdp_config_api_v1_clients_uid_pdp_config_put(uid, pdp_config_update_request, x_encryption_key=x_encryption_key)
        print("The response of ClientManagementApi->update_pdp_config_api_v1_clients_uid_pdp_config_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->update_pdp_config_api_v1_clients_uid_pdp_config_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **UUID**|  | 
 **pdp_config_update_request** | [**PDPConfigUpdateRequest**](PDPConfigUpdateRequest.md)|  | 
 **x_encryption_key** | **str**| Client encryption key for double encryption mode. Must be a base64-encoded AES-256 key (32 bytes). Required only when accessing resources encrypted with encryption_mode&#x3D;&#39;double&#39;. | [optional] 

### Return type

[**PDPConfigResponse**](PDPConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid JWT token |  -  |
**403** | Access denied |  -  |
**404** | Client not found |  -  |
**500** | Server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

