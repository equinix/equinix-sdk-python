# CrossConnectLink

Link to a Cross Connect sub-resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Sub-resource URI. | [optional] [readonly] 
**rel** | **str** | Operation identifier of the linked sub-resource. | [optional] [readonly] 
**method** | **str** | HTTP method to use on the sub-resource. | [optional] [readonly] 
**content_type** | **str** | Content type returned by the sub-resource. | [optional] [readonly] 
**authenticate** | **bool** | Whether authentication is required. | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_link import CrossConnectLink

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectLink from a JSON string
cross_connect_link_instance = CrossConnectLink.from_json(json)
# print the JSON string representation of the object
print(CrossConnectLink.to_json())

# convert the object into a dict
cross_connect_link_dict = cross_connect_link_instance.to_dict()
# create an instance of CrossConnectLink from a dict
cross_connect_link_from_dict = CrossConnectLink.from_dict(cross_connect_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


