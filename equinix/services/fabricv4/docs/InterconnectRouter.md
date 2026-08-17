# InterconnectRouter

Router associated with the interconnect <font color=\"red\"> <sup color='red'>Beta</sup></font>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Router URI | [optional] 
**type** | [**InterconnectRouterType**](InterconnectRouterType.md) |  | [optional] 
**uuid** | **str** | Router identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.interconnect_router import InterconnectRouter

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectRouter from a JSON string
interconnect_router_instance = InterconnectRouter.from_json(json)
# print the JSON string representation of the object
print(InterconnectRouter.to_json())

# convert the object into a dict
interconnect_router_dict = interconnect_router_instance.to_dict()
# create an instance of InterconnectRouter from a dict
interconnect_router_from_dict = InterconnectRouter.from_dict(interconnect_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


