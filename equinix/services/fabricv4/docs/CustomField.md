# CustomField

Define Custom Attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**description** | **str** |  | 
**required** | **bool** |  | [optional] 
**data_type** | [**CustomFieldDataType**](CustomFieldDataType.md) |  | 
**options** | **List[str]** |  | [optional] 
**capture_in_email** | **bool** | capture this field as a part of email notification | [optional] 

## Example

```python
from equinix.services.fabricv4.models.custom_field import CustomField

# TODO update the JSON string below
json = "{}"
# create an instance of CustomField from a JSON string
custom_field_instance = CustomField.from_json(json)
# print the JSON string representation of the object
print(CustomField.to_json())

# convert the object into a dict
custom_field_dict = custom_field_instance.to_dict()
# create an instance of CustomField from a dict
custom_field_from_dict = CustomField.from_dict(custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


