# PeeringProtocolDataRouteCollectors

Route Collectors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | Primary Route Collector | [optional] 
**secondary** | **str** | Secondary Route Collector | [optional] 

## Example

```python
from equinix.services.fabricv4.models.peering_protocol_data_route_collectors import PeeringProtocolDataRouteCollectors

# TODO update the JSON string below
json = "{}"
# create an instance of PeeringProtocolDataRouteCollectors from a JSON string
peering_protocol_data_route_collectors_instance = PeeringProtocolDataRouteCollectors.from_json(json)
# print the JSON string representation of the object
print(PeeringProtocolDataRouteCollectors.to_json())

# convert the object into a dict
peering_protocol_data_route_collectors_dict = peering_protocol_data_route_collectors_instance.to_dict()
# create an instance of PeeringProtocolDataRouteCollectors from a dict
peering_protocol_data_route_collectors_from_dict = PeeringProtocolDataRouteCollectors.from_dict(peering_protocol_data_route_collectors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


