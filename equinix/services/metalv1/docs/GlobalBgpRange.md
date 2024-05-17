# GlobalBgpRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**project** | [**Href**](Href.md) |  | [optional] 
**range** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.global_bgp_range import GlobalBgpRange

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalBgpRange from a JSON string
global_bgp_range_instance = GlobalBgpRange.from_json(json)
# print the JSON string representation of the object
print(GlobalBgpRange.to_json())

# convert the object into a dict
global_bgp_range_dict = global_bgp_range_instance.to_dict()
# create an instance of GlobalBgpRange from a dict
global_bgp_range_form_dict = global_bgp_range.from_dict(global_bgp_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


