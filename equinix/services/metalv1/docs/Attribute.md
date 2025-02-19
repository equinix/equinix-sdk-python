# Attribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Datetime when the block was created. | [optional] [readonly] 
**data** | [**AttributeData**](AttributeData.md) |  | [optional] 
**href** | **str** |  | [optional] 
**namespace** | **str** | Attribute namespace | [optional] [readonly] 
**updated_at** | **datetime** | Datetime when the block was updated. | [optional] [readonly] 

## Example

```python
from equinix.services.metalv1.models.attribute import Attribute

# TODO update the JSON string below
json = "{}"
# create an instance of Attribute from a JSON string
attribute_instance = Attribute.from_json(json)
# print the JSON string representation of the object
print(Attribute.to_json())

# convert the object into a dict
attribute_dict = attribute_instance.to_dict()
# create an instance of Attribute from a dict
attribute_from_dict = Attribute.from_dict(attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


