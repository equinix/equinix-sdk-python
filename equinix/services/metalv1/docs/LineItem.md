# LineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**plan** | [**Plan**](Plan.md) |  | [optional] 
**unit** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**hostname** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**item_type** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**project_id** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**project** | [**ProjectIdName**](ProjectIdName.md) |  | [optional] 
**adjustments** | [**List[LineItemAdjustment]**](LineItemAdjustment.md) | Adjustments for the line item | [optional] 

## Example

```python
from equinix.services.metalv1.models.line_item import LineItem

# TODO update the JSON string below
json = "{}"
# create an instance of LineItem from a JSON string
line_item_instance = LineItem.from_json(json)
# print the JSON string representation of the object
print(LineItem.to_json())

# convert the object into a dict
line_item_dict = line_item_instance.to_dict()
# create an instance of LineItem from a dict
line_item_form_dict = line_item.from_dict(line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


