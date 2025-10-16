# MetricSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/subject&#x60; - Metric subject description (required and limited to 1 value)  * &#x60;/name&#x60; - Metric names (required)  * &#x60;/dataPoints/endDateTime&#x60; - Time of Metrics  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;&gt;&#x60; - greater than  * &#x60;&gt;&#x3D;&#x60; - greater than or equal to  * &#x60;&lt;&#x60; - less than  * &#x60;&lt;&#x3D;&#x60; - less than or equal to  * &#x60;BETWEEN&#x60; - between  * &#x60;IN&#x60; - in  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metric_simple_expression import MetricSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of MetricSimpleExpression from a JSON string
metric_simple_expression_instance = MetricSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(MetricSimpleExpression.to_json())

# convert the object into a dict
metric_simple_expression_dict = metric_simple_expression_instance.to_dict()
# create an instance of MetricSimpleExpression from a dict
metric_simple_expression_from_dict = MetricSimpleExpression.from_dict(metric_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


