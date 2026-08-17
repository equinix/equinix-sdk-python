# RouteCollector

Route Collector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | Route Collector ASN | [optional] 
**ip_v4** | **str** | Route Collector ipV4 address | [optional] 
**ip_v6** | **str** | Route Collector ipV6 address | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_collector import RouteCollector

# TODO update the JSON string below
json = "{}"
# create an instance of RouteCollector from a JSON string
route_collector_instance = RouteCollector.from_json(json)
# print the JSON string representation of the object
print(RouteCollector.to_json())

# convert the object into a dict
route_collector_dict = route_collector_instance.to_dict()
# create an instance of RouteCollector from a dict
route_collector_from_dict = RouteCollector.from_dict(route_collector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


