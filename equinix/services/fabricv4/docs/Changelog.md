# Changelog

Change log

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | Created by User Key | [optional] 
**created_by_full_name** | **str** | Created by User Full Name | [optional] 
**created_by_email** | **str** | Created by User Email Address | [optional] 
**created_date_time** | **datetime** | Created by Date and Time | [optional] 
**updated_by** | **str** | Updated by User Key | [optional] 
**updated_by_full_name** | **str** | Updated by User Full Name | [optional] 
**updated_by_email** | **str** | Updated by User Email Address | [optional] 
**updated_date_time** | **datetime** | Updated by Date and Time | [optional] 
**deleted_by** | **str** | Deleted by User Key | [optional] 
**deleted_by_full_name** | **str** | Deleted by User Full Name | [optional] 
**deleted_by_email** | **str** | Deleted by User Email Address | [optional] 
**deleted_date_time** | **datetime** | Deleted by Date and Time | [optional] 

## Example

```python
from equinix.services.fabricv4.models.changelog import Changelog

# TODO update the JSON string below
json = "{}"
# create an instance of Changelog from a JSON string
changelog_instance = Changelog.from_json(json)
# print the JSON string representation of the object
print(Changelog.to_json())

# convert the object into a dict
changelog_dict = changelog_instance.to_dict()
# create an instance of Changelog from a dict
changelog_form_dict = changelog.from_dict(changelog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


