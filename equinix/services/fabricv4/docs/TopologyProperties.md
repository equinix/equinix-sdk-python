# TopologyProperties

TopologyProperties is a schema that defines the properties of a topology in the orchestrator. It includes the element ID and any dependencies that the topology may have. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**element_id** | **str** |  | 
**depends_on** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.topology_properties import TopologyProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TopologyProperties from a JSON string
topology_properties_instance = TopologyProperties.from_json(json)
# print the JSON string representation of the object
print(TopologyProperties.to_json())

# convert the object into a dict
topology_properties_dict = topology_properties_instance.to_dict()
# create an instance of TopologyProperties from a dict
topology_properties_from_dict = TopologyProperties.from_dict(topology_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


