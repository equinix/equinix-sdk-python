# StreamSubscriptionOperationErrors

Error information for stream subscription delivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | Equinix Observability error code | [optional] 
**error_message** | **str** | Equinix Observability error message | [optional] 
**date_time** | **datetime** | Equinix Observability error date time | [optional] 
**additional_info** | [**StreamSubscriptionOperationAdditionalInfo**](StreamSubscriptionOperationAdditionalInfo.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_operation_errors import StreamSubscriptionOperationErrors

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionOperationErrors from a JSON string
stream_subscription_operation_errors_instance = StreamSubscriptionOperationErrors.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionOperationErrors.to_json())

# convert the object into a dict
stream_subscription_operation_errors_dict = stream_subscription_operation_errors_instance.to_dict()
# create an instance of StreamSubscriptionOperationErrors from a dict
stream_subscription_operation_errors_from_dict = StreamSubscriptionOperationErrors.from_dict(stream_subscription_operation_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


