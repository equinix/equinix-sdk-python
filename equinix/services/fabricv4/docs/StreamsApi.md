# equinix.services.fabricv4.StreamsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_streams**](StreamsApi.md#create_streams) | **POST** /fabric/v4/streams | Create Stream
[**delete_stream_asset_by_uuid**](StreamsApi.md#delete_stream_asset_by_uuid) | **DELETE** /fabric/v4/streams/{streamId}/{asset}/{assetId} | Detach Asset
[**delete_stream_by_uuid**](StreamsApi.md#delete_stream_by_uuid) | **DELETE** /fabric/v4/streams/{streamId} | Delete Stream
[**delete_stream_device**](StreamsApi.md#delete_stream_device) | **DELETE** /fabric/v4/streams/{streamId}/devices/{deviceId} | Detach Network Edge Device
[**get_stream_asset_by_uuid**](StreamsApi.md#get_stream_asset_by_uuid) | **GET** /fabric/v4/streams/{streamId}/{asset}/{assetId} | Get Asset
[**get_stream_by_uuid**](StreamsApi.md#get_stream_by_uuid) | **GET** /fabric/v4/streams/{streamId} | Get Stream
[**get_stream_device**](StreamsApi.md#get_stream_device) | **GET** /fabric/v4/streams/{streamId}/devices/{deviceId} | Get Network Edge Device
[**get_streams**](StreamsApi.md#get_streams) | **GET** /fabric/v4/streams | Get Streams
[**search_stream_assets**](StreamsApi.md#search_stream_assets) | **POST** /fabric/v4/streamAssets/search | Search Stream Assets
[**search_streams**](StreamsApi.md#search_streams) | **POST** /fabric/v4/streams/search | Search Streams
[**update_stream_asset_by_uuid**](StreamsApi.md#update_stream_asset_by_uuid) | **PUT** /fabric/v4/streams/{streamId}/{asset}/{assetId} | Attach Asset
[**update_stream_by_uuid**](StreamsApi.md#update_stream_by_uuid) | **PUT** /fabric/v4/streams/{streamId} | Update Stream
[**update_stream_device**](StreamsApi.md#update_stream_device) | **PUT** /fabric/v4/streams/{streamId}/devices/{deviceId} | Attach Network Edge Device Interfaces


# **create_streams**
> Stream create_streams(stream_post_request)

Create Stream

This API provides capability to create user's stream

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream import Stream
from equinix.services.fabricv4.models.stream_post_request import StreamPostRequest
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    stream_post_request = {"type":"TELEMETRY_STREAM","name":"splunk1","description":"subscription-1","project":{"projectId":"dadd3ab6-c0af-430c-8216-43d44f08c1c5"},"account":{"accountNumber":123456},"notifications":[{"type":"ALL","emails":["johndoe@equinix.com"]}]} # StreamPostRequest | 

    try:
        # Create Stream
        api_response = api_instance.create_streams(stream_post_request)
        print("The response of StreamsApi->create_streams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->create_streams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_post_request** | [**StreamPostRequest**](StreamPostRequest.md)|  | 

### Return type

[**Stream**](Stream.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stream_asset_by_uuid**
> StreamAsset delete_stream_asset_by_uuid(asset_id, asset, stream_id)

Detach Asset

This API provides capability to detach an asset from a stream

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.asset import Asset
from equinix.services.fabricv4.models.stream_asset import StreamAsset
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    asset_id = '757400f8-d360-11e9-bb65-2a2ae2dbcce6' # str | asset UUID
    asset = equinix.services.fabricv4.Asset() # Asset | asset
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID

    try:
        # Detach Asset
        api_response = api_instance.delete_stream_asset_by_uuid(asset_id, asset, stream_id)
        print("The response of StreamsApi->delete_stream_asset_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->delete_stream_asset_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| asset UUID | 
 **asset** | [**Asset**](.md)| asset | 
 **stream_id** | **str**| Stream UUID | 

### Return type

[**StreamAsset**](StreamAsset.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stream_by_uuid**
> Stream delete_stream_by_uuid(stream_id)

Delete Stream

This API provides capability to delete user's stream

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream import Stream
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID

    try:
        # Delete Stream
        api_response = api_instance.delete_stream_by_uuid(stream_id)
        print("The response of StreamsApi->delete_stream_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->delete_stream_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream UUID | 

### Return type

[**Stream**](Stream.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stream_device**
> StreamAsset delete_stream_device(stream_id, device_id)

Detach Network Edge Device

This API provides capability to detach a Network Edge Device and all of its interfaces from a stream

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream_asset import StreamAsset
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID
    device_id = '8a9b7c6d-1e2f-4a3b-9c4d-5e6f7a8b9c0d' # str | Network Edge Device UUID

    try:
        # Detach Network Edge Device
        api_response = api_instance.delete_stream_device(stream_id, device_id)
        print("The response of StreamsApi->delete_stream_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->delete_stream_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream UUID | 
 **device_id** | **str**| Network Edge Device UUID | 

### Return type

[**StreamAsset**](StreamAsset.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream Network Edge Device asset object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_asset_by_uuid**
> StreamAsset get_stream_asset_by_uuid(asset_id, asset, stream_id)

Get Asset

This API provides capability to get user's assets attached to a stream

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.asset import Asset
from equinix.services.fabricv4.models.stream_asset import StreamAsset
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    asset_id = '757400f8-d360-11e9-bb65-2a2ae2dbcce6' # str | asset UUID
    asset = equinix.services.fabricv4.Asset() # Asset | asset
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID

    try:
        # Get Asset
        api_response = api_instance.get_stream_asset_by_uuid(asset_id, asset, stream_id)
        print("The response of StreamsApi->get_stream_asset_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->get_stream_asset_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| asset UUID | 
 **asset** | [**Asset**](.md)| asset | 
 **stream_id** | **str**| Stream UUID | 

### Return type

[**StreamAsset**](StreamAsset.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream asset object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_by_uuid**
> Stream get_stream_by_uuid(stream_id)

Get Stream

This API provides capability to get user's stream

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream import Stream
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID

    try:
        # Get Stream
        api_response = api_instance.get_stream_by_uuid(stream_id)
        print("The response of StreamsApi->get_stream_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->get_stream_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream UUID | 

### Return type

[**Stream**](Stream.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_device**
> StreamAsset get_stream_device(stream_id, device_id)

Get Network Edge Device

This API provides capability to get a Network Edge Device and its interfaces attached to a stream

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream_asset import StreamAsset
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID
    device_id = '8a9b7c6d-1e2f-4a3b-9c4d-5e6f7a8b9c0d' # str | Network Edge Device UUID

    try:
        # Get Network Edge Device
        api_response = api_instance.get_stream_device(stream_id, device_id)
        print("The response of StreamsApi->get_stream_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->get_stream_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream UUID | 
 **device_id** | **str**| Network Edge Device UUID | 

### Return type

[**StreamAsset**](StreamAsset.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream Network Edge Device asset object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_streams**
> GetAllStreamResponse get_streams(offset=offset, limit=limit)

Get Streams

This API provides capability to retrieve streams

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_all_stream_response import GetAllStreamResponse
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get Streams
        api_response = api_instance.get_streams(offset=offset, limit=limit)
        print("The response of StreamsApi->get_streams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->get_streams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**GetAllStreamResponse**](GetAllStreamResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_stream_assets**
> SearchStreamAssetResponse search_stream_assets(stream_asset_search_request)

Search Stream Assets

This API provides capability to search stream assets

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.search_stream_asset_response import SearchStreamAssetResponse
from equinix.services.fabricv4.models.stream_asset_search_request import StreamAssetSearchRequest
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    stream_asset_search_request = {"filter":{"and":[{"property":"/uuid","operator":"IN","values":["8ac8ecfe-c7cb-4def-9f77-5ce93c19d83d","9ac8ecfe-c7cb-4def-9f77-5ce93c19d83e"]},{"property":"/streamUuid","operator":"=","values":["4719e319-65ae-4001-aabf-ca5f107b9b29"]},{"property":"/attachmentStatus","operator":"IN","values":["ATTACHED","ATTACHING"]}]},"sort":[{"direction":"DESC","property":"/uuid"}],"pagination":{"offset":0,"limit":20}} # StreamAssetSearchRequest | 

    try:
        # Search Stream Assets
        api_response = api_instance.search_stream_assets(stream_asset_search_request)
        print("The response of StreamsApi->search_stream_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->search_stream_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_asset_search_request** | [**StreamAssetSearchRequest**](StreamAssetSearchRequest.md)|  | 

### Return type

[**SearchStreamAssetResponse**](SearchStreamAssetResponse.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_streams**
> SearchStreamResponse search_streams(stream_search_request=stream_search_request)

Search Streams

This API provides capability to search streams

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.search_stream_response import SearchStreamResponse
from equinix.services.fabricv4.models.stream_search_request import StreamSearchRequest
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    stream_search_request = {"filter":{"and":[{"property":"/project/projectId","operator":"IN","values":["2f7f1a59-2dbf-43f8-b1a4-3c1f4e4b55b5"]},{"or":[{"property":"/uuid","operator":"IN","values":["12f4d4a1-c7cb-4def-9f77-5ce93c19d999","8ac8ecfe-c7cb-4def-9f77-5ce93c19d83d"]}]},{"property":"/state","operator":"=","values":["PROVISIONED"]}]},"sort":[{"direction":"DESC","property":"/changeLog/createdDateTime"}],"pagination":{"offset":0,"limit":20}} # StreamSearchRequest |  (optional)

    try:
        # Search Streams
        api_response = api_instance.search_streams(stream_search_request=stream_search_request)
        print("The response of StreamsApi->search_streams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->search_streams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_search_request** | [**StreamSearchRequest**](StreamSearchRequest.md)|  | [optional] 

### Return type

[**SearchStreamResponse**](SearchStreamResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stream_asset_by_uuid**
> StreamAsset update_stream_asset_by_uuid(asset_id, asset, stream_id, stream_asset_put_request)

Attach Asset

This API provides capability to attach an asset to a stream

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.asset import Asset
from equinix.services.fabricv4.models.stream_asset import StreamAsset
from equinix.services.fabricv4.models.stream_asset_put_request import StreamAssetPutRequest
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    asset_id = '757400f8-d360-11e9-bb65-2a2ae2dbcce6' # str | asset UUID
    asset = equinix.services.fabricv4.Asset() # Asset | asset
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID
    stream_asset_put_request = {"metricsEnabled":false} # StreamAssetPutRequest | 

    try:
        # Attach Asset
        api_response = api_instance.update_stream_asset_by_uuid(asset_id, asset, stream_id, stream_asset_put_request)
        print("The response of StreamsApi->update_stream_asset_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->update_stream_asset_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| asset UUID | 
 **asset** | [**Asset**](.md)| asset | 
 **stream_id** | **str**| Stream UUID | 
 **stream_asset_put_request** | [**StreamAssetPutRequest**](StreamAssetPutRequest.md)|  | 

### Return type

[**StreamAsset**](StreamAsset.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stream_by_uuid**
> Stream update_stream_by_uuid(stream_id, stream_put_request)

Update Stream

This API provides capability to update user's stream

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream import Stream
from equinix.services.fabricv4.models.stream_put_request import StreamPutRequest
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID
    stream_put_request = {"name":"splunk1","description":"subscription 1"} # StreamPutRequest | 

    try:
        # Update Stream
        api_response = api_instance.update_stream_by_uuid(stream_id, stream_put_request)
        print("The response of StreamsApi->update_stream_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->update_stream_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream UUID | 
 **stream_put_request** | [**StreamPutRequest**](StreamPutRequest.md)|  | 

### Return type

[**Stream**](Stream.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stream_device**
> StreamAsset update_stream_device(stream_id, device_id, stream_device_put_request)

Attach Network Edge Device Interfaces

This API provides capability to attach a Network Edge Device and its interfaces to a stream. The provided interfaces list is the complete desired set: interfaces not in the list are detached, new interfaces are attached. An empty or absent interfaces list detaches all currently attached interfaces. metricsEnabled must be true when interfaces are provided.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream_asset import StreamAsset
from equinix.services.fabricv4.models.stream_device_put_request import StreamDevicePutRequest
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
    api_instance = equinix.services.fabricv4.StreamsApi(api_client)
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID
    device_id = '8a9b7c6d-1e2f-4a3b-9c4d-5e6f7a8b9c0d' # str | Network Edge Device UUID
    stream_device_put_request = {"metricsEnabled":true,"interfaces":[{"id":3},{"id":5}]} # StreamDevicePutRequest | 

    try:
        # Attach Network Edge Device Interfaces
        api_response = api_instance.update_stream_device(stream_id, device_id, stream_device_put_request)
        print("The response of StreamsApi->update_stream_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->update_stream_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream UUID | 
 **device_id** | **str**| Network Edge Device UUID | 
 **stream_device_put_request** | [**StreamDevicePutRequest**](StreamDevicePutRequest.md)|  | 

### Return type

[**StreamAsset**](StreamAsset.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream Network Edge Device asset object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

