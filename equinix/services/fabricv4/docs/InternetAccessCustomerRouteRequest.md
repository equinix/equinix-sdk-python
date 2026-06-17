# InternetAccessCustomerRouteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_block** | [**InternetAccessIpBlockRequest**](InternetAccessIpBlockRequest.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_customer_route_request import InternetAccessCustomerRouteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessCustomerRouteRequest from a JSON string
internet_access_customer_route_request_instance = InternetAccessCustomerRouteRequest.from_json(json)
# print the JSON string representation of the object
print(InternetAccessCustomerRouteRequest.to_json())

# convert the object into a dict
internet_access_customer_route_request_dict = internet_access_customer_route_request_instance.to_dict()
# create an instance of InternetAccessCustomerRouteRequest from a dict
internet_access_customer_route_request_from_dict = InternetAccessCustomerRouteRequest.from_dict(internet_access_customer_route_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


