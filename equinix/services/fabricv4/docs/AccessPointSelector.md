# AccessPointSelector

List of criteria for selecting network access points with optimal efficiency, security, compatibility, and availability.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AccessPointSelectorType**](AccessPointSelectorType.md) |  | [optional] 
**port** | [**SimplifiedMetadataEntity**](SimplifiedMetadataEntity.md) |  | [optional] 
**link_protocol** | [**LinkProtocol**](LinkProtocol.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.access_point_selector import AccessPointSelector

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPointSelector from a JSON string
access_point_selector_instance = AccessPointSelector.from_json(json)
# print the JSON string representation of the object
print(AccessPointSelector.to_json())

# convert the object into a dict
access_point_selector_dict = access_point_selector_instance.to_dict()
# create an instance of AccessPointSelector from a dict
access_point_selector_from_dict = AccessPointSelector.from_dict(access_point_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


