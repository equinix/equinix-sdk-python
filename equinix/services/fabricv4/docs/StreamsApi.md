# equinix.services.fabricv4.StreamsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_streams**](StreamsApi.md#create_streams) | **POST** /fabric/v4/streams | Create Stream
[**delete_stream_asset_by_uuid**](StreamsApi.md#delete_stream_asset_by_uuid) | **DELETE** /fabric/v4/streams/{streamId}/{asset}/{assetId} | Detach Asset
[**delete_stream_by_uuid**](StreamsApi.md#delete_stream_by_uuid) | **DELETE** /fabric/v4/streams/{streamId} | Delete Stream
[**get_stream_asset_by_uuid**](StreamsApi.md#get_stream_asset_by_uuid) | **GET** /fabric/v4/streams/{streamId}/{asset}/{assetId} | Get Asset
[**get_stream_by_uuid**](StreamsApi.md#get_stream_by_uuid) | **GET** /fabric/v4/streams/{streamId} | Get Stream
[**get_streams**](StreamsApi.md#get_streams) | **GET** /fabric/v4/streams | Get Streams
[**get_streams_assets**](StreamsApi.md#get_streams_assets) | **POST** /fabric/v4/streamAssets/search | Get Assets
[**update_stream_asset_by_uuid**](StreamsApi.md#update_stream_asset_by_uuid) | **PUT** /fabric/v4/streams/{streamId}/{asset}/{assetId} | Attach Asset
[**update_stream_by_uuid**](StreamsApi.md#update_stream_by_uuid) | **PUT** /fabric/v4/streams/{streamId} | Update Stream


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
    stream_post_request = equinix.services.fabricv4.StreamPostRequest() # StreamPostRequest | 

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
    asset_id = 'asset_id_example' # str | asset UUID
    asset = equinix.services.fabricv4.Asset() # Asset | asset
    stream_id = 'stream_id_example' # str | Stream UUID

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
    stream_id = 'stream_id_example' # str | Stream UUID

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
    asset_id = 'asset_id_example' # str | asset UUID
    asset = equinix.services.fabricv4.Asset() # Asset | asset
    stream_id = 'stream_id_example' # str | Stream UUID

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
    stream_id = 'stream_id_example' # str | Stream UUID

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

# **get_streams_assets**
> GetAllStreamAssetResponse get_streams_assets(stream_asset_search_request, offset=offset, limit=limit)

Get Assets

This API provides capability to retrieve stream assets

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_all_stream_asset_response import GetAllStreamAssetResponse
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
    stream_asset_search_request = equinix.services.fabricv4.StreamAssetSearchRequest() # StreamAssetSearchRequest | 
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get Assets
        api_response = api_instance.get_streams_assets(stream_asset_search_request, offset=offset, limit=limit)
        print("The response of StreamsApi->get_streams_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->get_streams_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_asset_search_request** | [**StreamAssetSearchRequest**](StreamAssetSearchRequest.md)|  | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**GetAllStreamAssetResponse**](GetAllStreamAssetResponse.md)

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
    asset_id = 'asset_id_example' # str | asset UUID
    asset = equinix.services.fabricv4.Asset() # Asset | asset
    stream_id = 'stream_id_example' # str | Stream UUID
    stream_asset_put_request = equinix.services.fabricv4.StreamAssetPutRequest() # StreamAssetPutRequest | 

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
    stream_id = 'stream_id_example' # str | Stream UUID
    stream_put_request = equinix.services.fabricv4.StreamPutRequest() # StreamPutRequest | 

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

