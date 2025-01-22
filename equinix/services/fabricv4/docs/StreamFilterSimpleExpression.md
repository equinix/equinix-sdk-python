# StreamFilterSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/subject&#x60; - subject  * &#x60;/type&#x60; - type  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;in&#x60; - in  * &#x60;LIKE&#x60; - case-sensitive like  * &#x60;ILIKE&#x60; - case-insensitive like  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_filter_simple_expression import StreamFilterSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of StreamFilterSimpleExpression from a JSON string
stream_filter_simple_expression_instance = StreamFilterSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(StreamFilterSimpleExpression.to_json())

# convert the object into a dict
stream_filter_simple_expression_dict = stream_filter_simple_expression_instance.to_dict()
# create an instance of StreamFilterSimpleExpression from a dict
stream_filter_simple_expression_from_dict = StreamFilterSimpleExpression.from_dict(stream_filter_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


