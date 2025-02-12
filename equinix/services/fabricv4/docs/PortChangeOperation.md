# PortChangeOperation

Port change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | Handy shortcut for operation name | 
**path** | **str** | path inside document leading to updated parameter | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.port_change_operation import PortChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of PortChangeOperation from a JSON string
port_change_operation_instance = PortChangeOperation.from_json(json)
# print the JSON string representation of the object
print(PortChangeOperation.to_json())

# convert the object into a dict
port_change_operation_dict = port_change_operation_instance.to_dict()
# create an instance of PortChangeOperation from a dict
port_change_operation_from_dict = PortChangeOperation.from_dict(port_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


