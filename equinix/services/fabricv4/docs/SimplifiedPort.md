# SimplifiedPort

Port specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PortType**](PortType.md) |  | [optional] 
**id** | **int** | Equinix assigned response attribute for Port Id | [optional] 
**href** | **str** | Equinix assigned response attribute for an absolute URL that is the subject of the link&#39;s context. | [optional] [readonly] 
**uuid** | **str** | Equinix assigned response attribute for  port identifier | [optional] 
**name** | **str** | Equinix assigned response attribute for Port name | [optional] 
**description** | **str** | Equinix assigned response attribute for Port description | [optional] 
**physical_ports_speed** | **int** | Physical Ports Speed in Mbps | [optional] 
**connections_count** | **int** | Equinix assigned response attribute for Connection count | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**state** | [**PortState**](PortState.md) |  | [optional] 
**cvp_id** | **str** | Equinix assigned response attribute for Unique ID for a virtual port. | [optional] 
**operation** | [**PortOperation**](PortOperation.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**service_type** | [**PortResponseServiceType**](PortResponseServiceType.md) |  | [optional] 
**bandwidth** | **int** | Equinix assigned response attribute for Port bandwidth in Mbps | [optional] 
**available_bandwidth** | **int** | Equinix assigned response attribute for Port available bandwidth in Mbps | [optional] 
**used_bandwidth** | **int** | Equinix assigned response attribute for Port used bandwidth in Mbps | [optional] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 
**device** | [**PortDevice**](PortDevice.md) |  | [optional] 
**interface** | [**PortInterface**](PortInterface.md) |  | [optional] 
**tether** | [**PortTether**](PortTether.md) |  | [optional] 
**demarcation_point** | [**PortDemarcationPoint**](PortDemarcationPoint.md) |  | [optional] 
**redundancy** | [**PortRedundancy**](PortRedundancy.md) |  | [optional] 
**encapsulation** | [**PortEncapsulation**](PortEncapsulation.md) |  | [optional] 
**lag_enabled** | **bool** | If LAG enabled | [optional] 
**settings** | [**PortSettings**](PortSettings.md) |  | [optional] 
**physical_port_quantity** | **int** | Number of physical ports | [optional] 
**additional_info** | [**List[PortAdditionalInfo]**](PortAdditionalInfo.md) | Port additional information | [optional] 
**physical_ports** | [**List[PhysicalPort]**](PhysicalPort.md) | Physical ports that implement this port | [optional] 

## Example

```python
from equinix.services.fabricv4.models.simplified_port import SimplifiedPort

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedPort from a JSON string
simplified_port_instance = SimplifiedPort.from_json(json)
# print the JSON string representation of the object
print(SimplifiedPort.to_json())

# convert the object into a dict
simplified_port_dict = simplified_port_instance.to_dict()
# create an instance of SimplifiedPort from a dict
simplified_port_from_dict = SimplifiedPort.from_dict(simplified_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


