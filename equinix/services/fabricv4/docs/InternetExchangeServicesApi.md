# equinix.services.fabricv4.InternetExchangeServicesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exchange_service_by_id**](InternetExchangeServicesApi.md#get_exchange_service_by_id) | **GET** /fabric/v4/exchangeServices/{exchangeServiceId} | Get Internet Exchange Service
[**search_exchange_service**](InternetExchangeServicesApi.md#search_exchange_service) | **POST** /fabric/v4/exchangeServices/search | Search Internet Exchange Service


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

Search Internet Exchange Service

The API provides capability to get list of user's Internet Exchange Service using search criteria, including optional filtering, pagination and sorting.

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
        # Search Internet Exchange Service
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

