# IPReservationMetro


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.ip_reservation_metro import IPReservationMetro

# TODO update the JSON string below
json = "{}"
# create an instance of IPReservationMetro from a JSON string
ip_reservation_metro_instance = IPReservationMetro.from_json(json)
# print the JSON string representation of the object
print(IPReservationMetro.to_json())

# convert the object into a dict
ip_reservation_metro_dict = ip_reservation_metro_instance.to_dict()
# create an instance of IPReservationMetro from a dict
ip_reservation_metro_form_dict = ip_reservation_metro.from_dict(ip_reservation_metro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


