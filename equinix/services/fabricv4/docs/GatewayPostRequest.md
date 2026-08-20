# GatewayPostRequest

Create Gateway

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GatewayType**](GatewayType.md) |  | 
**name** | **str** | Customer-provided Gateway name | 
**description** | **str** | Customer-provided Gateway description | [optional] 
**bandwidth** | **int** | Gateway bandwidth in Mbps | 
**local_asn** | **int** | Gateway local Autonomous System Number | 
**router** | [**Router**](Router.md) |  | 
**ha_enabled** | **bool** | High availability enabled | [optional] [default to False]
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | 
**project** | [**Project**](Project.md) |  | 
**order** | [**Order**](Order.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.gateway_post_request import GatewayPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayPostRequest from a JSON string
gateway_post_request_instance = GatewayPostRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayPostRequest.to_json())

# convert the object into a dict
gateway_post_request_dict = gateway_post_request_instance.to_dict()
# create an instance of GatewayPostRequest from a dict
gateway_post_request_from_dict = GatewayPostRequest.from_dict(gateway_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


