# RaAttachmentSortItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**RaAttachmentSortItemProperty**](RaAttachmentSortItemProperty.md) |  | [optional] [default to RaAttachmentSortItemProperty.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]
**direction** | [**SortItemDirection**](SortItemDirection.md) |  | [optional] [default to SortItemDirection.DESC]

## Example

```python
from equinix.services.fabricv4.models.ra_attachment_sort_item import RaAttachmentSortItem

# TODO update the JSON string below
json = "{}"
# create an instance of RaAttachmentSortItem from a JSON string
ra_attachment_sort_item_instance = RaAttachmentSortItem.from_json(json)
# print the JSON string representation of the object
print(RaAttachmentSortItem.to_json())

# convert the object into a dict
ra_attachment_sort_item_dict = ra_attachment_sort_item_instance.to_dict()
# create an instance of RaAttachmentSortItem from a dict
ra_attachment_sort_item_from_dict = RaAttachmentSortItem.from_dict(ra_attachment_sort_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


