# OutputStructuredPingResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | **int** |  | [optional] 
**ip** | **str** |  | [optional] 
**icmp_seq** | **int** |  | [optional] 
**ttl** | **int** |  | [optional] 
**time** | **float** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.output_structured_ping_response_item import OutputStructuredPingResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of OutputStructuredPingResponseItem from a JSON string
output_structured_ping_response_item_instance = OutputStructuredPingResponseItem.from_json(json)
# print the JSON string representation of the object
print(OutputStructuredPingResponseItem.to_json())

# convert the object into a dict
output_structured_ping_response_item_dict = output_structured_ping_response_item_instance.to_dict()
# create an instance of OutputStructuredPingResponseItem from a dict
output_structured_ping_response_item_from_dict = OutputStructuredPingResponseItem.from_dict(output_structured_ping_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


