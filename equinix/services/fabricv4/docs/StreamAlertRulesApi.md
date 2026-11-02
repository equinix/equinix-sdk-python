# equinix.services.fabricv4.StreamAlertRulesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stream_alert_rules**](StreamAlertRulesApi.md#create_stream_alert_rules) | **POST** /fabric/v4/streams/{streamId}/alertRules | Create Stream Alert Rule
[**delete_stream_alert_rule_by_uuid**](StreamAlertRulesApi.md#delete_stream_alert_rule_by_uuid) | **DELETE** /fabric/v4/streams/{streamId}/alertRules/{alertRuleId} | Delete Stream Alert Rule
[**get_stream_alert_rule_by_uuid**](StreamAlertRulesApi.md#get_stream_alert_rule_by_uuid) | **GET** /fabric/v4/streams/{streamId}/alertRules/{alertRuleId} | Get Stream Alert Rule
[**get_stream_alert_rules**](StreamAlertRulesApi.md#get_stream_alert_rules) | **GET** /fabric/v4/streams/{streamId}/alertRules | Get Stream Alert Rules
[**update_stream_alert_rule_by_uuid**](StreamAlertRulesApi.md#update_stream_alert_rule_by_uuid) | **PUT** /fabric/v4/streams/{streamId}/alertRules/{alertRuleId} | Update Stream Alert Rule


# **create_stream_alert_rules**
> StreamAlertRule create_stream_alert_rules(stream_id, alert_rule_post_request)

Create Stream Alert Rule

This API provides capability to create user's Stream Alert Rules

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.alert_rule_post_request import AlertRulePostRequest
from equinix.services.fabricv4.models.stream_alert_rule import StreamAlertRule
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
    api_instance = equinix.services.fabricv4.StreamAlertRulesApi(api_client)
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID
    alert_rule_post_request = {"name":"metric-alert-1","type":"METRIC_ALERT","description":"metric-alert-1","enabled":true,"metricSelector":{"include":["equinix.fabric.connection.bandwidth_tx.usage"]},"resourceSelector":{"include":["/fabric/v4/connections/8b140c74-0331-46d1-9cb3-2981be84dd1b"]},"detectionMethod":{"type":"THRESHOLD","windowSize":"PT15M","warningThreshold":"35000000","criticalThreshold":"45000000"}} # AlertRulePostRequest | 

    try:
        # Create Stream Alert Rule
        api_response = api_instance.create_stream_alert_rules(stream_id, alert_rule_post_request)
        print("The response of StreamAlertRulesApi->create_stream_alert_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamAlertRulesApi->create_stream_alert_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream UUID | 
 **alert_rule_post_request** | [**AlertRulePostRequest**](AlertRulePostRequest.md)|  | 

### Return type

[**StreamAlertRule**](StreamAlertRule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream Alert Rules object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stream_alert_rule_by_uuid**
> StreamAlertRule delete_stream_alert_rule_by_uuid(stream_id, alert_rule_id)

Delete Stream Alert Rule

This API provides capability to delete a user's stream alert rule

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream_alert_rule import StreamAlertRule
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
    api_instance = equinix.services.fabricv4.StreamAlertRulesApi(api_client)
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID
    alert_rule_id = '0bbcea48-1333-4ad5-a7ea-e4d58a5fbd15' # str | alert rule UUID

    try:
        # Delete Stream Alert Rule
        api_response = api_instance.delete_stream_alert_rule_by_uuid(stream_id, alert_rule_id)
        print("The response of StreamAlertRulesApi->delete_stream_alert_rule_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamAlertRulesApi->delete_stream_alert_rule_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream UUID | 
 **alert_rule_id** | **str**| alert rule UUID | 

### Return type

[**StreamAlertRule**](StreamAlertRule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream Alert Rules object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_alert_rule_by_uuid**
> StreamAlertRule get_stream_alert_rule_by_uuid(stream_id, alert_rule_id)

Get Stream Alert Rule

This API provides capability to get user's stream alert rule

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.stream_alert_rule import StreamAlertRule
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
    api_instance = equinix.services.fabricv4.StreamAlertRulesApi(api_client)
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID
    alert_rule_id = '0bbcea48-1333-4ad5-a7ea-e4d58a5fbd15' # str | alert rule UUID

    try:
        # Get Stream Alert Rule
        api_response = api_instance.get_stream_alert_rule_by_uuid(stream_id, alert_rule_id)
        print("The response of StreamAlertRulesApi->get_stream_alert_rule_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamAlertRulesApi->get_stream_alert_rule_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream UUID | 
 **alert_rule_id** | **str**| alert rule UUID | 

### Return type

[**StreamAlertRule**](StreamAlertRule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream Alert Rules object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_alert_rules**
> GetAllStreamAlertRuleResponse get_stream_alert_rules(stream_id, offset=offset, limit=limit)

Get Stream Alert Rules

This API provides capability to retrieve stream alert rules

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_all_stream_alert_rule_response import GetAllStreamAlertRuleResponse
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
    api_instance = equinix.services.fabricv4.StreamAlertRulesApi(api_client)
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get Stream Alert Rules
        api_response = api_instance.get_stream_alert_rules(stream_id, offset=offset, limit=limit)
        print("The response of StreamAlertRulesApi->get_stream_alert_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamAlertRulesApi->get_stream_alert_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream UUID | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**GetAllStreamAlertRuleResponse**](GetAllStreamAlertRuleResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream Alert Rules object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stream_alert_rule_by_uuid**
> StreamAlertRule update_stream_alert_rule_by_uuid(stream_id, alert_rule_id, alert_rule_put_request)

Update Stream Alert Rule

This API provides capability to update a user's stream alert rule

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.alert_rule_put_request import AlertRulePutRequest
from equinix.services.fabricv4.models.stream_alert_rule import StreamAlertRule
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
    api_instance = equinix.services.fabricv4.StreamAlertRulesApi(api_client)
    stream_id = '657400f8-d360-11e9-bb65-2a2ae2dbcce5' # str | Stream UUID
    alert_rule_id = '0bbcea48-1333-4ad5-a7ea-e4d58a5fbd15' # str | alert rule UUID
    alert_rule_put_request = {"name":"metric-alert-1","type":"METRIC_ALERT","description":"metric-alert-1","enabled":true,"metricSelector":{"include":["equinix.fabric.connection.bandwidth_tx.usage"]},"resourceSelector":{"include":["/fabric/v4/connections/8b140c74-0331-46d1-9cb3-2981be84dd1b"]},"detectionMethod":{"type":"THRESHOLD","windowSize":"PT15M","operand":"ABOVE","warningThreshold":"35000000","criticalThreshold":"45000000"}} # AlertRulePutRequest | 

    try:
        # Update Stream Alert Rule
        api_response = api_instance.update_stream_alert_rule_by_uuid(stream_id, alert_rule_id, alert_rule_put_request)
        print("The response of StreamAlertRulesApi->update_stream_alert_rule_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamAlertRulesApi->update_stream_alert_rule_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream UUID | 
 **alert_rule_id** | **str**| alert rule UUID | 
 **alert_rule_put_request** | [**AlertRulePutRequest**](AlertRulePutRequest.md)|  | 

### Return type

[**StreamAlertRule**](StreamAlertRule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Stream Alert Rules object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

