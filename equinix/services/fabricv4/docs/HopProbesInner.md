# HopProbesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**asn** | **int** |  | [optional] 
**rtt** | **str** |  | [optional] 
**annotation** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.hop_probes_inner import HopProbesInner

# TODO update the JSON string below
json = "{}"
# create an instance of HopProbesInner from a JSON string
hop_probes_inner_instance = HopProbesInner.from_json(json)
# print the JSON string representation of the object
print(HopProbesInner.to_json())

# convert the object into a dict
hop_probes_inner_dict = hop_probes_inner_instance.to_dict()
# create an instance of HopProbesInner from a dict
hop_probes_inner_from_dict = HopProbesInner.from_dict(hop_probes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


