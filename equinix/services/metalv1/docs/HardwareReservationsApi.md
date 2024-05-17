# equinix_metal.HardwareReservationsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_hardware_reservation**](HardwareReservationsApi.md#activate_hardware_reservation) | **POST** /hardware-reservations/{id}/activate | Activate a spare hardware reservation
[**find_hardware_reservation_by_id**](HardwareReservationsApi.md#find_hardware_reservation_by_id) | **GET** /hardware-reservations/{id} | Retrieve a hardware reservation
[**find_project_hardware_reservations**](HardwareReservationsApi.md#find_project_hardware_reservations) | **GET** /projects/{id}/hardware-reservations | Retrieve all hardware reservations for a given project
[**find_project_hardware_reservations_all_pages**](HardwareReservationsApi.md#find_project_hardware_reservations_all_pages) | **GET** /projects/{id}/hardware-reservations | Retrieve all hardware reservations for a given project, fetches all the pages
[**move_hardware_reservation**](HardwareReservationsApi.md#move_hardware_reservation) | **POST** /hardware-reservations/{id}/move | Move a hardware reservation


# **activate_hardware_reservation**
> HardwareReservation activate_hardware_reservation(id, include=include, exclude=exclude, activate_hardware_reservation_request=activate_hardware_reservation_request)

Activate a spare hardware reservation

Activate a spare hardware reservation

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.activate_hardware_reservation_request import ActivateHardwareReservationRequest
from equinix_metal.models.hardware_reservation import HardwareReservation
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
    api_instance = equinix_metal.HardwareReservationsApi(api_client)
    id = 'id_example' # str | Hardware Reservation UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
    activate_hardware_reservation_request = equinix_metal.ActivateHardwareReservationRequest() # ActivateHardwareReservationRequest | Note to attach to the reservation (optional)

    try:
        # Activate a spare hardware reservation
        api_response = api_instance.activate_hardware_reservation(id, include=include, exclude=exclude, activate_hardware_reservation_request=activate_hardware_reservation_request)
        print("The response of HardwareReservationsApi->activate_hardware_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HardwareReservationsApi->activate_hardware_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Hardware Reservation UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **activate_hardware_reservation_request** | [**ActivateHardwareReservationRequest**](ActivateHardwareReservationRequest.md)| Note to attach to the reservation | [optional] 

### Return type

[**HardwareReservation**](HardwareReservation.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ok |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_hardware_reservation_by_id**
> HardwareReservation find_hardware_reservation_by_id(id, include=include, exclude=exclude)

Retrieve a hardware reservation

Returns a single hardware reservation

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.hardware_reservation import HardwareReservation
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
    api_instance = equinix_metal.HardwareReservationsApi(api_client)
    id = 'id_example' # str | HardwareReservation UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve a hardware reservation
        api_response = api_instance.find_hardware_reservation_by_id(id, include=include, exclude=exclude)
        print("The response of HardwareReservationsApi->find_hardware_reservation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HardwareReservationsApi->find_hardware_reservation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| HardwareReservation UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**HardwareReservation**](HardwareReservation.md)

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
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_project_hardware_reservations**
> HardwareReservationList find_project_hardware_reservations(id, query=query, state=state, provisionable=provisionable, include=include, exclude=exclude, page=page, per_page=per_page)

Retrieve all hardware reservations for a given project

Provides a collection of hardware reservations for a given project.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.hardware_reservation_list import HardwareReservationList
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
    api_instance = equinix_metal.HardwareReservationsApi(api_client)
    id = 'id_example' # str | Project UUID
    query = 'query_example' # str | Search by facility code, plan name, project name, reservation short ID or device hostname (optional)
    state = 'state_example' # str | Filter by hardware reservation state (optional)
    provisionable = 'provisionable_example' # str | Filter hardware reservation that is provisionable (optional)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
    page = 1 # int | Page to return (optional) (default to 1)
    per_page = 10 # int | Items returned per page (optional) (default to 10)

    try:
        # Retrieve all hardware reservations for a given project
        api_response = api_instance.find_project_hardware_reservations(id, query=query, state=state, provisionable=provisionable, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of HardwareReservationsApi->find_project_hardware_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HardwareReservationsApi->find_project_hardware_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **query** | **str**| Search by facility code, plan name, project name, reservation short ID or device hostname | [optional] 
 **state** | **str**| Filter by hardware reservation state | [optional] 
 **provisionable** | **str**| Filter hardware reservation that is provisionable | [optional] 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **page** | **int**| Page to return | [optional] [default to 1]
 **per_page** | **int**| Items returned per page | [optional] [default to 10]

### Return type

[**HardwareReservationList**](HardwareReservationList.md)

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
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_project_hardware_reservations_all_pages**
> HardwareReservationList find_project_hardware_reservations_all_pages(id, query=query, state=state, provisionable=provisionable, include=include, exclude=exclude, per_page=per_page)
Just like [**find_project_hardware_reservations**](HardwareReservationsApi.md#find_project_hardware_reservations) but fetches resources from all pages. This method doesn't take `page` parameter. Other parameters, return type and other characteristics are the same as in [**find_project_hardware_reservations**](HardwareReservationsApi.md#find_project_hardware_reservations).
# **move_hardware_reservation**
> HardwareReservation move_hardware_reservation(id, move_hardware_reservation_request, include=include, exclude=exclude)

Move a hardware reservation

Move a hardware reservation to another project

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.hardware_reservation import HardwareReservation
from equinix_metal.models.move_hardware_reservation_request import MoveHardwareReservationRequest
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
    api_instance = equinix_metal.HardwareReservationsApi(api_client)
    id = 'id_example' # str | Hardware Reservation UUID
    move_hardware_reservation_request = equinix_metal.MoveHardwareReservationRequest() # MoveHardwareReservationRequest | Destination Project UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Move a hardware reservation
        api_response = api_instance.move_hardware_reservation(id, move_hardware_reservation_request, include=include, exclude=exclude)
        print("The response of HardwareReservationsApi->move_hardware_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HardwareReservationsApi->move_hardware_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Hardware Reservation UUID | 
 **move_hardware_reservation_request** | [**MoveHardwareReservationRequest**](MoveHardwareReservationRequest.md)| Destination Project UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**HardwareReservation**](HardwareReservation.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ok |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
