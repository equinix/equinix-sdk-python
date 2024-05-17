# equinix_metal.OperatingSystemsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_operating_system_version**](OperatingSystemsApi.md#find_operating_system_version) | **GET** /operating-system-versions | Retrieve all operating system versions
[**find_operating_systems**](OperatingSystemsApi.md#find_operating_systems) | **GET** /operating-systems | Retrieve all operating systems


# **find_operating_system_version**
> OperatingSystemList find_operating_system_version()

Retrieve all operating system versions

Provides a listing of available operating system versions.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.operating_system_list import OperatingSystemList
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
    api_instance = equinix_metal.OperatingSystemsApi(api_client)

    try:
        # Retrieve all operating system versions
        api_response = api_instance.find_operating_system_version()
        print("The response of OperatingSystemsApi->find_operating_system_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatingSystemsApi->find_operating_system_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OperatingSystemList**](OperatingSystemList.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_operating_systems**
> OperatingSystemList find_operating_systems()

Retrieve all operating systems

Provides a listing of available operating systems to provision your new device with.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.operating_system_list import OperatingSystemList
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
    api_instance = equinix_metal.OperatingSystemsApi(api_client)

    try:
        # Retrieve all operating systems
        api_response = api_instance.find_operating_systems()
        print("The response of OperatingSystemsApi->find_operating_systems:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatingSystemsApi->find_operating_systems: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OperatingSystemList**](OperatingSystemList.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
