# equinix.services.fabricv4.CloudEventsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cloud_event**](CloudEventsApi.md#get_cloud_event) | **GET** /fabric/v4/cloudevents/{cloudEventId} | Get Cloud Event
[**get_cloud_event_by_asset_id**](CloudEventsApi.md#get_cloud_event_by_asset_id) | **GET** /fabric/v4/{asset}/{assetId}/cloudevents | Get Cloud Events by Asset Id
[**search_cloud_events**](CloudEventsApi.md#search_cloud_events) | **POST** /fabric/v4/cloudevents/search | Search Cloud Events


# **get_cloud_event**
> CloudEvent get_cloud_event(cloud_event_id)

Get Cloud Event

This API provides capability to retrieve a cloud event by uuid

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_event import CloudEvent
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
    api_instance = equinix.services.fabricv4.CloudEventsApi(api_client)
    cloud_event_id = 'cloud_event_id_example' # str | Cloud Event UUID

    try:
        # Get Cloud Event
        api_response = api_instance.get_cloud_event(cloud_event_id)
        print("The response of CloudEventsApi->get_cloud_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudEventsApi->get_cloud_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_event_id** | **str**| Cloud Event UUID | 

### Return type

[**CloudEvent**](CloudEvent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Event object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_event_by_asset_id**
> GetCloudEventsByAssetResponse get_cloud_event_by_asset_id(asset, asset_id, from_date_time=from_date_time, to_date_time=to_date_time, offset=offset, limit=limit)

Get Cloud Events by Asset Id

This API provides capability to retrieve cloud events of an asset id

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_event_asset_type import CloudEventAssetType
from equinix.services.fabricv4.models.get_cloud_events_by_asset_response import GetCloudEventsByAssetResponse
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
    api_instance = equinix.services.fabricv4.CloudEventsApi(api_client)
    asset = equinix.services.fabricv4.CloudEventAssetType() # CloudEventAssetType | asset
    asset_id = 'asset_id_example' # str | asset UUID
    from_date_time = '2013-10-20T19:20:30+01:00' # datetime | Start date and time (optional)
    to_date_time = '2013-10-20T19:20:30+01:00' # datetime | End date and time (optional)
    offset = 0 # int | offset (optional) (default to 0)
    limit = 20 # int | limit (optional) (default to 20)

    try:
        # Get Cloud Events by Asset Id
        api_response = api_instance.get_cloud_event_by_asset_id(asset, asset_id, from_date_time=from_date_time, to_date_time=to_date_time, offset=offset, limit=limit)
        print("The response of CloudEventsApi->get_cloud_event_by_asset_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudEventsApi->get_cloud_event_by_asset_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**CloudEventAssetType**](.md)| asset | 
 **asset_id** | **str**| asset UUID | 
 **from_date_time** | **datetime**| Start date and time | [optional] 
 **to_date_time** | **datetime**| End date and time | [optional] 
 **offset** | **int**| offset | [optional] [default to 0]
 **limit** | **int**| limit | [optional] [default to 20]

### Return type

[**GetCloudEventsByAssetResponse**](GetCloudEventsByAssetResponse.md)

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

# **search_cloud_events**
> GetCloudEventsByAssetResponse search_cloud_events(cloud_event_search_request)

Search Cloud Events

This API provides capability to search cloud events from a filtered query

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_event_search_request import CloudEventSearchRequest
from equinix.services.fabricv4.models.get_cloud_events_by_asset_response import GetCloudEventsByAssetResponse
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
    api_instance = equinix.services.fabricv4.CloudEventsApi(api_client)
    cloud_event_search_request = equinix.services.fabricv4.CloudEventSearchRequest() # CloudEventSearchRequest | 

    try:
        # Search Cloud Events
        api_response = api_instance.search_cloud_events(cloud_event_search_request)
        print("The response of CloudEventsApi->search_cloud_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudEventsApi->search_cloud_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_event_search_request** | [**CloudEventSearchRequest**](CloudEventSearchRequest.md)|  | 

### Return type

[**GetCloudEventsByAssetResponse**](GetCloudEventsByAssetResponse.md)

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

