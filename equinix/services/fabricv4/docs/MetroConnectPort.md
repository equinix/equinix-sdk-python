# MetroConnectPort

Metro Connect Port

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | **str** | Port Type | [optional] 
**uuid** | **str** |  | [optional] [readonly] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metro_connect_port import MetroConnectPort

# TODO update the JSON string below
json = "{}"
# create an instance of MetroConnectPort from a JSON string
metro_connect_port_instance = MetroConnectPort.from_json(json)
# print the JSON string representation of the object
print(MetroConnectPort.to_json())

# convert the object into a dict
metro_connect_port_dict = metro_connect_port_instance.to_dict()
# create an instance of MetroConnectPort from a dict
metro_connect_port_from_dict = MetroConnectPort.from_dict(metro_connect_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


