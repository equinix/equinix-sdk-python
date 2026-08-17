# equinix.services.fabricv4.ApplicationServicesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_service**](ApplicationServicesApi.md#create_app_service) | **POST** /fabric/v4/appServices | Create App Service
[**delete_app_service_by_uuid**](ApplicationServicesApi.md#delete_app_service_by_uuid) | **DELETE** /fabric/v4/appServices/{appServiceId} | Delete App Service
[**get_app_service_by_uuid**](ApplicationServicesApi.md#get_app_service_by_uuid) | **GET** /fabric/v4/appServices/{appServiceId} | Get App Service
[**get_attached_app_links_by_app_service_id**](ApplicationServicesApi.md#get_attached_app_links_by_app_service_id) | **GET** /fabric/v4/appServices/{appServiceId}/appLinks | Get attached App Links for App Service
[**get_attached_app_subscriptions_by_app_service_id**](ApplicationServicesApi.md#get_attached_app_subscriptions_by_app_service_id) | **GET** /fabric/v4/appServices/{appServiceId}/appSubscriptions | Get attached App Subscriptions for App Service
[**search_app_services**](ApplicationServicesApi.md#search_app_services) | **POST** /fabric/v4/appServices/search | Search App Services
[**search_attached_app_subscriptions_by_app_service_id**](ApplicationServicesApi.md#search_attached_app_subscriptions_by_app_service_id) | **POST** /fabric/v4/appServices/{appServiceId}/appSubscriptions/search | Search attached App Subscriptions
[**update_app_service_by_uuid**](ApplicationServicesApi.md#update_app_service_by_uuid) | **PATCH** /fabric/v4/appServices/{appServiceId} | Update App Service


# **create_app_service**
> AppService create_app_service(app_service_post_request)

Create App Service

This API provides capability to create user's App Service

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_service import AppService
from equinix.services.fabricv4.models.app_service_post_request import AppServicePostRequest
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
    api_instance = equinix.services.fabricv4.ApplicationServicesApi(api_client)
    app_service_post_request = equinix.services.fabricv4.AppServicePostRequest() # AppServicePostRequest | 

    try:
        # Create App Service
        api_response = api_instance.create_app_service(app_service_post_request)
        print("The response of ApplicationServicesApi->create_app_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationServicesApi->create_app_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_service_post_request** | [**AppServicePostRequest**](AppServicePostRequest.md)|  | 

### Return type

[**AppService**](AppService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | App Service object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_service_by_uuid**
> AppService delete_app_service_by_uuid(app_service_id)

Delete App Service

This API provides capability to delete user's App Service

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_service import AppService
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
    api_instance = equinix.services.fabricv4.ApplicationServicesApi(api_client)
    app_service_id = 'app_service_id_example' # str | App Service UUID

    try:
        # Delete App Service
        api_response = api_instance.delete_app_service_by_uuid(app_service_id)
        print("The response of ApplicationServicesApi->delete_app_service_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationServicesApi->delete_app_service_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_service_id** | **str**| App Service UUID | 

### Return type

[**AppService**](AppService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | App Service object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_service_by_uuid**
> AppService get_app_service_by_uuid(app_service_id)

Get App Service

This API provides capability to retrieve user's App Service

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_service import AppService
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
    api_instance = equinix.services.fabricv4.ApplicationServicesApi(api_client)
    app_service_id = 'app_service_id_example' # str | App Service UUID

    try:
        # Get App Service
        api_response = api_instance.get_app_service_by_uuid(app_service_id)
        print("The response of ApplicationServicesApi->get_app_service_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationServicesApi->get_app_service_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_service_id** | **str**| App Service UUID | 

### Return type

[**AppService**](AppService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App Service object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attached_app_links_by_app_service_id**
> AppServiceAttachedAppLinks get_attached_app_links_by_app_service_id(app_service_id, offset=offset, limit=limit, state=state, order=order, style=style)

Get attached App Links for App Service

This API provides capability to retrieve App Links attached to an App Service.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_state import AppLinkState
from equinix.services.fabricv4.models.app_service_attached_app_links import AppServiceAttachedAppLinks
from equinix.services.fabricv4.models.attached_app_link_order import AttachedAppLinkOrder
from equinix.services.fabricv4.models.style import Style
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
    api_instance = equinix.services.fabricv4.ApplicationServicesApi(api_client)
    app_service_id = 'app_service_id_example' # str | App Service UUID
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)
    state = [equinix.services.fabricv4.AppLinkState()] # List[AppLinkState] | Filter attached App Links by one or more lifecycle states. (optional)
    order = DESC # AttachedAppLinkOrder | Sort order for attached App Links. (optional) (default to DESC)
    style = MEDIUM # Style | Detail level of the response. (optional) (default to MEDIUM)

    try:
        # Get attached App Links for App Service
        api_response = api_instance.get_attached_app_links_by_app_service_id(app_service_id, offset=offset, limit=limit, state=state, order=order, style=style)
        print("The response of ApplicationServicesApi->get_attached_app_links_by_app_service_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationServicesApi->get_attached_app_links_by_app_service_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_service_id** | **str**| App Service UUID | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 
 **state** | [**List[AppLinkState]**](AppLinkState.md)| Filter attached App Links by one or more lifecycle states. | [optional] 
 **order** | [**AttachedAppLinkOrder**](.md)| Sort order for attached App Links. | [optional] [default to DESC]
 **style** | [**Style**](.md)| Detail level of the response. | [optional] [default to MEDIUM]

### Return type

[**AppServiceAttachedAppLinks**](AppServiceAttachedAppLinks.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attached_app_subscriptions_by_app_service_id**
> AppServiceAttachedAppSubscriptions get_attached_app_subscriptions_by_app_service_id(app_service_id, offset=offset, limit=limit, state=state, order=order, style=style)

Get attached App Subscriptions for App Service

This API provides capability to retrieve App Subscriptions attached to an App Service.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_service_attached_app_subscriptions import AppServiceAttachedAppSubscriptions
from equinix.services.fabricv4.models.app_subscription_state import AppSubscriptionState
from equinix.services.fabricv4.models.attached_app_subscription_order import AttachedAppSubscriptionOrder
from equinix.services.fabricv4.models.style import Style
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
    api_instance = equinix.services.fabricv4.ApplicationServicesApi(api_client)
    app_service_id = 'app_service_id_example' # str | App Service UUID
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)
    state = [equinix.services.fabricv4.AppSubscriptionState()] # List[AppSubscriptionState] | Filter attached App Subscriptions by one or more lifecycle states. (optional)
    order = DESC # AttachedAppSubscriptionOrder | Sort order for attached App Subscriptions. (optional) (default to DESC)
    style = MEDIUM # Style | Detail level of the response. (optional) (default to MEDIUM)

    try:
        # Get attached App Subscriptions for App Service
        api_response = api_instance.get_attached_app_subscriptions_by_app_service_id(app_service_id, offset=offset, limit=limit, state=state, order=order, style=style)
        print("The response of ApplicationServicesApi->get_attached_app_subscriptions_by_app_service_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationServicesApi->get_attached_app_subscriptions_by_app_service_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_service_id** | **str**| App Service UUID | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 
 **state** | [**List[AppSubscriptionState]**](AppSubscriptionState.md)| Filter attached App Subscriptions by one or more lifecycle states. | [optional] 
 **order** | [**AttachedAppSubscriptionOrder**](.md)| Sort order for attached App Subscriptions. | [optional] [default to DESC]
 **style** | [**Style**](.md)| Detail level of the response. | [optional] [default to MEDIUM]

### Return type

[**AppServiceAttachedAppSubscriptions**](AppServiceAttachedAppSubscriptions.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_app_services**
> AppServiceSearchResponse search_app_services(app_service_search_request)

Search App Services

The API provides capability to get list of user's App Services using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_service_search_request import AppServiceSearchRequest
from equinix.services.fabricv4.models.app_service_search_response import AppServiceSearchResponse
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
    api_instance = equinix.services.fabricv4.ApplicationServicesApi(api_client)
    app_service_search_request = equinix.services.fabricv4.AppServiceSearchRequest() # AppServiceSearchRequest | 

    try:
        # Search App Services
        api_response = api_instance.search_app_services(app_service_search_request)
        print("The response of ApplicationServicesApi->search_app_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationServicesApi->search_app_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_service_search_request** | [**AppServiceSearchRequest**](AppServiceSearchRequest.md)|  | 

### Return type

[**AppServiceSearchResponse**](AppServiceSearchResponse.md)

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

# **search_attached_app_subscriptions_by_app_service_id**
> AppServiceAttachedAppSubscriptionSearchResponse search_attached_app_subscriptions_by_app_service_id(app_service_id, app_service_attached_app_subscription_search_request)

Search attached App Subscriptions

The API provides capability to get list of App Subscriptions attached to an App Service using search criteria.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_service_attached_app_subscription_search_request import AppServiceAttachedAppSubscriptionSearchRequest
from equinix.services.fabricv4.models.app_service_attached_app_subscription_search_response import AppServiceAttachedAppSubscriptionSearchResponse
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
    api_instance = equinix.services.fabricv4.ApplicationServicesApi(api_client)
    app_service_id = 'app_service_id_example' # str | App Service UUID
    app_service_attached_app_subscription_search_request = equinix.services.fabricv4.AppServiceAttachedAppSubscriptionSearchRequest() # AppServiceAttachedAppSubscriptionSearchRequest | 

    try:
        # Search attached App Subscriptions
        api_response = api_instance.search_attached_app_subscriptions_by_app_service_id(app_service_id, app_service_attached_app_subscription_search_request)
        print("The response of ApplicationServicesApi->search_attached_app_subscriptions_by_app_service_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationServicesApi->search_attached_app_subscriptions_by_app_service_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_service_id** | **str**| App Service UUID | 
 **app_service_attached_app_subscription_search_request** | [**AppServiceAttachedAppSubscriptionSearchRequest**](AppServiceAttachedAppSubscriptionSearchRequest.md)|  | 

### Return type

[**AppServiceAttachedAppSubscriptionSearchResponse**](AppServiceAttachedAppSubscriptionSearchResponse.md)

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

# **update_app_service_by_uuid**
> AppService update_app_service_by_uuid(app_service_id, app_service_change_operation)

Update App Service

This API provides capability to update user's App Service

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_service import AppService
from equinix.services.fabricv4.models.app_service_change_operation import AppServiceChangeOperation
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
    api_instance = equinix.services.fabricv4.ApplicationServicesApi(api_client)
    app_service_id = 'app_service_id_example' # str | App Service UUID
    app_service_change_operation = [equinix.services.fabricv4.AppServiceChangeOperation()] # List[AppServiceChangeOperation] | 

    try:
        # Update App Service
        api_response = api_instance.update_app_service_by_uuid(app_service_id, app_service_change_operation)
        print("The response of ApplicationServicesApi->update_app_service_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationServicesApi->update_app_service_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_service_id** | **str**| App Service UUID | 
 **app_service_change_operation** | [**List[AppServiceChangeOperation]**](AppServiceChangeOperation.md)|  | 

### Return type

[**AppService**](AppService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | App Service object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

