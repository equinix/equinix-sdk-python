# FacilityInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility** | [**FacilityInputFacility**](FacilityInputFacility.md) |  | 
**href** | **str** |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.facility_input import FacilityInput

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityInput from a JSON string
facility_input_instance = FacilityInput.from_json(json)
# print the JSON string representation of the object
print(FacilityInput.to_json())

# convert the object into a dict
facility_input_dict = facility_input_instance.to_dict()
# create an instance of FacilityInput from a dict
facility_input_from_dict = FacilityInput.from_dict(facility_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


