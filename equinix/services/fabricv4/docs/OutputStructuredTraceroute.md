# OutputStructuredTraceroute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_ip** | **str** |  | [optional] 
**destination_name** | **str** |  | [optional] 
**packet_bytes** | **int** |  | [optional] 
**hops_max** | **int** |  | [optional] 
**hops** | [**List[Hop]**](Hop.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.output_structured_traceroute import OutputStructuredTraceroute

# TODO update the JSON string below
json = "{}"
# create an instance of OutputStructuredTraceroute from a JSON string
output_structured_traceroute_instance = OutputStructuredTraceroute.from_json(json)
# print the JSON string representation of the object
print(OutputStructuredTraceroute.to_json())

# convert the object into a dict
output_structured_traceroute_dict = output_structured_traceroute_instance.to_dict()
# create an instance of OutputStructuredTraceroute from a dict
output_structured_traceroute_from_dict = OutputStructuredTraceroute.from_dict(output_structured_traceroute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


