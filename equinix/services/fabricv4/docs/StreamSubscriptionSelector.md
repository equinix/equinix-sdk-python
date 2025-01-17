# StreamSubscriptionSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**var_except** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_selector import StreamSubscriptionSelector

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionSelector from a JSON string
stream_subscription_selector_instance = StreamSubscriptionSelector.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionSelector.to_json())

# convert the object into a dict
stream_subscription_selector_dict = stream_subscription_selector_instance.to_dict()
# create an instance of StreamSubscriptionSelector from a dict
stream_subscription_selector_from_dict = StreamSubscriptionSelector.from_dict(stream_subscription_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


