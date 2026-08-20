# OperationalEventSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/subject&#x60; - Cloud Event subject description  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;IN&#x60; - in  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.operational_event_simple_expression import OperationalEventSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of OperationalEventSimpleExpression from a JSON string
operational_event_simple_expression_instance = OperationalEventSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(OperationalEventSimpleExpression.to_json())

# convert the object into a dict
operational_event_simple_expression_dict = operational_event_simple_expression_instance.to_dict()
# create an instance of OperationalEventSimpleExpression from a dict
operational_event_simple_expression_from_dict = OperationalEventSimpleExpression.from_dict(operational_event_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


