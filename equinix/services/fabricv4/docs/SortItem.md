# SortItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**SortItemProperty**](SortItemProperty.md) |  | [optional] [default to SortItemProperty.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]
**direction** | [**SortItemDirection**](SortItemDirection.md) |  | [optional] [default to SortItemDirection.DESC]

## Example

```python
from equinix.services.fabricv4.models.sort_item import SortItem

# TODO update the JSON string below
json = "{}"
# create an instance of SortItem from a JSON string
sort_item_instance = SortItem.from_json(json)
# print the JSON string representation of the object
print(SortItem.to_json())

# convert the object into a dict
sort_item_dict = sort_item_instance.to_dict()
# create an instance of SortItem from a dict
sort_item_from_dict = SortItem.from_dict(sort_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


