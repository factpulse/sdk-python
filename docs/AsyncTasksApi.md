# factpulse.AsyncTasksApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task_status_api_v1_processing_tasks_task_id_status_get**](AsyncTasksApi.md#get_task_status_api_v1_processing_tasks_task_id_status_get) | **GET** /api/v1/processing/tasks/{task_id}/status | Get task generation status


# **get_task_status_api_v1_processing_tasks_task_id_status_get**
> AsyncTaskStatus get_task_status_api_v1_processing_tasks_task_id_status_get(task_id)

Get task generation status

Retrieves the progress status of an invoice generation task.

## Possible states

The `status` field uses the `CeleryStatus` enum with values:
- **PENDING, STARTED, SUCCESS, FAILURE, RETRY**

See the `CeleryStatus` schema documentation for details.

## Business result

When `status="SUCCESS"`, the `result` field contains:
- `status`: "SUCCESS" or "ERROR" (business result)
- `content_b64`: Base64 encoded content (if success)
- `errorCode`, `errorMessage`, `details`: AFNOR format (if business error)

## Usage

Poll this endpoint every 2-3 seconds until
`status` is `SUCCESS` or `FAILURE`.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.async_task_status import AsyncTaskStatus
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
    api_instance = factpulse.AsyncTasksApi(api_client)
    task_id = 'task_id_example' # str | Celery task ID returned by async endpoints (UUID format)

    try:
        # Get task generation status
        api_response = api_instance.get_task_status_api_v1_processing_tasks_task_id_status_get(task_id)
        print("The response of AsyncTasksApi->get_task_status_api_v1_processing_tasks_task_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsyncTasksApi->get_task_status_api_v1_processing_tasks_task_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Celery task ID returned by async endpoints (UUID format) | 

### Return type

[**AsyncTaskStatus**](AsyncTaskStatus.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current task state |  -  |
**422** | Validation Error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

