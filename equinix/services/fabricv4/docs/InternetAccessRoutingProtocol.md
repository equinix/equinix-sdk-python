# InternetAccessRoutingProtocol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InternetAccessRoutingProtocolType**](InternetAccessRoutingProtocolType.md) |  | 
**customer_routes** | [**List[InternetAccessCustomerRoute]**](InternetAccessCustomerRoute.md) |  | 
**connections** | [**List[InternetAccessConnection]**](InternetAccessConnection.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_routing_protocol import InternetAccessRoutingProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessRoutingProtocol from a JSON string
internet_access_routing_protocol_instance = InternetAccessRoutingProtocol.from_json(json)
# print the JSON string representation of the object
print(InternetAccessRoutingProtocol.to_json())

# convert the object into a dict
internet_access_routing_protocol_dict = internet_access_routing_protocol_instance.to_dict()
# create an instance of InternetAccessRoutingProtocol from a dict
internet_access_routing_protocol_from_dict = InternetAccessRoutingProtocol.from_dict(internet_access_routing_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


