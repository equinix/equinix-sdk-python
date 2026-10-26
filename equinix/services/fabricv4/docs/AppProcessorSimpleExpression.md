# AppProcessorSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:   * &#x60;/project/projectId&#x60; - project id   * &#x60;/uuid&#x60; - App Processor uuid   * &#x60;/name&#x60; - App Processor name   * &#x60;/description&#x60; - App Processor description   * &#x60;/state&#x60; - App Processor status   * &#x60;/ipv4Subnet&#x60; - App Processor ipv4 subnet   * &#x60;/bandwidth&#x60; - App Processor bandwidth   * &#x60;/changeLog/createdDateTime&#x60; - App Processor creation timestamp   * &#x60;/changeLog/updatedDateTime&#x60; - App Processor last updated timestamp   * &#x60;/changeLog/deletedDateTime&#x60; - App Processor deletion timestamp  | [optional] 
**operator** | **str** | Possible operators to use on filters:   * &#x60;&#x3D;&#x60; - equal   * &#x60;!&#x3D;&#x60; - not equal   * &#x60;&gt;&#x60; - greater than   * &#x60;&lt;&#x60; - less than   * &#x60;IN&#x60; - in   * &#x60;NOT IN&#x60; - not in   * &#x60;LIKE&#x60; - like   * &#x60;ILIKE&#x60; - case-insensitive like   * &#x60;BETWEEN&#x60; - between   * &#x60;NOT BETWEEN&#x60; - not between  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_processor_simple_expression import AppProcessorSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of AppProcessorSimpleExpression from a JSON string
app_processor_simple_expression_instance = AppProcessorSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(AppProcessorSimpleExpression.to_json())

# convert the object into a dict
app_processor_simple_expression_dict = app_processor_simple_expression_instance.to_dict()
# create an instance of AppProcessorSimpleExpression from a dict
app_processor_simple_expression_from_dict = AppProcessorSimpleExpression.from_dict(app_processor_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


