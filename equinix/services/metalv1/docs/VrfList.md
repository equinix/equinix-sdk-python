# VrfList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**vrfs** | [**List[Vrf]**](Vrf.md) |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_list import VrfList

# TODO update the JSON string below
json = "{}"
# create an instance of VrfList from a JSON string
vrf_list_instance = VrfList.from_json(json)
# print the JSON string representation of the object
print(VrfList.to_json())

# convert the object into a dict
vrf_list_dict = vrf_list_instance.to_dict()
# create an instance of VrfList from a dict
vrf_list_form_dict = vrf_list.from_dict(vrf_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


