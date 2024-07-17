# Port

Port is the Request Object for Creating Fabric Ports

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PortType**](PortType.md) |  | 
**id** | **int** | Equinix assigned response attribute for Port Id | [optional] 
**href** | **str** | Equinix assigned response attribute for an absolute URL that is the subject of the link&#39;s context. | [optional] [readonly] 
**uuid** | **str** | Equinix assigned response attribute for  port identifier | [optional] 
**name** | **str** | Equinix assigned response attribute for Port name | [optional] 
**description** | **str** | Equinix assigned response attribute for Port description | [optional] 
**physical_ports_speed** | **int** | Physical Ports Speed in Mbps | 
**connections_count** | **int** | Equinix assigned response attribute for Connection count | [optional] 
**physical_ports_type** | [**PortResponsePhysicalPortsType**](PortResponsePhysicalPortsType.md) |  | 
**physical_ports_count** | **int** |  | [optional] 
**connectivity_source_type** | [**PortResponseConnectivitySourceType**](PortResponseConnectivitySourceType.md) |  | 
**bmmr_type** | [**PortResponseBmmrType**](PortResponseBmmrType.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**state** | [**PortState**](PortState.md) |  | [optional] 
**order** | [**PortOrder**](PortOrder.md) |  | [optional] 
**cvp_id** | **str** | Equinix assigned response attribute for Unique ID for a virtual port. | [optional] 
**operation** | [**PortOperation**](PortOperation.md) |  | [optional] 
**account** | [**SimplifiedAccountPortResponse**](SimplifiedAccountPortResponse.md) |  | 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 
**service_type** | [**PortResponseServiceType**](PortResponseServiceType.md) |  | [optional] 
**bandwidth** | **int** | Equinix assigned response attribute for Port bandwidth in Mbps | [optional] 
**available_bandwidth** | **int** | Equinix assigned response attribute for Port available bandwidth in Mbps | [optional] 
**used_bandwidth** | **int** | Equinix assigned response attribute for Port used bandwidth in Mbps | [optional] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | 
**device** | [**PortDevice**](PortDevice.md) |  | [optional] 
**interface** | [**PortInterface**](PortInterface.md) |  | [optional] 
**demarcation_point_ibx** | **str** | A-side/Equinix ibx | [optional] 
**tether_ibx** | **str** | z-side/Equinix ibx | [optional] 
**demarcation_point** | [**PortDemarcationPoint**](PortDemarcationPoint.md) |  | [optional] 
**redundancy** | [**PortRedundancy**](PortRedundancy.md) |  | [optional] 
**encapsulation** | [**PortEncapsulation**](PortEncapsulation.md) |  | 
**lag_enabled** | **bool** | If LAG enabled | [optional] 
**lag** | [**PortLag**](PortLag.md) |  | [optional] 
**asn** | **int** | Port ASN | [optional] 
**settings** | [**PortSettings**](PortSettings.md) |  | 
**physical_port_quantity** | **int** | Number of physical ports | [optional] 
**notifications** | [**List[PortNotification]**](PortNotification.md) | Notification preferences | [optional] 
**additional_info** | [**List[PortAdditionalInfo]**](PortAdditionalInfo.md) | Port additional information | [optional] 
**physical_ports** | [**List[PhysicalPort]**](PhysicalPort.md) | Physical ports that implement this port | [optional] 
**loas** | [**List[PortLoa]**](PortLoa.md) | Port Loas | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port import Port

# TODO update the JSON string below
json = "{}"
# create an instance of Port from a JSON string
port_instance = Port.from_json(json)
# print the JSON string representation of the object
print(Port.to_json())

# convert the object into a dict
port_dict = port_instance.to_dict()
# create an instance of Port from a dict
port_form_dict = port.from_dict(port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


