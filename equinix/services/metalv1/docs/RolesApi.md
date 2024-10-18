# equinix.services.metalv1.RolesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_role**](RolesApi.md#get_organization_role) | **GET** /organizations/{id}/roles/{role_id} | Get details about a specific role
[**list_organization_roles**](RolesApi.md#list_organization_roles) | **GET** /organizations/{id}/roles | List available roles


# **get_organization_role**
> Role get_organization_role(id, role_id)

Get details about a specific role

Learn what actions are in each role.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix.services.metalv1
from equinix.services.metalv1.models.role import Role
from equinix.services.metalv1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix.services.metalv1.Configuration(
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
with equinix.services.metalv1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix.services.metalv1.RolesApi(api_client)
    id = 'id_example' # str | Organization UUID
    role_id = 'role_id_example' # str | Role ID

    try:
        # Get details about a specific role
        api_response = api_instance.get_organization_role(id, role_id)
        print("The response of RolesApi->get_organization_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_organization_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization UUID | 
 **role_id** | **str**| Role ID | 

### Return type

[**Role**](Role.md)

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
# **list_organization_roles**
> RoleList list_organization_roles(id)

List available roles

This list of roles can be used to update Members or new Invitations with additional permissions.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix.services.metalv1
from equinix.services.metalv1.models.role_list import RoleList
from equinix.services.metalv1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix.services.metalv1.Configuration(
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
with equinix.services.metalv1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix.services.metalv1.RolesApi(api_client)
    id = 'id_example' # str | Organization UUID

    try:
        # List available roles
        api_response = api_instance.list_organization_roles(id)
        print("The response of RolesApi->list_organization_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->list_organization_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization UUID | 

### Return type

[**RoleList**](RoleList.md)

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
