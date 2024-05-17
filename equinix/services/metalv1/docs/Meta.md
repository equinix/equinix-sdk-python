# Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**first** | [**Href**](Href.md) |  | [optional] 
**href** | **str** |  | [optional] 
**last** | [**Href**](Href.md) |  | [optional] 
**last_page** | **int** |  | [optional] 
**next** | [**Href**](Href.md) |  | [optional] 
**previous** | [**Href**](Href.md) |  | [optional] 
**var_self** | [**Href**](Href.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from equinix_metal.models.meta import Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Meta from a JSON string
meta_instance = Meta.from_json(json)
# print the JSON string representation of the object
print(Meta.to_json())

# convert the object into a dict
meta_dict = meta_instance.to_dict()
# create an instance of Meta from a dict
meta_form_dict = meta.from_dict(meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


