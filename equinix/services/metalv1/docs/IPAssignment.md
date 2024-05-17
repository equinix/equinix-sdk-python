# IPAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**address_family** | **int** |  | [optional] 
**assigned_to** | [**Href**](Href.md) |  | 
**cidr** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**gateway** | **str** |  | [optional] 
**global_ip** | **bool** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**manageable** | **bool** |  | [optional] 
**management** | **bool** |  | [optional] 
**metro** | [**IPAssignmentMetro**](IPAssignmentMetro.md) |  | [optional] 
**netmask** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**next_hop** | **str** | Only set when this is a Metal Gateway Elastic IP Assignment.  The IP address within the Metal Gateway to which requests to the Elastic IP are forwarded.  | [optional] 
**parent_block** | [**ParentBlock**](ParentBlock.md) |  | [optional] 
**public** | **bool** |  | [optional] 
**state** | **str** | Only set when this is a Metal Gateway Elastic IP Assignment.  Describes the current configuration state of this IP on the network.  | [optional] 

## Example

```python
from equinix_metal.models.ip_assignment import IPAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of IPAssignment from a JSON string
ip_assignment_instance = IPAssignment.from_json(json)
# print the JSON string representation of the object
print(IPAssignment.to_json())

# convert the object into a dict
ip_assignment_dict = ip_assignment_instance.to_dict()
# create an instance of IPAssignment from a dict
ip_assignment_form_dict = ip_assignment.from_dict(ip_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


