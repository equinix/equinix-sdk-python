# equinix.services.fabricv4.LoasApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_loa**](LoasApi.md#create_loa) | **POST** /fabric/v4/loas | Create Loa
[**create_loa_note_by_loa_id**](LoasApi.md#create_loa_note_by_loa_id) | **POST** /fabric/v4/loas/{loaId}/notes | Create Loa Note
[**get_loa_actions_by_uuid**](LoasApi.md#get_loa_actions_by_uuid) | **GET** /fabric/v4/loas/{loaId}/actions/{actionId} | Get Loa Action by Action ID
[**get_loa_by_uuid**](LoasApi.md#get_loa_by_uuid) | **GET** /fabric/v4/loas/{loaId} | Get Loa
[**get_loa_consumers_by_loa_id**](LoasApi.md#get_loa_consumers_by_loa_id) | **GET** /fabric/v4/loas/{loaId}/consumers | Get Loa Consumers
[**get_loa_notes_by_uuid**](LoasApi.md#get_loa_notes_by_uuid) | **GET** /fabric/v4/loas/{loaId}/notes | Get Loa Notes
[**perform_loa_action**](LoasApi.md#perform_loa_action) | **POST** /fabric/v4/loas/{loaId}/actions | Loa Actions
[**search_loa**](LoasApi.md#search_loa) | **POST** /fabric/v4/loas/search | Search Loas
[**search_loa_action**](LoasApi.md#search_loa_action) | **POST** /fabric/v4/loas/{loaId}/actions/search | Search Loa Actions
[**update_loa_by_uuid**](LoasApi.md#update_loa_by_uuid) | **PATCH** /fabric/v4/loas/{loaId} | Update Loa


# **create_loa**
> LoaResponse create_loa(create_loa)

Create Loa

The API provides capability to create a new Loa

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.create_loa import CreateLoa
from equinix.services.fabricv4.models.loa_response import LoaResponse
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
    api_instance = equinix.services.fabricv4.LoasApi(api_client)
    create_loa = equinix.services.fabricv4.CreateLoa() # CreateLoa | 

    try:
        # Create Loa
        api_response = api_instance.create_loa(create_loa)
        print("The response of LoasApi->create_loa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoasApi->create_loa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_loa** | [**CreateLoa**](CreateLoa.md)|  | 

### Return type

[**LoaResponse**](LoaResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized request |  -  |
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_loa_note_by_loa_id**
> LoaNoteDetails create_loa_note_by_loa_id(loa_id, create_loa_note)

Create Loa Note

The API provides capability to create Loa note by Loa ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.create_loa_note import CreateLoaNote
from equinix.services.fabricv4.models.loa_note_details import LoaNoteDetails
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
    api_instance = equinix.services.fabricv4.LoasApi(api_client)
    loa_id = 'loa_id_example' # str | Loa UUID
    create_loa_note = equinix.services.fabricv4.CreateLoaNote() # CreateLoaNote | 

    try:
        # Create Loa Note
        api_response = api_instance.create_loa_note_by_loa_id(loa_id, create_loa_note)
        print("The response of LoasApi->create_loa_note_by_loa_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoasApi->create_loa_note_by_loa_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loa_id** | **str**| Loa UUID | 
 **create_loa_note** | [**CreateLoaNote**](CreateLoaNote.md)|  | 

### Return type

[**LoaNoteDetails**](LoaNoteDetails.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized request |  -  |
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loa_actions_by_uuid**
> LoaActionResponse get_loa_actions_by_uuid(loa_id, action_id)

Get Loa Action by Action ID

This API provides capability to fetch action details

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.loa_action_response import LoaActionResponse
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
    api_instance = equinix.services.fabricv4.LoasApi(api_client)
    loa_id = 'loa_id_example' # str | Loa UUID
    action_id = 'action_id_example' # str | Action UUID

    try:
        # Get Loa Action by Action ID
        api_response = api_instance.get_loa_actions_by_uuid(loa_id, action_id)
        print("The response of LoasApi->get_loa_actions_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoasApi->get_loa_actions_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loa_id** | **str**| Loa UUID | 
 **action_id** | **str**| Action UUID | 

### Return type

[**LoaActionResponse**](LoaActionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized request |  -  |
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loa_by_uuid**
> LoaResponse get_loa_by_uuid(loa_id)

Get Loa

The API provides capability to get Loa details by Loa ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.loa_response import LoaResponse
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
    api_instance = equinix.services.fabricv4.LoasApi(api_client)
    loa_id = 'loa_id_example' # str | Loa UUID

    try:
        # Get Loa
        api_response = api_instance.get_loa_by_uuid(loa_id)
        print("The response of LoasApi->get_loa_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoasApi->get_loa_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loa_id** | **str**| Loa UUID | 

### Return type

[**LoaResponse**](LoaResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized request |  -  |
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loa_consumers_by_loa_id**
> LoaConsumersResponse get_loa_consumers_by_loa_id(loa_id)

Get Loa Consumers

The API provides capability to get Loa consumers by Loa ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.loa_consumers_response import LoaConsumersResponse
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
    api_instance = equinix.services.fabricv4.LoasApi(api_client)
    loa_id = 'loa_id_example' # str | Loa UUID

    try:
        # Get Loa Consumers
        api_response = api_instance.get_loa_consumers_by_loa_id(loa_id)
        print("The response of LoasApi->get_loa_consumers_by_loa_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoasApi->get_loa_consumers_by_loa_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loa_id** | **str**| Loa UUID | 

### Return type

[**LoaConsumersResponse**](LoaConsumersResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized request |  -  |
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loa_notes_by_uuid**
> LoaNotesResponse get_loa_notes_by_uuid(loa_id)

Get Loa Notes

The API provides capability to get Loa notes by Loa ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.loa_notes_response import LoaNotesResponse
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
    api_instance = equinix.services.fabricv4.LoasApi(api_client)
    loa_id = 'loa_id_example' # str | Loa UUID

    try:
        # Get Loa Notes
        api_response = api_instance.get_loa_notes_by_uuid(loa_id)
        print("The response of LoasApi->get_loa_notes_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoasApi->get_loa_notes_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loa_id** | **str**| Loa UUID | 

### Return type

[**LoaNotesResponse**](LoaNotesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized request |  -  |
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_loa_action**
> LoaActionResponse perform_loa_action(loa_id, loa_action_request)

Loa Actions

The API provides capability to perform actions on Loa

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.loa_action_request import LoaActionRequest
from equinix.services.fabricv4.models.loa_action_response import LoaActionResponse
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
    api_instance = equinix.services.fabricv4.LoasApi(api_client)
    loa_id = 'loa_id_example' # str | Loa UUID
    loa_action_request = equinix.services.fabricv4.LoaActionRequest() # LoaActionRequest | 

    try:
        # Loa Actions
        api_response = api_instance.perform_loa_action(loa_id, loa_action_request)
        print("The response of LoasApi->perform_loa_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoasApi->perform_loa_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loa_id** | **str**| Loa UUID | 
 **loa_action_request** | [**LoaActionRequest**](LoaActionRequest.md)|  | 

### Return type

[**LoaActionResponse**](LoaActionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized request |  -  |
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_loa**
> LoaSearchResponse search_loa(loa_search_request)

Search Loas

The API provides capability to get list of user's Loa using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.loa_search_request import LoaSearchRequest
from equinix.services.fabricv4.models.loa_search_response import LoaSearchResponse
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
    api_instance = equinix.services.fabricv4.LoasApi(api_client)
    loa_search_request = equinix.services.fabricv4.LoaSearchRequest() # LoaSearchRequest | 

    try:
        # Search Loas
        api_response = api_instance.search_loa(loa_search_request)
        print("The response of LoasApi->search_loa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoasApi->search_loa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loa_search_request** | [**LoaSearchRequest**](LoaSearchRequest.md)|  | 

### Return type

[**LoaSearchResponse**](LoaSearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized request |  -  |
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_loa_action**
> LoaActionSearchResponse search_loa_action(loa_id, loa_action_search_request)

Search Loa Actions

The API provides capability to get list of user's Loa Actions using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.loa_action_search_request import LoaActionSearchRequest
from equinix.services.fabricv4.models.loa_action_search_response import LoaActionSearchResponse
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
    api_instance = equinix.services.fabricv4.LoasApi(api_client)
    loa_id = 'loa_id_example' # str | Loa UUID
    loa_action_search_request = equinix.services.fabricv4.LoaActionSearchRequest() # LoaActionSearchRequest | 

    try:
        # Search Loa Actions
        api_response = api_instance.search_loa_action(loa_id, loa_action_search_request)
        print("The response of LoasApi->search_loa_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoasApi->search_loa_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loa_id** | **str**| Loa UUID | 
 **loa_action_search_request** | [**LoaActionSearchRequest**](LoaActionSearchRequest.md)|  | 

### Return type

[**LoaActionSearchResponse**](LoaActionSearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized request |  -  |
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loa_by_uuid**
> LoaResponse update_loa_by_uuid(loa_id, loa_replace_operation)

Update Loa

The API provides capability to update Loa details by Loa ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.loa_replace_operation import LoaReplaceOperation
from equinix.services.fabricv4.models.loa_response import LoaResponse
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
    api_instance = equinix.services.fabricv4.LoasApi(api_client)
    loa_id = 'loa_id_example' # str | Loa UUID
    loa_replace_operation = [equinix.services.fabricv4.LoaReplaceOperation()] # List[LoaReplaceOperation] | 

    try:
        # Update Loa
        api_response = api_instance.update_loa_by_uuid(loa_id, loa_replace_operation)
        print("The response of LoasApi->update_loa_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoasApi->update_loa_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loa_id** | **str**| Loa UUID | 
 **loa_replace_operation** | [**List[LoaReplaceOperation]**](LoaReplaceOperation.md)|  | 

### Return type

[**LoaResponse**](LoaResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized request |  -  |
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**500** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

