# IpBlockChangeLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date_time** | **datetime** |  | 
**updated_date_time** | **datetime** |  | [optional] 
**deleted_date_time** | **datetime** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.ip_block_change_log import IpBlockChangeLog

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockChangeLog from a JSON string
ip_block_change_log_instance = IpBlockChangeLog.from_json(json)
# print the JSON string representation of the object
print(IpBlockChangeLog.to_json())

# convert the object into a dict
ip_block_change_log_dict = ip_block_change_log_instance.to_dict()
# create an instance of IpBlockChangeLog from a dict
ip_block_change_log_from_dict = IpBlockChangeLog.from_dict(ip_block_change_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


