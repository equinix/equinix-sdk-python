# SpotPricesPerNewFacility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baremetal_1e** | [**SpotPricesPerBaremetal**](SpotPricesPerBaremetal.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.spot_prices_per_new_facility import SpotPricesPerNewFacility

# TODO update the JSON string below
json = "{}"
# create an instance of SpotPricesPerNewFacility from a JSON string
spot_prices_per_new_facility_instance = SpotPricesPerNewFacility.from_json(json)
# print the JSON string representation of the object
print(SpotPricesPerNewFacility.to_json())

# convert the object into a dict
spot_prices_per_new_facility_dict = spot_prices_per_new_facility_instance.to_dict()
# create an instance of SpotPricesPerNewFacility from a dict
spot_prices_per_new_facility_form_dict = spot_prices_per_new_facility.from_dict(spot_prices_per_new_facility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


