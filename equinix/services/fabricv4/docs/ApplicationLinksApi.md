# equinix.services.fabricv4.ApplicationLinksApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_app_domain_to_app_link**](ApplicationLinksApi.md#attach_app_domain_to_app_link) | **PUT** /fabric/v4/appLinks/{appLinkId}/appDomains/{appDomainId} | Attach App Domain to App Link
[**attach_app_service_to_app_link**](ApplicationLinksApi.md#attach_app_service_to_app_link) | **PUT** /fabric/v4/appLinks/{appLinkId}/appServices/{appServiceId} | Attach App Service to App Link
[**create_app_link**](ApplicationLinksApi.md#create_app_link) | **POST** /fabric/v4/appLinks | Create App Link
[**delete_app_link_by_uuid**](ApplicationLinksApi.md#delete_app_link_by_uuid) | **DELETE** /fabric/v4/appLinks/{appLinkId} | Delete App Link
[**detach_app_domain_from_app_link**](ApplicationLinksApi.md#detach_app_domain_from_app_link) | **DELETE** /fabric/v4/appLinks/{appLinkId}/appDomains/{appDomainId} | Detach App Domain from App Link
[**detach_app_service_from_app_link**](ApplicationLinksApi.md#detach_app_service_from_app_link) | **DELETE** /fabric/v4/appLinks/{appLinkId}/appServices/{appServiceId} | Detach App Service from App Link
[**get_app_link_by_uuid**](ApplicationLinksApi.md#get_app_link_by_uuid) | **GET** /fabric/v4/appLinks/{appLinkId} | Get App Link
[**get_attached_app_domain_by_uuid**](ApplicationLinksApi.md#get_attached_app_domain_by_uuid) | **GET** /fabric/v4/appLinks/{appLinkId}/appDomains/{appDomainId} | Get attached App Domain for App Link
[**get_attached_app_domains_by_app_link_id**](ApplicationLinksApi.md#get_attached_app_domains_by_app_link_id) | **GET** /fabric/v4/appLinks/{appLinkId}/appDomains | Get attached App Domains for App Link
[**get_attached_app_service_by_uuid**](ApplicationLinksApi.md#get_attached_app_service_by_uuid) | **GET** /fabric/v4/appLinks/{appLinkId}/appServices/{appServiceId} | Get attached App Service for App Link
[**get_attached_app_services_by_app_link_id**](ApplicationLinksApi.md#get_attached_app_services_by_app_link_id) | **GET** /fabric/v4/appLinks/{appLinkId}/appServices | Get attached App Services for App Link
[**search_app_links**](ApplicationLinksApi.md#search_app_links) | **POST** /fabric/v4/appLinks/search | Search App Links
[**search_attached_app_domains**](ApplicationLinksApi.md#search_attached_app_domains) | **POST** /fabric/v4/appLinks/{appLinkId}/appDomains/search | Search attached App Domain to App Link
[**search_attached_app_services**](ApplicationLinksApi.md#search_attached_app_services) | **POST** /fabric/v4/appLinks/{appLinkId}/appServices/search | Search attached App Service to App Link
[**update_app_link_by_uuid**](ApplicationLinksApi.md#update_app_link_by_uuid) | **PATCH** /fabric/v4/appLinks/{appLinkId} | Update App Link
[**update_app_service_attachment_to_app_link**](ApplicationLinksApi.md#update_app_service_attachment_to_app_link) | **PATCH** /fabric/v4/appLinks/{appLinkId}/appServices/{appServiceId} | Update App Service attachment to App Link


# **attach_app_domain_to_app_link**
> AppLinkAppDomainAttachment attach_app_domain_to_app_link(app_link_id, app_domain_id)

Attach App Domain to App Link

This API provides ability to attach the user's App Domain to App Link.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_app_domain_attachment import AppLinkAppDomainAttachment
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID
    app_domain_id = 'app_domain_id_example' # str | App Domain UUID

    try:
        # Attach App Domain to App Link
        api_response = api_instance.attach_app_domain_to_app_link(app_link_id, app_domain_id)
        print("The response of ApplicationLinksApi->attach_app_domain_to_app_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->attach_app_domain_to_app_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 
 **app_domain_id** | **str**| App Domain UUID | 

### Return type

[**AppLinkAppDomainAttachment**](AppLinkAppDomainAttachment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Attach App Domain object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_app_service_to_app_link**
> AppLinkAppServiceAttachment attach_app_service_to_app_link(app_link_id, app_service_id, app_link_attach_service_request)

Attach App Service to App Link

This API provides ability to attach the user's App Service to App Link.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_app_service_attachment import AppLinkAppServiceAttachment
from equinix.services.fabricv4.models.app_link_attach_service_request import AppLinkAttachServiceRequest
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID
    app_service_id = 'app_service_id_example' # str | App Service UUID
    app_link_attach_service_request = equinix.services.fabricv4.AppLinkAttachServiceRequest() # AppLinkAttachServiceRequest | 

    try:
        # Attach App Service to App Link
        api_response = api_instance.attach_app_service_to_app_link(app_link_id, app_service_id, app_link_attach_service_request)
        print("The response of ApplicationLinksApi->attach_app_service_to_app_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->attach_app_service_to_app_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 
 **app_service_id** | **str**| App Service UUID | 
 **app_link_attach_service_request** | [**AppLinkAttachServiceRequest**](AppLinkAttachServiceRequest.md)|  | 

### Return type

[**AppLinkAppServiceAttachment**](AppLinkAppServiceAttachment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Attach App Service object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_link**
> AppLink create_app_link(app_link_post_request)

Create App Link

This API provides capability to create user's App Link

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link import AppLink
from equinix.services.fabricv4.models.app_link_post_request import AppLinkPostRequest
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_post_request = equinix.services.fabricv4.AppLinkPostRequest() # AppLinkPostRequest | 

    try:
        # Create App Link
        api_response = api_instance.create_app_link(app_link_post_request)
        print("The response of ApplicationLinksApi->create_app_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->create_app_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_post_request** | [**AppLinkPostRequest**](AppLinkPostRequest.md)|  | 

### Return type

[**AppLink**](AppLink.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | App Link object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_link_by_uuid**
> AppLink delete_app_link_by_uuid(app_link_id)

Delete App Link

This API provides capability to delete user's App Link

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link import AppLink
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID

    try:
        # Delete App Link
        api_response = api_instance.delete_app_link_by_uuid(app_link_id)
        print("The response of ApplicationLinksApi->delete_app_link_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->delete_app_link_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 

### Return type

[**AppLink**](AppLink.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | App Link object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_app_domain_from_app_link**
> AppLinkAppDomainAttachment detach_app_domain_from_app_link(app_link_id, app_domain_id)

Detach App Domain from App Link

This API provides ability to detach App Domain from App Link

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_app_domain_attachment import AppLinkAppDomainAttachment
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID
    app_domain_id = 'app_domain_id_example' # str | App Domain UUID

    try:
        # Detach App Domain from App Link
        api_response = api_instance.detach_app_domain_from_app_link(app_link_id, app_domain_id)
        print("The response of ApplicationLinksApi->detach_app_domain_from_app_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->detach_app_domain_from_app_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 
 **app_domain_id** | **str**| App Domain UUID | 

### Return type

[**AppLinkAppDomainAttachment**](AppLinkAppDomainAttachment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Detach App Domain object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_app_service_from_app_link**
> AppLinkAppServiceAttachment detach_app_service_from_app_link(app_link_id, app_service_id)

Detach App Service from App Link

This API provides ability to detach App Service from App Link

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_app_service_attachment import AppLinkAppServiceAttachment
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID
    app_service_id = 'app_service_id_example' # str | App Service UUID

    try:
        # Detach App Service from App Link
        api_response = api_instance.detach_app_service_from_app_link(app_link_id, app_service_id)
        print("The response of ApplicationLinksApi->detach_app_service_from_app_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->detach_app_service_from_app_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 
 **app_service_id** | **str**| App Service UUID | 

### Return type

[**AppLinkAppServiceAttachment**](AppLinkAppServiceAttachment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Detach App Service object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_link_by_uuid**
> AppLink get_app_link_by_uuid(app_link_id)

Get App Link

This API provides capability to retrieve user's App Link

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link import AppLink
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID

    try:
        # Get App Link
        api_response = api_instance.get_app_link_by_uuid(app_link_id)
        print("The response of ApplicationLinksApi->get_app_link_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->get_app_link_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 

### Return type

[**AppLink**](AppLink.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App Link object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attached_app_domain_by_uuid**
> AppLinkAppDomainAttachment get_attached_app_domain_by_uuid(app_link_id, app_domain_id)

Get attached App Domain for App Link

This API provides ability to retrieve an App Domain attached to an App Link.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_app_domain_attachment import AppLinkAppDomainAttachment
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID
    app_domain_id = 'app_domain_id_example' # str | App Domain UUID

    try:
        # Get attached App Domain for App Link
        api_response = api_instance.get_attached_app_domain_by_uuid(app_link_id, app_domain_id)
        print("The response of ApplicationLinksApi->get_attached_app_domain_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->get_attached_app_domain_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 
 **app_domain_id** | **str**| App Domain UUID | 

### Return type

[**AppLinkAppDomainAttachment**](AppLinkAppDomainAttachment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attached App Domain object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attached_app_domains_by_app_link_id**
> AppLinkAttachedAppDomains get_attached_app_domains_by_app_link_id(app_link_id, offset=offset, limit=limit, attachment_status=attachment_status, order=order, style=style)

Get attached App Domains for App Link

This API provides capability to retrieve App Domains attached to an App Link.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_attach_state import AppLinkAttachState
from equinix.services.fabricv4.models.app_link_attached_app_domains import AppLinkAttachedAppDomains
from equinix.services.fabricv4.models.attached_app_domain_order import AttachedAppDomainOrder
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)
    attachment_status = [equinix.services.fabricv4.AppLinkAttachState()] # List[AppLinkAttachState] | Filter attached App Domains by one or more attachment lifecycle states. (optional)
    order = DESC # AttachedAppDomainOrder | Sort order for attached App Domains. (optional) (default to DESC)
    style = MEDIUM # Style | Detail level of the response. (optional) (default to MEDIUM)

    try:
        # Get attached App Domains for App Link
        api_response = api_instance.get_attached_app_domains_by_app_link_id(app_link_id, offset=offset, limit=limit, attachment_status=attachment_status, order=order, style=style)
        print("The response of ApplicationLinksApi->get_attached_app_domains_by_app_link_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->get_attached_app_domains_by_app_link_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 
 **attachment_status** | [**List[AppLinkAttachState]**](AppLinkAttachState.md)| Filter attached App Domains by one or more attachment lifecycle states. | [optional] 
 **order** | [**AttachedAppDomainOrder**](.md)| Sort order for attached App Domains. | [optional] [default to DESC]
 **style** | [**Style**](.md)| Detail level of the response. | [optional] [default to MEDIUM]

### Return type

[**AppLinkAttachedAppDomains**](AppLinkAttachedAppDomains.md)

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

# **get_attached_app_service_by_uuid**
> AppLinkAppServiceAttachment get_attached_app_service_by_uuid(app_link_id, app_service_id)

Get attached App Service for App Link

This API provides ability to retrieve an App Service attached to an App Link.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_app_service_attachment import AppLinkAppServiceAttachment
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID
    app_service_id = 'app_service_id_example' # str | App Service UUID

    try:
        # Get attached App Service for App Link
        api_response = api_instance.get_attached_app_service_by_uuid(app_link_id, app_service_id)
        print("The response of ApplicationLinksApi->get_attached_app_service_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->get_attached_app_service_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 
 **app_service_id** | **str**| App Service UUID | 

### Return type

[**AppLinkAppServiceAttachment**](AppLinkAppServiceAttachment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attached App Service object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attached_app_services_by_app_link_id**
> AppLinkAttachedAppServices get_attached_app_services_by_app_link_id(app_link_id, offset=offset, limit=limit, attachment_status=attachment_status, order=order, style=style)

Get attached App Services for App Link

This API provides capability to retrieve App Services attached to an App Link.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_attach_state import AppLinkAttachState
from equinix.services.fabricv4.models.app_link_attached_app_services import AppLinkAttachedAppServices
from equinix.services.fabricv4.models.attached_app_service_order import AttachedAppServiceOrder
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)
    attachment_status = [equinix.services.fabricv4.AppLinkAttachState()] # List[AppLinkAttachState] | Filter attached App Services by one or more attachment lifecycle states. (optional)
    order = DESC # AttachedAppServiceOrder | Sort order for attached App Services. (optional) (default to DESC)
    style = MEDIUM # Style | Detail level of the response. (optional) (default to MEDIUM)

    try:
        # Get attached App Services for App Link
        api_response = api_instance.get_attached_app_services_by_app_link_id(app_link_id, offset=offset, limit=limit, attachment_status=attachment_status, order=order, style=style)
        print("The response of ApplicationLinksApi->get_attached_app_services_by_app_link_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->get_attached_app_services_by_app_link_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 
 **attachment_status** | [**List[AppLinkAttachState]**](AppLinkAttachState.md)| Filter attached App Services by one or more attachment lifecycle states. | [optional] 
 **order** | [**AttachedAppServiceOrder**](.md)| Sort order for attached App Services. | [optional] [default to DESC]
 **style** | [**Style**](.md)| Detail level of the response. | [optional] [default to MEDIUM]

### Return type

[**AppLinkAttachedAppServices**](AppLinkAttachedAppServices.md)

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

# **search_app_links**
> AppLinkSearchResponse search_app_links(app_link_search_request)

Search App Links

The API provides capability to get list of user's App Links using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_search_request import AppLinkSearchRequest
from equinix.services.fabricv4.models.app_link_search_response import AppLinkSearchResponse
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_search_request = equinix.services.fabricv4.AppLinkSearchRequest() # AppLinkSearchRequest | 

    try:
        # Search App Links
        api_response = api_instance.search_app_links(app_link_search_request)
        print("The response of ApplicationLinksApi->search_app_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->search_app_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_search_request** | [**AppLinkSearchRequest**](AppLinkSearchRequest.md)|  | 

### Return type

[**AppLinkSearchResponse**](AppLinkSearchResponse.md)

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

# **search_attached_app_domains**
> AppLinkAttachDomainSearchResponse search_attached_app_domains(app_link_id, app_link_attach_domain_search_request)

Search attached App Domain to App Link

The API provides capability to get list of user's attached App Domains using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_attach_domain_search_request import AppLinkAttachDomainSearchRequest
from equinix.services.fabricv4.models.app_link_attach_domain_search_response import AppLinkAttachDomainSearchResponse
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID
    app_link_attach_domain_search_request = equinix.services.fabricv4.AppLinkAttachDomainSearchRequest() # AppLinkAttachDomainSearchRequest | 

    try:
        # Search attached App Domain to App Link
        api_response = api_instance.search_attached_app_domains(app_link_id, app_link_attach_domain_search_request)
        print("The response of ApplicationLinksApi->search_attached_app_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->search_attached_app_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 
 **app_link_attach_domain_search_request** | [**AppLinkAttachDomainSearchRequest**](AppLinkAttachDomainSearchRequest.md)|  | 

### Return type

[**AppLinkAttachDomainSearchResponse**](AppLinkAttachDomainSearchResponse.md)

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

# **search_attached_app_services**
> AppLinkAttachServiceSearchResponse search_attached_app_services(app_link_id, app_link_attach_service_search_request)

Search attached App Service to App Link

The API provides capability to get list of user's attached App Services using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_attach_service_search_request import AppLinkAttachServiceSearchRequest
from equinix.services.fabricv4.models.app_link_attach_service_search_response import AppLinkAttachServiceSearchResponse
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID
    app_link_attach_service_search_request = equinix.services.fabricv4.AppLinkAttachServiceSearchRequest() # AppLinkAttachServiceSearchRequest | 

    try:
        # Search attached App Service to App Link
        api_response = api_instance.search_attached_app_services(app_link_id, app_link_attach_service_search_request)
        print("The response of ApplicationLinksApi->search_attached_app_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->search_attached_app_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 
 **app_link_attach_service_search_request** | [**AppLinkAttachServiceSearchRequest**](AppLinkAttachServiceSearchRequest.md)|  | 

### Return type

[**AppLinkAttachServiceSearchResponse**](AppLinkAttachServiceSearchResponse.md)

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

# **update_app_link_by_uuid**
> AppLink update_app_link_by_uuid(app_link_id, app_link_change_operation)

Update App Link

This API provides capability to update user's App Link

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link import AppLink
from equinix.services.fabricv4.models.app_link_change_operation import AppLinkChangeOperation
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID
    app_link_change_operation = [equinix.services.fabricv4.AppLinkChangeOperation()] # List[AppLinkChangeOperation] | 

    try:
        # Update App Link
        api_response = api_instance.update_app_link_by_uuid(app_link_id, app_link_change_operation)
        print("The response of ApplicationLinksApi->update_app_link_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->update_app_link_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 
 **app_link_change_operation** | [**List[AppLinkChangeOperation]**](AppLinkChangeOperation.md)|  | 

### Return type

[**AppLink**](AppLink.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | App Link object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_service_attachment_to_app_link**
> AppLinkAppServiceAttachment update_app_service_attachment_to_app_link(app_link_id, app_service_id, app_link_app_service_attachment_change_operation)

Update App Service attachment to App Link

This API provides ability to update the App Service attachment to App Link.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_link_app_service_attachment import AppLinkAppServiceAttachment
from equinix.services.fabricv4.models.app_link_app_service_attachment_change_operation import AppLinkAppServiceAttachmentChangeOperation
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
    api_instance = equinix.services.fabricv4.ApplicationLinksApi(api_client)
    app_link_id = 'app_link_id_example' # str | App Link UUID
    app_service_id = 'app_service_id_example' # str | App Service UUID
    app_link_app_service_attachment_change_operation = [equinix.services.fabricv4.AppLinkAppServiceAttachmentChangeOperation()] # List[AppLinkAppServiceAttachmentChangeOperation] | 

    try:
        # Update App Service attachment to App Link
        api_response = api_instance.update_app_service_attachment_to_app_link(app_link_id, app_service_id, app_link_app_service_attachment_change_operation)
        print("The response of ApplicationLinksApi->update_app_service_attachment_to_app_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLinksApi->update_app_service_attachment_to_app_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_link_id** | **str**| App Link UUID | 
 **app_service_id** | **str**| App Service UUID | 
 **app_link_app_service_attachment_change_operation** | [**List[AppLinkAppServiceAttachmentChangeOperation]**](AppLinkAppServiceAttachmentChangeOperation.md)|  | 

### Return type

[**AppLinkAppServiceAttachment**](AppLinkAppServiceAttachment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Update App Service attachment object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

