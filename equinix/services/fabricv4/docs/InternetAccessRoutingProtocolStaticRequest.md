# InternetAccessRoutingProtocolStaticRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[InternetAccessConnectionStaticRequest]**](InternetAccessConnectionStaticRequest.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_routing_protocol_static_request import InternetAccessRoutingProtocolStaticRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessRoutingProtocolStaticRequest from a JSON string
internet_access_routing_protocol_static_request_instance = InternetAccessRoutingProtocolStaticRequest.from_json(json)
# print the JSON string representation of the object
print(InternetAccessRoutingProtocolStaticRequest.to_json())

# convert the object into a dict
internet_access_routing_protocol_static_request_dict = internet_access_routing_protocol_static_request_instance.to_dict()
# create an instance of InternetAccessRoutingProtocolStaticRequest from a dict
internet_access_routing_protocol_static_request_from_dict = InternetAccessRoutingProtocolStaticRequest.from_dict(internet_access_routing_protocol_static_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


