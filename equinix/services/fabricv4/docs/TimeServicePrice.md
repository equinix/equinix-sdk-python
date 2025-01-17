# TimeServicePrice

Time Service Product configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PrecisionTimeServiceRequestType**](PrecisionTimeServiceRequestType.md) |  | [optional] 
**package** | [**PrecisionTimePackageRequest**](PrecisionTimePackageRequest.md) |  | [optional] 
**connection** | [**TimeServicePriceConnection**](TimeServicePriceConnection.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.time_service_price import TimeServicePrice

# TODO update the JSON string below
json = "{}"
# create an instance of TimeServicePrice from a JSON string
time_service_price_instance = TimeServicePrice.from_json(json)
# print the JSON string representation of the object
print(TimeServicePrice.to_json())

# convert the object into a dict
time_service_price_dict = time_service_price_instance.to_dict()
# create an instance of TimeServicePrice from a dict
time_service_price_from_dict = TimeServicePrice.from_dict(time_service_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


