# ConnectedMetro

Arrays of objects containing latency data for the specified metros

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The Canonical URL at which the resource resides. | [optional] 
**code** | **str** | Code assigned to an Equinix International Business Exchange (IBX) data center in a specified metropolitan area. | [optional] 
**avg_latency** | **float** | Average latency (in milliseconds[ms]) between two specified metros. | [optional] 
**remote_vc_bandwidth_max** | **int** | This field holds the Max Connection speed with connected metros | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connected_metro import ConnectedMetro

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedMetro from a JSON string
connected_metro_instance = ConnectedMetro.from_json(json)
# print the JSON string representation of the object
print(ConnectedMetro.to_json())

# convert the object into a dict
connected_metro_dict = connected_metro_instance.to_dict()
# create an instance of ConnectedMetro from a dict
connected_metro_form_dict = connected_metro.from_dict(connected_metro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


