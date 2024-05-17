# HardwareReservationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardware_reservations** | [**List[HardwareReservation]**](HardwareReservation.md) |  | [optional] 
**href** | **str** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from equinix_metal.models.hardware_reservation_list import HardwareReservationList

# TODO update the JSON string below
json = "{}"
# create an instance of HardwareReservationList from a JSON string
hardware_reservation_list_instance = HardwareReservationList.from_json(json)
# print the JSON string representation of the object
print(HardwareReservationList.to_json())

# convert the object into a dict
hardware_reservation_list_dict = hardware_reservation_list_instance.to_dict()
# create an instance of HardwareReservationList from a dict
hardware_reservation_list_form_dict = hardware_reservation_list.from_dict(hardware_reservation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


