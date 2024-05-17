# MetroList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**metros** | [**List[Metro]**](Metro.md) |  | [optional] 

## Example

```python
from equinix_metal.models.metro_list import MetroList

# TODO update the JSON string below
json = "{}"
# create an instance of MetroList from a JSON string
metro_list_instance = MetroList.from_json(json)
# print the JSON string representation of the object
print(MetroList.to_json())

# convert the object into a dict
metro_list_dict = metro_list_instance.to_dict()
# create an instance of MetroList from a dict
metro_list_form_dict = metro_list.from_dict(metro_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


