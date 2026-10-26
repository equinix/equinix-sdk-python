# CrossConnectASideResponse

A-Side connection details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**demarcation_point** | [**CrossConnectASideDemarcationPoint**](CrossConnectASideDemarcationPoint.md) |  | [optional] 
**location** | [**CrossConnectLocation**](CrossConnectLocation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_a_side_response import CrossConnectASideResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectASideResponse from a JSON string
cross_connect_a_side_response_instance = CrossConnectASideResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectASideResponse.to_json())

# convert the object into a dict
cross_connect_a_side_response_dict = cross_connect_a_side_response_instance.to_dict()
# create an instance of CrossConnectASideResponse from a dict
cross_connect_a_side_response_from_dict = CrossConnectASideResponse.from_dict(cross_connect_a_side_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


