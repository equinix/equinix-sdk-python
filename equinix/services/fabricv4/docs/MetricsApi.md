# equinix.services.fabricv4.MetricsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metric_by_asset_id**](MetricsApi.md#get_metric_by_asset_id) | **GET** /fabric/v4/{asset}/{assetId}/metrics | Get Metrics by Asset Id


# **get_metric_by_asset_id**
> GetMetricsByAssetResponse get_metric_by_asset_id(asset, asset_id, from_date_time=from_date_time, to_date_time=to_date_time, offset=offset, limit=limit)

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
    from_date_time = '2013-10-20T19:20:30+01:00' # datetime | Start date and time (optional)
    to_date_time = '2013-10-20T19:20:30+01:00' # datetime | End date and time (optional)
    offset = 0 # int | offset (optional) (default to 0)
    limit = 20 # int | limit (optional) (default to 20)

    try:
        # Get Metrics by Asset Id
        api_response = api_instance.get_metric_by_asset_id(asset, asset_id, from_date_time=from_date_time, to_date_time=to_date_time, offset=offset, limit=limit)
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

