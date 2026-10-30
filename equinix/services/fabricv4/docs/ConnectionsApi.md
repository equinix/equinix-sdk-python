# equinix.services.fabricv4.ConnectionsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection**](ConnectionsApi.md#create_connection) | **POST** /fabric/v4/connections | Create Connection
[**create_connection_action**](ConnectionsApi.md#create_connection_action) | **POST** /fabric/v4/connections/{connectionId}/actions | Create Connection Action
[**delete_connection_by_uuid**](ConnectionsApi.md#delete_connection_by_uuid) | **DELETE** /fabric/v4/connections/{connectionId} | Delete Connection by ID
[**get_connection_by_uuid**](ConnectionsApi.md#get_connection_by_uuid) | **GET** /fabric/v4/connections/{connectionId} | Get Connection by ID
[**search_connections**](ConnectionsApi.md#search_connections) | **POST** /fabric/v4/connections/search | Search Connections
[**update_connection_by_uuid**](ConnectionsApi.md#update_connection_by_uuid) | **PATCH** /fabric/v4/connections/{connectionId} | Update Connection by ID
[**validate_connections**](ConnectionsApi.md#validate_connections) | **POST** /fabric/v4/connections/validate | Validate Connection


# **create_connection**
> Connection create_connection(connection_post_request, dry_run=dry_run)

Create Connection

This API provides capability to create user's virtual connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection import Connection
from equinix.services.fabricv4.models.connection_post_request import ConnectionPostRequest
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
    api_instance = equinix.services.fabricv4.ConnectionsApi(api_client)
    connection_post_request = {"type":"EVPL_VC","name":"My-Port-2-Port-Connection-1","bandwidth":1000,"order":{"purchaseOrderNumber":"po1234","termLength":1},"aSide":{"accessPoint":{"type":"COLO","port":{"uuid":"a8ba52de-faae-43b5-b0b1-6904d37ee063"},"linkProtocol":{"type":"DOT1Q","vlanTag":1001}}},"zSide":{"accessPoint":{"type":"COLO","port":{"uuid":"a00cef6f-8e35-4794-9ff9-665e084e4e6d"},"linkProtocol":{"type":"DOT1Q","vlanTag":1001}}},"project":{"projectId":"ac4d34ca-0d9c-4bc2-9aab-1234567abcde"},"notifications":[{"type":"ALL","emails":["test@test.com"]}]} # ConnectionPostRequest | 
    dry_run = False # bool | option to verify that API calls will succeed (optional) (default to False)

    try:
        # Create Connection
        api_response = api_instance.create_connection(connection_post_request, dry_run=dry_run)
        print("The response of ConnectionsApi->create_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->create_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_post_request** | [**ConnectionPostRequest**](ConnectionPostRequest.md)|  | 
 **dry_run** | **bool**| option to verify that API calls will succeed | [optional] [default to False]

### Return type

[**Connection**](Connection.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**201** | Accept Connection Request |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connection_action**
> ConnectionAction create_connection_action(connection_id, connection_action_request)

Create Connection Action

This API provides capability to accept/reject user's virtual connection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_action import ConnectionAction
from equinix.services.fabricv4.models.connection_action_request import ConnectionActionRequest
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
    api_instance = equinix.services.fabricv4.ConnectionsApi(api_client)
    connection_id = '557400f8-d360-11e9-bb65-2a2ae2dbcce4' # str | Connection Id
    connection_action_request = {"type":"CONNECTION_CREATION_ACCEPTANCE","data":{"zSide":{"accessPoint":{"type":"COLO","port":{"uuid":"20d32a80-0d61-4333-bc03-707b591ae2f4"},"linkProtocol":{"type":"QINQ","vlanSTag":1002,"vlanCTag":1001}}}}} # ConnectionActionRequest | 

    try:
        # Create Connection Action
        api_response = api_instance.create_connection_action(connection_id, connection_action_request)
        print("The response of ConnectionsApi->create_connection_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->create_connection_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 
 **connection_action_request** | [**ConnectionActionRequest**](ConnectionActionRequest.md)|  | 

### Return type

[**ConnectionAction**](ConnectionAction.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection_by_uuid**
> Connection delete_connection_by_uuid(connection_id)

Delete Connection by ID

Delete Connection by ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection import Connection
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
    api_instance = equinix.services.fabricv4.ConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | Connection UUID

    try:
        # Delete Connection by ID
        api_response = api_instance.delete_connection_by_uuid(connection_id)
        print("The response of ConnectionsApi->delete_connection_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->delete_connection_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection UUID | 

### Return type

[**Connection**](Connection.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete Connection Request |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_by_uuid**
> Connection get_connection_by_uuid(connection_id, direction=direction)

Get Connection by ID

The API provides capability to get user's virtual connection details (Service Tokens, Access Points, Link Protocols, etc) by it's connection ID (UUID)

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection import Connection
from equinix.services.fabricv4.models.connection_direction import ConnectionDirection
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
    api_instance = equinix.services.fabricv4.ConnectionsApi(api_client)
    connection_id = '557400f8-d360-11e9-bb65-2a2ae2dbcce4' # str | Connection Id
    direction = equinix.services.fabricv4.ConnectionDirection() # ConnectionDirection | Connection Direction (optional)

    try:
        # Get Connection by ID
        api_response = api_instance.get_connection_by_uuid(connection_id, direction=direction)
        print("The response of ConnectionsApi->get_connection_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->get_connection_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 
 **direction** | [**ConnectionDirection**](.md)| Connection Direction | [optional] 

### Return type

[**Connection**](Connection.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_connections**
> ConnectionSearchResponse search_connections(search_request)

Search Connections

The API provides capability to get list of user's virtual connections using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_search_response import ConnectionSearchResponse
from equinix.services.fabricv4.models.search_request import SearchRequest
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
    api_instance = equinix.services.fabricv4.ConnectionsApi(api_client)
    search_request = {"filter":{"and":[{"property":"/direction","operator":"=","values":["OUTGOING"]}]},"pagination":{"limit":25,"offset":0},"sort":[{"property":"/changeLog/updatedDateTime","direction":"DESC"}]} # SearchRequest | 

    try:
        # Search Connections
        api_response = api_instance.search_connections(search_request)
        print("The response of ConnectionsApi->search_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->search_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)|  | 

### Return type

[**ConnectionSearchResponse**](ConnectionSearchResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection_by_uuid**
> Connection update_connection_by_uuid(connection_id, connection_change_operation, dry_run=dry_run)

Update Connection by ID

Update Connection by ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection import Connection
from equinix.services.fabricv4.models.connection_change_operation import ConnectionChangeOperation
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
    api_instance = equinix.services.fabricv4.ConnectionsApi(api_client)
    connection_id = '557400f8-d360-11e9-bb65-2a2ae2dbcce4' # str | Connection Id
    connection_change_operation = [{"op":"replace","path":"/name","value":"Conn-Name-2"}] # List[ConnectionChangeOperation] | 
    dry_run = False # bool | option to verify that API calls will succeed (optional) (default to False)

    try:
        # Update Connection by ID
        api_response = api_instance.update_connection_by_uuid(connection_id, connection_change_operation, dry_run=dry_run)
        print("The response of ConnectionsApi->update_connection_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->update_connection_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 
 **connection_change_operation** | [**List[ConnectionChangeOperation]**](ConnectionChangeOperation.md)|  | 
 **dry_run** | **bool**| option to verify that API calls will succeed | [optional] [default to False]

### Return type

[**Connection**](Connection.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_connections**
> ConnectionResponse validate_connections(validate_request)

Validate Connection

This API provides capability to validate by auth key

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_response import ConnectionResponse
from equinix.services.fabricv4.models.validate_request import ValidateRequest
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
    api_instance = equinix.services.fabricv4.ConnectionsApi(api_client)
    validate_request = {"filter":{"and":[{"property":"/zSide/accessPoint/authenticationKey","operator":"=","values":["xxx-xxx-xxx"]},{"property":"/zSide/accessPoint/profile/uuid","operator":"=","values":["xxx-xxx-xxx"]},{"property":"/zSide/accessPoint/sellerRegion","operator":"=","values":["San Jose 2"]}]}} # ValidateRequest | 

    try:
        # Validate Connection
        api_response = api_instance.validate_connections(validate_request)
        print("The response of ConnectionsApi->validate_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->validate_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_request** | [**ValidateRequest**](ValidateRequest.md)|  | 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

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

