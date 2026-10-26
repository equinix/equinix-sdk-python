# equinix.services.fabricv4.InternetExchangeServicesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_exchange_service**](InternetExchangeServicesApi.md#create_exchange_service) | **POST** /fabric/v4/exchangeServices | Create Internet Exchange Service
[**create_exchange_service_action**](InternetExchangeServicesApi.md#create_exchange_service_action) | **POST** /fabric/v4/exchangeServices/{exchangeServiceId}/actions | Create Internet Exchange Service Action
[**get_exchange_service_by_id**](InternetExchangeServicesApi.md#get_exchange_service_by_id) | **GET** /fabric/v4/exchangeServices/{exchangeServiceId} | Get Internet Exchange Service
[**search_exchange_service**](InternetExchangeServicesApi.md#search_exchange_service) | **POST** /fabric/v4/exchangeServices/search | Search Internet Exchange Services
[**update_exchange_service_by_id**](InternetExchangeServicesApi.md#update_exchange_service_by_id) | **PATCH** /fabric/v4/exchangeServices/{exchangeServiceId} | Update Internet Exchange Service


# **create_exchange_service**
> ExchangeServiceResponse create_exchange_service(exchange_service_create_request)

Create Internet Exchange Service

This API provides capability to create Internet Exchange Service

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.exchange_service_create_request import ExchangeServiceCreateRequest
from equinix.services.fabricv4.models.exchange_service_response import ExchangeServiceResponse
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
    api_instance = equinix.services.fabricv4.InternetExchangeServicesApi(api_client)
    exchange_service_create_request = equinix.services.fabricv4.ExchangeServiceCreateRequest() # ExchangeServiceCreateRequest | 

    try:
        # Create Internet Exchange Service
        api_response = api_instance.create_exchange_service(exchange_service_create_request)
        print("The response of InternetExchangeServicesApi->create_exchange_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetExchangeServicesApi->create_exchange_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_service_create_request** | [**ExchangeServiceCreateRequest**](ExchangeServiceCreateRequest.md)|  | 

### Return type

[**ExchangeServiceResponse**](ExchangeServiceResponse.md)

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
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_exchange_service_action**
> ExchangeServiceActionResponse create_exchange_service_action(exchange_service_id, exchange_service_action_request)

Create Internet Exchange Service Action

This API provides capability to perform actions on Internet Exchange Service

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.exchange_service_action_request import ExchangeServiceActionRequest
from equinix.services.fabricv4.models.exchange_service_action_response import ExchangeServiceActionResponse
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
    api_instance = equinix.services.fabricv4.InternetExchangeServicesApi(api_client)
    exchange_service_id = 'exchange_service_id_example' # str | Internet Exchange Service Id
    exchange_service_action_request = equinix.services.fabricv4.ExchangeServiceActionRequest() # ExchangeServiceActionRequest | 

    try:
        # Create Internet Exchange Service Action
        api_response = api_instance.create_exchange_service_action(exchange_service_id, exchange_service_action_request)
        print("The response of InternetExchangeServicesApi->create_exchange_service_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetExchangeServicesApi->create_exchange_service_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_service_id** | **str**| Internet Exchange Service Id | 
 **exchange_service_action_request** | [**ExchangeServiceActionRequest**](ExchangeServiceActionRequest.md)|  | 

### Return type

[**ExchangeServiceActionResponse**](ExchangeServiceActionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_service_by_id**
> ExchangeServiceResponse get_exchange_service_by_id(exchange_service_id)

Get Internet Exchange Service

The API provides capability to get Internet Exchange Service

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.exchange_service_response import ExchangeServiceResponse
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
    api_instance = equinix.services.fabricv4.InternetExchangeServicesApi(api_client)
    exchange_service_id = 'exchange_service_id_example' # str | Internet Exchange Service Id

    try:
        # Get Internet Exchange Service
        api_response = api_instance.get_exchange_service_by_id(exchange_service_id)
        print("The response of InternetExchangeServicesApi->get_exchange_service_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetExchangeServicesApi->get_exchange_service_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_service_id** | **str**| Internet Exchange Service Id | 

### Return type

[**ExchangeServiceResponse**](ExchangeServiceResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_exchange_service**
> ExchangeServiceSearchResponse search_exchange_service(exchange_service_search_request)

Search Internet Exchange Services

The API provides capability to get list of user's Internet Exchange Service using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.exchange_service_search_request import ExchangeServiceSearchRequest
from equinix.services.fabricv4.models.exchange_service_search_response import ExchangeServiceSearchResponse
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
    api_instance = equinix.services.fabricv4.InternetExchangeServicesApi(api_client)
    exchange_service_search_request = equinix.services.fabricv4.ExchangeServiceSearchRequest() # ExchangeServiceSearchRequest | 

    try:
        # Search Internet Exchange Services
        api_response = api_instance.search_exchange_service(exchange_service_search_request)
        print("The response of InternetExchangeServicesApi->search_exchange_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetExchangeServicesApi->search_exchange_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_service_search_request** | [**ExchangeServiceSearchRequest**](ExchangeServiceSearchRequest.md)|  | 

### Return type

[**ExchangeServiceSearchResponse**](ExchangeServiceSearchResponse.md)

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
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_exchange_service_by_id**
> ExchangeServiceResponse update_exchange_service_by_id(exchange_service_id, exchange_service_replace_operation)

Update Internet Exchange Service

The API provides capability to update Internet Exchange Service

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.exchange_service_replace_operation import ExchangeServiceReplaceOperation
from equinix.services.fabricv4.models.exchange_service_response import ExchangeServiceResponse
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
    api_instance = equinix.services.fabricv4.InternetExchangeServicesApi(api_client)
    exchange_service_id = 'exchange_service_id_example' # str | Internet Exchange Service Id
    exchange_service_replace_operation = [equinix.services.fabricv4.ExchangeServiceReplaceOperation()] # List[ExchangeServiceReplaceOperation] | 

    try:
        # Update Internet Exchange Service
        api_response = api_instance.update_exchange_service_by_id(exchange_service_id, exchange_service_replace_operation)
        print("The response of InternetExchangeServicesApi->update_exchange_service_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetExchangeServicesApi->update_exchange_service_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_service_id** | **str**| Internet Exchange Service Id | 
 **exchange_service_replace_operation** | [**List[ExchangeServiceReplaceOperation]**](ExchangeServiceReplaceOperation.md)|  | 

### Return type

[**ExchangeServiceResponse**](ExchangeServiceResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

