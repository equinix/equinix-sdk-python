# RoutingProtocolChangeDataResponse

List of network changes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RoutingProtocolChangeData]**](RoutingProtocolChangeData.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_change_data_response import RoutingProtocolChangeDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolChangeDataResponse from a JSON string
routing_protocol_change_data_response_instance = RoutingProtocolChangeDataResponse.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolChangeDataResponse.to_json())

# convert the object into a dict
routing_protocol_change_data_response_dict = routing_protocol_change_data_response_instance.to_dict()
# create an instance of RoutingProtocolChangeDataResponse from a dict
routing_protocol_change_data_response_from_dict = RoutingProtocolChangeDataResponse.from_dict(routing_protocol_change_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


