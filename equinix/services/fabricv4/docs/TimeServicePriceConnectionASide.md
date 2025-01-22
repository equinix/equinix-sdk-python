# TimeServicePriceConnectionASide

Time Service Price Connection ASide configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_point** | [**TimeServicePriceConnectionAccessPoint**](TimeServicePriceConnectionAccessPoint.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.time_service_price_connection_a_side import TimeServicePriceConnectionASide

# TODO update the JSON string below
json = "{}"
# create an instance of TimeServicePriceConnectionASide from a JSON string
time_service_price_connection_a_side_instance = TimeServicePriceConnectionASide.from_json(json)
# print the JSON string representation of the object
print(TimeServicePriceConnectionASide.to_json())

# convert the object into a dict
time_service_price_connection_a_side_dict = time_service_price_connection_a_side_instance.to_dict()
# create an instance of TimeServicePriceConnectionASide from a dict
time_service_price_connection_a_side_from_dict = TimeServicePriceConnectionASide.from_dict(time_service_price_connection_a_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


