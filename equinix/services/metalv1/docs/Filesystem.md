# Filesystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**mount** | [**Mount**](Mount.md) |  | [optional] 

## Example

```python
from equinix_metal.models.filesystem import Filesystem

# TODO update the JSON string below
json = "{}"
# create an instance of Filesystem from a JSON string
filesystem_instance = Filesystem.from_json(json)
# print the JSON string representation of the object
print(Filesystem.to_json())

# convert the object into a dict
filesystem_dict = filesystem_instance.to_dict()
# create an instance of Filesystem from a dict
filesystem_form_dict = filesystem.from_dict(filesystem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


