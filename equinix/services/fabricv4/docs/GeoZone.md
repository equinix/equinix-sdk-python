# GeoZone

Geographic zone of a Fabric Metro

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code assigned to a geographic zone. | [optional] 
**name** | **str** | Name of a geographic zone. | [optional] 
**description** | **str** | Description of a geographic zone. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.geo_zone import GeoZone

# TODO update the JSON string below
json = "{}"
# create an instance of GeoZone from a JSON string
geo_zone_instance = GeoZone.from_json(json)
# print the JSON string representation of the object
print(GeoZone.to_json())

# convert the object into a dict
geo_zone_dict = geo_zone_instance.to_dict()
# create an instance of GeoZone from a dict
geo_zone_from_dict = GeoZone.from_dict(geo_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


