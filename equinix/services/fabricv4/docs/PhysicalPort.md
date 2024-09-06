# PhysicalPort

Physical Port specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PhysicalPortType**](PhysicalPortType.md) |  | [optional] 
**id** | **int** | Equinix assigned response attribute for Physical Port Id | [optional] 
**href** | **str** | Equinix assigned response attribute for an absolute URL that is the subject of the link&#39;s context. | [optional] [readonly] 
**state** | [**PortState**](PortState.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**interface_speed** | **int** | Physical Port Speed in Mbps | [optional] 
**interface_type** | **str** | Physical Port Interface Type | [optional] 
**tether** | [**PortTether**](PortTether.md) |  | [optional] 
**demarcation_point** | [**PortDemarcationPoint**](PortDemarcationPoint.md) |  | [optional] 
**notifications** | [**List[PortNotification]**](PortNotification.md) | Notification preferences | [optional] 
**additional_info** | [**List[PortAdditionalInfo]**](PortAdditionalInfo.md) | Physical Port additional information | [optional] 
**order** | [**PortOrder**](PortOrder.md) |  | [optional] 
**operation** | [**PortOperation**](PortOperation.md) |  | [optional] 
**loas** | [**List[PortLoa]**](PortLoa.md) | Port Loas | [optional] 

## Example

```python
from equinix.services.fabricv4.models.physical_port import PhysicalPort

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalPort from a JSON string
physical_port_instance = PhysicalPort.from_json(json)
# print the JSON string representation of the object
print(PhysicalPort.to_json())

# convert the object into a dict
physical_port_dict = physical_port_instance.to_dict()
# create an instance of PhysicalPort from a dict
physical_port_from_dict = PhysicalPort.from_dict(physical_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


