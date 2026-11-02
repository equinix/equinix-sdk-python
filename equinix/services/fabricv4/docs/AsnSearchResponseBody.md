# AsnSearchResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**sort** | [**List[AsnSearchSortCriteria]**](AsnSearchSortCriteria.md) |  | [optional] 
**data** | [**List[Asn]**](Asn.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.asn_search_response_body import AsnSearchResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of AsnSearchResponseBody from a JSON string
asn_search_response_body_instance = AsnSearchResponseBody.from_json(json)
# print the JSON string representation of the object
print(AsnSearchResponseBody.to_json())

# convert the object into a dict
asn_search_response_body_dict = asn_search_response_body_instance.to_dict()
# create an instance of AsnSearchResponseBody from a dict
asn_search_response_body_from_dict = AsnSearchResponseBody.from_dict(asn_search_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


