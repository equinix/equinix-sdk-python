# CrossConnectContactPreference

Cross Connect Contact Preference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | Timezone. | [optional] 
**availability** | [**CrossConnectContactAvailability**](CrossConnectContactAvailability.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_contact_preference import CrossConnectContactPreference

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectContactPreference from a JSON string
cross_connect_contact_preference_instance = CrossConnectContactPreference.from_json(json)
# print the JSON string representation of the object
print(CrossConnectContactPreference.to_json())

# convert the object into a dict
cross_connect_contact_preference_dict = cross_connect_contact_preference_instance.to_dict()
# create an instance of CrossConnectContactPreference from a dict
cross_connect_contact_preference_from_dict = CrossConnectContactPreference.from_dict(cross_connect_contact_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


