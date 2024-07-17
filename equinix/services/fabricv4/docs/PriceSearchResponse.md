# PriceSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Price]**](Price.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.price_search_response import PriceSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PriceSearchResponse from a JSON string
price_search_response_instance = PriceSearchResponse.from_json(json)
# print the JSON string representation of the object
print(PriceSearchResponse.to_json())

# convert the object into a dict
price_search_response_dict = price_search_response_instance.to_dict()
# create an instance of PriceSearchResponse from a dict
price_search_response_form_dict = price_search_response.from_dict(price_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


