# ConnectionChangeOperation

Connection change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | Handy shortcut for operation name | 
**path** | **str** | path inside document leading to updated parameter | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.connection_change_operation import ConnectionChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionChangeOperation from a JSON string
connection_change_operation_instance = ConnectionChangeOperation.from_json(json)
# print the JSON string representation of the object
print(ConnectionChangeOperation.to_json())

# convert the object into a dict
connection_change_operation_dict = connection_change_operation_instance.to_dict()
# create an instance of ConnectionChangeOperation from a dict
connection_change_operation_form_dict = connection_change_operation.from_dict(connection_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


