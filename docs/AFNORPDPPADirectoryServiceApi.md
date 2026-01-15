# factpulse.AFNORPDPPADirectoryServiceApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_post**](AFNORPDPPADirectoryServiceApi.md#create_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_post) | **POST** /api/v1/afnor/directory/v1/directory-line | Creating a directory line
[**create_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_post**](AFNORPDPPADirectoryServiceApi.md#create_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_post) | **POST** /api/v1/afnor/directory/v1/routing-code | Create a routing code
[**delete_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_delete**](AFNORPDPPADirectoryServiceApi.md#delete_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_delete) | **DELETE** /api/v1/afnor/directory/v1/directory-line/id-instance:{id_instance} | Delete a directory line
[**directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get**](AFNORPDPPADirectoryServiceApi.md#directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get) | **GET** /api/v1/afnor/directory/v1/healthcheck | Healthcheck Directory Service
[**get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get**](AFNORPDPPADirectoryServiceApi.md#get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get) | **GET** /api/v1/afnor/directory/v1/directory-line/code:{addressing_identifier} | Get a directory line.
[**get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get**](AFNORPDPPADirectoryServiceApi.md#get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get) | **GET** /api/v1/afnor/directory/v1/directory-line/id-instance:{id_instance} | Get a directory line.
[**get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get**](AFNORPDPPADirectoryServiceApi.md#get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get) | **GET** /api/v1/afnor/directory/v1/routing-code/id-instance:{id_instance} | Get a routing code by instance-id.
[**get_routing_code_by_siret_and_code_proxy_api_v1_afnor_directory_v1_routing_code_siret_siret_code_routing_identifier_get**](AFNORPDPPADirectoryServiceApi.md#get_routing_code_by_siret_and_code_proxy_api_v1_afnor_directory_v1_routing_code_siret_siret_code_routing_identifier_get) | **GET** /api/v1/afnor/directory/v1/routing-code/siret:{siret}/code:{routing_identifier} | Get a routing code by SIRET and routing identifier
[**get_siren_by_code_insee_proxy_api_v1_afnor_directory_v1_siren_code_insee_siren_get**](AFNORPDPPADirectoryServiceApi.md#get_siren_by_code_insee_proxy_api_v1_afnor_directory_v1_siren_code_insee_siren_get) | **GET** /api/v1/afnor/directory/v1/siren/code-insee:{siren} | Consult a siren (legal unit) by SIREN number
[**get_siren_by_id_instance_proxy_api_v1_afnor_directory_v1_siren_id_instance_id_instance_get**](AFNORPDPPADirectoryServiceApi.md#get_siren_by_id_instance_proxy_api_v1_afnor_directory_v1_siren_id_instance_id_instance_get) | **GET** /api/v1/afnor/directory/v1/siren/id-instance:{id_instance} | Gets a siren (legal unit) by instance ID
[**get_siret_by_code_insee_proxy_api_v1_afnor_directory_v1_siret_code_insee_siret_get**](AFNORPDPPADirectoryServiceApi.md#get_siret_by_code_insee_proxy_api_v1_afnor_directory_v1_siret_code_insee_siret_get) | **GET** /api/v1/afnor/directory/v1/siret/code-insee:{siret} | Gets a siret (facility) by SIRET number
[**get_siret_by_id_instance_proxy_api_v1_afnor_directory_v1_siret_id_instance_id_instance_get**](AFNORPDPPADirectoryServiceApi.md#get_siret_by_id_instance_proxy_api_v1_afnor_directory_v1_siret_id_instance_id_instance_get) | **GET** /api/v1/afnor/directory/v1/siret/id-instance:{id_instance} | Gets a siret (facility) by id-instance
[**patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch**](AFNORPDPPADirectoryServiceApi.md#patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch) | **PATCH** /api/v1/afnor/directory/v1/directory-line/id-instance:{id_instance} | Partially updates a directory line..
[**patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch**](AFNORPDPPADirectoryServiceApi.md#patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch) | **PATCH** /api/v1/afnor/directory/v1/routing-code/id-instance:{id_instance} | Partially update a private routing code.
[**put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put**](AFNORPDPPADirectoryServiceApi.md#put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put) | **PUT** /api/v1/afnor/directory/v1/routing-code/id-instance:{id_instance} | Completely update a private routing code.
[**search_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_search_post**](AFNORPDPPADirectoryServiceApi.md#search_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_search_post) | **POST** /api/v1/afnor/directory/v1/directory-line/search | Search for a directory line
[**search_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_search_post**](AFNORPDPPADirectoryServiceApi.md#search_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_search_post) | **POST** /api/v1/afnor/directory/v1/routing-code/search | Search for a routing code
[**search_siren_proxy_api_v1_afnor_directory_v1_siren_search_post**](AFNORPDPPADirectoryServiceApi.md#search_siren_proxy_api_v1_afnor_directory_v1_siren_search_post) | **POST** /api/v1/afnor/directory/v1/siren/search | SIREN search (or legal unit)
[**search_siret_proxy_api_v1_afnor_directory_v1_siret_search_post**](AFNORPDPPADirectoryServiceApi.md#search_siret_proxy_api_v1_afnor_directory_v1_siret_search_post) | **POST** /api/v1/afnor/directory/v1/siret/search | Search for a SIRET (facility)


# **create_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_post**
> object create_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_post()

Creating a directory line

Creation of a new directory line for a SIREN, a SIRET or a ROUTING CODE.

### Example


```python
import factpulse
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
**201** | A new resource has been created. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_post**
> object create_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_post()

Create a routing code

Creating a routing code.

### Example


```python
import factpulse
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
**201** | A new resource has been created. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_delete**
> object delete_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_delete(id_instance)

Delete a directory line

Delete a directory line.

### Example


```python
import factpulse
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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    id_instance = 'id_instance_example' # str | AFNOR instance ID (UUID)

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
 **id_instance** | **str**| AFNOR instance ID (UUID) | 

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
**204** | OK. The resource has been deleted. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get**
> object directory_healthcheck_proxy_api_v1_afnor_directory_v1_healthcheck_get()

Healthcheck Directory Service

Check Directory Service availability (AFNOR XP Z12-013 compliant)

### Example


```python
import factpulse
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
**200** | OK - Service is operational |  -  |
**500** | Internal Server Error. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get**
> AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get(addressing_identifier)

Get a directory line.

Retrieve the data from the directory line corresponding to the identifier passed in parameters.

### Example


```python
import factpulse
from factpulse.models.afnor_directory_line_payload_history_legal_unit_facility_routing_code import AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode
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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    addressing_identifier = 'addressing_identifier_example' # str | Addressing identifier (SIREN, SIRET or routing code)

    try:
        # Get a directory line.
        api_response = api_instance.get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get(addressing_identifier)
        print("The response of AFNORPDPPADirectoryServiceApi->get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->get_directory_line_by_code_proxy_api_v1_afnor_directory_v1_directory_line_code_addressing_identifier_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addressing_identifier** | **str**| Addressing identifier (SIREN, SIRET or routing code) | 

### Return type

[**AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode**](AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retourns a directory line. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get**
> AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get(id_instance)

Get a directory line.

Retrieve the data from the directory line corresponding to the identifier passed in parameters.

### Example


```python
import factpulse
from factpulse.models.afnor_directory_line_payload_history_legal_unit_facility_routing_code import AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode
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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    id_instance = 'id_instance_example' # str | AFNOR instance ID (UUID)

    try:
        # Get a directory line.
        api_response = api_instance.get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->get_directory_line_by_id_instance_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**| AFNOR instance ID (UUID) | 

### Return type

[**AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode**](AFNORDirectoryLinePayloadHistoryLegalUnitFacilityRoutingCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a directory line. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get**
> AFNORRoutingCodePayloadHistoryLegalUnitFacility get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get(id_instance)

Get a routing code by instance-id.

Retrieve the Routing Code data corresponding to the Instance ID.

### Example


```python
import factpulse
from factpulse.models.afnor_routing_code_payload_history_legal_unit_facility import AFNORRoutingCodePayloadHistoryLegalUnitFacility
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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    id_instance = 'id_instance_example' # str | AFNOR instance ID (UUID)

    try:
        # Get a routing code by instance-id.
        api_response = api_instance.get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->get_routing_code_by_id_instance_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**| AFNOR instance ID (UUID) | 

### Return type

[**AFNORRoutingCodePayloadHistoryLegalUnitFacility**](AFNORRoutingCodePayloadHistoryLegalUnitFacility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a routing code. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routing_code_by_siret_and_code_proxy_api_v1_afnor_directory_v1_routing_code_siret_siret_code_routing_identifier_get**
> AFNORRoutingCodePayloadHistoryLegalUnitFacility get_routing_code_by_siret_and_code_proxy_api_v1_afnor_directory_v1_routing_code_siret_siret_code_routing_identifier_get(siret, routing_identifier)

Get a routing code by SIRET and routing identifier

Retrieve the Routing Code data corresponding to the identifier passed in parameters.

### Example


```python
import factpulse
from factpulse.models.afnor_routing_code_payload_history_legal_unit_facility import AFNORRoutingCodePayloadHistoryLegalUnitFacility
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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    siret = 'siret_example' # str | 14-digit SIRET number (INSEE establishment identifier)
    routing_identifier = 'routing_identifier_example' # str | Routing code identifier

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
 **siret** | **str**| 14-digit SIRET number (INSEE establishment identifier) | 
 **routing_identifier** | **str**| Routing code identifier | 

### Return type

[**AFNORRoutingCodePayloadHistoryLegalUnitFacility**](AFNORRoutingCodePayloadHistoryLegalUnitFacility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a routing code. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_siren_by_code_insee_proxy_api_v1_afnor_directory_v1_siren_code_insee_siren_get**
> AFNORLegalUnitPayloadHistory get_siren_by_code_insee_proxy_api_v1_afnor_directory_v1_siren_code_insee_siren_get(siren)

Consult a siren (legal unit) by SIREN number

Returns the details of a company (legal unit) identified by the SIREN number passed as a parameter.

### Example


```python
import factpulse
from factpulse.models.afnor_legal_unit_payload_history import AFNORLegalUnitPayloadHistory
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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    siren = 'siren_example' # str | 9-digit SIREN number (INSEE company identifier)

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
 **siren** | **str**| 9-digit SIREN number (INSEE company identifier) | 

### Return type

[**AFNORLegalUnitPayloadHistory**](AFNORLegalUnitPayloadHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a company. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_siren_by_id_instance_proxy_api_v1_afnor_directory_v1_siren_id_instance_id_instance_get**
> AFNORLegalUnitPayloadHistory get_siren_by_id_instance_proxy_api_v1_afnor_directory_v1_siren_id_instance_id_instance_get(id_instance)

Gets a siren (legal unit) by instance ID

Returns the details of a company (legal unit) identified by the id-instance passed as a parameter.

### Example


```python
import factpulse
from factpulse.models.afnor_legal_unit_payload_history import AFNORLegalUnitPayloadHistory
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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    id_instance = 'id_instance_example' # str | AFNOR instance ID (UUID)

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
 **id_instance** | **str**| AFNOR instance ID (UUID) | 

### Return type

[**AFNORLegalUnitPayloadHistory**](AFNORLegalUnitPayloadHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a routing code. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_siret_by_code_insee_proxy_api_v1_afnor_directory_v1_siret_code_insee_siret_get**
> AFNORFacilityPayloadHistory get_siret_by_code_insee_proxy_api_v1_afnor_directory_v1_siret_code_insee_siret_get(siret)

Gets a siret (facility) by SIRET number

Returns the details of a facility associated to a SIRET.

### Example


```python
import factpulse
from factpulse.models.afnor_facility_payload_history import AFNORFacilityPayloadHistory
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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    siret = 'siret_example' # str | 14-digit SIRET number (INSEE establishment identifier)

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
 **siret** | **str**| 14-digit SIRET number (INSEE establishment identifier) | 

### Return type

[**AFNORFacilityPayloadHistory**](AFNORFacilityPayloadHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a facility. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_siret_by_id_instance_proxy_api_v1_afnor_directory_v1_siret_id_instance_id_instance_get**
> AFNORFacilityPayloadHistory get_siret_by_id_instance_proxy_api_v1_afnor_directory_v1_siret_id_instance_id_instance_get(id_instance)

Gets a siret (facility) by id-instance

Returns the details of a facility according to an instance-id.

### Example


```python
import factpulse
from factpulse.models.afnor_facility_payload_history import AFNORFacilityPayloadHistory
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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    id_instance = 'id_instance_example' # str | AFNOR instance ID (UUID)

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
 **id_instance** | **str**| AFNOR instance ID (UUID) | 

### Return type

[**AFNORFacilityPayloadHistory**](AFNORFacilityPayloadHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a routing code. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch**
> AFNORDirectoryLinePost201Response patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch(id_instance)

Partially updates a directory line..

Partially updates a directory line.

### Example


```python
import factpulse
from factpulse.models.afnor_directory_line_post201_response import AFNORDirectoryLinePost201Response
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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    id_instance = 'id_instance_example' # str | AFNOR instance ID (UUID)

    try:
        # Partially updates a directory line..
        api_response = api_instance.patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->patch_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_id_instance_id_instance_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**| AFNOR instance ID (UUID) | 

### Return type

[**AFNORDirectoryLinePost201Response**](AFNORDirectoryLinePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch**
> AFNORRoutingCodePost201Response patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch(id_instance)

Partially update a private routing code.

Partially update a private routing code.

### Example


```python
import factpulse
from factpulse.models.afnor_routing_code_post201_response import AFNORRoutingCodePost201Response
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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    id_instance = 'id_instance_example' # str | AFNOR instance ID (UUID)

    try:
        # Partially update a private routing code.
        api_response = api_instance.patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->patch_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**| AFNOR instance ID (UUID) | 

### Return type

[**AFNORRoutingCodePost201Response**](AFNORRoutingCodePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**206** | Request processed without error, but the volume of information returned has been reduced. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put**
> AFNORRoutingCodePost201Response put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put(id_instance)

Completely update a private routing code.

Completely update a private routing code.

### Example


```python
import factpulse
from factpulse.models.afnor_routing_code_post201_response import AFNORRoutingCodePost201Response
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
    api_instance = factpulse.AFNORPDPPADirectoryServiceApi(api_client)
    id_instance = 'id_instance_example' # str | AFNOR instance ID (UUID)

    try:
        # Completely update a private routing code.
        api_response = api_instance.put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put(id_instance)
        print("The response of AFNORPDPPADirectoryServiceApi->put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AFNORPDPPADirectoryServiceApi->put_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_id_instance_id_instance_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_instance** | **str**| AFNOR instance ID (UUID) | 

### Return type

[**AFNORRoutingCodePost201Response**](AFNORRoutingCodePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**206** | Request processed without error, but the volume of information returned has been reduced. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_search_post**
> AFNORDirectoryLineSearchPost200Response search_directory_line_proxy_api_v1_afnor_directory_v1_directory_line_search_post()

Search for a directory line

Search for directory lines that meet all the criteria passed as parameters and return the results in the desired format.

### Example


```python
import factpulse
from factpulse.models.afnor_directory_line_search_post200_response import AFNORDirectoryLineSearchPost200Response
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

[**AFNORDirectoryLineSearchPost200Response**](AFNORDirectoryLineSearchPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns the directory line(s) matching the search criteria. |  -  |
**206** | Request processed without error, but the volume of information returned has been reduced. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_search_post**
> AFNORRoutingCodeSearchPost200Response search_routing_code_proxy_api_v1_afnor_directory_v1_routing_code_search_post()

Search for a routing code

Search for routing codes that meet all the criteria passed as parameters and return the routing codes in the desired format.

### Example


```python
import factpulse
from factpulse.models.afnor_routing_code_search_post200_response import AFNORRoutingCodeSearchPost200Response
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

[**AFNORRoutingCodeSearchPost200Response**](AFNORRoutingCodeSearchPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the routing code(s) matching the search criteria. |  -  |
**206** | Request processed without error, but the volume of information returned has been reduced. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_siren_proxy_api_v1_afnor_directory_v1_siren_search_post**
> AFNORSirenSearchPost200Response search_siren_proxy_api_v1_afnor_directory_v1_siren_search_post()

SIREN search (or legal unit)

Multi-criteria company search.

### Example


```python
import factpulse
from factpulse.models.afnor_siren_search_post200_response import AFNORSirenSearchPost200Response
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

[**AFNORSirenSearchPost200Response**](AFNORSirenSearchPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns one or more companies. |  -  |
**206** | Request processed without error, but the volume of information returned has been reduced. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_siret_proxy_api_v1_afnor_directory_v1_siret_search_post**
> AFNORSiretSearchPost200Response search_siret_proxy_api_v1_afnor_directory_v1_siret_search_post()

Search for a SIRET (facility)

Multi-criteria search for facilities.

### Example


```python
import factpulse
from factpulse.models.afnor_siret_search_post200_response import AFNORSiretSearchPost200Response
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

[**AFNORSiretSearchPost200Response**](AFNORSiretSearchPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an establishment as defined on a given observation date or as defined on the current date if the observation date is not specified. |  -  |
**206** | Request processed without error, but the volume of information returned has been reduced. |  -  |
**400** | Bad request. The request is invalid or cannot be completed. |  -  |
**401** | Unauthorized. The request requires user authentication. |  -  |
**403** | Forbidden. The server understood the request but denied access or access is not authorized. |  -  |
**404** | Not found. There is no resource at the given URI. |  -  |
**408** | Request timeout exceeded. |  -  |
**422** | Data validation error. |  -  |
**429** | The client has issued too many calls within a given time frame. |  -  |
**500** | Internal Server Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

