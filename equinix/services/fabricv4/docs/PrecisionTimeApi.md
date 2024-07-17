# equinix.services.fabricv4.PrecisionTimeApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_time_services**](PrecisionTimeApi.md#create_time_services) | **POST** /fabric/v4/timeServices | Create Time Service
[**delete_time_service_by_id**](PrecisionTimeApi.md#delete_time_service_by_id) | **DELETE** /fabric/v4/timeServices/{serviceId} | Delete time service
[**get_time_services_by_id**](PrecisionTimeApi.md#get_time_services_by_id) | **GET** /fabric/v4/timeServices/{serviceId} | Get Time Service
[**get_time_services_connections_by_service_id**](PrecisionTimeApi.md#get_time_services_connections_by_service_id) | **GET** /fabric/v4/timeServices/{serviceId}/connections | Get Connection Links
[**get_time_services_package_by_code**](PrecisionTimeApi.md#get_time_services_package_by_code) | **GET** /fabric/v4/timeServicePackages/{packageCode} | Get Package By Code
[**get_time_services_packages**](PrecisionTimeApi.md#get_time_services_packages) | **GET** /fabric/v4/timeServicePackages | Get Packages
[**update_time_services_by_id**](PrecisionTimeApi.md#update_time_services_by_id) | **PATCH** /fabric/v4/timeServices/{serviceId} | Patch time service


# **create_time_services**
> PrecisionTimeServiceCreateResponse create_time_services(precision_time_service_request)

Create Time Service

The API provides capability to create timing service

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.precision_time_service_create_response import PrecisionTimeServiceCreateResponse
from equinix.services.fabricv4.models.precision_time_service_request import PrecisionTimeServiceRequest
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
    api_instance = equinix.services.fabricv4.PrecisionTimeApi(api_client)
    precision_time_service_request = equinix.services.fabricv4.PrecisionTimeServiceRequest() # PrecisionTimeServiceRequest | 

    try:
        # Create Time Service
        api_response = api_instance.create_time_services(precision_time_service_request)
        print("The response of PrecisionTimeApi->create_time_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrecisionTimeApi->create_time_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **precision_time_service_request** | [**PrecisionTimeServiceRequest**](PrecisionTimeServiceRequest.md)|  | 

### Return type

[**PrecisionTimeServiceCreateResponse**](PrecisionTimeServiceCreateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_time_service_by_id**
> PrecisionTimeServiceCreateResponse delete_time_service_by_id(service_id)

Delete time service

Delete EPT service by it's uuid

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.precision_time_service_create_response import PrecisionTimeServiceCreateResponse
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
    api_instance = equinix.services.fabricv4.PrecisionTimeApi(api_client)
    service_id = 'service_id_example' # str | Service UUID

    try:
        # Delete time service
        api_response = api_instance.delete_time_service_by_id(service_id)
        print("The response of PrecisionTimeApi->delete_time_service_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrecisionTimeApi->delete_time_service_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service UUID | 

### Return type

[**PrecisionTimeServiceCreateResponse**](PrecisionTimeServiceCreateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_services_by_id**
> PrecisionTimeServiceCreateResponse get_time_services_by_id(service_id)

Get Time Service

The API provides capability to get precision timing service's details

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.precision_time_service_create_response import PrecisionTimeServiceCreateResponse
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
    api_instance = equinix.services.fabricv4.PrecisionTimeApi(api_client)
    service_id = 'service_id_example' # str | Service UUID

    try:
        # Get Time Service
        api_response = api_instance.get_time_services_by_id(service_id)
        print("The response of PrecisionTimeApi->get_time_services_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrecisionTimeApi->get_time_services_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service UUID | 

### Return type

[**PrecisionTimeServiceCreateResponse**](PrecisionTimeServiceCreateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_services_connections_by_service_id**
> PrecisionTimeServiceConnectionsResponse get_time_services_connections_by_service_id(service_id)

Get Connection Links

The API provides capability to get prevision timing service's details

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.precision_time_service_connections_response import PrecisionTimeServiceConnectionsResponse
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
    api_instance = equinix.services.fabricv4.PrecisionTimeApi(api_client)
    service_id = 'service_id_example' # str | Service UUID

    try:
        # Get Connection Links
        api_response = api_instance.get_time_services_connections_by_service_id(service_id)
        print("The response of PrecisionTimeApi->get_time_services_connections_by_service_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrecisionTimeApi->get_time_services_connections_by_service_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service UUID | 

### Return type

[**PrecisionTimeServiceConnectionsResponse**](PrecisionTimeServiceConnectionsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return Time Service Connection |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_services_package_by_code**
> PrecisionTimePackageResponse get_time_services_package_by_code(package_code)

Get Package By Code

The API provides capability to get timing service's package by code

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_time_services_package_by_code_package_code_parameter import GetTimeServicesPackageByCodePackageCodeParameter
from equinix.services.fabricv4.models.precision_time_package_response import PrecisionTimePackageResponse
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
    api_instance = equinix.services.fabricv4.PrecisionTimeApi(api_client)
    package_code = equinix.services.fabricv4.GetTimeServicesPackageByCodePackageCodeParameter() # GetTimeServicesPackageByCodePackageCodeParameter | Package Code

    try:
        # Get Package By Code
        api_response = api_instance.get_time_services_package_by_code(package_code)
        print("The response of PrecisionTimeApi->get_time_services_package_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrecisionTimeApi->get_time_services_package_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_code** | [**GetTimeServicesPackageByCodePackageCodeParameter**](.md)| Package Code | 

### Return type

[**PrecisionTimePackageResponse**](PrecisionTimePackageResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_services_packages**
> PrecisionTimeServicePackagesResponse get_time_services_packages()

Get Packages

The API provides capability to get timing service's packages

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.precision_time_service_packages_response import PrecisionTimeServicePackagesResponse
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
    api_instance = equinix.services.fabricv4.PrecisionTimeApi(api_client)

    try:
        # Get Packages
        api_response = api_instance.get_time_services_packages()
        print("The response of PrecisionTimeApi->get_time_services_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrecisionTimeApi->get_time_services_packages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PrecisionTimeServicePackagesResponse**](PrecisionTimeServicePackagesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_time_services_by_id**
> PrecisionTimeServiceCreateResponse update_time_services_by_id(service_id, precision_time_change_operation)

Patch time service

The API provides capability to update timing service

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.precision_time_change_operation import PrecisionTimeChangeOperation
from equinix.services.fabricv4.models.precision_time_service_create_response import PrecisionTimeServiceCreateResponse
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
    api_instance = equinix.services.fabricv4.PrecisionTimeApi(api_client)
    service_id = 'service_id_example' # str | Service UUID
    precision_time_change_operation = [equinix.services.fabricv4.PrecisionTimeChangeOperation()] # List[PrecisionTimeChangeOperation] | 

    try:
        # Patch time service
        api_response = api_instance.update_time_services_by_id(service_id, precision_time_change_operation)
        print("The response of PrecisionTimeApi->update_time_services_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrecisionTimeApi->update_time_services_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service UUID | 
 **precision_time_change_operation** | [**List[PrecisionTimeChangeOperation]**](PrecisionTimeChangeOperation.md)|  | 

### Return type

[**PrecisionTimeServiceCreateResponse**](PrecisionTimeServiceCreateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

