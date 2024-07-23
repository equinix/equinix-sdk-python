# GeoCoordinates

Geographic location data of Fabric Metro

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude of a Fabric Metro | [optional] 
**longitude** | **float** | Longitude of a Fabric Metro | [optional] 

## Example

```python
from equinix.services.fabricv4.models.geo_coordinates import GeoCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of GeoCoordinates from a JSON string
geo_coordinates_instance = GeoCoordinates.from_json(json)
# print the JSON string representation of the object
print(GeoCoordinates.to_json())

# convert the object into a dict
geo_coordinates_dict = geo_coordinates_instance.to_dict()
# create an instance of GeoCoordinates from a dict
geo_coordinates_form_dict = geo_coordinates.from_dict(geo_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


