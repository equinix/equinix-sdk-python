# equinix.services.fabricv4.OpticalMetroConnectsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_optical_connect**](OpticalMetroConnectsApi.md#create_bulk_optical_connect) | **POST** /fabric/v4/opticalConnects/bulk | Create Dual Diverse Optical Metro Connect Service
[**create_optical_connect**](OpticalMetroConnectsApi.md#create_optical_connect) | **POST** /fabric/v4/opticalConnects | Create Optical Metro Connect Service
[**get_optical_connect_by_uuid**](OpticalMetroConnectsApi.md#get_optical_connect_by_uuid) | **GET** /fabric/v4/opticalConnects/{opticalConnectId} | Get Optical Metro Connect Service
[**search_optical_connect**](OpticalMetroConnectsApi.md#search_optical_connect) | **POST** /fabric/v4/opticalConnects/search | Search Optical Metro Connect Services


# **create_bulk_optical_connect**
> OpticalConnectBulk create_bulk_optical_connect(bulk_optical_connect_request)

Create Dual Diverse Optical Metro Connect Service

Create a dual diverse pair of circuits on separate optical paths.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.bulk_optical_connect_request import BulkOpticalConnectRequest
from equinix.services.fabricv4.models.optical_connect_bulk import OpticalConnectBulk
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
    api_instance = equinix.services.fabricv4.OpticalMetroConnectsApi(api_client)
    bulk_optical_connect_request = equinix.services.fabricv4.BulkOpticalConnectRequest() # BulkOpticalConnectRequest | 

    try:
        # Create Dual Diverse Optical Metro Connect Service
        api_response = api_instance.create_bulk_optical_connect(bulk_optical_connect_request)
        print("The response of OpticalMetroConnectsApi->create_bulk_optical_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpticalMetroConnectsApi->create_bulk_optical_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_optical_connect_request** | [**BulkOpticalConnectRequest**](BulkOpticalConnectRequest.md)|  | 

### Return type

[**OpticalConnectBulk**](OpticalConnectBulk.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted Operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_optical_connect**
> OpticalConnectResponse create_optical_connect(optical_connect_post_request)

Create Optical Metro Connect Service

Create a single Optical Metro Connect circuit.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.optical_connect_post_request import OpticalConnectPostRequest
from equinix.services.fabricv4.models.optical_connect_response import OpticalConnectResponse
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
    api_instance = equinix.services.fabricv4.OpticalMetroConnectsApi(api_client)
    optical_connect_post_request = equinix.services.fabricv4.OpticalConnectPostRequest() # OpticalConnectPostRequest | 

    try:
        # Create Optical Metro Connect Service
        api_response = api_instance.create_optical_connect(optical_connect_post_request)
        print("The response of OpticalMetroConnectsApi->create_optical_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpticalMetroConnectsApi->create_optical_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optical_connect_post_request** | [**OpticalConnectPostRequest**](OpticalConnectPostRequest.md)|  | 

### Return type

[**OpticalConnectResponse**](OpticalConnectResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted Operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_optical_connect_by_uuid**
> OpticalConnectResponse get_optical_connect_by_uuid(optical_connect_id)

Get Optical Metro Connect Service

Get a single Optical Metro Connect by UUID.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.optical_connect_response import OpticalConnectResponse
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
    api_instance = equinix.services.fabricv4.OpticalMetroConnectsApi(api_client)
    optical_connect_id = 'optical_connect_id_example' # str | Unique identifier of an Optical Connect.

    try:
        # Get Optical Metro Connect Service
        api_response = api_instance.get_optical_connect_by_uuid(optical_connect_id)
        print("The response of OpticalMetroConnectsApi->get_optical_connect_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpticalMetroConnectsApi->get_optical_connect_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optical_connect_id** | **str**| Unique identifier of an Optical Connect. | 

### Return type

[**OpticalConnectResponse**](OpticalConnectResponse.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_optical_connect**
> OpticalConnectServiceSearchResponse search_optical_connect(optical_connect_search_request)

Search Optical Metro Connect Services

Get Optical Metro Connects matching the supplied criteria, with optional filtering, pagination and sorting.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.optical_connect_search_request import OpticalConnectSearchRequest
from equinix.services.fabricv4.models.optical_connect_service_search_response import OpticalConnectServiceSearchResponse
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
    api_instance = equinix.services.fabricv4.OpticalMetroConnectsApi(api_client)
    optical_connect_search_request = equinix.services.fabricv4.OpticalConnectSearchRequest() # OpticalConnectSearchRequest | 

    try:
        # Search Optical Metro Connect Services
        api_response = api_instance.search_optical_connect(optical_connect_search_request)
        print("The response of OpticalMetroConnectsApi->search_optical_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpticalMetroConnectsApi->search_optical_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optical_connect_search_request** | [**OpticalConnectSearchRequest**](OpticalConnectSearchRequest.md)|  | 

### Return type

[**OpticalConnectServiceSearchResponse**](OpticalConnectServiceSearchResponse.md)

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
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

