# AppServiceAttachedAppSubscriptionFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:   * &#x60;/uuid&#x60; - App Subscription UUID   * &#x60;/state&#x60; - App Subscription lifecycle state  | [optional] 
**operator** | **str** | Possible operators to use on filters:   * &#x60;&#x3D;&#x60; - equal   * &#x60;!&#x3D;&#x60; - not equal   * &#x60;IN&#x60; - in   * &#x60;NOT IN&#x60; - not in  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_or** | [**List[AppServiceAttachedAppSubscriptionSimpleExpression]**](AppServiceAttachedAppSubscriptionSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_attached_app_subscription_filter import AppServiceAttachedAppSubscriptionFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAttachedAppSubscriptionFilter from a JSON string
app_service_attached_app_subscription_filter_instance = AppServiceAttachedAppSubscriptionFilter.from_json(json)
# print the JSON string representation of the object
print(AppServiceAttachedAppSubscriptionFilter.to_json())

# convert the object into a dict
app_service_attached_app_subscription_filter_dict = app_service_attached_app_subscription_filter_instance.to_dict()
# create an instance of AppServiceAttachedAppSubscriptionFilter from a dict
app_service_attached_app_subscription_filter_from_dict = AppServiceAttachedAppSubscriptionFilter.from_dict(app_service_attached_app_subscription_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


