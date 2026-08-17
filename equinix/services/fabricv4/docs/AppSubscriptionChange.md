# AppSubscriptionChange

Current state of latest AppSubscription change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | [optional] 
**type** | [**AppSubscriptionChangeType**](AppSubscriptionChangeType.md) |  | 
**status** | [**PortChangeStatus**](PortChangeStatus.md) |  | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | [optional] 
**updated_date_time** | **datetime** | Set when change object is updated | 
**data** | [**List[AppSubscriptionChangeOperation]**](AppSubscriptionChangeOperation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_change import AppSubscriptionChange

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionChange from a JSON string
app_subscription_change_instance = AppSubscriptionChange.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionChange.to_json())

# convert the object into a dict
app_subscription_change_dict = app_subscription_change_instance.to_dict()
# create an instance of AppSubscriptionChange from a dict
app_subscription_change_from_dict = AppSubscriptionChange.from_dict(app_subscription_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


