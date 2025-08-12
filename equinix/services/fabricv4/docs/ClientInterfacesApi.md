# equinix.services.fabricv4.ClientInterfacesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_terraform_templates**](ClientInterfacesApi.md#create_terraform_templates) | **POST** /fabric/v4/deployments/{deploymentId}/download | Generate Terraform Deployment Templates


# **create_terraform_templates**
> bytearray create_terraform_templates(deployment_id, client_interfaces)

Generate Terraform Deployment Templates

The Client Interfaces API is used to generate Terraform Templates based on Deployment details.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.client_interfaces import ClientInterfaces
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
    api_instance = equinix.services.fabricv4.ClientInterfacesApi(api_client)
    deployment_id = 'deployment_id_example' # str | Deployment UUID
    client_interfaces = equinix.services.fabricv4.ClientInterfaces() # ClientInterfaces | 

    try:
        # Generate Terraform Deployment Templates
        api_response = api_instance.create_terraform_templates(deployment_id, client_interfaces)
        print("The response of ClientInterfacesApi->create_terraform_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientInterfacesApi->create_terraform_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| Deployment UUID | 
 **client_interfaces** | [**ClientInterfaces**](ClientInterfaces.md)|  | 

### Return type

**bytearray**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Terraform deployment templates ZIP file generated successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

