# LoaRequest

Create Loa

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LoaType**](LoaType.md) |  | 
**name** | **str** | A short, descriptive name for this LOA. | 
**description** | **str** | Additional context about this LOA. | [optional] 
**authorized_product_type** | [**LoaProductType**](LoaProductType.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.loa_request import LoaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoaRequest from a JSON string
loa_request_instance = LoaRequest.from_json(json)
# print the JSON string representation of the object
print(LoaRequest.to_json())

# convert the object into a dict
loa_request_dict = loa_request_instance.to_dict()
# create an instance of LoaRequest from a dict
loa_request_from_dict = LoaRequest.from_dict(loa_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


