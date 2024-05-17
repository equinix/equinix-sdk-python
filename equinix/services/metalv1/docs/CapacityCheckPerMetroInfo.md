# CapacityCheckPerMetroInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Returns true if there is enough capacity in the metro to fulfill the quantity set. Returns false if there is not enough. | [optional] 
**href** | **str** |  | [optional] 
**metro** | **str** | The metro ID or code sent to check capacity. | [optional] 
**plan** | **str** | The plan ID or slug sent to check capacity. | [optional] 
**quantity** | **str** | The number of servers sent to check capacity. | [optional] 

## Example

```python
from equinix_metal.models.capacity_check_per_metro_info import CapacityCheckPerMetroInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityCheckPerMetroInfo from a JSON string
capacity_check_per_metro_info_instance = CapacityCheckPerMetroInfo.from_json(json)
# print the JSON string representation of the object
print(CapacityCheckPerMetroInfo.to_json())

# convert the object into a dict
capacity_check_per_metro_info_dict = capacity_check_per_metro_info_instance.to_dict()
# create an instance of CapacityCheckPerMetroInfo from a dict
capacity_check_per_metro_info_form_dict = capacity_check_per_metro_info.from_dict(capacity_check_per_metro_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


