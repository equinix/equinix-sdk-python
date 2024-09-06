# BGPActionsBulkData

List of BGP Actions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[BGPActionData]**](BGPActionData.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.bgp_actions_bulk_data import BGPActionsBulkData

# TODO update the JSON string below
json = "{}"
# create an instance of BGPActionsBulkData from a JSON string
bgp_actions_bulk_data_instance = BGPActionsBulkData.from_json(json)
# print the JSON string representation of the object
print(BGPActionsBulkData.to_json())

# convert the object into a dict
bgp_actions_bulk_data_dict = bgp_actions_bulk_data_instance.to_dict()
# create an instance of BGPActionsBulkData from a dict
bgp_actions_bulk_data_from_dict = BGPActionsBulkData.from_dict(bgp_actions_bulk_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


