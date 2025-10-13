# equinix.services.fabricv4.CloudRoutersApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_router**](CloudRoutersApi.md#create_cloud_router) | **POST** /fabric/v4/routers | Create Routers
[**create_cloud_router_action**](CloudRoutersApi.md#create_cloud_router_action) | **POST** /fabric/v4/routers/{routerId}/actions | Create Route Table Action
[**create_cloud_router_command**](CloudRoutersApi.md#create_cloud_router_command) | **POST** /fabric/v4/routers/{routerId}/commands | Initiate Command
[**delete_cloud_router_by_uuid**](CloudRoutersApi.md#delete_cloud_router_by_uuid) | **DELETE** /fabric/v4/routers/{routerId} | Delete Routers
[**delete_cloud_router_command_by_uuid**](CloudRoutersApi.md#delete_cloud_router_command_by_uuid) | **DELETE** /fabric/v4/routers/{routerId}/commands/{commandId} | Delete Command
[**get_all_cloud_router_commands**](CloudRoutersApi.md#get_all_cloud_router_commands) | **GET** /fabric/v4/routers/{routerId}/commands | Get Commands
[**get_cloud_router_actions**](CloudRoutersApi.md#get_cloud_router_actions) | **GET** /fabric/v4/routers/{routerId}/actions | Get Route Table Actions
[**get_cloud_router_actions_by_uuid**](CloudRoutersApi.md#get_cloud_router_actions_by_uuid) | **GET** /fabric/v4/routers/{routerId}/actions/{actionId} | Get Route Table Action by ID
[**get_cloud_router_by_uuid**](CloudRoutersApi.md#get_cloud_router_by_uuid) | **GET** /fabric/v4/routers/{routerId} | Get Routers
[**get_cloud_router_command**](CloudRoutersApi.md#get_cloud_router_command) | **GET** /fabric/v4/routers/{routerId}/commands/{commandId} | Get Command
[**get_cloud_router_package_by_code**](CloudRoutersApi.md#get_cloud_router_package_by_code) | **GET** /fabric/v4/routerPackages/{routerPackageCode} | Get Package Details
[**get_cloud_router_packages**](CloudRoutersApi.md#get_cloud_router_packages) | **GET** /fabric/v4/routerPackages | List Packages
[**get_gateway_attachment_to_cloud_router_by_uuid**](CloudRoutersApi.md#get_gateway_attachment_to_cloud_router_by_uuid) | **GET** /fabric/v4/gateways/{gatewayId}/routers/{routerId} | Get Gateway Attachment details to a Cloud Router
[**list_gateway_attachments_to_cloud_router**](CloudRoutersApi.md#list_gateway_attachments_to_cloud_router) | **GET** /fabric/v4/gateways/{gatewayId}/routers | List Cloud Routers of a Gateway Attachment.
[**search_cloud_router_commands**](CloudRoutersApi.md#search_cloud_router_commands) | **POST** /fabric/v4/routers/{routerId}/commands/search | Search Commands
[**search_cloud_router_routes**](CloudRoutersApi.md#search_cloud_router_routes) | **POST** /fabric/v4/routers/{routerId}/routes/search | Search Route Table
[**search_cloud_routers**](CloudRoutersApi.md#search_cloud_routers) | **POST** /fabric/v4/routers/search | Search Routers
[**search_connection_advertised_routes**](CloudRoutersApi.md#search_connection_advertised_routes) | **POST** /fabric/v4/connections/{connectionId}/advertisedRoutes/search | Search Advertised Routes
[**search_connection_received_routes**](CloudRoutersApi.md#search_connection_received_routes) | **POST** /fabric/v4/connections/{connectionId}/receivedRoutes/search | Search Received Routes
[**search_router_actions**](CloudRoutersApi.md#search_router_actions) | **POST** /fabric/v4/routers/{routerId}/actions/search | Search Route Table Actions
[**update_cloud_router_by_uuid**](CloudRoutersApi.md#update_cloud_router_by_uuid) | **PATCH** /fabric/v4/routers/{routerId} | Update Routers


# **create_cloud_router**
> CloudRouter create_cloud_router(cloud_router_post_request, dry_run=dry_run)

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
    dry_run = False # bool | option to verify that API calls will succeed (optional) (default to False)

    try:
        # Create Routers
        api_response = api_instance.create_cloud_router(cloud_router_post_request, dry_run=dry_run)
        print("The response of CloudRoutersApi->create_cloud_router:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->create_cloud_router: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_router_post_request** | [**CloudRouterPostRequest**](CloudRouterPostRequest.md)|  | 
 **dry_run** | **bool**| option to verify that API calls will succeed | [optional] [default to False]

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

Create Route Table Action

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
        # Create Route Table Action
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

# **create_cloud_router_command**
> CloudRouterCommand create_cloud_router_command(router_id, cloud_router_command_post_request)

Initiate Command

This API provides capability to initiate Command

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router_command import CloudRouterCommand
from equinix.services.fabricv4.models.cloud_router_command_post_request import CloudRouterCommandPostRequest
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
    cloud_router_command_post_request = equinix.services.fabricv4.CloudRouterCommandPostRequest() # CloudRouterCommandPostRequest | 

    try:
        # Initiate Command
        api_response = api_instance.create_cloud_router_command(router_id, cloud_router_command_post_request)
        print("The response of CloudRoutersApi->create_cloud_router_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->create_cloud_router_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Router UUID | 
 **cloud_router_command_post_request** | [**CloudRouterCommandPostRequest**](CloudRouterCommandPostRequest.md)|  | 

### Return type

[**CloudRouterCommand**](CloudRouterCommand.md)

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

# **delete_cloud_router_command_by_uuid**
> delete_cloud_router_command_by_uuid(router_id, command_id)

Delete Command

This API provides capability to delete command based on command Id

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
    router_id = 'router_id_example' # str | Router UUID
    command_id = 'command_id_example' # str | Command UUID

    try:
        # Delete Command
        api_instance.delete_cloud_router_command_by_uuid(router_id, command_id)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->delete_cloud_router_command_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Router UUID | 
 **command_id** | **str**| Command UUID | 

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
**204** | Deleted command successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cloud_router_commands**
> GetAllCloudRouterCommands get_all_cloud_router_commands(router_id)

Get Commands

This API provides capability to fetch all commands

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_all_cloud_router_commands import GetAllCloudRouterCommands
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

    try:
        # Get Commands
        api_response = api_instance.get_all_cloud_router_commands(router_id)
        print("The response of CloudRoutersApi->get_all_cloud_router_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->get_all_cloud_router_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Router UUID | 

### Return type

[**GetAllCloudRouterCommands**](GetAllCloudRouterCommands.md)

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

# **get_cloud_router_actions**
> CloudRouterActionResponse get_cloud_router_actions(router_id, state=state)

Get Route Table Actions

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
        # Get Route Table Actions
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

# **get_cloud_router_actions_by_uuid**
> CloudRouterActionResponse get_cloud_router_actions_by_uuid(router_id, action_id, state=state)

Get Route Table Action by ID

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
    action_id = 'action_id_example' # str | Action UUID
    state = equinix.services.fabricv4.CloudRouterActionState() # CloudRouterActionState | Action state (optional)

    try:
        # Get Route Table Action by ID
        api_response = api_instance.get_cloud_router_actions_by_uuid(router_id, action_id, state=state)
        print("The response of CloudRoutersApi->get_cloud_router_actions_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->get_cloud_router_actions_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Router UUID | 
 **action_id** | **str**| Action UUID | 
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

# **get_cloud_router_command**
> CloudRouterCommand get_cloud_router_command(router_id, command_id)

Get Command

This API provides capability to fetch command using command Id

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router_command import CloudRouterCommand
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
    command_id = 'command_id_example' # str | Command UUID

    try:
        # Get Command
        api_response = api_instance.get_cloud_router_command(router_id, command_id)
        print("The response of CloudRoutersApi->get_cloud_router_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->get_cloud_router_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Router UUID | 
 **command_id** | **str**| Command UUID | 

### Return type

[**CloudRouterCommand**](CloudRouterCommand.md)

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

# **get_gateway_attachment_to_cloud_router_by_uuid**
> CloudRouterForGatewayAttachmentResponse get_gateway_attachment_to_cloud_router_by_uuid(gateway_id, router_id)

Get Gateway Attachment details to a Cloud Router

Get details of a Specific Gateway Attachment to a Cloud Router.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router_for_gateway_attachment_response import CloudRouterForGatewayAttachmentResponse
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
    gateway_id = 'gateway_id_example' # str | Gateway UUID
    router_id = 'router_id_example' # str | Cloud Router UUID

    try:
        # Get Gateway Attachment details to a Cloud Router
        api_response = api_instance.get_gateway_attachment_to_cloud_router_by_uuid(gateway_id, router_id)
        print("The response of CloudRoutersApi->get_gateway_attachment_to_cloud_router_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->get_gateway_attachment_to_cloud_router_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| Gateway UUID | 
 **router_id** | **str**| Cloud Router UUID | 

### Return type

[**CloudRouterForGatewayAttachmentResponse**](CloudRouterForGatewayAttachmentResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Router associated to a Gateway Attachment. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_gateway_attachments_to_cloud_router**
> CloudRouterListForGatewayAttachment list_gateway_attachments_to_cloud_router(gateway_id, offset=offset, limit=limit)

List Cloud Routers of a Gateway Attachment.

Get all Cloud Routers attached on a Gateway.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router_list_for_gateway_attachment import CloudRouterListForGatewayAttachment
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
    gateway_id = 'gateway_id_example' # str | Gateway UUID
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # List Cloud Routers of a Gateway Attachment.
        api_response = api_instance.list_gateway_attachments_to_cloud_router(gateway_id, offset=offset, limit=limit)
        print("The response of CloudRoutersApi->list_gateway_attachments_to_cloud_router:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->list_gateway_attachments_to_cloud_router: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| Gateway UUID | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**CloudRouterListForGatewayAttachment**](CloudRouterListForGatewayAttachment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Cloud Routers on a Gateway Attachment. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_cloud_router_commands**
> CloudRouterCommandSearchResponse search_cloud_router_commands(router_id, cloud_router_command_search_request)

Search Commands

This API provides capability to search commands

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router_command_search_request import CloudRouterCommandSearchRequest
from equinix.services.fabricv4.models.cloud_router_command_search_response import CloudRouterCommandSearchResponse
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
    cloud_router_command_search_request = equinix.services.fabricv4.CloudRouterCommandSearchRequest() # CloudRouterCommandSearchRequest | 

    try:
        # Search Commands
        api_response = api_instance.search_cloud_router_commands(router_id, cloud_router_command_search_request)
        print("The response of CloudRoutersApi->search_cloud_router_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->search_cloud_router_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Router UUID | 
 **cloud_router_command_search_request** | [**CloudRouterCommandSearchRequest**](CloudRouterCommandSearchRequest.md)|  | 

### Return type

[**CloudRouterCommandSearchResponse**](CloudRouterCommandSearchResponse.md)

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

# **search_connection_advertised_routes**
> ConnectionRouteTableEntrySearchResponse search_connection_advertised_routes(connection_id, connection_route_search_request)

Search Advertised Routes

The API provides capability to get list of user's advertised routes using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_route_search_request import ConnectionRouteSearchRequest
from equinix.services.fabricv4.models.connection_route_table_entry_search_response import ConnectionRouteTableEntrySearchResponse
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
    connection_id = 'connection_id_example' # str | Connection Id
    connection_route_search_request = equinix.services.fabricv4.ConnectionRouteSearchRequest() # ConnectionRouteSearchRequest | 

    try:
        # Search Advertised Routes
        api_response = api_instance.search_connection_advertised_routes(connection_id, connection_route_search_request)
        print("The response of CloudRoutersApi->search_connection_advertised_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->search_connection_advertised_routes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 
 **connection_route_search_request** | [**ConnectionRouteSearchRequest**](ConnectionRouteSearchRequest.md)|  | 

### Return type

[**ConnectionRouteTableEntrySearchResponse**](ConnectionRouteTableEntrySearchResponse.md)

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

# **search_connection_received_routes**
> ConnectionRouteTableEntrySearchResponse search_connection_received_routes(connection_id, connection_route_search_request)

Search Received Routes

The API provides capability to get list of received routes using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_route_search_request import ConnectionRouteSearchRequest
from equinix.services.fabricv4.models.connection_route_table_entry_search_response import ConnectionRouteTableEntrySearchResponse
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
    connection_id = 'connection_id_example' # str | Connection Id
    connection_route_search_request = equinix.services.fabricv4.ConnectionRouteSearchRequest() # ConnectionRouteSearchRequest | 

    try:
        # Search Received Routes
        api_response = api_instance.search_connection_received_routes(connection_id, connection_route_search_request)
        print("The response of CloudRoutersApi->search_connection_received_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->search_connection_received_routes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection Id | 
 **connection_route_search_request** | [**ConnectionRouteSearchRequest**](ConnectionRouteSearchRequest.md)|  | 

### Return type

[**ConnectionRouteTableEntrySearchResponse**](ConnectionRouteTableEntrySearchResponse.md)

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

# **search_router_actions**
> CloudRouterActionsSearchResponse search_router_actions(router_id, cloud_router_actions_search_request)

Search Route Table Actions

This API provides capability to refresh route table and bgp session summary information

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router_actions_search_request import CloudRouterActionsSearchRequest
from equinix.services.fabricv4.models.cloud_router_actions_search_response import CloudRouterActionsSearchResponse
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
    cloud_router_actions_search_request = equinix.services.fabricv4.CloudRouterActionsSearchRequest() # CloudRouterActionsSearchRequest | 

    try:
        # Search Route Table Actions
        api_response = api_instance.search_router_actions(router_id, cloud_router_actions_search_request)
        print("The response of CloudRoutersApi->search_router_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRoutersApi->search_router_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | **str**| Router UUID | 
 **cloud_router_actions_search_request** | [**CloudRouterActionsSearchRequest**](CloudRouterActionsSearchRequest.md)|  | 

### Return type

[**CloudRouterActionsSearchResponse**](CloudRouterActionsSearchResponse.md)

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

