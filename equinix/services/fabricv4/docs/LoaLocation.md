# LoaLocation

Eligible location where LOA can be issued.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ibx_code** | **str** | IBX Code | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_location import LoaLocation

# TODO update the JSON string below
json = "{}"
# create an instance of LoaLocation from a JSON string
loa_location_instance = LoaLocation.from_json(json)
# print the JSON string representation of the object
print(LoaLocation.to_json())

# convert the object into a dict
loa_location_dict = loa_location_instance.to_dict()
# create an instance of LoaLocation from a dict
loa_location_from_dict = LoaLocation.from_dict(loa_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


