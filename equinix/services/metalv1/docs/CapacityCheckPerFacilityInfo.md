# CapacityCheckPerFacilityInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** |  | [optional] 
**facility** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**plan** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.capacity_check_per_facility_info import CapacityCheckPerFacilityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityCheckPerFacilityInfo from a JSON string
capacity_check_per_facility_info_instance = CapacityCheckPerFacilityInfo.from_json(json)
# print the JSON string representation of the object
print(CapacityCheckPerFacilityInfo.to_json())

# convert the object into a dict
capacity_check_per_facility_info_dict = capacity_check_per_facility_info_instance.to_dict()
# create an instance of CapacityCheckPerFacilityInfo from a dict
capacity_check_per_facility_info_form_dict = capacity_check_per_facility_info.from_dict(capacity_check_per_facility_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


