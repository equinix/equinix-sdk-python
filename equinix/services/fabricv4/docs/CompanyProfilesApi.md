# equinix.services.fabricv4.CompanyProfilesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_private_service_to_profile**](CompanyProfilesApi.md#attach_private_service_to_profile) | **PUT** /fabric/v4/companyProfiles/{companyProfileId}/privateServices/{privateServiceId} | Attach Private Service
[**attach_service_profile_to_profile**](CompanyProfilesApi.md#attach_service_profile_to_profile) | **PUT** /fabric/v4/companyProfiles/{companyProfileId}/serviceProfiles/{serviceProfileId} | Attach Service Profile
[**attach_tag_to_profile**](CompanyProfilesApi.md#attach_tag_to_profile) | **PUT** /fabric/v4/companyProfiles/{companyProfileId}/tags/{tagId} | Attach Tag
[**create_company_profile**](CompanyProfilesApi.md#create_company_profile) | **POST** /fabric/v4/companyProfiles | Create Company Profile
[**delete_company_profile**](CompanyProfilesApi.md#delete_company_profile) | **DELETE** /fabric/v4/companyProfiles/{companyProfileId} | Delete Company Profile
[**detach_private_service_from_profile**](CompanyProfilesApi.md#detach_private_service_from_profile) | **DELETE** /fabric/v4/companyProfiles/{companyProfileId}/privateServices/{privateServiceId} | Detach Private Service
[**detach_service_profile_from_profile**](CompanyProfilesApi.md#detach_service_profile_from_profile) | **DELETE** /fabric/v4/companyProfiles/{companyProfileId}/serviceProfiles/{serviceProfileId} | Detach Service Profile
[**detach_tag_from_profile**](CompanyProfilesApi.md#detach_tag_from_profile) | **DELETE** /fabric/v4/companyProfiles/{companyProfileId}/tags/{tagId} | Detach Tag
[**get_company_profile**](CompanyProfilesApi.md#get_company_profile) | **GET** /fabric/v4/companyProfiles/{companyProfileId} | Get Company Profile by UUID
[**get_company_profile_private_services**](CompanyProfilesApi.md#get_company_profile_private_services) | **GET** /fabric/v4/companyProfiles/{companyProfileId}/privateServices | Get Private Services
[**get_company_profile_service_profiles**](CompanyProfilesApi.md#get_company_profile_service_profiles) | **GET** /fabric/v4/companyProfiles/{companyProfileId}/serviceProfiles | Get Service Profiles
[**get_tags**](CompanyProfilesApi.md#get_tags) | **GET** /fabric/v4/companyProfiles/{companyProfileId}/tags | Get Tags
[**search_company_profile**](CompanyProfilesApi.md#search_company_profile) | **POST** /fabric/v4/companyProfiles/search | Search Company Profiles


# **attach_private_service_to_profile**
> AttachPrivateServiceResponse attach_private_service_to_profile(company_profile_id, private_service_id)

Attach Private Service

Attach a private service to a company profile <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.attach_private_service_response import AttachPrivateServiceResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_id = 'company_profile_id_example' # str | Company Profile UUID
    private_service_id = 'private_service_id_example' # str | Private Service UUID

    try:
        # Attach Private Service
        api_response = api_instance.attach_private_service_to_profile(company_profile_id, private_service_id)
        print("The response of CompanyProfilesApi->attach_private_service_to_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->attach_private_service_to_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_id** | **str**| Company Profile UUID | 
 **private_service_id** | **str**| Private Service UUID | 

### Return type

[**AttachPrivateServiceResponse**](AttachPrivateServiceResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_service_profile_to_profile**
> AttachServiceProfileResponse attach_service_profile_to_profile(company_profile_id, service_profile_id)

Attach Service Profile

Attach a service profile to a company profile <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.attach_service_profile_response import AttachServiceProfileResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_id = 'company_profile_id_example' # str | Company Profile UUID
    service_profile_id = 'service_profile_id_example' # str | Service Profile UUID

    try:
        # Attach Service Profile
        api_response = api_instance.attach_service_profile_to_profile(company_profile_id, service_profile_id)
        print("The response of CompanyProfilesApi->attach_service_profile_to_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->attach_service_profile_to_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_id** | **str**| Company Profile UUID | 
 **service_profile_id** | **str**| Service Profile UUID | 

### Return type

[**AttachServiceProfileResponse**](AttachServiceProfileResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_tag_to_profile**
> AttachTagResponse attach_tag_to_profile(company_profile_id, tag_id)

Attach Tag

Attach a tag to a company profile <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.attach_tag_response import AttachTagResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_id = 'company_profile_id_example' # str | Company Profile UUID
    tag_id = 'tag_id_example' # str | Tag UUID

    try:
        # Attach Tag
        api_response = api_instance.attach_tag_to_profile(company_profile_id, tag_id)
        print("The response of CompanyProfilesApi->attach_tag_to_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->attach_tag_to_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_id** | **str**| Company Profile UUID | 
 **tag_id** | **str**| Tag UUID | 

### Return type

[**AttachTagResponse**](AttachTagResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_company_profile**
> CompanyProfileResponse create_company_profile(company_profile_request)

Create Company Profile

Create a new company profile <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.company_profile_request import CompanyProfileRequest
from equinix.services.fabricv4.models.company_profile_response import CompanyProfileResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_request = equinix.services.fabricv4.CompanyProfileRequest() # CompanyProfileRequest | 

    try:
        # Create Company Profile
        api_response = api_instance.create_company_profile(company_profile_request)
        print("The response of CompanyProfilesApi->create_company_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->create_company_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_request** | [**CompanyProfileRequest**](CompanyProfileRequest.md)|  | 

### Return type

[**CompanyProfileResponse**](CompanyProfileResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Company profile created successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_profile**
> CompanyProfileResponse delete_company_profile(company_profile_id)

Delete Company Profile

Delete company profile by UUID <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.company_profile_response import CompanyProfileResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_id = 'company_profile_id_example' # str | Company Profile UUID

    try:
        # Delete Company Profile
        api_response = api_instance.delete_company_profile(company_profile_id)
        print("The response of CompanyProfilesApi->delete_company_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->delete_company_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_id** | **str**| Company Profile UUID | 

### Return type

[**CompanyProfileResponse**](CompanyProfileResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_private_service_from_profile**
> AttachPrivateServiceResponse detach_private_service_from_profile(company_profile_id, private_service_id)

Detach Private Service

Detach a private service from a company profile <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.attach_private_service_response import AttachPrivateServiceResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_id = 'company_profile_id_example' # str | Company Profile UUID
    private_service_id = 'private_service_id_example' # str | Private Service UUID

    try:
        # Detach Private Service
        api_response = api_instance.detach_private_service_from_profile(company_profile_id, private_service_id)
        print("The response of CompanyProfilesApi->detach_private_service_from_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->detach_private_service_from_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_id** | **str**| Company Profile UUID | 
 **private_service_id** | **str**| Private Service UUID | 

### Return type

[**AttachPrivateServiceResponse**](AttachPrivateServiceResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_service_profile_from_profile**
> AttachServiceProfileResponse detach_service_profile_from_profile(company_profile_id, service_profile_id)

Detach Service Profile

Detach a service profile from a company profile <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.attach_service_profile_response import AttachServiceProfileResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_id = 'company_profile_id_example' # str | Company Profile UUID
    service_profile_id = 'service_profile_id_example' # str | Service Profile UUID

    try:
        # Detach Service Profile
        api_response = api_instance.detach_service_profile_from_profile(company_profile_id, service_profile_id)
        print("The response of CompanyProfilesApi->detach_service_profile_from_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->detach_service_profile_from_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_id** | **str**| Company Profile UUID | 
 **service_profile_id** | **str**| Service Profile UUID | 

### Return type

[**AttachServiceProfileResponse**](AttachServiceProfileResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_tag_from_profile**
> AttachTagResponse detach_tag_from_profile(company_profile_id, tag_id)

Detach Tag

Detach a tag from a company profile <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.attach_tag_response import AttachTagResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_id = 'company_profile_id_example' # str | Company Profile UUID
    tag_id = 'tag_id_example' # str | Tag UUID

    try:
        # Detach Tag
        api_response = api_instance.detach_tag_from_profile(company_profile_id, tag_id)
        print("The response of CompanyProfilesApi->detach_tag_from_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->detach_tag_from_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_id** | **str**| Company Profile UUID | 
 **tag_id** | **str**| Tag UUID | 

### Return type

[**AttachTagResponse**](AttachTagResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_profile**
> CompanyProfileResponse get_company_profile(company_profile_id)

Get Company Profile by UUID

Get company profile details by UUID <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.company_profile_response import CompanyProfileResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_id = 'company_profile_id_example' # str | Company Profile UUID

    try:
        # Get Company Profile by UUID
        api_response = api_instance.get_company_profile(company_profile_id)
        print("The response of CompanyProfilesApi->get_company_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->get_company_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_id** | **str**| Company Profile UUID | 

### Return type

[**CompanyProfileResponse**](CompanyProfileResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_profile_private_services**
> PrivateServiceListResponse get_company_profile_private_services(company_profile_id)

Get Private Services

Get all private services attached to a company profile <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.private_service_list_response import PrivateServiceListResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_id = 'company_profile_id_example' # str | Company Profile UUID

    try:
        # Get Private Services
        api_response = api_instance.get_company_profile_private_services(company_profile_id)
        print("The response of CompanyProfilesApi->get_company_profile_private_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->get_company_profile_private_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_id** | **str**| Company Profile UUID | 

### Return type

[**PrivateServiceListResponse**](PrivateServiceListResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_profile_service_profiles**
> ServiceProfileListResponse get_company_profile_service_profiles(company_profile_id)

Get Service Profiles

Get all service profiles attached to a company profile <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.service_profile_list_response import ServiceProfileListResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_id = 'company_profile_id_example' # str | Company Profile UUID

    try:
        # Get Service Profiles
        api_response = api_instance.get_company_profile_service_profiles(company_profile_id)
        print("The response of CompanyProfilesApi->get_company_profile_service_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->get_company_profile_service_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_id** | **str**| Company Profile UUID | 

### Return type

[**ServiceProfileListResponse**](ServiceProfileListResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> TagListResponse get_tags(company_profile_id)

Get Tags

Get all tags attached to a company profile <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.tag_list_response import TagListResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_id = 'company_profile_id_example' # str | Company Profile UUID

    try:
        # Get Tags
        api_response = api_instance.get_tags(company_profile_id)
        print("The response of CompanyProfilesApi->get_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->get_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_id** | **str**| Company Profile UUID | 

### Return type

[**TagListResponse**](TagListResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_company_profile**
> CompanyProfileSearchResponse search_company_profile(company_profile_search_request, view_point=view_point)

Search Company Profiles

Search company profiles based on filter criteria <font color="red"> <sup color='red'>Beta</sup></font>

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.company_profile_search_request import CompanyProfileSearchRequest
from equinix.services.fabricv4.models.company_profile_search_response import CompanyProfileSearchResponse
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
    api_instance = equinix.services.fabricv4.CompanyProfilesApi(api_client)
    company_profile_search_request = equinix.services.fabricv4.CompanyProfileSearchRequest() # CompanyProfileSearchRequest | 
    view_point = 'aSide' # str | Viewpoint for the request, either 'aSide' or 'zSide' (optional) (default to 'aSide')

    try:
        # Search Company Profiles
        api_response = api_instance.search_company_profile(company_profile_search_request, view_point=view_point)
        print("The response of CompanyProfilesApi->search_company_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfilesApi->search_company_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_profile_search_request** | [**CompanyProfileSearchRequest**](CompanyProfileSearchRequest.md)|  | 
 **view_point** | **str**| Viewpoint for the request, either &#39;aSide&#39; or &#39;zSide&#39; | [optional] [default to &#39;aSide&#39;]

### Return type

[**CompanyProfileSearchResponse**](CompanyProfileSearchResponse.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

