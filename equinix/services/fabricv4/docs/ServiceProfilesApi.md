# equinix.services.fabricv4.ServiceProfilesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_profile**](ServiceProfilesApi.md#create_service_profile) | **POST** /fabric/v4/serviceProfiles | Create Profile
[**delete_service_profile_by_uuid**](ServiceProfilesApi.md#delete_service_profile_by_uuid) | **DELETE** /fabric/v4/serviceProfiles/{serviceProfileId} | Delete Profile
[**get_service_profile_by_uuid**](ServiceProfilesApi.md#get_service_profile_by_uuid) | **GET** /fabric/v4/serviceProfiles/{serviceProfileId} | Get Profile
[**get_service_profile_metros_by_uuid**](ServiceProfilesApi.md#get_service_profile_metros_by_uuid) | **GET** /fabric/v4/serviceProfiles/{serviceProfileId}/metros | Get Profile Metros
[**get_service_profiles**](ServiceProfilesApi.md#get_service_profiles) | **GET** /fabric/v4/serviceProfiles | Get all Profiles
[**put_service_profile_by_uuid**](ServiceProfilesApi.md#put_service_profile_by_uuid) | **PUT** /fabric/v4/serviceProfiles/{serviceProfileId} | Replace Profile
[**search_service_profiles**](ServiceProfilesApi.md#search_service_profiles) | **POST** /fabric/v4/serviceProfiles/search | Profile Search
[**update_service_profile_by_uuid**](ServiceProfilesApi.md#update_service_profile_by_uuid) | **PATCH** /fabric/v4/serviceProfiles/{serviceProfileId} | Update Profile


# **create_service_profile**
> ServiceProfile create_service_profile(service_profile_request)

Create Profile

Create Service Profile creates Equinix Fabric? Service Profile.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.service_profile import ServiceProfile
from equinix.services.fabricv4.models.service_profile_request import ServiceProfileRequest
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
    api_instance = equinix.services.fabricv4.ServiceProfilesApi(api_client)
    service_profile_request = equinix.services.fabricv4.ServiceProfileRequest() # ServiceProfileRequest | 

    try:
        # Create Profile
        api_response = api_instance.create_service_profile(service_profile_request)
        print("The response of ServiceProfilesApi->create_service_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceProfilesApi->create_service_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_profile_request** | [**ServiceProfileRequest**](ServiceProfileRequest.md)|  | 

### Return type

[**ServiceProfile**](ServiceProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=UTF-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Create operation |  * ETag -  <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_profile_by_uuid**
> ServiceProfile delete_service_profile_by_uuid(service_profile_id)

Delete Profile

delete Service Profile by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.service_profile import ServiceProfile
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
    api_instance = equinix.services.fabricv4.ServiceProfilesApi(api_client)
    service_profile_id = 'service_profile_id_example' # str | Service Profile UUID

    try:
        # Delete Profile
        api_response = api_instance.delete_service_profile_by_uuid(service_profile_id)
        print("The response of ServiceProfilesApi->delete_service_profile_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceProfilesApi->delete_service_profile_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_profile_id** | **str**| Service Profile UUID | 

### Return type

[**ServiceProfile**](ServiceProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Delete operation |  * ETag -  <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_profile_by_uuid**
> ServiceProfile get_service_profile_by_uuid(service_profile_id, view_point=view_point)

Get Profile

Get service profile by UUID. View Point parameter if set to zSide will give seller's view of the profile otherwise buyer's view.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_service_profiles_view_point_parameter import GetServiceProfilesViewPointParameter
from equinix.services.fabricv4.models.service_profile import ServiceProfile
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
    api_instance = equinix.services.fabricv4.ServiceProfilesApi(api_client)
    service_profile_id = 'service_profile_id_example' # str | Service Profile UUID
    view_point = aSide # GetServiceProfilesViewPointParameter | flips view between buyer and seller representation (optional) (default to aSide)

    try:
        # Get Profile
        api_response = api_instance.get_service_profile_by_uuid(service_profile_id, view_point=view_point)
        print("The response of ServiceProfilesApi->get_service_profile_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceProfilesApi->get_service_profile_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_profile_id** | **str**| Service Profile UUID | 
 **view_point** | [**GetServiceProfilesViewPointParameter**](.md)| flips view between buyer and seller representation | [optional] [default to aSide]

### Return type

[**ServiceProfile**](ServiceProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * ETag -  <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_profile_metros_by_uuid**
> ServiceMetros get_service_profile_metros_by_uuid(service_profile_id, offset=offset, limit=limit)

Get Profile Metros

Get service profile metros by UUID.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.service_metros import ServiceMetros
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
    api_instance = equinix.services.fabricv4.ServiceProfilesApi(api_client)
    service_profile_id = 'service_profile_id_example' # str | Service Profile UUID
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get Profile Metros
        api_response = api_instance.get_service_profile_metros_by_uuid(service_profile_id, offset=offset, limit=limit)
        print("The response of ServiceProfilesApi->get_service_profile_metros_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceProfilesApi->get_service_profile_metros_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_profile_id** | **str**| Service Profile UUID | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**ServiceMetros**](ServiceMetros.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_profiles**
> ServiceProfiles get_service_profiles(offset=offset, limit=limit, view_point=view_point)

Get all Profiles

The API request returns all Equinix Fabric Service Profiles in accordance with the view point requested.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_service_profiles_view_point_parameter import GetServiceProfilesViewPointParameter
from equinix.services.fabricv4.models.service_profiles import ServiceProfiles
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
    api_instance = equinix.services.fabricv4.ServiceProfilesApi(api_client)
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)
    view_point = aSide # GetServiceProfilesViewPointParameter | flips view between buyer and seller representation (optional) (default to aSide)

    try:
        # Get all Profiles
        api_response = api_instance.get_service_profiles(offset=offset, limit=limit, view_point=view_point)
        print("The response of ServiceProfilesApi->get_service_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceProfilesApi->get_service_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 
 **view_point** | [**GetServiceProfilesViewPointParameter**](.md)| flips view between buyer and seller representation | [optional] [default to aSide]

### Return type

[**ServiceProfiles**](ServiceProfiles.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_profile_by_uuid**
> ServiceProfile put_service_profile_by_uuid(service_profile_id, if_match, service_profile_request)

Replace Profile

This API request replaces a service profile definition

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.service_profile import ServiceProfile
from equinix.services.fabricv4.models.service_profile_request import ServiceProfileRequest
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
    api_instance = equinix.services.fabricv4.ServiceProfilesApi(api_client)
    service_profile_id = 'service_profile_id_example' # str | Service Profile UUID
    if_match = 'if_match_example' # str | conditional request
    service_profile_request = equinix.services.fabricv4.ServiceProfileRequest() # ServiceProfileRequest | 

    try:
        # Replace Profile
        api_response = api_instance.put_service_profile_by_uuid(service_profile_id, if_match, service_profile_request)
        print("The response of ServiceProfilesApi->put_service_profile_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceProfilesApi->put_service_profile_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_profile_id** | **str**| Service Profile UUID | 
 **if_match** | **str**| conditional request | 
 **service_profile_request** | [**ServiceProfileRequest**](ServiceProfileRequest.md)|  | 

### Return type

[**ServiceProfile**](ServiceProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=UTF-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Put operation |  * ETag -  <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_service_profiles**
> ServiceProfiles search_service_profiles(service_profile_search_request, view_point=view_point)

Profile Search

Search service profiles by search criteria

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.get_service_profiles_view_point_parameter import GetServiceProfilesViewPointParameter
from equinix.services.fabricv4.models.service_profile_search_request import ServiceProfileSearchRequest
from equinix.services.fabricv4.models.service_profiles import ServiceProfiles
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
    api_instance = equinix.services.fabricv4.ServiceProfilesApi(api_client)
    service_profile_search_request = equinix.services.fabricv4.ServiceProfileSearchRequest() # ServiceProfileSearchRequest | 
    view_point = aSide # GetServiceProfilesViewPointParameter | flips view between buyer and seller representation (optional) (default to aSide)

    try:
        # Profile Search
        api_response = api_instance.search_service_profiles(service_profile_search_request, view_point=view_point)
        print("The response of ServiceProfilesApi->search_service_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceProfilesApi->search_service_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_profile_search_request** | [**ServiceProfileSearchRequest**](ServiceProfileSearchRequest.md)|  | 
 **view_point** | [**GetServiceProfilesViewPointParameter**](.md)| flips view between buyer and seller representation | [optional] [default to aSide]

### Return type

[**ServiceProfiles**](ServiceProfiles.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=UTF-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_profile_by_uuid**
> ServiceProfile update_service_profile_by_uuid(service_profile_id, if_match, json_patch_operation)

Update Profile

Update Service Profile by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.json_patch_operation import JsonPatchOperation
from equinix.services.fabricv4.models.service_profile import ServiceProfile
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
    api_instance = equinix.services.fabricv4.ServiceProfilesApi(api_client)
    service_profile_id = 'service_profile_id_example' # str | Service Profile UUID
    if_match = 'if_match_example' # str | conditional request
    json_patch_operation = [equinix.services.fabricv4.JsonPatchOperation()] # List[JsonPatchOperation] | 

    try:
        # Update Profile
        api_response = api_instance.update_service_profile_by_uuid(service_profile_id, if_match, json_patch_operation)
        print("The response of ServiceProfilesApi->update_service_profile_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceProfilesApi->update_service_profile_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_profile_id** | **str**| Service Profile UUID | 
 **if_match** | **str**| conditional request | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 

### Return type

[**ServiceProfile**](ServiceProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json; charset=UTF-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Patch operation |  * ETag -  <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

