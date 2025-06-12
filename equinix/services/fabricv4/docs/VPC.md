# VPC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**VPCType**](VPCType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**state** | [**VPCState**](VPCState.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.vpc import VPC

# TODO update the JSON string below
json = "{}"
# create an instance of VPC from a JSON string
vpc_instance = VPC.from_json(json)
# print the JSON string representation of the object
print(VPC.to_json())

# convert the object into a dict
vpc_dict = vpc_instance.to_dict()
# create an instance of VPC from a dict
vpc_from_dict = VPC.from_dict(vpc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


