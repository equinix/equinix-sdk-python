# Gateway

Gateway object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Gateways URI | [optional] [readonly] 
**type** | [**GatewayType**](GatewayType.md) |  | [optional] 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**name** | **str** | Customer-provided Gateway name | [optional] 
**description** | **str** | Customer-provided Gateway description | [optional] 
**state** | [**GatewayState**](GatewayState.md) |  | [optional] 
**bandwidth** | **int** | Gateway bandwidth in Mbps | [optional] 
**local_asn** | **int** | Gateway local Autonomous System Number | [optional] 
**router** | [**Router**](Router.md) |  | [optional] 
**ipv4** | [**GatewayIpv4**](GatewayIpv4.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.gateway import Gateway

# TODO update the JSON string below
json = "{}"
# create an instance of Gateway from a JSON string
gateway_instance = Gateway.from_json(json)
# print the JSON string representation of the object
print(Gateway.to_json())

# convert the object into a dict
gateway_dict = gateway_instance.to_dict()
# create an instance of Gateway from a dict
gateway_from_dict = Gateway.from_dict(gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


