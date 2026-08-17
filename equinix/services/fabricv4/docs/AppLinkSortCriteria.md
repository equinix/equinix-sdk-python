# AppLinkSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**AppLinkSortDirection**](AppLinkSortDirection.md) |  | [optional] [default to AppLinkSortDirection.DESC]
**var_property** | **str** | Possible field names to use on &#39;400_InvalidSorting&#39;:   * &#x60;/name&#x60; - App Link name   * &#x60;/uuid&#x60; - App Link uuid   * &#x60;/state&#x60; - App Link status   * &#x60;/changeLog/createdDateTime&#x60; - Date and time when change flow starts   * &#x60;/changeLog/updatedDateTime&#x60; - Date and time when change object is updated  | [optional] [default to '/changeLog/updatedDateTime']

## Example

```python
from equinix.services.fabricv4.models.app_link_sort_criteria import AppLinkSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkSortCriteria from a JSON string
app_link_sort_criteria_instance = AppLinkSortCriteria.from_json(json)
# print the JSON string representation of the object
print(AppLinkSortCriteria.to_json())

# convert the object into a dict
app_link_sort_criteria_dict = app_link_sort_criteria_instance.to_dict()
# create an instance of AppLinkSortCriteria from a dict
app_link_sort_criteria_from_dict = AppLinkSortCriteria.from_dict(app_link_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


