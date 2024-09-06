# FacilityList2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facilities** | [**List[Facility]**](Facility.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.facility_list2 import FacilityList2

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityList2 from a JSON string
facility_list2_instance = FacilityList2.from_json(json)
# print the JSON string representation of the object
print(FacilityList2.to_json())

# convert the object into a dict
facility_list2_dict = facility_list2_instance.to_dict()
# create an instance of FacilityList2 from a dict
facility_list2_from_dict = FacilityList2.from_dict(facility_list2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


