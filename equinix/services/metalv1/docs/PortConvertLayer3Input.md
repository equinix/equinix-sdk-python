# PortConvertLayer3Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**request_ips** | [**List[PortConvertLayer3InputRequestIpsInner]**](PortConvertLayer3InputRequestIpsInner.md) |  | [optional] 

## Example

```python
from equinix_metal.models.port_convert_layer3_input import PortConvertLayer3Input

# TODO update the JSON string below
json = "{}"
# create an instance of PortConvertLayer3Input from a JSON string
port_convert_layer3_input_instance = PortConvertLayer3Input.from_json(json)
# print the JSON string representation of the object
print(PortConvertLayer3Input.to_json())

# convert the object into a dict
port_convert_layer3_input_dict = port_convert_layer3_input_instance.to_dict()
# create an instance of PortConvertLayer3Input from a dict
port_convert_layer3_input_form_dict = port_convert_layer3_input.from_dict(port_convert_layer3_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


