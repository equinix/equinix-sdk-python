# CrossConnectChangelog

Cross Connect Change Log.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date_time** | **datetime** | Created Date and Time. | [optional] 
**created_by** | **str** | User key of the user who created the resource. | [optional] 
**updated_date_time** | **datetime** | Updated Date and Time. | [optional] 
**updated_by** | **str** | User key of the user who last updated the resource. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_changelog import CrossConnectChangelog

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectChangelog from a JSON string
cross_connect_changelog_instance = CrossConnectChangelog.from_json(json)
# print the JSON string representation of the object
print(CrossConnectChangelog.to_json())

# convert the object into a dict
cross_connect_changelog_dict = cross_connect_changelog_instance.to_dict()
# create an instance of CrossConnectChangelog from a dict
cross_connect_changelog_from_dict = CrossConnectChangelog.from_dict(cross_connect_changelog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


