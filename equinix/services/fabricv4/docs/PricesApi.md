# equinix.services.fabricv4.PricesApi

All URIs are relative to *https://api.equinix.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_prices**](PricesApi.md#search_prices) | **POST** /fabric/v4/prices/search | Get Prices


# **search_prices**
> PriceSearchResponse search_prices(filter_body)

Get Prices

Search prices by search criteria

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import equinix.services.fabricv4
from equinix.services.fabricv4.models.filter_body import FilterBody
from equinix.services.fabricv4.models.price_search_response import PriceSearchResponse
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
    api_instance = equinix.services.fabricv4.PricesApi(api_client)
    filter_body = equinix.services.fabricv4.FilterBody() # FilterBody | 

    try:
        # Get Prices
        api_response = api_instance.search_prices(filter_body)
        print("The response of PricesApi->search_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->search_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_body** | [**FilterBody**](FilterBody.md)|  | 

### Return type

[**PriceSearchResponse**](PriceSearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

