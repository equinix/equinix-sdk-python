# equinix.services.fabricv4.ApplicationProcessorsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_processor_by_uuid**](ApplicationProcessorsApi.md#get_app_processor_by_uuid) | **GET** /fabric/v4/appProcessors/{appProcessorId} | Get Processor
[**search_app_processors**](ApplicationProcessorsApi.md#search_app_processors) | **POST** /fabric/v4/appProcessors/search | Search Processors


# **get_app_processor_by_uuid**
> AppProcessor get_app_processor_by_uuid(app_processor_id)

Get Processor

This API provides capability to retrieve user's App Processor

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_processor import AppProcessor
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
    api_instance = equinix.services.fabricv4.ApplicationProcessorsApi(api_client)
    app_processor_id = '90ee425c-9988-454c-96d9-1128bc16350f' # str | App Processor UUID

    try:
        # Get Processor
        api_response = api_instance.get_app_processor_by_uuid(app_processor_id)
        print("The response of ApplicationProcessorsApi->get_app_processor_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationProcessorsApi->get_app_processor_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_processor_id** | **str**| App Processor UUID | 

### Return type

[**AppProcessor**](AppProcessor.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App Processor object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_app_processors**
> AppProcessorSearchResponse search_app_processors(app_processor_search_request)

Search Processors

The API provides capability to get list of user's App Processors using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.app_processor_search_request import AppProcessorSearchRequest
from equinix.services.fabricv4.models.app_processor_search_response import AppProcessorSearchResponse
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
    api_instance = equinix.services.fabricv4.ApplicationProcessorsApi(api_client)
    app_processor_search_request = {"filter":{"and":[{"property":"/state","operator":"=","values":["PROVISIONED"]},{"property":"/project/projectId","operator":"IN","values":["71b55fef-fd2e-402f-ae3c-01d5f00bf2d4"]}]},"pagination":{"offset":0,"limit":20},"sort":[{"direction":"DESC","property":"/changeLog/createdDateTime"}]} # AppProcessorSearchRequest | 

    try:
        # Search Processors
        api_response = api_instance.search_app_processors(app_processor_search_request)
        print("The response of ApplicationProcessorsApi->search_app_processors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationProcessorsApi->search_app_processors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_processor_search_request** | [**AppProcessorSearchRequest**](AppProcessorSearchRequest.md)|  | 

### Return type

[**AppProcessorSearchResponse**](AppProcessorSearchResponse.md)

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

