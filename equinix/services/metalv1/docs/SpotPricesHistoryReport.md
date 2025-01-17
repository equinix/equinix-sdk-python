# SpotPricesHistoryReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**prices_history** | [**SpotPricesDatapoints**](SpotPricesDatapoints.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.spot_prices_history_report import SpotPricesHistoryReport

# TODO update the JSON string below
json = "{}"
# create an instance of SpotPricesHistoryReport from a JSON string
spot_prices_history_report_instance = SpotPricesHistoryReport.from_json(json)
# print the JSON string representation of the object
print(SpotPricesHistoryReport.to_json())

# convert the object into a dict
spot_prices_history_report_dict = spot_prices_history_report_instance.to_dict()
# create an instance of SpotPricesHistoryReport from a dict
spot_prices_history_report_from_dict = SpotPricesHistoryReport.from_dict(spot_prices_history_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


