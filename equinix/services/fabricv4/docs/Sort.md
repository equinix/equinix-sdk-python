# Sort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Property to sort by | [optional] 
**direction** | [**CompanyProfileSortDirection**](CompanyProfileSortDirection.md) |  | [optional] [default to CompanyProfileSortDirection.ASC]

## Example

```python
from equinix.services.fabricv4.models.sort import Sort

# TODO update the JSON string below
json = "{}"
# create an instance of Sort from a JSON string
sort_instance = Sort.from_json(json)
# print the JSON string representation of the object
print(Sort.to_json())

# convert the object into a dict
sort_dict = sort_instance.to_dict()
# create an instance of Sort from a dict
sort_from_dict = Sort.from_dict(sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


