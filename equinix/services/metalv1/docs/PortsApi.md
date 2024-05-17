# equinix_metal.PortsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_native_vlan**](PortsApi.md#assign_native_vlan) | **POST** /ports/{id}/native-vlan | Assign a native VLAN
[**assign_port**](PortsApi.md#assign_port) | **POST** /ports/{id}/assign | Assign a port to virtual network
[**bond_port**](PortsApi.md#bond_port) | **POST** /ports/{id}/bond | Enabling bonding
[**convert_layer2**](PortsApi.md#convert_layer2) | **POST** /ports/{id}/convert/layer-2 | Convert to Layer 2
[**convert_layer3**](PortsApi.md#convert_layer3) | **POST** /ports/{id}/convert/layer-3 | Convert to Layer 3
[**create_port_vlan_assignment_batch**](PortsApi.md#create_port_vlan_assignment_batch) | **POST** /ports/{id}/vlan-assignments/batches | Create a new Port-VLAN Assignment management batch
[**delete_native_vlan**](PortsApi.md#delete_native_vlan) | **DELETE** /ports/{id}/native-vlan | Remove native VLAN
[**disbond_port**](PortsApi.md#disbond_port) | **POST** /ports/{id}/disbond | Disabling bonding
[**find_port_by_id**](PortsApi.md#find_port_by_id) | **GET** /ports/{id} | Retrieve a port
[**find_port_vlan_assignment_batch_by_port_id_and_batch_id**](PortsApi.md#find_port_vlan_assignment_batch_by_port_id_and_batch_id) | **GET** /ports/{id}/vlan-assignments/batches/{batch_id} | Retrieve a VLAN Assignment Batch&#39;s details
[**find_port_vlan_assignment_batches**](PortsApi.md#find_port_vlan_assignment_batches) | **GET** /ports/{id}/vlan-assignments/batches | List the VLAN Assignment Batches for a port
[**find_port_vlan_assignment_by_port_id_and_assignment_id**](PortsApi.md#find_port_vlan_assignment_by_port_id_and_assignment_id) | **GET** /ports/{id}/vlan-assignments/{assignment_id} | Show a particular Port VLAN assignment&#39;s details
[**find_port_vlan_assignments**](PortsApi.md#find_port_vlan_assignments) | **GET** /ports/{id}/vlan-assignments | List Current VLAN assignments for a port
[**unassign_port**](PortsApi.md#unassign_port) | **POST** /ports/{id}/unassign | Unassign a port


# **assign_native_vlan**
> Port assign_native_vlan(id, vnid, include=include)

Assign a native VLAN

Sets a virtual network on this port as a \"native VLAN\". The VLAN must have already been assigned using the using the \"Assign a port to a virtual network\" operation.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port import Port
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    vnid = 'vnid_example' # str | Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: '1001').
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Assign a native VLAN
        api_response = api_instance.assign_native_vlan(id, vnid, include=include)
        print("The response of PortsApi->assign_native_vlan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->assign_native_vlan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **vnid** | **str**| Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: &#39;1001&#39;). | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**Port**](Port.md)

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
# **assign_port**
> Port assign_port(id, port_assign_input, include=include)

Assign a port to virtual network

Assign a hardware port to a virtual network.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port import Port
from equinix_metal.models.port_assign_input import PortAssignInput
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    port_assign_input = equinix_metal.PortAssignInput() # PortAssignInput | Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: '1001').
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Assign a port to virtual network
        api_response = api_instance.assign_port(id, port_assign_input, include=include)
        print("The response of PortsApi->assign_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->assign_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **port_assign_input** | [**PortAssignInput**](PortAssignInput.md)| Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: &#39;1001&#39;). | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**Port**](Port.md)

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
# **bond_port**
> Port bond_port(id, bulk_enable=bulk_enable, include=include)

Enabling bonding

Enabling bonding for one or all ports

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port import Port
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    bulk_enable = True # bool | enable both ports (optional)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Enabling bonding
        api_response = api_instance.bond_port(id, bulk_enable=bulk_enable, include=include)
        print("The response of PortsApi->bond_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->bond_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **bulk_enable** | **bool**| enable both ports | [optional] 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**Port**](Port.md)

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
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **convert_layer2**
> Port convert_layer2(id, port_assign_input, include=include)

Convert to Layer 2

Converts a bond port to Layer 2. IP assignments of the port will be removed.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port import Port
from equinix_metal.models.port_assign_input import PortAssignInput
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    port_assign_input = equinix_metal.PortAssignInput() # PortAssignInput | Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: '1001').
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Convert to Layer 2
        api_response = api_instance.convert_layer2(id, port_assign_input, include=include)
        print("The response of PortsApi->convert_layer2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->convert_layer2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **port_assign_input** | [**PortAssignInput**](PortAssignInput.md)| Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: &#39;1001&#39;). | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**Port**](Port.md)

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
# **convert_layer3**
> Port convert_layer3(id, include=include, port_convert_layer3_input=port_convert_layer3_input)

Convert to Layer 3

Converts a bond port to Layer 3. VLANs must first be unassigned.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port import Port
from equinix_metal.models.port_convert_layer3_input import PortConvertLayer3Input
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    port_convert_layer3_input = equinix_metal.PortConvertLayer3Input() # PortConvertLayer3Input | IPs to request (optional)

    try:
        # Convert to Layer 3
        api_response = api_instance.convert_layer3(id, include=include, port_convert_layer3_input=port_convert_layer3_input)
        print("The response of PortsApi->convert_layer3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->convert_layer3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **port_convert_layer3_input** | [**PortConvertLayer3Input**](PortConvertLayer3Input.md)| IPs to request | [optional] 

### Return type

[**Port**](Port.md)

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
# **create_port_vlan_assignment_batch**
> PortVlanAssignmentBatch create_port_vlan_assignment_batch(id, port_vlan_assignment_batch_create_input, include=include)

Create a new Port-VLAN Assignment management batch

Create a new asynchronous batch request which handles adding and/or removing the VLANs to which the port is assigned.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port_vlan_assignment_batch import PortVlanAssignmentBatch
from equinix_metal.models.port_vlan_assignment_batch_create_input import PortVlanAssignmentBatchCreateInput
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    port_vlan_assignment_batch_create_input = equinix_metal.PortVlanAssignmentBatchCreateInput() # PortVlanAssignmentBatchCreateInput | VLAN Assignment batch details
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Create a new Port-VLAN Assignment management batch
        api_response = api_instance.create_port_vlan_assignment_batch(id, port_vlan_assignment_batch_create_input, include=include)
        print("The response of PortsApi->create_port_vlan_assignment_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->create_port_vlan_assignment_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **port_vlan_assignment_batch_create_input** | [**PortVlanAssignmentBatchCreateInput**](PortVlanAssignmentBatchCreateInput.md)| VLAN Assignment batch details | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**PortVlanAssignmentBatch**](PortVlanAssignmentBatch.md)

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
# **delete_native_vlan**
> Port delete_native_vlan(id, include=include)

Remove native VLAN

Removes the native VLAN from this port

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port import Port
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Remove native VLAN
        api_response = api_instance.delete_native_vlan(id, include=include)
        print("The response of PortsApi->delete_native_vlan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->delete_native_vlan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**Port**](Port.md)

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
# **disbond_port**
> Port disbond_port(id, bulk_disable=bulk_disable, include=include)

Disabling bonding

Disabling bonding for one or all ports

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port import Port
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    bulk_disable = True # bool | disable both ports (optional)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Disabling bonding
        api_response = api_instance.disbond_port(id, bulk_disable=bulk_disable, include=include)
        print("The response of PortsApi->disbond_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->disbond_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **bulk_disable** | **bool**| disable both ports | [optional] 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**Port**](Port.md)

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
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_port_by_id**
> Port find_port_by_id(id, include=include)

Retrieve a port

Returns a port

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port import Port
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Retrieve a port
        api_response = api_instance.find_port_by_id(id, include=include)
        print("The response of PortsApi->find_port_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->find_port_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**Port**](Port.md)

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
# **find_port_vlan_assignment_batch_by_port_id_and_batch_id**
> PortVlanAssignmentBatch find_port_vlan_assignment_batch_by_port_id_and_batch_id(id, batch_id, include=include)

Retrieve a VLAN Assignment Batch's details

Returns the details of an existing Port-VLAN Assignment batch, including the list of VLANs to assign or unassign, and the current state of the batch.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port_vlan_assignment_batch import PortVlanAssignmentBatch
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    batch_id = 'batch_id_example' # str | Batch ID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Retrieve a VLAN Assignment Batch's details
        api_response = api_instance.find_port_vlan_assignment_batch_by_port_id_and_batch_id(id, batch_id, include=include)
        print("The response of PortsApi->find_port_vlan_assignment_batch_by_port_id_and_batch_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->find_port_vlan_assignment_batch_by_port_id_and_batch_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **batch_id** | **str**| Batch ID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**PortVlanAssignmentBatch**](PortVlanAssignmentBatch.md)

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
# **find_port_vlan_assignment_batches**
> PortVlanAssignmentBatchList find_port_vlan_assignment_batches(id)

List the VLAN Assignment Batches for a port

Show all the VLAN assignment batches that have been created for managing this port's VLAN assignments

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port_vlan_assignment_batch_list import PortVlanAssignmentBatchList
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID

    try:
        # List the VLAN Assignment Batches for a port
        api_response = api_instance.find_port_vlan_assignment_batches(id)
        print("The response of PortsApi->find_port_vlan_assignment_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->find_port_vlan_assignment_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 

### Return type

[**PortVlanAssignmentBatchList**](PortVlanAssignmentBatchList.md)

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
# **find_port_vlan_assignment_by_port_id_and_assignment_id**
> PortVlanAssignment find_port_vlan_assignment_by_port_id_and_assignment_id(id, assignment_id, include=include)

Show a particular Port VLAN assignment's details

Show the details of a specific Port-VLAN assignment, including the current state and if the VLAN is set as native.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port_vlan_assignment import PortVlanAssignment
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    assignment_id = 'assignment_id_example' # str | Assignment ID
    include = ["port","virtual_network"] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional) (default to ["port","virtual_network"])

    try:
        # Show a particular Port VLAN assignment's details
        api_response = api_instance.find_port_vlan_assignment_by_port_id_and_assignment_id(id, assignment_id, include=include)
        print("The response of PortsApi->find_port_vlan_assignment_by_port_id_and_assignment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->find_port_vlan_assignment_by_port_id_and_assignment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **assignment_id** | **str**| Assignment ID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] [default to [&quot;port&quot;,&quot;virtual_network&quot;]]

### Return type

[**PortVlanAssignment**](PortVlanAssignment.md)

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
# **find_port_vlan_assignments**
> PortVlanAssignmentList find_port_vlan_assignments(id, include=include)

List Current VLAN assignments for a port

Show the port's current VLAN assignments, including if this VLAN is set as native, and the current state of the assignment (ex. 'assigned' or 'unassigning')

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port_vlan_assignment_list import PortVlanAssignmentList
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    include = ["port","virtual_network"] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional) (default to ["port","virtual_network"])

    try:
        # List Current VLAN assignments for a port
        api_response = api_instance.find_port_vlan_assignments(id, include=include)
        print("The response of PortsApi->find_port_vlan_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->find_port_vlan_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] [default to [&quot;port&quot;,&quot;virtual_network&quot;]]

### Return type

[**PortVlanAssignmentList**](PortVlanAssignmentList.md)

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
# **unassign_port**
> Port unassign_port(id, port_assign_input, include=include)

Unassign a port

Unassign a port for a hardware.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.port import Port
from equinix_metal.models.port_assign_input import PortAssignInput
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
    api_instance = equinix_metal.PortsApi(api_client)
    id = 'id_example' # str | Port UUID
    port_assign_input = equinix_metal.PortAssignInput() # PortAssignInput | Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: '1001').
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Unassign a port
        api_response = api_instance.unassign_port(id, port_assign_input, include=include)
        print("The response of PortsApi->unassign_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->unassign_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Port UUID | 
 **port_assign_input** | [**PortAssignInput**](PortAssignInput.md)| Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: &#39;1001&#39;). | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**Port**](Port.md)

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
