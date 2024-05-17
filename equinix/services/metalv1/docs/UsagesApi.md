# equinix_metal.UsagesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_device_usages**](UsagesApi.md#find_device_usages) | **GET** /devices/{id}/usages | Retrieve all usages for device
[**find_project_usage**](UsagesApi.md#find_project_usage) | **GET** /projects/{id}/usages | Retrieve all usages for project


# **find_device_usages**
> DeviceUsageList find_device_usages(id, created_after=created_after, created_before=created_before)

Retrieve all usages for device

Returns all usages for a device.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.device_usage_list import DeviceUsageList
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
    api_instance = equinix_metal.UsagesApi(api_client)
    id = 'id_example' # str | Device UUID
    created_after = 'created_after_example' # str | Filter usages created after this date (optional)
    created_before = 'created_before_example' # str | Filter usages created before this date (optional)

    try:
        # Retrieve all usages for device
        api_response = api_instance.find_device_usages(id, created_after=created_after, created_before=created_before)
        print("The response of UsagesApi->find_device_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsagesApi->find_device_usages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **created_after** | **str**| Filter usages created after this date | [optional] 
 **created_before** | **str**| Filter usages created before this date | [optional] 

### Return type

[**DeviceUsageList**](DeviceUsageList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_project_usage**
> ProjectUsageList find_project_usage(id, created_after=created_after, created_before=created_before)

Retrieve all usages for project

Returns all usages for a project.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.project_usage_list import ProjectUsageList
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
    api_instance = equinix_metal.UsagesApi(api_client)
    id = 'id_example' # str | Project UUID
    created_after = 'created_after_example' # str | Filter usages created after this date (optional)
    created_before = 'created_before_example' # str | Filter usages created before this date (optional)

    try:
        # Retrieve all usages for project
        api_response = api_instance.find_project_usage(id, created_after=created_after, created_before=created_before)
        print("The response of UsagesApi->find_project_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsagesApi->find_project_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **created_after** | **str**| Filter usages created after this date | [optional] 
 **created_before** | **str**| Filter usages created before this date | [optional] 

### Return type

[**ProjectUsageList**](ProjectUsageList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
