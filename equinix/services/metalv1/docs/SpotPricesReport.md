# SpotPricesReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ams1** | [**SpotPricesPerFacility**](SpotPricesPerFacility.md) |  | [optional] 
**atl1** | [**SpotPricesPerNewFacility**](SpotPricesPerNewFacility.md) |  | [optional] 
**dfw1** | [**SpotPricesPerNewFacility**](SpotPricesPerNewFacility.md) |  | [optional] 
**ewr1** | [**SpotPricesPerFacility**](SpotPricesPerFacility.md) |  | [optional] 
**fra1** | [**SpotPricesPerNewFacility**](SpotPricesPerNewFacility.md) |  | [optional] 
**href** | **str** |  | [optional] 
**iad1** | [**SpotPricesPerNewFacility**](SpotPricesPerNewFacility.md) |  | [optional] 
**lax1** | [**SpotPricesPerNewFacility**](SpotPricesPerNewFacility.md) |  | [optional] 
**nrt1** | [**SpotPricesPerFacility**](SpotPricesPerFacility.md) |  | [optional] 
**ord1** | [**SpotPricesPerNewFacility**](SpotPricesPerNewFacility.md) |  | [optional] 
**sea1** | [**SpotPricesPerNewFacility**](SpotPricesPerNewFacility.md) |  | [optional] 
**sin1** | [**SpotPricesPerNewFacility**](SpotPricesPerNewFacility.md) |  | [optional] 
**sjc1** | [**SpotPricesPerFacility**](SpotPricesPerFacility.md) |  | [optional] 
**syd1** | [**SpotPricesPerNewFacility**](SpotPricesPerNewFacility.md) |  | [optional] 
**yyz1** | [**SpotPricesPerNewFacility**](SpotPricesPerNewFacility.md) |  | [optional] 

## Example

```python
from equinix_metal.models.spot_prices_report import SpotPricesReport

# TODO update the JSON string below
json = "{}"
# create an instance of SpotPricesReport from a JSON string
spot_prices_report_instance = SpotPricesReport.from_json(json)
# print the JSON string representation of the object
print(SpotPricesReport.to_json())

# convert the object into a dict
spot_prices_report_dict = spot_prices_report_instance.to_dict()
# create an instance of SpotPricesReport from a dict
spot_prices_report_form_dict = spot_prices_report.from_dict(spot_prices_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


