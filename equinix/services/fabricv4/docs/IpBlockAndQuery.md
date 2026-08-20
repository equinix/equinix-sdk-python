# IpBlockAndQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | 
**operator** | [**ExchangeServicePropertyExpressionOperator**](ExchangeServicePropertyExpressionOperator.md) |  | 
**values** | **List[str]** |  | 

## Example

```python
from equinix.services.fabricv4.models.ip_block_and_query import IpBlockAndQuery

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockAndQuery from a JSON string
ip_block_and_query_instance = IpBlockAndQuery.from_json(json)
# print the JSON string representation of the object
print(IpBlockAndQuery.to_json())

# convert the object into a dict
ip_block_and_query_dict = ip_block_and_query_instance.to_dict()
# create an instance of IpBlockAndQuery from a dict
ip_block_and_query_from_dict = IpBlockAndQuery.from_dict(ip_block_and_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


