# equinix.services.fabricv4.RoutingProtocolsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection_routing_protocol**](RoutingProtocolsApi.md#create_connection_routing_protocol) | **POST** /fabric/v4/connections/{connectionId}/routingProtocols | Create Protocol
[**create_connection_routing_protocols_in_bulk**](RoutingProtocolsApi.md#create_connection_routing_protocols_in_bulk) | **POST** /fabric/v4/connections/{connectionId}/routingProtocols/bulk | Bulk Create Protocol
[**delete_connection_routing_protocol_by_uuid**](RoutingProtocolsApi.md#delete_connection_routing_protocol_by_uuid) | **DELETE** /fabric/v4/connections/{connectionId}/routingProtocols/{routingProtocolId} | Delete Protocol
[**get_connection_routing_protocol_all_bgp_actions**](RoutingProtocolsApi.md#get_connection_routing_protocol_all_bgp_actions) | **GET** /fabric/v4/connections/{connectionId}/routingProtocols/{routingProtocolId}/actions | Get BGP Actions
[**get_connection_routing_protocol_by_uuid**](RoutingProtocolsApi.md#get_connection_routing_protocol_by_uuid) | **GET** /fabric/v4/connections/{connectionId}/routingProtocols/{routingProtocolId} | Get Protocol
[**get_connection_routing_protocols**](RoutingProtocolsApi.md#get_connection_routing_protocols) | **GET** /fabric/v4/connections/{connectionId}/routingProtocols | GetRoutingProtocols
[**get_connection_routing_protocols_bgp_action_by_uuid**](RoutingProtocolsApi.md#get_connection_routing_protocols_bgp_action_by_uuid) | **GET** /fabric/v4/connections/{connectionId}/routingProtocols/{routingProtocolId}/actions/{actionId} | Get BGP Action
[**get_connection_routing_protocols_change_by_uuid**](RoutingProtocolsApi.md#get_connection_routing_protocols_change_by_uuid) | **GET** /fabric/v4/connections/{connectionId}/routingProtocols/{routingProtocolId}/changes/{changeId} | Get Change By ID
[**get_connection_routing_protocols_changes**](RoutingProtocolsApi.md#get_connection_routing_protocols_changes) | **GET** /fabric/v4/connections/{connectionId}/routingProtocols/{routingProtocolId}/changes | Get Changes
[**patch_connection_routing_protocol_by_uuid**](RoutingProtocolsApi.md#patch_connection_routing_protocol_by_uuid) | **PATCH** /fabric/v4/connections/{connectionId}/routingProtocols/{routingProtocolId} | Patch Protocol
[**post_connection_routing_protocol_bgp_action_by_uuid**](RoutingProtocolsApi.md#post_connection_routing_protocol_bgp_action_by_uuid) | **POST** /fabric/v4/connections/{connectionId}/routingProtocols/{routingProtocolId}/actions | Clear/Reset BGP
[**replace_connection_routing_protocol_by_uuid**](RoutingProtocolsApi.md#replace_connection_routing_protocol_by_uuid) | **PUT** /fabric/v4/connections/{connectionId}/routingProtocols/{routingProtocolId} | Replace Protocol
[**validate_routing_protocol**](RoutingProtocolsApi.md#validate_routing_protocol) | **POST** /fabric/v4/routers/{routerId}/validate | Validate Subnet


# **create_connection_routing_protocol**
> RoutingProtocolData create_connection_routing_protocol(connection_id, routing_protocol_base)

Create Protocol

This API provides capability to create Routing Protocol for connections

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.routing_protocol_base import RoutingProtocolBase
from equinix.services.fabricv4.models.routing_protocol_data import RoutingProtocolData
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    connection_id = 'connection_id_example' # str | Connection Id
    routing_protocol_base = equinix.services.fabricv4.RoutingProtocolBase() # RoutingProtocolBase | 

    try:
        # Create Protocol
        api_response = api_instance.create_connection_routing_protocol(connection_id, routing_protocol_base)
        print("The response of RoutingProtocolsApi->create_connection_routing_protocol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->create_connection_routing_protocol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 
 **routing_protocol_base** | [**RoutingProtocolBase**](RoutingProtocolBase.md)|  | 

### Return type

[**RoutingProtocolData**](RoutingProtocolData.md)

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
**404** | Connection ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connection_routing_protocols_in_bulk**
> GetResponse create_connection_routing_protocols_in_bulk(connection_id, connection_routing_protocol_post_request)

Bulk Create Protocol

This API provides capability to create Routing Protocol for connections

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_routing_protocol_post_request import ConnectionRoutingProtocolPostRequest
from equinix.services.fabricv4.models.get_response import GetResponse
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    connection_id = 'connection_id_example' # str | Connection Id
    connection_routing_protocol_post_request = equinix.services.fabricv4.ConnectionRoutingProtocolPostRequest() # ConnectionRoutingProtocolPostRequest | 

    try:
        # Bulk Create Protocol
        api_response = api_instance.create_connection_routing_protocols_in_bulk(connection_id, connection_routing_protocol_post_request)
        print("The response of RoutingProtocolsApi->create_connection_routing_protocols_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->create_connection_routing_protocols_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 
 **connection_routing_protocol_post_request** | [**ConnectionRoutingProtocolPostRequest**](ConnectionRoutingProtocolPostRequest.md)|  | 

### Return type

[**GetResponse**](GetResponse.md)

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
**404** | Connection ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection_routing_protocol_by_uuid**
> RoutingProtocolData delete_connection_routing_protocol_by_uuid(routing_protocol_id, connection_id)

Delete Protocol

This API provides capability to delete Routing Protocols on virtual connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.routing_protocol_data import RoutingProtocolData
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    routing_protocol_id = 'routing_protocol_id_example' # str | Routing Protocol Id
    connection_id = 'connection_id_example' # str | Connection Id

    try:
        # Delete Protocol
        api_response = api_instance.delete_connection_routing_protocol_by_uuid(routing_protocol_id, connection_id)
        print("The response of RoutingProtocolsApi->delete_connection_routing_protocol_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->delete_connection_routing_protocol_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_protocol_id** | **str**| Routing Protocol Id | 
 **connection_id** | **str**| Connection Id | 

### Return type

[**RoutingProtocolData**](RoutingProtocolData.md)

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
**404** | Connection ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_routing_protocol_all_bgp_actions**
> BGPActionsBulkData get_connection_routing_protocol_all_bgp_actions(routing_protocol_id, connection_id, offset=offset, limit=limit)

Get BGP Actions

This API provides capability to get all BGP actions status

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.bgp_actions_bulk_data import BGPActionsBulkData
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    routing_protocol_id = 'routing_protocol_id_example' # str | Routing Protocol Id
    connection_id = 'connection_id_example' # str | Connection Id
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get BGP Actions
        api_response = api_instance.get_connection_routing_protocol_all_bgp_actions(routing_protocol_id, connection_id, offset=offset, limit=limit)
        print("The response of RoutingProtocolsApi->get_connection_routing_protocol_all_bgp_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->get_connection_routing_protocol_all_bgp_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_protocol_id** | **str**| Routing Protocol Id | 
 **connection_id** | **str**| Connection Id | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**BGPActionsBulkData**](BGPActionsBulkData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric BGP Action object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Connection ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_routing_protocol_by_uuid**
> RoutingProtocolData get_connection_routing_protocol_by_uuid(routing_protocol_id, connection_id)

Get Protocol

This API provides capability to accept/reject user's virtual connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.routing_protocol_data import RoutingProtocolData
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    routing_protocol_id = 'routing_protocol_id_example' # str | Routing Protocol Id
    connection_id = 'connection_id_example' # str | Connection Id

    try:
        # Get Protocol
        api_response = api_instance.get_connection_routing_protocol_by_uuid(routing_protocol_id, connection_id)
        print("The response of RoutingProtocolsApi->get_connection_routing_protocol_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->get_connection_routing_protocol_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_protocol_id** | **str**| Routing Protocol Id | 
 **connection_id** | **str**| Connection Id | 

### Return type

[**RoutingProtocolData**](RoutingProtocolData.md)

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
**404** | Connection ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_routing_protocols**
> GetResponse get_connection_routing_protocols(connection_id, offset=offset, limit=limit)

GetRoutingProtocols

This API provides capability to get Routing Protocols for connections

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_response import GetResponse
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    connection_id = 'connection_id_example' # str | Connection Id
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # GetRoutingProtocols
        api_response = api_instance.get_connection_routing_protocols(connection_id, offset=offset, limit=limit)
        print("The response of RoutingProtocolsApi->get_connection_routing_protocols:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->get_connection_routing_protocols: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**GetResponse**](GetResponse.md)

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
**404** | Connection ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_routing_protocols_bgp_action_by_uuid**
> BGPActionData get_connection_routing_protocols_bgp_action_by_uuid(connection_id, routing_protocol_id, action_id)

Get BGP Action

This API provides capability to retrieve specific BGP action

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.bgp_action_data import BGPActionData
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    connection_id = 'connection_id_example' # str | Connection Id
    routing_protocol_id = 'routing_protocol_id_example' # str | Routing Protocol Id
    action_id = 'action_id_example' # str | BGP Action UUID

    try:
        # Get BGP Action
        api_response = api_instance.get_connection_routing_protocols_bgp_action_by_uuid(connection_id, routing_protocol_id, action_id)
        print("The response of RoutingProtocolsApi->get_connection_routing_protocols_bgp_action_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->get_connection_routing_protocols_bgp_action_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 
 **routing_protocol_id** | **str**| Routing Protocol Id | 
 **action_id** | **str**| BGP Action UUID | 

### Return type

[**BGPActionData**](BGPActionData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric BGP Action object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Connection ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_routing_protocols_change_by_uuid**
> RoutingProtocolChangeData get_connection_routing_protocols_change_by_uuid(connection_id, routing_protocol_id, change_id)

Get Change By ID

This API provides capability to retrieve specific Routing Protocol Change

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.routing_protocol_change_data import RoutingProtocolChangeData
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    connection_id = 'connection_id_example' # str | Connection Id
    routing_protocol_id = 'routing_protocol_id_example' # str | Routing Protocol Id
    change_id = 'change_id_example' # str | Routing Protocol Change UUID

    try:
        # Get Change By ID
        api_response = api_instance.get_connection_routing_protocols_change_by_uuid(connection_id, routing_protocol_id, change_id)
        print("The response of RoutingProtocolsApi->get_connection_routing_protocols_change_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->get_connection_routing_protocols_change_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 
 **routing_protocol_id** | **str**| Routing Protocol Id | 
 **change_id** | **str**| Routing Protocol Change UUID | 

### Return type

[**RoutingProtocolChangeData**](RoutingProtocolChangeData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Routing Protocol Change object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Connection ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_routing_protocols_changes**
> RoutingProtocolChangeDataResponse get_connection_routing_protocols_changes(connection_id, routing_protocol_id, offset=offset, limit=limit)

Get Changes

This API provides capability to retrieve user's Routing Protocol Changes

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.routing_protocol_change_data_response import RoutingProtocolChangeDataResponse
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    connection_id = 'connection_id_example' # str | Connection Id
    routing_protocol_id = 'routing_protocol_id_example' # str | Routing Protocol Id
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get Changes
        api_response = api_instance.get_connection_routing_protocols_changes(connection_id, routing_protocol_id, offset=offset, limit=limit)
        print("The response of RoutingProtocolsApi->get_connection_routing_protocols_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->get_connection_routing_protocols_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 
 **routing_protocol_id** | **str**| Routing Protocol Id | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**RoutingProtocolChangeDataResponse**](RoutingProtocolChangeDataResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Routing Protocol Change object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Connection ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_connection_routing_protocol_by_uuid**
> RoutingProtocolData patch_connection_routing_protocol_by_uuid(routing_protocol_id, connection_id, connection_change_operation)

Patch Protocol

This API provides capability to partially update Routing Protocols on a virtual connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_change_operation import ConnectionChangeOperation
from equinix.services.fabricv4.models.routing_protocol_data import RoutingProtocolData
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    routing_protocol_id = 'routing_protocol_id_example' # str | Routing Protocol Id
    connection_id = 'connection_id_example' # str | Connection Id
    connection_change_operation = [equinix.services.fabricv4.ConnectionChangeOperation()] # List[ConnectionChangeOperation] | 

    try:
        # Patch Protocol
        api_response = api_instance.patch_connection_routing_protocol_by_uuid(routing_protocol_id, connection_id, connection_change_operation)
        print("The response of RoutingProtocolsApi->patch_connection_routing_protocol_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->patch_connection_routing_protocol_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_protocol_id** | **str**| Routing Protocol Id | 
 **connection_id** | **str**| Connection Id | 
 **connection_change_operation** | [**List[ConnectionChangeOperation]**](ConnectionChangeOperation.md)|  | 

### Return type

[**RoutingProtocolData**](RoutingProtocolData.md)

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
**404** | Connection ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_connection_routing_protocol_bgp_action_by_uuid**
> BGPActionData post_connection_routing_protocol_bgp_action_by_uuid(routing_protocol_id, connection_id, bgp_action_request)

Clear/Reset BGP

This API provides capability to clear/reset Routing Protocols BGP session

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.bgp_action_data import BGPActionData
from equinix.services.fabricv4.models.bgp_action_request import BGPActionRequest
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    routing_protocol_id = 'routing_protocol_id_example' # str | Routing Protocol Id
    connection_id = 'connection_id_example' # str | Connection Id
    bgp_action_request = equinix.services.fabricv4.BGPActionRequest() # BGPActionRequest | 

    try:
        # Clear/Reset BGP
        api_response = api_instance.post_connection_routing_protocol_bgp_action_by_uuid(routing_protocol_id, connection_id, bgp_action_request)
        print("The response of RoutingProtocolsApi->post_connection_routing_protocol_bgp_action_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->post_connection_routing_protocol_bgp_action_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_protocol_id** | **str**| Routing Protocol Id | 
 **connection_id** | **str**| Connection Id | 
 **bgp_action_request** | [**BGPActionRequest**](BGPActionRequest.md)|  | 

### Return type

[**BGPActionData**](BGPActionData.md)

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
**404** | Connection ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_connection_routing_protocol_by_uuid**
> RoutingProtocolData replace_connection_routing_protocol_by_uuid(routing_protocol_id, connection_id, routing_protocol_base)

Replace Protocol

This API provides capability to replace complete Routing Protocols on a virtual connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.routing_protocol_base import RoutingProtocolBase
from equinix.services.fabricv4.models.routing_protocol_data import RoutingProtocolData
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    routing_protocol_id = 'routing_protocol_id_example' # str | Routing Protocol Id
    connection_id = 'connection_id_example' # str | Connection Id
    routing_protocol_base = equinix.services.fabricv4.RoutingProtocolBase() # RoutingProtocolBase | 

    try:
        # Replace Protocol
        api_response = api_instance.replace_connection_routing_protocol_by_uuid(routing_protocol_id, connection_id, routing_protocol_base)
        print("The response of RoutingProtocolsApi->replace_connection_routing_protocol_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->replace_connection_routing_protocol_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_protocol_id** | **str**| Routing Protocol Id | 
 **connection_id** | **str**| Connection Id | 
 **routing_protocol_base** | [**RoutingProtocolBase**](RoutingProtocolBase.md)|  | 

### Return type

[**RoutingProtocolData**](RoutingProtocolData.md)

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
**404** | Connection ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_routing_protocol**
> ValidateSubnetResponse validate_routing_protocol(router_id, validate_request)

Validate Subnet

This API provides capability to validate all subnets associated with any connection in the given FCR

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.validate_request import ValidateRequest
from equinix.services.fabricv4.models.validate_subnet_response import ValidateSubnetResponse
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
    api_instance = equinix.services.fabricv4.RoutingProtocolsApi(api_client)
    router_id = 'router_id_example' # str | Cloud Router UUID
    validate_request = equinix.services.fabricv4.ValidateRequest() # ValidateRequest | 

    try:
        # Validate Subnet
        api_response = api_instance.validate_routing_protocol(router_id, validate_request)
        print("The response of RoutingProtocolsApi->validate_routing_protocol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingProtocolsApi->validate_routing_protocol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Cloud Router UUID | 
 **validate_request** | [**ValidateRequest**](ValidateRequest.md)|  | 

### Return type

[**ValidateSubnetResponse**](ValidateSubnetResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

