# DeviceCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_thumb_url** | **str** | Avatar thumbnail URL of the User | [optional] 
**created_at** | **datetime** | When the user was created | [optional] 
**email** | **str** | Primary email address of the User | [optional] 
**first_name** | **str** | First name of the User | [optional] 
**full_name** | **str** | Full name of the User | [optional] 
**href** | **str** | API URL uniquely representing the User | [optional] 
**id** | **str** | ID of the User | 
**last_name** | **str** | Last name of the User | [optional] 
**short_id** | **str** | Short ID of the User | 
**updated_at** | **datetime** | When the user details were last updated | [optional] 

## Example

```python
from equinix_metal.models.device_created_by import DeviceCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceCreatedBy from a JSON string
device_created_by_instance = DeviceCreatedBy.from_json(json)
# print the JSON string representation of the object
print(DeviceCreatedBy.to_json())

# convert the object into a dict
device_created_by_dict = device_created_by_instance.to_dict()
# create an instance of DeviceCreatedBy from a dict
device_created_by_form_dict = device_created_by.from_dict(device_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


