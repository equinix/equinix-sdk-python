# SpotMarketPricesPerMetroReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**am** | [**SpotPricesPerFacility**](SpotPricesPerFacility.md) |  | [optional] 
**ch** | [**SpotPricesPerFacility**](SpotPricesPerFacility.md) |  | [optional] 
**da** | [**SpotPricesPerFacility**](SpotPricesPerFacility.md) |  | [optional] 
**href** | **str** |  | [optional] 
**la** | [**SpotPricesPerFacility**](SpotPricesPerFacility.md) |  | [optional] 
**ny** | [**SpotPricesPerFacility**](SpotPricesPerFacility.md) |  | [optional] 
**sg** | [**SpotPricesPerFacility**](SpotPricesPerFacility.md) |  | [optional] 
**sv** | [**SpotPricesPerFacility**](SpotPricesPerFacility.md) |  | [optional] 

## Example

```python
from equinix_metal.models.spot_market_prices_per_metro_report import SpotMarketPricesPerMetroReport

# TODO update the JSON string below
json = "{}"
# create an instance of SpotMarketPricesPerMetroReport from a JSON string
spot_market_prices_per_metro_report_instance = SpotMarketPricesPerMetroReport.from_json(json)
# print the JSON string representation of the object
print(SpotMarketPricesPerMetroReport.to_json())

# convert the object into a dict
spot_market_prices_per_metro_report_dict = spot_market_prices_per_metro_report_instance.to_dict()
# create an instance of SpotMarketPricesPerMetroReport from a dict
spot_market_prices_per_metro_report_form_dict = spot_market_prices_per_metro_report.from_dict(spot_market_prices_per_metro_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


