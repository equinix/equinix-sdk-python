# equinix.services.fabricv4.FabricOneApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_interconnect**](FabricOneApi.md#create_interconnect) | **POST** /fabric/v4/interconnects | Create Interconnect
[**delete_interconnect_by_uuid**](FabricOneApi.md#delete_interconnect_by_uuid) | **DELETE** /fabric/v4/interconnects/{interconnectId} | Delete Interconnect By ID
[**get_interconnect_by_uuid**](FabricOneApi.md#get_interconnect_by_uuid) | **GET** /fabric/v4/interconnects/{interconnectId} | Get Interconnect By ID
[**get_interconnect_packages**](FabricOneApi.md#get_interconnect_packages) | **GET** /fabric/v4/interconnectPackages | Get All Interconnect Packages
[**search_interconnects**](FabricOneApi.md#search_interconnects) | **POST** /fabric/v4/interconnects/search | Search Interconnects


# **create_interconnect**
> Interconnect create_interconnect(interconnect_post_request)

Create Interconnect

This API provides capability to create user's Interconnect <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.interconnect import Interconnect
from equinix.services.fabricv4.models.interconnect_post_request import InterconnectPostRequest
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
    api_instance = equinix.services.fabricv4.FabricOneApi(api_client)
    interconnect_post_request = equinix.services.fabricv4.InterconnectPostRequest() # InterconnectPostRequest | 

    try:
        # Create Interconnect
        api_response = api_instance.create_interconnect(interconnect_post_request)
        print("The response of FabricOneApi->create_interconnect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FabricOneApi->create_interconnect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interconnect_post_request** | [**InterconnectPostRequest**](InterconnectPostRequest.md)|  | 

### Return type

[**Interconnect**](Interconnect.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Interconnect created successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_interconnect_by_uuid**
> Interconnect delete_interconnect_by_uuid(interconnect_id)

Delete Interconnect By ID

This API provides capability to delete user's Interconnect <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.interconnect import Interconnect
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
    api_instance = equinix.services.fabricv4.FabricOneApi(api_client)
    interconnect_id = 'interconnect_id_example' # str | Interconnect UUID

    try:
        # Delete Interconnect By ID
        api_response = api_instance.delete_interconnect_by_uuid(interconnect_id)
        print("The response of FabricOneApi->delete_interconnect_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FabricOneApi->delete_interconnect_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interconnect_id** | **str**| Interconnect UUID | 

### Return type

[**Interconnect**](Interconnect.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Fabric Interconnect object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interconnect_by_uuid**
> Interconnect get_interconnect_by_uuid(interconnect_id)

Get Interconnect By ID

This API provides capability to retrieve user's Interconnect <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.interconnect import Interconnect
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
    api_instance = equinix.services.fabricv4.FabricOneApi(api_client)
    interconnect_id = 'interconnect_id_example' # str | Interconnect UUID

    try:
        # Get Interconnect By ID
        api_response = api_instance.get_interconnect_by_uuid(interconnect_id)
        print("The response of FabricOneApi->get_interconnect_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FabricOneApi->get_interconnect_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interconnect_id** | **str**| Interconnect UUID | 

### Return type

[**Interconnect**](Interconnect.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Interconnect object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interconnect_packages**
> AllInterconnectPackagesResponse get_interconnect_packages(offset=offset, limit=limit)

Get All Interconnect Packages

Get All Interconnect Packages returns details of all available interconnect packages for the specified user credentials. <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.all_interconnect_packages_response import AllInterconnectPackagesResponse
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
    api_instance = equinix.services.fabricv4.FabricOneApi(api_client)
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get All Interconnect Packages
        api_response = api_instance.get_interconnect_packages(offset=offset, limit=limit)
        print("The response of FabricOneApi->get_interconnect_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FabricOneApi->get_interconnect_packages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**AllInterconnectPackagesResponse**](AllInterconnectPackagesResponse.md)

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
**415** | Unsupported Media Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_interconnects**
> InterconnectSearchResponse search_interconnects(interconnect_search_request)

Search Interconnects

The API provides capability to get list of user's Interconnects using search criteria, including optional filtering, pagination and sorting <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.interconnect_search_request import InterconnectSearchRequest
from equinix.services.fabricv4.models.interconnect_search_response import InterconnectSearchResponse
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
    api_instance = equinix.services.fabricv4.FabricOneApi(api_client)
    interconnect_search_request = equinix.services.fabricv4.InterconnectSearchRequest() # InterconnectSearchRequest | 

    try:
        # Search Interconnects
        api_response = api_instance.search_interconnects(interconnect_search_request)
        print("The response of FabricOneApi->search_interconnects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FabricOneApi->search_interconnects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interconnect_search_request** | [**InterconnectSearchRequest**](InterconnectSearchRequest.md)|  | 

### Return type

[**InterconnectSearchResponse**](InterconnectSearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Interconnect Search Response |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

