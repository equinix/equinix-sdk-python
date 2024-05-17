# Coordinates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**latitude** | **str** |  | [optional] 
**longitude** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.coordinates import Coordinates

# TODO update the JSON string below
json = "{}"
# create an instance of Coordinates from a JSON string
coordinates_instance = Coordinates.from_json(json)
# print the JSON string representation of the object
print(Coordinates.to_json())

# convert the object into a dict
coordinates_dict = coordinates_instance.to_dict()
# create an instance of Coordinates from a dict
coordinates_form_dict = coordinates.from_dict(coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


