# BGPConnectionOperation

BGP IPv4 or IPv6 Connection State operational data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operational_status** | [**BGPConnectionOperationOperationalStatus**](BGPConnectionOperationOperationalStatus.md) |  | [optional] 
**op_status_changed_at** | **datetime** | Last BGP State Update by Date and Time | [optional] 

## Example

```python
from equinix.services.fabricv4.models.bgp_connection_operation import BGPConnectionOperation

# TODO update the JSON string below
json = "{}"
# create an instance of BGPConnectionOperation from a JSON string
bgp_connection_operation_instance = BGPConnectionOperation.from_json(json)
# print the JSON string representation of the object
print(BGPConnectionOperation.to_json())

# convert the object into a dict
bgp_connection_operation_dict = bgp_connection_operation_instance.to_dict()
# create an instance of BGPConnectionOperation from a dict
bgp_connection_operation_form_dict = bgp_connection_operation.from_dict(bgp_connection_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


