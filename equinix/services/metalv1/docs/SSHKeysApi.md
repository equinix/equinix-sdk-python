# equinix_metal.SSHKeysApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_ssh_key**](SSHKeysApi.md#create_project_ssh_key) | **POST** /projects/{id}/ssh-keys | Create a ssh key for the given project
[**create_ssh_key**](SSHKeysApi.md#create_ssh_key) | **POST** /ssh-keys | Create a ssh key for the current user
[**delete_ssh_key**](SSHKeysApi.md#delete_ssh_key) | **DELETE** /ssh-keys/{id} | Delete the ssh key
[**find_device_ssh_keys**](SSHKeysApi.md#find_device_ssh_keys) | **GET** /devices/{id}/ssh-keys | Retrieve a device&#39;s ssh keys
[**find_project_ssh_keys**](SSHKeysApi.md#find_project_ssh_keys) | **GET** /projects/{id}/ssh-keys | Retrieve a project&#39;s ssh keys
[**find_ssh_key_by_id**](SSHKeysApi.md#find_ssh_key_by_id) | **GET** /ssh-keys/{id} | Retrieve a ssh key
[**find_ssh_keys**](SSHKeysApi.md#find_ssh_keys) | **GET** /ssh-keys | Retrieve all ssh keys
[**update_ssh_key**](SSHKeysApi.md#update_ssh_key) | **PUT** /ssh-keys/{id} | Update the ssh key


# **create_project_ssh_key**
> SSHKey create_project_ssh_key(id, ssh_key_create_input, include=include)

Create a ssh key for the given project

Creates a ssh key.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.ssh_key import SSHKey
from equinix_metal.models.ssh_key_create_input import SSHKeyCreateInput
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
    api_instance = equinix_metal.SSHKeysApi(api_client)
    id = 'id_example' # str | Project UUID
    ssh_key_create_input = equinix_metal.SSHKeyCreateInput() # SSHKeyCreateInput | ssh key to create
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Create a ssh key for the given project
        api_response = api_instance.create_project_ssh_key(id, ssh_key_create_input, include=include)
        print("The response of SSHKeysApi->create_project_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHKeysApi->create_project_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **ssh_key_create_input** | [**SSHKeyCreateInput**](SSHKeyCreateInput.md)| ssh key to create | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**SSHKey**](SSHKey.md)

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
# **create_ssh_key**
> SSHKey create_ssh_key(ssh_key_create_input, include=include)

Create a ssh key for the current user

Creates a ssh key.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.ssh_key import SSHKey
from equinix_metal.models.ssh_key_create_input import SSHKeyCreateInput
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
    api_instance = equinix_metal.SSHKeysApi(api_client)
    ssh_key_create_input = equinix_metal.SSHKeyCreateInput() # SSHKeyCreateInput | ssh key to create
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Create a ssh key for the current user
        api_response = api_instance.create_ssh_key(ssh_key_create_input, include=include)
        print("The response of SSHKeysApi->create_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHKeysApi->create_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_create_input** | [**SSHKeyCreateInput**](SSHKeyCreateInput.md)| ssh key to create | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**SSHKey**](SSHKey.md)

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
# **delete_ssh_key**
> delete_ssh_key(id)

Delete the ssh key

Deletes the ssh key.

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
    api_instance = equinix_metal.SSHKeysApi(api_client)
    id = 'id_example' # str | ssh key UUID

    try:
        # Delete the ssh key
        api_instance.delete_ssh_key(id)
    except Exception as e:
        print("Exception when calling SSHKeysApi->delete_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ssh key UUID | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_device_ssh_keys**
> SSHKeyList find_device_ssh_keys(id, search_string=search_string, include=include)

Retrieve a device's ssh keys

Returns a collection of the device's ssh keys.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.ssh_key_list import SSHKeyList
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
    api_instance = equinix_metal.SSHKeysApi(api_client)
    id = 'id_example' # str | Project UUID
    search_string = 'search_string_example' # str | Search by key, label, or fingerprint (optional)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Retrieve a device's ssh keys
        api_response = api_instance.find_device_ssh_keys(id, search_string=search_string, include=include)
        print("The response of SSHKeysApi->find_device_ssh_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHKeysApi->find_device_ssh_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **search_string** | **str**| Search by key, label, or fingerprint | [optional] 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**SSHKeyList**](SSHKeyList.md)

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
# **find_project_ssh_keys**
> SSHKeyList find_project_ssh_keys(id, query=query, include=include)

Retrieve a project's ssh keys

Returns a collection of the project's ssh keys.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.ssh_key_list import SSHKeyList
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
    api_instance = equinix_metal.SSHKeysApi(api_client)
    id = 'id_example' # str | Project UUID
    query = 'query_example' # str | Search by key, label, or fingerprint (optional)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Retrieve a project's ssh keys
        api_response = api_instance.find_project_ssh_keys(id, query=query, include=include)
        print("The response of SSHKeysApi->find_project_ssh_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHKeysApi->find_project_ssh_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **query** | **str**| Search by key, label, or fingerprint | [optional] 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**SSHKeyList**](SSHKeyList.md)

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
# **find_ssh_key_by_id**
> SSHKey find_ssh_key_by_id(id, include=include)

Retrieve a ssh key

Returns a single ssh key if the user has access

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.ssh_key import SSHKey
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
    api_instance = equinix_metal.SSHKeysApi(api_client)
    id = 'id_example' # str | SSH Key UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Retrieve a ssh key
        api_response = api_instance.find_ssh_key_by_id(id, include=include)
        print("The response of SSHKeysApi->find_ssh_key_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHKeysApi->find_ssh_key_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SSH Key UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**SSHKey**](SSHKey.md)

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
# **find_ssh_keys**
> SSHKeyList find_ssh_keys(search=search, include=include)

Retrieve all ssh keys

Returns a collection of the user’s ssh keys.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.ssh_key_list import SSHKeyList
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
    api_instance = equinix_metal.SSHKeysApi(api_client)
    search = 'search_example' # str | Search by key, label, or fingerprint (optional)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Retrieve all ssh keys
        api_response = api_instance.find_ssh_keys(search=search, include=include)
        print("The response of SSHKeysApi->find_ssh_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHKeysApi->find_ssh_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search by key, label, or fingerprint | [optional] 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**SSHKeyList**](SSHKeyList.md)

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
# **update_ssh_key**
> SSHKey update_ssh_key(id, ssh_key_input, include=include)

Update the ssh key

Updates the ssh key.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.ssh_key import SSHKey
from equinix_metal.models.ssh_key_input import SSHKeyInput
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
    api_instance = equinix_metal.SSHKeysApi(api_client)
    id = 'id_example' # str | SSH Key UUID
    ssh_key_input = equinix_metal.SSHKeyInput() # SSHKeyInput | ssh key to update
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)

    try:
        # Update the ssh key
        api_response = api_instance.update_ssh_key(id, ssh_key_input, include=include)
        print("The response of SSHKeysApi->update_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHKeysApi->update_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SSH Key UUID | 
 **ssh_key_input** | [**SSHKeyInput**](SSHKeyInput.md)| ssh key to update | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 

### Return type

[**SSHKey**](SSHKey.md)

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
