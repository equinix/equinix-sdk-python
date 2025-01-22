# Pagination

Pagination response information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Index of the first item returned in the response. The default is 0. | [optional] [default to 0]
**limit** | **int** | Maximum number of search results returned per page. Number must be between 1 and 100, and the default is 20. | [default to 20]
**total** | **int** | Total number of elements returned. | 
**next** | **str** | URL relative to the next item in the response. | [optional] 
**previous** | **str** | URL relative to the previous item in the response. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print(Pagination.to_json())

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_from_dict = Pagination.from_dict(pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


