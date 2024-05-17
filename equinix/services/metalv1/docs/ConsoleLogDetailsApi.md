# equinix_metal.ConsoleLogDetailsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capture_screenshot**](ConsoleLogDetailsApi.md#capture_screenshot) | **GET** /devices/{id}/diagnostics/screenshot | 


# **capture_screenshot**
> bytearray capture_screenshot(id)



Capture a screenshot from the device, if supported, via the BMC.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
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
    api_instance = equinix_metal.ConsoleLogDetailsApi(api_client)
    id = 'id_example' # str | Device UUID

    try:
        api_response = api_instance.capture_screenshot(id)
        print("The response of ConsoleLogDetailsApi->capture_screenshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsoleLogDetailsApi->capture_screenshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 

### Return type

**bytearray**

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jpeg, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An image file |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**501** | not implemented for device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
