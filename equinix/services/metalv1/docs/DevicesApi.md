# equinix_metal.DevicesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bgp_session**](DevicesApi.md#create_bgp_session) | **POST** /devices/{id}/bgp/sessions | Create a BGP session
[**create_device**](DevicesApi.md#create_device) | **POST** /projects/{id}/devices | Create a device
[**create_ip_assignment**](DevicesApi.md#create_ip_assignment) | **POST** /devices/{id}/ips | Create an ip assignment
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /devices/{id} | Delete the device
[**find_bgp_sessions**](DevicesApi.md#find_bgp_sessions) | **GET** /devices/{id}/bgp/sessions | Retrieve all BGP sessions
[**find_device_by_id**](DevicesApi.md#find_device_by_id) | **GET** /devices/{id} | Retrieve a device
[**find_device_customdata**](DevicesApi.md#find_device_customdata) | **GET** /devices/{id}/customdata | Retrieve the custom metadata of an instance
[**find_device_metadata_by_id**](DevicesApi.md#find_device_metadata_by_id) | **GET** /devices/{id}/metadata | Retrieve metadata
[**find_device_userdata_by_id**](DevicesApi.md#find_device_userdata_by_id) | **GET** /devices/{id}/userdata | Retrieve userdata
[**find_instance_bandwidth**](DevicesApi.md#find_instance_bandwidth) | **GET** /devices/{id}/bandwidth | Retrieve an instance bandwidth
[**find_ip_assignment_customdata**](DevicesApi.md#find_ip_assignment_customdata) | **GET** /devices/{instance_id}/ips/{id}/customdata | Retrieve the custom metadata of an IP Assignment
[**find_ip_assignments**](DevicesApi.md#find_ip_assignments) | **GET** /devices/{id}/ips | Retrieve all ip assignments
[**find_organization_devices**](DevicesApi.md#find_organization_devices) | **GET** /organizations/{id}/devices | Retrieve all devices of an organization
[**find_organization_devices_all_pages**](DevicesApi.md#find_organization_devices_all_pages) | **GET** /organizations/{id}/devices | Retrieve all devices of an organization, fetches all the pages
[**find_project_devices**](DevicesApi.md#find_project_devices) | **GET** /projects/{id}/devices | Retrieve all devices of a project
[**find_project_devices_all_pages**](DevicesApi.md#find_project_devices_all_pages) | **GET** /projects/{id}/devices | Retrieve all devices of a project, fetches all the pages
[**find_traffic**](DevicesApi.md#find_traffic) | **GET** /devices/{id}/traffic | Retrieve device traffic
[**get_bgp_neighbor_data**](DevicesApi.md#get_bgp_neighbor_data) | **GET** /devices/{id}/bgp/neighbors | Retrieve BGP neighbor data for this device
[**get_device_firmware_sets**](DevicesApi.md#get_device_firmware_sets) | **GET** /devices/{id}/firmware-sets | Get Device&#39;s associated Firmware Set
[**get_device_health_rollup**](DevicesApi.md#get_device_health_rollup) | **GET** /devices/{id}/diagnostics/health/rollup | Get Device&#39;s Health Status
[**perform_action**](DevicesApi.md#perform_action) | **POST** /devices/{id}/actions | Perform an action
[**update_device**](DevicesApi.md#update_device) | **PUT** /devices/{id} | Update the device


# **create_bgp_session**
> BgpSession create_bgp_session(id, bgp_session_input, include=include)

Create a BGP session

Creates a BGP session.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.bgp_session_input import BGPSessionInput
from equinix_metal.models.bgp_session import BgpSession
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    bgp_session_input = equinix_metal.BGPSessionInput() # BGPSessionInput | BGP session to create
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Create a BGP session
        api_response = api_instance.create_bgp_session(id, bgp_session_input, include=include)
        print("The response of DevicesApi->create_bgp_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->create_bgp_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **bgp_session_input** | [**BGPSessionInput**](BGPSessionInput.md)| BGP session to create | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**BgpSession**](BgpSession.md)

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
**403** | forbidden |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **create_device**
> Device create_device(id, create_device_request, include=include, exclude=exclude)

Create a device

Creates a new device and provisions it in the specified location.  Device type-specific options are accepted.  For example, `baremetal` devices accept `operating_system`, `hostname`, and `plan`. These parameters may not be accepted for other device types. The default device type is `baremetal`.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.create_device_request import CreateDeviceRequest
from equinix_metal.models.device import Device
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Project UUID
    create_device_request = equinix_metal.CreateDeviceRequest() # CreateDeviceRequest | Device to create
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Create a device
        api_response = api_instance.create_device(id, create_device_request, include=include, exclude=exclude)
        print("The response of DevicesApi->create_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->create_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **create_device_request** | [**CreateDeviceRequest**](CreateDeviceRequest.md)| Device to create | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**Device**](Device.md)

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
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **create_ip_assignment**
> IPAssignment create_ip_assignment(id, ip_assignment_input, include=include, exclude=exclude)

Create an ip assignment

Creates an ip assignment for a device.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.ip_assignment import IPAssignment
from equinix_metal.models.ip_assignment_input import IPAssignmentInput
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    ip_assignment_input = equinix_metal.IPAssignmentInput() # IPAssignmentInput | IPAssignment to create
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Create an ip assignment
        api_response = api_instance.create_ip_assignment(id, ip_assignment_input, include=include, exclude=exclude)
        print("The response of DevicesApi->create_ip_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->create_ip_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **ip_assignment_input** | [**IPAssignmentInput**](IPAssignmentInput.md)| IPAssignment to create | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**IPAssignment**](IPAssignment.md)

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
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **delete_device**
> delete_device(id, force_delete=force_delete)

Delete the device

Deletes a device and deprovisions it in our datacenter.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    force_delete = True # bool | Force the deletion of the device, by detaching any storage volume still active. (optional)

    try:
        # Delete the device
        api_instance.delete_device(id, force_delete=force_delete)
    except Exception as e:
        print("Exception when calling DevicesApi->delete_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **force_delete** | **bool**| Force the deletion of the device, by detaching any storage volume still active. | [optional] 

### Return type

void (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | no content |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_bgp_sessions**
> BgpSessionList find_bgp_sessions(id, include=include)

Retrieve all BGP sessions

Provides a listing of available BGP sessions for the device.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.bgp_session_list import BgpSessionList
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Retrieve all BGP sessions
        api_response = api_instance.find_bgp_sessions(id, include=include)
        print("The response of DevicesApi->find_bgp_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_bgp_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**BgpSessionList**](BgpSessionList.md)

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
# **find_device_by_id**
> Device find_device_by_id(id, include=include, exclude=exclude)

Retrieve a device

Type-specific options (such as facility for baremetal devices) will be included as part of the main data structure.                          State value can be one of: active inactive queued or provisioning

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.device import Device
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve a device
        api_response = api_instance.find_device_by_id(id, include=include, exclude=exclude)
        print("The response of DevicesApi->find_device_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_device_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**Device**](Device.md)

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
# **find_device_customdata**
> find_device_customdata(id)

Retrieve the custom metadata of an instance

Provides the custom metadata stored for this instance in json format

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Instance UUID

    try:
        # Retrieve the custom metadata of an instance
        api_instance.find_device_customdata(id)
    except Exception as e:
        print("Exception when calling DevicesApi->find_device_customdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Instance UUID | 

### Return type

void (empty response body)

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
# **find_device_metadata_by_id**
> Metadata find_device_metadata_by_id(id)

Retrieve metadata

Retrieve device metadata

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.metadata import Metadata
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID

    try:
        # Retrieve metadata
        api_response = api_instance.find_device_metadata_by_id(id)
        print("The response of DevicesApi->find_device_metadata_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_device_metadata_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 

### Return type

[**Metadata**](Metadata.md)

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
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_device_userdata_by_id**
> Userdata find_device_userdata_by_id(id)

Retrieve userdata

Retrieve device userdata

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.userdata import Userdata
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID

    try:
        # Retrieve userdata
        api_response = api_instance.find_device_userdata_by_id(id)
        print("The response of DevicesApi->find_device_userdata_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_device_userdata_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 

### Return type

[**Userdata**](Userdata.md)

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
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_instance_bandwidth**
> find_instance_bandwidth(id, var_from, until)

Retrieve an instance bandwidth

Retrieve an instance bandwidth for a given period of time.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    var_from = 'var_from_example' # str | Timestamp from range
    until = 'until_example' # str | Timestamp to range

    try:
        # Retrieve an instance bandwidth
        api_instance.find_instance_bandwidth(id, var_from, until)
    except Exception as e:
        print("Exception when calling DevicesApi->find_instance_bandwidth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **var_from** | **str**| Timestamp from range | 
 **until** | **str**| Timestamp to range | 

### Return type

void (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_ip_assignment_customdata**
> find_ip_assignment_customdata(instance_id, id)

Retrieve the custom metadata of an IP Assignment

Provides the custom metadata stored for this IP Assignment in json format

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
    api_instance = equinix_metal.DevicesApi(api_client)
    instance_id = 'instance_id_example' # str | Instance UUID
    id = 'id_example' # str | Ip Assignment UUID

    try:
        # Retrieve the custom metadata of an IP Assignment
        api_instance.find_ip_assignment_customdata(instance_id, id)
    except Exception as e:
        print("Exception when calling DevicesApi->find_ip_assignment_customdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance UUID | 
 **id** | **str**| Ip Assignment UUID | 

### Return type

void (empty response body)

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
# **find_ip_assignments**
> IPAssignmentList find_ip_assignments(id, include=include, exclude=exclude)

Retrieve all ip assignments

Returns all ip assignments for a device.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.ip_assignment_list import IPAssignmentList
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve all ip assignments
        api_response = api_instance.find_ip_assignments(id, include=include, exclude=exclude)
        print("The response of DevicesApi->find_ip_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_ip_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**IPAssignmentList**](IPAssignmentList.md)

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
# **find_organization_devices**
> DeviceList find_organization_devices(id, search=search, categories=categories, facility=facility, hostname=hostname, reserved=reserved, tag=tag, type=type, has_termination_time=has_termination_time, mac_address=mac_address, include=include, exclude=exclude, page=page, per_page=per_page)

Retrieve all devices of an organization

Provides a collection of devices for a given organization.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.device_list import DeviceList
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Organization UUID
    search = 'search_example' # str | Search by hostname, description, short_id, reservation short_id, tags, plan name, plan slug, facility code, facility name, operating system name, operating system slug, IP addresses. (optional)
    categories = ['categories_example'] # List[str] | Filter by plan category (optional)
    facility = 'facility_example' # str | Filter by device facility (optional)
    hostname = 'hostname_example' # str | Filter by partial hostname (optional)
    reserved = True # bool | Filter only reserved instances. When set to true, only include reserved instances. When set to false, only include on-demand instances. (optional)
    tag = 'tag_example' # str | Filter by device tag (optional)
    type = 'type_example' # str | Filter by instance type (ondemand,spot,reserved) (optional)
    has_termination_time = True # bool | Filter only instances marked for termination. When set to true, only include instances that have a termination time. When set to false, only include instances that do not have a termination time. (optional)
    mac_address = 'mac_address_example' # str | Filter by MAC address (optional)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
    page = 1 # int | Page to return (optional) (default to 1)
    per_page = 10 # int | Items returned per page (optional) (default to 10)

    try:
        # Retrieve all devices of an organization
        api_response = api_instance.find_organization_devices(id, search=search, categories=categories, facility=facility, hostname=hostname, reserved=reserved, tag=tag, type=type, has_termination_time=has_termination_time, mac_address=mac_address, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of DevicesApi->find_organization_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_organization_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization UUID | 
 **search** | **str**| Search by hostname, description, short_id, reservation short_id, tags, plan name, plan slug, facility code, facility name, operating system name, operating system slug, IP addresses. | [optional] 
 **categories** | [**List[str]**](str.md)| Filter by plan category | [optional] 
 **facility** | **str**| Filter by device facility | [optional] 
 **hostname** | **str**| Filter by partial hostname | [optional] 
 **reserved** | **bool**| Filter only reserved instances. When set to true, only include reserved instances. When set to false, only include on-demand instances. | [optional] 
 **tag** | **str**| Filter by device tag | [optional] 
 **type** | **str**| Filter by instance type (ondemand,spot,reserved) | [optional] 
 **has_termination_time** | **bool**| Filter only instances marked for termination. When set to true, only include instances that have a termination time. When set to false, only include instances that do not have a termination time. | [optional] 
 **mac_address** | **str**| Filter by MAC address | [optional] 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **page** | **int**| Page to return | [optional] [default to 1]
 **per_page** | **int**| Items returned per page | [optional] [default to 10]

### Return type

[**DeviceList**](DeviceList.md)

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
# **find_organization_devices_all_pages**
> DeviceList find_organization_devices_all_pages(id, search=search, categories=categories, facility=facility, hostname=hostname, reserved=reserved, tag=tag, type=type, has_termination_time=has_termination_time, mac_address=mac_address, include=include, exclude=exclude, per_page=per_page)
Just like [**find_organization_devices**](DevicesApi.md#find_organization_devices) but fetches resources from all pages. This method doesn't take `page` parameter. Other parameters, return type and other characteristics are the same as in [**find_organization_devices**](DevicesApi.md#find_organization_devices).
# **find_project_devices**
> DeviceList find_project_devices(id, search=search, categories=categories, facility=facility, metro=metro, hostname=hostname, reserved=reserved, tag=tag, type=type, has_termination_time=has_termination_time, mac_address=mac_address, include=include, exclude=exclude, page=page, per_page=per_page)

Retrieve all devices of a project

Provides a collection of devices for a given project.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.device_list import DeviceList
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Project UUID
    search = 'search_example' # str | Search by hostname, description, short_id, reservation short_id, tags, plan name, plan slug, facility code, facility name, operating system name, operating system slug, IP addresses. (optional)
    categories = ['categories_example'] # List[str] | Filter by plan category (optional)
    facility = 'facility_example' # str | Filter by device facility (optional)
    metro = 'metro_example' # str | Filter by device metro (optional)
    hostname = 'hostname_example' # str | Filter by partial hostname (optional)
    reserved = True # bool | Filter only reserved instances. When set to true, only include reserved instances. When set to false, only include on-demand instances. (optional)
    tag = 'tag_example' # str | Filter by device tag (optional)
    type = 'type_example' # str | Filter by instance type (ondemand,spot,reserved) (optional)
    has_termination_time = True # bool | Filter only instances marked for termination. When set to true, only include instances that have a termination time. When set to false, only include instances that do not have a termination time. (optional)
    mac_address = 'mac_address_example' # str | Filter by MAC address (optional)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
    page = 1 # int | Page to return (optional) (default to 1)
    per_page = 10 # int | Items returned per page (optional) (default to 10)

    try:
        # Retrieve all devices of a project
        api_response = api_instance.find_project_devices(id, search=search, categories=categories, facility=facility, metro=metro, hostname=hostname, reserved=reserved, tag=tag, type=type, has_termination_time=has_termination_time, mac_address=mac_address, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of DevicesApi->find_project_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_project_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **search** | **str**| Search by hostname, description, short_id, reservation short_id, tags, plan name, plan slug, facility code, facility name, operating system name, operating system slug, IP addresses. | [optional] 
 **categories** | [**List[str]**](str.md)| Filter by plan category | [optional] 
 **facility** | **str**| Filter by device facility | [optional] 
 **metro** | **str**| Filter by device metro | [optional] 
 **hostname** | **str**| Filter by partial hostname | [optional] 
 **reserved** | **bool**| Filter only reserved instances. When set to true, only include reserved instances. When set to false, only include on-demand instances. | [optional] 
 **tag** | **str**| Filter by device tag | [optional] 
 **type** | **str**| Filter by instance type (ondemand,spot,reserved) | [optional] 
 **has_termination_time** | **bool**| Filter only instances marked for termination. When set to true, only include instances that have a termination time. When set to false, only include instances that do not have a termination time. | [optional] 
 **mac_address** | **str**| Filter by MAC address | [optional] 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **page** | **int**| Page to return | [optional] [default to 1]
 **per_page** | **int**| Items returned per page | [optional] [default to 10]

### Return type

[**DeviceList**](DeviceList.md)

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
# **find_project_devices_all_pages**
> DeviceList find_project_devices_all_pages(id, search=search, categories=categories, facility=facility, metro=metro, hostname=hostname, reserved=reserved, tag=tag, type=type, has_termination_time=has_termination_time, mac_address=mac_address, include=include, exclude=exclude, per_page=per_page)
Just like [**find_project_devices**](DevicesApi.md#find_project_devices) but fetches resources from all pages. This method doesn't take `page` parameter. Other parameters, return type and other characteristics are the same as in [**find_project_devices**](DevicesApi.md#find_project_devices).
# **find_traffic**
> find_traffic(id, direction, interval=interval, bucket=bucket, timeframe=timeframe)

Retrieve device traffic

Returns the total amount of inbound or outbound traffic for a specific device. The default time period is 1 hour.  Please note the results capture all network traffic for the server, but not all traffic may come from or be destined to the Internet and may be non-billable. Only Internet bound traffic is charged. 

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.find_traffic_timeframe_parameter import FindTrafficTimeframeParameter
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    direction = 'direction_example' # str | Traffic direction
    interval = 'interval_example' # str | Traffic interval (optional)
    bucket = 'bucket_example' # str | Traffic bucket (optional)
    timeframe = equinix_metal.FindTrafficTimeframeParameter() # FindTrafficTimeframeParameter |  (optional)

    try:
        # Retrieve device traffic
        api_instance.find_traffic(id, direction, interval=interval, bucket=bucket, timeframe=timeframe)
    except Exception as e:
        print("Exception when calling DevicesApi->find_traffic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **direction** | **str**| Traffic direction | 
 **interval** | **str**| Traffic interval | [optional] 
 **bucket** | **str**| Traffic bucket | [optional] 
 **timeframe** | [**FindTrafficTimeframeParameter**](.md)|  | [optional] 

### Return type

void (empty response body)

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
# **get_bgp_neighbor_data**
> BgpSessionNeighbors get_bgp_neighbor_data(id, include=include)

Retrieve BGP neighbor data for this device

Provides a summary of the BGP neighbor data associated to the BGP sessions for this device.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.bgp_session_neighbors import BgpSessionNeighbors
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Retrieve BGP neighbor data for this device
        api_response = api_instance.get_bgp_neighbor_data(id, include=include)
        print("The response of DevicesApi->get_bgp_neighbor_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_bgp_neighbor_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**BgpSessionNeighbors**](BgpSessionNeighbors.md)

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
# **get_device_firmware_sets**
> FirmwareSetResponse get_device_firmware_sets(id)

Get Device's associated Firmware Set

Returns the firmware set associated with the device. If a custom firmware set is associated with the device, then it is returned. Otherwise, if a default firmware set is available it is returned.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.firmware_set_response import FirmwareSetResponse
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID

    try:
        # Get Device's associated Firmware Set
        api_response = api_instance.get_device_firmware_sets(id)
        print("The response of DevicesApi->get_device_firmware_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_firmware_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 

### Return type

[**FirmwareSetResponse**](FirmwareSetResponse.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Error responses are included with 4xx and 5xx HTTP responses from the API service. Either \&quot;error\&quot; or \&quot;errors\&quot; will be set. |  -  |
**404** | Error responses are included with 4xx and 5xx HTTP responses from the API service. Either \&quot;error\&quot; or \&quot;errors\&quot; will be set. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **get_device_health_rollup**
> DeviceHealthRollup get_device_health_rollup(id)

Get Device's Health Status

Returns the health rollup status of the device.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.device_health_rollup import DeviceHealthRollup
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID

    try:
        # Get Device's Health Status
        api_response = api_instance.get_device_health_rollup(id)
        print("The response of DevicesApi->get_device_health_rollup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_health_rollup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 

### Return type

[**DeviceHealthRollup**](DeviceHealthRollup.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Error responses are included with 4xx and 5xx HTTP responses from the API service. Either \&quot;error\&quot; or \&quot;errors\&quot; will be set. |  -  |
**404** | Error responses are included with 4xx and 5xx HTTP responses from the API service. Either \&quot;error\&quot; or \&quot;errors\&quot; will be set. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **perform_action**
> perform_action(id, device_action_input)

Perform an action

Performs an action for the given device.  Possible actions include: power_on, power_off, reboot, reinstall, and rescue (reboot the device into rescue OS.)

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.device_action_input import DeviceActionInput
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    device_action_input = equinix_metal.DeviceActionInput() # DeviceActionInput | Action to perform

    try:
        # Perform an action
        api_instance.perform_action(id, device_action_input)
    except Exception as e:
        print("Exception when calling DevicesApi->perform_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **device_action_input** | [**DeviceActionInput**](DeviceActionInput.md)| Action to perform | 

### Return type

void (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | accepted |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **update_device**
> Device update_device(id, device_update_input, include=include, exclude=exclude)

Update the device

Updates the device.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.device import Device
from equinix_metal.models.device_update_input import DeviceUpdateInput
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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    device_update_input = equinix_metal.DeviceUpdateInput() # DeviceUpdateInput | Device to update
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Update the device
        api_response = api_instance.update_device(id, device_update_input, include=include, exclude=exclude)
        print("The response of DevicesApi->update_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->update_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **device_update_input** | [**DeviceUpdateInput**](DeviceUpdateInput.md)| Device to update | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**Device**](Device.md)

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
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
