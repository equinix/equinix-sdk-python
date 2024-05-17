# Error

Error responses are included with 4xx and 5xx HTTP responses from the API service. Either \"error\" or \"errors\" will be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | A description of the error that caused the request to fail. | [optional] 
**errors** | **List[str]** | A list of errors that contributed to the request failing. | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_form_dict = error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


