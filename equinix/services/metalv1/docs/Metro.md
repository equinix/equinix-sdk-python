# Metro


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.metro import Metro

# TODO update the JSON string below
json = "{}"
# create an instance of Metro from a JSON string
metro_instance = Metro.from_json(json)
# print the JSON string representation of the object
print(Metro.to_json())

# convert the object into a dict
metro_dict = metro_instance.to_dict()
# create an instance of Metro from a dict
metro_form_dict = metro.from_dict(metro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


