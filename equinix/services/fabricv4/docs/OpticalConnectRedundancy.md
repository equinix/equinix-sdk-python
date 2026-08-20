# OpticalConnectRedundancy

Optical Connect redundancy configuration. <br> Required only for DUAL_DIVERSE connection. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | [**OpticalConnectRedundancyPriority**](OpticalConnectRedundancyPriority.md) |  | [optional] 
**group** | **str** | Redundancy group identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_redundancy import OpticalConnectRedundancy

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectRedundancy from a JSON string
optical_connect_redundancy_instance = OpticalConnectRedundancy.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectRedundancy.to_json())

# convert the object into a dict
optical_connect_redundancy_dict = optical_connect_redundancy_instance.to_dict()
# create an instance of OpticalConnectRedundancy from a dict
optical_connect_redundancy_from_dict = OpticalConnectRedundancy.from_dict(optical_connect_redundancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


