# AppSubscriptionOrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[AppSubscriptionSimpleExpression]**](AppSubscriptionSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_or_filter import AppSubscriptionOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionOrFilter from a JSON string
app_subscription_or_filter_instance = AppSubscriptionOrFilter.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionOrFilter.to_json())

# convert the object into a dict
app_subscription_or_filter_dict = app_subscription_or_filter_instance.to_dict()
# create an instance of AppSubscriptionOrFilter from a dict
app_subscription_or_filter_from_dict = AppSubscriptionOrFilter.from_dict(app_subscription_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


