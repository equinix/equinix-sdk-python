# IPReservationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**ip_addresses** | [**List[IPReservationListIpAddressesInner]**](IPReservationListIpAddressesInner.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from equinix_metal.models.ip_reservation_list import IPReservationList

# TODO update the JSON string below
json = "{}"
# create an instance of IPReservationList from a JSON string
ip_reservation_list_instance = IPReservationList.from_json(json)
# print the JSON string representation of the object
print(IPReservationList.to_json())

# convert the object into a dict
ip_reservation_list_dict = ip_reservation_list_instance.to_dict()
# create an instance of IPReservationList from a dict
ip_reservation_list_form_dict = ip_reservation_list.from_dict(ip_reservation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


