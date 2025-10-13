# TimeServiceOperation

time service operational data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operational_status** | [**TimeServiceOperationOperationalStatus**](TimeServiceOperationOperationalStatus.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.time_service_operation import TimeServiceOperation

# TODO update the JSON string below
json = "{}"
# create an instance of TimeServiceOperation from a JSON string
time_service_operation_instance = TimeServiceOperation.from_json(json)
# print the JSON string representation of the object
print(TimeServiceOperation.to_json())

# convert the object into a dict
time_service_operation_dict = time_service_operation_instance.to_dict()
# create an instance of TimeServiceOperation from a dict
time_service_operation_from_dict = TimeServiceOperation.from_dict(time_service_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


