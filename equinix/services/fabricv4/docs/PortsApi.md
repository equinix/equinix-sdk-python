# equinix.services.fabricv4.PortsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_to_lag**](PortsApi.md#add_to_lag) | **POST** /fabric/v4/ports/{portId}/physicalPorts/bulk | Add to Lag
[**create_bulk_port**](PortsApi.md#create_bulk_port) | **POST** /fabric/v4/ports/bulk | Create Port
[**create_port**](PortsApi.md#create_port) | **POST** /fabric/v4/ports | Create Port
[**delete_port**](PortsApi.md#delete_port) | **DELETE** /fabric/v4/ports/{portId} | Delete a single port
[**get_port_by_uuid**](PortsApi.md#get_port_by_uuid) | **GET** /fabric/v4/ports/{portId} | Get Port by uuid
[**get_ports**](PortsApi.md#get_ports) | **GET** /fabric/v4/ports | Get All Ports
[**get_vlans**](PortsApi.md#get_vlans) | **GET** /fabric/v4/ports/{portUuid}/linkProtocols | Get Vlans
[**search_ports**](PortsApi.md#search_ports) | **POST** /fabric/v4/ports/search | Search ports
[**update_port_by_uuid**](PortsApi.md#update_port_by_uuid) | **PATCH** /fabric/v4/ports/{portId} | Update by UUID


# **add_to_lag**
> AllPhysicalPortsResponse add_to_lag(port_id, bulk_physical_port)

Add to Lag

Add Physical Ports to Virtual Port.<font color="red"> <sup color='red'>Preview</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.all_physical_ports_response import AllPhysicalPortsResponse
from equinix.services.fabricv4.models.bulk_physical_port import BulkPhysicalPort
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
    api_instance = equinix.services.fabricv4.PortsApi(api_client)
    port_id = 'port_id_example' # str | Port UUID
    bulk_physical_port = equinix.services.fabricv4.BulkPhysicalPort() # BulkPhysicalPort | 

    try:
        # Add to Lag
        api_response = api_instance.add_to_lag(port_id, bulk_physical_port)
        print("The response of PortsApi->add_to_lag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->add_to_lag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_id** | **str**| Port UUID | 
 **bulk_physical_port** | [**BulkPhysicalPort**](BulkPhysicalPort.md)|  | 

### Return type

[**AllPhysicalPortsResponse**](AllPhysicalPortsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bulk_port**
> BulkPort create_bulk_port(bulk_port_request)

Create Port

Create Port creates Equinix Fabric? Port.<font color="red"> <sup color='red'>Preview</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.bulk_port import BulkPort
from equinix.services.fabricv4.models.bulk_port_request import BulkPortRequest
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
    api_instance = equinix.services.fabricv4.PortsApi(api_client)
    bulk_port_request = equinix.services.fabricv4.BulkPortRequest() # BulkPortRequest | 

    try:
        # Create Port
        api_response = api_instance.create_bulk_port(bulk_port_request)
        print("The response of PortsApi->create_bulk_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->create_bulk_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_port_request** | [**BulkPortRequest**](BulkPortRequest.md)|  | 

### Return type

[**BulkPort**](BulkPort.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation for COLO Bulk Port |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_port**
> Port create_port(port_request)

Create Port

Creates Equinix Fabric? Port.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.port import Port
from equinix.services.fabricv4.models.port_request import PortRequest
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
    api_instance = equinix.services.fabricv4.PortsApi(api_client)
    port_request = equinix.services.fabricv4.PortRequest() # PortRequest | 

    try:
        # Create Port
        api_response = api_instance.create_port(port_request)
        print("The response of PortsApi->create_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->create_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_request** | [**PortRequest**](PortRequest.md)|  | 

### Return type

[**Port**](Port.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation for COLO Single Port Non Lag |  -  |
**400** | Bad request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_port**
> Port delete_port(port_id)

Delete a single port

The API provides capability to delete a single port

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.port import Port
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
    api_instance = equinix.services.fabricv4.PortsApi(api_client)
    port_id = 'port_id_example' # str | Port UUID

    try:
        # Delete a single port
        api_response = api_instance.delete_port(port_id)
        print("The response of PortsApi->delete_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->delete_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_id** | **str**| Port UUID | 

### Return type

[**Port**](Port.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_by_uuid**
> Port get_port_by_uuid(port_id)

Get Port by uuid

Get Port By uuid returns details of assigned and available Equinix Fabric port for the specified user credentials. The metro code attribute in the response shows the origin of the proposed connection.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.port import Port
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
    api_instance = equinix.services.fabricv4.PortsApi(api_client)
    port_id = 'port_id_example' # str | Port UUID

    try:
        # Get Port by uuid
        api_response = api_instance.get_port_by_uuid(port_id)
        print("The response of PortsApi->get_port_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->get_port_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_id** | **str**| Port UUID | 

### Return type

[**Port**](Port.md)

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
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ports**
> AllPortsResponse get_ports(name=name)

Get All Ports

Get All Ports returns details of all assigned and available ports for the specified user credentials. The metro attribute in the response shows the origin of the proposed connection.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.all_ports_response import AllPortsResponse
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
    api_instance = equinix.services.fabricv4.PortsApi(api_client)
    name = 'name_example' # str | port name to be provided if specific port(s) to be retrieved (optional)

    try:
        # Get All Ports
        api_response = api_instance.get_ports(name=name)
        print("The response of PortsApi->get_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->get_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| port name to be provided if specific port(s) to be retrieved | [optional] 

### Return type

[**AllPortsResponse**](AllPortsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vlans**
> LinkProtocolGetResponse get_vlans(port_uuid)

Get Vlans

The API provides capability to retrieve Vlans for a Port.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.link_protocol_get_response import LinkProtocolGetResponse
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
    api_instance = equinix.services.fabricv4.PortsApi(api_client)
    port_uuid = 'port_uuid_example' # str | Port UUID

    try:
        # Get Vlans
        api_response = api_instance.get_vlans(port_uuid)
        print("The response of PortsApi->get_vlans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->get_vlans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_uuid** | **str**| Port UUID | 

### Return type

[**LinkProtocolGetResponse**](LinkProtocolGetResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Vlans |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ports**
> AllPortsResponse search_ports(port_v4_search_request)

Search ports

The API provides capability to get list of user's virtual ports using search criteria, including optional filtering, pagination and sorting

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.all_ports_response import AllPortsResponse
from equinix.services.fabricv4.models.port_v4_search_request import PortV4SearchRequest
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
    api_instance = equinix.services.fabricv4.PortsApi(api_client)
    port_v4_search_request = equinix.services.fabricv4.PortV4SearchRequest() # PortV4SearchRequest | 

    try:
        # Search ports
        api_response = api_instance.search_ports(port_v4_search_request)
        print("The response of PortsApi->search_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->search_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_v4_search_request** | [**PortV4SearchRequest**](PortV4SearchRequest.md)|  | 

### Return type

[**AllPortsResponse**](AllPortsResponse.md)

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_port_by_uuid**
> AllPortsResponse update_port_by_uuid(port_id, port_change_operation)

Update by UUID

Update Port by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.all_ports_response import AllPortsResponse
from equinix.services.fabricv4.models.port_change_operation import PortChangeOperation
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
    api_instance = equinix.services.fabricv4.PortsApi(api_client)
    port_id = 'port_id_example' # str | Port UUID
    port_change_operation = [equinix.services.fabricv4.PortChangeOperation()] # List[PortChangeOperation] | 

    try:
        # Update by UUID
        api_response = api_instance.update_port_by_uuid(port_id, port_change_operation)
        print("The response of PortsApi->update_port_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->update_port_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_id** | **str**| Port UUID | 
 **port_change_operation** | [**List[PortChangeOperation]**](PortChangeOperation.md)|  | 

### Return type

[**AllPortsResponse**](AllPortsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

