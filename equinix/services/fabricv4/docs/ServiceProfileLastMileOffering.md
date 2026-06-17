# ServiceProfileLastMileOffering

Last-mile offering details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth** | **int** | Offered bandwidth in Mbps. | [optional] 
**price** | [**ServiceProfileLastMilePriceRange**](ServiceProfileLastMilePriceRange.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_last_mile_offering import ServiceProfileLastMileOffering

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileLastMileOffering from a JSON string
service_profile_last_mile_offering_instance = ServiceProfileLastMileOffering.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileLastMileOffering.to_json())

# convert the object into a dict
service_profile_last_mile_offering_dict = service_profile_last_mile_offering_instance.to_dict()
# create an instance of ServiceProfileLastMileOffering from a dict
service_profile_last_mile_offering_from_dict = ServiceProfileLastMileOffering.from_dict(service_profile_last_mile_offering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


