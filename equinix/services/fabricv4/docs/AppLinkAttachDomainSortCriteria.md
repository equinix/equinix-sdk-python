# AppLinkAttachDomainSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**AppLinkAttachDomainSortDirection**](AppLinkAttachDomainSortDirection.md) |  | [optional] [default to AppLinkAttachDomainSortDirection.DESC]
**var_property** | **str** | Possible field names to use on &#39;400_InvalidSorting&#39;:   * &#x60;/uuid&#x60; - App Domain attach to App Link uuid   * &#x60;/attachmentStatus&#x60; - App Domain attach to App Link status   * &#x60;/changeLog/createdDateTime&#x60; - Date and time when change flow starts   * &#x60;/changeLog/updatedDateTime&#x60; - Date and time when change object is updated  | [optional] [default to '/changeLog/updatedDateTime']

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_domain_sort_criteria import AppLinkAttachDomainSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachDomainSortCriteria from a JSON string
app_link_attach_domain_sort_criteria_instance = AppLinkAttachDomainSortCriteria.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachDomainSortCriteria.to_json())

# convert the object into a dict
app_link_attach_domain_sort_criteria_dict = app_link_attach_domain_sort_criteria_instance.to_dict()
# create an instance of AppLinkAttachDomainSortCriteria from a dict
app_link_attach_domain_sort_criteria_from_dict = AppLinkAttachDomainSortCriteria.from_dict(app_link_attach_domain_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


