# equinix_metal.OTPsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_ensure_otp**](OTPsApi.md#find_ensure_otp) | **POST** /user/otp/verify/{otp} | Verify user by providing an OTP
[**find_recovery_codes**](OTPsApi.md#find_recovery_codes) | **GET** /user/otp/recovery-codes | Retrieve my recovery codes
[**receive_codes**](OTPsApi.md#receive_codes) | **POST** /user/otp/sms/receive | Receive an OTP per sms
[**regenerate_codes**](OTPsApi.md#regenerate_codes) | **POST** /user/otp/recovery-codes | Generate new recovery codes


# **find_ensure_otp**
> find_ensure_otp(otp)

Verify user by providing an OTP

It verifies the user once a valid OTP is provided. It gives back a session token, essentially logging in the user.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
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
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.OTPsApi(api_client)
    otp = 'otp_example' # str | OTP

    try:
        # Verify user by providing an OTP
        api_instance.find_ensure_otp(otp)
    except Exception as e:
        print("Exception when calling OTPsApi->find_ensure_otp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otp** | **str**| OTP | 

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
**400** | bad request |  -  |
**401** | unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **find_recovery_codes**
> RecoveryCodeList find_recovery_codes()

Retrieve my recovery codes

Returns my recovery codes.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.recovery_code_list import RecoveryCodeList
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
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
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.OTPsApi(api_client)

    try:
        # Retrieve my recovery codes
        api_response = api_instance.find_recovery_codes()
        print("The response of OTPsApi->find_recovery_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OTPsApi->find_recovery_codes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RecoveryCodeList**](RecoveryCodeList.md)

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
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **receive_codes**
> receive_codes()

Receive an OTP per sms

Sends an OTP to the user's mobile phone.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
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
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.OTPsApi(api_client)

    try:
        # Receive an OTP per sms
        api_instance.receive_codes()
    except Exception as e:
        print("Exception when calling OTPsApi->receive_codes: %s\n" % e)
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
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**422** | unprocessable entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **regenerate_codes**
> RecoveryCodeList regenerate_codes()

Generate new recovery codes

Generate a new set of recovery codes.

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.recovery_code_list import RecoveryCodeList
from equinix_metal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
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
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.OTPsApi(api_client)

    try:
        # Generate new recovery codes
        api_response = api_instance.regenerate_codes()
        print("The response of OTPsApi->regenerate_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OTPsApi->regenerate_codes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RecoveryCodeList**](RecoveryCodeList.md)

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
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
