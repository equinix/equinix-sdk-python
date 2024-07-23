# equinix.services.fabricv4.MetrosApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metro_by_code**](MetrosApi.md#get_metro_by_code) | **GET** /fabric/v4/metros/{metroCode} | Get Metro by Code
[**get_metros**](MetrosApi.md#get_metros) | **GET** /fabric/v4/metros | Get all Metros


# **get_metro_by_code**
> Metro get_metro_by_code(metro_code)

Get Metro by Code

GET Metros retrieves all Equinix Fabric metros, as well as latency data between each metro location. .

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.metro import Metro
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
    api_instance = equinix.services.fabricv4.MetrosApi(api_client)
    metro_code = 'metro_code_example' # str | Metro Code

    try:
        # Get Metro by Code
        api_response = api_instance.get_metro_by_code(metro_code)
        print("The response of MetrosApi->get_metro_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetrosApi->get_metro_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metro_code** | **str**| Metro Code | 

### Return type

[**Metro**](Metro.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metros**
> MetroResponse get_metros(presence=presence, offset=offset, limit=limit)

Get all Metros

GET All Subscriber Metros with an option query parameter to return all Equinix Fabric metros in which the customer has a presence, as well as latency data for each location.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.metro_response import MetroResponse
from equinix.services.fabricv4.models.presence import Presence
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
    api_instance = equinix.services.fabricv4.MetrosApi(api_client)
    presence = equinix.services.fabricv4.Presence() # Presence | User On Boarded Metros based on Fabric resource availability (optional)
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get all Metros
        api_response = api_instance.get_metros(presence=presence, offset=offset, limit=limit)
        print("The response of MetrosApi->get_metros:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetrosApi->get_metros: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **presence** | [**Presence**](.md)| User On Boarded Metros based on Fabric resource availability | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**MetroResponse**](MetroResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

