# ServiceProfileSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**ServiceProfileSortDirection**](ServiceProfileSortDirection.md) |  | [optional] [default to ServiceProfileSortDirection.DESC]
**var_property** | [**ServiceProfileSortBy**](ServiceProfileSortBy.md) |  | [optional] [default to ServiceProfileSortBy.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.service_profile_sort_criteria import ServiceProfileSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileSortCriteria from a JSON string
service_profile_sort_criteria_instance = ServiceProfileSortCriteria.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileSortCriteria.to_json())

# convert the object into a dict
service_profile_sort_criteria_dict = service_profile_sort_criteria_instance.to_dict()
# create an instance of ServiceProfileSortCriteria from a dict
service_profile_sort_criteria_from_dict = ServiceProfileSortCriteria.from_dict(service_profile_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


