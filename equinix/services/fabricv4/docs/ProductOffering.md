# ProductOffering

Product offering for connection. Applicable to zSide only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product offering identifier | [optional] 
**name** | **str** | Product offering name | [optional] 

## Example

```python
from equinix.services.fabricv4.models.product_offering import ProductOffering

# TODO update the JSON string below
json = "{}"
# create an instance of ProductOffering from a JSON string
product_offering_instance = ProductOffering.from_json(json)
# print the JSON string representation of the object
print(ProductOffering.to_json())

# convert the object into a dict
product_offering_dict = product_offering_instance.to_dict()
# create an instance of ProductOffering from a dict
product_offering_from_dict = ProductOffering.from_dict(product_offering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


