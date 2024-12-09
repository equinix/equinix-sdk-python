# TimeServicePriceConnectionAccessPoint

Time Service Price Connection Access Point configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**PriceLocation**](PriceLocation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.time_service_price_connection_access_point import TimeServicePriceConnectionAccessPoint

# TODO update the JSON string below
json = "{}"
# create an instance of TimeServicePriceConnectionAccessPoint from a JSON string
time_service_price_connection_access_point_instance = TimeServicePriceConnectionAccessPoint.from_json(json)
# print the JSON string representation of the object
print(TimeServicePriceConnectionAccessPoint.to_json())

# convert the object into a dict
time_service_price_connection_access_point_dict = time_service_price_connection_access_point_instance.to_dict()
# create an instance of TimeServicePriceConnectionAccessPoint from a dict
time_service_price_connection_access_point_form_dict = time_service_price_connection_access_point.from_dict(time_service_price_connection_access_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


