# equinix.services.fabricv4.PrecisionTimePackagesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_time_services_package_by_code**](PrecisionTimePackagesApi.md#get_time_services_package_by_code) | **GET** /fabric/v4/timeServicePackages/{packageCode} | Get Package By Code
[**get_time_services_packages**](PrecisionTimePackagesApi.md#get_time_services_packages) | **GET** /fabric/v4/timeServicePackages | Get Packages


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
    api_instance = equinix.services.fabricv4.PrecisionTimePackagesApi(api_client)
    package_code = equinix.services.fabricv4.GetTimeServicesPackageByCodePackageCodeParameter() # GetTimeServicesPackageByCodePackageCodeParameter | Package Code

    try:
        # Get Package By Code
        api_response = api_instance.get_time_services_package_by_code(package_code)
        print("The response of PrecisionTimePackagesApi->get_time_services_package_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrecisionTimePackagesApi->get_time_services_package_by_code: %s\n" % e)
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
    api_instance = equinix.services.fabricv4.PrecisionTimePackagesApi(api_client)

    try:
        # Get Packages
        api_response = api_instance.get_time_services_packages()
        print("The response of PrecisionTimePackagesApi->get_time_services_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrecisionTimePackagesApi->get_time_services_packages: %s\n" % e)
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

