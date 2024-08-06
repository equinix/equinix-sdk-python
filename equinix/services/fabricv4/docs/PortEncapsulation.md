# PortEncapsulation

Port encapsulation configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PortEncapsulationType**](PortEncapsulationType.md) |  | [optional] 
**tag_protocol_id** | **str** | Port encapsulation tag protocol identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_encapsulation import PortEncapsulation

# TODO update the JSON string below
json = "{}"
# create an instance of PortEncapsulation from a JSON string
port_encapsulation_instance = PortEncapsulation.from_json(json)
# print the JSON string representation of the object
print(PortEncapsulation.to_json())

# convert the object into a dict
port_encapsulation_dict = port_encapsulation_instance.to_dict()
# create an instance of PortEncapsulation from a dict
port_encapsulation_from_dict = PortEncapsulation.from_dict(port_encapsulation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


