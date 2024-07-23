# equinix.services.fabricv4.StatisticsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connection_stats_by_port_uuid**](StatisticsApi.md#get_connection_stats_by_port_uuid) | **GET** /fabric/v4/connections/{connectionId}/stats | Get Stats by uuid
[**get_port_stats**](StatisticsApi.md#get_port_stats) | **GET** /fabric/v4/ports/stats | Top Port Statistics
[**get_port_stats_by_port_uuid**](StatisticsApi.md#get_port_stats_by_port_uuid) | **GET** /fabric/v4/ports/{portId}/stats | Get Stats by uuid


# **get_connection_stats_by_port_uuid**
> Statistics get_connection_stats_by_port_uuid(connection_id, start_date_time, end_date_time, view_point)

Get Stats by uuid

This API provides service-level metrics so that you can view access and gather key information required to manage service subscription sizing and capacity

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.statistics import Statistics
from equinix.services.fabricv4.models.view_point import ViewPoint
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
    api_instance = equinix.services.fabricv4.StatisticsApi(api_client)
    connection_id = 'connection_id_example' # str | Connection UUID
    start_date_time = '2020-11-06T07:00:00Z' # datetime | startDateTime
    end_date_time = '2020-11-10T07:00:00Z' # datetime | endDateTime
    view_point = equinix.services.fabricv4.ViewPoint() # ViewPoint | viewPoint

    try:
        # Get Stats by uuid
        api_response = api_instance.get_connection_stats_by_port_uuid(connection_id, start_date_time, end_date_time, view_point)
        print("The response of StatisticsApi->get_connection_stats_by_port_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->get_connection_stats_by_port_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection UUID | 
 **start_date_time** | **datetime**| startDateTime | 
 **end_date_time** | **datetime**| endDateTime | 
 **view_point** | [**ViewPoint**](.md)| viewPoint | 

### Return type

[**Statistics**](Statistics.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_stats**
> TopUtilizedStatistics get_port_stats(metros, sort=sort, top=top, duration=duration, direction=direction, metric_interval=metric_interval, project_id=project_id)

Top Port Statistics

This API provides top utilized service-level traffic metrics so that you can view access and gather key information required to manage service subscription sizing and capacity.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.duration import Duration
from equinix.services.fabricv4.models.metric_interval import MetricInterval
from equinix.services.fabricv4.models.query_direction import QueryDirection
from equinix.services.fabricv4.models.sort import Sort
from equinix.services.fabricv4.models.top_utilized_statistics import TopUtilizedStatistics
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
    api_instance = equinix.services.fabricv4.StatisticsApi(api_client)
    metros = ['metros_example'] # List[str] | Two-letter prefix indicating the metropolitan area in which a specified Equinix asset is located.
    sort = equinix.services.fabricv4.Sort() # Sort | Key or set of keys that organizes the search payload by property (such as createdDate or metroCode) or by direction. Ascending (ASC) is the default value. The \"?\" prefix indicates descending (DESC) order. (optional)
    top = 5 # int | Filter returning only the specified number of most heavily trafficked ports. The standard value is [1...10], and the default is 5. (optional) (default to 5)
    duration = equinix.services.fabricv4.Duration() # Duration | duration (optional)
    direction = equinix.services.fabricv4.QueryDirection() # QueryDirection | Direction of traffic from the requester's viewpoint. The default is outbound. (optional)
    metric_interval = equinix.services.fabricv4.MetricInterval() # MetricInterval | metricInterval (optional)
    project_id = 'project_id_example' # str | projectId (optional)

    try:
        # Top Port Statistics
        api_response = api_instance.get_port_stats(metros, sort=sort, top=top, duration=duration, direction=direction, metric_interval=metric_interval, project_id=project_id)
        print("The response of StatisticsApi->get_port_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->get_port_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metros** | [**List[str]**](str.md)| Two-letter prefix indicating the metropolitan area in which a specified Equinix asset is located. | 
 **sort** | [**Sort**](.md)| Key or set of keys that organizes the search payload by property (such as createdDate or metroCode) or by direction. Ascending (ASC) is the default value. The \&quot;?\&quot; prefix indicates descending (DESC) order. | [optional] 
 **top** | **int**| Filter returning only the specified number of most heavily trafficked ports. The standard value is [1...10], and the default is 5. | [optional] [default to 5]
 **duration** | [**Duration**](.md)| duration | [optional] 
 **direction** | [**QueryDirection**](.md)| Direction of traffic from the requester&#39;s viewpoint. The default is outbound. | [optional] 
 **metric_interval** | [**MetricInterval**](.md)| metricInterval | [optional] 
 **project_id** | **str**| projectId | [optional] 

### Return type

[**TopUtilizedStatistics**](TopUtilizedStatistics.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_stats_by_port_uuid**
> Statistics get_port_stats_by_port_uuid(port_id, start_date_time, end_date_time)

Get Stats by uuid

This API provides service-level traffic metrics so that you can view access and gather key information required to manage service subscription sizing and capacity.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.statistics import Statistics
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
    api_instance = equinix.services.fabricv4.StatisticsApi(api_client)
    port_id = 'port_id_example' # str | Port UUID
    start_date_time = '2020-11-06T07:00:00Z' # datetime | startDateTime
    end_date_time = '2020-11-10T07:00:00Z' # datetime | endDateTime

    try:
        # Get Stats by uuid
        api_response = api_instance.get_port_stats_by_port_uuid(port_id, start_date_time, end_date_time)
        print("The response of StatisticsApi->get_port_stats_by_port_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->get_port_stats_by_port_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_id** | **str**| Port UUID | 
 **start_date_time** | **datetime**| startDateTime | 
 **end_date_time** | **datetime**| endDateTime | 

### Return type

[**Statistics**](Statistics.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

