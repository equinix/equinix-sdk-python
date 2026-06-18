# InternetAccessRoutingProtocolDirectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[InternetAccessConnectionDirectRequest]**](InternetAccessConnectionDirectRequest.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_routing_protocol_direct_request import InternetAccessRoutingProtocolDirectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessRoutingProtocolDirectRequest from a JSON string
internet_access_routing_protocol_direct_request_instance = InternetAccessRoutingProtocolDirectRequest.from_json(json)
# print the JSON string representation of the object
print(InternetAccessRoutingProtocolDirectRequest.to_json())

# convert the object into a dict
internet_access_routing_protocol_direct_request_dict = internet_access_routing_protocol_direct_request_instance.to_dict()
# create an instance of InternetAccessRoutingProtocolDirectRequest from a dict
internet_access_routing_protocol_direct_request_from_dict = InternetAccessRoutingProtocolDirectRequest.from_dict(internet_access_routing_protocol_direct_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


