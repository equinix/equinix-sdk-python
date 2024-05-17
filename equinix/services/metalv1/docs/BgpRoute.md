# BgpRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exact** | **bool** |  | [optional] 
**href** | **str** |  | [optional] 
**route** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.bgp_route import BgpRoute

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRoute from a JSON string
bgp_route_instance = BgpRoute.from_json(json)
# print the JSON string representation of the object
print(BgpRoute.to_json())

# convert the object into a dict
bgp_route_dict = bgp_route_instance.to_dict()
# create an instance of BgpRoute from a dict
bgp_route_form_dict = bgp_route.from_dict(bgp_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


