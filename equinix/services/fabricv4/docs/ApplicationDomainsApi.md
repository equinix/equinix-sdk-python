# equinix.services.fabricv4.ApplicationDomainsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_domain**](ApplicationDomainsApi.md#create_app_domain) | **POST** /fabric/v4/appDomains | Create App Domain
[**delete_app_domain_by_uuid**](ApplicationDomainsApi.md#delete_app_domain_by_uuid) | **DELETE** /fabric/v4/appDomains/{appDomainId} | Delete App Domain
[**get_app_domain_by_uuid**](ApplicationDomainsApi.md#get_app_domain_by_uuid) | **GET** /fabric/v4/appDomains/{appDomainId} | Get App Domain
[**get_attached_app_links_by_app_domain_id**](ApplicationDomainsApi.md#get_attached_app_links_by_app_domain_id) | **GET** /fabric/v4/appDomains/{appDomainId}/appLinks | Get attached App Links for App Domain
[**search_app_domains**](ApplicationDomainsApi.md#search_app_domains) | **POST** /fabric/v4/appDomains/search | Search App Domains
[**update_app_domain_by_uuid**](ApplicationDomainsApi.md#update_app_domain_by_uuid) | **PATCH** /fabric/v4/appDomains/{appDomainId} | Update App Domain


# **create_app_domain**
> AppDomain create_app_domain(app_domain_post_request)

Create App Domain

This API provides capability to create user's App Domain

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_domain import AppDomain
from equinix.services.fabricv4.models.app_domain_post_request import AppDomainPostRequest
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
    api_instance = equinix.services.fabricv4.ApplicationDomainsApi(api_client)
    app_domain_post_request = equinix.services.fabricv4.AppDomainPostRequest() # AppDomainPostRequest | 

    try:
        # Create App Domain
        api_response = api_instance.create_app_domain(app_domain_post_request)
        print("The response of ApplicationDomainsApi->create_app_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationDomainsApi->create_app_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_domain_post_request** | [**AppDomainPostRequest**](AppDomainPostRequest.md)|  | 

### Return type

[**AppDomain**](AppDomain.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | App Domain object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_domain_by_uuid**
> AppDomain delete_app_domain_by_uuid(app_domain_id)

Delete App Domain

This API provides capability to delete user's App Domain

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_domain import AppDomain
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
    api_instance = equinix.services.fabricv4.ApplicationDomainsApi(api_client)
    app_domain_id = 'app_domain_id_example' # str | App Domain UUID

    try:
        # Delete App Domain
        api_response = api_instance.delete_app_domain_by_uuid(app_domain_id)
        print("The response of ApplicationDomainsApi->delete_app_domain_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationDomainsApi->delete_app_domain_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_domain_id** | **str**| App Domain UUID | 

### Return type

[**AppDomain**](AppDomain.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | App Domain object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_domain_by_uuid**
> AppDomain get_app_domain_by_uuid(app_domain_id)

Get App Domain

This API provides capability to retrieve user's App Domain

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_domain import AppDomain
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
    api_instance = equinix.services.fabricv4.ApplicationDomainsApi(api_client)
    app_domain_id = 'app_domain_id_example' # str | App Domain UUID

    try:
        # Get App Domain
        api_response = api_instance.get_app_domain_by_uuid(app_domain_id)
        print("The response of ApplicationDomainsApi->get_app_domain_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationDomainsApi->get_app_domain_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_domain_id** | **str**| App Domain UUID | 

### Return type

[**AppDomain**](AppDomain.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App Domain object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attached_app_links_by_app_domain_id**
> AppDomainAttachedAppLinks get_attached_app_links_by_app_domain_id(app_domain_id, offset=offset, limit=limit, state=state, order=order, style=style)

Get attached App Links for App Domain

This API provides capability to retrieve App Links attached to an App Domain.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_domain_attached_app_links import AppDomainAttachedAppLinks
from equinix.services.fabricv4.models.app_link_state import AppLinkState
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
    api_instance = equinix.services.fabricv4.ApplicationDomainsApi(api_client)
    app_domain_id = 'app_domain_id_example' # str | App Domain UUID
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)
    state = [equinix.services.fabricv4.AppLinkState()] # List[AppLinkState] | Filter attached App Links by one or more lifecycle states. (optional)
    order = DESC # AttachedAppLinkOrder | Sort order for attached App Links. (optional) (default to DESC)
    style = MEDIUM # Style | Detail level of the response. (optional) (default to MEDIUM)

    try:
        # Get attached App Links for App Domain
        api_response = api_instance.get_attached_app_links_by_app_domain_id(app_domain_id, offset=offset, limit=limit, state=state, order=order, style=style)
        print("The response of ApplicationDomainsApi->get_attached_app_links_by_app_domain_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationDomainsApi->get_attached_app_links_by_app_domain_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_domain_id** | **str**| App Domain UUID | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 
 **state** | [**List[AppLinkState]**](AppLinkState.md)| Filter attached App Links by one or more lifecycle states. | [optional] 
 **order** | [**AttachedAppLinkOrder**](.md)| Sort order for attached App Links. | [optional] [default to DESC]
 **style** | [**Style**](.md)| Detail level of the response. | [optional] [default to MEDIUM]

### Return type

[**AppDomainAttachedAppLinks**](AppDomainAttachedAppLinks.md)

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

# **search_app_domains**
> AppDomainSearchResponse search_app_domains(app_domain_search_request)

Search App Domains

The API provides capability to get list of user's App Domains using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_domain_search_request import AppDomainSearchRequest
from equinix.services.fabricv4.models.app_domain_search_response import AppDomainSearchResponse
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
    api_instance = equinix.services.fabricv4.ApplicationDomainsApi(api_client)
    app_domain_search_request = equinix.services.fabricv4.AppDomainSearchRequest() # AppDomainSearchRequest | 

    try:
        # Search App Domains
        api_response = api_instance.search_app_domains(app_domain_search_request)
        print("The response of ApplicationDomainsApi->search_app_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationDomainsApi->search_app_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_domain_search_request** | [**AppDomainSearchRequest**](AppDomainSearchRequest.md)|  | 

### Return type

[**AppDomainSearchResponse**](AppDomainSearchResponse.md)

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

# **update_app_domain_by_uuid**
> AppDomain update_app_domain_by_uuid(app_domain_id, app_domain_change_operation)

Update App Domain

This API provides capability to update user's App Domain

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_domain import AppDomain
from equinix.services.fabricv4.models.app_domain_change_operation import AppDomainChangeOperation
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
    api_instance = equinix.services.fabricv4.ApplicationDomainsApi(api_client)
    app_domain_id = 'app_domain_id_example' # str | App Domain UUID
    app_domain_change_operation = [equinix.services.fabricv4.AppDomainChangeOperation()] # List[AppDomainChangeOperation] | 

    try:
        # Update App Domain
        api_response = api_instance.update_app_domain_by_uuid(app_domain_id, app_domain_change_operation)
        print("The response of ApplicationDomainsApi->update_app_domain_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationDomainsApi->update_app_domain_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_domain_id** | **str**| App Domain UUID | 
 **app_domain_change_operation** | [**List[AppDomainChangeOperation]**](AppDomainChangeOperation.md)|  | 

### Return type

[**AppDomain**](AppDomain.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | App Domain object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

