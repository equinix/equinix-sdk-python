# GlobalBgpRangeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_bgp_ranges** | [**List[GlobalBgpRange]**](GlobalBgpRange.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.global_bgp_range_list import GlobalBgpRangeList

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalBgpRangeList from a JSON string
global_bgp_range_list_instance = GlobalBgpRangeList.from_json(json)
# print the JSON string representation of the object
print(GlobalBgpRangeList.to_json())

# convert the object into a dict
global_bgp_range_list_dict = global_bgp_range_list_instance.to_dict()
# create an instance of GlobalBgpRangeList from a dict
global_bgp_range_list_form_dict = global_bgp_range_list.from_dict(global_bgp_range_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


