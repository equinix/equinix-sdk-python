# AttributeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**latest** | **bool** | Boolean flag to know if the firmware set is the latest for the model and vendor | [optional] [readonly] 
**model** | **str** | Model on which this firmware set can be applied | [optional] [readonly] 
**plan** | **str** | Plan where the firmware set can be applied | [optional] [readonly] 
**vendor** | **str** | Vendor on which this firmware set can be applied | [optional] [readonly] 

## Example

```python
from equinix_metal.models.attribute_data import AttributeData

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeData from a JSON string
attribute_data_instance = AttributeData.from_json(json)
# print the JSON string representation of the object
print(AttributeData.to_json())

# convert the object into a dict
attribute_data_dict = attribute_data_instance.to_dict()
# create an instance of AttributeData from a dict
attribute_data_form_dict = attribute_data.from_dict(attribute_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


