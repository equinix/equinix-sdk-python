# equinix.services.fabricv4.PeeringProtocolsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection_peering_protocol**](PeeringProtocolsApi.md#create_connection_peering_protocol) | **POST** /fabric/v4/connections/{uuid}/peeringProtocols | Create Peering Protocol


# **create_connection_peering_protocol**
> PeeringProtocolData create_connection_peering_protocol(uuid, connection_peering_protocol_post_request)

Create Peering Protocol

This API provides capability to create Peering Protocol for connections

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.connection_peering_protocol_post_request import ConnectionPeeringProtocolPostRequest
from equinix.services.fabricv4.models.peering_protocol_data import PeeringProtocolData
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
    api_instance = equinix.services.fabricv4.PeeringProtocolsApi(api_client)
    uuid = 'uuid_example' # str | uuid
    connection_peering_protocol_post_request = equinix.services.fabricv4.ConnectionPeeringProtocolPostRequest() # ConnectionPeeringProtocolPostRequest | 

    try:
        # Create Peering Protocol
        api_response = api_instance.create_connection_peering_protocol(uuid, connection_peering_protocol_post_request)
        print("The response of PeeringProtocolsApi->create_connection_peering_protocol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeeringProtocolsApi->create_connection_peering_protocol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| uuid | 
 **connection_peering_protocol_post_request** | [**ConnectionPeeringProtocolPostRequest**](ConnectionPeeringProtocolPostRequest.md)|  | 

### Return type

[**PeeringProtocolData**](PeeringProtocolData.md)

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
**404** | Connection ID Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

