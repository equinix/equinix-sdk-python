# SimplifiedLocationWithoutIBX


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metro_href** | **str** | The Canonical URL at which the resource resides. | [optional] 
**region** | **str** |  | [optional] 
**metro_name** | **str** |  | [optional] 
**metro_code** | **str** |  | 

## Example

```python
from equinix.services.fabricv4.models.simplified_location_without_ibx import SimplifiedLocationWithoutIBX

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedLocationWithoutIBX from a JSON string
simplified_location_without_ibx_instance = SimplifiedLocationWithoutIBX.from_json(json)
# print the JSON string representation of the object
print(SimplifiedLocationWithoutIBX.to_json())

# convert the object into a dict
simplified_location_without_ibx_dict = simplified_location_without_ibx_instance.to_dict()
# create an instance of SimplifiedLocationWithoutIBX from a dict
simplified_location_without_ibx_from_dict = SimplifiedLocationWithoutIBX.from_dict(simplified_location_without_ibx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


