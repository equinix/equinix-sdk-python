# SubInterface

Sub Interface information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of subinterafce of a port | [optional] 
**unit** | **int** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.sub_interface import SubInterface

# TODO update the JSON string below
json = "{}"
# create an instance of SubInterface from a JSON string
sub_interface_instance = SubInterface.from_json(json)
# print the JSON string representation of the object
print(SubInterface.to_json())

# convert the object into a dict
sub_interface_dict = sub_interface_instance.to_dict()
# create an instance of SubInterface from a dict
sub_interface_form_dict = sub_interface.from_dict(sub_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


