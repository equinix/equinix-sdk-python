# ServiceProfileLastMilePriceRange

Range details for price or delivery window.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Unit for this range, such as USD or DAYS. | [optional] 
**min** | **float** | Minimum value for the range. | [optional] 
**max** | **float** | Maximum value for the range. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_last_mile_price_range import ServiceProfileLastMilePriceRange

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileLastMilePriceRange from a JSON string
service_profile_last_mile_price_range_instance = ServiceProfileLastMilePriceRange.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileLastMilePriceRange.to_json())

# convert the object into a dict
service_profile_last_mile_price_range_dict = service_profile_last_mile_price_range_instance.to_dict()
# create an instance of ServiceProfileLastMilePriceRange from a dict
service_profile_last_mile_price_range_from_dict = ServiceProfileLastMilePriceRange.from_dict(service_profile_last_mile_price_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


