# factpulse.PDFXMLVerificationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_verification_status_api_v1_verification_verify_async_task_id_status_get**](PDFXMLVerificationApi.md#get_verification_status_api_v1_verification_verify_async_task_id_status_get) | **GET** /api/v1/verification/verify-async/{task_id}/status | Get status of an asynchronous verification
[**get_verification_status_api_v1_verification_verify_async_task_id_status_get_0**](PDFXMLVerificationApi.md#get_verification_status_api_v1_verification_verify_async_task_id_status_get_0) | **GET** /api/v1/verification/verify-async/{task_id}/status | Get status of an asynchronous verification
[**verify_pdf_async_api_v1_verification_verify_async_post**](PDFXMLVerificationApi.md#verify_pdf_async_api_v1_verification_verify_async_post) | **POST** /api/v1/verification/verify-async | Verify PDF/XML Factur-X compliance (asynchronous)
[**verify_pdf_async_api_v1_verification_verify_async_post_0**](PDFXMLVerificationApi.md#verify_pdf_async_api_v1_verification_verify_async_post_0) | **POST** /api/v1/verification/verify-async | Verify PDF/XML Factur-X compliance (asynchronous)
[**verify_pdf_sync_api_v1_verification_verify_post**](PDFXMLVerificationApi.md#verify_pdf_sync_api_v1_verification_verify_post) | **POST** /api/v1/verification/verify | Verify PDF/XML Factur-X compliance (synchronous)
[**verify_pdf_sync_api_v1_verification_verify_post_0**](PDFXMLVerificationApi.md#verify_pdf_sync_api_v1_verification_verify_post_0) | **POST** /api/v1/verification/verify | Verify PDF/XML Factur-X compliance (synchronous)


# **get_verification_status_api_v1_verification_verify_async_task_id_status_get**
> AsyncTaskStatus get_verification_status_api_v1_verification_verify_async_task_id_status_get(task_id)

Get status of an asynchronous verification

Retrieves the status and result of an asynchronous verification task.

**Possible statuses:**
- `PENDING`: Task waiting in queue
- `STARTED`: Task currently running
- `SUCCESS`: Task completed successfully (see `result`)
- `FAILURE`: System error (unhandled exception)

**Note:** The `result.status` field can be "SUCCESS" or "ERROR"
independently of Celery status (which will always be SUCCESS if the task ran).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.async_task_status import AsyncTaskStatus
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
    api_instance = factpulse.PDFXMLVerificationApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Get status of an asynchronous verification
        api_response = api_instance.get_verification_status_api_v1_verification_verify_async_task_id_status_get(task_id)
        print("The response of PDFXMLVerificationApi->get_verification_status_api_v1_verification_verify_async_task_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFXMLVerificationApi->get_verification_status_api_v1_verification_verify_async_task_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verification_status_api_v1_verification_verify_async_task_id_status_get_0**
> AsyncTaskStatus get_verification_status_api_v1_verification_verify_async_task_id_status_get_0(task_id)

Get status of an asynchronous verification

Retrieves the status and result of an asynchronous verification task.

**Possible statuses:**
- `PENDING`: Task waiting in queue
- `STARTED`: Task currently running
- `SUCCESS`: Task completed successfully (see `result`)
- `FAILURE`: System error (unhandled exception)

**Note:** The `result.status` field can be "SUCCESS" or "ERROR"
independently of Celery status (which will always be SUCCESS if the task ran).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.async_task_status import AsyncTaskStatus
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
    api_instance = factpulse.PDFXMLVerificationApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Get status of an asynchronous verification
        api_response = api_instance.get_verification_status_api_v1_verification_verify_async_task_id_status_get_0(task_id)
        print("The response of PDFXMLVerificationApi->get_verification_status_api_v1_verification_verify_async_task_id_status_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFXMLVerificationApi->get_verification_status_api_v1_verification_verify_async_task_id_status_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_pdf_async_api_v1_verification_verify_async_post**
> TaskResponse verify_pdf_async_api_v1_verification_verify_async_post(pdf_file, force_ocr=force_ocr)

Verify PDF/XML Factur-X compliance (asynchronous)

Verifies PDF/XML Factur-X compliance asynchronously.

**IMPORTANT**: Only Factur-X PDFs (with embedded XML) are accepted.
PDFs without Factur-X XML will return a `NOT_FACTURX` error in the result.

This version uses a Celery task and can call the OCR service
if the PDF is an image or if `force_ocr=true`.

**Returns immediately** a task ID. Use `/verify-async/{task_id}/status`
to retrieve the result.

**Verification principle (Factur-X 1.08):**
- Principle #2: XML can only contain info present in the PDF
- Principle #4: All XML info must be present and compliant in the PDF

**Verified fields:**
- Identification: BT-1 (invoice #), BT-2 (date), BT-3 (type), BT-5 (currency), BT-23 (framework)
- Seller: BT-27 (name), BT-29 (SIRET), BT-30 (SIREN), BT-31 (VAT)
- Buyer: BT-44 (name), BT-46 (SIRET), BT-47 (SIREN), BT-48 (VAT)
- Amounts: BT-109 (excl. tax), BT-110 (VAT), BT-112 (incl. tax), BT-115 (amount due)
- VAT breakdown: BT-116, BT-117, BT-118, BT-119
- Invoice lines: BT-153, BT-129, BT-146, BT-131
- Mandatory notes: PMT, PMD, AAB
- Rule BR-FR-09: SIRET/SIREN consistency

**Advantages over synchronous version:**
- OCR support for image PDFs (via DocTR service)
- Longer timeout for large documents
- Doesn't block the server

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.task_response import TaskResponse
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
    api_instance = factpulse.PDFXMLVerificationApi(api_client)
    pdf_file = None # bytearray | Factur-X PDF file to verify
    force_ocr = False # bool | Force OCR usage even if PDF contains native text (optional) (default to False)

    try:
        # Verify PDF/XML Factur-X compliance (asynchronous)
        api_response = api_instance.verify_pdf_async_api_v1_verification_verify_async_post(pdf_file, force_ocr=force_ocr)
        print("The response of PDFXMLVerificationApi->verify_pdf_async_api_v1_verification_verify_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFXMLVerificationApi->verify_pdf_async_api_v1_verification_verify_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_file** | **bytearray**| Factur-X PDF file to verify | 
 **force_ocr** | **bool**| Force OCR usage even if PDF contains native text | [optional] [default to False]

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_pdf_async_api_v1_verification_verify_async_post_0**
> TaskResponse verify_pdf_async_api_v1_verification_verify_async_post_0(pdf_file, force_ocr=force_ocr)

Verify PDF/XML Factur-X compliance (asynchronous)

Verifies PDF/XML Factur-X compliance asynchronously.

**IMPORTANT**: Only Factur-X PDFs (with embedded XML) are accepted.
PDFs without Factur-X XML will return a `NOT_FACTURX` error in the result.

This version uses a Celery task and can call the OCR service
if the PDF is an image or if `force_ocr=true`.

**Returns immediately** a task ID. Use `/verify-async/{task_id}/status`
to retrieve the result.

**Verification principle (Factur-X 1.08):**
- Principle #2: XML can only contain info present in the PDF
- Principle #4: All XML info must be present and compliant in the PDF

**Verified fields:**
- Identification: BT-1 (invoice #), BT-2 (date), BT-3 (type), BT-5 (currency), BT-23 (framework)
- Seller: BT-27 (name), BT-29 (SIRET), BT-30 (SIREN), BT-31 (VAT)
- Buyer: BT-44 (name), BT-46 (SIRET), BT-47 (SIREN), BT-48 (VAT)
- Amounts: BT-109 (excl. tax), BT-110 (VAT), BT-112 (incl. tax), BT-115 (amount due)
- VAT breakdown: BT-116, BT-117, BT-118, BT-119
- Invoice lines: BT-153, BT-129, BT-146, BT-131
- Mandatory notes: PMT, PMD, AAB
- Rule BR-FR-09: SIRET/SIREN consistency

**Advantages over synchronous version:**
- OCR support for image PDFs (via DocTR service)
- Longer timeout for large documents
- Doesn't block the server

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.task_response import TaskResponse
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
    api_instance = factpulse.PDFXMLVerificationApi(api_client)
    pdf_file = None # bytearray | Factur-X PDF file to verify
    force_ocr = False # bool | Force OCR usage even if PDF contains native text (optional) (default to False)

    try:
        # Verify PDF/XML Factur-X compliance (asynchronous)
        api_response = api_instance.verify_pdf_async_api_v1_verification_verify_async_post_0(pdf_file, force_ocr=force_ocr)
        print("The response of PDFXMLVerificationApi->verify_pdf_async_api_v1_verification_verify_async_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFXMLVerificationApi->verify_pdf_async_api_v1_verification_verify_async_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_file** | **bytearray**| Factur-X PDF file to verify | 
 **force_ocr** | **bool**| Force OCR usage even if PDF contains native text | [optional] [default to False]

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_pdf_sync_api_v1_verification_verify_post**
> VerificationSuccessResponse verify_pdf_sync_api_v1_verification_verify_post(pdf_file)

Verify PDF/XML Factur-X compliance (synchronous)

Verifies compliance between the PDF and its embedded Factur-X XML.

**IMPORTANT**: Only Factur-X PDFs (with embedded XML) are accepted.
PDFs without Factur-X XML will be rejected with a 400 error.

This synchronous version uses only native PDF extraction (pdfplumber).
For image PDFs requiring OCR, use the `/verify-async` endpoint.

**Verification principle (Factur-X 1.08):**
- Principle #2: XML can only contain info present in the PDF
- Principle #4: All XML info must be present and compliant in the PDF

**Verified fields:**
- Identification: BT-1 (invoice #), BT-2 (date), BT-3 (type), BT-5 (currency), BT-23 (framework)
- Seller: BT-27 (name), BT-29 (SIRET), BT-30 (SIREN), BT-31 (VAT)
- Buyer: BT-44 (name), BT-46 (SIRET), BT-47 (SIREN), BT-48 (VAT)
- Amounts: BT-109 (excl. tax), BT-110 (VAT), BT-112 (incl. tax), BT-115 (amount due)
- VAT breakdown: BT-116, BT-117, BT-118, BT-119
- Invoice lines: BT-153, BT-129, BT-146, BT-131
- Mandatory notes: PMT, PMD, AAB
- Rule BR-FR-09: SIRET/SIREN consistency

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.verification_success_response import VerificationSuccessResponse
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
    api_instance = factpulse.PDFXMLVerificationApi(api_client)
    pdf_file = None # bytearray | Factur-X PDF file to verify

    try:
        # Verify PDF/XML Factur-X compliance (synchronous)
        api_response = api_instance.verify_pdf_sync_api_v1_verification_verify_post(pdf_file)
        print("The response of PDFXMLVerificationApi->verify_pdf_sync_api_v1_verification_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFXMLVerificationApi->verify_pdf_sync_api_v1_verification_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_file** | **bytearray**| Factur-X PDF file to verify | 

### Return type

[**VerificationSuccessResponse**](VerificationSuccessResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verification successful |  -  |
**400** | Verification error (non Factur-X PDF, invalid, etc.) |  -  |
**413** | PDF too large or too many pages |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_pdf_sync_api_v1_verification_verify_post_0**
> VerificationSuccessResponse verify_pdf_sync_api_v1_verification_verify_post_0(pdf_file)

Verify PDF/XML Factur-X compliance (synchronous)

Verifies compliance between the PDF and its embedded Factur-X XML.

**IMPORTANT**: Only Factur-X PDFs (with embedded XML) are accepted.
PDFs without Factur-X XML will be rejected with a 400 error.

This synchronous version uses only native PDF extraction (pdfplumber).
For image PDFs requiring OCR, use the `/verify-async` endpoint.

**Verification principle (Factur-X 1.08):**
- Principle #2: XML can only contain info present in the PDF
- Principle #4: All XML info must be present and compliant in the PDF

**Verified fields:**
- Identification: BT-1 (invoice #), BT-2 (date), BT-3 (type), BT-5 (currency), BT-23 (framework)
- Seller: BT-27 (name), BT-29 (SIRET), BT-30 (SIREN), BT-31 (VAT)
- Buyer: BT-44 (name), BT-46 (SIRET), BT-47 (SIREN), BT-48 (VAT)
- Amounts: BT-109 (excl. tax), BT-110 (VAT), BT-112 (incl. tax), BT-115 (amount due)
- VAT breakdown: BT-116, BT-117, BT-118, BT-119
- Invoice lines: BT-153, BT-129, BT-146, BT-131
- Mandatory notes: PMT, PMD, AAB
- Rule BR-FR-09: SIRET/SIREN consistency

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.verification_success_response import VerificationSuccessResponse
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
    api_instance = factpulse.PDFXMLVerificationApi(api_client)
    pdf_file = None # bytearray | Factur-X PDF file to verify

    try:
        # Verify PDF/XML Factur-X compliance (synchronous)
        api_response = api_instance.verify_pdf_sync_api_v1_verification_verify_post_0(pdf_file)
        print("The response of PDFXMLVerificationApi->verify_pdf_sync_api_v1_verification_verify_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFXMLVerificationApi->verify_pdf_sync_api_v1_verification_verify_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_file** | **bytearray**| Factur-X PDF file to verify | 

### Return type

[**VerificationSuccessResponse**](VerificationSuccessResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verification successful |  -  |
**400** | Verification error (non Factur-X PDF, invalid, etc.) |  -  |
**413** | PDF too large or too many pages |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

