# SpotMarketPricesPerMetroList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**spot_market_prices** | [**SpotMarketPricesPerMetroReport**](SpotMarketPricesPerMetroReport.md) |  | [optional] 

## Example

```python
from equinix_metal.models.spot_market_prices_per_metro_list import SpotMarketPricesPerMetroList

# TODO update the JSON string below
json = "{}"
# create an instance of SpotMarketPricesPerMetroList from a JSON string
spot_market_prices_per_metro_list_instance = SpotMarketPricesPerMetroList.from_json(json)
# print the JSON string representation of the object
print(SpotMarketPricesPerMetroList.to_json())

# convert the object into a dict
spot_market_prices_per_metro_list_dict = spot_market_prices_per_metro_list_instance.to_dict()
# create an instance of SpotMarketPricesPerMetroList from a dict
spot_market_prices_per_metro_list_form_dict = spot_market_prices_per_metro_list.from_dict(spot_market_prices_per_metro_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


