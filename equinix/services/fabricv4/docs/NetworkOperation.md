# NetworkOperation

Network operational data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equinix_status** | [**NetworkEquinixStatus**](NetworkEquinixStatus.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.network_operation import NetworkOperation

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkOperation from a JSON string
network_operation_instance = NetworkOperation.from_json(json)
# print the JSON string representation of the object
print(NetworkOperation.to_json())

# convert the object into a dict
network_operation_dict = network_operation_instance.to_dict()
# create an instance of NetworkOperation from a dict
network_operation_from_dict = NetworkOperation.from_dict(network_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


