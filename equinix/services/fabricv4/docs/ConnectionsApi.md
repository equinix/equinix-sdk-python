# equinix.services.fabricv4.ConnectionsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection**](ConnectionsApi.md#create_connection) | **POST** /fabric/v4/connections | Create Connection
[**create_connection_action**](ConnectionsApi.md#create_connection_action) | **POST** /fabric/v4/connections/{connectionId}/actions | Connection Actions
[**delete_connection_by_uuid**](ConnectionsApi.md#delete_connection_by_uuid) | **DELETE** /fabric/v4/connections/{connectionId} | Delete by ID
[**get_connection_by_uuid**](ConnectionsApi.md#get_connection_by_uuid) | **GET** /fabric/v4/connections/{connectionId} | Get Connection by ID
[**search_connections**](ConnectionsApi.md#search_connections) | **POST** /fabric/v4/connections/search | Search connections
[**update_connection_by_uuid**](ConnectionsApi.md#update_connection_by_uuid) | **PATCH** /fabric/v4/connections/{connectionId} | Update by ID
[**validate_connections**](ConnectionsApi.md#validate_connections) | **POST** /fabric/v4/connections/validate | Validate Connection


# **create_connection**
> Connection create_connection(connection_post_request)

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
    connection_post_request = equinix.services.fabricv4.ConnectionPostRequest() # ConnectionPostRequest | 

    try:
        # Create Connection
        api_response = api_instance.create_connection(connection_post_request)
        print("The response of ConnectionsApi->create_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->create_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_post_request** | [**ConnectionPostRequest**](ConnectionPostRequest.md)|  | 

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
**201** | Accept Connection Request |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connection_action**
> ConnectionAction create_connection_action(connection_id, connection_action_request)

Connection Actions

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
    connection_id = 'connection_id_example' # str | Connection Id
    connection_action_request = equinix.services.fabricv4.ConnectionActionRequest() # ConnectionActionRequest | 

    try:
        # Connection Actions
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

Delete by ID

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
        # Delete by ID
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
    connection_id = 'connection_id_example' # str | Connection Id
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

Search connections

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
    search_request = equinix.services.fabricv4.SearchRequest() # SearchRequest | 

    try:
        # Search connections
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
> Connection update_connection_by_uuid(connection_id, connection_change_operation)

Update by ID

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
    connection_id = 'connection_id_example' # str | Connection Id
    connection_change_operation = [equinix.services.fabricv4.ConnectionChangeOperation()] # List[ConnectionChangeOperation] | 

    try:
        # Update by ID
        api_response = api_instance.update_connection_by_uuid(connection_id, connection_change_operation)
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
**202** | Successful operation |  -  |
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
    validate_request = equinix.services.fabricv4.ValidateRequest() # ValidateRequest | 

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

