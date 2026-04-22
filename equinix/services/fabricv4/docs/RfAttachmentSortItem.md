# RfAttachmentSortItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**RfAttachmentSortItemProperty**](RfAttachmentSortItemProperty.md) |  | [optional] [default to RfAttachmentSortItemProperty.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]
**direction** | [**SortItemDirection**](SortItemDirection.md) |  | [optional] [default to SortItemDirection.DESC]

## Example

```python
from equinix.services.fabricv4.models.rf_attachment_sort_item import RfAttachmentSortItem

# TODO update the JSON string below
json = "{}"
# create an instance of RfAttachmentSortItem from a JSON string
rf_attachment_sort_item_instance = RfAttachmentSortItem.from_json(json)
# print the JSON string representation of the object
print(RfAttachmentSortItem.to_json())

# convert the object into a dict
rf_attachment_sort_item_dict = rf_attachment_sort_item_instance.to_dict()
# create an instance of RfAttachmentSortItem from a dict
rf_attachment_sort_item_from_dict = RfAttachmentSortItem.from_dict(rf_attachment_sort_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


