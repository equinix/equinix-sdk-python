# MoveHardwareReservationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.move_hardware_reservation_request import MoveHardwareReservationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MoveHardwareReservationRequest from a JSON string
move_hardware_reservation_request_instance = MoveHardwareReservationRequest.from_json(json)
# print the JSON string representation of the object
print(MoveHardwareReservationRequest.to_json())

# convert the object into a dict
move_hardware_reservation_request_dict = move_hardware_reservation_request_instance.to_dict()
# create an instance of MoveHardwareReservationRequest from a dict
move_hardware_reservation_request_form_dict = move_hardware_reservation_request.from_dict(move_hardware_reservation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


