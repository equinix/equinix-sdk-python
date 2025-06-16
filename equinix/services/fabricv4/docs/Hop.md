# Hop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hop** | **int** |  | [optional] 
**probes** | [**List[HopProbes]**](HopProbes.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.hop import Hop

# TODO update the JSON string below
json = "{}"
# create an instance of Hop from a JSON string
hop_instance = Hop.from_json(json)
# print the JSON string representation of the object
print(Hop.to_json())

# convert the object into a dict
hop_dict = hop_instance.to_dict()
# create an instance of Hop from a dict
hop_from_dict = Hop.from_dict(hop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


