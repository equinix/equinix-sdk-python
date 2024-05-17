# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[DeviceActionsInner]**](DeviceActionsInner.md) | Actions supported by the device instance. | [optional] 
**always_pxe** | **bool** |  | [optional] 
**billing_cycle** | **str** |  | [optional] 
**bonding_mode** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | [**DeviceCreatedBy**](DeviceCreatedBy.md) |  | [optional] 
**customdata** | **Dict[str, object]** |  | [optional] 
**description** | **str** |  | [optional] 
**facility** | [**Facility**](Facility.md) |  | [optional] 
**firmware_set_id** | **str** | The UUID of the firmware set to associate with the device. | [optional] 
**hardware_reservation** | [**HardwareReservation**](HardwareReservation.md) |  | [optional] 
**hostname** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**ip_addresses** | [**List[IPAssignment]**](IPAssignment.md) |  | [optional] 
**ipxe_script_url** | **str** |  | [optional] 
**iqn** | **str** |  | [optional] 
**locked** | **bool** | Prevents accidental deletion of this resource when set to true. | [optional] 
**metro** | [**DeviceMetro**](DeviceMetro.md) |  | [optional] 
**network_frozen** | **bool** | Whether network mode changes such as converting to/from Layer2 or Layer3 networking, bonding or disbonding network interfaces are permitted for the device. | [optional] 
**network_ports** | [**List[Port]**](Port.md) | By default, servers at Equinix Metal are configured in a “bonded” mode using LACP (Link Aggregation Control Protocol). Each 2-NIC server is configured with a single bond (namely bond0) with both interfaces eth0 and eth1 as members of the bond in a default Layer 3 mode. Some device plans may have a different number of ports and bonds available. | [optional] 
**operating_system** | [**OperatingSystem**](OperatingSystem.md) |  | [optional] 
**plan** | [**Plan**](Plan.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**project_lite** | [**DeviceProjectLite**](DeviceProjectLite.md) |  | [optional] 
**provisioning_events** | [**List[Event]**](Event.md) |  | [optional] 
**provisioning_percentage** | **float** | Only visible while device provisioning | [optional] 
**root_password** | **str** | Root password is automatically generated when server is provisioned and it is removed after 24 hours | [optional] 
**short_id** | **str** |  | [optional] 
**sos** | **str** | Hostname used to connect to the instance via the SOS (Serial over SSH) out-of-band console. | [optional] 
**spot_instance** | **bool** | Whether or not the device is a spot instance. | [optional] 
**spot_price_max** | **float** | The maximum price per hour you are willing to pay to keep this spot instance.  If you are outbid, the termination will be set allowing two minutes before shutdown. | [optional] 
**ssh_keys** | [**List[Href]**](Href.md) |  | [optional] 
**state** | **str** | The current state the instance is in.  * When an instance is initially created it will be in the &#x60;queued&#x60; state until it is picked up by the provisioner. * Once provisioning has begun on the instance it&#39;s state will move to &#x60;provisioning&#x60;. * When an instance is deleted, it will move to &#x60;deprovisioning&#x60; state until the deprovision is completed and the instance state moves to &#x60;deleted&#x60;. * If an instance fails to provision or deprovision it will move to &#x60;failed&#x60; state. * Once an instance has completed provisioning it will move to &#x60;active&#x60; state. * If an instance is currently powering off or powering on it will move to &#x60;powering_off&#x60; or &#x60;powering_on&#x60; states respectively.  * When the instance is powered off completely it will move to the &#x60;inactive&#x60; state. * When an instance is powered on completely it will move to the &#x60;active&#x60; state. * Using the reinstall action to install a new OS on the instance will cause the instance state to change to &#x60;reinstalling&#x60;. * When the reinstall action is complete the instance will move to &#x60;active&#x60; state. | [optional] 
**storage** | [**Storage**](Storage.md) |  | [optional] 
**switch_uuid** | **str** | Switch short id. This can be used to determine if two devices are connected to the same switch, for example. | [optional] 
**tags** | **List[str]** |  | [optional] 
**termination_time** | **datetime** | When the device will be terminated. If you don&#39;t supply timezone info, the timestamp is assumed to be in UTC.  This is commonly set in advance for ephemeral spot market instances but this field may also be set with on-demand and reservation instances to automatically delete the resource at a given time. The termination time can also be used to release a hardware reservation instance at a given time, keeping the reservation open for other uses.  On a spot market device, the termination time will be set automatically when outbid. | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user** | **str** |  | [optional] 
**userdata** | **str** |  | [optional] 
**volumes** | [**List[Href]**](Href.md) |  | [optional] 

## Example

```python
from equinix_metal.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_form_dict = device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


