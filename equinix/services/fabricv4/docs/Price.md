# Price


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | An absolute URL that returns specified pricing data | [optional] 
**type** | [**ProductType**](ProductType.md) |  | [optional] 
**code** | **str** | Equinix-assigned product code | [optional] 
**name** | **str** | Full product name | [optional] 
**description** | **str** | Product description | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**charges** | [**List[PriceCharge]**](PriceCharge.md) |  | [optional] 
**currency** | **str** | Product offering price currency | [optional] 
**term_length** | [**PriceTermLength**](PriceTermLength.md) |  | [optional] 
**catgory** | [**PriceCategory**](PriceCategory.md) |  | [optional] 
**connection** | [**VirtualConnectionPrice**](VirtualConnectionPrice.md) |  | [optional] 
**ip_block** | [**IpBlockPrice**](IpBlockPrice.md) |  | [optional] 
**router** | [**FabricCloudRouterPrice**](FabricCloudRouterPrice.md) |  | [optional] 
**port** | [**VirtualPortPrice**](VirtualPortPrice.md) |  | [optional] 
**time_service** | [**TimeServicePrice**](TimeServicePrice.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.price import Price

# TODO update the JSON string below
json = "{}"
# create an instance of Price from a JSON string
price_instance = Price.from_json(json)
# print the JSON string representation of the object
print(Price.to_json())

# convert the object into a dict
price_dict = price_instance.to_dict()
# create an instance of Price from a dict
price_form_dict = price.from_dict(price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


