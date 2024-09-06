# VirtualPortPrice

Preferences and settings for a virtual port connected to an internet service provider (ISP) or other Equinix platform entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier assigned to the virtual port. Either the uuid or the remaining attributes must be supplied. | [optional] 
**type** | [**VirtualPortType**](VirtualPortType.md) |  | [optional] 
**location** | [**VirtualPortLocation**](VirtualPortLocation.md) |  | [optional] 
**lag** | [**LinkAggregationGroup**](LinkAggregationGroup.md) |  | [optional] 
**physical_ports_quantity** | **int** | Number of physical ports requested. The defaults is 1. | [optional] [default to 1]
**bandwidth** | **int** | Aggregated data transfer capacity,  expressed as follows &lt;br&gt; -&gt; Mbps, megabits (1 million bits) per second &lt;br&gt; -&gt; Gbps, gigabits (1 billion bits) per second &lt;br&gt; Bandwidth must be divisible by physicalPortsQuantity. | [optional] 
**redundancy** | [**VirtualPortRedundancy**](VirtualPortRedundancy.md) |  | [optional] 
**connectivity_source** | [**ConnectivitySource**](ConnectivitySource.md) |  | [optional] 
**service_type** | [**VirtualPortServiceType**](VirtualPortServiceType.md) |  | [optional] [default to VirtualPortServiceType.MSP]
**settings** | [**VirtualPortConfiguration**](VirtualPortConfiguration.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.virtual_port_price import VirtualPortPrice

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPortPrice from a JSON string
virtual_port_price_instance = VirtualPortPrice.from_json(json)
# print the JSON string representation of the object
print(VirtualPortPrice.to_json())

# convert the object into a dict
virtual_port_price_dict = virtual_port_price_instance.to_dict()
# create an instance of VirtualPortPrice from a dict
virtual_port_price_from_dict = VirtualPortPrice.from_dict(virtual_port_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


