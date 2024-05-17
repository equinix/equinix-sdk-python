# BondPortData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**id** | **str** | ID of the bonding port | [optional] 
**name** | **str** | Name of the port interface for the bond (\&quot;bond0\&quot;) | [optional] 

## Example

```python
from equinix_metal.models.bond_port_data import BondPortData

# TODO update the JSON string below
json = "{}"
# create an instance of BondPortData from a JSON string
bond_port_data_instance = BondPortData.from_json(json)
# print the JSON string representation of the object
print(BondPortData.to_json())

# convert the object into a dict
bond_port_data_dict = bond_port_data_instance.to_dict()
# create an instance of BondPortData from a dict
bond_port_data_form_dict = bond_port_data.from_dict(bond_port_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


