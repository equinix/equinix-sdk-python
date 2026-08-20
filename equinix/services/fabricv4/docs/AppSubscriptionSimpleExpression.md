# AppSubscriptionSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:   * &#x60;/project/projectId&#x60; - project id   * &#x60;/uuid&#x60; - App Subscription uuid   * &#x60;/state&#x60; - App Subscription status   * &#x60;/source/appLink/uuid&#x60; - Source App Link uuid   * &#x60;/source/ipSubnets&#x60; - Source App Link ip subnets   * &#x60;/target/appService/uuid&#x60; - Target App Service uuid   * &#x60;/target/geoScope&#x60; - Target App Service geo scope   * &#x60;/target/prioritization&#x60; - Target App Service prioritization   * &#x60;/changeLog/createdDateTime&#x60; - App Subscription creation timestamp   * &#x60;/changeLog/updatedDateTime&#x60; - App Subscription last updated timestamp   * &#x60;/changeLog/deletedDateTime&#x60; - App Subscription deletion timestamp  | [optional] 
**operator** | **str** | Possible operators to use on filters:   * &#x60;&#x3D;&#x60; - equal   * &#x60;!&#x3D;&#x60; - not equal   * &#x60;&gt;&#x60; - greater than   * &#x60;&lt;&#x60; - less than   * &#x60;IN&#x60; - in   * &#x60;NOT IN&#x60; - not in   * &#x60;LIKE&#x60; - like   * &#x60;ILIKE&#x60; - case-insensitive like   * &#x60;BETWEEN&#x60; - between   * &#x60;NOT BETWEEN&#x60; - not between  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_simple_expression import AppSubscriptionSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionSimpleExpression from a JSON string
app_subscription_simple_expression_instance = AppSubscriptionSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionSimpleExpression.to_json())

# convert the object into a dict
app_subscription_simple_expression_dict = app_subscription_simple_expression_instance.to_dict()
# create an instance of AppSubscriptionSimpleExpression from a dict
app_subscription_simple_expression_from_dict = AppSubscriptionSimpleExpression.from_dict(app_subscription_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


