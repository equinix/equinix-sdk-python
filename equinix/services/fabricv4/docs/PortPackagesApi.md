# equinix.services.fabricv4.PortPackagesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_port_packages**](PortPackagesApi.md#get_port_packages) | **GET** /fabric/v4/portPackages | Get All Port Packages


# **get_port_packages**
> AllPortPackagesResponse get_port_packages()

Get All Port Packages

Get All Port Packages returns details of all available port packages for the specified user credentials.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.all_port_packages_response import AllPortPackagesResponse
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
    api_instance = equinix.services.fabricv4.PortPackagesApi(api_client)

    try:
        # Get All Port Packages
        api_response = api_instance.get_port_packages()
        print("The response of PortPackagesApi->get_port_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortPackagesApi->get_port_packages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AllPortPackagesResponse**](AllPortPackagesResponse.md)

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
**415** | Unsupported Media Type |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

