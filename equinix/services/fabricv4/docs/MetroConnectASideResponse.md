# MetroConnectASideResponse

Metro Connection ASide configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_panel** | [**MetroConnectPatchPanel**](MetroConnectPatchPanel.md) |  | [optional] 
**port** | [**MetroConnectPort**](MetroConnectPort.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metro_connect_a_side_response import MetroConnectASideResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MetroConnectASideResponse from a JSON string
metro_connect_a_side_response_instance = MetroConnectASideResponse.from_json(json)
# print the JSON string representation of the object
print(MetroConnectASideResponse.to_json())

# convert the object into a dict
metro_connect_a_side_response_dict = metro_connect_a_side_response_instance.to_dict()
# create an instance of MetroConnectASideResponse from a dict
metro_connect_a_side_response_from_dict = MetroConnectASideResponse.from_dict(metro_connect_a_side_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


