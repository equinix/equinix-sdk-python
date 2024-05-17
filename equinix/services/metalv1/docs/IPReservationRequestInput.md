# IPReservationRequestInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** |  | [optional] 
**customdata** | **object** |  | [optional] 
**details** | **str** |  | [optional] 
**facility** | **str** |  | [optional] 
**fail_on_approval_required** | **bool** |  | [optional] 
**href** | **str** |  | [optional] 
**metro** | **str** | The code of the metro you are requesting the IP reservation in. | [optional] 
**quantity** | **int** |  | 
**tags** | **List[str]** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from equinix_metal.models.ip_reservation_request_input import IPReservationRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of IPReservationRequestInput from a JSON string
ip_reservation_request_input_instance = IPReservationRequestInput.from_json(json)
# print the JSON string representation of the object
print(IPReservationRequestInput.to_json())

# convert the object into a dict
ip_reservation_request_input_dict = ip_reservation_request_input_instance.to_dict()
# create an instance of IPReservationRequestInput from a dict
ip_reservation_request_input_form_dict = ip_reservation_request_input.from_dict(ip_reservation_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


