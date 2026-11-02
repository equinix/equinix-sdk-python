# AsnSearchRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**filter** | [**SearchExpression**](SearchExpression.md) |  | [optional] 
**sort** | [**List[AsnSearchSortCriteria]**](AsnSearchSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.asn_search_request_body import AsnSearchRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AsnSearchRequestBody from a JSON string
asn_search_request_body_instance = AsnSearchRequestBody.from_json(json)
# print the JSON string representation of the object
print(AsnSearchRequestBody.to_json())

# convert the object into a dict
asn_search_request_body_dict = asn_search_request_body_instance.to_dict()
# create an instance of AsnSearchRequestBody from a dict
asn_search_request_body_from_dict = AsnSearchRequestBody.from_dict(asn_search_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


