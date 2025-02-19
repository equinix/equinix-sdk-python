# equinix.services.metalv1.TwoFactorAuthApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_tfa_app**](TwoFactorAuthApi.md#disable_tfa_app) | **DELETE** /user/otp/app | Disable two factor authentication
[**enable_tfa_app**](TwoFactorAuthApi.md#enable_tfa_app) | **POST** /user/otp/app | Enable two factor auth using app


# **disable_tfa_app**
> disable_tfa_app()

Disable two factor authentication

Disables two factor authentication.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix.services.metalv1
from equinix.services.metalv1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix.services.metalv1.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix.services.metalv1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix.services.metalv1.TwoFactorAuthApi(api_client)

    try:
        # Disable two factor authentication
        api_instance.disable_tfa_app()
    except Exception as e:
        print("Exception when calling TwoFactorAuthApi->disable_tfa_app: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | no content |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **enable_tfa_app**
> enable_tfa_app()

Enable two factor auth using app

Enables two factor authentication using authenticator app.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix.services.metalv1
from equinix.services.metalv1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix.services.metalv1.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix.services.metalv1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix.services.metalv1.TwoFactorAuthApi(api_client)

    try:
        # Enable two factor auth using app
        api_instance.enable_tfa_app()
    except Exception as e:
        print("Exception when calling TwoFactorAuthApi->enable_tfa_app: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
