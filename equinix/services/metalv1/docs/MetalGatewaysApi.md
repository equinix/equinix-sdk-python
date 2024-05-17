# equinix_metal.MetalGatewaysApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metal_gateway**](MetalGatewaysApi.md#create_metal_gateway) | **POST** /projects/{project_id}/metal-gateways | Create a metal gateway
[**create_metal_gateway_elastic_ip**](MetalGatewaysApi.md#create_metal_gateway_elastic_ip) | **POST** /metal-gateways/{id}/ips | Create a Metal Gateway Elastic IP
[**delete_metal_gateway**](MetalGatewaysApi.md#delete_metal_gateway) | **DELETE** /metal-gateways/{id} | Deletes the metal gateway
[**find_metal_gateway_by_id**](MetalGatewaysApi.md#find_metal_gateway_by_id) | **GET** /metal-gateways/{id} | Returns the metal gateway
[**find_metal_gateways_by_project**](MetalGatewaysApi.md#find_metal_gateways_by_project) | **GET** /projects/{project_id}/metal-gateways | Returns all metal gateways for a project
[**find_metal_gateways_by_project_all_pages**](MetalGatewaysApi.md#find_metal_gateways_by_project_all_pages) | **GET** /projects/{project_id}/metal-gateways | Returns all metal gateways for a project, fetches all the pages
[**get_metal_gateway_elastic_ips**](MetalGatewaysApi.md#get_metal_gateway_elastic_ips) | **GET** /metal-gateways/{id}/ips | List Metal Gateway Elastic IPs


# **create_metal_gateway**
> FindMetalGatewayById200Response create_metal_gateway(project_id, create_metal_gateway_request, include=include, exclude=exclude, page=page, per_page=per_page)

Create a metal gateway

Create a metal gateway in a project

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.create_metal_gateway_request import CreateMetalGatewayRequest
from equinix_metal.models.find_metal_gateway_by_id200_response import FindMetalGatewayById200Response
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
    api_instance = equinix_metal.MetalGatewaysApi(api_client)
    project_id = 'project_id_example' # str | Project UUID
    create_metal_gateway_request = equinix_metal.CreateMetalGatewayRequest() # CreateMetalGatewayRequest | Metal Gateway to create
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
    page = 1 # int | Page to return (optional) (default to 1)
    per_page = 10 # int | Items returned per page (optional) (default to 10)

    try:
        # Create a metal gateway
        api_response = api_instance.create_metal_gateway(project_id, create_metal_gateway_request, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of MetalGatewaysApi->create_metal_gateway:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetalGatewaysApi->create_metal_gateway: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project UUID | 
 **create_metal_gateway_request** | [**CreateMetalGatewayRequest**](CreateMetalGatewayRequest.md)| Metal Gateway to create | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **page** | **int**| Page to return | [optional] [default to 1]
 **per_page** | **int**| Items returned per page | [optional] [default to 10]

### Return type

[**FindMetalGatewayById200Response**](FindMetalGatewayById200Response.md)

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
# **create_metal_gateway_elastic_ip**
> IPAssignment create_metal_gateway_elastic_ip(id, metal_gateway_elastic_ip_create_input, include=include, exclude=exclude)

Create a Metal Gateway Elastic IP

Create a new Elastic IP on this Metal Gateway.  Assign an IPv4 range as an elastic IP to the Metal Gateway, with a specified next-hop address contained within the Metal Gateway.  Notice: Elastic IPs on Metal Gateways are a test feature currently under active development, and only available to certain users. Please contact Customer Success for more information. 

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.ip_assignment import IPAssignment
from equinix_metal.models.metal_gateway_elastic_ip_create_input import MetalGatewayElasticIpCreateInput
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
    api_instance = equinix_metal.MetalGatewaysApi(api_client)
    id = 'id_example' # str | Metal Gateway UUID
    metal_gateway_elastic_ip_create_input = equinix_metal.MetalGatewayElasticIpCreateInput() # MetalGatewayElasticIpCreateInput | 
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Create a Metal Gateway Elastic IP
        api_response = api_instance.create_metal_gateway_elastic_ip(id, metal_gateway_elastic_ip_create_input, include=include, exclude=exclude)
        print("The response of MetalGatewaysApi->create_metal_gateway_elastic_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetalGatewaysApi->create_metal_gateway_elastic_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Metal Gateway UUID | 
 **metal_gateway_elastic_ip_create_input** | [**MetalGatewayElasticIpCreateInput**](MetalGatewayElasticIpCreateInput.md)|  | 
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
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **delete_metal_gateway**
> FindMetalGatewayById200Response delete_metal_gateway(id, include=include, exclude=exclude)

Deletes the metal gateway

Deletes a metal gateway and any elastic IP assignments associated with this metal gateway.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.find_metal_gateway_by_id200_response import FindMetalGatewayById200Response
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
    api_instance = equinix_metal.MetalGatewaysApi(api_client)
    id = 'id_example' # str | Metal Gateway UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Deletes the metal gateway
        api_response = api_instance.delete_metal_gateway(id, include=include, exclude=exclude)
        print("The response of MetalGatewaysApi->delete_metal_gateway:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetalGatewaysApi->delete_metal_gateway: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Metal Gateway UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**FindMetalGatewayById200Response**](FindMetalGatewayById200Response.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | accepted |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_metal_gateway_by_id**
> FindMetalGatewayById200Response find_metal_gateway_by_id(id, include=include, exclude=exclude)

Returns the metal gateway

Returns a specific metal gateway

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.find_metal_gateway_by_id200_response import FindMetalGatewayById200Response
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
    api_instance = equinix_metal.MetalGatewaysApi(api_client)
    id = 'id_example' # str | Metal Gateway UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Returns the metal gateway
        api_response = api_instance.find_metal_gateway_by_id(id, include=include, exclude=exclude)
        print("The response of MetalGatewaysApi->find_metal_gateway_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetalGatewaysApi->find_metal_gateway_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Metal Gateway UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**FindMetalGatewayById200Response**](FindMetalGatewayById200Response.md)

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
# **find_metal_gateways_by_project**
> MetalGatewayList find_metal_gateways_by_project(project_id, include=include, exclude=exclude, page=page, per_page=per_page)

Returns all metal gateways for a project

Return all metal gateways for a project

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.metal_gateway_list import MetalGatewayList
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
    api_instance = equinix_metal.MetalGatewaysApi(api_client)
    project_id = 'project_id_example' # str | Project UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
    page = 1 # int | Page to return (optional) (default to 1)
    per_page = 10 # int | Items returned per page (optional) (default to 10)

    try:
        # Returns all metal gateways for a project
        api_response = api_instance.find_metal_gateways_by_project(project_id, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of MetalGatewaysApi->find_metal_gateways_by_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetalGatewaysApi->find_metal_gateways_by_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **page** | **int**| Page to return | [optional] [default to 1]
 **per_page** | **int**| Items returned per page | [optional] [default to 10]

### Return type

[**MetalGatewayList**](MetalGatewayList.md)

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
# **find_metal_gateways_by_project_all_pages**
> MetalGatewayList find_metal_gateways_by_project_all_pages(project_id, include=include, exclude=exclude, per_page=per_page)
Just like [**find_metal_gateways_by_project**](MetalGatewaysApi.md#find_metal_gateways_by_project) but fetches resources from all pages. This method doesn't take `page` parameter. Other parameters, return type and other characteristics are the same as in [**find_metal_gateways_by_project**](MetalGatewaysApi.md#find_metal_gateways_by_project).
# **get_metal_gateway_elastic_ips**
> IPAssignmentList get_metal_gateway_elastic_ips(id, include=include, exclude=exclude)

List Metal Gateway Elastic IPs

Returns the list of Elastic IPs assigned to this Metal Gateway

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
    api_instance = equinix_metal.MetalGatewaysApi(api_client)
    id = 'id_example' # str | Metal Gateway UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # List Metal Gateway Elastic IPs
        api_response = api_instance.get_metal_gateway_elastic_ips(id, include=include, exclude=exclude)
        print("The response of MetalGatewaysApi->get_metal_gateway_elastic_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetalGatewaysApi->get_metal_gateway_elastic_ips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Metal Gateway UUID | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
