# ActivateHardwareReservationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.activate_hardware_reservation_request import ActivateHardwareReservationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateHardwareReservationRequest from a JSON string
activate_hardware_reservation_request_instance = ActivateHardwareReservationRequest.from_json(json)
# print the JSON string representation of the object
print(ActivateHardwareReservationRequest.to_json())

# convert the object into a dict
activate_hardware_reservation_request_dict = activate_hardware_reservation_request_instance.to_dict()
# create an instance of ActivateHardwareReservationRequest from a dict
activate_hardware_reservation_request_form_dict = activate_hardware_reservation_request.from_dict(activate_hardware_reservation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


