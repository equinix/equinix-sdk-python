# equinix.services.fabricv4.RouteAggregationRulesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_route_aggregation_rule**](RouteAggregationRulesApi.md#create_route_aggregation_rule) | **POST** /fabric/v4/routeAggregations/{routeAggregationId}/routeAggregationRules | Create RARule
[**create_route_aggregation_rules_in_bulk**](RouteAggregationRulesApi.md#create_route_aggregation_rules_in_bulk) | **POST** /fabric/v4/routeAggregations/{routeAggregationId}/routeAggregationRules/bulk | Bulk RARules
[**delete_route_aggregation_rule_by_uuid**](RouteAggregationRulesApi.md#delete_route_aggregation_rule_by_uuid) | **DELETE** /fabric/v4/routeAggregations/{routeAggregationId}/routeAggregationRules/{routeAggregationRuleId} | DeleteRARule
[**get_route_aggregation_rule_by_uuid**](RouteAggregationRulesApi.md#get_route_aggregation_rule_by_uuid) | **GET** /fabric/v4/routeAggregations/{routeAggregationId}/routeAggregationRules/{routeAggregationRuleId} | GetRARule By UUID
[**get_route_aggregation_rule_change_by_uuid**](RouteAggregationRulesApi.md#get_route_aggregation_rule_change_by_uuid) | **GET** /fabric/v4/routeAggregations/{routeAggregationId}/routeAggregationRules/{routeAggregationRuleId}/changes/{changeId} | Get Change By ID
[**get_route_aggregation_rule_changes**](RouteAggregationRulesApi.md#get_route_aggregation_rule_changes) | **GET** /fabric/v4/routeAggregations/{routeAggregationId}/routeAggregationRules/{routeAggregationRuleId}/changes | Get All Changes
[**get_route_aggregation_rules**](RouteAggregationRulesApi.md#get_route_aggregation_rules) | **GET** /fabric/v4/routeAggregations/{routeAggregationId}/routeAggregationRules | GetRARules
[**patch_route_aggregation_rule_by_uuid**](RouteAggregationRulesApi.md#patch_route_aggregation_rule_by_uuid) | **PATCH** /fabric/v4/routeAggregations/{routeAggregationId}/routeAggregationRules/{routeAggregationRuleId} | PatchRARule
[**replace_route_aggregation_rule_by_uuid**](RouteAggregationRulesApi.md#replace_route_aggregation_rule_by_uuid) | **PUT** /fabric/v4/routeAggregations/{routeAggregationId}/routeAggregationRules/{routeAggregationRuleId} | ReplaceRARule


# **create_route_aggregation_rule**
> RouteAggregationRulesData create_route_aggregation_rule(route_aggregation_id, route_aggregation_rules_base)

Create RARule

This API provides capability to create a Route Aggregation Rule

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregation_rules_base import RouteAggregationRulesBase
from equinix.services.fabricv4.models.route_aggregation_rules_data import RouteAggregationRulesData
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
    api_instance = equinix.services.fabricv4.RouteAggregationRulesApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    route_aggregation_rules_base = equinix.services.fabricv4.RouteAggregationRulesBase() # RouteAggregationRulesBase | 

    try:
        # Create RARule
        api_response = api_instance.create_route_aggregation_rule(route_aggregation_id, route_aggregation_rules_base)
        print("The response of RouteAggregationRulesApi->create_route_aggregation_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationRulesApi->create_route_aggregation_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **route_aggregation_rules_base** | [**RouteAggregationRulesBase**](RouteAggregationRulesBase.md)|  | 

### Return type

[**RouteAggregationRulesData**](RouteAggregationRulesData.md)

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
**404** | Route Aggregation Rule ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_route_aggregation_rules_in_bulk**
> GetRouteAggregationRulesResponse create_route_aggregation_rules_in_bulk(route_aggregation_id, route_aggregation_rules_post_request)

Bulk RARules

This API provides capability to create bulk route aggregation rules

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_route_aggregation_rules_response import GetRouteAggregationRulesResponse
from equinix.services.fabricv4.models.route_aggregation_rules_post_request import RouteAggregationRulesPostRequest
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
    api_instance = equinix.services.fabricv4.RouteAggregationRulesApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    route_aggregation_rules_post_request = equinix.services.fabricv4.RouteAggregationRulesPostRequest() # RouteAggregationRulesPostRequest | 

    try:
        # Bulk RARules
        api_response = api_instance.create_route_aggregation_rules_in_bulk(route_aggregation_id, route_aggregation_rules_post_request)
        print("The response of RouteAggregationRulesApi->create_route_aggregation_rules_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationRulesApi->create_route_aggregation_rules_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **route_aggregation_rules_post_request** | [**RouteAggregationRulesPostRequest**](RouteAggregationRulesPostRequest.md)|  | 

### Return type

[**GetRouteAggregationRulesResponse**](GetRouteAggregationRulesResponse.md)

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

# **delete_route_aggregation_rule_by_uuid**
> RouteAggregationRulesData delete_route_aggregation_rule_by_uuid(route_aggregation_id, route_aggregation_rule_id)

DeleteRARule

This API provides capability to delete a Route aggregation Rule

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregation_rules_data import RouteAggregationRulesData
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
    api_instance = equinix.services.fabricv4.RouteAggregationRulesApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    route_aggregation_rule_id = 'route_aggregation_rule_id_example' # str | Route Aggregation Rules Id

    try:
        # DeleteRARule
        api_response = api_instance.delete_route_aggregation_rule_by_uuid(route_aggregation_id, route_aggregation_rule_id)
        print("The response of RouteAggregationRulesApi->delete_route_aggregation_rule_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationRulesApi->delete_route_aggregation_rule_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **route_aggregation_rule_id** | **str**| Route Aggregation Rules Id | 

### Return type

[**RouteAggregationRulesData**](RouteAggregationRulesData.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_aggregation_rule_by_uuid**
> RouteAggregationRulesData get_route_aggregation_rule_by_uuid(route_aggregation_id, route_aggregation_rule_id)

GetRARule By UUID

This API provides capability to view a Route Aggregation Rule by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregation_rules_data import RouteAggregationRulesData
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
    api_instance = equinix.services.fabricv4.RouteAggregationRulesApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    route_aggregation_rule_id = 'route_aggregation_rule_id_example' # str | Route Aggregation Rules Id

    try:
        # GetRARule By UUID
        api_response = api_instance.get_route_aggregation_rule_by_uuid(route_aggregation_id, route_aggregation_rule_id)
        print("The response of RouteAggregationRulesApi->get_route_aggregation_rule_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationRulesApi->get_route_aggregation_rule_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **route_aggregation_rule_id** | **str**| Route Aggregation Rules Id | 

### Return type

[**RouteAggregationRulesData**](RouteAggregationRulesData.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_aggregation_rule_change_by_uuid**
> RouteAggregationRulesChangeData get_route_aggregation_rule_change_by_uuid(route_aggregation_id, route_aggregation_rule_id, change_id)

Get Change By ID

This API provides capability to retrieve a specific Route Aggregation Rule's Changes

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregation_rules_change_data import RouteAggregationRulesChangeData
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
    api_instance = equinix.services.fabricv4.RouteAggregationRulesApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    route_aggregation_rule_id = 'route_aggregation_rule_id_example' # str | Route Aggregation Rules Id
    change_id = 'change_id_example' # str | Route Aggregation Rule Change UUID

    try:
        # Get Change By ID
        api_response = api_instance.get_route_aggregation_rule_change_by_uuid(route_aggregation_id, route_aggregation_rule_id, change_id)
        print("The response of RouteAggregationRulesApi->get_route_aggregation_rule_change_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationRulesApi->get_route_aggregation_rule_change_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **route_aggregation_rule_id** | **str**| Route Aggregation Rules Id | 
 **change_id** | **str**| Route Aggregation Rule Change UUID | 

### Return type

[**RouteAggregationRulesChangeData**](RouteAggregationRulesChangeData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Route Aggregation Change object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Aggregation ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_aggregation_rule_changes**
> RouteAggregationRulesChangeDataResponse get_route_aggregation_rule_changes(route_aggregation_id, route_aggregation_rule_id, offset=offset, limit=limit)

Get All Changes

This API provides capability to retrieve all of a Route Aggregation Rule's Changes

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregation_rules_change_data_response import RouteAggregationRulesChangeDataResponse
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
    api_instance = equinix.services.fabricv4.RouteAggregationRulesApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    route_aggregation_rule_id = 'route_aggregation_rule_id_example' # str | Route Aggregation Rules Id
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get All Changes
        api_response = api_instance.get_route_aggregation_rule_changes(route_aggregation_id, route_aggregation_rule_id, offset=offset, limit=limit)
        print("The response of RouteAggregationRulesApi->get_route_aggregation_rule_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationRulesApi->get_route_aggregation_rule_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **route_aggregation_rule_id** | **str**| Route Aggregation Rules Id | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**RouteAggregationRulesChangeDataResponse**](RouteAggregationRulesChangeDataResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabric Route Aggregation Rule Change object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Route Aggregation ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_aggregation_rules**
> GetRouteAggregationRulesResponse get_route_aggregation_rules(route_aggregation_id, offset=offset, limit=limit)

GetRARules

This API provides capability to get all Route Aggregations Rules for Fabric

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_route_aggregation_rules_response import GetRouteAggregationRulesResponse
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
    api_instance = equinix.services.fabricv4.RouteAggregationRulesApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # GetRARules
        api_response = api_instance.get_route_aggregation_rules(route_aggregation_id, offset=offset, limit=limit)
        print("The response of RouteAggregationRulesApi->get_route_aggregation_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationRulesApi->get_route_aggregation_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**GetRouteAggregationRulesResponse**](GetRouteAggregationRulesResponse.md)

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
**404** | Route Aggregation Rule ID Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_route_aggregation_rule_by_uuid**
> RouteAggregationRulesData patch_route_aggregation_rule_by_uuid(route_aggregation_id, route_aggregation_rule_id, route_aggregation_rules_patch_request_item)

PatchRARule

This API provides capability to partially update a Route Aggregation Rule

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregation_rules_data import RouteAggregationRulesData
from equinix.services.fabricv4.models.route_aggregation_rules_patch_request_item import RouteAggregationRulesPatchRequestItem
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
    api_instance = equinix.services.fabricv4.RouteAggregationRulesApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    route_aggregation_rule_id = 'route_aggregation_rule_id_example' # str | Route Aggregation Rules Id
    route_aggregation_rules_patch_request_item = [equinix.services.fabricv4.RouteAggregationRulesPatchRequestItem()] # List[RouteAggregationRulesPatchRequestItem] | 

    try:
        # PatchRARule
        api_response = api_instance.patch_route_aggregation_rule_by_uuid(route_aggregation_id, route_aggregation_rule_id, route_aggregation_rules_patch_request_item)
        print("The response of RouteAggregationRulesApi->patch_route_aggregation_rule_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationRulesApi->patch_route_aggregation_rule_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **route_aggregation_rule_id** | **str**| Route Aggregation Rules Id | 
 **route_aggregation_rules_patch_request_item** | [**List[RouteAggregationRulesPatchRequestItem]**](RouteAggregationRulesPatchRequestItem.md)|  | 

### Return type

[**RouteAggregationRulesData**](RouteAggregationRulesData.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_route_aggregation_rule_by_uuid**
> RouteAggregationRulesData replace_route_aggregation_rule_by_uuid(route_aggregation_id, route_aggregation_rule_id, route_aggregation_rules_base)

ReplaceRARule

This API provides capability to replace a Route Aggregation Rule completely

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.route_aggregation_rules_base import RouteAggregationRulesBase
from equinix.services.fabricv4.models.route_aggregation_rules_data import RouteAggregationRulesData
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
    api_instance = equinix.services.fabricv4.RouteAggregationRulesApi(api_client)
    route_aggregation_id = 'route_aggregation_id_example' # str | Route Aggregations Id
    route_aggregation_rule_id = 'route_aggregation_rule_id_example' # str | Route Aggregation Rules Id
    route_aggregation_rules_base = equinix.services.fabricv4.RouteAggregationRulesBase() # RouteAggregationRulesBase | 

    try:
        # ReplaceRARule
        api_response = api_instance.replace_route_aggregation_rule_by_uuid(route_aggregation_id, route_aggregation_rule_id, route_aggregation_rules_base)
        print("The response of RouteAggregationRulesApi->replace_route_aggregation_rule_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteAggregationRulesApi->replace_route_aggregation_rule_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_aggregation_id** | **str**| Route Aggregations Id | 
 **route_aggregation_rule_id** | **str**| Route Aggregation Rules Id | 
 **route_aggregation_rules_base** | [**RouteAggregationRulesBase**](RouteAggregationRulesBase.md)|  | 

### Return type

[**RouteAggregationRulesData**](RouteAggregationRulesData.md)

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
**404** | Route Aggregation ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

