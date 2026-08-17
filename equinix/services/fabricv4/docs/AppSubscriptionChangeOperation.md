# AppSubscriptionChangeOperation

App Subscription change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**PrecisionTimeChangeOperationOp**](PrecisionTimeChangeOperationOp.md) |  | 
**path** | **str** | path inside document leading to updated parameter | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_change_operation import AppSubscriptionChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionChangeOperation from a JSON string
app_subscription_change_operation_instance = AppSubscriptionChangeOperation.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionChangeOperation.to_json())

# convert the object into a dict
app_subscription_change_operation_dict = app_subscription_change_operation_instance.to_dict()
# create an instance of AppSubscriptionChangeOperation from a dict
app_subscription_change_operation_from_dict = AppSubscriptionChangeOperation.from_dict(app_subscription_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


