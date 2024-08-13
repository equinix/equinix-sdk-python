# equinix.services.fabricv4.MarketplaceSubscriptionsApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subscription_by_id**](MarketplaceSubscriptionsApi.md#get_subscription_by_id) | **GET** /fabric/v4/marketplaceSubscriptions/{subscriptionId} | Get Subscription


# **get_subscription_by_id**
> SubscriptionResponse get_subscription_by_id(subscription_id)

Get Subscription

The API provides capability to get subscription

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.subscription_response import SubscriptionResponse
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
    api_instance = equinix.services.fabricv4.MarketplaceSubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | Subscription UUID

    try:
        # Get Subscription
        api_response = api_instance.get_subscription_by_id(subscription_id)
        print("The response of MarketplaceSubscriptionsApi->get_subscription_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceSubscriptionsApi->get_subscription_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription UUID | 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

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
**415** | Unsupported Media Type |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

