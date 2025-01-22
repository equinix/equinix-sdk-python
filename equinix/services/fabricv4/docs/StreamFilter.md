# StreamFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/subject&#x60; - subject  * &#x60;/type&#x60; - type  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;in&#x60; - in  * &#x60;LIKE&#x60; - case-sensitive like  * &#x60;ILIKE&#x60; - case-insensitive like  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_or** | [**List[StreamFilterSimpleExpression]**](StreamFilterSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_filter import StreamFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StreamFilter from a JSON string
stream_filter_instance = StreamFilter.from_json(json)
# print the JSON string representation of the object
print(StreamFilter.to_json())

# convert the object into a dict
stream_filter_dict = stream_filter_instance.to_dict()
# create an instance of StreamFilter from a dict
stream_filter_from_dict = StreamFilter.from_dict(stream_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


