# BulkPortRequest

Create bulk port request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PortRequest]**](PortRequest.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.bulk_port_request import BulkPortRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPortRequest from a JSON string
bulk_port_request_instance = BulkPortRequest.from_json(json)
# print the JSON string representation of the object
print(BulkPortRequest.to_json())

# convert the object into a dict
bulk_port_request_dict = bulk_port_request_instance.to_dict()
# create an instance of BulkPortRequest from a dict
bulk_port_request_form_dict = bulk_port_request.from_dict(bulk_port_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


