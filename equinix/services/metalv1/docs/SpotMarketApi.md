# equinix_metal.SpotMarketApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_spot_market_request**](SpotMarketApi.md#create_spot_market_request) | **POST** /projects/{id}/spot-market-requests | Create a spot market request
[**delete_spot_market_request**](SpotMarketApi.md#delete_spot_market_request) | **DELETE** /spot-market-requests/{id} | Delete the spot market request
[**find_metro_spot_market_prices**](SpotMarketApi.md#find_metro_spot_market_prices) | **GET** /market/spot/prices/metros | Get current spot market prices for metros
[**find_spot_market_prices**](SpotMarketApi.md#find_spot_market_prices) | **GET** /market/spot/prices | Get current spot market prices
[**find_spot_market_prices_history**](SpotMarketApi.md#find_spot_market_prices_history) | **GET** /market/spot/prices/history | Get spot market prices for a given period of time
[**find_spot_market_request_by_id**](SpotMarketApi.md#find_spot_market_request_by_id) | **GET** /spot-market-requests/{id} | Retrieve a spot market request
[**list_spot_market_requests**](SpotMarketApi.md#list_spot_market_requests) | **GET** /projects/{id}/spot-market-requests | List spot market requests


# **create_spot_market_request**
> SpotMarketRequest create_spot_market_request(id, spot_market_request_create_input)

Create a spot market request

Creates a new spot market request.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have. For example, if you require a server with a TPM chip, you may specify `{ \"features\": { \"tpm\": \"required\" } }` (or `{ \"features\": [\"tpm\"] }` in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.spot_market_request import SpotMarketRequest
from equinix_metal.models.spot_market_request_create_input import SpotMarketRequestCreateInput
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.SpotMarketApi(api_client)
    id = 'id_example' # str | Project UUID
    spot_market_request_create_input = equinix_metal.SpotMarketRequestCreateInput() # SpotMarketRequestCreateInput | Spot Market Request to create

    try:
        # Create a spot market request
        api_response = api_instance.create_spot_market_request(id, spot_market_request_create_input)
        print("The response of SpotMarketApi->create_spot_market_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotMarketApi->create_spot_market_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **spot_market_request_create_input** | [**SpotMarketRequestCreateInput**](SpotMarketRequestCreateInput.md)| Spot Market Request to create | 

### Return type

[**SpotMarketRequest**](SpotMarketRequest.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **delete_spot_market_request**
> delete_spot_market_request(id, force_termination=force_termination)

Delete the spot market request

Deletes the spot market request.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.SpotMarketApi(api_client)
    id = 'id_example' # str | SpotMarketRequest UUID
    force_termination = True # bool | Terminate associated spot instances (optional)

    try:
        # Delete the spot market request
        api_instance.delete_spot_market_request(id, force_termination=force_termination)
    except Exception as e:
        print("Exception when calling SpotMarketApi->delete_spot_market_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SpotMarketRequest UUID | 
 **force_termination** | **bool**| Terminate associated spot instances | [optional] 

### Return type

void (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | no content |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_metro_spot_market_prices**
> SpotMarketPricesPerMetroList find_metro_spot_market_prices(metro=metro, plan=plan)

Get current spot market prices for metros

Get Equinix Metal current spot market prices for all metros.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.spot_market_prices_per_metro_list import SpotMarketPricesPerMetroList
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.SpotMarketApi(api_client)
    metro = 'metro_example' # str | Metro to filter spot market prices (optional)
    plan = 'plan_example' # str | Plan to filter spot market prices (optional)

    try:
        # Get current spot market prices for metros
        api_response = api_instance.find_metro_spot_market_prices(metro=metro, plan=plan)
        print("The response of SpotMarketApi->find_metro_spot_market_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotMarketApi->find_metro_spot_market_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metro** | **str**| Metro to filter spot market prices | [optional] 
 **plan** | **str**| Plan to filter spot market prices | [optional] 

### Return type

[**SpotMarketPricesPerMetroList**](SpotMarketPricesPerMetroList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_spot_market_prices**
> SpotMarketPricesList find_spot_market_prices(facility=facility, plan=plan)

Get current spot market prices

Get Equinix Metal current spot market prices.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.spot_market_prices_list import SpotMarketPricesList
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.SpotMarketApi(api_client)
    facility = 'facility_example' # str | Facility to check spot market prices (optional)
    plan = 'plan_example' # str | Plan to check spot market prices (optional)

    try:
        # Get current spot market prices
        api_response = api_instance.find_spot_market_prices(facility=facility, plan=plan)
        print("The response of SpotMarketApi->find_spot_market_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotMarketApi->find_spot_market_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility** | **str**| Facility to check spot market prices | [optional] 
 **plan** | **str**| Plan to check spot market prices | [optional] 

### Return type

[**SpotMarketPricesList**](SpotMarketPricesList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_spot_market_prices_history**
> SpotPricesHistoryReport find_spot_market_prices_history(facility, plan, var_from, until, metro=metro)

Get spot market prices for a given period of time

Get spot market prices for a given plan and facility in a fixed period of time  *Note: In the `200` response, the property `datapoints` contains arrays of `[float, integer]`.*

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.spot_prices_history_report import SpotPricesHistoryReport
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.SpotMarketApi(api_client)
    facility = 'facility_example' # str | Facility to check spot market prices
    plan = 'plan_example' # str | Plan to check spot market prices
    var_from = 'var_from_example' # str | Timestamp from range
    until = 'until_example' # str | Timestamp to range
    metro = 'metro_example' # str | Metro to check spot market price history (optional)

    try:
        # Get spot market prices for a given period of time
        api_response = api_instance.find_spot_market_prices_history(facility, plan, var_from, until, metro=metro)
        print("The response of SpotMarketApi->find_spot_market_prices_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotMarketApi->find_spot_market_prices_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility** | **str**| Facility to check spot market prices | 
 **plan** | **str**| Plan to check spot market prices | 
 **var_from** | **str**| Timestamp from range | 
 **until** | **str**| Timestamp to range | 
 **metro** | **str**| Metro to check spot market price history | [optional] 

### Return type

[**SpotPricesHistoryReport**](SpotPricesHistoryReport.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_spot_market_request_by_id**
> SpotMarketRequest find_spot_market_request_by_id(id, include=include)

Retrieve a spot market request

Returns a single spot market request

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.spot_market_request import SpotMarketRequest
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.SpotMarketApi(api_client)
    id = 'id_example' # str | SpotMarketRequest UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Retrieve a spot market request
        api_response = api_instance.find_spot_market_request_by_id(id, include=include)
        print("The response of SpotMarketApi->find_spot_market_request_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotMarketApi->find_spot_market_request_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SpotMarketRequest UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**SpotMarketRequest**](SpotMarketRequest.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **list_spot_market_requests**
> SpotMarketRequestList list_spot_market_requests(id)

List spot market requests

View all spot market requests for a given project.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.spot_market_request_list import SpotMarketRequestList
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.SpotMarketApi(api_client)
    id = 'id_example' # str | Project UUID

    try:
        # List spot market requests
        api_response = api_instance.list_spot_market_requests(id)
        print("The response of SpotMarketApi->list_spot_market_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotMarketApi->list_spot_market_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 

### Return type

[**SpotMarketRequestList**](SpotMarketRequestList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
