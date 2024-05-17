# SelfServiceReservationItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metro_code** | **str** |  | [optional] 
**metro_id** | **str** |  | [optional] 
**metro_name** | **str** |  | [optional] 
**plan** | [**Plan**](Plan.md) |  | [optional] 
**plan_categories** | **List[str]** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**plan_name** | **str** |  | [optional] 
**plan_slug** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**term** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.self_service_reservation_item_response import SelfServiceReservationItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SelfServiceReservationItemResponse from a JSON string
self_service_reservation_item_response_instance = SelfServiceReservationItemResponse.from_json(json)
# print the JSON string representation of the object
print(SelfServiceReservationItemResponse.to_json())

# convert the object into a dict
self_service_reservation_item_response_dict = self_service_reservation_item_response_instance.to_dict()
# create an instance of SelfServiceReservationItemResponse from a dict
self_service_reservation_item_response_form_dict = self_service_reservation_item_response.from_dict(self_service_reservation_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


