# CompanyProfileChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_date_time** | **datetime** |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_profile_change import CompanyProfileChange

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileChange from a JSON string
company_profile_change_instance = CompanyProfileChange.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileChange.to_json())

# convert the object into a dict
company_profile_change_dict = company_profile_change_instance.to_dict()
# create an instance of CompanyProfileChange from a dict
company_profile_change_from_dict = CompanyProfileChange.from_dict(company_profile_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


