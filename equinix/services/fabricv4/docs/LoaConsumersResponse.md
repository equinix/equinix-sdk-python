# LoaConsumersResponse

List of Consumers associated with a LOA

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[LoaConsumer]**](LoaConsumer.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_consumers_response import LoaConsumersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoaConsumersResponse from a JSON string
loa_consumers_response_instance = LoaConsumersResponse.from_json(json)
# print the JSON string representation of the object
print(LoaConsumersResponse.to_json())

# convert the object into a dict
loa_consumers_response_dict = loa_consumers_response_instance.to_dict()
# create an instance of LoaConsumersResponse from a dict
loa_consumers_response_from_dict = LoaConsumersResponse.from_dict(loa_consumers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


