# PlatformChangelog

Change log

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | Created by User Key | [optional] 
**created_date_time** | **datetime** | Created by Date and Time | [optional] 
**updated_by** | **str** | Updated by User Key | [optional] 
**updated_date_time** | **datetime** | Updated by Date and Time | [optional] 
**deleted_by** | **str** | Deleted by User Key | [optional] 
**deleted_date_time** | **datetime** | Deleted by Date and Time | [optional] 

## Example

```python
from equinix.services.fabricv4.models.platform_changelog import PlatformChangelog

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformChangelog from a JSON string
platform_changelog_instance = PlatformChangelog.from_json(json)
# print the JSON string representation of the object
print(PlatformChangelog.to_json())

# convert the object into a dict
platform_changelog_dict = platform_changelog_instance.to_dict()
# create an instance of PlatformChangelog from a dict
platform_changelog_from_dict = PlatformChangelog.from_dict(platform_changelog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


