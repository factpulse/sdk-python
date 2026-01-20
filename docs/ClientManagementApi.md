# factpulse.ClientManagementApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_client_api_v1_clients_uid_activer_post**](ClientManagementApi.md#activate_client_api_v1_clients_uid_activer_post) | **POST** /api/v1/clients/{uid}/activer | Activate a client
[**create_client_api_v1_clients_post**](ClientManagementApi.md#create_client_api_v1_clients_post) | **POST** /api/v1/clients | Create a client
[**deactivate_client_api_v1_clients_uid_desactiver_post**](ClientManagementApi.md#deactivate_client_api_v1_clients_uid_desactiver_post) | **POST** /api/v1/clients/{uid}/desactiver | Deactivate a client
[**get_client_api_v1_clients_uid_get**](ClientManagementApi.md#get_client_api_v1_clients_uid_get) | **GET** /api/v1/clients/{uid} | Get client details
[**get_pdp_config_api_v1_clients_uid_pdp_config_get**](ClientManagementApi.md#get_pdp_config_api_v1_clients_uid_pdp_config_get) | **GET** /api/v1/clients/{uid}/pdp-config | Get client PDP configuration
[**list_clients_api_v1_clients_get**](ClientManagementApi.md#list_clients_api_v1_clients_get) | **GET** /api/v1/clients | List clients
[**update_client_api_v1_clients_uid_patch**](ClientManagementApi.md#update_client_api_v1_clients_uid_patch) | **PATCH** /api/v1/clients/{uid} | Update a client
[**update_pdp_config_api_v1_clients_uid_pdp_config_put**](ClientManagementApi.md#update_pdp_config_api_v1_clients_uid_pdp_config_put) | **PUT** /api/v1/clients/{uid}/pdp-config | Configure client PDP


# **activate_client_api_v1_clients_uid_activer_post**
> ClientActivateResponse activate_client_api_v1_clients_uid_activer_post(uid)

Activate a client

Activate a deactivated client.

**Scope**: Client level (JWT with client_uid that must match {uid})

### Example

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

[HTTPBearer](../README.md#HTTPBearer)

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

[HTTPBearer](../README.md#HTTPBearer)

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

[HTTPBearer](../README.md#HTTPBearer)

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

[HTTPBearer](../README.md#HTTPBearer)

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

[HTTPBearer](../README.md#HTTPBearer)

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

[HTTPBearer](../README.md#HTTPBearer)

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

[HTTPBearer](../README.md#HTTPBearer)

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
> PDPConfigResponse update_pdp_config_api_v1_clients_uid_pdp_config_put(uid, pdp_config_update_request)

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

**Security**: The `clientSecret` is stored encrypted on Django side
and is never returned in API responses.

### Example

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

    try:
        # Configure client PDP
        api_response = api_instance.update_pdp_config_api_v1_clients_uid_pdp_config_put(uid, pdp_config_update_request)
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

### Return type

[**PDPConfigResponse**](PDPConfigResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

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

