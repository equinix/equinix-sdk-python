# CrossConnectASideRequest

A-Side connection details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**demarcation_point** | [**CrossConnectASideRequestDemarcationPoint**](CrossConnectASideRequestDemarcationPoint.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_a_side_request import CrossConnectASideRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectASideRequest from a JSON string
cross_connect_a_side_request_instance = CrossConnectASideRequest.from_json(json)
# print the JSON string representation of the object
print(CrossConnectASideRequest.to_json())

# convert the object into a dict
cross_connect_a_side_request_dict = cross_connect_a_side_request_instance.to_dict()
# create an instance of CrossConnectASideRequest from a dict
cross_connect_a_side_request_from_dict = CrossConnectASideRequest.from_dict(cross_connect_a_side_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


