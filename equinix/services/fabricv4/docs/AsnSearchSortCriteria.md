# AsnSearchSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**AsnSearchSortCriteriaDirection**](AsnSearchSortCriteriaDirection.md) |  | [optional] [default to AsnSearchSortCriteriaDirection.DESC]
**var_property** | **str** | Possible field names to use on sorting | [optional] [default to '/changeLog/updatedDateTime']

## Example

```python
from equinix.services.fabricv4.models.asn_search_sort_criteria import AsnSearchSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of AsnSearchSortCriteria from a JSON string
asn_search_sort_criteria_instance = AsnSearchSortCriteria.from_json(json)
# print the JSON string representation of the object
print(AsnSearchSortCriteria.to_json())

# convert the object into a dict
asn_search_sort_criteria_dict = asn_search_sort_criteria_instance.to_dict()
# create an instance of AsnSearchSortCriteria from a dict
asn_search_sort_criteria_from_dict = AsnSearchSortCriteria.from_dict(asn_search_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


