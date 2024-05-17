# Raid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | **List[str]** |  | [optional] 
**href** | **str** |  | [optional] 
**level** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.raid import Raid

# TODO update the JSON string below
json = "{}"
# create an instance of Raid from a JSON string
raid_instance = Raid.from_json(json)
# print the JSON string representation of the object
print(Raid.to_json())

# convert the object into a dict
raid_dict = raid_instance.to_dict()
# create an instance of Raid from a dict
raid_form_dict = raid.from_dict(raid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


