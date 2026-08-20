# Sort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Property to sort by. Supported values:  * &#x60;/name&#x60; - Company profile name  * &#x60;/state&#x60; - Company profile state  * &#x60;/changeLog/updatedDateTime&#x60; - Date and time the profile was last updated  * &#x60;/changeLog/createdDateTime&#x60; - Date and time the profile was created  | [optional] 
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


