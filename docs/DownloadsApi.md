# factpulse.DownloadsApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_file_api_v1_download_download_id_head**](DownloadsApi.md#check_file_api_v1_download_download_id_head) | **HEAD** /api/v1/download/{download_id} | Check if a file exists
[**check_file_api_v1_download_download_id_head_0**](DownloadsApi.md#check_file_api_v1_download_download_id_head_0) | **HEAD** /api/v1/download/{download_id} | Check if a file exists
[**download_file_api_v1_download_download_id_get**](DownloadsApi.md#download_file_api_v1_download_download_id_get) | **GET** /api/v1/download/{download_id} | Download a temporary file
[**download_file_api_v1_download_download_id_get_0**](DownloadsApi.md#download_file_api_v1_download_download_id_get_0) | **GET** /api/v1/download/{download_id} | Download a temporary file


# **check_file_api_v1_download_download_id_head**
> object check_file_api_v1_download_download_id_head(download_id)

Check if a file exists

Check if a temporary file exists and get its metadata without downloading.

Useful for:
- Verifying a download URL is still valid
- Getting file size before downloading
- Checking expiration time

**Security**: Requires authentication, only file owner can check.

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
    api_instance = factpulse.DownloadsApi(api_client)
    download_id = 'download_id_example' # str | 

    try:
        # Check if a file exists
        api_response = api_instance.check_file_api_v1_download_download_id_head(download_id)
        print("The response of DownloadsApi->check_file_api_v1_download_download_id_head:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadsApi->check_file_api_v1_download_download_id_head: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**|  | 

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
**200** | File exists |  -  |
**401** | Authentication required |  -  |
**403** | Access denied |  -  |
**404** | File not found or expired |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_file_api_v1_download_download_id_head_0**
> object check_file_api_v1_download_download_id_head_0(download_id)

Check if a file exists

Check if a temporary file exists and get its metadata without downloading.

Useful for:
- Verifying a download URL is still valid
- Getting file size before downloading
- Checking expiration time

**Security**: Requires authentication, only file owner can check.

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
    api_instance = factpulse.DownloadsApi(api_client)
    download_id = 'download_id_example' # str | 

    try:
        # Check if a file exists
        api_response = api_instance.check_file_api_v1_download_download_id_head_0(download_id)
        print("The response of DownloadsApi->check_file_api_v1_download_download_id_head_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadsApi->check_file_api_v1_download_download_id_head_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**|  | 

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
**200** | File exists |  -  |
**401** | Authentication required |  -  |
**403** | Access denied |  -  |
**404** | File not found or expired |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_api_v1_download_download_id_get**
> object download_file_api_v1_download_download_id_get(download_id, delete_after=delete_after)

Download a temporary file

Download a file stored temporarily after asynchronous processing.

**Usage**:
- This URL is provided in webhook notifications when using `webhook_mode: "download_url"`
- Files are automatically deleted after 1 hour
- Each file can only be downloaded until it expires

**Security**:
- Requires a valid JWT token
- Only the user who initiated the task can download the file

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
    api_instance = factpulse.DownloadsApi(api_client)
    download_id = 'download_id_example' # str | 
    delete_after = False # bool | If true, delete the file after download (one-time download) (optional) (default to False)

    try:
        # Download a temporary file
        api_response = api_instance.download_file_api_v1_download_download_id_get(download_id, delete_after=delete_after)
        print("The response of DownloadsApi->download_file_api_v1_download_download_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadsApi->download_file_api_v1_download_download_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**|  | 
 **delete_after** | **bool**| If true, delete the file after download (one-time download) | [optional] [default to False]

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf, application/xml, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File content |  -  |
**401** | Authentication required |  -  |
**403** | Access denied - file belongs to another user |  -  |
**404** | File not found or expired |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_api_v1_download_download_id_get_0**
> object download_file_api_v1_download_download_id_get_0(download_id, delete_after=delete_after)

Download a temporary file

Download a file stored temporarily after asynchronous processing.

**Usage**:
- This URL is provided in webhook notifications when using `webhook_mode: "download_url"`
- Files are automatically deleted after 1 hour
- Each file can only be downloaded until it expires

**Security**:
- Requires a valid JWT token
- Only the user who initiated the task can download the file

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
    api_instance = factpulse.DownloadsApi(api_client)
    download_id = 'download_id_example' # str | 
    delete_after = False # bool | If true, delete the file after download (one-time download) (optional) (default to False)

    try:
        # Download a temporary file
        api_response = api_instance.download_file_api_v1_download_download_id_get_0(download_id, delete_after=delete_after)
        print("The response of DownloadsApi->download_file_api_v1_download_download_id_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadsApi->download_file_api_v1_download_download_id_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**|  | 
 **delete_after** | **bool**| If true, delete the file after download (one-time download) | [optional] [default to False]

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf, application/xml, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File content |  -  |
**401** | Authentication required |  -  |
**403** | Access denied - file belongs to another user |  -  |
**404** | File not found or expired |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

