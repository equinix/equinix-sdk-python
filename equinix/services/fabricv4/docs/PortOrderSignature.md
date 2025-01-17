# PortOrderSignature

Port signature Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signatory** | [**PortOrderSignatureSignatory**](PortOrderSignatureSignatory.md) |  | [optional] 
**delegate** | [**PortOrderSignatureDelegate**](PortOrderSignatureDelegate.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_order_signature import PortOrderSignature

# TODO update the JSON string below
json = "{}"
# create an instance of PortOrderSignature from a JSON string
port_order_signature_instance = PortOrderSignature.from_json(json)
# print the JSON string representation of the object
print(PortOrderSignature.to_json())

# convert the object into a dict
port_order_signature_dict = port_order_signature_instance.to_dict()
# create an instance of PortOrderSignature from a dict
port_order_signature_from_dict = PortOrderSignature.from_dict(port_order_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


