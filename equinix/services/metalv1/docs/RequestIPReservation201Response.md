# RequestIPReservation201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | **int** |  | [optional] 
**cidr** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | [**Href**](Href.md) |  | [optional] 
**details** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metal_gateway** | [**MetalGatewayLite**](MetalGatewayLite.md) |  | [optional] 
**netmask** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**state** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**vrf** | [**Vrf**](Vrf.md) |  | 
**public** | **bool** |  | [optional] 
**management** | **bool** |  | [optional] 
**manageable** | **bool** |  | [optional] 
**customdata** | **object** |  | [optional] 
**bill** | **bool** |  | [optional] 
**project_lite** | [**Project**](Project.md) |  | [optional] 
**address** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 
**metro** | [**Metro**](Metro.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.request_ip_reservation201_response import RequestIPReservation201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RequestIPReservation201Response from a JSON string
request_ip_reservation201_response_instance = RequestIPReservation201Response.from_json(json)
# print the JSON string representation of the object
print(RequestIPReservation201Response.to_json())

# convert the object into a dict
request_ip_reservation201_response_dict = request_ip_reservation201_response_instance.to_dict()
# create an instance of RequestIPReservation201Response from a dict
request_ip_reservation201_response_form_dict = request_ip_reservation201_response.from_dict(request_ip_reservation201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


