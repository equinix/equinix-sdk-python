# OpticalConnectLOA

Letter of Authorization granting the right to terminate at the Z-side location. <br> Required for BMMR and REMOTE. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Identifier of the Letter of Authorization | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_loa import OpticalConnectLOA

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectLOA from a JSON string
optical_connect_loa_instance = OpticalConnectLOA.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectLOA.to_json())

# convert the object into a dict
optical_connect_loa_dict = optical_connect_loa_instance.to_dict()
# create an instance of OpticalConnectLOA from a dict
optical_connect_loa_from_dict = OpticalConnectLOA.from_dict(optical_connect_loa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


