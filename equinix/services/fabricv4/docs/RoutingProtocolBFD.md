# RoutingProtocolBFD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**interval** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_bfd import RoutingProtocolBFD

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolBFD from a JSON string
routing_protocol_bfd_instance = RoutingProtocolBFD.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolBFD.to_json())

# convert the object into a dict
routing_protocol_bfd_dict = routing_protocol_bfd_instance.to_dict()
# create an instance of RoutingProtocolBFD from a dict
routing_protocol_bfd_form_dict = routing_protocol_bfd.from_dict(routing_protocol_bfd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


