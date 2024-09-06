# NetworkConnections

List of network changes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[Connection]**](Connection.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.network_connections import NetworkConnections

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkConnections from a JSON string
network_connections_instance = NetworkConnections.from_json(json)
# print the JSON string representation of the object
print(NetworkConnections.to_json())

# convert the object into a dict
network_connections_dict = network_connections_instance.to_dict()
# create an instance of NetworkConnections from a dict
network_connections_from_dict = NetworkConnections.from_dict(network_connections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


