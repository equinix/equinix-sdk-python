# equinix.services.fabricv4.GatewaysApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gateway**](GatewaysApi.md#create_gateway) | **POST** /fabric/v4/gateways | Create Gateway
[**delete_gateway_by_uuid**](GatewaysApi.md#delete_gateway_by_uuid) | **DELETE** /fabric/v4/gateways/{gatewayId} | Delete Gateway
[**get_gateway_by_uuid**](GatewaysApi.md#get_gateway_by_uuid) | **GET** /fabric/v4/gateways/{gatewayId} | Get Gateway
[**update_gateway_by_uuid**](GatewaysApi.md#update_gateway_by_uuid) | **PATCH** /fabric/v4/gateways/{gatewayId} | Update Gateway by ID


# **create_gateway**
> Gateway create_gateway(gateway_post_request)

Create Gateway

This API provides capability to create user's Gateways

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.gateway import Gateway
from equinix.services.fabricv4.models.gateway_post_request import GatewayPostRequest
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
    api_instance = equinix.services.fabricv4.GatewaysApi(api_client)
    gateway_post_request = equinix.services.fabricv4.GatewayPostRequest() # GatewayPostRequest | 

    try:
        # Create Gateway
        api_response = api_instance.create_gateway(gateway_post_request)
        print("The response of GatewaysApi->create_gateway:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GatewaysApi->create_gateway: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_post_request** | [**GatewayPostRequest**](GatewayPostRequest.md)|  | 

### Return type

[**Gateway**](Gateway.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Gateway object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gateway_by_uuid**
> Gateway delete_gateway_by_uuid(gateway_id)

Delete Gateway

This API provides capability to delete user's Gateways

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.gateway import Gateway
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
    api_instance = equinix.services.fabricv4.GatewaysApi(api_client)
    gateway_id = 'gateway_id_example' # str | Gateway UUID

    try:
        # Delete Gateway
        api_response = api_instance.delete_gateway_by_uuid(gateway_id)
        print("The response of GatewaysApi->delete_gateway_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GatewaysApi->delete_gateway_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| Gateway UUID | 

### Return type

[**Gateway**](Gateway.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Gateway object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gateway_by_uuid**
> Gateway get_gateway_by_uuid(gateway_id)

Get Gateway

This API provides capability to retrieve user's Gateways

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.gateway import Gateway
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
    api_instance = equinix.services.fabricv4.GatewaysApi(api_client)
    gateway_id = 'gateway_id_example' # str | Gateway UUID

    try:
        # Get Gateway
        api_response = api_instance.get_gateway_by_uuid(gateway_id)
        print("The response of GatewaysApi->get_gateway_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GatewaysApi->get_gateway_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| Gateway UUID | 

### Return type

[**Gateway**](Gateway.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gateway object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gateway_by_uuid**
> Gateway update_gateway_by_uuid(gateway_id, gateway_change_operation)

Update Gateway by ID

Update Gateway by Uuid

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.gateway import Gateway
from equinix.services.fabricv4.models.gateway_change_operation import GatewayChangeOperation
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
    api_instance = equinix.services.fabricv4.GatewaysApi(api_client)
    gateway_id = 'gateway_id_example' # str | Gateway UUID
    gateway_change_operation = [equinix.services.fabricv4.GatewayChangeOperation()] # List[GatewayChangeOperation] | 

    try:
        # Update Gateway by ID
        api_response = api_instance.update_gateway_by_uuid(gateway_id, gateway_change_operation)
        print("The response of GatewaysApi->update_gateway_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GatewaysApi->update_gateway_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| Gateway UUID | 
 **gateway_change_operation** | [**List[GatewayChangeOperation]**](GatewayChangeOperation.md)|  | 

### Return type

[**Gateway**](Gateway.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Gateway object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

