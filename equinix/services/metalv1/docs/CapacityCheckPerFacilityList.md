# CapacityCheckPerFacilityList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**servers** | [**List[CapacityCheckPerFacilityInfo]**](CapacityCheckPerFacilityInfo.md) |  | [optional] 

## Example

```python
from equinix_metal.models.capacity_check_per_facility_list import CapacityCheckPerFacilityList

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityCheckPerFacilityList from a JSON string
capacity_check_per_facility_list_instance = CapacityCheckPerFacilityList.from_json(json)
# print the JSON string representation of the object
print(CapacityCheckPerFacilityList.to_json())

# convert the object into a dict
capacity_check_per_facility_list_dict = capacity_check_per_facility_list_instance.to_dict()
# create an instance of CapacityCheckPerFacilityList from a dict
capacity_check_per_facility_list_form_dict = capacity_check_per_facility_list.from_dict(capacity_check_per_facility_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


