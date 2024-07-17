# equinix.services.fabricv4.CloudRoutersApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_router**](CloudRoutersApi.md#create_cloud_router) | **POST** /fabric/v4/routers | Create Routers
[**create_cloud_router_action**](CloudRoutersApi.md#create_cloud_router_action) | **POST** /fabric/v4/routers/{routerId}/actions | Route table actions
[**delete_cloud_router_by_uuid**](CloudRoutersApi.md#delete_cloud_router_by_uuid) | **DELETE** /fabric/v4/routers/{routerId} | Delete Routers
[**get_cloud_router_actions**](CloudRoutersApi.md#get_cloud_router_actions) | **GET** /fabric/v4/routers/{routerId}/actions | Get actions
[**get_cloud_router_by_uuid**](CloudRoutersApi.md#get_cloud_router_by_uuid) | **GET** /fabric/v4/routers/{routerId} | Get Routers
[**get_cloud_router_package_by_code**](CloudRoutersApi.md#get_cloud_router_package_by_code) | **GET** /fabric/v4/routerPackages/{routerPackageCode} | Get Package Details
[**get_cloud_router_packages**](CloudRoutersApi.md#get_cloud_router_packages) | **GET** /fabric/v4/routerPackages | List Packages
[**search_cloud_router_routes**](CloudRoutersApi.md#search_cloud_router_routes) | **POST** /fabric/v4/routers/{routerId}/routes/search | Search Route Table
[**search_cloud_routers**](CloudRoutersApi.md#search_cloud_routers) | **POST** /fabric/v4/routers/search | Search Routers
[**update_cloud_router_by_uuid**](CloudRoutersApi.md#update_cloud_router_by_uuid) | **PATCH** /fabric/v4/routers/{routerId} | Update Routers


# **create_cloud_router**
> CloudRouter create_cloud_router(cloud_router_post_request)

Create Routers

This API provides capability to create user's Cloud Routers

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router import CloudRouter
from equinix.services.fabricv4.models.cloud_router_post_request import CloudRouterPostRequest
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
    api_instance = equinix.services.fabricv4.CloudRoutersApi(api_client)
    cloud_router_post_request = equinix.services.fabricv4.CloudRouterPostRequest() # CloudRouterPostRequest | 

    try:
        # Create Routers
        api_response = api_instance.create_cloud_router(cloud_router_post_request)
        print("The response of CloudRoutersApi->create_cloud_router:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->create_cloud_router: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_router_post_request** | [**CloudRouterPostRequest**](CloudRouterPostRequest.md)|  | 

### Return type

[**CloudRouter**](CloudRouter.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Cloud Router object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_router_action**
> CloudRouterActionResponse create_cloud_router_action(router_id, cloud_router_action_request)

Route table actions

This API provides capability to refresh route table and bgp session summary information

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router_action_request import CloudRouterActionRequest
from equinix.services.fabricv4.models.cloud_router_action_response import CloudRouterActionResponse
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
    api_instance = equinix.services.fabricv4.CloudRoutersApi(api_client)
    router_id = 'router_id_example' # str | Router UUID
    cloud_router_action_request = equinix.services.fabricv4.CloudRouterActionRequest() # CloudRouterActionRequest | 

    try:
        # Route table actions
        api_response = api_instance.create_cloud_router_action(router_id, cloud_router_action_request)
        print("The response of CloudRoutersApi->create_cloud_router_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->create_cloud_router_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Router UUID | 
 **cloud_router_action_request** | [**CloudRouterActionRequest**](CloudRouterActionRequest.md)|  | 

### Return type

[**CloudRouterActionResponse**](CloudRouterActionResponse.md)

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
**404** | Not Found |  -  |
**415** | Internal server error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_router_by_uuid**
> delete_cloud_router_by_uuid(router_id)

Delete Routers

This API provides capability to delete user's Cloud Routers

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
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
    api_instance = equinix.services.fabricv4.CloudRoutersApi(api_client)
    router_id = 'router_id_example' # str | Cloud Router UUID

    try:
        # Delete Routers
        api_instance.delete_cloud_router_by_uuid(router_id)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->delete_cloud_router_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Cloud Router UUID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted Cloud Router Successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_router_actions**
> CloudRouterActionResponse get_cloud_router_actions(router_id, state=state)

Get actions

This API provides capability to fetch action status

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router_action_response import CloudRouterActionResponse
from equinix.services.fabricv4.models.cloud_router_action_state import CloudRouterActionState
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
    api_instance = equinix.services.fabricv4.CloudRoutersApi(api_client)
    router_id = 'router_id_example' # str | Router UUID
    state = equinix.services.fabricv4.CloudRouterActionState() # CloudRouterActionState | Action state (optional)

    try:
        # Get actions
        api_response = api_instance.get_cloud_router_actions(router_id, state=state)
        print("The response of CloudRoutersApi->get_cloud_router_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->get_cloud_router_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Router UUID | 
 **state** | [**CloudRouterActionState**](.md)| Action state | [optional] 

### Return type

[**CloudRouterActionResponse**](CloudRouterActionResponse.md)

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
**404** | Not Found |  -  |
**415** | Internal server error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_router_by_uuid**
> CloudRouter get_cloud_router_by_uuid(router_id)

Get Routers

This API provides capability to retrieve user's Cloud Routers

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router import CloudRouter
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
    api_instance = equinix.services.fabricv4.CloudRoutersApi(api_client)
    router_id = 'router_id_example' # str | Cloud Router UUID

    try:
        # Get Routers
        api_response = api_instance.get_cloud_router_by_uuid(router_id)
        print("The response of CloudRoutersApi->get_cloud_router_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->get_cloud_router_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Cloud Router UUID | 

### Return type

[**CloudRouter**](CloudRouter.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Cloud Router object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = equinix.services.fabricv4.CloudRoutersApi(api_client)
    router_package_code = equinix.services.fabricv4.RouterPackageCode() # RouterPackageCode | Equinix-assigned Cloud Router package identifier

    try:
        # Get Package Details
        api_response = api_instance.get_cloud_router_package_by_code(router_package_code)
        print("The response of CloudRoutersApi->get_cloud_router_package_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->get_cloud_router_package_by_code: %s\n" % e)
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
    api_instance = equinix.services.fabricv4.CloudRoutersApi(api_client)
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # List Packages
        api_response = api_instance.get_cloud_router_packages(offset=offset, limit=limit)
        print("The response of CloudRoutersApi->get_cloud_router_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->get_cloud_router_packages: %s\n" % e)
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

# **search_cloud_router_routes**
> RouteTableEntrySearchResponse search_cloud_router_routes(router_id, route_table_entry_search_request)

Search Route Table

The API provides capability to get list of user's Fabric Cloud Router route table entries using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_table_entry_search_request import RouteTableEntrySearchRequest
from equinix.services.fabricv4.models.route_table_entry_search_response import RouteTableEntrySearchResponse
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
    api_instance = equinix.services.fabricv4.CloudRoutersApi(api_client)
    router_id = 'router_id_example' # str | Router UUID
    route_table_entry_search_request = equinix.services.fabricv4.RouteTableEntrySearchRequest() # RouteTableEntrySearchRequest | 

    try:
        # Search Route Table
        api_response = api_instance.search_cloud_router_routes(router_id, route_table_entry_search_request)
        print("The response of CloudRoutersApi->search_cloud_router_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->search_cloud_router_routes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Router UUID | 
 **route_table_entry_search_request** | [**RouteTableEntrySearchRequest**](RouteTableEntrySearchRequest.md)|  | 

### Return type

[**RouteTableEntrySearchResponse**](RouteTableEntrySearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Internal server error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_cloud_routers**
> SearchResponse search_cloud_routers(cloud_router_search_request)

Search Routers

The API provides capability to get list of user's Cloud Routers using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router_search_request import CloudRouterSearchRequest
from equinix.services.fabricv4.models.search_response import SearchResponse
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
    api_instance = equinix.services.fabricv4.CloudRoutersApi(api_client)
    cloud_router_search_request = equinix.services.fabricv4.CloudRouterSearchRequest() # CloudRouterSearchRequest | 

    try:
        # Search Routers
        api_response = api_instance.search_cloud_routers(cloud_router_search_request)
        print("The response of CloudRoutersApi->search_cloud_routers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->search_cloud_routers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_router_search_request** | [**CloudRouterSearchRequest**](CloudRouterSearchRequest.md)|  | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_cloud_router_by_uuid**
> CloudRouter update_cloud_router_by_uuid(router_id, cloud_router_change_operation)

Update Routers

This API provides capability to update user's Cloud Routers

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router import CloudRouter
from equinix.services.fabricv4.models.cloud_router_change_operation import CloudRouterChangeOperation
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
    api_instance = equinix.services.fabricv4.CloudRoutersApi(api_client)
    router_id = 'router_id_example' # str | Cloud Router UUID
    cloud_router_change_operation = [equinix.services.fabricv4.CloudRouterChangeOperation()] # List[CloudRouterChangeOperation] | 

    try:
        # Update Routers
        api_response = api_instance.update_cloud_router_by_uuid(router_id, cloud_router_change_operation)
        print("The response of CloudRoutersApi->update_cloud_router_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->update_cloud_router_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Cloud Router UUID | 
 **cloud_router_change_operation** | [**List[CloudRouterChangeOperation]**](CloudRouterChangeOperation.md)|  | 

### Return type

[**CloudRouter**](CloudRouter.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Cloud Router object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

