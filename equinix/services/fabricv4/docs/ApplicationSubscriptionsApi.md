# equinix.services.fabricv4.ApplicationSubscriptionsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_subscription**](ApplicationSubscriptionsApi.md#create_app_subscription) | **POST** /fabric/v4/appSubscriptions | Create App Subscription
[**delete_app_subscription_by_uuid**](ApplicationSubscriptionsApi.md#delete_app_subscription_by_uuid) | **DELETE** /fabric/v4/appSubscriptions/{appSubscriptionId} | Delete App Subscription
[**get_app_subscription_by_uuid**](ApplicationSubscriptionsApi.md#get_app_subscription_by_uuid) | **GET** /fabric/v4/appSubscriptions/{appSubscriptionId} | Get App Subscription
[**search_app_subscriptions**](ApplicationSubscriptionsApi.md#search_app_subscriptions) | **POST** /fabric/v4/appSubscriptions/search | Search App Subscriptions
[**update_app_subscription_by_uuid**](ApplicationSubscriptionsApi.md#update_app_subscription_by_uuid) | **PATCH** /fabric/v4/appSubscriptions/{appSubscriptionId} | Update App Subscription


# **create_app_subscription**
> AppSubscription create_app_subscription(app_subscription_post_request)

Create App Subscription

This API provides capability to create user's App Subscription

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_subscription import AppSubscription
from equinix.services.fabricv4.models.app_subscription_post_request import AppSubscriptionPostRequest
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
    api_instance = equinix.services.fabricv4.ApplicationSubscriptionsApi(api_client)
    app_subscription_post_request = equinix.services.fabricv4.AppSubscriptionPostRequest() # AppSubscriptionPostRequest | 

    try:
        # Create App Subscription
        api_response = api_instance.create_app_subscription(app_subscription_post_request)
        print("The response of ApplicationSubscriptionsApi->create_app_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSubscriptionsApi->create_app_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_subscription_post_request** | [**AppSubscriptionPostRequest**](AppSubscriptionPostRequest.md)|  | 

### Return type

[**AppSubscription**](AppSubscription.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | App Subscription object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_subscription_by_uuid**
> AppSubscription delete_app_subscription_by_uuid(app_subscription_id)

Delete App Subscription

This API provides capability to delete user's App Subscription

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_subscription import AppSubscription
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
    api_instance = equinix.services.fabricv4.ApplicationSubscriptionsApi(api_client)
    app_subscription_id = 'app_subscription_id_example' # str | App Subscription UUID

    try:
        # Delete App Subscription
        api_response = api_instance.delete_app_subscription_by_uuid(app_subscription_id)
        print("The response of ApplicationSubscriptionsApi->delete_app_subscription_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSubscriptionsApi->delete_app_subscription_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_subscription_id** | **str**| App Subscription UUID | 

### Return type

[**AppSubscription**](AppSubscription.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | App Subscription object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_subscription_by_uuid**
> AppSubscription get_app_subscription_by_uuid(app_subscription_id)

Get App Subscription

This API provides capability to retrieve user's App Subscription

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_subscription import AppSubscription
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
    api_instance = equinix.services.fabricv4.ApplicationSubscriptionsApi(api_client)
    app_subscription_id = 'app_subscription_id_example' # str | App Subscription UUID

    try:
        # Get App Subscription
        api_response = api_instance.get_app_subscription_by_uuid(app_subscription_id)
        print("The response of ApplicationSubscriptionsApi->get_app_subscription_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSubscriptionsApi->get_app_subscription_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_subscription_id** | **str**| App Subscription UUID | 

### Return type

[**AppSubscription**](AppSubscription.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App Subscription object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_app_subscriptions**
> AppSubscriptionSearchResponse search_app_subscriptions(app_subscription_search_request)

Search App Subscriptions

The API provides capability to get list of user's App Subscriptions using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_subscription_search_request import AppSubscriptionSearchRequest
from equinix.services.fabricv4.models.app_subscription_search_response import AppSubscriptionSearchResponse
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
    api_instance = equinix.services.fabricv4.ApplicationSubscriptionsApi(api_client)
    app_subscription_search_request = equinix.services.fabricv4.AppSubscriptionSearchRequest() # AppSubscriptionSearchRequest | 

    try:
        # Search App Subscriptions
        api_response = api_instance.search_app_subscriptions(app_subscription_search_request)
        print("The response of ApplicationSubscriptionsApi->search_app_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSubscriptionsApi->search_app_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_subscription_search_request** | [**AppSubscriptionSearchRequest**](AppSubscriptionSearchRequest.md)|  | 

### Return type

[**AppSubscriptionSearchResponse**](AppSubscriptionSearchResponse.md)

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
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_subscription_by_uuid**
> AppSubscription update_app_subscription_by_uuid(app_subscription_id, app_subscription_change_operation)

Update App Subscription

This API provides capability to update user's App Subscription

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_subscription import AppSubscription
from equinix.services.fabricv4.models.app_subscription_change_operation import AppSubscriptionChangeOperation
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
    api_instance = equinix.services.fabricv4.ApplicationSubscriptionsApi(api_client)
    app_subscription_id = 'app_subscription_id_example' # str | App Subscription UUID
    app_subscription_change_operation = [equinix.services.fabricv4.AppSubscriptionChangeOperation()] # List[AppSubscriptionChangeOperation] | 

    try:
        # Update App Subscription
        api_response = api_instance.update_app_subscription_by_uuid(app_subscription_id, app_subscription_change_operation)
        print("The response of ApplicationSubscriptionsApi->update_app_subscription_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSubscriptionsApi->update_app_subscription_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_subscription_id** | **str**| App Subscription UUID | 
 **app_subscription_change_operation** | [**List[AppSubscriptionChangeOperation]**](AppSubscriptionChangeOperation.md)|  | 

### Return type

[**AppSubscription**](AppSubscription.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | App Subscription object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

