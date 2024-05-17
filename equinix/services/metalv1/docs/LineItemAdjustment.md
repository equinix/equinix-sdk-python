# LineItemAdjustment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.line_item_adjustment import LineItemAdjustment

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemAdjustment from a JSON string
line_item_adjustment_instance = LineItemAdjustment.from_json(json)
# print the JSON string representation of the object
print(LineItemAdjustment.to_json())

# convert the object into a dict
line_item_adjustment_dict = line_item_adjustment_instance.to_dict()
# create an instance of LineItemAdjustment from a dict
line_item_adjustment_form_dict = line_item_adjustment.from_dict(line_item_adjustment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


