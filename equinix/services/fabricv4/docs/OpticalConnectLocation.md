# OpticalConnectLocation

Destination location for BMMR and REMOTE connections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ibx_code** | **str** | Equinix IBX data centre code. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_location import OpticalConnectLocation

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectLocation from a JSON string
optical_connect_location_instance = OpticalConnectLocation.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectLocation.to_json())

# convert the object into a dict
optical_connect_location_dict = optical_connect_location_instance.to_dict()
# create an instance of OpticalConnectLocation from a dict
optical_connect_location_from_dict = OpticalConnectLocation.from_dict(optical_connect_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


