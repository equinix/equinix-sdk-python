# equinix.services.fabricv4.RouteFiltersApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_connection_route_filter**](RouteFiltersApi.md#attach_connection_route_filter) | **PUT** /fabric/v4/connections/{connectionId}/routeFilters/{routeFilterId} | Attach Route Filter
[**create_route_filter**](RouteFiltersApi.md#create_route_filter) | **POST** /fabric/v4/routeFilters | Create Route Filters
[**delete_route_filter_by_uuid**](RouteFiltersApi.md#delete_route_filter_by_uuid) | **DELETE** /fabric/v4/routeFilters/{routeFilterId} | Delete Route Filter
[**detach_connection_route_filter**](RouteFiltersApi.md#detach_connection_route_filter) | **DELETE** /fabric/v4/connections/{connectionId}/routeFilters/{routeFilterId} | Detach Route Filter
[**get_connection_route_filter_by_uuid**](RouteFiltersApi.md#get_connection_route_filter_by_uuid) | **GET** /fabric/v4/connections/{connectionId}/routeFilters/{routeFilterId} | Get Route Filter
[**get_connection_route_filters**](RouteFiltersApi.md#get_connection_route_filters) | **GET** /fabric/v4/connections/{connectionId}/routeFilters | Get All Route Filters
[**get_route_filter_by_uuid**](RouteFiltersApi.md#get_route_filter_by_uuid) | **GET** /fabric/v4/routeFilters/{routeFilterId} | Get Route Filter By UUID
[**get_route_filter_change_by_uuid**](RouteFiltersApi.md#get_route_filter_change_by_uuid) | **GET** /fabric/v4/routeFilters/{routeFilterId}/changes/{changeId} | Get Change By ID
[**get_route_filter_changes**](RouteFiltersApi.md#get_route_filter_changes) | **GET** /fabric/v4/routeFilters/{routeFilterId}/changes | Get All Changes
[**get_route_filter_connections**](RouteFiltersApi.md#get_route_filter_connections) | **GET** /fabric/v4/routeFilters/{routeFilterId}/connections | Get All Connections on Route Filter
[**patch_route_filter_by_uuid**](RouteFiltersApi.md#patch_route_filter_by_uuid) | **PATCH** /fabric/v4/routeFilters/{routeFilterId} | Patch Route Filter
[**search_route_filters**](RouteFiltersApi.md#search_route_filters) | **POST** /fabric/v4/routeFilters/search | Search Route Filters


# **attach_connection_route_filter**
> ConnectionRouteFilterData attach_connection_route_filter(route_filter_id, connection_id, connection_route_filters_base)

Attach Route Filter

This API provides capability to attach a Route Filter to a Connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_route_filter_data import ConnectionRouteFilterData
from equinix.services.fabricv4.models.connection_route_filters_base import ConnectionRouteFiltersBase
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
    api_instance = equinix.services.fabricv4.RouteFiltersApi(api_client)
    route_filter_id = 'route_filter_id_example' # str | Route Filters Id
    connection_id = 'connection_id_example' # str | Connection Id
    connection_route_filters_base = equinix.services.fabricv4.ConnectionRouteFiltersBase() # ConnectionRouteFiltersBase | 

    try:
        # Attach Route Filter
        api_response = api_instance.attach_connection_route_filter(route_filter_id, connection_id, connection_route_filters_base)
        print("The response of RouteFiltersApi->attach_connection_route_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFiltersApi->attach_connection_route_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **connection_id** | **str**| Connection Id | 
 **connection_route_filters_base** | [**ConnectionRouteFiltersBase**](ConnectionRouteFiltersBase.md)|  | 

### Return type

[**ConnectionRouteFilterData**](ConnectionRouteFilterData.md)

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
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_route_filter**
> RouteFiltersData create_route_filter(route_filters_base)

Create Route Filters

This API provides capability to create a Route Filter

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filters_base import RouteFiltersBase
from equinix.services.fabricv4.models.route_filters_data import RouteFiltersData
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
    api_instance = equinix.services.fabricv4.RouteFiltersApi(api_client)
    route_filters_base = equinix.services.fabricv4.RouteFiltersBase() # RouteFiltersBase | 

    try:
        # Create Route Filters
        api_response = api_instance.create_route_filter(route_filters_base)
        print("The response of RouteFiltersApi->create_route_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFiltersApi->create_route_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filters_base** | [**RouteFiltersBase**](RouteFiltersBase.md)|  | 

### Return type

[**RouteFiltersData**](RouteFiltersData.md)

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
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_route_filter_by_uuid**
> RouteFiltersData delete_route_filter_by_uuid(route_filter_id)

Delete Route Filter

This API provides capability to delete a Route Filter

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filters_data import RouteFiltersData
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
    api_instance = equinix.services.fabricv4.RouteFiltersApi(api_client)
    route_filter_id = 'route_filter_id_example' # str | Route Filters Id

    try:
        # Delete Route Filter
        api_response = api_instance.delete_route_filter_by_uuid(route_filter_id)
        print("The response of RouteFiltersApi->delete_route_filter_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFiltersApi->delete_route_filter_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 

### Return type

[**RouteFiltersData**](RouteFiltersData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_connection_route_filter**
> ConnectionRouteFilterData detach_connection_route_filter(route_filter_id, connection_id)

Detach Route Filter

This API provides capability to detach a Route Filter from a Connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_route_filter_data import ConnectionRouteFilterData
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
    api_instance = equinix.services.fabricv4.RouteFiltersApi(api_client)
    route_filter_id = 'route_filter_id_example' # str | Route Filters Id
    connection_id = 'connection_id_example' # str | Connection Id

    try:
        # Detach Route Filter
        api_response = api_instance.detach_connection_route_filter(route_filter_id, connection_id)
        print("The response of RouteFiltersApi->detach_connection_route_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFiltersApi->detach_connection_route_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **connection_id** | **str**| Connection Id | 

### Return type

[**ConnectionRouteFilterData**](ConnectionRouteFilterData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_route_filter_by_uuid**
> ConnectionRouteFilterData get_connection_route_filter_by_uuid(route_filter_id, connection_id)

Get Route Filter

This API provides capability to view a specific Route Filter attached to a Connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_route_filter_data import ConnectionRouteFilterData
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
    api_instance = equinix.services.fabricv4.RouteFiltersApi(api_client)
    route_filter_id = 'route_filter_id_example' # str | Route Filters Id
    connection_id = 'connection_id_example' # str | Connection Id

    try:
        # Get Route Filter
        api_response = api_instance.get_connection_route_filter_by_uuid(route_filter_id, connection_id)
        print("The response of RouteFiltersApi->get_connection_route_filter_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFiltersApi->get_connection_route_filter_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **connection_id** | **str**| Connection Id | 

### Return type

[**ConnectionRouteFilterData**](ConnectionRouteFilterData.md)

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
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_route_filters**
> GetAllConnectionRouteFiltersResponse get_connection_route_filters(connection_id)

Get All Route Filters

This API provides capability to view all Route Filters attached to a Connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_all_connection_route_filters_response import GetAllConnectionRouteFiltersResponse
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
    api_instance = equinix.services.fabricv4.RouteFiltersApi(api_client)
    connection_id = 'connection_id_example' # str | Connection Id

    try:
        # Get All Route Filters
        api_response = api_instance.get_connection_route_filters(connection_id)
        print("The response of RouteFiltersApi->get_connection_route_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFiltersApi->get_connection_route_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 

### Return type

[**GetAllConnectionRouteFiltersResponse**](GetAllConnectionRouteFiltersResponse.md)

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
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_filter_by_uuid**
> RouteFiltersData get_route_filter_by_uuid(route_filter_id)

Get Route Filter By UUID

This API provides capability to view a Route Filter by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filters_data import RouteFiltersData
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
    api_instance = equinix.services.fabricv4.RouteFiltersApi(api_client)
    route_filter_id = 'route_filter_id_example' # str | Route Filters Id

    try:
        # Get Route Filter By UUID
        api_response = api_instance.get_route_filter_by_uuid(route_filter_id)
        print("The response of RouteFiltersApi->get_route_filter_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFiltersApi->get_route_filter_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 

### Return type

[**RouteFiltersData**](RouteFiltersData.md)

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
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_filter_change_by_uuid**
> RouteFilterChangeData get_route_filter_change_by_uuid(route_filter_id, change_id)

Get Change By ID

This API provides capability to retrieve a specific Route Filter's Changes

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filter_change_data import RouteFilterChangeData
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
    api_instance = equinix.services.fabricv4.RouteFiltersApi(api_client)
    route_filter_id = 'route_filter_id_example' # str | Route Filters Id
    change_id = 'change_id_example' # str | Routing Protocol Change UUID

    try:
        # Get Change By ID
        api_response = api_instance.get_route_filter_change_by_uuid(route_filter_id, change_id)
        print("The response of RouteFiltersApi->get_route_filter_change_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFiltersApi->get_route_filter_change_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **change_id** | **str**| Routing Protocol Change UUID | 

### Return type

[**RouteFilterChangeData**](RouteFilterChangeData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Route Filter Change object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Filter ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_filter_changes**
> RouteFilterChangeDataResponse get_route_filter_changes(route_filter_id, offset=offset, limit=limit)

Get All Changes

This API provides capability to retrieve all of a Route Filter's Changes

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filter_change_data_response import RouteFilterChangeDataResponse
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
    api_instance = equinix.services.fabricv4.RouteFiltersApi(api_client)
    route_filter_id = 'route_filter_id_example' # str | Route Filters Id
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get All Changes
        api_response = api_instance.get_route_filter_changes(route_filter_id, offset=offset, limit=limit)
        print("The response of RouteFiltersApi->get_route_filter_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFiltersApi->get_route_filter_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**RouteFilterChangeDataResponse**](RouteFilterChangeDataResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Route Filter Change object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Filter ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_filter_connections**
> GetRouteFilterGetConnectionsResponse get_route_filter_connections(route_filter_id)

Get All Connections on Route Filter

This API provides capability to view all Connections using the Route Filter

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_route_filter_get_connections_response import GetRouteFilterGetConnectionsResponse
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
    api_instance = equinix.services.fabricv4.RouteFiltersApi(api_client)
    route_filter_id = 'route_filter_id_example' # str | Route Filters Id

    try:
        # Get All Connections on Route Filter
        api_response = api_instance.get_route_filter_connections(route_filter_id)
        print("The response of RouteFiltersApi->get_route_filter_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFiltersApi->get_route_filter_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 

### Return type

[**GetRouteFilterGetConnectionsResponse**](GetRouteFilterGetConnectionsResponse.md)

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
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_route_filter_by_uuid**
> RouteFiltersData patch_route_filter_by_uuid(route_filter_id, route_filters_patch_request_item)

Patch Route Filter

This API provides capability to partially update a Route Filter

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filters_data import RouteFiltersData
from equinix.services.fabricv4.models.route_filters_patch_request_item import RouteFiltersPatchRequestItem
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
    api_instance = equinix.services.fabricv4.RouteFiltersApi(api_client)
    route_filter_id = 'route_filter_id_example' # str | Route Filters Id
    route_filters_patch_request_item = [equinix.services.fabricv4.RouteFiltersPatchRequestItem()] # List[RouteFiltersPatchRequestItem] | 

    try:
        # Patch Route Filter
        api_response = api_instance.patch_route_filter_by_uuid(route_filter_id, route_filters_patch_request_item)
        print("The response of RouteFiltersApi->patch_route_filter_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFiltersApi->patch_route_filter_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **route_filters_patch_request_item** | [**List[RouteFiltersPatchRequestItem]**](RouteFiltersPatchRequestItem.md)|  | 

### Return type

[**RouteFiltersData**](RouteFiltersData.md)

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
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_route_filters**
> RouteFiltersSearchResponse search_route_filters(route_filters_search_base)

Search Route Filters

This API provides capability to search Route Filters

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filters_search_base import RouteFiltersSearchBase
from equinix.services.fabricv4.models.route_filters_search_response import RouteFiltersSearchResponse
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
    api_instance = equinix.services.fabricv4.RouteFiltersApi(api_client)
    route_filters_search_base = equinix.services.fabricv4.RouteFiltersSearchBase() # RouteFiltersSearchBase | 

    try:
        # Search Route Filters
        api_response = api_instance.search_route_filters(route_filters_search_base)
        print("The response of RouteFiltersApi->search_route_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFiltersApi->search_route_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filters_search_base** | [**RouteFiltersSearchBase**](RouteFiltersSearchBase.md)|  | 

### Return type

[**RouteFiltersSearchResponse**](RouteFiltersSearchResponse.md)

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
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

