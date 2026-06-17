# SearchSortItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**SearchSortItemDirection**](SearchSortItemDirection.md) |  | 
**var_property** | **str** |  | 

## Example

```python
from equinix.services.fabricv4.models.search_sort_item import SearchSortItem

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSortItem from a JSON string
search_sort_item_instance = SearchSortItem.from_json(json)
# print the JSON string representation of the object
print(SearchSortItem.to_json())

# convert the object into a dict
search_sort_item_dict = search_sort_item_instance.to_dict()
# create an instance of SearchSortItem from a dict
search_sort_item_from_dict = SearchSortItem.from_dict(search_sort_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


