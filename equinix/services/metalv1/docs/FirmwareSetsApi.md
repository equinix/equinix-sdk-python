# equinix_metal.FirmwareSetsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_firmware_sets**](FirmwareSetsApi.md#get_organization_firmware_sets) | **GET** /organizations/{id}/firmware-sets | Get Organization&#39;s Firmware Sets
[**get_project_firmware_sets**](FirmwareSetsApi.md#get_project_firmware_sets) | **GET** /projects/{id}/firmware-sets | Get Project&#39;s Firmware Sets


# **get_organization_firmware_sets**
> FirmwareSetListResponse get_organization_firmware_sets(id, page=page, per_page=per_page)

Get Organization's Firmware Sets

Returns all firmware sets associated with the organization.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.firmware_set_list_response import FirmwareSetListResponse
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.FirmwareSetsApi(api_client)
    id = 'id_example' # str | Organization UUID
    page = 56 # int | page number to return (optional)
    per_page = 56 # int | items returned per page. (optional)

    try:
        # Get Organization's Firmware Sets
        api_response = api_instance.get_organization_firmware_sets(id, page=page, per_page=per_page)
        print("The response of FirmwareSetsApi->get_organization_firmware_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirmwareSetsApi->get_organization_firmware_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization UUID | 
 **page** | **int**| page number to return | [optional] 
 **per_page** | **int**| items returned per page. | [optional] 

### Return type

[**FirmwareSetListResponse**](FirmwareSetListResponse.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Error responses are included with 4xx and 5xx HTTP responses from the API service. Either \&quot;error\&quot; or \&quot;errors\&quot; will be set. |  -  |
**404** | Error responses are included with 4xx and 5xx HTTP responses from the API service. Either \&quot;error\&quot; or \&quot;errors\&quot; will be set. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **get_project_firmware_sets**
> FirmwareSetListResponse get_project_firmware_sets(id, page=page, per_page=per_page)

Get Project's Firmware Sets

Returns all firmware sets associated with the project or organization.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.firmware_set_list_response import FirmwareSetListResponse
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.FirmwareSetsApi(api_client)
    id = 'id_example' # str | Project UUID
    page = 56 # int | page number to return (optional)
    per_page = 56 # int | items returned per page. (optional)

    try:
        # Get Project's Firmware Sets
        api_response = api_instance.get_project_firmware_sets(id, page=page, per_page=per_page)
        print("The response of FirmwareSetsApi->get_project_firmware_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirmwareSetsApi->get_project_firmware_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **page** | **int**| page number to return | [optional] 
 **per_page** | **int**| items returned per page. | [optional] 

### Return type

[**FirmwareSetListResponse**](FirmwareSetListResponse.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Error responses are included with 4xx and 5xx HTTP responses from the API service. Either \&quot;error\&quot; or \&quot;errors\&quot; will be set. |  -  |
**404** | Error responses are included with 4xx and 5xx HTTP responses from the API service. Either \&quot;error\&quot; or \&quot;errors\&quot; will be set. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
