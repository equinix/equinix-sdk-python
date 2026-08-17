# PublicPeeringConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Connection type IX_VC | [optional] 
**href** | **str** | URI | [optional] 
**uuid** | **str** | uuid | [optional] 

## Example

```python
from equinix.services.fabricv4.models.public_peering_connection_response import PublicPeeringConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicPeeringConnectionResponse from a JSON string
public_peering_connection_response_instance = PublicPeeringConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(PublicPeeringConnectionResponse.to_json())

# convert the object into a dict
public_peering_connection_response_dict = public_peering_connection_response_instance.to_dict()
# create an instance of PublicPeeringConnectionResponse from a dict
public_peering_connection_response_from_dict = PublicPeeringConnectionResponse.from_dict(public_peering_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


