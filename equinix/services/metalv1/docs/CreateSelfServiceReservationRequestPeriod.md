# CreateSelfServiceReservationRequestPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.create_self_service_reservation_request_period import CreateSelfServiceReservationRequestPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSelfServiceReservationRequestPeriod from a JSON string
create_self_service_reservation_request_period_instance = CreateSelfServiceReservationRequestPeriod.from_json(json)
# print the JSON string representation of the object
print(CreateSelfServiceReservationRequestPeriod.to_json())

# convert the object into a dict
create_self_service_reservation_request_period_dict = create_self_service_reservation_request_period_instance.to_dict()
# create an instance of CreateSelfServiceReservationRequestPeriod from a dict
create_self_service_reservation_request_period_form_dict = create_self_service_reservation_request_period.from_dict(create_self_service_reservation_request_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


