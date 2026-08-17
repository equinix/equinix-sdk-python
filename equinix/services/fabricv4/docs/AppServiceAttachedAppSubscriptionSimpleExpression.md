# AppServiceAttachedAppSubscriptionSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:   * &#x60;/uuid&#x60; - App Subscription UUID   * &#x60;/state&#x60; - App Subscription lifecycle state  | [optional] 
**operator** | **str** | Possible operators to use on filters:   * &#x60;&#x3D;&#x60; - equal   * &#x60;!&#x3D;&#x60; - not equal   * &#x60;IN&#x60; - in   * &#x60;NOT IN&#x60; - not in  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_attached_app_subscription_simple_expression import AppServiceAttachedAppSubscriptionSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAttachedAppSubscriptionSimpleExpression from a JSON string
app_service_attached_app_subscription_simple_expression_instance = AppServiceAttachedAppSubscriptionSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(AppServiceAttachedAppSubscriptionSimpleExpression.to_json())

# convert the object into a dict
app_service_attached_app_subscription_simple_expression_dict = app_service_attached_app_subscription_simple_expression_instance.to_dict()
# create an instance of AppServiceAttachedAppSubscriptionSimpleExpression from a dict
app_service_attached_app_subscription_simple_expression_from_dict = AppServiceAttachedAppSubscriptionSimpleExpression.from_dict(app_service_attached_app_subscription_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


