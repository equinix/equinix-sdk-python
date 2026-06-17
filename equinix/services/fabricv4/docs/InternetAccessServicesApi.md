# equinix.services.fabricv4.InternetAccessServicesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_eia_service**](InternetAccessServicesApi.md#create_eia_service) | **POST** /fabric/v4/internetAccessServices | Creates Internet Access Service
[**delete_eia_service**](InternetAccessServicesApi.md#delete_eia_service) | **DELETE** /fabric/v4/internetAccessServices/{uuid} | Delete Internet Access Service by UUID
[**get_eia_service**](InternetAccessServicesApi.md#get_eia_service) | **GET** /fabric/v4/internetAccessServices/{uuid} | Retrieve Internet Access Service by UUID
[**patch_eia_service**](InternetAccessServicesApi.md#patch_eia_service) | **PATCH** /fabric/v4/internetAccessServices/{uuid} | Patch Internet Access Service by UUID
[**search_eia_services**](InternetAccessServicesApi.md#search_eia_services) | **POST** /fabric/v4/internetAccessServices/search | Search for Internet Access Services


# **create_eia_service**
> InternetAccessService create_eia_service(internet_access_post_request)

Creates Internet Access Service

Creates Internet Access Service

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.internet_access_post_request import InternetAccessPostRequest
from equinix.services.fabricv4.models.internet_access_service import InternetAccessService
from equinix.services.fabricv4.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix.services.fabricv4.Configuration(
    host = "https://api.equinix.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = equinix.services.fabricv4.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with equinix.services.fabricv4.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix.services.fabricv4.InternetAccessServicesApi(api_client)
    internet_access_post_request = equinix.services.fabricv4.InternetAccessPostRequest() # InternetAccessPostRequest | 

    try:
        # Creates Internet Access Service
        api_response = api_instance.create_eia_service(internet_access_post_request)
        print("The response of InternetAccessServicesApi->create_eia_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetAccessServicesApi->create_eia_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internet_access_post_request** | [**InternetAccessPostRequest**](InternetAccessPostRequest.md)|  | 

### Return type

[**InternetAccessService**](InternetAccessService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | EIA Service creation or update accepted |  -  |
**400** | Invalid input parameter |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_eia_service**
> InternetAccessService delete_eia_service(uuid)

Delete Internet Access Service by UUID

Delete Internet Access Service by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.internet_access_service import InternetAccessService
from equinix.services.fabricv4.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix.services.fabricv4.Configuration(
    host = "https://api.equinix.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = equinix.services.fabricv4.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with equinix.services.fabricv4.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix.services.fabricv4.InternetAccessServicesApi(api_client)
    uuid = 'uuid_example' # str | UUID of the EIA Service

    try:
        # Delete Internet Access Service by UUID
        api_response = api_instance.delete_eia_service(uuid)
        print("The response of InternetAccessServicesApi->delete_eia_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetAccessServicesApi->delete_eia_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the EIA Service | 

### Return type

[**InternetAccessService**](InternetAccessService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | EIA Service creation or update accepted |  -  |
**404** | EIA Service not found |  -  |
**409** | EIA Service cannot be deleted due to active products |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eia_service**
> InternetAccessService get_eia_service(uuid)

Retrieve Internet Access Service by UUID

Retrieve Internet Access Service by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.internet_access_service import InternetAccessService
from equinix.services.fabricv4.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix.services.fabricv4.Configuration(
    host = "https://api.equinix.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = equinix.services.fabricv4.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with equinix.services.fabricv4.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix.services.fabricv4.InternetAccessServicesApi(api_client)
    uuid = 'uuid_example' # str | UUID of the EIA Service

    try:
        # Retrieve Internet Access Service by UUID
        api_response = api_instance.get_eia_service(uuid)
        print("The response of InternetAccessServicesApi->get_eia_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetAccessServicesApi->get_eia_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the EIA Service | 

### Return type

[**InternetAccessService**](InternetAccessService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EIA Service retrieved successfully |  -  |
**404** | EIA Service not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_eia_service**
> InternetAccessService patch_eia_service(uuid, internet_access_patch_operation_update)

Patch Internet Access Service by UUID

Patch Internet Access Service by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.internet_access_patch_operation_update import InternetAccessPatchOperationUpdate
from equinix.services.fabricv4.models.internet_access_service import InternetAccessService
from equinix.services.fabricv4.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix.services.fabricv4.Configuration(
    host = "https://api.equinix.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = equinix.services.fabricv4.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with equinix.services.fabricv4.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix.services.fabricv4.InternetAccessServicesApi(api_client)
    uuid = 'uuid_example' # str | UUID of the EIA Service
    internet_access_patch_operation_update = [equinix.services.fabricv4.InternetAccessPatchOperationUpdate()] # List[InternetAccessPatchOperationUpdate] | 

    try:
        # Patch Internet Access Service by UUID
        api_response = api_instance.patch_eia_service(uuid, internet_access_patch_operation_update)
        print("The response of InternetAccessServicesApi->patch_eia_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetAccessServicesApi->patch_eia_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the EIA Service | 
 **internet_access_patch_operation_update** | [**List[InternetAccessPatchOperationUpdate]**](InternetAccessPatchOperationUpdate.md)|  | 

### Return type

[**InternetAccessService**](InternetAccessService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | EIA Service creation or update accepted |  -  |
**404** | EIA Service not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_eia_services**
> InternetAccessServices search_eia_services(internet_access_search_request)

Search for Internet Access Services

Search for Internet Access Services

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.internet_access_search_request import InternetAccessSearchRequest
from equinix.services.fabricv4.models.internet_access_services import InternetAccessServices
from equinix.services.fabricv4.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix.services.fabricv4.Configuration(
    host = "https://api.equinix.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = equinix.services.fabricv4.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with equinix.services.fabricv4.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix.services.fabricv4.InternetAccessServicesApi(api_client)
    internet_access_search_request = equinix.services.fabricv4.InternetAccessSearchRequest() # InternetAccessSearchRequest | 

    try:
        # Search for Internet Access Services
        api_response = api_instance.search_eia_services(internet_access_search_request)
        print("The response of InternetAccessServicesApi->search_eia_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetAccessServicesApi->search_eia_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internet_access_search_request** | [**InternetAccessSearchRequest**](InternetAccessSearchRequest.md)|  | 

### Return type

[**InternetAccessServices**](InternetAccessServices.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EIA Services retrieved successfully |  -  |
**400** | Invalid input parameter |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

