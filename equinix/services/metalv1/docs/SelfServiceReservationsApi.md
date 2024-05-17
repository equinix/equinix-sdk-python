# equinix_metal.SelfServiceReservationsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_self_service_reservation**](SelfServiceReservationsApi.md#create_self_service_reservation) | **POST** /projects/{project_id}/self-service/reservations | Create a reservation
[**find_self_service_reservation**](SelfServiceReservationsApi.md#find_self_service_reservation) | **GET** /projects/{project_id}/self-service/reservations/{id} | Retrieve a reservation
[**find_self_service_reservations**](SelfServiceReservationsApi.md#find_self_service_reservations) | **GET** /projects/{project_id}/self-service/reservations | Retrieve all reservations


# **create_self_service_reservation**
> SelfServiceReservationResponse create_self_service_reservation(project_id, create_self_service_reservation_request)

Create a reservation

Creates a reservation.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.create_self_service_reservation_request import CreateSelfServiceReservationRequest
from equinix_metal.models.self_service_reservation_response import SelfServiceReservationResponse
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
    api_instance = equinix_metal.SelfServiceReservationsApi(api_client)
    project_id = 'project_id_example' # str | Project UUID
    create_self_service_reservation_request = equinix_metal.CreateSelfServiceReservationRequest() # CreateSelfServiceReservationRequest | reservation to create

    try:
        # Create a reservation
        api_response = api_instance.create_self_service_reservation(project_id, create_self_service_reservation_request)
        print("The response of SelfServiceReservationsApi->create_self_service_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfServiceReservationsApi->create_self_service_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project UUID | 
 **create_self_service_reservation_request** | [**CreateSelfServiceReservationRequest**](CreateSelfServiceReservationRequest.md)| reservation to create | 

### Return type

[**SelfServiceReservationResponse**](SelfServiceReservationResponse.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**401** | unauthorized |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_self_service_reservation**
> SelfServiceReservationResponse find_self_service_reservation(id, project_id)

Retrieve a reservation

Returns a reservation

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.self_service_reservation_response import SelfServiceReservationResponse
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
    api_instance = equinix_metal.SelfServiceReservationsApi(api_client)
    id = 'id_example' # str | Reservation short_id
    project_id = 'project_id_example' # str | Project UUID

    try:
        # Retrieve a reservation
        api_response = api_instance.find_self_service_reservation(id, project_id)
        print("The response of SelfServiceReservationsApi->find_self_service_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfServiceReservationsApi->find_self_service_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Reservation short_id | 
 **project_id** | **str**| Project UUID | 

### Return type

[**SelfServiceReservationResponse**](SelfServiceReservationResponse.md)

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
# **find_self_service_reservations**
> SelfServiceReservationList find_self_service_reservations(project_id, page=page, per_page=per_page, categories=categories)

Retrieve all reservations

Returns all reservations.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.self_service_reservation_list import SelfServiceReservationList
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
    api_instance = equinix_metal.SelfServiceReservationsApi(api_client)
    project_id = 'project_id_example' # str | Project UUID
    page = 1 # int | Page to return (optional) (default to 1)
    per_page = 10 # int | Items returned per page (optional) (default to 10)
    categories = ['categories_example'] # List[str] | Filter reservations by items category (optional)

    try:
        # Retrieve all reservations
        api_response = api_instance.find_self_service_reservations(project_id, page=page, per_page=per_page, categories=categories)
        print("The response of SelfServiceReservationsApi->find_self_service_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfServiceReservationsApi->find_self_service_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project UUID | 
 **page** | **int**| Page to return | [optional] [default to 1]
 **per_page** | **int**| Items returned per page | [optional] [default to 10]
 **categories** | [**List[str]**](str.md)| Filter reservations by items category | [optional] 

### Return type

[**SelfServiceReservationList**](SelfServiceReservationList.md)

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
