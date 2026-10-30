# equinix.services.fabricv4.CrossConnectsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cross_connect**](CrossConnectsApi.md#create_cross_connect) | **POST** /fabric/v4/crossConnects | Create Cross Connect
[**create_diverse_cross_connect**](CrossConnectsApi.md#create_diverse_cross_connect) | **POST** /fabric/v4/crossConnects/bulk | Create Diverse Cross Connect
[**get_cross_connect_action_by_uuid**](CrossConnectsApi.md#get_cross_connect_action_by_uuid) | **GET** /fabric/v4/crossConnects/{crossConnectId}/actions/{actionId} | Get Cross Connect Action by Action ID
[**get_cross_connect_attachments_by_uuid**](CrossConnectsApi.md#get_cross_connect_attachments_by_uuid) | **GET** /fabric/v4/crossConnects/{crossConnectId}/attachments | Get Cross Connect Attachments
[**get_cross_connect_by_uuid**](CrossConnectsApi.md#get_cross_connect_by_uuid) | **GET** /fabric/v4/crossConnects/{crossConnectId} | Get Cross Connect
[**get_cross_connect_notes_by_uuid**](CrossConnectsApi.md#get_cross_connect_notes_by_uuid) | **GET** /fabric/v4/crossConnects/{crossConnectId}/notes | Get Cross Connect Notes
[**get_cross_connect_schedules_by_uuid**](CrossConnectsApi.md#get_cross_connect_schedules_by_uuid) | **GET** /fabric/v4/crossConnects/{crossConnectId}/schedules | Get Cross Connect Schedules
[**get_cross_connect_services_by_uuid**](CrossConnectsApi.md#get_cross_connect_services_by_uuid) | **GET** /fabric/v4/crossConnects/{crossConnectId}/services | Get Cross Connect Services
[**perform_cross_connect_action**](CrossConnectsApi.md#perform_cross_connect_action) | **POST** /fabric/v4/crossConnects/{crossConnectId}/actions | Cross Connect Actions
[**search_cross_connect_action**](CrossConnectsApi.md#search_cross_connect_action) | **POST** /fabric/v4/crossConnects/{crossConnectId}/actions/search | Search Cross Connect Actions
[**search_cross_connect_schedules**](CrossConnectsApi.md#search_cross_connect_schedules) | **POST** /fabric/v4/crossConnectSchedules/search | Search Cross Connect Schedules
[**search_cross_connects**](CrossConnectsApi.md#search_cross_connects) | **POST** /fabric/v4/crossConnects/search | Search Cross Connects


# **create_cross_connect**
> CrossConnectResponse create_cross_connect(create_cross_connect)

Create Cross Connect

The API provides capability to create a new Cross Connect.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.create_cross_connect import CreateCrossConnect
from equinix.services.fabricv4.models.cross_connect_response import CrossConnectResponse
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
    api_instance = equinix.services.fabricv4.CrossConnectsApi(api_client)
    create_cross_connect = {"type":"XC","name":"My-CC-service","aSide":{"demarcationPoint":{"patchPanelId":"CP:Demarc:1259684","patchPanelPortA":35,"patchPanelPortB":32,"connectorType":"SC"}},"zSide":{"demarcationPoint":{"patchPanelId":"CP:Demarc:1259684","patchPanelPortA":12,"patchPanelPortB":24,"connectorType":"SC"}},"schedule":{"code":"STANDARD","requestedDateTime":"2026-02-27T07:21:39Z"}} # CreateCrossConnect | 

    try:
        # Create Cross Connect
        api_response = api_instance.create_cross_connect(create_cross_connect)
        print("The response of CrossConnectsApi->create_cross_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrossConnectsApi->create_cross_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cross_connect** | [**CreateCrossConnect**](CreateCrossConnect.md)|  | 

### Return type

[**CrossConnectResponse**](CrossConnectResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Operation not allowed. |  -  |
**404** | Not found. |  -  |
**500** | Internal Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_diverse_cross_connect**
> CrossConnectDiverse create_diverse_cross_connect(diverse_cross_connect_request)

Create Diverse Cross Connect

The API provides capability to create several Cross Connects in a single order - a diverse pair where the PRIMARY and the SECONDARY Cross Connect are placed at the same time, or multiple Cross Connects by sending one entry per Cross Connect.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cross_connect_diverse import CrossConnectDiverse
from equinix.services.fabricv4.models.diverse_cross_connect_request import DiverseCrossConnectRequest
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
    api_instance = equinix.services.fabricv4.CrossConnectsApi(api_client)
    diverse_cross_connect_request = {"data":[{"type":"XC","name":"My-CC-service-PRI","redundancy":{"priority":"PRIMARY"},"aSide":{"demarcationPoint":{"patchPanelId":"CP:Demarc:1259684","patchPanelPortA":35,"patchPanelPortB":32,"connectorType":"SC"}},"zSide":{"demarcationPoint":{"patchPanelId":"CP:Demarc:1259684","patchPanelPortA":12,"patchPanelPortB":24,"connectorType":"SC"}},"schedule":{"code":"STANDARD","requestedDateTime":"2026-02-27T07:21:39Z"},"notifications":[{"type":"TECHNICAL","emails":["abc@test.com"],"phone":[{"type":"MOBILE","number":"+14085551234","contactPreference":{"timezone":"PST","availability":"ANYTIME"}}]}],"order":{"customerReferenceId":"12345"}},{"type":"XC","name":"My-CC-service-SEC","redundancy":{"priority":"SECONDARY"},"aSide":{"demarcationPoint":{"patchPanelId":"PP:Demarc:1260379","patchPanelPortA":14,"patchPanelPortB":15,"connectorType":"SC"}},"zSide":{"demarcationPoint":{"patchPanelId":"PP:Demarc:1260379","patchPanelPortA":22,"patchPanelPortB":23,"connectorType":"SC"}},"schedule":{"code":"STANDARD","requestedDateTime":"2026-02-27T07:21:39Z"},"notifications":[{"type":"TECHNICAL","emails":["abc@test.com"],"phone":[{"type":"MOBILE","number":"+14085551234","contactPreference":{"timezone":"PST","availability":"ANYTIME"}}]}],"order":{"customerReferenceId":"12345"}}]} # DiverseCrossConnectRequest | 

    try:
        # Create Diverse Cross Connect
        api_response = api_instance.create_diverse_cross_connect(diverse_cross_connect_request)
        print("The response of CrossConnectsApi->create_diverse_cross_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrossConnectsApi->create_diverse_cross_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diverse_cross_connect_request** | [**DiverseCrossConnectRequest**](DiverseCrossConnectRequest.md)|  | 

### Return type

[**CrossConnectDiverse**](CrossConnectDiverse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Operation not allowed. |  -  |
**404** | Not found. |  -  |
**500** | Internal Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cross_connect_action_by_uuid**
> CrossConnectActionResponse get_cross_connect_action_by_uuid(cross_connect_id, action_id)

Get Cross Connect Action by Action ID

The API provides capability to fetch Cross Connect action details by Action ID.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cross_connect_action_response import CrossConnectActionResponse
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
    api_instance = equinix.services.fabricv4.CrossConnectsApi(api_client)
    cross_connect_id = '46bb1a31-c28f-4197-8b10-06e0e03d0743' # str | Cross Connect UUID.
    action_id = '30cc7878-54e3-4e1a-8651-87a61354bad4' # str | Cross Connect Action UUID.

    try:
        # Get Cross Connect Action by Action ID
        api_response = api_instance.get_cross_connect_action_by_uuid(cross_connect_id, action_id)
        print("The response of CrossConnectsApi->get_cross_connect_action_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrossConnectsApi->get_cross_connect_action_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_connect_id** | **str**| Cross Connect UUID. | 
 **action_id** | **str**| Cross Connect Action UUID. | 

### Return type

[**CrossConnectActionResponse**](CrossConnectActionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Operation not allowed. |  -  |
**404** | Not found. |  -  |
**500** | Internal Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cross_connect_attachments_by_uuid**
> CrossConnectAttachmentsResponse get_cross_connect_attachments_by_uuid(cross_connect_id)

Get Cross Connect Attachments

The API provides capability to get the documents attached to a Cross Connect by Cross Connect ID.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cross_connect_attachments_response import CrossConnectAttachmentsResponse
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
    api_instance = equinix.services.fabricv4.CrossConnectsApi(api_client)
    cross_connect_id = '46bb1a31-c28f-4197-8b10-06e0e03d0743' # str | Cross Connect UUID.

    try:
        # Get Cross Connect Attachments
        api_response = api_instance.get_cross_connect_attachments_by_uuid(cross_connect_id)
        print("The response of CrossConnectsApi->get_cross_connect_attachments_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrossConnectsApi->get_cross_connect_attachments_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_connect_id** | **str**| Cross Connect UUID. | 

### Return type

[**CrossConnectAttachmentsResponse**](CrossConnectAttachmentsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Operation not allowed. |  -  |
**404** | Not found. |  -  |
**500** | Internal Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cross_connect_by_uuid**
> CrossConnectResponse get_cross_connect_by_uuid(cross_connect_id)

Get Cross Connect

The API provides capability to get Cross Connect details by Cross Connect ID.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cross_connect_response import CrossConnectResponse
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
    api_instance = equinix.services.fabricv4.CrossConnectsApi(api_client)
    cross_connect_id = '46bb1a31-c28f-4197-8b10-06e0e03d0743' # str | Cross Connect UUID.

    try:
        # Get Cross Connect
        api_response = api_instance.get_cross_connect_by_uuid(cross_connect_id)
        print("The response of CrossConnectsApi->get_cross_connect_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrossConnectsApi->get_cross_connect_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_connect_id** | **str**| Cross Connect UUID. | 

### Return type

[**CrossConnectResponse**](CrossConnectResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Operation not allowed. |  -  |
**404** | Not found. |  -  |
**500** | Internal Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cross_connect_notes_by_uuid**
> CrossConnectNotesResponse get_cross_connect_notes_by_uuid(cross_connect_id, offset=offset, limit=limit)

Get Cross Connect Notes

The API provides capability to get the notes added to a Cross Connect by Cross Connect ID.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cross_connect_notes_response import CrossConnectNotesResponse
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
    api_instance = equinix.services.fabricv4.CrossConnectsApi(api_client)
    cross_connect_id = '46bb1a31-c28f-4197-8b10-06e0e03d0743' # str | Cross Connect UUID.
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get Cross Connect Notes
        api_response = api_instance.get_cross_connect_notes_by_uuid(cross_connect_id, offset=offset, limit=limit)
        print("The response of CrossConnectsApi->get_cross_connect_notes_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrossConnectsApi->get_cross_connect_notes_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_connect_id** | **str**| Cross Connect UUID. | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**CrossConnectNotesResponse**](CrossConnectNotesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Operation not allowed. |  -  |
**404** | Not found. |  -  |
**500** | Internal Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cross_connect_schedules_by_uuid**
> SchedulesResponse get_cross_connect_schedules_by_uuid(cross_connect_id)

Get Cross Connect Schedules

The API provides capability to get the schedules of a Cross Connect by Cross Connect ID.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.schedules_response import SchedulesResponse
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
    api_instance = equinix.services.fabricv4.CrossConnectsApi(api_client)
    cross_connect_id = '46bb1a31-c28f-4197-8b10-06e0e03d0743' # str | Cross Connect UUID.

    try:
        # Get Cross Connect Schedules
        api_response = api_instance.get_cross_connect_schedules_by_uuid(cross_connect_id)
        print("The response of CrossConnectsApi->get_cross_connect_schedules_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrossConnectsApi->get_cross_connect_schedules_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_connect_id** | **str**| Cross Connect UUID. | 

### Return type

[**SchedulesResponse**](SchedulesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Operation not allowed. |  -  |
**404** | Not found. |  -  |
**500** | Internal Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cross_connect_services_by_uuid**
> CrossConnectServicesResponse get_cross_connect_services_by_uuid(cross_connect_id)

Get Cross Connect Services

The API provides capability to get the services ordered alongside a Cross Connect by Cross Connect ID.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cross_connect_services_response import CrossConnectServicesResponse
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
    api_instance = equinix.services.fabricv4.CrossConnectsApi(api_client)
    cross_connect_id = '46bb1a31-c28f-4197-8b10-06e0e03d0743' # str | Cross Connect UUID.

    try:
        # Get Cross Connect Services
        api_response = api_instance.get_cross_connect_services_by_uuid(cross_connect_id)
        print("The response of CrossConnectsApi->get_cross_connect_services_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrossConnectsApi->get_cross_connect_services_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_connect_id** | **str**| Cross Connect UUID. | 

### Return type

[**CrossConnectServicesResponse**](CrossConnectServicesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Operation not allowed. |  -  |
**404** | Not found. |  -  |
**500** | Internal Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_cross_connect_action**
> CrossConnectActionResponse perform_cross_connect_action(cross_connect_id, cross_connect_action_request)

Cross Connect Actions

The API provides capability to perform an action on a Cross Connect that is in the PENDING_ACTION state. The applicable action types are listed in the allowedActions of the Cross Connect.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cross_connect_action_request import CrossConnectActionRequest
from equinix.services.fabricv4.models.cross_connect_action_response import CrossConnectActionResponse
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
    api_instance = equinix.services.fabricv4.CrossConnectsApi(api_client)
    cross_connect_id = '46bb1a31-c28f-4197-8b10-06e0e03d0743' # str | Cross Connect UUID.
    cross_connect_action_request = {"type":"XC_SIGNATURE_SUBMISSION"} # CrossConnectActionRequest | 

    try:
        # Cross Connect Actions
        api_response = api_instance.perform_cross_connect_action(cross_connect_id, cross_connect_action_request)
        print("The response of CrossConnectsApi->perform_cross_connect_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrossConnectsApi->perform_cross_connect_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_connect_id** | **str**| Cross Connect UUID. | 
 **cross_connect_action_request** | [**CrossConnectActionRequest**](CrossConnectActionRequest.md)|  | 

### Return type

[**CrossConnectActionResponse**](CrossConnectActionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Operation not allowed. |  -  |
**404** | Not found. |  -  |
**500** | Internal Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_cross_connect_action**
> CrossConnectActionSearchResponse search_cross_connect_action(cross_connect_id, cross_connect_action_search_request)

Search Cross Connect Actions

The API provides capability to get list of Cross Connect Actions using search criteria, including optional filtering, pagination and sorting.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cross_connect_action_search_request import CrossConnectActionSearchRequest
from equinix.services.fabricv4.models.cross_connect_action_search_response import CrossConnectActionSearchResponse
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
    api_instance = equinix.services.fabricv4.CrossConnectsApi(api_client)
    cross_connect_id = '46bb1a31-c28f-4197-8b10-06e0e03d0743' # str | Cross Connect UUID.
    cross_connect_action_search_request = {"filter":{"and":[{"property":"/type","operator":"=","values":["XC_INFORMATION_UPDATE"]}]},"pagination":{"limit":25,"offset":0},"sort":[{"property":"/changeLog/createdDateTime","direction":"DESC"}]} # CrossConnectActionSearchRequest | 

    try:
        # Search Cross Connect Actions
        api_response = api_instance.search_cross_connect_action(cross_connect_id, cross_connect_action_search_request)
        print("The response of CrossConnectsApi->search_cross_connect_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrossConnectsApi->search_cross_connect_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_connect_id** | **str**| Cross Connect UUID. | 
 **cross_connect_action_search_request** | [**CrossConnectActionSearchRequest**](CrossConnectActionSearchRequest.md)|  | 

### Return type

[**CrossConnectActionSearchResponse**](CrossConnectActionSearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Operation not allowed. |  -  |
**404** | Not found. |  -  |
**500** | Internal Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_cross_connect_schedules**
> SearchSchedulesResponse search_cross_connect_schedules(cross_connect_schedule_search_request)

Search Cross Connect Schedules

The API provides capability to search the Cross Connect schedule windows offered at an IBX, including optional filtering, pagination and sorting.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cross_connect_schedule_search_request import CrossConnectScheduleSearchRequest
from equinix.services.fabricv4.models.search_schedules_response import SearchSchedulesResponse
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
    api_instance = equinix.services.fabricv4.CrossConnectsApi(api_client)
    cross_connect_schedule_search_request = {"filter":{"and":[{"property":"/type","operator":"=","values":["XC_INSTALL_SCHEDULE"]},{"property":"/code","operator":"IN","values":["EXPEDITE","FLEXIBLE","STANDARD"]},{"property":"/aSide/location/ibxCode","operator":"=","values":["SV11"]},{"property":"/zSide/location/ibxCode","operator":"=","values":["SV11"]}]},"pagination":{"offset":0,"limit":20},"sort":[{"direction":"DESC","property":"/startDateTime"}]} # CrossConnectScheduleSearchRequest | 

    try:
        # Search Cross Connect Schedules
        api_response = api_instance.search_cross_connect_schedules(cross_connect_schedule_search_request)
        print("The response of CrossConnectsApi->search_cross_connect_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrossConnectsApi->search_cross_connect_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_connect_schedule_search_request** | [**CrossConnectScheduleSearchRequest**](CrossConnectScheduleSearchRequest.md)|  | 

### Return type

[**SearchSchedulesResponse**](SearchSchedulesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Operation not allowed. |  -  |
**404** | Not found. |  -  |
**500** | Internal Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_cross_connects**
> CrossConnectSearchResponse search_cross_connects(cross_connect_search_request)

Search Cross Connects

The API provides capability to get list of user's Cross Connects using search criteria, including optional filtering, pagination and sorting.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cross_connect_search_request import CrossConnectSearchRequest
from equinix.services.fabricv4.models.cross_connect_search_response import CrossConnectSearchResponse
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
    api_instance = equinix.services.fabricv4.CrossConnectsApi(api_client)
    cross_connect_search_request = {"filter":{"and":[{"property":"/name","operator":"LIKE","values":["My-CC-service"]},{"property":"/state","operator":"IN","values":["PENDING","PENDING_ACTION"]}]},"pagination":{"limit":25,"offset":0},"sort":[{"property":"/changeLog/updatedDateTime","direction":"DESC"}]} # CrossConnectSearchRequest | 

    try:
        # Search Cross Connects
        api_response = api_instance.search_cross_connects(cross_connect_search_request)
        print("The response of CrossConnectsApi->search_cross_connects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrossConnectsApi->search_cross_connects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_connect_search_request** | [**CrossConnectSearchRequest**](CrossConnectSearchRequest.md)|  | 

### Return type

[**CrossConnectSearchResponse**](CrossConnectSearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Operation not allowed. |  -  |
**404** | Not found. |  -  |
**500** | Internal Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

