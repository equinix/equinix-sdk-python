# Component


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | **str** | File checksum | [optional] [readonly] 
**component** | **str** | Component type | [optional] [readonly] 
**created_at** | **datetime** | Datetime when the block was created. | [optional] [readonly] 
**filename** | **str** | name of the file | [optional] [readonly] 
**href** | **str** |  | [optional] 
**model** | **List[str]** | List of models where this component version can be applied | [optional] [readonly] 
**repository_url** | **str** | Location of the file in the repository | [optional] [readonly] 
**updated_at** | **datetime** | Datetime when the block was updated. | [optional] [readonly] 
**upstream_url** | **str** | Location of the file | [optional] [readonly] 
**uuid** | **str** | Component UUID | [optional] [readonly] 
**vendor** | **str** | Component vendor | [optional] [readonly] 
**version** | **str** | Version of the component | [optional] [readonly] 

## Example

```python
from equinix_metal.models.component import Component

# TODO update the JSON string below
json = "{}"
# create an instance of Component from a JSON string
component_instance = Component.from_json(json)
# print the JSON string representation of the object
print(Component.to_json())

# convert the object into a dict
component_dict = component_instance.to_dict()
# create an instance of Component from a dict
component_form_dict = component.from_dict(component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


