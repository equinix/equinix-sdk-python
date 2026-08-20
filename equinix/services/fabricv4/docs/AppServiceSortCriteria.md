# AppServiceSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**AppServiceSortDirection**](AppServiceSortDirection.md) |  | [optional] [default to AppServiceSortDirection.DESC]
**var_property** | **str** | Possible field names to use on &#39;400_InvalidSorting&#39;:   * &#x60;/name&#x60; - App Service name   * &#x60;/uuid&#x60; - App Service uuid   * &#x60;/state&#x60; - App Service status   * &#x60;/changeLog/createdDateTime&#x60; - Date and time when change flow starts   * &#x60;/changeLog/updatedDateTime&#x60; - Date and time when change object is updated  | [optional] [default to '/changeLog/updatedDateTime']

## Example

```python
from equinix.services.fabricv4.models.app_service_sort_criteria import AppServiceSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceSortCriteria from a JSON string
app_service_sort_criteria_instance = AppServiceSortCriteria.from_json(json)
# print the JSON string representation of the object
print(AppServiceSortCriteria.to_json())

# convert the object into a dict
app_service_sort_criteria_dict = app_service_sort_criteria_instance.to_dict()
# create an instance of AppServiceSortCriteria from a dict
app_service_sort_criteria_from_dict = AppServiceSortCriteria.from_dict(app_service_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


