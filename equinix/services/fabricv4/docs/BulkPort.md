# BulkPort

Create bulk port request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Port]**](Port.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.bulk_port import BulkPort

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPort from a JSON string
bulk_port_instance = BulkPort.from_json(json)
# print the JSON string representation of the object
print(BulkPort.to_json())

# convert the object into a dict
bulk_port_dict = bulk_port_instance.to_dict()
# create an instance of BulkPort from a dict
bulk_port_form_dict = bulk_port.from_dict(bulk_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


