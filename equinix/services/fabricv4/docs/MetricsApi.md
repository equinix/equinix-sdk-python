# equinix.services.fabricv4.MetricsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metric_by_asset_id**](MetricsApi.md#get_metric_by_asset_id) | **GET** /fabric/v4/{asset}/{assetId}/metrics | Get Metrics by Asset Id
[**get_metric_by_name**](MetricsApi.md#get_metric_by_name) | **GET** /fabric/v4/metrics | Get Metrics by Name
[**search_metrics**](MetricsApi.md#search_metrics) | **POST** /fabric/v4/metrics/search | Search Metrics


# **get_metric_by_asset_id**
> GetMetricsByAssetResponse get_metric_by_asset_id(asset, asset_id, name, from_date_time=from_date_time, to_date_time=to_date_time, offset=offset, limit=limit)

Get Metrics by Asset Id

This API provides capability to retrieve Metrics of an asset id

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_metrics_by_asset_response import GetMetricsByAssetResponse
from equinix.services.fabricv4.models.metric_asset_type import MetricAssetType
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
    api_instance = equinix.services.fabricv4.MetricsApi(api_client)
    asset = equinix.services.fabricv4.MetricAssetType() # MetricAssetType | asset
    asset_id = 'asset_id_example' # str | asset UUID
    name = 'equinix.fabric.connection.bandwidth_rx.usage' # str | Name of the metric types:  - `equinix.fabric.connection.bandwidth_rx.usage` - `equinix.fabric.connection.bandwidth_tx.usage` - `equinix.fabric.connection.packets_dropped_rx_aside_rateexceeded.count` - `equinix.fabric.connection.packets_dropped_tx_aside_rateexceeded.count` - `equinix.fabric.connection.packets_dropped_rx_zside_rateexceeded.count` - `equinix.fabric.connection.packets_dropped_tx_zside_rateexceeded.count` - `equinix.fabric.port.bandwidth_rx.usage` - `equinix.fabric.port.bandwidth_tx.usage` - `equinix.fabric.port.packets_dropped_rx.count` - `equinix.fabric.port.packets_dropped_tx.count` - `equinix.fabric.port.packets_erred_rx.count` - `equinix.fabric.port.packets_erred_tx.count` - `equinix.fabric.metro.{SOURCE_METRO_CODE}_{DESTINATION_METRO_CODE}.latency` - `equinix.fabric.metro.{SOURCE_METRO_CODE}_{DESTINATION_METRO_CODE}.jitter_avg` 
    from_date_time = '2013-10-20T19:20:30+01:00' # datetime | Start date and time (optional)
    to_date_time = '2013-10-20T19:20:30+01:00' # datetime | End date and time (optional)
    offset = 0 # int | offset (optional) (default to 0)
    limit = 20 # int | limit (optional) (default to 20)

    try:
        # Get Metrics by Asset Id
        api_response = api_instance.get_metric_by_asset_id(asset, asset_id, name, from_date_time=from_date_time, to_date_time=to_date_time, offset=offset, limit=limit)
        print("The response of MetricsApi->get_metric_by_asset_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_metric_by_asset_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**MetricAssetType**](.md)| asset | 
 **asset_id** | **str**| asset UUID | 
 **name** | **str**| Name of the metric types:  - &#x60;equinix.fabric.connection.bandwidth_rx.usage&#x60; - &#x60;equinix.fabric.connection.bandwidth_tx.usage&#x60; - &#x60;equinix.fabric.connection.packets_dropped_rx_aside_rateexceeded.count&#x60; - &#x60;equinix.fabric.connection.packets_dropped_tx_aside_rateexceeded.count&#x60; - &#x60;equinix.fabric.connection.packets_dropped_rx_zside_rateexceeded.count&#x60; - &#x60;equinix.fabric.connection.packets_dropped_tx_zside_rateexceeded.count&#x60; - &#x60;equinix.fabric.port.bandwidth_rx.usage&#x60; - &#x60;equinix.fabric.port.bandwidth_tx.usage&#x60; - &#x60;equinix.fabric.port.packets_dropped_rx.count&#x60; - &#x60;equinix.fabric.port.packets_dropped_tx.count&#x60; - &#x60;equinix.fabric.port.packets_erred_rx.count&#x60; - &#x60;equinix.fabric.port.packets_erred_tx.count&#x60; - &#x60;equinix.fabric.metro.{SOURCE_METRO_CODE}_{DESTINATION_METRO_CODE}.latency&#x60; - &#x60;equinix.fabric.metro.{SOURCE_METRO_CODE}_{DESTINATION_METRO_CODE}.jitter_avg&#x60;  | 
 **from_date_time** | **datetime**| Start date and time | [optional] 
 **to_date_time** | **datetime**| End date and time | [optional] 
 **offset** | **int**| offset | [optional] [default to 0]
 **limit** | **int**| limit | [optional] [default to 20]

### Return type

[**GetMetricsByAssetResponse**](GetMetricsByAssetResponse.md)

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

# **get_metric_by_name**
> GetMetricsByNameResponse get_metric_by_name(name, value, offset=offset, limit=limit)

Get Metrics by Name

This API provides capability to retrieve Metrics by specific wildcard metric types

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_metrics_by_name_response import GetMetricsByNameResponse
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
    api_instance = equinix.services.fabricv4.MetricsApi(api_client)
    name = 'equinix.fabric.metro.*.latency' # str | Name of the metric types with wildcard:  - `equinix.fabric.metro.*.latency` - `equinix.fabric.metro.*.jitter_avg` 
    value = 'value_example' # str | value
    offset = 0 # int | offset (optional) (default to 0)
    limit = 20 # int | limit (optional) (default to 20)

    try:
        # Get Metrics by Name
        api_response = api_instance.get_metric_by_name(name, value, offset=offset, limit=limit)
        print("The response of MetricsApi->get_metric_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_metric_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the metric types with wildcard:  - &#x60;equinix.fabric.metro.*.latency&#x60; - &#x60;equinix.fabric.metro.*.jitter_avg&#x60;  | 
 **value** | **str**| value | 
 **offset** | **int**| offset | [optional] [default to 0]
 **limit** | **int**| limit | [optional] [default to 20]

### Return type

[**GetMetricsByNameResponse**](GetMetricsByNameResponse.md)

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

# **search_metrics**
> GetMetricsByAssetResponse search_metrics(metrics_search_request)

Search Metrics

This API provides capability to search metrics from a filtered query

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_metrics_by_asset_response import GetMetricsByAssetResponse
from equinix.services.fabricv4.models.metrics_search_request import MetricsSearchRequest
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
    api_instance = equinix.services.fabricv4.MetricsApi(api_client)
    metrics_search_request = equinix.services.fabricv4.MetricsSearchRequest() # MetricsSearchRequest | 

    try:
        # Search Metrics
        api_response = api_instance.search_metrics(metrics_search_request)
        print("The response of MetricsApi->search_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->search_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics_search_request** | [**MetricsSearchRequest**](MetricsSearchRequest.md)|  | 

### Return type

[**GetMetricsByAssetResponse**](GetMetricsByAssetResponse.md)

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

