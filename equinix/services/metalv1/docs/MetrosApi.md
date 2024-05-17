# equinix_metal.MetrosApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_metros**](MetrosApi.md#find_metros) | **GET** /locations/metros | Retrieve all metros
[**get_metro**](MetrosApi.md#get_metro) | **GET** /locations/metros/{id} | Retrieve a specific Metro&#39;s details


# **find_metros**
> MetroList find_metros()

Retrieve all metros

Provides a listing of available metros

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.metro_list import MetroList
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
    api_instance = equinix_metal.MetrosApi(api_client)

    try:
        # Retrieve all metros
        api_response = api_instance.find_metros()
        print("The response of MetrosApi->find_metros:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetrosApi->find_metros: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MetroList**](MetroList.md)

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
# **get_metro**
> Metro get_metro(id)

Retrieve a specific Metro's details

Show the details for a metro, including name, code, and country.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.metro import Metro
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
    api_instance = equinix_metal.MetrosApi(api_client)
    id = 'id_example' # str | Metro UUID

    try:
        # Retrieve a specific Metro's details
        api_response = api_instance.get_metro(id)
        print("The response of MetrosApi->get_metro:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetrosApi->get_metro: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Metro UUID | 

### Return type

[**Metro**](Metro.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
