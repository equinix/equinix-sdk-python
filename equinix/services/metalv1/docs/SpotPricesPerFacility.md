# SpotPricesPerFacility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baremetal_0** | [**SpotPricesPerBaremetal**](SpotPricesPerBaremetal.md) |  | [optional] 
**baremetal_1** | [**SpotPricesPerBaremetal**](SpotPricesPerBaremetal.md) |  | [optional] 
**baremetal_2** | [**SpotPricesPerBaremetal**](SpotPricesPerBaremetal.md) |  | [optional] 
**baremetal_2a** | [**SpotPricesPerBaremetal**](SpotPricesPerBaremetal.md) |  | [optional] 
**baremetal_2a2** | [**SpotPricesPerBaremetal**](SpotPricesPerBaremetal.md) |  | [optional] 
**baremetal_3** | [**SpotPricesPerBaremetal**](SpotPricesPerBaremetal.md) |  | [optional] 
**baremetal_s** | [**SpotPricesPerBaremetal**](SpotPricesPerBaremetal.md) |  | [optional] 
**c2_medium_x86** | [**SpotPricesPerBaremetal**](SpotPricesPerBaremetal.md) |  | [optional] 
**href** | **str** |  | [optional] 
**m2_xlarge_x86** | [**SpotPricesPerBaremetal**](SpotPricesPerBaremetal.md) |  | [optional] 

## Example

```python
from equinix_metal.models.spot_prices_per_facility import SpotPricesPerFacility

# TODO update the JSON string below
json = "{}"
# create an instance of SpotPricesPerFacility from a JSON string
spot_prices_per_facility_instance = SpotPricesPerFacility.from_json(json)
# print the JSON string representation of the object
print(SpotPricesPerFacility.to_json())

# convert the object into a dict
spot_prices_per_facility_dict = spot_prices_per_facility_instance.to_dict()
# create an instance of SpotPricesPerFacility from a dict
spot_prices_per_facility_form_dict = spot_prices_per_facility.from_dict(spot_prices_per_facility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


