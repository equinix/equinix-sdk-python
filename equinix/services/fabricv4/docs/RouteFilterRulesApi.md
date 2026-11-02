# equinix.services.fabricv4.RouteFilterRulesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_route_filter_rule**](RouteFilterRulesApi.md#create_route_filter_rule) | **POST** /fabric/v4/routeFilters/{routeFilterId}/routeFilterRules | Create Route Filter Rule
[**create_route_filter_rules_in_bulk**](RouteFilterRulesApi.md#create_route_filter_rules_in_bulk) | **POST** /fabric/v4/routeFilters/{routeFilterId}/routeFilterRules/bulk | Bulk Create Route Filter Rules
[**delete_route_filter_rule_by_uuid**](RouteFilterRulesApi.md#delete_route_filter_rule_by_uuid) | **DELETE** /fabric/v4/routeFilters/{routeFilterId}/routeFilterRules/{routeFilterRuleId} | Delete Route Filter Rule
[**get_route_filter_rule_by_uuid**](RouteFilterRulesApi.md#get_route_filter_rule_by_uuid) | **GET** /fabric/v4/routeFilters/{routeFilterId}/routeFilterRules/{routeFilterRuleId} | Get Route Filter Rule by ID
[**get_route_filter_rule_change_by_uuid**](RouteFilterRulesApi.md#get_route_filter_rule_change_by_uuid) | **GET** /fabric/v4/routeFilters/{routeFilterId}/routeFilterRules/{routeFilterRuleId}/changes/{changeId} | Get Change By ID
[**get_route_filter_rule_changes**](RouteFilterRulesApi.md#get_route_filter_rule_changes) | **GET** /fabric/v4/routeFilters/{routeFilterId}/routeFilterRules/{routeFilterRuleId}/changes | Get Route Filter Rule Changes
[**get_route_filter_rules**](RouteFilterRulesApi.md#get_route_filter_rules) | **GET** /fabric/v4/routeFilters/{routeFilterId}/routeFilterRules | Get Route Filter Rules
[**patch_route_filter_rule_by_uuid**](RouteFilterRulesApi.md#patch_route_filter_rule_by_uuid) | **PATCH** /fabric/v4/routeFilters/{routeFilterId}/routeFilterRules/{routeFilterRuleId} | Update Route Filter Rule
[**replace_route_filter_rule_by_uuid**](RouteFilterRulesApi.md#replace_route_filter_rule_by_uuid) | **PUT** /fabric/v4/routeFilters/{routeFilterId}/routeFilterRules/{routeFilterRuleId} | Replace Route Filter Rule
[**search_route_filter_rules**](RouteFilterRulesApi.md#search_route_filter_rules) | **POST** /fabric/v4/routeFilters/{routeFilterId}/routeFilterRules/search | Search Route Filter Rules


# **create_route_filter_rule**
> RouteFilterRulesData create_route_filter_rule(route_filter_id, route_filter_rules_base)

Create Route Filter Rule

This API provides capability to create a Route Filter Rule

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filter_rules_base import RouteFilterRulesBase
from equinix.services.fabricv4.models.route_filter_rules_data import RouteFilterRulesData
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
    api_instance = equinix.services.fabricv4.RouteFilterRulesApi(api_client)
    route_filter_id = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d' # str | Route Filters Id
    route_filter_rules_base = {"name":"Private-subnet-filter","description":"Test rule","prefix":"192.168.0.0/24","prefixMatch":"exact"} # RouteFilterRulesBase | 

    try:
        # Create Route Filter Rule
        api_response = api_instance.create_route_filter_rule(route_filter_id, route_filter_rules_base)
        print("The response of RouteFilterRulesApi->create_route_filter_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFilterRulesApi->create_route_filter_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **route_filter_rules_base** | [**RouteFilterRulesBase**](RouteFilterRulesBase.md)|  | 

### Return type

[**RouteFilterRulesData**](RouteFilterRulesData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Filter Rule ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_route_filter_rules_in_bulk**
> GetRouteFilterRulesResponse create_route_filter_rules_in_bulk(route_filter_id, route_filter_rules_post_request)

Bulk Create Route Filter Rules

This API provides capability to create bulk route filter rules

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_route_filter_rules_response import GetRouteFilterRulesResponse
from equinix.services.fabricv4.models.route_filter_rules_post_request import RouteFilterRulesPostRequest
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
    api_instance = equinix.services.fabricv4.RouteFilterRulesApi(api_client)
    route_filter_id = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d' # str | Route Filters Id
    route_filter_rules_post_request = equinix.services.fabricv4.RouteFilterRulesPostRequest() # RouteFilterRulesPostRequest | 

    try:
        # Bulk Create Route Filter Rules
        api_response = api_instance.create_route_filter_rules_in_bulk(route_filter_id, route_filter_rules_post_request)
        print("The response of RouteFilterRulesApi->create_route_filter_rules_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFilterRulesApi->create_route_filter_rules_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **route_filter_rules_post_request** | [**RouteFilterRulesPostRequest**](RouteFilterRulesPostRequest.md)|  | 

### Return type

[**GetRouteFilterRulesResponse**](GetRouteFilterRulesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Resource not found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_route_filter_rule_by_uuid**
> RouteFilterRulesData delete_route_filter_rule_by_uuid(route_filter_id, route_filter_rule_id)

Delete Route Filter Rule

This API provides capability to delete a Route Filter Rule

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filter_rules_data import RouteFilterRulesData
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
    api_instance = equinix.services.fabricv4.RouteFilterRulesApi(api_client)
    route_filter_id = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d' # str | Route Filters Id
    route_filter_rule_id = '65b025ef-022b-4180-85cf-82cfc1ab655b' # str | Route  Filter  Rules Id

    try:
        # Delete Route Filter Rule
        api_response = api_instance.delete_route_filter_rule_by_uuid(route_filter_id, route_filter_rule_id)
        print("The response of RouteFilterRulesApi->delete_route_filter_rule_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFilterRulesApi->delete_route_filter_rule_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **route_filter_rule_id** | **str**| Route  Filter  Rules Id | 

### Return type

[**RouteFilterRulesData**](RouteFilterRulesData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_filter_rule_by_uuid**
> RouteFilterRulesData get_route_filter_rule_by_uuid(route_filter_id, route_filter_rule_id)

Get Route Filter Rule by ID

This API provides capability to view a Route Filter Rule by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filter_rules_data import RouteFilterRulesData
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
    api_instance = equinix.services.fabricv4.RouteFilterRulesApi(api_client)
    route_filter_id = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d' # str | Route Filters Id
    route_filter_rule_id = '65b025ef-022b-4180-85cf-82cfc1ab655b' # str | Route  Filter  Rules Id

    try:
        # Get Route Filter Rule by ID
        api_response = api_instance.get_route_filter_rule_by_uuid(route_filter_id, route_filter_rule_id)
        print("The response of RouteFilterRulesApi->get_route_filter_rule_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFilterRulesApi->get_route_filter_rule_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **route_filter_rule_id** | **str**| Route  Filter  Rules Id | 

### Return type

[**RouteFilterRulesData**](RouteFilterRulesData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_filter_rule_change_by_uuid**
> RouteFilterRulesChangeData get_route_filter_rule_change_by_uuid(route_filter_id, route_filter_rule_id, change_id)

Get Change By ID

This API provides capability to retrieve a specific Route Filter Rule's Changes

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filter_rules_change_data import RouteFilterRulesChangeData
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
    api_instance = equinix.services.fabricv4.RouteFilterRulesApi(api_client)
    route_filter_id = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d' # str | Route Filters Id
    route_filter_rule_id = '65b025ef-022b-4180-85cf-82cfc1ab655b' # str | Route  Filter  Rules Id
    change_id = '6d500177-9404-41f2-99e8-2bf1a84d8db5' # str | Route Filter Rule Change UUID

    try:
        # Get Change By ID
        api_response = api_instance.get_route_filter_rule_change_by_uuid(route_filter_id, route_filter_rule_id, change_id)
        print("The response of RouteFilterRulesApi->get_route_filter_rule_change_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFilterRulesApi->get_route_filter_rule_change_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **route_filter_rule_id** | **str**| Route  Filter  Rules Id | 
 **change_id** | **str**| Route Filter Rule Change UUID | 

### Return type

[**RouteFilterRulesChangeData**](RouteFilterRulesChangeData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Route Filter Change object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Filter ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_filter_rule_changes**
> RouteFilterRulesChangeDataResponse get_route_filter_rule_changes(route_filter_id, route_filter_rule_id, offset=offset, limit=limit)

Get Route Filter Rule Changes

This API provides capability to retrieve all of a Route Filter Rule's Changes

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filter_rules_change_data_response import RouteFilterRulesChangeDataResponse
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
    api_instance = equinix.services.fabricv4.RouteFilterRulesApi(api_client)
    route_filter_id = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d' # str | Route Filters Id
    route_filter_rule_id = '65b025ef-022b-4180-85cf-82cfc1ab655b' # str | Route  Filter  Rules Id
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get Route Filter Rule Changes
        api_response = api_instance.get_route_filter_rule_changes(route_filter_id, route_filter_rule_id, offset=offset, limit=limit)
        print("The response of RouteFilterRulesApi->get_route_filter_rule_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFilterRulesApi->get_route_filter_rule_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **route_filter_rule_id** | **str**| Route  Filter  Rules Id | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**RouteFilterRulesChangeDataResponse**](RouteFilterRulesChangeDataResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Route Filter Rule Change object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Filter ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_filter_rules**
> GetRouteFilterRulesResponse get_route_filter_rules(route_filter_id, offset=offset, limit=limit)

Get Route Filter Rules

This API provides capability to get all Route Filters Rules for Fabric

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_route_filter_rules_response import GetRouteFilterRulesResponse
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
    api_instance = equinix.services.fabricv4.RouteFilterRulesApi(api_client)
    route_filter_id = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d' # str | Route Filters Id
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get Route Filter Rules
        api_response = api_instance.get_route_filter_rules(route_filter_id, offset=offset, limit=limit)
        print("The response of RouteFilterRulesApi->get_route_filter_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFilterRulesApi->get_route_filter_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**GetRouteFilterRulesResponse**](GetRouteFilterRulesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Resource not found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Filter Rule ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_route_filter_rule_by_uuid**
> RouteFilterRulesData patch_route_filter_rule_by_uuid(route_filter_id, route_filter_rule_id, route_filter_rules_patch_request_item)

Update Route Filter Rule

This API provides capability to partially update a Route Filter Rule

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filter_rules_data import RouteFilterRulesData
from equinix.services.fabricv4.models.route_filter_rules_patch_request_item import RouteFilterRulesPatchRequestItem
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
    api_instance = equinix.services.fabricv4.RouteFilterRulesApi(api_client)
    route_filter_id = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d' # str | Route Filters Id
    route_filter_rule_id = '65b025ef-022b-4180-85cf-82cfc1ab655b' # str | Route  Filter  Rules Id
    route_filter_rules_patch_request_item = [{"op":"replace","path":"/name","value":"test-route-filter-name-patch"}] # List[RouteFilterRulesPatchRequestItem] | 

    try:
        # Update Route Filter Rule
        api_response = api_instance.patch_route_filter_rule_by_uuid(route_filter_id, route_filter_rule_id, route_filter_rules_patch_request_item)
        print("The response of RouteFilterRulesApi->patch_route_filter_rule_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFilterRulesApi->patch_route_filter_rule_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **route_filter_rule_id** | **str**| Route  Filter  Rules Id | 
 **route_filter_rules_patch_request_item** | [**List[RouteFilterRulesPatchRequestItem]**](RouteFilterRulesPatchRequestItem.md)|  | 

### Return type

[**RouteFilterRulesData**](RouteFilterRulesData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_route_filter_rule_by_uuid**
> RouteFilterRulesData replace_route_filter_rule_by_uuid(route_filter_id, route_filter_rule_id, route_filter_rules_base)

Replace Route Filter Rule

This API provides capability to replace a Route Filter Rule completely

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filter_rules_base import RouteFilterRulesBase
from equinix.services.fabricv4.models.route_filter_rules_data import RouteFilterRulesData
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
    api_instance = equinix.services.fabricv4.RouteFilterRulesApi(api_client)
    route_filter_id = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d' # str | Route Filters Id
    route_filter_rule_id = '65b025ef-022b-4180-85cf-82cfc1ab655b' # str | Route  Filter  Rules Id
    route_filter_rules_base = {"name":"Private-subnet-filter-update","description":"Test rule","prefix":"192.168.0.0/24","prefixMatch":"exact"} # RouteFilterRulesBase | 

    try:
        # Replace Route Filter Rule
        api_response = api_instance.replace_route_filter_rule_by_uuid(route_filter_id, route_filter_rule_id, route_filter_rules_base)
        print("The response of RouteFilterRulesApi->replace_route_filter_rule_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFilterRulesApi->replace_route_filter_rule_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **route_filter_rule_id** | **str**| Route  Filter  Rules Id | 
 **route_filter_rules_base** | [**RouteFilterRulesBase**](RouteFilterRulesBase.md)|  | 

### Return type

[**RouteFilterRulesData**](RouteFilterRulesData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Filter ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_route_filter_rules**
> RouteFilterRulesSearchResponse search_route_filter_rules(route_filter_id, route_filter_rules_search_request)

Search Route Filter Rules

This API provides capability to search Route Filter Rules

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_filter_rules_search_request import RouteFilterRulesSearchRequest
from equinix.services.fabricv4.models.route_filter_rules_search_response import RouteFilterRulesSearchResponse
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
    api_instance = equinix.services.fabricv4.RouteFilterRulesApi(api_client)
    route_filter_id = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d' # str | Route Filters Id
    route_filter_rules_search_request = {"filter":{"and":[{"property":"/type","operator":"=","values":["BGP_IPv4_PREFIX_FILTER_RULE"]},{"property":"/state","operator":"=","values":["PROVISIONED"]},{"or":[{"property":"/name","operator":"LIKE","values":["%Demo%"]},{"property":"/name","operator":"LIKE","values":["%Production%"]}]},{"or":[{"property":"/state","operator":"=","values":["PROVISIONED"]},{"and":[{"property":"/prefix","operator":"=","values":["192.168.2.0/24"]},{"property":"/prefixMatch","operator":"=","values":["exact"]}]}]}]},"pagination":{"offset":0,"limit":20},"sort":[{"property":"/changeLog/updatedDateTime","direction":"DESC"}]} # RouteFilterRulesSearchRequest | 

    try:
        # Search Route Filter Rules
        api_response = api_instance.search_route_filter_rules(route_filter_id, route_filter_rules_search_request)
        print("The response of RouteFilterRulesApi->search_route_filter_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteFilterRulesApi->search_route_filter_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_filter_id** | **str**| Route Filters Id | 
 **route_filter_rules_search_request** | [**RouteFilterRulesSearchRequest**](RouteFilterRulesSearchRequest.md)|  | 

### Return type

[**RouteFilterRulesSearchResponse**](RouteFilterRulesSearchResponse.md)

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
**404** | Route Filter Rule ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

