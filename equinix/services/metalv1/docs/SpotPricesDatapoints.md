# SpotPricesDatapoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datapoints** | **List[List[float]]** |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.spot_prices_datapoints import SpotPricesDatapoints

# TODO update the JSON string below
json = "{}"
# create an instance of SpotPricesDatapoints from a JSON string
spot_prices_datapoints_instance = SpotPricesDatapoints.from_json(json)
# print the JSON string representation of the object
print(SpotPricesDatapoints.to_json())

# convert the object into a dict
spot_prices_datapoints_dict = spot_prices_datapoints_instance.to_dict()
# create an instance of SpotPricesDatapoints from a dict
spot_prices_datapoints_form_dict = spot_prices_datapoints.from_dict(spot_prices_datapoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


