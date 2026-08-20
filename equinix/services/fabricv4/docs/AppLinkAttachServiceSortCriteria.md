# AppLinkAttachServiceSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**AppLinkAttachServiceSortDirection**](AppLinkAttachServiceSortDirection.md) |  | [optional] [default to AppLinkAttachServiceSortDirection.DESC]
**var_property** | **str** | Possible field names to use on &#39;400_InvalidSorting&#39;:   * &#x60;/uuid&#x60; - App Service attach to App Link uuid   * &#x60;/attachmentStatus&#x60; - App Service attach to App Link status   * &#x60;/changeLog/createdDateTime&#x60; - Date and time when change flow starts   * &#x60;/changeLog/updatedDateTime&#x60; - Date and time when change object is updated  | [optional] [default to '/changeLog/updatedDateTime']

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_service_sort_criteria import AppLinkAttachServiceSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachServiceSortCriteria from a JSON string
app_link_attach_service_sort_criteria_instance = AppLinkAttachServiceSortCriteria.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachServiceSortCriteria.to_json())

# convert the object into a dict
app_link_attach_service_sort_criteria_dict = app_link_attach_service_sort_criteria_instance.to_dict()
# create an instance of AppLinkAttachServiceSortCriteria from a dict
app_link_attach_service_sort_criteria_from_dict = AppLinkAttachServiceSortCriteria.from_dict(app_link_attach_service_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


