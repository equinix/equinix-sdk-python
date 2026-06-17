# IpBlockRegulations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressing_plans** | [**List[IpBlockAddressingPlan]**](IpBlockAddressingPlan.md) | List of addressing plans | 
**questions** | [**IpBlockRegulationsQuestions**](IpBlockRegulationsQuestions.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.ip_block_regulations import IpBlockRegulations

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockRegulations from a JSON string
ip_block_regulations_instance = IpBlockRegulations.from_json(json)
# print the JSON string representation of the object
print(IpBlockRegulations.to_json())

# convert the object into a dict
ip_block_regulations_dict = ip_block_regulations_instance.to_dict()
# create an instance of IpBlockRegulations from a dict
ip_block_regulations_from_dict = IpBlockRegulations.from_dict(ip_block_regulations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


