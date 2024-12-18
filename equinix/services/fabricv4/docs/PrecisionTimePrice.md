# PrecisionTimePrice

Precision Time Price

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | offering price currency | [optional] 
**charges** | [**List[PriceCharge]**](PriceCharge.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.precision_time_price import PrecisionTimePrice

# TODO update the JSON string below
json = "{}"
# create an instance of PrecisionTimePrice from a JSON string
precision_time_price_instance = PrecisionTimePrice.from_json(json)
# print the JSON string representation of the object
print(PrecisionTimePrice.to_json())

# convert the object into a dict
precision_time_price_dict = precision_time_price_instance.to_dict()
# create an instance of PrecisionTimePrice from a dict
precision_time_price_form_dict = precision_time_price.from_dict(precision_time_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


