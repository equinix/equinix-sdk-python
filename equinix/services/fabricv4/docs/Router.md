# Router


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Fabric Cloud Router URI | [optional] [readonly] 
**uuid** | **str** | Cloud Router UUID | [optional] 
**type** | [**CloudRouterPostRequestBaseType**](CloudRouterPostRequestBaseType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.router import Router

# TODO update the JSON string below
json = "{}"
# create an instance of Router from a JSON string
router_instance = Router.from_json(json)
# print the JSON string representation of the object
print(Router.to_json())

# convert the object into a dict
router_dict = router_instance.to_dict()
# create an instance of Router from a dict
router_from_dict = Router.from_dict(router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


