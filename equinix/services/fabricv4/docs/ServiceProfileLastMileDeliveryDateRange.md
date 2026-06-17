# ServiceProfileLastMileDeliveryDateRange

Range details for delivery window.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Unit for this range is DAYS. | [optional] 
**min** | **int** | Minimum value for the range. | [optional] 
**max** | **int** | Maximum value for the range. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_last_mile_delivery_date_range import ServiceProfileLastMileDeliveryDateRange

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileLastMileDeliveryDateRange from a JSON string
service_profile_last_mile_delivery_date_range_instance = ServiceProfileLastMileDeliveryDateRange.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileLastMileDeliveryDateRange.to_json())

# convert the object into a dict
service_profile_last_mile_delivery_date_range_dict = service_profile_last_mile_delivery_date_range_instance.to_dict()
# create an instance of ServiceProfileLastMileDeliveryDateRange from a dict
service_profile_last_mile_delivery_date_range_from_dict = ServiceProfileLastMileDeliveryDateRange.from_dict(service_profile_last_mile_delivery_date_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


