# equinix.services.fabricv4.CloudRouterPackagesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cloud_router_package_by_code**](CloudRouterPackagesApi.md#get_cloud_router_package_by_code) | **GET** /fabric/v4/routerPackages/{routerPackageCode} | Get Package Details
[**get_cloud_router_packages**](CloudRouterPackagesApi.md#get_cloud_router_packages) | **GET** /fabric/v4/routerPackages | List Packages


# **get_cloud_router_package_by_code**
> CloudRouterPackage get_cloud_router_package_by_code(router_package_code)

Get Package Details

This API provides capability to retrieve user's Cloud Routers Package Details

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router_package import CloudRouterPackage
from equinix.services.fabricv4.models.router_package_code import RouterPackageCode
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
    api_instance = equinix.services.fabricv4.CloudRouterPackagesApi(api_client)
    router_package_code = equinix.services.fabricv4.RouterPackageCode() # RouterPackageCode | Equinix-assigned Cloud Router package identifier

    try:
        # Get Package Details
        api_response = api_instance.get_cloud_router_package_by_code(router_package_code)
        print("The response of CloudRouterPackagesApi->get_cloud_router_package_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRouterPackagesApi->get_cloud_router_package_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_package_code** | [**RouterPackageCode**](.md)| Equinix-assigned Cloud Router package identifier | 

### Return type

[**CloudRouterPackage**](CloudRouterPackage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Cloud Router Package details |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_router_packages**
> PackageResponse get_cloud_router_packages(offset=offset, limit=limit)

List Packages

This API provides capability to retrieve user's Cloud Routers Packages

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.package_response import PackageResponse
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
    api_instance = equinix.services.fabricv4.CloudRouterPackagesApi(api_client)
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # List Packages
        api_response = api_instance.get_cloud_router_packages(offset=offset, limit=limit)
        print("The response of CloudRouterPackagesApi->get_cloud_router_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRouterPackagesApi->get_cloud_router_packages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**PackageResponse**](PackageResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Cloud Router Packages |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

