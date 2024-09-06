# FilterBody

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**SearchExpression**](SearchExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.filter_body import FilterBody

# TODO update the JSON string below
json = "{}"
# create an instance of FilterBody from a JSON string
filter_body_instance = FilterBody.from_json(json)
# print the JSON string representation of the object
print(FilterBody.to_json())

# convert the object into a dict
filter_body_dict = filter_body_instance.to_dict()
# create an instance of FilterBody from a dict
filter_body_from_dict = FilterBody.from_dict(filter_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


