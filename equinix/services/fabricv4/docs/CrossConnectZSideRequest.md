# CrossConnectZSideRequest

Z-Side connection details. Provide the demarcationPoint for a patch panel to patch panel Cross Connect, or location when connecting to a BMMR. loa is mandatory for a Cross Connect with LOA and when bmmrType is EQUINIX - provide either loa.uuid or loa.digitalLoaId. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**demarcation_point** | [**CrossConnectZSideRequestDemarcationPoint**](CrossConnectZSideRequestDemarcationPoint.md) | Required for a patch panel to patch panel Cross Connect. | [optional] 
**location** | [**CrossConnectLocation**](CrossConnectLocation.md) | Required when connecting to a BMMR. | [optional] 
**loa** | [**CrossConnectLoaRef**](CrossConnectLoaRef.md) | Required for a Cross Connect with LOA and when bmmrType is EQUINIX. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_z_side_request import CrossConnectZSideRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectZSideRequest from a JSON string
cross_connect_z_side_request_instance = CrossConnectZSideRequest.from_json(json)
# print the JSON string representation of the object
print(CrossConnectZSideRequest.to_json())

# convert the object into a dict
cross_connect_z_side_request_dict = cross_connect_z_side_request_instance.to_dict()
# create an instance of CrossConnectZSideRequest from a dict
cross_connect_z_side_request_from_dict = CrossConnectZSideRequest.from_dict(cross_connect_z_side_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


