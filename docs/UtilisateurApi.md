# factpulse.UtilisateurApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**obtenir_infos_utilisateur_api_v1_moi_get**](UtilisateurApi.md#obtenir_infos_utilisateur_api_v1_moi_get) | **GET** /api/v1/moi | Obtenir les informations de l&#39;utilisateur connecté


# **obtenir_infos_utilisateur_api_v1_moi_get**
> object obtenir_infos_utilisateur_api_v1_moi_get()

Obtenir les informations de l'utilisateur connecté

Retourne les informations de l'utilisateur authentifié.

Cet endpoint permet de :
- Vérifier que l'authentification fonctionne
- Obtenir les détails du compte connecté
- Tester la validité du token JWT
- Consulter son quota de consommation

**Nécessite une authentification valide.**

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
    api_instance = factpulse.UtilisateurApi(api_client)

    try:
        # Obtenir les informations de l'utilisateur connecté
        api_response = api_instance.obtenir_infos_utilisateur_api_v1_moi_get()
        print("The response of UtilisateurApi->obtenir_infos_utilisateur_api_v1_moi_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilisateurApi->obtenir_infos_utilisateur_api_v1_moi_get: %s\n" % e)
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
**200** | Informations de l&#39;utilisateur |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

