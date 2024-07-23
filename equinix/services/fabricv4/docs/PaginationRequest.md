# PaginationRequest

Pagination request information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Index of the first element. | [optional] [default to 0]
**limit** | **int** | Number of elements to be requested per page. Number must be between 1 and 100, and the default is 20. | [optional] [default to 20]

## Example

```python
from equinix.services.fabricv4.models.pagination_request import PaginationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequest from a JSON string
pagination_request_instance = PaginationRequest.from_json(json)
# print the JSON string representation of the object
print(PaginationRequest.to_json())

# convert the object into a dict
pagination_request_dict = pagination_request_instance.to_dict()
# create an instance of PaginationRequest from a dict
pagination_request_form_dict = pagination_request.from_dict(pagination_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


