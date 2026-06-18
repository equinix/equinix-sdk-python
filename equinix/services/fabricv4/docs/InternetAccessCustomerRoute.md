# InternetAccessCustomerRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_block** | [**InternetAccessIpBlock**](InternetAccessIpBlock.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_customer_route import InternetAccessCustomerRoute

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessCustomerRoute from a JSON string
internet_access_customer_route_instance = InternetAccessCustomerRoute.from_json(json)
# print the JSON string representation of the object
print(InternetAccessCustomerRoute.to_json())

# convert the object into a dict
internet_access_customer_route_dict = internet_access_customer_route_instance.to_dict()
# create an instance of InternetAccessCustomerRoute from a dict
internet_access_customer_route_from_dict = InternetAccessCustomerRoute.from_dict(internet_access_customer_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


