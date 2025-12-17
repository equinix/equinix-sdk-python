# equinix.services.fabricv4.RouteAggregationsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_connection_route_aggregation**](RouteAggregationsApi.md#attach_connection_route_aggregation) | **PUT** /fabric/v4/connections/{connectionId}/routeAggregations/{routeAggregationId} | Attach Aggregation
[**create_route_aggregation**](RouteAggregationsApi.md#create_route_aggregation) | **POST** /fabric/v4/routeAggregations | Create Aggregations
[**delete_route_aggregation_by_uuid**](RouteAggregationsApi.md#delete_route_aggregation_by_uuid) | **DELETE** /fabric/v4/routeAggregations/{routeAggregationId} | Delete Aggregation
[**detach_connection_route_aggregation**](RouteAggregationsApi.md#detach_connection_route_aggregation) | **DELETE** /fabric/v4/connections/{connectionId}/routeAggregations/{routeAggregationId} | Detach Aggregation
[**get_connection_route_aggregation_by_uuid**](RouteAggregationsApi.md#get_connection_route_aggregation_by_uuid) | **GET** /fabric/v4/connections/{connectionId}/routeAggregations/{routeAggregationId} | Get Aggregation
[**get_connection_route_aggregations**](RouteAggregationsApi.md#get_connection_route_aggregations) | **GET** /fabric/v4/connections/{connectionId}/routeAggregations | Get All Aggregations
[**get_route_aggregation_by_uuid**](RouteAggregationsApi.md#get_route_aggregation_by_uuid) | **GET** /fabric/v4/routeAggregations/{routeAggregationId} | Get Aggregation
[**get_route_aggregation_change_by_uuid**](RouteAggregationsApi.md#get_route_aggregation_change_by_uuid) | **GET** /fabric/v4/routeAggregations/{routeAggregationId}/changes/{changeId} | Get Change By ID
[**get_route_aggregation_changes**](RouteAggregationsApi.md#get_route_aggregation_changes) | **GET** /fabric/v4/routeAggregations/{routeAggregationId}/changes | Get All Changes
[**get_route_aggregation_connections**](RouteAggregationsApi.md#get_route_aggregation_connections) | **GET** /fabric/v4/routeAggregations/{routeAggregationId}/connections | Get All Connections on Route Aggregation
[**patch_route_aggregation_by_uuid**](RouteAggregationsApi.md#patch_route_aggregation_by_uuid) | **PATCH** /fabric/v4/routeAggregations/{routeAggregationId} | Patch Aggregation
[**search_route_aggregations**](RouteAggregationsApi.md#search_route_aggregations) | **POST** /fabric/v4/routeAggregations/search | Search Aggregations


# **attach_connection_route_aggregation**
> ConnectionRouteAggregationData attach_connection_route_aggregation(route_aggregation_id, connection_id)

Attach Aggregation

This API provides capability to attach a Route Aggregation to a Connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_route_aggregation_data import ConnectionRouteAggregationData
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
    api_instance = equinix.services.fabricv4.RouteAggregationsApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    connection_id = 'connection_id_example' # str | Connection Id

    try:
        # Attach Aggregation
        api_response = api_instance.attach_connection_route_aggregation(route_aggregation_id, connection_id)
        print("The response of RouteAggregationsApi->attach_connection_route_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationsApi->attach_connection_route_aggregation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **connection_id** | **str**| Connection Id | 

### Return type

[**ConnectionRouteAggregationData**](ConnectionRouteAggregationData.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_route_aggregation**
> RouteAggregationsData create_route_aggregation(route_aggregations_base)

Create Aggregations

This API provides capability to create a Route Aggregation

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregations_base import RouteAggregationsBase
from equinix.services.fabricv4.models.route_aggregations_data import RouteAggregationsData
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
    api_instance = equinix.services.fabricv4.RouteAggregationsApi(api_client)
    route_aggregations_base = equinix.services.fabricv4.RouteAggregationsBase() # RouteAggregationsBase | 

    try:
        # Create Aggregations
        api_response = api_instance.create_route_aggregation(route_aggregations_base)
        print("The response of RouteAggregationsApi->create_route_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationsApi->create_route_aggregation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregations_base** | [**RouteAggregationsBase**](RouteAggregationsBase.md)|  | 

### Return type

[**RouteAggregationsData**](RouteAggregationsData.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_route_aggregation_by_uuid**
> RouteAggregationsData delete_route_aggregation_by_uuid(route_aggregation_id)

Delete Aggregation

This API provides capability to delete a Route Aggregation

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregations_data import RouteAggregationsData
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
    api_instance = equinix.services.fabricv4.RouteAggregationsApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id

    try:
        # Delete Aggregation
        api_response = api_instance.delete_route_aggregation_by_uuid(route_aggregation_id)
        print("The response of RouteAggregationsApi->delete_route_aggregation_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationsApi->delete_route_aggregation_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 

### Return type

[**RouteAggregationsData**](RouteAggregationsData.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_connection_route_aggregation**
> ConnectionRouteAggregationData detach_connection_route_aggregation(route_aggregation_id, connection_id)

Detach Aggregation

This API provides capability to detach a Route Aggregation from a Connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_route_aggregation_data import ConnectionRouteAggregationData
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
    api_instance = equinix.services.fabricv4.RouteAggregationsApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    connection_id = 'connection_id_example' # str | Connection Id

    try:
        # Detach Aggregation
        api_response = api_instance.detach_connection_route_aggregation(route_aggregation_id, connection_id)
        print("The response of RouteAggregationsApi->detach_connection_route_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationsApi->detach_connection_route_aggregation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **connection_id** | **str**| Connection Id | 

### Return type

[**ConnectionRouteAggregationData**](ConnectionRouteAggregationData.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_route_aggregation_by_uuid**
> ConnectionRouteAggregationData get_connection_route_aggregation_by_uuid(route_aggregation_id, connection_id)

Get Aggregation

This API provides capability to view a specific Route Aggregation attached to a Connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_route_aggregation_data import ConnectionRouteAggregationData
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
    api_instance = equinix.services.fabricv4.RouteAggregationsApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    connection_id = 'connection_id_example' # str | Connection Id

    try:
        # Get Aggregation
        api_response = api_instance.get_connection_route_aggregation_by_uuid(route_aggregation_id, connection_id)
        print("The response of RouteAggregationsApi->get_connection_route_aggregation_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationsApi->get_connection_route_aggregation_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **connection_id** | **str**| Connection Id | 

### Return type

[**ConnectionRouteAggregationData**](ConnectionRouteAggregationData.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_route_aggregations**
> GetAllConnectionRouteAggregationsResponse get_connection_route_aggregations(connection_id)

Get All Aggregations

This API provides capability to view all Route Aggregations attached to a Connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_all_connection_route_aggregations_response import GetAllConnectionRouteAggregationsResponse
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
    api_instance = equinix.services.fabricv4.RouteAggregationsApi(api_client)
    connection_id = 'connection_id_example' # str | Connection Id

    try:
        # Get All Aggregations
        api_response = api_instance.get_connection_route_aggregations(connection_id)
        print("The response of RouteAggregationsApi->get_connection_route_aggregations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationsApi->get_connection_route_aggregations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 

### Return type

[**GetAllConnectionRouteAggregationsResponse**](GetAllConnectionRouteAggregationsResponse.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_aggregation_by_uuid**
> RouteAggregationsData get_route_aggregation_by_uuid(route_aggregation_id)

Get Aggregation

This API provides capability to view a Route Aggregation by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregations_data import RouteAggregationsData
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
    api_instance = equinix.services.fabricv4.RouteAggregationsApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id

    try:
        # Get Aggregation
        api_response = api_instance.get_route_aggregation_by_uuid(route_aggregation_id)
        print("The response of RouteAggregationsApi->get_route_aggregation_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationsApi->get_route_aggregation_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 

### Return type

[**RouteAggregationsData**](RouteAggregationsData.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_aggregation_change_by_uuid**
> RouteAggregationChangeData get_route_aggregation_change_by_uuid(route_aggregation_id, change_id)

Get Change By ID

This API provides capability to retrieve a specific Route Aggregation's Changes

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregation_change_data import RouteAggregationChangeData
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
    api_instance = equinix.services.fabricv4.RouteAggregationsApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    change_id = 'change_id_example' # str | Routing Protocol Change UUID

    try:
        # Get Change By ID
        api_response = api_instance.get_route_aggregation_change_by_uuid(route_aggregation_id, change_id)
        print("The response of RouteAggregationsApi->get_route_aggregation_change_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationsApi->get_route_aggregation_change_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **change_id** | **str**| Routing Protocol Change UUID | 

### Return type

[**RouteAggregationChangeData**](RouteAggregationChangeData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Route Aggregation Change object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Aggregation ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_aggregation_changes**
> RouteAggregationChangeDataResponse get_route_aggregation_changes(route_aggregation_id, offset=offset, limit=limit)

Get All Changes

This API provides capability to retrieve all of a Route Aggregation's Changes

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregation_change_data_response import RouteAggregationChangeDataResponse
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
    api_instance = equinix.services.fabricv4.RouteAggregationsApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get All Changes
        api_response = api_instance.get_route_aggregation_changes(route_aggregation_id, offset=offset, limit=limit)
        print("The response of RouteAggregationsApi->get_route_aggregation_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationsApi->get_route_aggregation_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**RouteAggregationChangeDataResponse**](RouteAggregationChangeDataResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Route Aggregation Change object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Aggregation ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_aggregation_connections**
> GetRouteAggregationGetConnectionsResponse get_route_aggregation_connections(route_aggregation_id)

Get All Connections on Route Aggregation

This API provides capability to view all Connections using the Route Aggregation

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_route_aggregation_get_connections_response import GetRouteAggregationGetConnectionsResponse
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
    api_instance = equinix.services.fabricv4.RouteAggregationsApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id

    try:
        # Get All Connections on Route Aggregation
        api_response = api_instance.get_route_aggregation_connections(route_aggregation_id)
        print("The response of RouteAggregationsApi->get_route_aggregation_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationsApi->get_route_aggregation_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 

### Return type

[**GetRouteAggregationGetConnectionsResponse**](GetRouteAggregationGetConnectionsResponse.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_route_aggregation_by_uuid**
> RouteAggregationsData patch_route_aggregation_by_uuid(route_aggregation_id, route_aggregations_patch_request_item)

Patch Aggregation

This API provides capability to partially update a Route Aggregation

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregations_data import RouteAggregationsData
from equinix.services.fabricv4.models.route_aggregations_patch_request_item import RouteAggregationsPatchRequestItem
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
    api_instance = equinix.services.fabricv4.RouteAggregationsApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    route_aggregations_patch_request_item = [equinix.services.fabricv4.RouteAggregationsPatchRequestItem()] # List[RouteAggregationsPatchRequestItem] | 

    try:
        # Patch Aggregation
        api_response = api_instance.patch_route_aggregation_by_uuid(route_aggregation_id, route_aggregations_patch_request_item)
        print("The response of RouteAggregationsApi->patch_route_aggregation_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationsApi->patch_route_aggregation_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **route_aggregations_patch_request_item** | [**List[RouteAggregationsPatchRequestItem]**](RouteAggregationsPatchRequestItem.md)|  | 

### Return type

[**RouteAggregationsData**](RouteAggregationsData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_route_aggregations**
> RouteAggregationsSearchResponse search_route_aggregations(route_aggregations_search_base)

Search Aggregations

This API provides capability to search Route Aggregations

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregations_search_base import RouteAggregationsSearchBase
from equinix.services.fabricv4.models.route_aggregations_search_response import RouteAggregationsSearchResponse
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
    api_instance = equinix.services.fabricv4.RouteAggregationsApi(api_client)
    route_aggregations_search_base = equinix.services.fabricv4.RouteAggregationsSearchBase() # RouteAggregationsSearchBase | 

    try:
        # Search Aggregations
        api_response = api_instance.search_route_aggregations(route_aggregations_search_base)
        print("The response of RouteAggregationsApi->search_route_aggregations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationsApi->search_route_aggregations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregations_search_base** | [**RouteAggregationsSearchBase**](RouteAggregationsSearchBase.md)|  | 

### Return type

[**RouteAggregationsSearchResponse**](RouteAggregationsSearchResponse.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

