# factpulse.InvoiceProcessingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_invoice_api_v1_processing_generate_invoice_post**](InvoiceProcessingApi.md#generate_invoice_api_v1_processing_generate_invoice_post) | **POST** /api/v1/processing/generate-invoice | Generate a Factur-X invoice
[**generate_test_certificate_api_v1_processing_generate_test_certificate_post**](InvoiceProcessingApi.md#generate_test_certificate_api_v1_processing_generate_test_certificate_post) | **POST** /api/v1/processing/generate-test-certificate | Generate a self-signed X.509 test certificate
[**get_task_status_api_v1_processing_tasks_task_id_status_get**](InvoiceProcessingApi.md#get_task_status_api_v1_processing_tasks_task_id_status_get) | **GET** /api/v1/processing/tasks/{task_id}/status | Get task generation status
[**sign_pdf_api_v1_processing_sign_pdf_post**](InvoiceProcessingApi.md#sign_pdf_api_v1_processing_sign_pdf_post) | **POST** /api/v1/processing/sign-pdf | Sign a PDF with client&#39;s certificate (PAdES-B-LT)
[**sign_pdf_async_api_v1_processing_sign_pdf_async_post**](InvoiceProcessingApi.md#sign_pdf_async_api_v1_processing_sign_pdf_async_post) | **POST** /api/v1/processing/sign-pdf-async | Sign a PDF asynchronously (Celery)
[**submit_complete_invoice_api_v1_processing_invoices_submit_complete_post**](InvoiceProcessingApi.md#submit_complete_invoice_api_v1_processing_invoices_submit_complete_post) | **POST** /api/v1/processing/invoices/submit-complete | Submit a complete invoice (generation + signature + submission)
[**submit_complete_invoice_async_api_v1_processing_invoices_submit_complete_async_post**](InvoiceProcessingApi.md#submit_complete_invoice_async_api_v1_processing_invoices_submit_complete_async_post) | **POST** /api/v1/processing/invoices/submit-complete-async | Submit a complete invoice (asynchronous with Celery)
[**validate_facturx_pdf_api_v1_processing_validate_facturx_pdf_post**](InvoiceProcessingApi.md#validate_facturx_pdf_api_v1_processing_validate_facturx_pdf_post) | **POST** /api/v1/processing/validate-facturx-pdf | Validate a complete Factur-X PDF
[**validate_facturx_pdf_async_api_v1_processing_validate_facturx_async_post**](InvoiceProcessingApi.md#validate_facturx_pdf_async_api_v1_processing_validate_facturx_async_post) | **POST** /api/v1/processing/validate-facturx-async | Validate a Factur-X PDF (asynchronous with polling)
[**validate_pdf_signature_endpoint_api_v1_processing_validate_pdf_signature_post**](InvoiceProcessingApi.md#validate_pdf_signature_endpoint_api_v1_processing_validate_pdf_signature_post) | **POST** /api/v1/processing/validate-pdf-signature | Validate electronic signatures of a PDF
[**validate_xml_api_v1_processing_validate_xml_post**](InvoiceProcessingApi.md#validate_xml_api_v1_processing_validate_xml_post) | **POST** /api/v1/processing/validate-xml | Validate an existing Factur-X XML


# **generate_invoice_api_v1_processing_generate_invoice_post**
> TaskResponse generate_invoice_api_v1_processing_generate_invoice_post(invoice_data, profile=profile, output_format=output_format, auto_enrich=auto_enrich, source_pdf=source_pdf)

Generate a Factur-X invoice

Generates an electronic invoice in Factur-X format compliant with European standards.

## Applied Standards

- **Factur-X** (France): FNFE-MPE standard (Forum National de la Facture Électronique)
- **ZUGFeRD** (Germany): German format compatible with Factur-X
- **EN 16931**: European semantic standard for electronic invoicing
- **ISO 19005-3** (PDF/A-3): Long-term electronic archiving
- **Cross Industry Invoice (CII)**: UN/CEFACT XML syntax

## 🆕 New: Simplified format with auto-enrichment (P0.1)

You can now create an invoice by providing only:
- An invoice number
- A sender SIRET + **IBAN** (required)
- A recipient SIRET
- Invoice lines (description, quantity, net price)

**Simplified format example**:
```json
{
  "numero": "FACT-2025-001",
  "emetteur": {
    "siret": "92019522900017",
    "iban": "FR7630001007941234567890185"
  },
  "destinataire": {"siret": "35600000000048"},
  "lignes": [
    {"description": "Service", "quantite": 10, "prix_ht": 100.00, "tva": 20.0}
  ]
}
```

**⚠️ Required fields (simplified format)**:
- `numero`: Unique invoice number
- `emetteur.siret`: Sender's SIRET (14 digits)
- `emetteur.iban`: Bank account IBAN (no public API to retrieve it)
- `destinataire.siret`: Recipient's SIRET
- `lignes[]`: At least one invoice line

**What happens automatically with `auto_enrich=True`**:
- ✅ Name enrichment from Chorus Pro API
- ✅ Address enrichment from Business Search API (free, public)
- ✅ Automatic intra-EU VAT calculation (FR + key + SIREN)
- ✅ Chorus Pro ID retrieval for electronic invoicing
- ✅ Net/VAT/Gross totals calculation
- ✅ Date generation (today + 30-day due date)
- ✅ Multi-rate VAT handling

**Supported identifiers**:
- SIRET (14 digits): Specific establishment ⭐ Recommended
- SIREN (9 digits): Company (auto-selection of headquarters)
- Special types: UE_HORS_FRANCE, RIDET, TAHITI, etc.

## Checks performed during generation

### 1. Data validation (Pydantic)
- Data types (amounts as Decimal, ISO 8601 dates)
- Formats (14-digit SIRET, 9-digit SIREN, IBAN)
- Required fields per profile
- Amount consistency (Net + VAT = Gross)

### 2. CII-compliant XML generation
- Serialization according to Cross Industry Invoice XSD schema
- Correct UN/CEFACT namespaces
- Hierarchical structure respected
- UTF-8 encoding without BOM

### 3. Schematron validation
- Business rules for selected profile (MINIMUM, BASIC, EN16931, EXTENDED)
- Element cardinality (required, optional, repeatable)
- Calculation rules (totals, VAT, discounts)
- European EN 16931 compliance

### 4. PDF/A-3 conversion (if output_format='pdf')
- Source PDF conversion to PDF/A-3 via Ghostscript
- Factur-X XML embedding in PDF
- Compliant XMP metadata
- ICC sRGB color profile
- Removal of forbidden elements (JavaScript, forms)

## How it works

1. **Submission**: Invoice is queued in Celery for asynchronous processing
2. **Immediate return**: You receive a `task_id` (HTTP 202 Accepted)
3. **Tracking**: Use the `/tasks/{task_id}/status` endpoint to track progress

## Output formats

- **xml**: Generates only Factur-X XML (recommended for testing)
- **pdf**: Generates PDF/A-3 with embedded XML (requires `source_pdf`)

## Factur-X profiles

- **MINIMUM**: Minimal data (simplified invoice)
- **BASIC**: Basic information (SMEs)
- **EN16931**: European standard (recommended, compliant with directive 2014/55/EU)
- **EXTENDED**: All available data (large accounts)

## What you get

After successful processing (status `completed`):
- **XML only**: Base64-encoded Factur-X compliant XML file
- **PDF/A-3**: PDF with embedded XML, ready for sending/archiving
- **Metadata**: Profile, Factur-X version, file size
- **Validation**: Schematron compliance confirmation

## Validation

Data is automatically validated according to detected format.
On error, a 422 status is returned with invalid field details.

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
    api_instance = factpulse.InvoiceProcessingApi(api_client)
    invoice_data = 'invoice_data_example' # str | Invoice data in JSON format.              Two formats accepted:             1. **Classic format**: Complete FactureFacturX structure (all fields)             2. **Simplified format** (🆕 P0.1): Minimal structure with auto-enrichment              Format is detected automatically!             
    profile = factpulse.APIProfile() # APIProfile | Factur-X profile: MINIMUM, BASIC, EN16931 or EXTENDED. (optional)
    output_format = factpulse.OutputFormat() # OutputFormat | Output format: 'xml' (XML only) or 'pdf' (Factur-X PDF with embedded XML). (optional)
    auto_enrich = True # bool | 🆕 Enable auto-enrichment from SIRET/SIREN (simplified format only) (optional) (default to True)
    source_pdf = None # bytearray |  (optional)

    try:
        # Generate a Factur-X invoice
        api_response = api_instance.generate_invoice_api_v1_processing_generate_invoice_post(invoice_data, profile=profile, output_format=output_format, auto_enrich=auto_enrich, source_pdf=source_pdf)
        print("The response of InvoiceProcessingApi->generate_invoice_api_v1_processing_generate_invoice_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceProcessingApi->generate_invoice_api_v1_processing_generate_invoice_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_data** | **str**| Invoice data in JSON format.              Two formats accepted:             1. **Classic format**: Complete FactureFacturX structure (all fields)             2. **Simplified format** (🆕 P0.1): Minimal structure with auto-enrichment              Format is detected automatically!              | 
 **profile** | [**APIProfile**](APIProfile.md)| Factur-X profile: MINIMUM, BASIC, EN16931 or EXTENDED. | [optional] 
 **output_format** | [**OutputFormat**](OutputFormat.md)| Output format: &#39;xml&#39; (XML only) or &#39;pdf&#39; (Factur-X PDF with embedded XML). | [optional] 
 **auto_enrich** | **bool**| 🆕 Enable auto-enrichment from SIRET/SIREN (simplified format only) | [optional] [default to True]
 **source_pdf** | **bytearray**|  | [optional] 

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
**400** | Invalid invoice data or missing PDF file |  -  |
**422** | Invoice data validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_test_certificate_api_v1_processing_generate_test_certificate_post**
> GenerateCertificateResponse generate_test_certificate_api_v1_processing_generate_test_certificate_post(generate_certificate_request)

Generate a self-signed X.509 test certificate

Generates a self-signed X.509 certificate for PDF electronic signature testing.

    **⚠️ WARNING: TEST certificate only!**

    This certificate is:
    - ✅ Suitable for testing and development
    - ✅ Compatible with PDF signing (PAdES)
    - ✅ Compliant with eIDAS **SES** level (Simple Electronic Signature)
    - ❌ **NEVER usable in production**
    - ❌ **Not recognized** by browsers and PDF readers
    - ❌ **No legal value**

    ## eIDAS levels

    - **SES** (Simple): Self-signed certificate ← Generated by this endpoint
    - **AdES** (Advanced): Commercial CA certificate (Let's Encrypt, etc.)
    - **QES** (Qualified): Qualified certificate from QTSP (CertEurope, Universign, etc.)

    ## Usage

    Once generated, the certificate can be:

    1. **Saved in Django** (recommended):
       - Django Admin > Signing Certificates
       - Upload `certificate_pem` and `private_key_pem`

    2. **Used directly**:
       - Sign a PDF with `/sign-pdf`
       - The certificate will be automatically used

    ## Example call

    ```bash
    curl -X POST "https://www.factpulse.fr/api/v1/processing/generate-test-certificate" \
      -H "Authorization: Bearer eyJ0eXAi..." \
      -H "Content-Type: application/json" \
      -d '{
        "cn": "Test Client XYZ",
        "organization": "Client XYZ Ltd",
        "email": "contact@xyz.com",
        "validity_days": 365
      }'
    ```

    ## Use cases

    - PDF signature testing in development
    - Electronic signature POC
    - Training and demos
    - Automated integration tests

    ## Technical compliance

    Certificate generated with:
    - RSA key 2048 or 4096 bits
    - SHA-256 algorithm
    - Key Usage extensions: `digitalSignature`, `contentCommitment` (non-repudiation)
    - Extended Key Usage extensions: `codeSigning`, `emailProtection`
    - Validity: 1 day to 10 years (configurable)
    - Format: PEM (certificate and key)
    - Optional: PKCS#12 (.p12)

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.generate_certificate_request import GenerateCertificateRequest
from factpulse.models.generate_certificate_response import GenerateCertificateResponse
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
    api_instance = factpulse.InvoiceProcessingApi(api_client)
    generate_certificate_request = factpulse.GenerateCertificateRequest() # GenerateCertificateRequest | 

    try:
        # Generate a self-signed X.509 test certificate
        api_response = api_instance.generate_test_certificate_api_v1_processing_generate_test_certificate_post(generate_certificate_request)
        print("The response of InvoiceProcessingApi->generate_test_certificate_api_v1_processing_generate_test_certificate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceProcessingApi->generate_test_certificate_api_v1_processing_generate_test_certificate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_certificate_request** | [**GenerateCertificateRequest**](GenerateCertificateRequest.md)|  | 

### Return type

[**GenerateCertificateResponse**](GenerateCertificateResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificate generated successfully |  -  |
**400** | Invalid request (incorrect parameters) |  -  |
**500** | Server error during generation |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_status_api_v1_processing_tasks_task_id_status_get**
> TaskStatus get_task_status_api_v1_processing_tasks_task_id_status_get(task_id)

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
from factpulse.models.task_status import TaskStatus
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
    api_instance = factpulse.InvoiceProcessingApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Get task generation status
        api_response = api_instance.get_task_status_api_v1_processing_tasks_task_id_status_get(task_id)
        print("The response of InvoiceProcessingApi->get_task_status_api_v1_processing_tasks_task_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceProcessingApi->get_task_status_api_v1_processing_tasks_task_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**TaskStatus**](TaskStatus.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_pdf_api_v1_processing_sign_pdf_post**
> object sign_pdf_api_v1_processing_sign_pdf_post(pdf_file, reason=reason, location=location, contact=contact, field_name=field_name, use_pades_lt=use_pades_lt, use_timestamp=use_timestamp)

Sign a PDF with client's certificate (PAdES-B-LT)

Signs an uploaded PDF with the electronic certificate configured for the client (via client_uid from JWT).

    **Supported standards**: PAdES-B-B, PAdES-B-T (timestamping), PAdES-B-LT (long-term archiving).

    **eIDAS levels**: SES (self-signed), AdES (commercial CA), QES (PSCO - out of scope).

    **Security**: Double authentication X-Internal-Secret + JWT Bearer to retrieve the certificate.

    **⚠️ Legal disclaimer**: Generated signatures are electronic seals as defined by
    the eIDAS regulation. The level of legal validity depends on the certificate used (SES/AdES/QES).
    FactPulse does not provide QES qualified certificates - you must obtain a certificate from
    a PSCO (qualified Trust Service Provider) for maximum legal validity.

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
    api_instance = factpulse.InvoiceProcessingApi(api_client)
    pdf_file = None # bytearray | PDF file to sign (will be processed and returned signed in base64)
    reason = 'reason_example' # str |  (optional)
    location = 'location_example' # str |  (optional)
    contact = 'contact_example' # str |  (optional)
    field_name = 'FactPulseSignature' # str | PDF signature field name (optional) (default to 'FactPulseSignature')
    use_pades_lt = False # bool | Enable PAdES-B-LT (long-term archiving with embedded validation data). REQUIRES a certificate with OCSP/CRL access. (optional) (default to False)
    use_timestamp = True # bool | Enable RFC 3161 timestamping with FreeTSA (PAdES-B-T) (optional) (default to True)

    try:
        # Sign a PDF with client's certificate (PAdES-B-LT)
        api_response = api_instance.sign_pdf_api_v1_processing_sign_pdf_post(pdf_file, reason=reason, location=location, contact=contact, field_name=field_name, use_pades_lt=use_pades_lt, use_timestamp=use_timestamp)
        print("The response of InvoiceProcessingApi->sign_pdf_api_v1_processing_sign_pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceProcessingApi->sign_pdf_api_v1_processing_sign_pdf_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_file** | **bytearray**| PDF file to sign (will be processed and returned signed in base64) | 
 **reason** | **str**|  | [optional] 
 **location** | **str**|  | [optional] 
 **contact** | **str**|  | [optional] 
 **field_name** | **str**| PDF signature field name | [optional] [default to &#39;FactPulseSignature&#39;]
 **use_pades_lt** | **bool**| Enable PAdES-B-LT (long-term archiving with embedded validation data). REQUIRES a certificate with OCSP/CRL access. | [optional] [default to False]
 **use_timestamp** | **bool**| Enable RFC 3161 timestamping with FreeTSA (PAdES-B-T) | [optional] [default to True]

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF signed successfully |  -  |
**400** | Invalid or expired certificate |  -  |
**404** | No certificate configured for this client |  -  |
**401** | Not authenticated - Missing or invalid JWT token |  -  |
**503** | Django service unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_pdf_async_api_v1_processing_sign_pdf_async_post**
> object sign_pdf_async_api_v1_processing_sign_pdf_async_post(pdf_file, reason=reason, location=location, contact=contact, field_name=field_name, use_pades_lt=use_pades_lt, use_timestamp=use_timestamp)

Sign a PDF asynchronously (Celery)

Signs an uploaded PDF asynchronously via a Celery task.

    **Difference with /sign-pdf**:
    - `/sign-pdf`: Synchronous signature (blocking until completion)
    - `/sign-pdf-async`: Asynchronous signature (returns immediately with task_id)

    **Async advantages**:
    - No timeout for large files
    - No blocking of FastAPI worker
    - Progress tracking via task_id
    - Ideal for batch processing

    **Supported standards**: PAdES-B-B, PAdES-B-T (timestamping), PAdES-B-LT (long-term archiving).

    **⚠️ Legal disclaimer**: Same as /sign-pdf (see that endpoint's documentation).

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
    api_instance = factpulse.InvoiceProcessingApi(api_client)
    pdf_file = None # bytearray | PDF file to sign (processed asynchronously)
    reason = 'reason_example' # str |  (optional)
    location = 'location_example' # str |  (optional)
    contact = 'contact_example' # str |  (optional)
    field_name = 'FactPulseSignature' # str | PDF signature field name (optional) (default to 'FactPulseSignature')
    use_pades_lt = False # bool | Enable PAdES-B-LT (long-term archiving with embedded validation data). REQUIRES a certificate with OCSP/CRL access. (optional) (default to False)
    use_timestamp = True # bool | Enable RFC 3161 timestamping with FreeTSA (PAdES-B-T) (optional) (default to True)

    try:
        # Sign a PDF asynchronously (Celery)
        api_response = api_instance.sign_pdf_async_api_v1_processing_sign_pdf_async_post(pdf_file, reason=reason, location=location, contact=contact, field_name=field_name, use_pades_lt=use_pades_lt, use_timestamp=use_timestamp)
        print("The response of InvoiceProcessingApi->sign_pdf_async_api_v1_processing_sign_pdf_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceProcessingApi->sign_pdf_async_api_v1_processing_sign_pdf_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_file** | **bytearray**| PDF file to sign (processed asynchronously) | 
 **reason** | **str**|  | [optional] 
 **location** | **str**|  | [optional] 
 **contact** | **str**|  | [optional] 
 **field_name** | **str**| PDF signature field name | [optional] [default to &#39;FactPulseSignature&#39;]
 **use_pades_lt** | **bool**| Enable PAdES-B-LT (long-term archiving with embedded validation data). REQUIRES a certificate with OCSP/CRL access. | [optional] [default to False]
 **use_timestamp** | **bool**| Enable RFC 3161 timestamping with FreeTSA (PAdES-B-T) | [optional] [default to True]

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**202** | Signature task created successfully |  -  |
**400** | Invalid parameters |  -  |
**401** | Not authenticated - Missing or invalid JWT token |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_complete_invoice_api_v1_processing_invoices_submit_complete_post**
> SubmitCompleteInvoiceResponse submit_complete_invoice_api_v1_processing_invoices_submit_complete_post(submit_complete_invoice_request)

Submit a complete invoice (generation + signature + submission)

Unified endpoint to submit a complete invoice to different destinations.

    **Automated workflow:**
    1. **Auto-enrichment** (optional): retrieves data via public APIs and Chorus Pro/AFNOR
    2. **Factur-X PDF generation**: creates a PDF/A-3 with embedded XML
    3. **Electronic signature** (optional): signs the PDF with a certificate
    4. **Submission**: sends to the chosen destination (Chorus Pro or AFNOR PDP)

    **Supported destinations:**
    - **Chorus Pro**: French B2G platform (invoices to public sector)
    - **AFNOR PDP**: Partner Dematerialization Platforms

    **Destination credentials - 2 modes available:**

    **Mode 1 - Retrieval via JWT (recommended):**
    - Credentials are retrieved automatically via the JWT `client_uid`
    - Do not provide the `credentials` field in `destination`
    - Zero-trust architecture: no secrets in the payload
    - Example: `"destination": {"type": "chorus_pro"}`

    **Mode 2 - Credentials in the payload:**
    - Provide credentials directly in the payload
    - Useful for tests or third-party integrations
    - Example: `"destination": {"type": "chorus_pro", "credentials": {...}}`


    **Electronic signature (optional) - 2 modes available:**

    **Mode 1 - Stored certificate (recommended):**
    - Certificate is retrieved automatically via the JWT `client_uid`
    - No key to provide in the payload
    - PAdES-B-LT signature with timestamp (eIDAS compliant)
    - Example: `"signature": {"reason": "Factur-X compliance"}`

    **Mode 2 - Keys in the payload (for tests):**
    - Provide `key_pem` and `cert_pem` directly
    - PEM format accepted: raw or base64
    - Useful for tests or special cases without stored certificate
    - Example: `"signature": {"key_pem": "-----BEGIN...", "cert_pem": "-----BEGIN..."}`

    If `key_pem` and `cert_pem` are provided → Mode 2
    Otherwise → Mode 1 (certificate retrieved via `client_uid`)

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.submit_complete_invoice_request import SubmitCompleteInvoiceRequest
from factpulse.models.submit_complete_invoice_response import SubmitCompleteInvoiceResponse
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
    api_instance = factpulse.InvoiceProcessingApi(api_client)
    submit_complete_invoice_request = factpulse.SubmitCompleteInvoiceRequest() # SubmitCompleteInvoiceRequest | 

    try:
        # Submit a complete invoice (generation + signature + submission)
        api_response = api_instance.submit_complete_invoice_api_v1_processing_invoices_submit_complete_post(submit_complete_invoice_request)
        print("The response of InvoiceProcessingApi->submit_complete_invoice_api_v1_processing_invoices_submit_complete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceProcessingApi->submit_complete_invoice_api_v1_processing_invoices_submit_complete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_complete_invoice_request** | [**SubmitCompleteInvoiceRequest**](SubmitCompleteInvoiceRequest.md)|  | 

### Return type

[**SubmitCompleteInvoiceResponse**](SubmitCompleteInvoiceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_complete_invoice_async_api_v1_processing_invoices_submit_complete_async_post**
> TaskResponse submit_complete_invoice_async_api_v1_processing_invoices_submit_complete_async_post(submit_complete_invoice_request)

Submit a complete invoice (asynchronous with Celery)

Asynchronous version of the `/invoices/submit-complete` endpoint using Celery for background processing.

    **Automated workflow (same as synchronous version):**
    1. **Auto-enrichment** (optional): retrieves data via public APIs and Chorus Pro/AFNOR
    2. **Factur-X PDF generation**: creates a PDF/A-3 with embedded XML
    3. **Electronic signature** (optional): signs the PDF with a certificate
    4. **Submission**: sends to the chosen destination (Chorus Pro or AFNOR PDP)

    **Supported destinations:**
    - **Chorus Pro**: French B2G platform (invoices to public sector)
    - **AFNOR PDP**: Partner Dematerialization Platforms

    **Differences with synchronous version:**
    - ✅ **Non-blocking**: Returns immediately with a `task_id` (HTTP 202 Accepted)
    - ✅ **Background processing**: Invoice is processed by a Celery worker
    - ✅ **Progress tracking**: Use `/tasks/{task_id}/status` to track status
    - ✅ **Ideal for high volumes**: Allows processing many invoices in parallel

    **How to use:**
    1. **Submission**: Call this endpoint with your invoice data
    2. **Immediate return**: You receive a `task_id` (e.g., "abc123-def456")
    3. **Tracking**: Call `/tasks/{task_id}/status` to check progress
    4. **Result**: When `status = "SUCCESS"`, the `result` field contains the complete response

    **Credentials and signature**: Same modes as the synchronous version (JWT or payload).

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.submit_complete_invoice_request import SubmitCompleteInvoiceRequest
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
    api_instance = factpulse.InvoiceProcessingApi(api_client)
    submit_complete_invoice_request = factpulse.SubmitCompleteInvoiceRequest() # SubmitCompleteInvoiceRequest | 

    try:
        # Submit a complete invoice (asynchronous with Celery)
        api_response = api_instance.submit_complete_invoice_async_api_v1_processing_invoices_submit_complete_async_post(submit_complete_invoice_request)
        print("The response of InvoiceProcessingApi->submit_complete_invoice_async_api_v1_processing_invoices_submit_complete_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceProcessingApi->submit_complete_invoice_async_api_v1_processing_invoices_submit_complete_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_complete_invoice_request** | [**SubmitCompleteInvoiceRequest**](SubmitCompleteInvoiceRequest.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_facturx_pdf_api_v1_processing_validate_facturx_pdf_post**
> PDFValidationResultAPI validate_facturx_pdf_api_v1_processing_validate_facturx_pdf_post(pdf_file, profile=profile, use_verapdf=use_verapdf)

Validate a complete Factur-X PDF

Validates a complete Factur-X PDF according to European and French standards.

## Applied validation standards

- **EN 16931**: European semantic standard (directive 2014/55/EU)
- **ISO 19005-3** (PDF/A-3): Long-term electronic archiving
- **Factur-X / ZUGFeRD**: Franco-German specification
- **Schematron**: XML business rules validation
- **eIDAS**: European regulation on electronic identification (signatures)

## Checks performed

### 1. Factur-X XML extraction and validation
**Checks performed:**
- Presence of embedded XML file (`factur-x.xml` or `zugferd-invoice.xml`)
- Automatic profile detection (MINIMUM, BASIC, EN16931, EXTENDED)
- XML parsing with UTF-8 validation
- GuidelineSpecifiedDocumentContextParameter/ID extraction

**Schematron validation:**
- Business rules for detected profile (MINIMUM: 45 rules, EN16931: 178 rules)
- Cardinality of required elements
- Calculation consistency (net, VAT, gross amounts, discounts)
- Identifier formats (SIRET, intra-EU VAT, IBAN)
- Standardized codes (ISO country codes, UN/ECE units, VAT codes)

**What is verified:**
- ✅ XML structure conforming to Cross Industry Invoice XSD
- ✅ Correct UN/CEFACT namespace
- ✅ European business rules (BR-xx)
- ✅ French-specific rules (FR-xx)

### 2. PDF/A-3 compliance
**Basic validation (metadata):**
- Presence of `/Type` field set to `Catalog`
- Metadata `pdfaid:part` = 3 (PDF/A-3)
- Metadata `pdfaid:conformance` = B or U
- PDF version >= 1.4

**Strict VeraPDF validation (if use_verapdf=True):**
- 146+ ISO 19005-3 rules (PDF/A-3B)
- Absence of forbidden content (JavaScript, multimedia, dynamic forms)
- Correctly embedded fonts and subsets
- Compliant color spaces (sRGB, DeviceGray)
- Valid file structure (cross-reference table)
- XMP metadata conforming to ISO 16684-1

**What is verified:**
- ✅ Long-term archivable file (20+ years)
- ✅ Guaranteed readability (embedded fonts)
- ✅ Legal compliance (France, Germany, EU)

### 3. XMP metadata (eXtensible Metadata Platform)
**Checks performed:**
- Presence of `<?xpacket>` block with XMP metadata
- `fx:` namespace for Factur-X: `urn:factur-x:pdfa:CrossIndustryDocument:invoice:1p0#`
- Required Factur-X fields:
  - `fx:ConformanceLevel`: Profile (MINIMUM, BASIC, EN16931, EXTENDED)
  - `fx:DocumentFileName`: Embedded XML name
  - `fx:DocumentType`: "INVOICE"
  - `fx:Version`: Factur-X version (1.0.07)

**What is verified:**
- ✅ Metadata conforming to ISO 16684-1
- ✅ Correct declared Factur-X profile
- ✅ Supported Factur-X version

### 4. Electronic signatures
**Detection and analysis:**
- Presence of `/Sig` dictionaries in PDF
- Signature type: PAdES (PDF Advanced Electronic Signature)
- Information extraction:
  - Signer name (`/Name`)
  - Signing date (`/M`)
  - Signature reason (`/Reason`)
  - Signature location (`/Location`)
  - Signature type (approval, certification)

**What is verified:**
- ✅ Presence of signatures or seals
- ✅ Number of signatures (single or multi-signature)
- ℹ️ No cryptographic verification (requires certificates)

## Parameters

- **pdf_file** (required): The Factur-X PDF file to validate
- **profile** (optional): Expected profile. If absent, auto-detected from XML
- **use_verapdf** (optional, default=false): Enable strict PDF/A validation with VeraPDF
  - `false`: Fast metadata validation (2-3 seconds)
  - `true`: Complete ISO 19005-3 validation (15-30 seconds, **recommended for production**)

## Detailed response

```json
{
  "isCompliant": true,
  "xml": {
    "present": true,
    "compliant": true,
    "profile": "EN16931",
    "errors": []
  },
  "pdfa": {
    "compliant": true,
    "version": "PDF/A-3B",
    "method": "verapdf",
    "errors": []
  },
  "xmp": {
    "present": true,
    "compliant": true,
    "metadata": {...}
  },
  "signatures": {
    "present": true,
    "count": 1,
    "details": [...]
  }
}
```

## Use cases

- **Before sending**: Validate generated invoice before transmission to client
- **On reception**: Verify compliance of invoice received from supplier
- **Audit**: Check quality of invoice batches
- **Legal compliance**: Ensure B2B/B2G obligations are met in France
- **Debugging**: Identify issues in generation process
- **Archiving**: Guarantee long-term validity (PDF/A-3)

## Processing time

- Basic validation: 2-3 seconds
- VeraPDF validation: 15-30 seconds (depends on PDF size)

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.pdf_validation_result_api import PDFValidationResultAPI
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
    api_instance = factpulse.InvoiceProcessingApi(api_client)
    pdf_file = None # bytearray | Factur-X PDF file to validate (.pdf format).
    profile = factpulse.APIProfile() # APIProfile |  (optional)
    use_verapdf = False # bool | Enable strict PDF/A validation with VeraPDF (recommended for production). If False, uses basic metadata validation. (optional) (default to False)

    try:
        # Validate a complete Factur-X PDF
        api_response = api_instance.validate_facturx_pdf_api_v1_processing_validate_facturx_pdf_post(pdf_file, profile=profile, use_verapdf=use_verapdf)
        print("The response of InvoiceProcessingApi->validate_facturx_pdf_api_v1_processing_validate_facturx_pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceProcessingApi->validate_facturx_pdf_api_v1_processing_validate_facturx_pdf_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_file** | **bytearray**| Factur-X PDF file to validate (.pdf format). | 
 **profile** | [**APIProfile**](APIProfile.md)|  | [optional] 
 **use_verapdf** | **bool**| Enable strict PDF/A validation with VeraPDF (recommended for production). If False, uses basic metadata validation. | [optional] [default to False]

### Return type

[**PDFValidationResultAPI**](PDFValidationResultAPI.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validation completed successfully (check is_compliant field for result) |  -  |
**400** | Invalid or unreadable PDF file |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_facturx_pdf_async_api_v1_processing_validate_facturx_async_post**
> TaskResponse validate_facturx_pdf_async_api_v1_processing_validate_facturx_async_post(pdf_file, profile=profile, use_verapdf=use_verapdf)

Validate a Factur-X PDF (asynchronous with polling)

Validates a Factur-X PDF asynchronously with polling system.

## How it works

1. **Submission**: PDF is queued for asynchronous validation
2. **Immediate return**: You receive a `task_id` (HTTP 202)
3. **Tracking**: Use the `/tasks/{task_id}/status` endpoint to track progress

## Advantages of asynchronous mode

- **No timeout**: Ideal for large PDFs or VeraPDF validation (which can take several seconds)
- **Scalability**: Validations are processed by dedicated Celery workers
- **Status tracking**: Allows you to monitor validation progress
- **Non-blocking**: Your client doesn't wait during validation

## When to use this mode?

- **VeraPDF validation enabled** (`use_verapdf=True`): Strict validation can take 2-10 seconds
- **Large PDF files**: PDFs > 1 MB
- **Batch processing**: Validating multiple invoices in parallel
- **Asynchronous integration**: Your system supports polling

## Checks performed

### 1. Factur-X XML extraction and validation
- Verifies presence of Factur-X compliant embedded XML file
- Automatically detects profile used (MINIMUM, BASIC, EN16931, EXTENDED)
- Validates XML against detected profile's Schematron rules

### 2. PDF/A compliance
- **Without VeraPDF**: Basic metadata validation (fast, ~100ms)
- **With VeraPDF**: Strict ISO 19005 validation (146+ rules, 2-10s)
  - Detects PDF/A version (PDF/A-1, PDF/A-3, etc.)
  - Detailed non-compliance reports

### 3. XMP metadata
- Verifies presence of XMP metadata in PDF
- Validates Factur-X metadata compliance (profile, version)
- Extracts all available XMP metadata

### 4. Electronic signatures
- Detects presence of electronic signatures or seals
- Extracts information about each signature (signer, date, reason)
- Counts number of signatures present

## Parameters

- **pdf_file**: The Factur-X PDF file to validate
- **profile**: Expected Factur-X profile (optional). If not specified, profile
  will be auto-detected from embedded XML file.
- **use_verapdf**: Enable strict PDF/A validation with VeraPDF.
  ⚠️ **Warning**: VeraPDF can take 2-10 seconds depending on PDF size.
  Recommended only in asynchronous mode to avoid timeouts.

## Retrieving results

After submission, use `GET /tasks/{task_id}/status` endpoint to retrieve the result.

**Polling example**:
```python
import requests
import time

# 1. Submit task
response = requests.post("/validate-facturx-async", files={"pdf_file": pdf_file})
task_id = response.json()["taskId"]

# 2. Poll every 2 seconds
while True:
    status_response = requests.get(f"/tasks/{task_id}/status")
    status = status_response.json()

    if status["status"] == "SUCCESS":
        result = status["result"]["validation_result"]
        print(f"Compliant: {result['is_compliant']}")
        break
    elif status["status"] == "FAILURE":
        print(f"Error: {status['result']['errorMessage']}")
        break

    time.sleep(2)  # Wait 2 seconds before next check
```

## Use cases

- Validate invoices before sending with VeraPDF (strict validation)
- Process invoice batches in parallel
- Integrate validation into an asynchronous pipeline
- Validate large PDFs without timeout risk

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
    api_instance = factpulse.InvoiceProcessingApi(api_client)
    pdf_file = None # bytearray | Factur-X PDF file to validate (.pdf format).
    profile = factpulse.APIProfile() # APIProfile |  (optional)
    use_verapdf = False # bool | Enable strict PDF/A validation with VeraPDF (recommended for production). May take several seconds. (optional) (default to False)

    try:
        # Validate a Factur-X PDF (asynchronous with polling)
        api_response = api_instance.validate_facturx_pdf_async_api_v1_processing_validate_facturx_async_post(pdf_file, profile=profile, use_verapdf=use_verapdf)
        print("The response of InvoiceProcessingApi->validate_facturx_pdf_async_api_v1_processing_validate_facturx_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceProcessingApi->validate_facturx_pdf_async_api_v1_processing_validate_facturx_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_file** | **bytearray**| Factur-X PDF file to validate (.pdf format). | 
 **profile** | [**APIProfile**](APIProfile.md)|  | [optional] 
 **use_verapdf** | **bool**| Enable strict PDF/A validation with VeraPDF (recommended for production). May take several seconds. | [optional] [default to False]

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
**400** | Invalid or unreadable PDF file |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_pdf_signature_endpoint_api_v1_processing_validate_pdf_signature_post**
> object validate_pdf_signature_endpoint_api_v1_processing_validate_pdf_signature_post(pdf_file)

Validate electronic signatures of a PDF

Validates electronic signatures present in an uploaded PDF.

    **Verifications performed**:
    - Presence of signatures
    - Document integrity (not modified since signing)
    - Certificate validity
    - Chain of trust (if available)
    - Presence of timestamp (PAdES-B-T)
    - Validation data (PAdES-B-LT)

    **Supported standards**: PAdES-B-B, PAdES-B-T, PAdES-B-LT, ISO 32000-2.

    **⚠️ Note**: This validation is technical (cryptographic integrity). Legal validity
    depends on the eIDAS level of the certificate (SES/AdES/QES) and the context of use.

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
    api_instance = factpulse.InvoiceProcessingApi(api_client)
    pdf_file = None # bytearray | PDF file to validate (will be analyzed to detect and validate signatures)

    try:
        # Validate electronic signatures of a PDF
        api_response = api_instance.validate_pdf_signature_endpoint_api_v1_processing_validate_pdf_signature_post(pdf_file)
        print("The response of InvoiceProcessingApi->validate_pdf_signature_endpoint_api_v1_processing_validate_pdf_signature_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceProcessingApi->validate_pdf_signature_endpoint_api_v1_processing_validate_pdf_signature_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_file** | **bytearray**| PDF file to validate (will be analyzed to detect and validate signatures) | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validation successful |  -  |
**400** | Invalid or unreadable file |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_xml_api_v1_processing_validate_xml_post**
> ValidationSuccessResponse validate_xml_api_v1_processing_validate_xml_post(xml_file, profile=profile)

Validate an existing Factur-X XML

Validates a Factur-X XML file against Schematron business rules according to EN 16931 standard.

## Applied Standard

**Schematron ISO/IEC 19757-3**: Business rules validation language for XML
- Semantic validation (beyond XSD syntax)
- European EN 16931 business rules
- French-specific Factur-X rules
- Arithmetic calculations and data consistency

## Profiles and validated rules

### MINIMUM (45 rules)
- Unique invoice identifier
- Dates (issue, due date)
- Party identifiers (SIRET/SIREN)
- Total gross amount

### BASIC (102 rules)
- All MINIMUM rules
- Detailed invoice lines
- Basic VAT calculations
- Payment methods
- References (order, contract)

### EN16931 (178 rules)
- All BASIC rules
- **European rules (BR-xx)**: 81 business rules
- **French rules (FR-xx)**: 12 France-specific rules
- **Advanced calculations (CR-xx)**: 32 calculation rules
- **Standardized codes (CL-xx)**: 52 code lists

### EXTENDED (210+ rules)
- All EN16931 rules
- Logistics information
- Advanced accounting data
- Multiple external references

## Checks performed

### 1. Syntax validation
- Correct XML parsing (UTF-8, well-formed)
- UN/CEFACT namespaces present
- Hierarchical structure respected

### 2. Business rules (BR-xx)
Examples:
- `BR-1`: Invoice total must equal sum of line totals + document-level amounts
- `BR-CO-10`: Sum of VAT base amounts must equal invoice net total
- `BR-16`: Invoice currency code must be in ISO 4217 list

### 3. French rules (FR-xx)
Examples:
- `FR-1`: Supplier SIRET must have 14 digits
- `FR-2`: Customer SIRET must have 14 digits (if present)
- `FR-5`: Intra-EU VAT number must be in format FRxx999999999

### 4. Calculation rules (CR-xx)
- Net + VAT = Gross amounts
- Sum of lines = Document total
- Discounts and surcharges correctly applied
- Compliant rounding (2 decimals for amounts)

### 5. Standardized codes (CL-xx)
- ISO 3166-1 alpha-2 country codes
- ISO 4217 currency codes
- UN/ECE Rec 20 measurement units
- VAT codes (types, categories, exemptions)
- SchemeID for identifiers (0002=SIREN, 0009=SIRET, etc.)

## Validation process

1. **XSLT loading**: Schematron file converted to XSLT (Saxon-HE)
2. **Transformation**: Rules applied to XML
3. **Results analysis**: Extraction of errors (`failed-assert`) and warnings (`successful-report`)
4. **Report**: Structured list of non-conformities

## Responses

**200 OK**: Compliant XML
```json
{
  "message": "XML is compliant with EN16931 profile"
}
```

**400 Bad Request**: Non-compliant XML
```json
{
  "detail": [
    "[BR-1] Invoice total (120.00) does not match calculated sum (100.00 + 20.00)",
    "[FR-1] Supplier SIRET must contain exactly 14 digits"
  ]
}
```

## Use cases

- **Pre-validation**: Verify XML before PDF/A integration
- **Debugging**: Precisely identify generation errors
- **Testing**: Validate test or example XMLs
- **Compliance**: Ensure European and French rules are met
- **Development**: Quick testing without PDF generation

## Processing time

- MINIMUM profile: ~0.5 second
- EN16931 profile: ~1-2 seconds
- EXTENDED profile: ~2-3 seconds

### Example

* Bearer Authentication (HTTPBearer):

```python
import factpulse
from factpulse.models.validation_success_response import ValidationSuccessResponse
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
    api_instance = factpulse.InvoiceProcessingApi(api_client)
    xml_file = None # bytearray | Factur-X XML file to validate (.xml format).
    profile = factpulse.APIProfile() # APIProfile | Validation profile (MINIMUM, BASIC, EN16931, EXTENDED). (optional)

    try:
        # Validate an existing Factur-X XML
        api_response = api_instance.validate_xml_api_v1_processing_validate_xml_post(xml_file, profile=profile)
        print("The response of InvoiceProcessingApi->validate_xml_api_v1_processing_validate_xml_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceProcessingApi->validate_xml_api_v1_processing_validate_xml_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xml_file** | **bytearray**| Factur-X XML file to validate (.xml format). | 
 **profile** | [**APIProfile**](APIProfile.md)| Validation profile (MINIMUM, BASIC, EN16931, EXTENDED). | [optional] 

### Return type

[**ValidationSuccessResponse**](ValidationSuccessResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | XML does not comply with Factur-X profile rules |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

