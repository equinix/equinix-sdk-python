# IpBlockFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[IpBlockAndQuery]**](IpBlockAndQuery.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.ip_block_filter import IpBlockFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockFilter from a JSON string
ip_block_filter_instance = IpBlockFilter.from_json(json)
# print the JSON string representation of the object
print(IpBlockFilter.to_json())

# convert the object into a dict
ip_block_filter_dict = ip_block_filter_instance.to_dict()
# create an instance of IpBlockFilter from a dict
ip_block_filter_from_dict = IpBlockFilter.from_dict(ip_block_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


