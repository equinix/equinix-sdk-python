# StreamFilterOrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[StreamFilterSimpleExpression]**](StreamFilterSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_filter_or_filter import StreamFilterOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StreamFilterOrFilter from a JSON string
stream_filter_or_filter_instance = StreamFilterOrFilter.from_json(json)
# print the JSON string representation of the object
print(StreamFilterOrFilter.to_json())

# convert the object into a dict
stream_filter_or_filter_dict = stream_filter_or_filter_instance.to_dict()
# create an instance of StreamFilterOrFilter from a dict
stream_filter_or_filter_from_dict = StreamFilterOrFilter.from_dict(stream_filter_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


