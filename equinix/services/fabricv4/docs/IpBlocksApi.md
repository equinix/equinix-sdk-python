# equinix.services.fabricv4.IpBlocksApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ip_block_by_id**](IpBlocksApi.md#delete_ip_block_by_id) | **DELETE** /fabric/v4/ipBlocks/{uuid} | Delete Ip Block by UUID
[**get_ip_block**](IpBlocksApi.md#get_ip_block) | **GET** /fabric/v4/ipBlocks/{uuid} | Retrieve Ip Block by UUID
[**patch_ip_block_by_id**](IpBlocksApi.md#patch_ip_block_by_id) | **PATCH** /fabric/v4/ipBlocks/{uuid} | patch Ip Block by UUID
[**search_ip_blocks**](IpBlocksApi.md#search_ip_blocks) | **POST** /fabric/v4/ipBlocks/search | Search for Ip Blocks
[**submit_ip_block**](IpBlocksApi.md#submit_ip_block) | **POST** /fabric/v4/ipBlocks | Submits new Equinix owned or customer owned Ip Block request


# **delete_ip_block_by_id**
> IpBlock delete_ip_block_by_id(uuid)

Delete Ip Block by UUID

Delete Ip Block by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.ip_block import IpBlock
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
    api_instance = equinix.services.fabricv4.IpBlocksApi(api_client)
    uuid = 'uuid_example' # str | UUID of the Ip Block

    try:
        # Delete Ip Block by UUID
        api_response = api_instance.delete_ip_block_by_id(uuid)
        print("The response of IpBlocksApi->delete_ip_block_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpBlocksApi->delete_ip_block_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the Ip Block | 

### Return type

[**IpBlock**](IpBlock.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Ip Block submitted, patched, or deletion accepted |  -  |
**400** | Invalid input parameter |  -  |
**403** | Forbidden |  -  |
**404** | Ip Block not found |  -  |
**409** | Ip Block cannot be deleted due to active products |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_block**
> IpBlock get_ip_block(uuid)

Retrieve Ip Block by UUID

Retrieve Ip Block by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.ip_block import IpBlock
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
    api_instance = equinix.services.fabricv4.IpBlocksApi(api_client)
    uuid = 'uuid_example' # str | UUID of the Ip Block

    try:
        # Retrieve Ip Block by UUID
        api_response = api_instance.get_ip_block(uuid)
        print("The response of IpBlocksApi->get_ip_block:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpBlocksApi->get_ip_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the Ip Block | 

### Return type

[**IpBlock**](IpBlock.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ip Block retrieved successfully |  -  |
**403** | Forbidden |  -  |
**404** | Ip Block not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ip_block_by_id**
> IpBlock patch_ip_block_by_id(uuid, patch_ip_block_request_body_item)

patch Ip Block by UUID

patch Ip Block by UUID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.ip_block import IpBlock
from equinix.services.fabricv4.models.patch_ip_block_request_body_item import PatchIpBlockRequestBodyItem
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
    api_instance = equinix.services.fabricv4.IpBlocksApi(api_client)
    uuid = 'uuid_example' # str | UUID of the Ip Block
    patch_ip_block_request_body_item = [equinix.services.fabricv4.PatchIpBlockRequestBodyItem()] # List[PatchIpBlockRequestBodyItem] | 

    try:
        # patch Ip Block by UUID
        api_response = api_instance.patch_ip_block_by_id(uuid, patch_ip_block_request_body_item)
        print("The response of IpBlocksApi->patch_ip_block_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpBlocksApi->patch_ip_block_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the Ip Block | 
 **patch_ip_block_request_body_item** | [**List[PatchIpBlockRequestBodyItem]**](PatchIpBlockRequestBodyItem.md)|  | 

### Return type

[**IpBlock**](IpBlock.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Ip Block submitted, patched, or deletion accepted |  -  |
**404** | Ip Block not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ip_blocks**
> IpBlockSearchResponseBody search_ip_blocks(ip_blocks_search_request_body)

Search for Ip Blocks

Search for Ip Blocks based on criteria

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.ip_block_search_response_body import IpBlockSearchResponseBody
from equinix.services.fabricv4.models.ip_blocks_search_request_body import IpBlocksSearchRequestBody
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
    api_instance = equinix.services.fabricv4.IpBlocksApi(api_client)
    ip_blocks_search_request_body = equinix.services.fabricv4.IpBlocksSearchRequestBody() # IpBlocksSearchRequestBody | 

    try:
        # Search for Ip Blocks
        api_response = api_instance.search_ip_blocks(ip_blocks_search_request_body)
        print("The response of IpBlocksApi->search_ip_blocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpBlocksApi->search_ip_blocks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_blocks_search_request_body** | [**IpBlocksSearchRequestBody**](IpBlocksSearchRequestBody.md)|  | 

### Return type

[**IpBlockSearchResponseBody**](IpBlockSearchResponseBody.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ip Blocks found successfully |  -  |
**400** | Invalid input parameter |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_ip_block**
> IpBlock submit_ip_block(submit_ip_block_request_body)

Submits new Equinix owned or customer owned Ip Block request

Submits new Equinix owned or customer owned Ip Block request

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.ip_block import IpBlock
from equinix.services.fabricv4.models.submit_ip_block_request_body import SubmitIpBlockRequestBody
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
    api_instance = equinix.services.fabricv4.IpBlocksApi(api_client)
    submit_ip_block_request_body = equinix.services.fabricv4.SubmitIpBlockRequestBody() # SubmitIpBlockRequestBody | 

    try:
        # Submits new Equinix owned or customer owned Ip Block request
        api_response = api_instance.submit_ip_block(submit_ip_block_request_body)
        print("The response of IpBlocksApi->submit_ip_block:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpBlocksApi->submit_ip_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_ip_block_request_body** | [**SubmitIpBlockRequestBody**](SubmitIpBlockRequestBody.md)|  | 

### Return type

[**IpBlock**](IpBlock.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Ip Block submitted, patched, or deletion accepted |  -  |
**400** | Invalid input parameter |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

