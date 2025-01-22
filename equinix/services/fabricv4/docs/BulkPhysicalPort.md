# BulkPhysicalPort

Add to Lag request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PhysicalPort]**](PhysicalPort.md) | add physical ports to virtual port | [optional] 

## Example

```python
from equinix.services.fabricv4.models.bulk_physical_port import BulkPhysicalPort

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPhysicalPort from a JSON string
bulk_physical_port_instance = BulkPhysicalPort.from_json(json)
# print the JSON string representation of the object
print(BulkPhysicalPort.to_json())

# convert the object into a dict
bulk_physical_port_dict = bulk_physical_port_instance.to_dict()
# create an instance of BulkPhysicalPort from a dict
bulk_physical_port_from_dict = BulkPhysicalPort.from_dict(bulk_physical_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


