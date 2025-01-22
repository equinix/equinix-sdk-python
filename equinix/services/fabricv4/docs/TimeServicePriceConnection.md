# TimeServicePriceConnection

Time Service Price Connection configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_side** | [**TimeServicePriceConnectionASide**](TimeServicePriceConnectionASide.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.time_service_price_connection import TimeServicePriceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of TimeServicePriceConnection from a JSON string
time_service_price_connection_instance = TimeServicePriceConnection.from_json(json)
# print the JSON string representation of the object
print(TimeServicePriceConnection.to_json())

# convert the object into a dict
time_service_price_connection_dict = time_service_price_connection_instance.to_dict()
# create an instance of TimeServicePriceConnection from a dict
time_service_price_connection_from_dict = TimeServicePriceConnection.from_dict(time_service_price_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


