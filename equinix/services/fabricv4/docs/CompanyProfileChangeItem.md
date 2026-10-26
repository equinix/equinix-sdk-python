# CompanyProfileChangeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | Handy shortcut for operation name | 
**path** | **str** | path inside document leading to updated parameter | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.company_profile_change_item import CompanyProfileChangeItem

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileChangeItem from a JSON string
company_profile_change_item_instance = CompanyProfileChangeItem.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileChangeItem.to_json())

# convert the object into a dict
company_profile_change_item_dict = company_profile_change_item_instance.to_dict()
# create an instance of CompanyProfileChangeItem from a dict
company_profile_change_item_from_dict = CompanyProfileChangeItem.from_dict(company_profile_change_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


