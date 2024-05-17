# PortData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonded** | **bool** | Bonded is true for NetworkPort ports in a bond and NetworkBondPort ports that are active | [optional] 
**href** | **str** |  | [optional] 
**mac** | **str** | MAC address is set for NetworkPort ports | [optional] 

## Example

```python
from equinix_metal.models.port_data import PortData

# TODO update the JSON string below
json = "{}"
# create an instance of PortData from a JSON string
port_data_instance = PortData.from_json(json)
# print the JSON string representation of the object
print(PortData.to_json())

# convert the object into a dict
port_data_dict = port_data_instance.to_dict()
# create an instance of PortData from a dict
port_data_form_dict = port_data.from_dict(port_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


