# CloudEventSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/subject&#x60; - Cloud Event subject description  * &#x60;/type&#x60; - Cloud Event type  * &#x60;/time&#x60; - Time of Cloud Events  * &#x60;/equinixproject&#x60; - Equinix Project of Cloud Events  * &#x60;/equinixorganization&#x60; - Equinix Organization of Cloud Events  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;&gt;&#x60; - greater than  * &#x60;&gt;&#x3D;&#x60; - greater than or equal to  * &#x60;&lt;&#x60; - less than  * &#x60;&lt;&#x3D;&#x60; - less than or equal to  * &#x60;BETWEEN&#x60; - between  * &#x60;IN&#x60; - in  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_event_simple_expression import CloudEventSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of CloudEventSimpleExpression from a JSON string
cloud_event_simple_expression_instance = CloudEventSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(CloudEventSimpleExpression.to_json())

# convert the object into a dict
cloud_event_simple_expression_dict = cloud_event_simple_expression_instance.to_dict()
# create an instance of CloudEventSimpleExpression from a dict
cloud_event_simple_expression_from_dict = CloudEventSimpleExpression.from_dict(cloud_event_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


