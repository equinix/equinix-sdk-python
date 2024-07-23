# Md5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**Md5Type**](Md5Type.md) |  | [optional] 
**id** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.md5 import Md5

# TODO update the JSON string below
json = "{}"
# create an instance of Md5 from a JSON string
md5_instance = Md5.from_json(json)
# print the JSON string representation of the object
print(Md5.to_json())

# convert the object into a dict
md5_dict = md5_instance.to_dict()
# create an instance of Md5 from a dict
md5_form_dict = md5.from_dict(md5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


