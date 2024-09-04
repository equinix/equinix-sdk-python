# equinix_metal.UsersApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users | Create a user
[**find_current_user**](UsersApi.md#find_current_user) | **GET** /user | Retrieve the current user
[**find_invitations**](UsersApi.md#find_invitations) | **GET** /invitations | Retrieve current user invitations
[**find_user_by_id**](UsersApi.md#find_user_by_id) | **GET** /users/{id} | Retrieve a user
[**find_user_customdata**](UsersApi.md#find_user_customdata) | **GET** /users/{id}/customdata | Retrieve the custom metadata of a user
[**find_users**](UsersApi.md#find_users) | **GET** /users | Retrieve all users
[**find_users_all_pages**](UsersApi.md#find_users_all_pages) | **GET** /users | Retrieve all users, fetches all the pages
[**update_current_user**](UsersApi.md#update_current_user) | **PUT** /user | Update the current user


# **create_user**
> create_user(user_create_input, include=include, exclude=exclude)

Create a user

Creates a user.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.user_create_input import UserCreateInput
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
    api_instance = equinix_metal.UsersApi(api_client)
    user_create_input = equinix_metal.UserCreateInput() # UserCreateInput | User to create
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Create a user
        api_instance.create_user(user_create_input, include=include, exclude=exclude)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_input** | [**UserCreateInput**](UserCreateInput.md)| User to create | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

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
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_current_user**
> User find_current_user(include=include, exclude=exclude)

Retrieve the current user

Returns the user object for the currently logged-in user.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.user import User
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
    api_instance = equinix_metal.UsersApi(api_client)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve the current user
        api_response = api_instance.find_current_user(include=include, exclude=exclude)
        print("The response of UsersApi->find_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->find_current_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**User**](User.md)

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
# **find_invitations**
> InvitationList find_invitations(include=include, page=page, per_page=per_page)

Retrieve current user invitations

Returns all invitations in current user.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.invitation_list import InvitationList
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
    api_instance = equinix_metal.UsersApi(api_client)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    page = 1 # int | Page to return (optional) (default to 1)
    per_page = 10 # int | Items returned per page (optional) (default to 10)

    try:
        # Retrieve current user invitations
        api_response = api_instance.find_invitations(include=include, page=page, per_page=per_page)
        print("The response of UsersApi->find_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->find_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **page** | **int**| Page to return | [optional] [default to 1]
 **per_page** | **int**| Items returned per page | [optional] [default to 10]

### Return type

[**InvitationList**](InvitationList.md)

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
# **find_user_by_id**
> User find_user_by_id(id, include=include, exclude=exclude)

Retrieve a user

Returns a single user if the user has access

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.user import User
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
    api_instance = equinix_metal.UsersApi(api_client)
    id = 'id_example' # str | User UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve a user
        api_response = api_instance.find_user_by_id(id, include=include, exclude=exclude)
        print("The response of UsersApi->find_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->find_user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**User**](User.md)

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
# **find_user_customdata**
> find_user_customdata(id)

Retrieve the custom metadata of a user

Provides the custom metadata stored for this user in json format

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
    api_instance = equinix_metal.UsersApi(api_client)
    id = 'id_example' # str | User UUID

    try:
        # Retrieve the custom metadata of a user
        api_instance.find_user_customdata(id)
    except Exception as e:
        print("Exception when calling UsersApi->find_user_customdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User UUID | 

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
# **find_users**
> UserList find_users(include=include, exclude=exclude, page=page, per_page=per_page)

Retrieve all users

Returns a list of users that the are accessible to the current user (all users in the current user’s projects, essentially).

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.user_list import UserList
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
    api_instance = equinix_metal.UsersApi(api_client)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
    page = 1 # int | Page to return (optional) (default to 1)
    per_page = 10 # int | Items returned per page (optional) (default to 10)

    try:
        # Retrieve all users
        api_response = api_instance.find_users(include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of UsersApi->find_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->find_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **page** | **int**| Page to return | [optional] [default to 1]
 **per_page** | **int**| Items returned per page | [optional] [default to 10]

### Return type

[**UserList**](UserList.md)

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
# **find_users_all_pages**
> UserList find_users_all_pages(include=include, exclude=exclude, per_page=per_page)
Just like [**find_users**](UsersApi.md#find_users) but fetches resources from all pages. This method doesn't take `page` parameter. Other parameters, return type and other characteristics are the same as in [**find_users**](UsersApi.md#find_users).
# **update_current_user**
> User update_current_user(user_update_input, include=include, exclude=exclude)

Update the current user

Updates the currently logged-in user.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.user import User
from equinix_metal.models.user_update_input import UserUpdateInput
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
    api_instance = equinix_metal.UsersApi(api_client)
    user_update_input = equinix_metal.UserUpdateInput() # UserUpdateInput | User to update
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Update the current user
        api_response = api_instance.update_current_user(user_update_input, include=include, exclude=exclude)
        print("The response of UsersApi->update_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_current_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_update_input** | [**UserUpdateInput**](UserUpdateInput.md)| User to update | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**User**](User.md)

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
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
