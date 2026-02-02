# factpulse.Flux6InvoiceLifecycleCDARApi

All URIs are relative to *https://factpulse.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_cdar_api_v1_cdar_generate_post**](Flux6InvoiceLifecycleCDARApi.md#generate_cdar_api_v1_cdar_generate_post) | **POST** /api/v1/cdar/generate | Generate a CDAR message
[**get_action_codes_api_v1_cdar_action_codes_get**](Flux6InvoiceLifecycleCDARApi.md#get_action_codes_api_v1_cdar_action_codes_get) | **GET** /api/v1/cdar/action-codes | List of CDAR action codes
[**get_reason_codes_api_v1_cdar_reason_codes_get**](Flux6InvoiceLifecycleCDARApi.md#get_reason_codes_api_v1_cdar_reason_codes_get) | **GET** /api/v1/cdar/reason-codes | List of CDAR reason codes
[**get_status_codes_api_v1_cdar_status_codes_get**](Flux6InvoiceLifecycleCDARApi.md#get_status_codes_api_v1_cdar_status_codes_get) | **GET** /api/v1/cdar/status-codes | List of CDAR status codes
[**submit_cdar_api_v1_cdar_submit_post**](Flux6InvoiceLifecycleCDARApi.md#submit_cdar_api_v1_cdar_submit_post) | **POST** /api/v1/cdar/submit | Generate and submit a CDAR message
[**submit_cdar_xml_api_v1_cdar_submit_xml_post**](Flux6InvoiceLifecycleCDARApi.md#submit_cdar_xml_api_v1_cdar_submit_xml_post) | **POST** /api/v1/cdar/submit-xml | Submit a pre-generated CDAR XML
[**submit_encaissee_api_v1_cdar_encaissee_post**](Flux6InvoiceLifecycleCDARApi.md#submit_encaissee_api_v1_cdar_encaissee_post) | **POST** /api/v1/cdar/encaissee | [Simplified] Submit PAID status (212) - Issued invoice
[**submit_refusee_api_v1_cdar_refusee_post**](Flux6InvoiceLifecycleCDARApi.md#submit_refusee_api_v1_cdar_refusee_post) | **POST** /api/v1/cdar/refusee | [Simplified] Submit REFUSED status (210) - Received invoice
[**validate_cdar_api_v1_cdar_validate_post**](Flux6InvoiceLifecycleCDARApi.md#validate_cdar_api_v1_cdar_validate_post) | **POST** /api/v1/cdar/validate | Validate CDAR structured data
[**validate_xml_cdar_api_v1_cdar_validate_xml_post**](Flux6InvoiceLifecycleCDARApi.md#validate_xml_cdar_api_v1_cdar_validate_xml_post) | **POST** /api/v1/cdar/validate-xml | Validate CDAR XML against XSD and Schematron BR-FR-CDV


# **generate_cdar_api_v1_cdar_generate_post**
> GenerateCDARResponse generate_cdar_api_v1_cdar_generate_post(create_cdar_request)

Generate a CDAR message

Generate a CDAR XML message (Cross Domain Acknowledgement and Response)
to communicate the status of an invoice.

**Message types:**
- **23** (Processing): Standard lifecycle message
- **305** (Transmission): Inter-platform transmission message

**Business rules:**
- BR-FR-CDV-14: Status 212 (PAID) requires a paid amount
- BR-FR-CDV-15: Statuses 206/207/208/210/213/501 require a reason code

### Example

* Api Key Authentication (APIKeyHeader):
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
    api_instance = factpulse.Flux6InvoiceLifecycleCDARApi(api_client)
    create_cdar_request = factpulse.CreateCDARRequest() # CreateCDARRequest | 

    try:
        # Generate a CDAR message
        api_response = api_instance.generate_cdar_api_v1_cdar_generate_post(create_cdar_request)
        print("The response of Flux6InvoiceLifecycleCDARApi->generate_cdar_api_v1_cdar_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux6InvoiceLifecycleCDARApi->generate_cdar_api_v1_cdar_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cdar_request** | [**CreateCDARRequest**](CreateCDARRequest.md)|  | 

### Return type

[**GenerateCDARResponse**](GenerateCDARResponse.md)

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
**422** | Validation error |  -  |
**500** | Server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_codes_api_v1_cdar_action_codes_get**
> ActionCodesResponse get_action_codes_api_v1_cdar_action_codes_get()

List of CDAR action codes

Returns the complete list of action codes (BR-FR-CDV-CL-10).

These codes indicate the requested action on the invoice.

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
    api_instance = factpulse.Flux6InvoiceLifecycleCDARApi(api_client)

    try:
        # List of CDAR action codes
        api_response = api_instance.get_action_codes_api_v1_cdar_action_codes_get()
        print("The response of Flux6InvoiceLifecycleCDARApi->get_action_codes_api_v1_cdar_action_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux6InvoiceLifecycleCDARApi->get_action_codes_api_v1_cdar_action_codes_get: %s\n" % e)
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
**400** | Invalid request |  -  |
**422** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reason_codes_api_v1_cdar_reason_codes_get**
> ReasonCodesResponse get_reason_codes_api_v1_cdar_reason_codes_get()

List of CDAR reason codes

Returns the complete list of status reason codes (BR-FR-CDV-CL-09).

These codes explain the reason for a particular status.

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
    api_instance = factpulse.Flux6InvoiceLifecycleCDARApi(api_client)

    try:
        # List of CDAR reason codes
        api_response = api_instance.get_reason_codes_api_v1_cdar_reason_codes_get()
        print("The response of Flux6InvoiceLifecycleCDARApi->get_reason_codes_api_v1_cdar_reason_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux6InvoiceLifecycleCDARApi->get_reason_codes_api_v1_cdar_reason_codes_get: %s\n" % e)
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
**400** | Invalid request |  -  |
**422** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_codes_api_v1_cdar_status_codes_get**
> StatusCodesResponse get_status_codes_api_v1_cdar_status_codes_get()

List of CDAR status codes

Returns the complete list of invoice status codes (BR-FR-CDV-CL-06).

These codes indicate the lifecycle state of an invoice.

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
    api_instance = factpulse.Flux6InvoiceLifecycleCDARApi(api_client)

    try:
        # List of CDAR status codes
        api_response = api_instance.get_status_codes_api_v1_cdar_status_codes_get()
        print("The response of Flux6InvoiceLifecycleCDARApi->get_status_codes_api_v1_cdar_status_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux6InvoiceLifecycleCDARApi->get_status_codes_api_v1_cdar_status_codes_get: %s\n" % e)
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
**400** | Invalid request |  -  |
**422** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_cdar_api_v1_cdar_submit_post**
> SubmitCDARResponse submit_cdar_api_v1_cdar_submit_post(submit_cdar_request)

Generate and submit a CDAR message

Generate a CDAR message and submit it to the PA/PDP platform.

**Authentication strategies:**
1. **JWT with client_uid** (recommended): PDP credentials retrieved from backend
2. **Zero-storage**: Provide pdpFlowServiceUrl, pdpClientId, pdpClientSecret in the request

**Flow types (flowType):**
- `CustomerInvoiceLC`: Client-side lifecycle (buyer)
- `SupplierInvoiceLC`: Supplier-side lifecycle (seller)

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.submit_cdar_request import SubmitCDARRequest
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
    api_instance = factpulse.Flux6InvoiceLifecycleCDARApi(api_client)
    submit_cdar_request = factpulse.SubmitCDARRequest() # SubmitCDARRequest | 

    try:
        # Generate and submit a CDAR message
        api_response = api_instance.submit_cdar_api_v1_cdar_submit_post(submit_cdar_request)
        print("The response of Flux6InvoiceLifecycleCDARApi->submit_cdar_api_v1_cdar_submit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux6InvoiceLifecycleCDARApi->submit_cdar_api_v1_cdar_submit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_cdar_request** | [**SubmitCDARRequest**](SubmitCDARRequest.md)|  | 

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
**400** | Invalid request |  -  |
**422** | Validation error |  -  |
**500** | Server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_cdar_xml_api_v1_cdar_submit_xml_post**
> SubmitCDARResponse submit_cdar_xml_api_v1_cdar_submit_xml_post(submit_cdarxml_request)

Submit a pre-generated CDAR XML

Submit a pre-generated CDAR XML message to the PA/PDP platform.

Useful for submitting XML generated by other systems.

**Validation:**
The XML is validated against XSD and Schematron BR-FR-CDV rules BEFORE submission.
Invalid XML will be rejected with detailed error messages.

**Authentication strategies:**
1. **JWT with client_uid** (recommended): PDP credentials retrieved from backend
2. **Zero-storage**: Provide pdpFlowServiceUrl, pdpClientId, pdpClientSecret in the request

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.submit_cdar_response import SubmitCDARResponse
from factpulse.models.submit_cdarxml_request import SubmitCDARXMLRequest
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
    api_instance = factpulse.Flux6InvoiceLifecycleCDARApi(api_client)
    submit_cdarxml_request = factpulse.SubmitCDARXMLRequest() # SubmitCDARXMLRequest | 

    try:
        # Submit a pre-generated CDAR XML
        api_response = api_instance.submit_cdar_xml_api_v1_cdar_submit_xml_post(submit_cdarxml_request)
        print("The response of Flux6InvoiceLifecycleCDARApi->submit_cdar_xml_api_v1_cdar_submit_xml_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux6InvoiceLifecycleCDARApi->submit_cdar_xml_api_v1_cdar_submit_xml_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_cdarxml_request** | [**SubmitCDARXMLRequest**](SubmitCDARXMLRequest.md)|  | 

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
**400** | Invalid request |  -  |
**422** | Validation error |  -  |
**500** | Server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_encaissee_api_v1_cdar_encaissee_post**
> SimplifiedCDARResponse submit_encaissee_api_v1_cdar_encaissee_post(encaissee_request)

[Simplified] Submit PAID status (212) - Issued invoice

**Simplified endpoint for OD** - Submit a PAID status (212) for an **ISSUED** invoice.

This status is **mandatory for PPF** (BR-FR-CDV-14 requires the paid amount).

**Use case:** The **seller** confirms payment receipt for an invoice they issued.

**Who issues this status?**
- **Issuer (IssuerTradeParty):** The seller (SE = Seller) who received payment
- **Recipient (RecipientTradeParty):** The buyer (BY = Buyer) who paid

**Reference:** XP Z12-014 Annex B, example UC1_F202500003_07-CDV-212_Encaissee.xml

**Authentication:** JWT Bearer (recommended) or PDP credentials in request.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.encaissee_request import EncaisseeRequest
from factpulse.models.simplified_cdar_response import SimplifiedCDARResponse
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
    api_instance = factpulse.Flux6InvoiceLifecycleCDARApi(api_client)
    encaissee_request = factpulse.EncaisseeRequest() # EncaisseeRequest | 

    try:
        # [Simplified] Submit PAID status (212) - Issued invoice
        api_response = api_instance.submit_encaissee_api_v1_cdar_encaissee_post(encaissee_request)
        print("The response of Flux6InvoiceLifecycleCDARApi->submit_encaissee_api_v1_cdar_encaissee_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux6InvoiceLifecycleCDARApi->submit_encaissee_api_v1_cdar_encaissee_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encaissee_request** | [**EncaisseeRequest**](EncaisseeRequest.md)|  | 

### Return type

[**SimplifiedCDARResponse**](SimplifiedCDARResponse.md)

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
**422** | Validation error |  -  |
**500** | Server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_refusee_api_v1_cdar_refusee_post**
> SimplifiedCDARResponse submit_refusee_api_v1_cdar_refusee_post(refusee_request)

[Simplified] Submit REFUSED status (210) - Received invoice

**Simplified endpoint for OD** - Submit a REFUSED status (210) for a **RECEIVED** invoice.

This status is **mandatory for PPF** (BR-FR-CDV-15 requires a reason code).

**Use case:** The **buyer** refuses an invoice they received.

**Who issues this status?**
- **Issuer (IssuerTradeParty):** The buyer (BY = Buyer) refusing the invoice
- **Recipient (RecipientTradeParty):** The seller (SE = Seller) who issued the invoice

**Reference:** XP Z12-014 Annex B, example UC3_F202500005_04-CDV-210_Refusee.xml

**Allowed reason codes (BR-FR-CDV-CL-09):**
- `TX_TVA_ERR`: Incorrect VAT rate
- `MONTANTTOTAL_ERR`: Incorrect total amount
- `CALCUL_ERR`: Calculation error
- `NON_CONFORME`: Non-compliant
- `DOUBLON`: Duplicate
- `DEST_ERR`: Wrong recipient
- `TRANSAC_INC`: Incomplete transaction
- `EMMET_INC`: Unknown issuer
- `CONTRAT_TERM`: Contract terminated
- `DOUBLE_FACT`: Double billing
- `CMD_ERR`: Order error
- `ADR_ERR`: Address error
- `REF_CT_ABSENT`: Missing contract reference

**Authentication:** JWT Bearer (recommended) or PDP credentials in request.

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.refusee_request import RefuseeRequest
from factpulse.models.simplified_cdar_response import SimplifiedCDARResponse
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
    api_instance = factpulse.Flux6InvoiceLifecycleCDARApi(api_client)
    refusee_request = factpulse.RefuseeRequest() # RefuseeRequest | 

    try:
        # [Simplified] Submit REFUSED status (210) - Received invoice
        api_response = api_instance.submit_refusee_api_v1_cdar_refusee_post(refusee_request)
        print("The response of Flux6InvoiceLifecycleCDARApi->submit_refusee_api_v1_cdar_refusee_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux6InvoiceLifecycleCDARApi->submit_refusee_api_v1_cdar_refusee_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refusee_request** | [**RefuseeRequest**](RefuseeRequest.md)|  | 

### Return type

[**SimplifiedCDARResponse**](SimplifiedCDARResponse.md)

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
**422** | Validation error |  -  |
**500** | Server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_cdar_api_v1_cdar_validate_post**
> ValidateCDARResponse validate_cdar_api_v1_cdar_validate_post(validate_cdar_request)

Validate CDAR structured data

Validate CDAR structured data without generating XML.

**Note:** This endpoint validates structured data fields only.
Use `/validate-xml` to validate a pre-generated CDAR XML file against XSD and Schematron.

Checks:
- Field formats (SIREN, dates, etc.)
- Enum codes (status, reason, action)
- Business rules BR-FR-CDV-*

### Example

* Api Key Authentication (APIKeyHeader):
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
    api_instance = factpulse.Flux6InvoiceLifecycleCDARApi(api_client)
    validate_cdar_request = factpulse.ValidateCDARRequest() # ValidateCDARRequest | 

    try:
        # Validate CDAR structured data
        api_response = api_instance.validate_cdar_api_v1_cdar_validate_post(validate_cdar_request)
        print("The response of Flux6InvoiceLifecycleCDARApi->validate_cdar_api_v1_cdar_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux6InvoiceLifecycleCDARApi->validate_cdar_api_v1_cdar_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_cdar_request** | [**ValidateCDARRequest**](ValidateCDARRequest.md)|  | 

### Return type

[**ValidateCDARResponse**](ValidateCDARResponse.md)

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
**422** | Validation error |  -  |
**500** | Server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_xml_cdar_api_v1_cdar_validate_xml_post**
> Dict[str, object] validate_xml_cdar_api_v1_cdar_validate_xml_post(xml_file)

Validate CDAR XML against XSD and Schematron BR-FR-CDV

Validates a CDAR XML file against:

1. **XSD schema**: UN/CEFACT D22B CrossDomainAcknowledgementAndResponse
2. **Schematron BR-FR-CDV**: French business rules for invoice lifecycle

Returns validation status and detailed error messages if invalid.

**Note:** Use `/validate` to validate structured data fields (JSON).

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
    api_instance = factpulse.Flux6InvoiceLifecycleCDARApi(api_client)
    xml_file = None # bytearray | CDAR XML file to validate

    try:
        # Validate CDAR XML against XSD and Schematron BR-FR-CDV
        api_response = api_instance.validate_xml_cdar_api_v1_cdar_validate_xml_post(xml_file)
        print("The response of Flux6InvoiceLifecycleCDARApi->validate_xml_cdar_api_v1_cdar_validate_xml_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Flux6InvoiceLifecycleCDARApi->validate_xml_cdar_api_v1_cdar_validate_xml_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xml_file** | **bytearray**| CDAR XML file to validate | 

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
**400** | Invalid request |  -  |
**422** | Validation error |  -  |
**500** | Server error |  -  |
**401** | Authentication required - Invalid or missing JWT token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

