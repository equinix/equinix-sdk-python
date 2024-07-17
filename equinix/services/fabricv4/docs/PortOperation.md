# PortOperation

Operational specifications for ports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operational_status** | [**PortOperationOperationalStatus**](PortOperationOperationalStatus.md) |  | [optional] 
**connection_count** | **int** | Total number of connections. | [optional] 
**op_status_changed_at** | **datetime** | Date and time at which port availability changed. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_operation import PortOperation

# TODO update the JSON string below
json = "{}"
# create an instance of PortOperation from a JSON string
port_operation_instance = PortOperation.from_json(json)
# print the JSON string representation of the object
print(PortOperation.to_json())

# convert the object into a dict
port_operation_dict = port_operation_instance.to_dict()
# create an instance of PortOperation from a dict
port_operation_form_dict = port_operation.from_dict(port_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


