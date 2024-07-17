# PortAdditionalInfo

Additional information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key | [optional] 
**value** | **str** | Value | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_additional_info import PortAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PortAdditionalInfo from a JSON string
port_additional_info_instance = PortAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(PortAdditionalInfo.to_json())

# convert the object into a dict
port_additional_info_dict = port_additional_info_instance.to_dict()
# create an instance of PortAdditionalInfo from a dict
port_additional_info_form_dict = port_additional_info.from_dict(port_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


