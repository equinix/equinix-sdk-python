# PublicPeeringConnectionRequest

Public Peering Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | connection id | [optional] 

## Example

```python
from equinix.services.fabricv4.models.public_peering_connection_request import PublicPeeringConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicPeeringConnectionRequest from a JSON string
public_peering_connection_request_instance = PublicPeeringConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(PublicPeeringConnectionRequest.to_json())

# convert the object into a dict
public_peering_connection_request_dict = public_peering_connection_request_instance.to_dict()
# create an instance of PublicPeeringConnectionRequest from a dict
public_peering_connection_request_from_dict = PublicPeeringConnectionRequest.from_dict(public_peering_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


