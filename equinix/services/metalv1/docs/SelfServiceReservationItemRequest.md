# SelfServiceReservationItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**metro_id** | **str** | Metro ID of the item. | [optional] 
**plan_id** | **str** | Plan ID of the item. | [optional] 
**quantity** | **int** | Number of items. | [optional] 
**term** | **str** | Contract term of the item. | [optional] 

## Example

```python
from equinix_metal.models.self_service_reservation_item_request import SelfServiceReservationItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SelfServiceReservationItemRequest from a JSON string
self_service_reservation_item_request_instance = SelfServiceReservationItemRequest.from_json(json)
# print the JSON string representation of the object
print(SelfServiceReservationItemRequest.to_json())

# convert the object into a dict
self_service_reservation_item_request_dict = self_service_reservation_item_request_instance.to_dict()
# create an instance of SelfServiceReservationItemRequest from a dict
self_service_reservation_item_request_form_dict = self_service_reservation_item_request.from_dict(self_service_reservation_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


