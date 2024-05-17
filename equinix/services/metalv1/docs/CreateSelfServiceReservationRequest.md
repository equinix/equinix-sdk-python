# CreateSelfServiceReservationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**item** | [**List[SelfServiceReservationItemRequest]**](SelfServiceReservationItemRequest.md) |  | [optional] 
**notes** | **str** |  | [optional] 
**period** | [**CreateSelfServiceReservationRequestPeriod**](CreateSelfServiceReservationRequestPeriod.md) |  | [optional] 
**start_date** | **datetime** |  | [optional] 

## Example

```python
from equinix_metal.models.create_self_service_reservation_request import CreateSelfServiceReservationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSelfServiceReservationRequest from a JSON string
create_self_service_reservation_request_instance = CreateSelfServiceReservationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSelfServiceReservationRequest.to_json())

# convert the object into a dict
create_self_service_reservation_request_dict = create_self_service_reservation_request_instance.to_dict()
# create an instance of CreateSelfServiceReservationRequest from a dict
create_self_service_reservation_request_form_dict = create_self_service_reservation_request.from_dict(create_self_service_reservation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


