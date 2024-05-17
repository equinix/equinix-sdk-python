# FacilityInputFacility

The datacenter where the device should be created.  Either metro or facility must be provided.  The API will accept either a single facility `{ \"facility\": \"f1\" }`, or it can be instructed to create the device in the best available datacenter `{ \"facility\": \"any\" }`.  Additionally it is possible to set a prioritized location selection. For example `{ \"facility\": [\"f3\", \"f2\", \"any\"] }` can be used to prioritize `f3` and then `f2` before accepting `any` facility. If none of the facilities provided have availability for the requested device the request will fail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from equinix_metal.models.facility_input_facility import FacilityInputFacility

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityInputFacility from a JSON string
facility_input_facility_instance = FacilityInputFacility.from_json(json)
# print the JSON string representation of the object
print(FacilityInputFacility.to_json())

# convert the object into a dict
facility_input_facility_dict = facility_input_facility_instance.to_dict()
# create an instance of FacilityInputFacility from a dict
facility_input_facility_form_dict = facility_input_facility.from_dict(facility_input_facility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


