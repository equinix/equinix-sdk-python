# SelfServiceReservationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**reservations** | [**List[SelfServiceReservationResponse]**](SelfServiceReservationResponse.md) |  | [optional] 

## Example

```python
from equinix_metal.models.self_service_reservation_list import SelfServiceReservationList

# TODO update the JSON string below
json = "{}"
# create an instance of SelfServiceReservationList from a JSON string
self_service_reservation_list_instance = SelfServiceReservationList.from_json(json)
# print the JSON string representation of the object
print(SelfServiceReservationList.to_json())

# convert the object into a dict
self_service_reservation_list_dict = self_service_reservation_list_instance.to_dict()
# create an instance of SelfServiceReservationList from a dict
self_service_reservation_list_form_dict = self_service_reservation_list.from_dict(self_service_reservation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


