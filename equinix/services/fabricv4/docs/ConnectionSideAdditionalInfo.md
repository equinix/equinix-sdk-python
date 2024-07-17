# ConnectionSideAdditionalInfo

Additional information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key | [optional] 
**value** | **str** | Value | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_side_additional_info import ConnectionSideAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionSideAdditionalInfo from a JSON string
connection_side_additional_info_instance = ConnectionSideAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(ConnectionSideAdditionalInfo.to_json())

# convert the object into a dict
connection_side_additional_info_dict = connection_side_additional_info_instance.to_dict()
# create an instance of ConnectionSideAdditionalInfo from a dict
connection_side_additional_info_form_dict = connection_side_additional_info.from_dict(connection_side_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


