# RequestLoa

Request Loa

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LoaType**](LoaType.md) |  | 
**name** | **str** | A short, descriptive name for this LOA. | 
**description** | **str** | Additional context about this LOA. | [optional] 
**authorized_product_type** | [**LoaProductType**](LoaProductType.md) |  | 
**issuer** | [**LoaIssuer**](LoaIssuer.md) |  | [optional] 
**location** | [**LoaLocation**](LoaLocation.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.request_loa import RequestLoa

# TODO update the JSON string below
json = "{}"
# create an instance of RequestLoa from a JSON string
request_loa_instance = RequestLoa.from_json(json)
# print the JSON string representation of the object
print(RequestLoa.to_json())

# convert the object into a dict
request_loa_dict = request_loa_instance.to_dict()
# create an instance of RequestLoa from a dict
request_loa_from_dict = RequestLoa.from_dict(request_loa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


