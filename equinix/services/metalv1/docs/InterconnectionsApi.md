# equinix_metal.InterconnectionsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_interconnection_port_virtual_circuit**](InterconnectionsApi.md#create_interconnection_port_virtual_circuit) | **POST** /connections/{connection_id}/ports/{port_id}/virtual-circuits | Create a new Virtual Circuit
[**create_organization_interconnection**](InterconnectionsApi.md#create_organization_interconnection) | **POST** /organizations/{organization_id}/connections | Request a new interconnection for the organization
[**create_project_interconnection**](InterconnectionsApi.md#create_project_interconnection) | **POST** /projects/{project_id}/connections | Request a new interconnection for the project&#39;s organization
[**delete_interconnection**](InterconnectionsApi.md#delete_interconnection) | **DELETE** /connections/{connection_id} | Delete interconnection
[**delete_virtual_circuit**](InterconnectionsApi.md#delete_virtual_circuit) | **DELETE** /virtual-circuits/{id} | Delete a virtual circuit
[**get_interconnection**](InterconnectionsApi.md#get_interconnection) | **GET** /connections/{connection_id} | Get interconnection
[**get_interconnection_metros**](InterconnectionsApi.md#get_interconnection_metros) | **GET** /connections/metros | Get connectivity to network provider by metro
[**get_interconnection_port**](InterconnectionsApi.md#get_interconnection_port) | **GET** /connections/{connection_id}/ports/{id} | Get a interconnection port
[**get_interconnection_pricing**](InterconnectionsApi.md#get_interconnection_pricing) | **GET** /connections/prices | Get Interconnection Pricing
[**get_virtual_circuit**](InterconnectionsApi.md#get_virtual_circuit) | **GET** /virtual-circuits/{id} | Get a virtual circuit
[**list_interconnection_port_virtual_circuits**](InterconnectionsApi.md#list_interconnection_port_virtual_circuits) | **GET** /connections/{connection_id}/ports/{port_id}/virtual-circuits | List a interconnection port&#39;s virtual circuits
[**list_interconnection_ports**](InterconnectionsApi.md#list_interconnection_ports) | **GET** /connections/{connection_id}/ports | List a interconnection&#39;s ports
[**list_interconnection_virtual_circuits**](InterconnectionsApi.md#list_interconnection_virtual_circuits) | **GET** /connections/{connection_id}/virtual-circuits | List a interconnection&#39;s virtual circuits
[**organization_list_interconnections**](InterconnectionsApi.md#organization_list_interconnections) | **GET** /organizations/{organization_id}/connections | List organization connections
[**project_list_interconnections**](InterconnectionsApi.md#project_list_interconnections) | **GET** /projects/{project_id}/connections | List project connections
[**project_list_interconnections_all_pages**](InterconnectionsApi.md#project_list_interconnections_all_pages) | **GET** /projects/{project_id}/connections | List project connections, fetches all the pages
[**update_interconnection**](InterconnectionsApi.md#update_interconnection) | **PUT** /connections/{connection_id} | Update interconnection
[**update_virtual_circuit**](InterconnectionsApi.md#update_virtual_circuit) | **PUT** /virtual-circuits/{id} | Update a virtual circuit


# **create_interconnection_port_virtual_circuit**
> VirtualCircuit create_interconnection_port_virtual_circuit(connection_id, port_id, virtual_circuit_create_input)

Create a new Virtual Circuit

Create a new Virtual Circuit on a Dedicated Port. To create a regular Virtual Circuit, specify a Virtual Network record and an NNI VLAN value. To create a VRF-based Virtual Circuit, specify the VRF ID and subnet, along with the NNI VLAN value.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.virtual_circuit import VirtualCircuit
from equinix_metal.models.virtual_circuit_create_input import VirtualCircuitCreateInput
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | UUID of the interconnection
    port_id = 'port_id_example' # str | UUID of the interconnection port
    virtual_circuit_create_input = equinix_metal.VirtualCircuitCreateInput() # VirtualCircuitCreateInput | Virtual Circuit details

    try:
        # Create a new Virtual Circuit
        api_response = api_instance.create_interconnection_port_virtual_circuit(connection_id, port_id, virtual_circuit_create_input)
        print("The response of InterconnectionsApi->create_interconnection_port_virtual_circuit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->create_interconnection_port_virtual_circuit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| UUID of the interconnection | 
 **port_id** | **str**| UUID of the interconnection port | 
 **virtual_circuit_create_input** | [**VirtualCircuitCreateInput**](VirtualCircuitCreateInput.md)| Virtual Circuit details | 

### Return type

[**VirtualCircuit**](VirtualCircuit.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **create_organization_interconnection**
> Interconnection create_organization_interconnection(organization_id, create_organization_interconnection_request, include=include, exclude=exclude)

Request a new interconnection for the organization

Creates a new interconnection request. A Project ID must be specified in the request body for connections on shared ports.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.create_organization_interconnection_request import CreateOrganizationInterconnectionRequest
from equinix_metal.models.interconnection import Interconnection
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    organization_id = 'organization_id_example' # str | UUID of the organization
    create_organization_interconnection_request = equinix_metal.CreateOrganizationInterconnectionRequest() # CreateOrganizationInterconnectionRequest | Dedicated port or shared interconnection (also known as Fabric VC) creation request.  Shared interconnections can be created with the following request types: * `VlanCSPConnectionCreateInput` creates a layer 2 interconnection directly to your Cloud Service Provider. * `SharedPortVCVlanCreateInput` creates a layer 2 interconnection that you can finish configuration in Fabric. For new connections, this type is preferred to `VlanFabricVCCreateInput`. * `VlanFabricVCCreateInput` creates a layer 2 interconnection that you can connect through Fabric with a service token. * `VrfFabricVCCreateInput` creates a layer 3 interconnection that you can connect through Fabric with a service token. 
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Request a new interconnection for the organization
        api_response = api_instance.create_organization_interconnection(organization_id, create_organization_interconnection_request, include=include, exclude=exclude)
        print("The response of InterconnectionsApi->create_organization_interconnection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->create_organization_interconnection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| UUID of the organization | 
 **create_organization_interconnection_request** | [**CreateOrganizationInterconnectionRequest**](CreateOrganizationInterconnectionRequest.md)| Dedicated port or shared interconnection (also known as Fabric VC) creation request.  Shared interconnections can be created with the following request types: * &#x60;VlanCSPConnectionCreateInput&#x60; creates a layer 2 interconnection directly to your Cloud Service Provider. * &#x60;SharedPortVCVlanCreateInput&#x60; creates a layer 2 interconnection that you can finish configuration in Fabric. For new connections, this type is preferred to &#x60;VlanFabricVCCreateInput&#x60;. * &#x60;VlanFabricVCCreateInput&#x60; creates a layer 2 interconnection that you can connect through Fabric with a service token. * &#x60;VrfFabricVCCreateInput&#x60; creates a layer 3 interconnection that you can connect through Fabric with a service token.  | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **create_project_interconnection**
> Interconnection create_project_interconnection(project_id, create_organization_interconnection_request, include=include, exclude=exclude)

Request a new interconnection for the project's organization

Creates a new interconnection request

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.create_organization_interconnection_request import CreateOrganizationInterconnectionRequest
from equinix_metal.models.interconnection import Interconnection
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    project_id = 'project_id_example' # str | UUID of the project
    create_organization_interconnection_request = equinix_metal.CreateOrganizationInterconnectionRequest() # CreateOrganizationInterconnectionRequest | Dedicated port or shared interconnection (also known as Fabric VC) creation request.  Shared interconnections can be created with the following request types: * `VlanCSPConnectionCreateInput` creates a layer 2 interconnection directly to your Cloud Service Provider. * `SharedPortVCVlanCreateInput` creates a layer 2 interconnection that you can finish configuration in Fabric. For new connections, this type is preferred to `VlanFabricVCCreateInput`. * `VlanFabricVCCreateInput` creates a layer 2 interconnection that you can connect through Fabric with a service token. * `VrfFabricVCCreateInput` creates a layer 3 interconnection that you can connect through Fabric with a service token. 
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Request a new interconnection for the project's organization
        api_response = api_instance.create_project_interconnection(project_id, create_organization_interconnection_request, include=include, exclude=exclude)
        print("The response of InterconnectionsApi->create_project_interconnection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->create_project_interconnection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| UUID of the project | 
 **create_organization_interconnection_request** | [**CreateOrganizationInterconnectionRequest**](CreateOrganizationInterconnectionRequest.md)| Dedicated port or shared interconnection (also known as Fabric VC) creation request.  Shared interconnections can be created with the following request types: * &#x60;VlanCSPConnectionCreateInput&#x60; creates a layer 2 interconnection directly to your Cloud Service Provider. * &#x60;SharedPortVCVlanCreateInput&#x60; creates a layer 2 interconnection that you can finish configuration in Fabric. For new connections, this type is preferred to &#x60;VlanFabricVCCreateInput&#x60;. * &#x60;VlanFabricVCCreateInput&#x60; creates a layer 2 interconnection that you can connect through Fabric with a service token. * &#x60;VrfFabricVCCreateInput&#x60; creates a layer 3 interconnection that you can connect through Fabric with a service token.  | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**403** | forbidden |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **delete_interconnection**
> Interconnection delete_interconnection(connection_id, include=include, exclude=exclude)

Delete interconnection

Delete a interconnection, its associated ports and virtual circuits.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.interconnection import Interconnection
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | Interconnection UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Delete interconnection
        api_response = api_instance.delete_interconnection(connection_id, include=include, exclude=exclude)
        print("The response of InterconnectionsApi->delete_interconnection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->delete_interconnection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Interconnection UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | accepted |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **delete_virtual_circuit**
> VirtualCircuit delete_virtual_circuit(id, include=include, exclude=exclude)

Delete a virtual circuit

Delete a virtual circuit from a Dedicated Port.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.virtual_circuit import VirtualCircuit
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    id = 'id_example' # str | Virtual Circuit UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Delete a virtual circuit
        api_response = api_instance.delete_virtual_circuit(id, include=include, exclude=exclude)
        print("The response of InterconnectionsApi->delete_virtual_circuit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->delete_virtual_circuit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Virtual Circuit UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**VirtualCircuit**](VirtualCircuit.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | accepted |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **get_interconnection**
> Interconnection get_interconnection(connection_id, include=include, exclude=exclude)

Get interconnection

Get the details of a interconnection

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.interconnection import Interconnection
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | Interconnection UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Get interconnection
        api_response = api_instance.get_interconnection(connection_id, include=include, exclude=exclude)
        print("The response of InterconnectionsApi->get_interconnection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->get_interconnection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Interconnection UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**Interconnection**](Interconnection.md)

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
# **get_interconnection_metros**
> InterconnectionMetroList get_interconnection_metros()

Get connectivity to network provider by metro

Displays which providers you can connect to directly from Equinix Metal Metros.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.interconnection_metro_list import InterconnectionMetroList
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)

    try:
        # Get connectivity to network provider by metro
        api_response = api_instance.get_interconnection_metros()
        print("The response of InterconnectionsApi->get_interconnection_metros:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->get_interconnection_metros: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InterconnectionMetroList**](InterconnectionMetroList.md)

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
# **get_interconnection_port**
> InterconnectionPort get_interconnection_port(connection_id, id, include=include, exclude=exclude)

Get a interconnection port

Get the details of an interconnection port.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.interconnection_port import InterconnectionPort
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | UUID of the interconnection
    id = 'id_example' # str | Port UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Get a interconnection port
        api_response = api_instance.get_interconnection_port(connection_id, id, include=include, exclude=exclude)
        print("The response of InterconnectionsApi->get_interconnection_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->get_interconnection_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| UUID of the interconnection | 
 **id** | **str**| Port UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**InterconnectionPort**](InterconnectionPort.md)

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
# **get_interconnection_pricing**
> InterconnectionPricingList get_interconnection_pricing()

Get Interconnection Pricing

Displays pricing information for connecting to networks outside of Equinix.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.interconnection_pricing_list import InterconnectionPricingList
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)

    try:
        # Get Interconnection Pricing
        api_response = api_instance.get_interconnection_pricing()
        print("The response of InterconnectionsApi->get_interconnection_pricing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->get_interconnection_pricing: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InterconnectionPricingList**](InterconnectionPricingList.md)

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
# **get_virtual_circuit**
> VirtualCircuit get_virtual_circuit(id, include=include, exclude=exclude)

Get a virtual circuit

Get the details of a virtual circuit

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.virtual_circuit import VirtualCircuit
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    id = 'id_example' # str | Virtual Circuit UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Get a virtual circuit
        api_response = api_instance.get_virtual_circuit(id, include=include, exclude=exclude)
        print("The response of InterconnectionsApi->get_virtual_circuit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->get_virtual_circuit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Virtual Circuit UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**VirtualCircuit**](VirtualCircuit.md)

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
# **list_interconnection_port_virtual_circuits**
> VirtualCircuitList list_interconnection_port_virtual_circuits(connection_id, port_id, include=include, exclude=exclude)

List a interconnection port's virtual circuits

List the virtual circuit record(s) associatiated with a particular interconnection port.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.virtual_circuit_list import VirtualCircuitList
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | UUID of the interconnection
    port_id = 'port_id_example' # str | UUID of the interconnection port
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # List a interconnection port's virtual circuits
        api_response = api_instance.list_interconnection_port_virtual_circuits(connection_id, port_id, include=include, exclude=exclude)
        print("The response of InterconnectionsApi->list_interconnection_port_virtual_circuits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->list_interconnection_port_virtual_circuits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| UUID of the interconnection | 
 **port_id** | **str**| UUID of the interconnection port | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**VirtualCircuitList**](VirtualCircuitList.md)

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
# **list_interconnection_ports**
> InterconnectionPortList list_interconnection_ports(connection_id)

List a interconnection's ports

List the ports associated to an interconnection.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.interconnection_port_list import InterconnectionPortList
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | UUID of the interconnection

    try:
        # List a interconnection's ports
        api_response = api_instance.list_interconnection_ports(connection_id)
        print("The response of InterconnectionsApi->list_interconnection_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->list_interconnection_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| UUID of the interconnection | 

### Return type

[**InterconnectionPortList**](InterconnectionPortList.md)

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
# **list_interconnection_virtual_circuits**
> VirtualCircuitList list_interconnection_virtual_circuits(connection_id)

List a interconnection's virtual circuits

List the virtual circuit record(s) associated with a particular interconnection id.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.virtual_circuit_list import VirtualCircuitList
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | UUID of the interconnection

    try:
        # List a interconnection's virtual circuits
        api_response = api_instance.list_interconnection_virtual_circuits(connection_id)
        print("The response of InterconnectionsApi->list_interconnection_virtual_circuits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->list_interconnection_virtual_circuits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| UUID of the interconnection | 

### Return type

[**VirtualCircuitList**](VirtualCircuitList.md)

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
# **organization_list_interconnections**
> InterconnectionList organization_list_interconnections(organization_id, include=include, exclude=exclude)

List organization connections

List the connections belonging to the organization

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.interconnection_list import InterconnectionList
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    organization_id = 'organization_id_example' # str | UUID of the organization
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # List organization connections
        api_response = api_instance.organization_list_interconnections(organization_id, include=include, exclude=exclude)
        print("The response of InterconnectionsApi->organization_list_interconnections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->organization_list_interconnections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| UUID of the organization | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**InterconnectionList**](InterconnectionList.md)

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
# **project_list_interconnections**
> InterconnectionList project_list_interconnections(project_id, include=include, exclude=exclude, page=page, per_page=per_page)

List project connections

List the connections belonging to the project

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.interconnection_list import InterconnectionList
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    project_id = 'project_id_example' # str | UUID of the project
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
    page = 1 # int | Page to return (optional) (default to 1)
    per_page = 10 # int | Items returned per page (optional) (default to 10)

    try:
        # List project connections
        api_response = api_instance.project_list_interconnections(project_id, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of InterconnectionsApi->project_list_interconnections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->project_list_interconnections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| UUID of the project | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **page** | **int**| Page to return | [optional] [default to 1]
 **per_page** | **int**| Items returned per page | [optional] [default to 10]

### Return type

[**InterconnectionList**](InterconnectionList.md)

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
# **project_list_interconnections_all_pages**
> InterconnectionList project_list_interconnections_all_pages(project_id, include=include, exclude=exclude, per_page=per_page)
Just like [**project_list_interconnections**](InterconnectionsApi.md#project_list_interconnections) but fetches resources from all pages. This method doesn't take `page` parameter. Other parameters, return type and other characteristics are the same as in [**project_list_interconnections**](InterconnectionsApi.md#project_list_interconnections).
# **update_interconnection**
> Interconnection update_interconnection(connection_id, interconnection_update_input, include=include, exclude=exclude)

Update interconnection

Update the details of a interconnection

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.interconnection import Interconnection
from equinix_metal.models.interconnection_update_input import InterconnectionUpdateInput
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | Interconnection UUID
    interconnection_update_input = equinix_metal.InterconnectionUpdateInput() # InterconnectionUpdateInput | Updated interconnection details
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Update interconnection
        api_response = api_instance.update_interconnection(connection_id, interconnection_update_input, include=include, exclude=exclude)
        print("The response of InterconnectionsApi->update_interconnection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->update_interconnection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Interconnection UUID | 
 **interconnection_update_input** | [**InterconnectionUpdateInput**](InterconnectionUpdateInput.md)| Updated interconnection details | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **update_virtual_circuit**
> VirtualCircuit update_virtual_circuit(id, virtual_circuit_update_input, include=include, exclude=exclude)

Update a virtual circuit

Update the details of a virtual circuit.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.virtual_circuit import VirtualCircuit
from equinix_metal.models.virtual_circuit_update_input import VirtualCircuitUpdateInput
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
    api_instance = equinix_metal.InterconnectionsApi(api_client)
    id = 'id_example' # str | Virtual Circuit UUID
    virtual_circuit_update_input = equinix_metal.VirtualCircuitUpdateInput() # VirtualCircuitUpdateInput | Updated Virtual Circuit details
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Update a virtual circuit
        api_response = api_instance.update_virtual_circuit(id, virtual_circuit_update_input, include=include, exclude=exclude)
        print("The response of InterconnectionsApi->update_virtual_circuit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterconnectionsApi->update_virtual_circuit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Virtual Circuit UUID | 
 **virtual_circuit_update_input** | [**VirtualCircuitUpdateInput**](VirtualCircuitUpdateInput.md)| Updated Virtual Circuit details | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**VirtualCircuit**](VirtualCircuit.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**202** | accepted |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
