# AppProcessorSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**AppProcessorSortDirection**](AppProcessorSortDirection.md) |  | [optional] [default to AppProcessorSortDirection.DESC]
**var_property** | **str** | Possible field names to use on &#39;400_InvalidSorting&#39;:   * &#x60;/name&#x60; - App Processor name   * &#x60;/uuid&#x60; - App Processor uuid   * &#x60;/state&#x60; - App Processor status   * &#x60;/changeLog/createdDateTime&#x60; - Date and time when change flow starts   * &#x60;/changeLog/updatedDateTime&#x60; - Date and time when change object is updated  | [optional] [default to '/changeLog/updatedDateTime']

## Example

```python
from equinix.services.fabricv4.models.app_processor_sort_criteria import AppProcessorSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of AppProcessorSortCriteria from a JSON string
app_processor_sort_criteria_instance = AppProcessorSortCriteria.from_json(json)
# print the JSON string representation of the object
print(AppProcessorSortCriteria.to_json())

# convert the object into a dict
app_processor_sort_criteria_dict = app_processor_sort_criteria_instance.to_dict()
# create an instance of AppProcessorSortCriteria from a dict
app_processor_sort_criteria_from_dict = AppProcessorSortCriteria.from_dict(app_processor_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


