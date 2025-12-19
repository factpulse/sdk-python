# factpulse.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_info_api_v1_me_get**](UserApi.md#get_user_info_api_v1_me_get) | **GET** /api/v1/me | Get current user information


# **get_user_info_api_v1_me_get**
> object get_user_info_api_v1_me_get()

Get current user information

Returns information about the authenticated user.

This endpoint allows you to:
- Verify that authentication works
- Get connected account details
- Test JWT token validity
- Check your consumption quota

**Requires valid authentication.**

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
    api_instance = factpulse.UserApi(api_client)

    try:
        # Get current user information
        api_response = api_instance.get_user_info_api_v1_me_get()
        print("The response of UserApi->get_user_info_api_v1_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_info_api_v1_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | User information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

