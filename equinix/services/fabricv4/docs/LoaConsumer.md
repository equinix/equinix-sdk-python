# LoaConsumer

Associated consumer response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Consumer URI | [optional] 
**uuid** | **str** | Consumer Identifier | [optional] 
**type** | [**LoaProductType**](LoaProductType.md) |  | [optional] 
**change_log** | [**LoaChangelog**](LoaChangelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_consumer import LoaConsumer

# TODO update the JSON string below
json = "{}"
# create an instance of LoaConsumer from a JSON string
loa_consumer_instance = LoaConsumer.from_json(json)
# print the JSON string representation of the object
print(LoaConsumer.to_json())

# convert the object into a dict
loa_consumer_dict = loa_consumer_instance.to_dict()
# create an instance of LoaConsumer from a dict
loa_consumer_from_dict = LoaConsumer.from_dict(loa_consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


