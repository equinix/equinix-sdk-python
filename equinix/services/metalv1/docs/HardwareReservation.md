# HardwareReservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**custom_rate** | **float** | Amount that will be charged for every billing_cycle. | [optional] 
**device** | [**Device**](Device.md) |  | [optional] 
**facility** | [**Facility**](Facility.md) |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**need_of_service** | **bool** | Whether this Device requires assistance from Equinix Metal. | [optional] 
**plan** | [**Plan**](Plan.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**provisionable** | **bool** | Whether the reserved server is provisionable or not. Spare devices can&#39;t be provisioned unless they are activated first. | [optional] 
**short_id** | **str** | Short version of the ID. | [optional] 
**spare** | **bool** | Whether the Hardware Reservation is a spare. Spare Hardware Reservations are used when a Hardware Reservations requires service from Equinix Metal | [optional] 
**switch_uuid** | **str** | Switch short id. This can be used to determine if two devices are connected to the same switch, for example. | [optional] 
**termination_time** | **datetime** | Expiration date for the reservation. | [optional] 

## Example

```python
from equinix_metal.models.hardware_reservation import HardwareReservation

# TODO update the JSON string below
json = "{}"
# create an instance of HardwareReservation from a JSON string
hardware_reservation_instance = HardwareReservation.from_json(json)
# print the JSON string representation of the object
print(HardwareReservation.to_json())

# convert the object into a dict
hardware_reservation_dict = hardware_reservation_instance.to_dict()
# create an instance of HardwareReservation from a dict
hardware_reservation_form_dict = hardware_reservation.from_dict(hardware_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


