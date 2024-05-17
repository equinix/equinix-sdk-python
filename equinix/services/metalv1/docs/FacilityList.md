# FacilityList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facilities** | [**List[Facility]**](Facility.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.facility_list import FacilityList

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityList from a JSON string
facility_list_instance = FacilityList.from_json(json)
# print the JSON string representation of the object
print(FacilityList.to_json())

# convert the object into a dict
facility_list_dict = facility_list_instance.to_dict()
# create an instance of FacilityList from a dict
facility_list_form_dict = facility_list.from_dict(facility_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


