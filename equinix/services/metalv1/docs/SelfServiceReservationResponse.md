# SelfServiceReservationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**href** | **str** |  | [optional] 
**item** | [**List[SelfServiceReservationItemResponse]**](SelfServiceReservationItemResponse.md) |  | [optional] 
**notes** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**period** | [**CreateSelfServiceReservationRequestPeriod**](CreateSelfServiceReservationRequestPeriod.md) |  | [optional] 
**project** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**total_cost** | **int** |  | [optional] 

## Example

```python
from equinix_metal.models.self_service_reservation_response import SelfServiceReservationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SelfServiceReservationResponse from a JSON string
self_service_reservation_response_instance = SelfServiceReservationResponse.from_json(json)
# print the JSON string representation of the object
print(SelfServiceReservationResponse.to_json())

# convert the object into a dict
self_service_reservation_response_dict = self_service_reservation_response_instance.to_dict()
# create an instance of SelfServiceReservationResponse from a dict
self_service_reservation_response_form_dict = self_service_reservation_response.from_dict(self_service_reservation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


