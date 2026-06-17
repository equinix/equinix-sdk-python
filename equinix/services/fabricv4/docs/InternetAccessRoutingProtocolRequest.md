# InternetAccessRoutingProtocolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InternetAccessRoutingProtocolType**](InternetAccessRoutingProtocolType.md) |  | 
**customer_routes** | [**List[InternetAccessCustomerRouteRequest]**](InternetAccessCustomerRouteRequest.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_routing_protocol_request import InternetAccessRoutingProtocolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessRoutingProtocolRequest from a JSON string
internet_access_routing_protocol_request_instance = InternetAccessRoutingProtocolRequest.from_json(json)
# print the JSON string representation of the object
print(InternetAccessRoutingProtocolRequest.to_json())

# convert the object into a dict
internet_access_routing_protocol_request_dict = internet_access_routing_protocol_request_instance.to_dict()
# create an instance of InternetAccessRoutingProtocolRequest from a dict
internet_access_routing_protocol_request_from_dict = InternetAccessRoutingProtocolRequest.from_dict(internet_access_routing_protocol_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


