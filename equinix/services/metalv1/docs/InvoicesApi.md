# equinix_metal.InvoicesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_organization_invoices**](InvoicesApi.md#find_organization_invoices) | **GET** /organizations/{id}/invoices | Retrieve all invoices for an organization
[**get_invoice_by_id**](InvoicesApi.md#get_invoice_by_id) | **GET** /invoices/{id} | Retrieve an invoice


# **find_organization_invoices**
> InvoiceList find_organization_invoices(id, page=page, per_page=per_page, status=status)

Retrieve all invoices for an organization

Returns all invoices for an organization

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.invoice_list import InvoiceList
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
    api_instance = equinix_metal.InvoicesApi(api_client)
    id = 'id_example' # str | Organization UUID
    page = 56 # int | page number (optional)
    per_page = 56 # int | per page (optional)
    status = 'status_example' # str | filter by status (optional)

    try:
        # Retrieve all invoices for an organization
        api_response = api_instance.find_organization_invoices(id, page=page, per_page=per_page, status=status)
        print("The response of InvoicesApi->find_organization_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->find_organization_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization UUID | 
 **page** | **int**| page number | [optional] 
 **per_page** | **int**| per page | [optional] 
 **status** | **str**| filter by status | [optional] 

### Return type

[**InvoiceList**](InvoiceList.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
# **get_invoice_by_id**
> Invoice get_invoice_by_id(id)

Retrieve an invoice

Returns the invoice identified by the provided id

### Example

* Api Key Authentication (x_auth_token):

```python
import equinix_metal
from equinix_metal.models.invoice import Invoice
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
    api_instance = equinix_metal.InvoicesApi(api_client)
    id = 'id_example' # str | Invoice UUID

    try:
        # Retrieve an invoice
        api_response = api_instance.get_invoice_by_id(id)
        print("The response of InvoicesApi->get_invoice_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invoice UUID | 

### Return type

[**Invoice**](Invoice.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
