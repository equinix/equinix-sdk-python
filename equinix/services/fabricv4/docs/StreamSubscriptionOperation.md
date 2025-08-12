# StreamSubscriptionOperation

Stream subscription operational information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events_delivered_count** | **int** | count of delivered events | [optional] 
**metrics_delivered_count** | **int** | count of delivered metrics | [optional] 
**alerts_delivered_count** | **int** | count of delivered alerts | [optional] 
**last_successful_delivery_date_time** | **datetime** | last successful date time of delivered event, metric, or alert | [optional] 
**suspended_date_time** | **datetime** | suspended date time of stream subscription delivery for event, metric, or alert | [optional] 
**errors** | [**List[StreamSubscriptionOperationErrors]**](StreamSubscriptionOperationErrors.md) | List of error information for stream subscription delivery | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_operation import StreamSubscriptionOperation

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionOperation from a JSON string
stream_subscription_operation_instance = StreamSubscriptionOperation.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionOperation.to_json())

# convert the object into a dict
stream_subscription_operation_dict = stream_subscription_operation_instance.to_dict()
# create an instance of StreamSubscriptionOperation from a dict
stream_subscription_operation_from_dict = StreamSubscriptionOperation.from_dict(stream_subscription_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


