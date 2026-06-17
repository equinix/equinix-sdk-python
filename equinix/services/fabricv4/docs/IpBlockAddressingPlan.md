# IpBlockAddressingPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | **str** | purpose | 
**size** | **int** | size | 

## Example

```python
from equinix.services.fabricv4.models.ip_block_addressing_plan import IpBlockAddressingPlan

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockAddressingPlan from a JSON string
ip_block_addressing_plan_instance = IpBlockAddressingPlan.from_json(json)
# print the JSON string representation of the object
print(IpBlockAddressingPlan.to_json())

# convert the object into a dict
ip_block_addressing_plan_dict = ip_block_addressing_plan_instance.to_dict()
# create an instance of IpBlockAddressingPlan from a dict
ip_block_addressing_plan_from_dict = IpBlockAddressingPlan.from_dict(ip_block_addressing_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


