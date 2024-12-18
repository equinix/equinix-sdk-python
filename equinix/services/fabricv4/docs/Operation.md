# Operation

Operation object for router actions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_ipv4_routes_count** | **int** | IPV4 route count | [optional] 
**bgp_ipv6_routes_count** | **int** | IPV6 route count | [optional] 

## Example

```python
from equinix.services.fabricv4.models.operation import Operation

# TODO update the JSON string below
json = "{}"
# create an instance of Operation from a JSON string
operation_instance = Operation.from_json(json)
# print the JSON string representation of the object
print(Operation.to_json())

# convert the object into a dict
operation_dict = operation_instance.to_dict()
# create an instance of Operation from a dict
operation_form_dict = operation.from_dict(operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


