# equinix.services.fabricv4.StreamSubscriptionsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stream_subscriptions**](StreamSubscriptionsApi.md#create_stream_subscriptions) | **POST** /fabric/v4/streamSubscriptions | Create Subscription
[**delete_stream_subscription_by_uuid**](StreamSubscriptionsApi.md#delete_stream_subscription_by_uuid) | **DELETE** /fabric/v4/streamSubscriptions/{streamSubscriptionId} | Delete Subscription
[**get_stream_subscription_by_uuid**](StreamSubscriptionsApi.md#get_stream_subscription_by_uuid) | **GET** /fabric/v4/streamSubscriptions/{streamSubscriptionId} | Get Subscription
[**get_stream_subscriptions**](StreamSubscriptionsApi.md#get_stream_subscriptions) | **GET** /fabric/v4/streamSubscriptions | Get Subscriptions
[**update_stream_subscription_by_uuid**](StreamSubscriptionsApi.md#update_stream_subscription_by_uuid) | **PUT** /fabric/v4/streamSubscriptions/{streamSubscriptionId} | Update Subscription


# **create_stream_subscriptions**
> StreamSubscription create_stream_subscriptions(stream_subscription_post_request)

Create Subscription

This API provides capability to create user's Stream Subscriptions

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream_subscription import StreamSubscription
from equinix.services.fabricv4.models.stream_subscription_post_request import StreamSubscriptionPostRequest
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
    api_instance = equinix.services.fabricv4.StreamSubscriptionsApi(api_client)
    stream_subscription_post_request = equinix.services.fabricv4.StreamSubscriptionPostRequest() # StreamSubscriptionPostRequest | 

    try:
        # Create Subscription
        api_response = api_instance.create_stream_subscriptions(stream_subscription_post_request)
        print("The response of StreamSubscriptionsApi->create_stream_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamSubscriptionsApi->create_stream_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_subscription_post_request** | [**StreamSubscriptionPostRequest**](StreamSubscriptionPostRequest.md)|  | 

### Return type

[**StreamSubscription**](StreamSubscription.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream Subscription object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stream_subscription_by_uuid**
> StreamSubscription delete_stream_subscription_by_uuid(stream_subscription_id)

Delete Subscription

This API provides capability to delete user's Stream Subscriptions

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream_subscription import StreamSubscription
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
    api_instance = equinix.services.fabricv4.StreamSubscriptionsApi(api_client)
    stream_subscription_id = 'stream_subscription_id_example' # str | Stream Subscription UUID

    try:
        # Delete Subscription
        api_response = api_instance.delete_stream_subscription_by_uuid(stream_subscription_id)
        print("The response of StreamSubscriptionsApi->delete_stream_subscription_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamSubscriptionsApi->delete_stream_subscription_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_subscription_id** | **str**| Stream Subscription UUID | 

### Return type

[**StreamSubscription**](StreamSubscription.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream Subscription object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_subscription_by_uuid**
> StreamSubscription get_stream_subscription_by_uuid(stream_subscription_id)

Get Subscription

This API provides capability to delete user's get Stream Subscriptions

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream_subscription import StreamSubscription
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
    api_instance = equinix.services.fabricv4.StreamSubscriptionsApi(api_client)
    stream_subscription_id = 'stream_subscription_id_example' # str | Stream Subscription UUID

    try:
        # Get Subscription
        api_response = api_instance.get_stream_subscription_by_uuid(stream_subscription_id)
        print("The response of StreamSubscriptionsApi->get_stream_subscription_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamSubscriptionsApi->get_stream_subscription_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_subscription_id** | **str**| Stream Subscription UUID | 

### Return type

[**StreamSubscription**](StreamSubscription.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream Subscription object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_subscriptions**
> GetAllStreamSubscriptionResponse get_stream_subscriptions(offset=offset, limit=limit)

Get Subscriptions

This API provides capability to retrieve stream subscriptions

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_all_stream_subscription_response import GetAllStreamSubscriptionResponse
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
    api_instance = equinix.services.fabricv4.StreamSubscriptionsApi(api_client)
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get Subscriptions
        api_response = api_instance.get_stream_subscriptions(offset=offset, limit=limit)
        print("The response of StreamSubscriptionsApi->get_stream_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamSubscriptionsApi->get_stream_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**GetAllStreamSubscriptionResponse**](GetAllStreamSubscriptionResponse.md)

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

# **update_stream_subscription_by_uuid**
> StreamSubscription update_stream_subscription_by_uuid(stream_subscription_id, stream_subscription_put_request)

Update Subscription

This API provides capability to update user's Stream Subscriptions

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream_subscription import StreamSubscription
from equinix.services.fabricv4.models.stream_subscription_put_request import StreamSubscriptionPutRequest
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
    api_instance = equinix.services.fabricv4.StreamSubscriptionsApi(api_client)
    stream_subscription_id = 'stream_subscription_id_example' # str | Stream Subscription UUID
    stream_subscription_put_request = equinix.services.fabricv4.StreamSubscriptionPutRequest() # StreamSubscriptionPutRequest | 

    try:
        # Update Subscription
        api_response = api_instance.update_stream_subscription_by_uuid(stream_subscription_id, stream_subscription_put_request)
        print("The response of StreamSubscriptionsApi->update_stream_subscription_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamSubscriptionsApi->update_stream_subscription_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_subscription_id** | **str**| Stream Subscription UUID | 
 **stream_subscription_put_request** | [**StreamSubscriptionPutRequest**](StreamSubscriptionPutRequest.md)|  | 

### Return type

[**StreamSubscription**](StreamSubscription.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream Subscription object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

