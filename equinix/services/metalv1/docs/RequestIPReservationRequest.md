# RequestIPReservationRequest


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
**type** | **str** | Must be set to &#39;vrf&#39; | 
**cidr** | **int** | The size of the VRF IP Reservation&#39;s subnet | 
**network** | **str** | The starting address for this VRF IP Reservation&#39;s subnet | 
**vrf_id** | **str** | The ID of the VRF in which this VRF IP Reservation is created. The VRF must have an existing IP Range that contains the requested subnet. This field may be aliased as just &#39;vrf&#39;. | 

## Example

```python
from equinix_metal.models.request_ip_reservation_request import RequestIPReservationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestIPReservationRequest from a JSON string
request_ip_reservation_request_instance = RequestIPReservationRequest.from_json(json)
# print the JSON string representation of the object
print(RequestIPReservationRequest.to_json())

# convert the object into a dict
request_ip_reservation_request_dict = request_ip_reservation_request_instance.to_dict()
# create an instance of RequestIPReservationRequest from a dict
request_ip_reservation_request_form_dict = request_ip_reservation_request.from_dict(request_ip_reservation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


