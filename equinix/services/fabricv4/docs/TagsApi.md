# equinix.services.fabricv4.TagsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagsApi.md#create_tag) | **POST** /fabric/v4/tags | Create Tag
[**list_tags**](TagsApi.md#list_tags) | **GET** /fabric/v4/tags | List Tags


# **create_tag**
> TagResponse create_tag(tag_request)

Create Tag

Create Tag for Equinix Fabric?.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.tag_request import TagRequest
from equinix.services.fabricv4.models.tag_response import TagResponse
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
    api_instance = equinix.services.fabricv4.TagsApi(api_client)
    tag_request = equinix.services.fabricv4.TagRequest() # TagRequest | 

    try:
        # Create Tag
        api_response = api_instance.create_tag(tag_request)
        print("The response of TagsApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_request** | [**TagRequest**](TagRequest.md)|  | 

### Return type

[**TagResponse**](TagResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Create operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> TagListResponse list_tags(type=type, offset=offset, limit=limit)

List Tags

Get all Tags

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.tag_list_response import TagListResponse
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
    api_instance = equinix.services.fabricv4.TagsApi(api_client)
    type = ['type_example'] # List[str] | Filter by tag type (optional)
    offset = 0 # int | Offset for pagination (optional) (default to 0)
    limit = 20 # int | Limit for pagination (optional) (default to 20)

    try:
        # List Tags
        api_response = api_instance.list_tags(type=type, offset=offset, limit=limit)
        print("The response of TagsApi->list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->list_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**List[str]**](str.md)| Filter by tag type | [optional] 
 **offset** | **int**| Offset for pagination | [optional] [default to 0]
 **limit** | **int**| Limit for pagination | [optional] [default to 20]

### Return type

[**TagListResponse**](TagListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful List operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

