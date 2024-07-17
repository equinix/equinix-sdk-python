# VirtualPortRedundancy

Specifications for redundant connections, which improve service continuity by routing traffic to secondary ports when primary ports are unavailable. <br> Redundancy increases resilience and boosts site reliability scores.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Parameter showing whether redundancy is mandatory. The default is false. | [optional] [default to False]

## Example

```python
from equinix.services.fabricv4.models.virtual_port_redundancy import VirtualPortRedundancy

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPortRedundancy from a JSON string
virtual_port_redundancy_instance = VirtualPortRedundancy.from_json(json)
# print the JSON string representation of the object
print(VirtualPortRedundancy.to_json())

# convert the object into a dict
virtual_port_redundancy_dict = virtual_port_redundancy_instance.to_dict()
# create an instance of VirtualPortRedundancy from a dict
virtual_port_redundancy_form_dict = virtual_port_redundancy.from_dict(virtual_port_redundancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


