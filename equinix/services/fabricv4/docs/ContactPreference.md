# ContactPreference

Contact preference for the phone number

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | Timezone of the contact preference | [optional] 
**availability** | [**ContactPreferenceAvailability**](ContactPreferenceAvailability.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.contact_preference import ContactPreference

# TODO update the JSON string below
json = "{}"
# create an instance of ContactPreference from a JSON string
contact_preference_instance = ContactPreference.from_json(json)
# print the JSON string representation of the object
print(ContactPreference.to_json())

# convert the object into a dict
contact_preference_dict = contact_preference_instance.to_dict()
# create an instance of ContactPreference from a dict
contact_preference_from_dict = ContactPreference.from_dict(contact_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


