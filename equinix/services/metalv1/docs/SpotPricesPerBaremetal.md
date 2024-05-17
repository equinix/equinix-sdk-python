# SpotPricesPerBaremetal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**price** | **float** |  | [optional] 

## Example

```python
from equinix_metal.models.spot_prices_per_baremetal import SpotPricesPerBaremetal

# TODO update the JSON string below
json = "{}"
# create an instance of SpotPricesPerBaremetal from a JSON string
spot_prices_per_baremetal_instance = SpotPricesPerBaremetal.from_json(json)
# print the JSON string representation of the object
print(SpotPricesPerBaremetal.to_json())

# convert the object into a dict
spot_prices_per_baremetal_dict = spot_prices_per_baremetal_instance.to_dict()
# create an instance of SpotPricesPerBaremetal from a dict
spot_prices_per_baremetal_form_dict = spot_prices_per_baremetal.from_dict(spot_prices_per_baremetal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


