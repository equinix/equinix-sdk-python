# Userdata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**userdata** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.userdata import Userdata

# TODO update the JSON string below
json = "{}"
# create an instance of Userdata from a JSON string
userdata_instance = Userdata.from_json(json)
# print the JSON string representation of the object
print(Userdata.to_json())

# convert the object into a dict
userdata_dict = userdata_instance.to_dict()
# create an instance of Userdata from a dict
userdata_form_dict = userdata.from_dict(userdata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


