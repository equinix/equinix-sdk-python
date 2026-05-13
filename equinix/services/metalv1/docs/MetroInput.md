# MetroInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**metro** | [**MetroInputMetro**](MetroInputMetro.md) |  | 

## Example

```python
from equinix.services.metalv1.models.metro_input import MetroInput

# TODO update the JSON string below
json = "{}"
# create an instance of MetroInput from a JSON string
metro_input_instance = MetroInput.from_json(json)
# print the JSON string representation of the object
print(MetroInput.to_json())

# convert the object into a dict
metro_input_dict = metro_input_instance.to_dict()
# create an instance of MetroInput from a dict
metro_input_from_dict = MetroInput.from_dict(metro_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


