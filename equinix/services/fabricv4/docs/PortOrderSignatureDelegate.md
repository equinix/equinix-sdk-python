# PortOrderSignatureDelegate

delegate oder details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | name of delegate | [optional] 
**last_name** | **str** | last Name of delegate | [optional] 
**email** | **str** | email of delegate | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_order_signature_delegate import PortOrderSignatureDelegate

# TODO update the JSON string below
json = "{}"
# create an instance of PortOrderSignatureDelegate from a JSON string
port_order_signature_delegate_instance = PortOrderSignatureDelegate.from_json(json)
# print the JSON string representation of the object
print(PortOrderSignatureDelegate.to_json())

# convert the object into a dict
port_order_signature_delegate_dict = port_order_signature_delegate_instance.to_dict()
# create an instance of PortOrderSignatureDelegate from a dict
port_order_signature_delegate_from_dict = PortOrderSignatureDelegate.from_dict(port_order_signature_delegate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


