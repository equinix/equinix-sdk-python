# equinix.services.fabricv4.NetworksApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network**](NetworksApi.md#create_network) | **POST** /fabric/v4/networks | Create Network
[**delete_network_by_uuid**](NetworksApi.md#delete_network_by_uuid) | **DELETE** /fabric/v4/networks/{networkId} | Delete Network By ID
[**get_connections_by_network_uuid**](NetworksApi.md#get_connections_by_network_uuid) | **GET** /fabric/v4/networks/{networkId}/connections | Get Connections
[**get_network_by_uuid**](NetworksApi.md#get_network_by_uuid) | **GET** /fabric/v4/networks/{networkId} | Get Network By ID
[**get_network_change_by_uuid**](NetworksApi.md#get_network_change_by_uuid) | **GET** /fabric/v4/networks/{networkId}/changes/{changeId} | Get Change By ID
[**get_network_changes**](NetworksApi.md#get_network_changes) | **GET** /fabric/v4/networks/{networkId}/changes | Get Network Changes
[**search_networks**](NetworksApi.md#search_networks) | **POST** /fabric/v4/networks/search | Search Network
[**update_network_by_uuid**](NetworksApi.md#update_network_by_uuid) | **PATCH** /fabric/v4/networks/{networkId} | Update Network By ID


# **create_network**
> Network create_network(network_post_request)

Create Network

This API provides capability to create user's Fabric Network

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.network import Network
from equinix.services.fabricv4.models.network_post_request import NetworkPostRequest
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
    api_instance = equinix.services.fabricv4.NetworksApi(api_client)
    network_post_request = equinix.services.fabricv4.NetworkPostRequest() # NetworkPostRequest | 

    try:
        # Create Network
        api_response = api_instance.create_network(network_post_request)
        print("The response of NetworksApi->create_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->create_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_post_request** | [**NetworkPostRequest**](NetworkPostRequest.md)|  | 

### Return type

[**Network**](Network.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Fabric Network Access point object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_by_uuid**
> Network delete_network_by_uuid(network_id)

Delete Network By ID

This API provides capability to delete user's Fabric Network

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.network import Network
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
    api_instance = equinix.services.fabricv4.NetworksApi(api_client)
    network_id = 'network_id_example' # str | Network UUID

    try:
        # Delete Network By ID
        api_response = api_instance.delete_network_by_uuid(network_id)
        print("The response of NetworksApi->delete_network_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->delete_network_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| Network UUID | 

### Return type

[**Network**](Network.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Fabric Network Access point object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections_by_network_uuid**
> NetworkConnections get_connections_by_network_uuid(network_id)

Get Connections

The API provides capability to get list of user's Fabric Network connections

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.network_connections import NetworkConnections
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
    api_instance = equinix.services.fabricv4.NetworksApi(api_client)
    network_id = 'network_id_example' # str | Network UUID

    try:
        # Get Connections
        api_response = api_instance.get_connections_by_network_uuid(network_id)
        print("The response of NetworksApi->get_connections_by_network_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->get_connections_by_network_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| Network UUID | 

### Return type

[**NetworkConnections**](NetworkConnections.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Network Access point object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_by_uuid**
> Network get_network_by_uuid(network_id)

Get Network By ID

This API provides capability to retrieve user's Fabric Network

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.network import Network
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
    api_instance = equinix.services.fabricv4.NetworksApi(api_client)
    network_id = 'network_id_example' # str | Network UUID

    try:
        # Get Network By ID
        api_response = api_instance.get_network_by_uuid(network_id)
        print("The response of NetworksApi->get_network_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->get_network_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| Network UUID | 

### Return type

[**Network**](Network.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Network Access point object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_change_by_uuid**
> NetworkChange get_network_change_by_uuid(network_id, change_id)

Get Change By ID

This API provides capability to retrieve user's Fabric Network Change

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.network_change import NetworkChange
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
    api_instance = equinix.services.fabricv4.NetworksApi(api_client)
    network_id = 'network_id_example' # str | Network UUID
    change_id = 'change_id_example' # str | Network Change UUID

    try:
        # Get Change By ID
        api_response = api_instance.get_network_change_by_uuid(network_id, change_id)
        print("The response of NetworksApi->get_network_change_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->get_network_change_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| Network UUID | 
 **change_id** | **str**| Network Change UUID | 

### Return type

[**NetworkChange**](NetworkChange.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Network Access point object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_changes**
> NetworkChangeResponse get_network_changes(network_id)

Get Network Changes

The API provides capability to get list of user's Fabric Network changes

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.network_change_response import NetworkChangeResponse
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
    api_instance = equinix.services.fabricv4.NetworksApi(api_client)
    network_id = 'network_id_example' # str | Network UUID

    try:
        # Get Network Changes
        api_response = api_instance.get_network_changes(network_id)
        print("The response of NetworksApi->get_network_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->get_network_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| Network UUID | 

### Return type

[**NetworkChangeResponse**](NetworkChangeResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Network Access point object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_networks**
> NetworkSearchResponse search_networks(network_search_request)

Search Network

The API provides capability to get list of user's Fabric Network using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.network_search_request import NetworkSearchRequest
from equinix.services.fabricv4.models.network_search_response import NetworkSearchResponse
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
    api_instance = equinix.services.fabricv4.NetworksApi(api_client)
    network_search_request = equinix.services.fabricv4.NetworkSearchRequest() # NetworkSearchRequest | 

    try:
        # Search Network
        api_response = api_instance.search_networks(network_search_request)
        print("The response of NetworksApi->search_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->search_networks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_search_request** | [**NetworkSearchRequest**](NetworkSearchRequest.md)|  | 

### Return type

[**NetworkSearchResponse**](NetworkSearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Network Access point object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_by_uuid**
> Network update_network_by_uuid(network_id, network_change_operation)

Update Network By ID

This API provides capability to update user's Fabric Network

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.network import Network
from equinix.services.fabricv4.models.network_change_operation import NetworkChangeOperation
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
    api_instance = equinix.services.fabricv4.NetworksApi(api_client)
    network_id = 'network_id_example' # str | Network UUID
    network_change_operation = [equinix.services.fabricv4.NetworkChangeOperation()] # List[NetworkChangeOperation] | 

    try:
        # Update Network By ID
        api_response = api_instance.update_network_by_uuid(network_id, network_change_operation)
        print("The response of NetworksApi->update_network_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->update_network_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| Network UUID | 
 **network_change_operation** | [**List[NetworkChangeOperation]**](NetworkChangeOperation.md)|  | 

### Return type

[**Network**](Network.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Network Access point object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

