# VirtualPortConfiguration

Port configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyout** | **bool** | Buyout (true) or standard (false) configuration of the port at this access point. &lt;br&gt; Buyout ports offer free, unlimited connections. Standard ports do not. The default is false. | [optional] [default to False]

## Example

```python
from equinix.services.fabricv4.models.virtual_port_configuration import VirtualPortConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPortConfiguration from a JSON string
virtual_port_configuration_instance = VirtualPortConfiguration.from_json(json)
# print the JSON string representation of the object
print(VirtualPortConfiguration.to_json())

# convert the object into a dict
virtual_port_configuration_dict = virtual_port_configuration_instance.to_dict()
# create an instance of VirtualPortConfiguration from a dict
virtual_port_configuration_from_dict = VirtualPortConfiguration.from_dict(virtual_port_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


