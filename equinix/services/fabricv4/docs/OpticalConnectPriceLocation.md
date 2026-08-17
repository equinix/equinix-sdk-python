# OpticalConnectPriceLocation

Optical Connect Location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ibx_code** | **str** | IBX identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_price_location import OpticalConnectPriceLocation

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectPriceLocation from a JSON string
optical_connect_price_location_instance = OpticalConnectPriceLocation.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectPriceLocation.to_json())

# convert the object into a dict
optical_connect_price_location_dict = optical_connect_price_location_instance.to_dict()
# create an instance of OpticalConnectPriceLocation from a dict
optical_connect_price_location_from_dict = OpticalConnectPriceLocation.from_dict(optical_connect_price_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


