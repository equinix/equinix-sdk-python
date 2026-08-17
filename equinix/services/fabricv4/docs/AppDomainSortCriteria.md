# AppDomainSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**AppDomainSortDirection**](AppDomainSortDirection.md) |  | [optional] [default to AppDomainSortDirection.DESC]
**var_property** | **str** | Possible field names to use on &#39;400_InvalidSorting&#39;:   * &#x60;/name&#x60; - App Domain name   * &#x60;/uuid&#x60; - App Domain uuid   * &#x60;/state&#x60; - App Domain status   * &#x60;/changeLog/createdDateTime&#x60; - Date and time when change flow starts   * &#x60;/changeLog/updatedDateTime&#x60; - Date and time when change object is updated  | [optional] [default to '/changeLog/updatedDateTime']

## Example

```python
from equinix.services.fabricv4.models.app_domain_sort_criteria import AppDomainSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of AppDomainSortCriteria from a JSON string
app_domain_sort_criteria_instance = AppDomainSortCriteria.from_json(json)
# print the JSON string representation of the object
print(AppDomainSortCriteria.to_json())

# convert the object into a dict
app_domain_sort_criteria_dict = app_domain_sort_criteria_instance.to_dict()
# create an instance of AppDomainSortCriteria from a dict
app_domain_sort_criteria_from_dict = AppDomainSortCriteria.from_dict(app_domain_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


