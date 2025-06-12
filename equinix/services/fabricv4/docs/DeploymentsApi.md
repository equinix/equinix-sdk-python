# equinix.services.fabricv4.DeploymentsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_deployment**](DeploymentsApi.md#action_deployment) | **POST** /fabric/v4/deployments/{deploymentId}/actions | Deploy, Dry Run or Destroy Deployment
[**create_topology_deployment**](DeploymentsApi.md#create_topology_deployment) | **POST** /fabric/v4/deployments | Create a new topology deployment
[**delete_deployment**](DeploymentsApi.md#delete_deployment) | **DELETE** /fabric/v4/deployments/{deploymentId} | Delete Deployment using UUID
[**get_deployment**](DeploymentsApi.md#get_deployment) | **GET** /fabric/v4/deployments/{deploymentId} | Retrieve Deployment details using UUID
[**search_deployments**](DeploymentsApi.md#search_deployments) | **POST** /fabric/v4/deployments/searchDeployments | Search deployments
[**search_provider_resources**](DeploymentsApi.md#search_provider_resources) | **POST** /fabric/v4/providerResources/search | Search provider resources


# **action_deployment**
> CloudRouterActionResponse action_deployment(deployment_id, deployment_action_request)

Deploy, Dry Run or Destroy Deployment

The deployment action is used to deploy, dry run or destroy a deployment. The request body must contain the type of action to be performed and the connection details.
The response will contain the status of the action.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.cloud_router_action_response import CloudRouterActionResponse
from equinix.services.fabricv4.models.deployment_action_request import DeploymentActionRequest
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
    api_instance = equinix.services.fabricv4.DeploymentsApi(api_client)
    deployment_id = 'deployment_id_example' # str | Deployment UUID
    deployment_action_request = equinix.services.fabricv4.DeploymentActionRequest() # DeploymentActionRequest | 

    try:
        # Deploy, Dry Run or Destroy Deployment
        api_response = api_instance.action_deployment(deployment_id, deployment_action_request)
        print("The response of DeploymentsApi->action_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->action_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| Deployment UUID | 
 **deployment_action_request** | [**DeploymentActionRequest**](DeploymentActionRequest.md)|  | 

### Return type

[**CloudRouterActionResponse**](CloudRouterActionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Internal server error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_topology_deployment**
> DeploymentResponse create_topology_deployment(deployment)

Create a new topology deployment

The deployment API is used to creates new deployment topologies. 
It allows users to define the properties of the deployment, including Fabric and CSP providers.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.deployment import Deployment
from equinix.services.fabricv4.models.deployment_response import DeploymentResponse
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
    api_instance = equinix.services.fabricv4.DeploymentsApi(api_client)
    deployment = equinix.services.fabricv4.Deployment() # Deployment | 

    try:
        # Create a new topology deployment
        api_response = api_instance.create_topology_deployment(deployment)
        print("The response of DeploymentsApi->create_topology_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->create_topology_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment** | [**Deployment**](Deployment.md)|  | 

### Return type

[**DeploymentResponse**](DeploymentResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Deployment created successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deployment**
> DeploymentResponse delete_deployment(deployment_id)

Delete Deployment using UUID

This API provides capability to delete user's deployment

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.deployment_response import DeploymentResponse
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
    api_instance = equinix.services.fabricv4.DeploymentsApi(api_client)
    deployment_id = 'deployment_id_example' # str | Deployment UUID

    try:
        # Delete Deployment using UUID
        api_response = api_instance.delete_deployment(deployment_id)
        print("The response of DeploymentsApi->delete_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->delete_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| Deployment UUID | 

### Return type

[**DeploymentResponse**](DeploymentResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment object |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment**
> DeploymentResponse get_deployment(deployment_id)

Retrieve Deployment details using UUID

This API provides capability to retrieve user's deployment details.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.deployment_response import DeploymentResponse
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
    api_instance = equinix.services.fabricv4.DeploymentsApi(api_client)
    deployment_id = 'deployment_id_example' # str | Deployment UUID

    try:
        # Retrieve Deployment details using UUID
        api_response = api_instance.get_deployment(deployment_id)
        print("The response of DeploymentsApi->get_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->get_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| Deployment UUID | 

### Return type

[**DeploymentResponse**](DeploymentResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment details |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_deployments**
> DeploymentSearchResponse search_deployments(deployment_search_request)

Search deployments

The API provides capability to get list of user's deployment using search criteria.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.deployment_search_request import DeploymentSearchRequest
from equinix.services.fabricv4.models.deployment_search_response import DeploymentSearchResponse
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
    api_instance = equinix.services.fabricv4.DeploymentsApi(api_client)
    deployment_search_request = equinix.services.fabricv4.DeploymentSearchRequest() # DeploymentSearchRequest | 

    try:
        # Search deployments
        api_response = api_instance.search_deployments(deployment_search_request)
        print("The response of DeploymentsApi->search_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->search_deployments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_search_request** | [**DeploymentSearchRequest**](DeploymentSearchRequest.md)|  | 

### Return type

[**DeploymentSearchResponse**](DeploymentSearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of deployments |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_provider_resources**
> ProviderSearchResponse search_provider_resources(provider_search_request)

Search provider resources

The API provides capability to get list of user's provider resources using search criteria, including optional filtering

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.provider_search_request import ProviderSearchRequest
from equinix.services.fabricv4.models.provider_search_response import ProviderSearchResponse
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
    api_instance = equinix.services.fabricv4.DeploymentsApi(api_client)
    provider_search_request = equinix.services.fabricv4.ProviderSearchRequest() # ProviderSearchRequest | 

    try:
        # Search provider resources
        api_response = api_instance.search_provider_resources(provider_search_request)
        print("The response of DeploymentsApi->search_provider_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->search_provider_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_search_request** | [**ProviderSearchRequest**](ProviderSearchRequest.md)|  | 

### Return type

[**ProviderSearchResponse**](ProviderSearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

