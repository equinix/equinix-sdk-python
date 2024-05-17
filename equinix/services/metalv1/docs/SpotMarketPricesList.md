# SpotMarketPricesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**spot_market_prices** | [**SpotPricesReport**](SpotPricesReport.md) |  | [optional] 

## Example

```python
from equinix_metal.models.spot_market_prices_list import SpotMarketPricesList

# TODO update the JSON string below
json = "{}"
# create an instance of SpotMarketPricesList from a JSON string
spot_market_prices_list_instance = SpotMarketPricesList.from_json(json)
# print the JSON string representation of the object
print(SpotMarketPricesList.to_json())

# convert the object into a dict
spot_market_prices_list_dict = spot_market_prices_list_instance.to_dict()
# create an instance of SpotMarketPricesList from a dict
spot_market_prices_list_form_dict = spot_market_prices_list.from_dict(spot_market_prices_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


