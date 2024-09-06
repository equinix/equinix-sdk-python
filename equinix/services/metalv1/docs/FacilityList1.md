# FacilityList1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facilities** | [**List[Facility]**](Facility.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.facility_list1 import FacilityList1

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityList1 from a JSON string
facility_list1_instance = FacilityList1.from_json(json)
# print the JSON string representation of the object
print(FacilityList1.to_json())

# convert the object into a dict
facility_list1_dict = facility_list1_instance.to_dict()
# create an instance of FacilityList1 from a dict
facility_list1_from_dict = FacilityList1.from_dict(facility_list1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


