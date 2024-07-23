# PortRedundancy

Port redundancy configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Access point redundancy | [optional] 
**group** | **str** | Port UUID of respective primary port | [optional] 
**priority** | [**PortPriority**](PortPriority.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_redundancy import PortRedundancy

# TODO update the JSON string below
json = "{}"
# create an instance of PortRedundancy from a JSON string
port_redundancy_instance = PortRedundancy.from_json(json)
# print the JSON string representation of the object
print(PortRedundancy.to_json())

# convert the object into a dict
port_redundancy_dict = port_redundancy_instance.to_dict()
# create an instance of PortRedundancy from a dict
port_redundancy_form_dict = port_redundancy.from_dict(port_redundancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


