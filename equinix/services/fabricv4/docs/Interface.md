# Interface

Interface Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Interface URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned Interface identifier | [optional] 
**id** | **int** | Interface id | [optional] 
**type** | [**InterfaceType**](InterfaceType.md) |  | [optional] 
**project_id** | **str** | Interface Project ID | [optional] 

## Example

```python
from equinix.services.fabricv4.models.interface import Interface

# TODO update the JSON string below
json = "{}"
# create an instance of Interface from a JSON string
interface_instance = Interface.from_json(json)
# print the JSON string representation of the object
print(Interface.to_json())

# convert the object into a dict
interface_dict = interface_instance.to_dict()
# create an instance of Interface from a dict
interface_form_dict = interface.from_dict(interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


