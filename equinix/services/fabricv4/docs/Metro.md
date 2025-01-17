# Metro

GET Metros retrieves all Equinix? Fabric? metros, as well as latency data for each location.This performance data helps network planning engineers and administrators make strategic decisions about port locations and traffic routes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The Canonical URL at which the resource resides. | [optional] 
**type** | **str** | Indicator of a Fabric Metro | [optional] 
**code** | **str** | Code Assigned to an Equinix IBX data center in a specified metropolitan area. | [optional] 
**region** | **str** | Board geographic area in which the data center is located | [optional] 
**name** | **str** | Name of the region in which the data center is located. | [optional] 
**equinix_asn** | **int** | Autonomous system number (ASN) for a specified Fabric metro. The ASN is a unique identifier that carries the network routing protocol and exchanges that data with other internal systems via border gateway protocol. | [optional] 
**local_vc_bandwidth_max** | **int** | This field holds Max Connection speed with in the metro | [optional] 
**geo_coordinates** | [**GeoCoordinates**](GeoCoordinates.md) |  | [optional] 
**connected_metros** | [**List[ConnectedMetro]**](ConnectedMetro.md) |  | [optional] 
**geo_scopes** | [**List[GeoScopeType]**](GeoScopeType.md) | List of supported geographic boundaries of a Fabric Metro. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metro import Metro

# TODO update the JSON string below
json = "{}"
# create an instance of Metro from a JSON string
metro_instance = Metro.from_json(json)
# print the JSON string representation of the object
print(Metro.to_json())

# convert the object into a dict
metro_dict = metro_instance.to_dict()
# create an instance of Metro from a dict
metro_from_dict = Metro.from_dict(metro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


