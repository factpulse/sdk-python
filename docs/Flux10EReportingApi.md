# factpulse.Flux10EReportingApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_aggregated_ereporting_api_v1_ereporting_generate_aggregated_post**](Flux10EReportingApi.md#generate_aggregated_ereporting_api_v1_ereporting_generate_aggregated_post) | **POST** /api/v1/ereporting/generate-aggregated | Generate aggregated e-reporting XML (PPF-compliant)
[**generate_ereporting_api_v1_ereporting_generate_post**](Flux10EReportingApi.md#generate_ereporting_api_v1_ereporting_generate_post) | **POST** /api/v1/ereporting/generate | Generate e-reporting XML
[**generate_ereporting_download_api_v1_ereporting_generate_download_post**](Flux10EReportingApi.md#generate_ereporting_download_api_v1_ereporting_generate_download_post) | **POST** /api/v1/ereporting/generate/download | Generate and download e-reporting XML
[**list_category_codes_api_v1_ereporting_category_codes_get**](Flux10EReportingApi.md#list_category_codes_api_v1_ereporting_category_codes_get) | **GET** /api/v1/ereporting/category-codes | List PPF-compliant category codes
[**list_flow_types_api_v1_ereporting_flow_types_get**](Flux10EReportingApi.md#list_flow_types_api_v1_ereporting_flow_types_get) | **GET** /api/v1/ereporting/flow-types | List available flow types
[**submit_aggregated_ereporting_api_v1_ereporting_submit_aggregated_post**](Flux10EReportingApi.md#submit_aggregated_ereporting_api_v1_ereporting_submit_aggregated_post) | **POST** /api/v1/ereporting/submit-aggregated | Submit aggregated e-reporting to PA/PDP
[**submit_ereporting_api_v1_ereporting_submit_post**](Flux10EReportingApi.md#submit_ereporting_api_v1_ereporting_submit_post) | **POST** /api/v1/ereporting/submit | Submit e-reporting to PA/PDP
[**submit_xml_ereporting_api_v1_ereporting_submit_xml_post**](Flux10EReportingApi.md#submit_xml_ereporting_api_v1_ereporting_submit_xml_post) | **POST** /api/v1/ereporting/submit-xml | Submit pre-generated e-reporting XML
[**validate_aggregated_ereporting_api_v1_ereporting_validate_aggregated_post**](Flux10EReportingApi.md#validate_aggregated_ereporting_api_v1_ereporting_validate_aggregated_post) | **POST** /api/v1/ereporting/validate-aggregated | Validate aggregated e-reporting data
[**validate_ereporting_api_v1_ereporting_validate_post**](Flux10EReportingApi.md#validate_ereporting_api_v1_ereporting_validate_post) | **POST** /api/v1/ereporting/validate | Validate e-reporting data
[**validate_xml_ereporting_api_v1_ereporting_validate_xml_post**](Flux10EReportingApi.md#validate_xml_ereporting_api_v1_ereporting_validate_xml_post) | **POST** /api/v1/ereporting/validate-xml | Validate e-reporting XML (PPF Annexe 6 v1.9 compliant)


# **generate_aggregated_ereporting_api_v1_ereporting_generate_aggregated_post**
> GenerateAggregatedReportResponse generate_aggregated_ereporting_api_v1_ereporting_generate_aggregated_post(create_aggregated_report_request)

Generate aggregated e-reporting XML (PPF-compliant)

Generate a PPF-compliant aggregated e-reporting XML containing multiple flux types in a single file.

This endpoint creates a Report XML that can contain:
- **TransactionsReport**: Invoice (10.1) AND/OR Transactions (10.3)
- **PaymentsReport**: Invoice payments (10.2) AND/OR Transaction payments (10.4)

The AFNOR FlowType is automatically determined based on content:
- Single type → Specific FlowType (e.g., AggregatedCustomerTransactionReport)
- Multiple types → MultiFlowReport

**CategoryCode (TT-81)** must use PPF-compliant values:
- TLB1: Goods deliveries
- TPS1: Service provisions
- TNT1: Non-taxed transactions
- TMA1: Mixed transactions

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.create_aggregated_report_request import CreateAggregatedReportRequest
from factpulse.models.generate_aggregated_report_response import GenerateAggregatedReportResponse
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
    api_instance = factpulse.Flux10EReportingApi(api_client)
    create_aggregated_report_request = factpulse.CreateAggregatedReportRequest() # CreateAggregatedReportRequest | 

    try:
        # Generate aggregated e-reporting XML (PPF-compliant)
        api_response = api_instance.generate_aggregated_ereporting_api_v1_ereporting_generate_aggregated_post(create_aggregated_report_request)
        print("The response of Flux10EReportingApi->generate_aggregated_ereporting_api_v1_ereporting_generate_aggregated_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux10EReportingApi->generate_aggregated_ereporting_api_v1_ereporting_generate_aggregated_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_aggregated_report_request** | [**CreateAggregatedReportRequest**](CreateAggregatedReportRequest.md)|  | 

### Return type

[**GenerateAggregatedReportResponse**](GenerateAggregatedReportResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request data |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_ereporting_api_v1_ereporting_generate_post**
> GenerateEReportingResponse generate_ereporting_api_v1_ereporting_generate_post(create_e_reporting_request)

Generate e-reporting XML

Generate e-reporting XML (FRR format) from structured data.

Supports all four flow types:
- **10.1**: Unitary B2B international transactions (use `invoices` field)
- **10.2**: Payments for B2B international invoices (use `invoicePayments` field)
- **10.3**: Aggregated B2C transactions (use `transactions` field)
- **10.4**: Aggregated B2C payments (use `aggregatedPayments` field)

The generated XML is compliant with DGFIP specifications and ready
for submission to a PA (Plateforme Agréée).

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.create_e_reporting_request import CreateEReportingRequest
from factpulse.models.generate_e_reporting_response import GenerateEReportingResponse
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
    api_instance = factpulse.Flux10EReportingApi(api_client)
    create_e_reporting_request = factpulse.CreateEReportingRequest() # CreateEReportingRequest | 

    try:
        # Generate e-reporting XML
        api_response = api_instance.generate_ereporting_api_v1_ereporting_generate_post(create_e_reporting_request)
        print("The response of Flux10EReportingApi->generate_ereporting_api_v1_ereporting_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux10EReportingApi->generate_ereporting_api_v1_ereporting_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_e_reporting_request** | [**CreateEReportingRequest**](CreateEReportingRequest.md)|  | 

### Return type

[**GenerateEReportingResponse**](GenerateEReportingResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request data |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_ereporting_download_api_v1_ereporting_generate_download_post**
> generate_ereporting_download_api_v1_ereporting_generate_download_post(create_e_reporting_request, filename=filename)

Generate and download e-reporting XML

Generate e-reporting XML and return as downloadable file.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.create_e_reporting_request import CreateEReportingRequest
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
    api_instance = factpulse.Flux10EReportingApi(api_client)
    create_e_reporting_request = factpulse.CreateEReportingRequest() # CreateEReportingRequest | 
    filename = 'filename_example' # str | Output filename (default: ereporting_{reportId}.xml) (optional)

    try:
        # Generate and download e-reporting XML
        api_instance.generate_ereporting_download_api_v1_ereporting_generate_download_post(create_e_reporting_request, filename=filename)
    except Exception as e:
        print("Exception when calling Flux10EReportingApi->generate_ereporting_download_api_v1_ereporting_generate_download_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_e_reporting_request** | [**CreateEReportingRequest**](CreateEReportingRequest.md)|  | 
 **filename** | **str**| Output filename (default: ereporting_{reportId}.xml) | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request data |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_category_codes_api_v1_ereporting_category_codes_get**
> Dict[str, object] list_category_codes_api_v1_ereporting_category_codes_get()

List PPF-compliant category codes

Returns the list of valid CategoryCode values (TT-81) for e-reporting transactions.

Source: Annexe 6 - Format sémantique FE e-reporting v1.9

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
    api_instance = factpulse.Flux10EReportingApi(api_client)

    try:
        # List PPF-compliant category codes
        api_response = api_instance.list_category_codes_api_v1_ereporting_category_codes_get()
        print("The response of Flux10EReportingApi->list_category_codes_api_v1_ereporting_category_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux10EReportingApi->list_category_codes_api_v1_ereporting_category_codes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request data |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_flow_types_api_v1_ereporting_flow_types_get**
> Dict[str, object] list_flow_types_api_v1_ereporting_flow_types_get()

List available flow types

Returns the list of supported e-reporting flow types with descriptions.

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
    api_instance = factpulse.Flux10EReportingApi(api_client)

    try:
        # List available flow types
        api_response = api_instance.list_flow_types_api_v1_ereporting_flow_types_get()
        print("The response of Flux10EReportingApi->list_flow_types_api_v1_ereporting_flow_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux10EReportingApi->list_flow_types_api_v1_ereporting_flow_types_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request data |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_aggregated_ereporting_api_v1_ereporting_submit_aggregated_post**
> SubmitEReportingResponse submit_aggregated_ereporting_api_v1_ereporting_submit_aggregated_post(submit_aggregated_report_request)

Submit aggregated e-reporting to PA/PDP

Generate and submit a PPF-compliant aggregated e-reporting to a PA/PDP.

Combines generation and submission in a single call.
Automatically determines the AFNOR FlowType based on content.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.submit_aggregated_report_request import SubmitAggregatedReportRequest
from factpulse.models.submit_e_reporting_response import SubmitEReportingResponse
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
    api_instance = factpulse.Flux10EReportingApi(api_client)
    submit_aggregated_report_request = factpulse.SubmitAggregatedReportRequest() # SubmitAggregatedReportRequest | 

    try:
        # Submit aggregated e-reporting to PA/PDP
        api_response = api_instance.submit_aggregated_ereporting_api_v1_ereporting_submit_aggregated_post(submit_aggregated_report_request)
        print("The response of Flux10EReportingApi->submit_aggregated_ereporting_api_v1_ereporting_submit_aggregated_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux10EReportingApi->submit_aggregated_ereporting_api_v1_ereporting_submit_aggregated_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_aggregated_report_request** | [**SubmitAggregatedReportRequest**](SubmitAggregatedReportRequest.md)|  | 

### Return type

[**SubmitEReportingResponse**](SubmitEReportingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request data |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_ereporting_api_v1_ereporting_submit_post**
> SubmitEReportingResponse submit_ereporting_api_v1_ereporting_submit_post(submit_e_reporting_request)

Submit e-reporting to PA/PDP

Generate and submit e-reporting to a PA (Plateforme Agréée).

Authentication strategies (same as invoices):
1. **JWT with client_uid** (recommended): PDP credentials fetched from backend
2. **Zero-storage**: Provide pdpFlowServiceUrl, pdpClientId, pdpClientSecret in request

The e-reporting is submitted using the AFNOR Flow Service API
with syntax=FRR (FRench Reporting).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.submit_e_reporting_request import SubmitEReportingRequest
from factpulse.models.submit_e_reporting_response import SubmitEReportingResponse
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
    api_instance = factpulse.Flux10EReportingApi(api_client)
    submit_e_reporting_request = factpulse.SubmitEReportingRequest() # SubmitEReportingRequest | 

    try:
        # Submit e-reporting to PA/PDP
        api_response = api_instance.submit_ereporting_api_v1_ereporting_submit_post(submit_e_reporting_request)
        print("The response of Flux10EReportingApi->submit_ereporting_api_v1_ereporting_submit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux10EReportingApi->submit_ereporting_api_v1_ereporting_submit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_e_reporting_request** | [**SubmitEReportingRequest**](SubmitEReportingRequest.md)|  | 

### Return type

[**SubmitEReportingResponse**](SubmitEReportingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request data |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_xml_ereporting_api_v1_ereporting_submit_xml_post**
> SubmitEReportingResponse submit_xml_ereporting_api_v1_ereporting_submit_xml_post(xml_file, tracking_id=tracking_id, skip_validation=skip_validation, pdp_flow_service_url=pdp_flow_service_url, pdp_token_url=pdp_token_url, pdp_client_id=pdp_client_id, pdp_client_secret=pdp_client_secret)

Submit pre-generated e-reporting XML

Submit a pre-generated e-reporting XML file directly to a PA/PDP.

This endpoint is designed for clients who generate their own PPF-compliant XML
and only need FactPulse for the PDP submission.

**Process:**
1. Validates the XML against PPF XSD schemas
2. Determines the appropriate AFNOR FlowType
3. Submits to the configured PDP/PA
4. Returns the flowId for tracking

**Authentication:** Same strategies as /submit endpoint (JWT or zero-storage credentials).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.submit_e_reporting_response import SubmitEReportingResponse
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
    api_instance = factpulse.Flux10EReportingApi(api_client)
    xml_file = None # bytearray | E-reporting XML file
    tracking_id = 'tracking_id_example' # str |  (optional)
    skip_validation = False # bool | Skip XSD validation (optional) (default to False)
    pdp_flow_service_url = 'pdp_flow_service_url_example' # str |  (optional)
    pdp_token_url = 'pdp_token_url_example' # str |  (optional)
    pdp_client_id = 'pdp_client_id_example' # str |  (optional)
    pdp_client_secret = 'pdp_client_secret_example' # str |  (optional)

    try:
        # Submit pre-generated e-reporting XML
        api_response = api_instance.submit_xml_ereporting_api_v1_ereporting_submit_xml_post(xml_file, tracking_id=tracking_id, skip_validation=skip_validation, pdp_flow_service_url=pdp_flow_service_url, pdp_token_url=pdp_token_url, pdp_client_id=pdp_client_id, pdp_client_secret=pdp_client_secret)
        print("The response of Flux10EReportingApi->submit_xml_ereporting_api_v1_ereporting_submit_xml_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux10EReportingApi->submit_xml_ereporting_api_v1_ereporting_submit_xml_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xml_file** | **bytearray**| E-reporting XML file | 
 **tracking_id** | **str**|  | [optional] 
 **skip_validation** | **bool**| Skip XSD validation | [optional] [default to False]
 **pdp_flow_service_url** | **str**|  | [optional] 
 **pdp_token_url** | **str**|  | [optional] 
 **pdp_client_id** | **str**|  | [optional] 
 **pdp_client_secret** | **str**|  | [optional] 

### Return type

[**SubmitEReportingResponse**](SubmitEReportingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request data |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_aggregated_ereporting_api_v1_ereporting_validate_aggregated_post**
> Dict[str, object] validate_aggregated_ereporting_api_v1_ereporting_validate_aggregated_post(create_aggregated_report_request)

Validate aggregated e-reporting data

Validates aggregated e-reporting data without generating XML.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.create_aggregated_report_request import CreateAggregatedReportRequest
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
    api_instance = factpulse.Flux10EReportingApi(api_client)
    create_aggregated_report_request = factpulse.CreateAggregatedReportRequest() # CreateAggregatedReportRequest | 

    try:
        # Validate aggregated e-reporting data
        api_response = api_instance.validate_aggregated_ereporting_api_v1_ereporting_validate_aggregated_post(create_aggregated_report_request)
        print("The response of Flux10EReportingApi->validate_aggregated_ereporting_api_v1_ereporting_validate_aggregated_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux10EReportingApi->validate_aggregated_ereporting_api_v1_ereporting_validate_aggregated_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_aggregated_report_request** | [**CreateAggregatedReportRequest**](CreateAggregatedReportRequest.md)|  | 

### Return type

**Dict[str, object]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request data |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_ereporting_api_v1_ereporting_validate_post**
> ValidateEReportingResponse validate_ereporting_api_v1_ereporting_validate_post(validate_e_reporting_request)

Validate e-reporting data

Validate e-reporting data without generating or submitting.

Performs:
- Schema validation
- Business rule validation (correct flux type vs data)
- Data consistency checks (tax totals, dates, etc.)

Returns validation errors and warnings.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.validate_e_reporting_request import ValidateEReportingRequest
from factpulse.models.validate_e_reporting_response import ValidateEReportingResponse
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
    api_instance = factpulse.Flux10EReportingApi(api_client)
    validate_e_reporting_request = factpulse.ValidateEReportingRequest() # ValidateEReportingRequest | 

    try:
        # Validate e-reporting data
        api_response = api_instance.validate_ereporting_api_v1_ereporting_validate_post(validate_e_reporting_request)
        print("The response of Flux10EReportingApi->validate_ereporting_api_v1_ereporting_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux10EReportingApi->validate_ereporting_api_v1_ereporting_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_e_reporting_request** | [**ValidateEReportingRequest**](ValidateEReportingRequest.md)|  | 

### Return type

[**ValidateEReportingResponse**](ValidateEReportingResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request data |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_xml_ereporting_api_v1_ereporting_validate_xml_post**
> Dict[str, object] validate_xml_ereporting_api_v1_ereporting_validate_xml_post(xml_file, validate_coherence=validate_coherence, validate_period=validate_period)

Validate e-reporting XML (PPF Annexe 6 v1.9 compliant)

Validates an e-reporting XML file against PPF specifications (Annexe 6 v1.9):

**Validation levels:**
1. **XSD (REJ_SEMAN)**: Structure, types, cardinality
2. **Semantic (REJ_SEMAN)**: Authorized values from codelists
3. **Coherence (REJ_COH)**: Data consistency (totals = sum of breakdowns)
4. **Period (REJ_PER)**: Transaction dates within declared period

**Validated codes:**
- SchemeID (ISO 6523): 0002=SIREN, 0009=SIRET, 0224=RoutingCode, etc.
- RoleCode (UNCL 3035): SE=Seller, BY=Buyer, WK=Working party
- CategoryCode (TT-81): TLB1, TPS1, TNT1, TMA1
- TaxCategoryCode (UNTDID 5305): S, Z, E, AE, K, G, O
- Currency (ISO 4217), Country (ISO 3166-1)

Returns structured validation errors with PPF rejection codes.

### Example

* Api Key Authentication (APIKeyHeader):
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
    api_instance = factpulse.Flux10EReportingApi(api_client)
    xml_file = None # bytearray | E-reporting XML file to validate
    validate_coherence = True # bool | Validate data coherence (REJ_COH) (optional) (default to True)
    validate_period = True # bool | Validate period coherence (REJ_PER) (optional) (default to True)

    try:
        # Validate e-reporting XML (PPF Annexe 6 v1.9 compliant)
        api_response = api_instance.validate_xml_ereporting_api_v1_ereporting_validate_xml_post(xml_file, validate_coherence=validate_coherence, validate_period=validate_period)
        print("The response of Flux10EReportingApi->validate_xml_ereporting_api_v1_ereporting_validate_xml_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux10EReportingApi->validate_xml_ereporting_api_v1_ereporting_validate_xml_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xml_file** | **bytearray**| E-reporting XML file to validate | 
 **validate_coherence** | **bool**| Validate data coherence (REJ_COH) | [optional] [default to True]
 **validate_period** | **bool**| Validate period coherence (REJ_PER) | [optional] [default to True]

### Return type

**Dict[str, object]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid request data |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

