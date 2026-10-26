# ConnectionRedundancy

Connection redundancy configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Redundancy group identifier (UUID of primary connection) | [optional] 
**priority** | [**ConnectionPriority**](ConnectionPriority.md) |  | [optional] 
**name** | **str** | Customer-provided name for the redundancy group | [optional] 
**description** | **str** | Customer-provided description for the redundancy group | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_redundancy import ConnectionRedundancy

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRedundancy from a JSON string
connection_redundancy_instance = ConnectionRedundancy.from_json(json)
# print the JSON string representation of the object
print(ConnectionRedundancy.to_json())

# convert the object into a dict
connection_redundancy_dict = connection_redundancy_instance.to_dict()
# create an instance of ConnectionRedundancy from a dict
connection_redundancy_from_dict = ConnectionRedundancy.from_dict(connection_redundancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


