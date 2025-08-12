# MetroConnectASide

Metro Connection ASide configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_panel** | [**MetroConnectPatchPanel**](MetroConnectPatchPanel.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metro_connect_a_side import MetroConnectASide

# TODO update the JSON string below
json = "{}"
# create an instance of MetroConnectASide from a JSON string
metro_connect_a_side_instance = MetroConnectASide.from_json(json)
# print the JSON string representation of the object
print(MetroConnectASide.to_json())

# convert the object into a dict
metro_connect_a_side_dict = metro_connect_a_side_instance.to_dict()
# create an instance of MetroConnectASide from a dict
metro_connect_a_side_from_dict = MetroConnectASide.from_dict(metro_connect_a_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


