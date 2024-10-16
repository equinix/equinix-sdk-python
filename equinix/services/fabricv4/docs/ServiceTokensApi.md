# equinix.services.fabricv4.ServiceTokensApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_token**](ServiceTokensApi.md#create_service_token) | **POST** /fabric/v4/serviceTokens | Create Service Token
[**create_service_token_action**](ServiceTokensApi.md#create_service_token_action) | **POST** /fabric/v4/serviceTokens/{serviceTokenId}/actions | ServiceToken Actions
[**delete_service_token_by_uuid**](ServiceTokensApi.md#delete_service_token_by_uuid) | **DELETE** /fabric/v4/serviceTokens/{serviceTokenId} | Delete Token by uuid
[**get_service_token_by_uuid**](ServiceTokensApi.md#get_service_token_by_uuid) | **GET** /fabric/v4/serviceTokens/{serviceTokenId} | Get Token by uuid
[**get_service_tokens**](ServiceTokensApi.md#get_service_tokens) | **GET** /fabric/v4/serviceTokens | Get All Tokens
[**search_service_tokens**](ServiceTokensApi.md#search_service_tokens) | **POST** /fabric/v4/serviceTokens/search | Search servicetokens
[**update_service_token_by_uuid**](ServiceTokensApi.md#update_service_token_by_uuid) | **PATCH** /fabric/v4/serviceTokens/{serviceTokenId} | Update Token By ID


# **create_service_token**
> ServiceToken create_service_token(service_token)

Create Service Token

Create Service Tokens generates Equinix Fabric? service tokens. These tokens authorize users to access protected resources and services.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.service_token import ServiceToken
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
    api_instance = equinix.services.fabricv4.ServiceTokensApi(api_client)
    service_token = equinix.services.fabricv4.ServiceToken() # ServiceToken | 

    try:
        # Create Service Token
        api_response = api_instance.create_service_token(service_token)
        print("The response of ServiceTokensApi->create_service_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTokensApi->create_service_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_token** | [**ServiceToken**](ServiceToken.md)|  | 

### Return type

[**ServiceToken**](ServiceToken.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_token_action**
> ServiceToken create_service_token_action(service_token_id, service_token_action_request)

ServiceToken Actions

This API provides capability to accept/reject user's servicetokens

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.service_token import ServiceToken
from equinix.services.fabricv4.models.service_token_action_request import ServiceTokenActionRequest
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
    api_instance = equinix.services.fabricv4.ServiceTokensApi(api_client)
    service_token_id = 'service_token_id_example' # str | Service Token UUID
    service_token_action_request = equinix.services.fabricv4.ServiceTokenActionRequest() # ServiceTokenActionRequest | 

    try:
        # ServiceToken Actions
        api_response = api_instance.create_service_token_action(service_token_id, service_token_action_request)
        print("The response of ServiceTokensApi->create_service_token_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTokensApi->create_service_token_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_token_id** | **str**| Service Token UUID | 
 **service_token_action_request** | [**ServiceTokenActionRequest**](ServiceTokenActionRequest.md)|  | 

### Return type

[**ServiceToken**](ServiceToken.md)

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

# **delete_service_token_by_uuid**
> ServiceToken delete_service_token_by_uuid(service_token_id)

Delete Token by uuid

Delete Service Tokens removes an Equinix Fabric service token corresponding to the specified uuid which are in INACTIVE state.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.service_token import ServiceToken
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
    api_instance = equinix.services.fabricv4.ServiceTokensApi(api_client)
    service_token_id = 'service_token_id_example' # str | Service Token UUID

    try:
        # Delete Token by uuid
        api_response = api_instance.delete_service_token_by_uuid(service_token_id)
        print("The response of ServiceTokensApi->delete_service_token_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTokensApi->delete_service_token_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_token_id** | **str**| Service Token UUID | 

### Return type

[**ServiceToken**](ServiceToken.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_token_by_uuid**
> ServiceToken get_service_token_by_uuid(service_token_id)

Get Token by uuid

Get Specified Service Tokens uses the uuid of an Equinix Fabric service token to return details about the token's type, state, location, bandwidth, and other key properties.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.service_token import ServiceToken
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
    api_instance = equinix.services.fabricv4.ServiceTokensApi(api_client)
    service_token_id = 'service_token_id_example' # str | Service Token UUID

    try:
        # Get Token by uuid
        api_response = api_instance.get_service_token_by_uuid(service_token_id)
        print("The response of ServiceTokensApi->get_service_token_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTokensApi->get_service_token_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_token_id** | **str**| Service Token UUID | 

### Return type

[**ServiceToken**](ServiceToken.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_tokens**
> ServiceTokens get_service_tokens(offset=offset, limit=limit)

Get All Tokens

Get All ServiceTokens creates a list of all Equinix Fabric service tokens associated with the subscriber's account.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.service_tokens import ServiceTokens
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
    api_instance = equinix.services.fabricv4.ServiceTokensApi(api_client)
    offset = 3.4 # float | offset (optional)
    limit = 3.4 # float | number of records to fetch (optional)

    try:
        # Get All Tokens
        api_response = api_instance.get_service_tokens(offset=offset, limit=limit)
        print("The response of ServiceTokensApi->get_service_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTokensApi->get_service_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**| offset | [optional] 
 **limit** | **float**| number of records to fetch | [optional] 

### Return type

[**ServiceTokens**](ServiceTokens.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_service_tokens**
> ServiceTokens search_service_tokens(service_token_search_request, offset=offset, limit=limit)

Search servicetokens

The API provides capability to get list of user's servicetokens using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.service_token_search_request import ServiceTokenSearchRequest
from equinix.services.fabricv4.models.service_tokens import ServiceTokens
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
    api_instance = equinix.services.fabricv4.ServiceTokensApi(api_client)
    service_token_search_request = equinix.services.fabricv4.ServiceTokenSearchRequest() # ServiceTokenSearchRequest | 
    offset = 3.4 # float | offset (optional)
    limit = 3.4 # float | number of records to fetch (optional)

    try:
        # Search servicetokens
        api_response = api_instance.search_service_tokens(service_token_search_request, offset=offset, limit=limit)
        print("The response of ServiceTokensApi->search_service_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTokensApi->search_service_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_token_search_request** | [**ServiceTokenSearchRequest**](ServiceTokenSearchRequest.md)|  | 
 **offset** | **float**| offset | [optional] 
 **limit** | **float**| number of records to fetch | [optional] 

### Return type

[**ServiceTokens**](ServiceTokens.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_token_by_uuid**
> ServiceToken update_service_token_by_uuid(service_token_id, service_token_change_operation)

Update Token By ID

This API provides capability to update user's Service Token

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.service_token import ServiceToken
from equinix.services.fabricv4.models.service_token_change_operation import ServiceTokenChangeOperation
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
    api_instance = equinix.services.fabricv4.ServiceTokensApi(api_client)
    service_token_id = 'service_token_id_example' # str | Service Token UUID
    service_token_change_operation = [equinix.services.fabricv4.ServiceTokenChangeOperation()] # List[ServiceTokenChangeOperation] | 

    try:
        # Update Token By ID
        api_response = api_instance.update_service_token_by_uuid(service_token_id, service_token_change_operation)
        print("The response of ServiceTokensApi->update_service_token_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTokensApi->update_service_token_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_token_id** | **str**| Service Token UUID | 
 **service_token_change_operation** | [**List[ServiceTokenChangeOperation]**](ServiceTokenChangeOperation.md)|  | 

### Return type

[**ServiceToken**](ServiceToken.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

