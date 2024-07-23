# PortLoa

Port Loas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | uuid | [optional] 
**href** | **str** | Loa uri. | [optional] [readonly] 
**type** | [**PortLoaType**](PortLoaType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_loa import PortLoa

# TODO update the JSON string below
json = "{}"
# create an instance of PortLoa from a JSON string
port_loa_instance = PortLoa.from_json(json)
# print the JSON string representation of the object
print(PortLoa.to_json())

# convert the object into a dict
port_loa_dict = port_loa_instance.to_dict()
# create an instance of PortLoa from a dict
port_loa_form_dict = port_loa.from_dict(port_loa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


