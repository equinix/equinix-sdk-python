# Ipv4

EPT service network information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | Primary Timing Server IP Address | 
**secondary** | **str** | Secondary Timing Server IP Address | 
**network_mask** | **str** | Network Mask | 
**default_gateway** | **str** | Gateway Interface IP address | [optional] 

## Example

```python
from equinix.services.fabricv4.models.ipv4 import Ipv4

# TODO update the JSON string below
json = "{}"
# create an instance of Ipv4 from a JSON string
ipv4_instance = Ipv4.from_json(json)
# print the JSON string representation of the object
print(Ipv4.to_json())

# convert the object into a dict
ipv4_dict = ipv4_instance.to_dict()
# create an instance of Ipv4 from a dict
ipv4_from_dict = Ipv4.from_dict(ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


