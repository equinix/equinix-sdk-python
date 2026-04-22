# equinix.services.fabricv4.AgentTemplatesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_template_by_uuid**](AgentTemplatesApi.md#get_agent_template_by_uuid) | **GET** /fabric/v4/agentTemplates/{agentTemplateId} | Get Agent Template by UUID
[**get_agent_templates**](AgentTemplatesApi.md#get_agent_templates) | **GET** /fabric/v4/agentTemplates | Get Agent Templates


# **get_agent_template_by_uuid**
> AgentTemplates get_agent_template_by_uuid(agent_template_id, offset=offset, limit=limit)

Get Agent Template by UUID

This API provides capability to retrieve an agent template by uuid

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.agent_templates import AgentTemplates
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
    api_instance = equinix.services.fabricv4.AgentTemplatesApi(api_client)
    agent_template_id = 'agent_template_id_example' # str | Agent Template UUID
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get Agent Template by UUID
        api_response = api_instance.get_agent_template_by_uuid(agent_template_id, offset=offset, limit=limit)
        print("The response of AgentTemplatesApi->get_agent_template_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTemplatesApi->get_agent_template_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_template_id** | **str**| Agent Template UUID | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**AgentTemplates**](AgentTemplates.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_templates**
> AgentTemplateGetAllResponse get_agent_templates(offset=offset, limit=limit)

Get Agent Templates

This API provides capability to retrieve agent templates

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.agent_template_get_all_response import AgentTemplateGetAllResponse
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
    api_instance = equinix.services.fabricv4.AgentTemplatesApi(api_client)
    offset = 1 # int | offset (optional)
    limit = 10 # int | number of records to fetch (optional)

    try:
        # Get Agent Templates
        api_response = api_instance.get_agent_templates(offset=offset, limit=limit)
        print("The response of AgentTemplatesApi->get_agent_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTemplatesApi->get_agent_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| number of records to fetch | [optional] 

### Return type

[**AgentTemplateGetAllResponse**](AgentTemplateGetAllResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

