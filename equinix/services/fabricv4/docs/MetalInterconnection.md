# MetalInterconnection

Metal Interconnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Equinix Metal Interconnection | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metal_interconnection import MetalInterconnection

# TODO update the JSON string below
json = "{}"
# create an instance of MetalInterconnection from a JSON string
metal_interconnection_instance = MetalInterconnection.from_json(json)
# print the JSON string representation of the object
print(MetalInterconnection.to_json())

# convert the object into a dict
metal_interconnection_dict = metal_interconnection_instance.to_dict()
# create an instance of MetalInterconnection from a dict
metal_interconnection_from_dict = MetalInterconnection.from_dict(metal_interconnection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


