# ConnectionOperation

Connection type-specific operational data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_status** | [**ProviderStatus**](ProviderStatus.md) |  | [optional] 
**equinix_status** | [**EquinixStatus**](EquinixStatus.md) |  | [optional] 
**operational_status** | [**ConnectionOperationOperationalStatus**](ConnectionOperationOperationalStatus.md) |  | [optional] 
**errors** | [**List[Error]**](Error.md) |  | [optional] 
**op_status_changed_at** | **datetime** | When connection transitioned into current operational status | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_operation import ConnectionOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionOperation from a JSON string
connection_operation_instance = ConnectionOperation.from_json(json)
# print the JSON string representation of the object
print(ConnectionOperation.to_json())

# convert the object into a dict
connection_operation_dict = connection_operation_instance.to_dict()
# create an instance of ConnectionOperation from a dict
connection_operation_from_dict = ConnectionOperation.from_dict(connection_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


