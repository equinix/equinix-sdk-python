# PriceCharge

Price  Charge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PriceChargeType**](PriceChargeType.md) |  | [optional] 
**price** | **float** | Offering price | [optional] 

## Example

```python
from equinix.services.fabricv4.models.price_charge import PriceCharge

# TODO update the JSON string below
json = "{}"
# create an instance of PriceCharge from a JSON string
price_charge_instance = PriceCharge.from_json(json)
# print the JSON string representation of the object
print(PriceCharge.to_json())

# convert the object into a dict
price_charge_dict = price_charge_instance.to_dict()
# create an instance of PriceCharge from a dict
price_charge_from_dict = PriceCharge.from_dict(price_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


