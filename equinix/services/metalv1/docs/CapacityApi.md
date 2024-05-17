# equinix_metal.CapacityApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_capacity_for_facility**](CapacityApi.md#check_capacity_for_facility) | **POST** /capacity | Check capacity
[**check_capacity_for_metro**](CapacityApi.md#check_capacity_for_metro) | **POST** /capacity/metros | Check capacity for a metro
[**find_capacity_for_facility**](CapacityApi.md#find_capacity_for_facility) | **GET** /capacity | View capacity
[**find_capacity_for_metro**](CapacityApi.md#find_capacity_for_metro) | **GET** /capacity/metros | View capacity for metros
[**find_organization_capacity_per_facility**](CapacityApi.md#find_organization_capacity_per_facility) | **GET** /organizations/{id}/capacity | View available hardware plans per Facility for given organization
[**find_organization_capacity_per_metro**](CapacityApi.md#find_organization_capacity_per_metro) | **GET** /organizations/{id}/capacity/metros | View available hardware plans per Metro for given organization


# **check_capacity_for_facility**
> CapacityCheckPerFacilityList check_capacity_for_facility(capacity_input)

Check capacity

Validates if a deploy can be fulfilled.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.capacity_check_per_facility_list import CapacityCheckPerFacilityList
from equinix_metal.models.capacity_input import CapacityInput
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
    api_instance = equinix_metal.CapacityApi(api_client)
    capacity_input = equinix_metal.CapacityInput() # CapacityInput | Facility to check capacity in

    try:
        # Check capacity
        api_response = api_instance.check_capacity_for_facility(capacity_input)
        print("The response of CapacityApi->check_capacity_for_facility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapacityApi->check_capacity_for_facility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capacity_input** | [**CapacityInput**](CapacityInput.md)| Facility to check capacity in | 

### Return type

[**CapacityCheckPerFacilityList**](CapacityCheckPerFacilityList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **check_capacity_for_metro**
> CapacityCheckPerMetroList check_capacity_for_metro(capacity_input)

Check capacity for a metro

Validates if a deploy can be fulfilled in a metro.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.capacity_check_per_metro_list import CapacityCheckPerMetroList
from equinix_metal.models.capacity_input import CapacityInput
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
    api_instance = equinix_metal.CapacityApi(api_client)
    capacity_input = equinix_metal.CapacityInput() # CapacityInput | Metro to check capacity in

    try:
        # Check capacity for a metro
        api_response = api_instance.check_capacity_for_metro(capacity_input)
        print("The response of CapacityApi->check_capacity_for_metro:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapacityApi->check_capacity_for_metro: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capacity_input** | [**CapacityInput**](CapacityInput.md)| Metro to check capacity in | 

### Return type

[**CapacityCheckPerMetroList**](CapacityCheckPerMetroList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_capacity_for_facility**
> CapacityList find_capacity_for_facility()

View capacity

Returns a list of facilities and plans with their current capacity.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.capacity_list import CapacityList
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
    api_instance = equinix_metal.CapacityApi(api_client)

    try:
        # View capacity
        api_response = api_instance.find_capacity_for_facility()
        print("The response of CapacityApi->find_capacity_for_facility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapacityApi->find_capacity_for_facility: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CapacityList**](CapacityList.md)

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
# **find_capacity_for_metro**
> CapacityList find_capacity_for_metro()

View capacity for metros

Returns a list of metros and plans with their current capacity.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.capacity_list import CapacityList
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
    api_instance = equinix_metal.CapacityApi(api_client)

    try:
        # View capacity for metros
        api_response = api_instance.find_capacity_for_metro()
        print("The response of CapacityApi->find_capacity_for_metro:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapacityApi->find_capacity_for_metro: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CapacityList**](CapacityList.md)

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
# **find_organization_capacity_per_facility**
> CapacityList find_organization_capacity_per_facility(id)

View available hardware plans per Facility for given organization

Returns a list of facilities and plans with their current capacity.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.capacity_list import CapacityList
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
    api_instance = equinix_metal.CapacityApi(api_client)
    id = 'id_example' # str | Organization UUID

    try:
        # View available hardware plans per Facility for given organization
        api_response = api_instance.find_organization_capacity_per_facility(id)
        print("The response of CapacityApi->find_organization_capacity_per_facility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapacityApi->find_organization_capacity_per_facility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization UUID | 

### Return type

[**CapacityList**](CapacityList.md)

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
**403** | forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_organization_capacity_per_metro**
> CapacityList find_organization_capacity_per_metro(id)

View available hardware plans per Metro for given organization

Returns a list of metros and plans with their current capacity.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.capacity_list import CapacityList
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
    api_instance = equinix_metal.CapacityApi(api_client)
    id = 'id_example' # str | Organization UUID

    try:
        # View available hardware plans per Metro for given organization
        api_response = api_instance.find_organization_capacity_per_metro(id)
        print("The response of CapacityApi->find_organization_capacity_per_metro:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapacityApi->find_organization_capacity_per_metro: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization UUID | 

### Return type

[**CapacityList**](CapacityList.md)

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
**403** | forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
