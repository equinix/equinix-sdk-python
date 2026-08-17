# AppSubscriptionFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AppSubscriptionFilter]**](AppSubscriptionFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_filters import AppSubscriptionFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionFilters from a JSON string
app_subscription_filters_instance = AppSubscriptionFilters.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionFilters.to_json())

# convert the object into a dict
app_subscription_filters_dict = app_subscription_filters_instance.to_dict()
# create an instance of AppSubscriptionFilters from a dict
app_subscription_filters_from_dict = AppSubscriptionFilters.from_dict(app_subscription_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


