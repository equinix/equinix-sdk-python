# equinix.services.fabricv4.ASNsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asn**](ASNsApi.md#create_asn) | **POST** /fabric/v4/asns | Create ASN
[**delete_asn_by_id**](ASNsApi.md#delete_asn_by_id) | **DELETE** /fabric/v4/asns/{asnId} | Delete ASN
[**get_asn_by_id**](ASNsApi.md#get_asn_by_id) | **GET** /fabric/v4/asns/{asnId} | Get ASN
[**patch_asn_by_id**](ASNsApi.md#patch_asn_by_id) | **PATCH** /fabric/v4/asns/{asnId} | Update ASN
[**search_asns**](ASNsApi.md#search_asns) | **POST** /fabric/v4/asns/search | Search ASNs


# **create_asn**
> Asn create_asn(create_asn_request)

Create ASN

Create a new Public or Private ASN record

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.asn import Asn
from equinix.services.fabricv4.models.create_asn_request import CreateAsnRequest
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
    api_instance = equinix.services.fabricv4.ASNsApi(api_client)
    create_asn_request = {"type":"PUBLIC_ASN","project":{"projectId":"03ed2230-604a-494c-bca2-c042d38d80bc"},"number":64497,"rirRegion":"RIPE_NCC","ownershipChallengeDetails":{"type":"RPKI"}} # CreateAsnRequest | 

    try:
        # Create ASN
        api_response = api_instance.create_asn(create_asn_request)
        print("The response of ASNsApi->create_asn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ASNsApi->create_asn: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_asn_request** | [**CreateAsnRequest**](CreateAsnRequest.md)|  | 

### Return type

[**Asn**](Asn.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ASN request accepted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asn_by_id**
> Asn delete_asn_by_id(asn_id)

Delete ASN

Deprovision ASN record by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.asn import Asn
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
    api_instance = equinix.services.fabricv4.ASNsApi(api_client)
    asn_id = 'asn_id_example' # str | UUID of the ASN record

    try:
        # Delete ASN
        api_response = api_instance.delete_asn_by_id(asn_id)
        print("The response of ASNsApi->delete_asn_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ASNsApi->delete_asn_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **str**| UUID of the ASN record | 

### Return type

[**Asn**](Asn.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ASN request accepted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asn_by_id**
> Asn get_asn_by_id(asn_id)

Get ASN

Retrieve ASN record by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.asn import Asn
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
    api_instance = equinix.services.fabricv4.ASNsApi(api_client)
    asn_id = 'asn_id_example' # str | UUID of the ASN record

    try:
        # Get ASN
        api_response = api_instance.get_asn_by_id(asn_id)
        print("The response of ASNsApi->get_asn_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ASNsApi->get_asn_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **str**| UUID of the ASN record | 

### Return type

[**Asn**](Asn.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ASN retrieved successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_asn_by_id**
> Asn patch_asn_by_id(asn_id, asn_patch_operation)

Update ASN

Update ASN record

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.asn import Asn
from equinix.services.fabricv4.models.asn_patch_operation import AsnPatchOperation
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
    api_instance = equinix.services.fabricv4.ASNsApi(api_client)
    asn_id = 'asn_id_example' # str | UUID of the ASN record
    asn_patch_operation = [{"op":"replace","path":"/ownershipChallengeDetails/signature","value":"MEUCIQCrExampleBase64SignatureValue7h4Yg=="}] # List[AsnPatchOperation] | 

    try:
        # Update ASN
        api_response = api_instance.patch_asn_by_id(asn_id, asn_patch_operation)
        print("The response of ASNsApi->patch_asn_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ASNsApi->patch_asn_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **str**| UUID of the ASN record | 
 **asn_patch_operation** | [**List[AsnPatchOperation]**](AsnPatchOperation.md)|  | 

### Return type

[**Asn**](Asn.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ASN request accepted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_asns**
> AsnSearchResponseBody search_asns(asn_search_request_body)

Search ASNs

Search for ASN records based on criteria

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.asn_search_request_body import AsnSearchRequestBody
from equinix.services.fabricv4.models.asn_search_response_body import AsnSearchResponseBody
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
    api_instance = equinix.services.fabricv4.ASNsApi(api_client)
    asn_search_request_body = {"pagination":{"offset":0,"limit":25},"filter":{"and":[{"property":"/project/projectId","operator":"=","values":["03ed2230-604a-494c-bca2-c042d38d80bc"]}]},"sort":[{"direction":"DESC","property":"/changeLog/createdDateTime"}]} # AsnSearchRequestBody | 

    try:
        # Search ASNs
        api_response = api_instance.search_asns(asn_search_request_body)
        print("The response of ASNsApi->search_asns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ASNsApi->search_asns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_search_request_body** | [**AsnSearchRequestBody**](AsnSearchRequestBody.md)|  | 

### Return type

[**AsnSearchResponseBody**](AsnSearchResponseBody.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ASN records found successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

