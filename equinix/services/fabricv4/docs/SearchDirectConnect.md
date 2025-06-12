# SearchDirectConnect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SearchDirectConnectType**](SearchDirectConnectType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**state** | [**SearchDirectConnectState**](SearchDirectConnectState.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.search_direct_connect import SearchDirectConnect

# TODO update the JSON string below
json = "{}"
# create an instance of SearchDirectConnect from a JSON string
search_direct_connect_instance = SearchDirectConnect.from_json(json)
# print the JSON string representation of the object
print(SearchDirectConnect.to_json())

# convert the object into a dict
search_direct_connect_dict = search_direct_connect_instance.to_dict()
# create an instance of SearchDirectConnect from a dict
search_direct_connect_from_dict = SearchDirectConnect.from_dict(search_direct_connect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


