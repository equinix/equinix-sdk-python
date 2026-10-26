# ServiceProfileLastMileContactInfoItem

Last-mile provider contact information item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ServiceProfileLastMileContactInfoItemType**](ServiceProfileLastMileContactInfoItemType.md) |  | [optional] 
**url** | **str** | Contact URL. | [optional] 
**emails** | **List[str]** | List of contact emails. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_last_mile_contact_info_item import ServiceProfileLastMileContactInfoItem

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileLastMileContactInfoItem from a JSON string
service_profile_last_mile_contact_info_item_instance = ServiceProfileLastMileContactInfoItem.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileLastMileContactInfoItem.to_json())

# convert the object into a dict
service_profile_last_mile_contact_info_item_dict = service_profile_last_mile_contact_info_item_instance.to_dict()
# create an instance of ServiceProfileLastMileContactInfoItem from a dict
service_profile_last_mile_contact_info_item_from_dict = ServiceProfileLastMileContactInfoItem.from_dict(service_profile_last_mile_contact_info_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


