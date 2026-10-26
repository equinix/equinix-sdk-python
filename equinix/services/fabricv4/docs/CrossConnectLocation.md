# CrossConnectLocation

Cross Connect Location details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ibx_code** | **str** | IBX Code. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_location import CrossConnectLocation

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectLocation from a JSON string
cross_connect_location_instance = CrossConnectLocation.from_json(json)
# print the JSON string representation of the object
print(CrossConnectLocation.to_json())

# convert the object into a dict
cross_connect_location_dict = cross_connect_location_instance.to_dict()
# create an instance of CrossConnectLocation from a dict
cross_connect_location_from_dict = CrossConnectLocation.from_dict(cross_connect_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


