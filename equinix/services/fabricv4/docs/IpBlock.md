# IpBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the IP Block | 
**href** | **str** | Resource URL path for the IP Block | 
**type** | [**TypeOfIpBlockProduct**](TypeOfIpBlockProduct.md) |  | 
**state** | [**IpBlockState**](IpBlockState.md) |  | 
**ownership** | [**IpBlockOwnership**](IpBlockOwnership.md) |  | 
**location** | [**IpBlockLocation**](IpBlockLocation.md) |  | [optional] 
**prefix_length** | **int** | IpBlockPrefix length | 
**prefix** | **str** | CIDR prefix | [optional] 
**order** | [**IpBlockOrderResponse**](IpBlockOrderResponse.md) |  | [optional] 
**account** | [**IpBlockAccount**](IpBlockAccount.md) |  | [optional] 
**project** | [**IpBlockProject**](IpBlockProject.md) |  | 
**regulations** | [**IpBlockRegulations**](IpBlockRegulations.md) |  | [optional] 
**assets** | [**List[IpBlockAsset]**](IpBlockAsset.md) | Products using this IP Block | [optional] 
**change** | [**IpBlockChange**](IpBlockChange.md) |  | [optional] 
**change_log** | [**IpBlockChangeLog**](IpBlockChangeLog.md) |  | 
**error** | [**Error**](Error.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.ip_block import IpBlock

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlock from a JSON string
ip_block_instance = IpBlock.from_json(json)
# print the JSON string representation of the object
print(IpBlock.to_json())

# convert the object into a dict
ip_block_dict = ip_block_instance.to_dict()
# create an instance of IpBlock from a dict
ip_block_from_dict = IpBlock.from_dict(ip_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


